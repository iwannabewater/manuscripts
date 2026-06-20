---
source_url: https://arxiv.org/html/2606.14249
fetched_for: learn/canonical-article
source_check_date: 2026-06-20
---

[fetch] tier=local status=ok extractor=stdlib hint="install readability-lxml + html2text for cleaner output"
# HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry

> Source: https://arxiv.org/html/2606.14249

Back to arXiv

License: CC BY 4.0

arXiv:2606.14249v1 [cs.AI] 12 Jun 2026

\contribution

See Contributions and Acknowledgments section for a full author list.

HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry

Darwin Agent Team

Abstract

AI agent performance depends critically on the runtime harness, comprising the prompts, tools, memory, and control flow that mediate how a model observes, reasons, and acts. Yet today’s harnesses remain largely hand-crafted and static: each new model or task still demands bespoke scaffolding, and the rich traces produced during execution are rarely distilled back into systematic improvement. We introduce HarnessX, a foundry for composable, adaptive, and evolvable agent harnesses. HarnessX assembles typed harness primitives via a substitution algebra, adapts them through AEGIS, a trace-driven multi-agent evolution engine grounded in an operational mirror between symbolic adaptation and reinforcement learning, and closes the harness–model loop by turning trajectories into both harness updates and model training signal. Across five benchmarks (ALFWorld, GAIA, WebShop, τ3\tau^{3}-Bench, and SWE-bench Verified), HarnessX yields an average gain of +14.5% (up to +44.0%), with gains largest where baselines are lowest.
These results suggest that agent progress need not come from model scaling alone: composing and evolving runtime interfaces from execution feedback is an actionable and complementary lever.
The complete codebase will be open-sourced in a future release.

Figure 1: HarnessX overview.

1 Introduction

The capacity of modern agents depends not only on the underlying model [deepseekai2026deepseekv4, glm5team2026glm5vibecodingagentic, yang2025qwen3, team2023gemini], but on the mediation imposed by the surrounding harness [lu2026openclaw, liagent, claudecode]. This harness converts raw model outputs into structured agent behaviors by determining how tasks are represented, how external services are accessed, and how intermediate decisions are communicated during execution. As agents tackle longer-horizon tasks in richer environments, harness design becomes integral to agent development.

Despite this importance, harness development remains far from a mature engineering discipline. First, harnesses are hand-engineered and static: any change in model version, tooling, or problem domain requires bespoke modification, with no mechanism for experience-driven improvement. Second, harnesses are architecturally entangled: they typically combine prompt templates, tool wrappers, retry policies, and memory in the same codepaths, so changes to one component silently break others, and reuse across domains reduces to copying rather than composition. Third, harness engineering and model training operate independently: trajectory data collected while improving the harness is discarded rather than incorporated into model training, and model improvements do not translate into harness improvements.

We address these gaps by treating the harness as a first-class object that can be composed, adapted, and evolved alongside the model. HarnessX embodies this principle as a unified harness foundry. It begins with a modular foundation: harness primitives spanning context, tools [feng2025retool], skills, control, and memory are described via typed interfaces and composed via a substitution algebra. This separates concerns that existing systems typically conflate. On top of this substrate, we introduce AEGIS, an observability-driven and auditable harness adaptation engine. Framing harness adaptation not as ad-hoc editing but as a learning problem over symbolic artifacts (prompts [zhou2025proposer], tools, memory, and control policies) reveals that standard RL pathologies (reward hacking, catastrophic forgetting [kirkpatrick2017overcoming], under-exploration [ladosz2022exploration]) become concrete design risks. To address these risks, AEGIS combines full trace observability with a four-stage pipeline (Digester, Planner, Evolver, and Critic) that compresses traces, plans adaptations, generates candidates, and assesses changes. Finally, we close the loop between harness adaptation and model training via harness-model co-evolution. Traces produced during harness adaptation serve as reinforcement-learning signal for model training, so that model improvements feed back into subsequent harness evolution.

We empirically validate HarnessX across five benchmarks (GAIA, ALFWorld, WebShop, τ3\tau^{3}-Bench, SWE-bench Verified), three task-agent families (Claude Sonnet 4.6, GPT-5.4, Qwen3.5-9B), and up to 15 evolution rounds. Harness evolution yields an average absolute gain of +14.5% across 15 model–benchmark configurations, with individual gains ranging from 0.0% to +44.0% among improving configurations (14 of 15), from +1.1% (τ3\tau^{3}-Bench, near-ceiling baseline) to +44.0% (ALFWorld, weakest agent). Gains exhibit an inverse-scaling pattern: on ALFWorld and GAIA, the weakest task agent benefits most (+44.0% for Qwen3.5-9B vs. +11.2% for Sonnet 4.6 on ALFWorld), suggesting that evolved harnesses address behavioral gaps that weaker models cannot self-correct. On heterogeneous task sets (GAIA), single-harness evolution stagnates; a variant-isolation ablation restores stable improvement (+13.6%, non-degrading over 15 rounds).

In summary, our contributions are four-fold:

•

Harness Composition (Section 3). We formalize the harness as a first-class, typed object composed of processors attached to lifecycle hooks. A nine-dimensional taxonomy spans the full behavioral space, and a substitution algebra enables per-task configuration with type-safe insertion and removal. This compositional structure makes the intended scope of each behavioral change explicit—a precondition for the variant isolation that stabilizes evolution.

•

Harness Adaptation (Section 4). We introduce AEGIS, a trace-driven, multi-agent harness evolution engine. An operational mirror maps harness adaptation onto standard RL constructs, converting familiar RL pathologies (reward hacking, catastrophic forgetting, under-exploration) into concrete design risks addressed by a four-stage pipeline (Digester, Planner, Evolver, Critic) with deterministic gating. An optional variant-isolation strategy prevents cross-task interference on heterogeneous benchmarks.

•

Harness-Model Co-Evolution (Section 5). We close the optimization loop by interleaving harness evolution with model reinforcement learning over a shared replay buffer. Cross-harness GRPO enables the model to internalize strategies from successive harness versions, breaking the scaffolding ceiling that limits harness-only adaptation and the training-signal ceiling that limits model-only RL.

•

Empirical Validation (Section 6). Across five benchmarks, three task-agent families, and up to 15 evolution rounds, HarnessX yields an average gain of +14.5% (up to +44.0%), with gains largest where baselines are lowest. A variant-isolation ablation resolves stagnation on heterogeneous task sets, and co-evolution yields an additional +4.7% over harness-only evolution (Section 6.5).

2 Related Work

2.1 Harness Engineering

Existing agent infrastructure occupies a spectrum of increasingly opinionated harness abstractions. At the primitive layer, libraries such as LangChain [langchain], LlamaIndex [Liu_LlamaIndex_2022], and Smolagents [smolagents] provide typed building blocks for prompts, tools, retrieval, and memory. These primitives can be tested in isolation but do not support harness-level composition: two harnesses built from identical primitives may still differ in structure.

The next level of abstraction orchestrates these primitives into reusable patterns. LangGraph [langgraph] models the behavior of an agent with a stateful graph; AutoGen [wu2024autogen] models multi-agent interaction as structured conversation; CrewAI [moura2025crewai] assigns role-based identities to agents; and Letta [packer2023memgpt] couples autonomous loops with persistent memory. Although these frameworks make harness writing easier, they impose a particular control loop, so combining patterns, replacing components, and porting enhancements across tasks mostly remain manual.

Lastly, there are productized, domain-specific harnesses such as Claude Code [claudecode], Cursor [cursor], Manus [shen2025mind], and DeerFlow [deerflow]. These systems demonstrate the impact of harness design but remain architecturally static, evolving only through manual iteration.

Two structural gaps persist across all three layers. First, no layer exposes the harness as a substitutable entity composed of typed elements, so building a per-task harness always involves rewriting. Second, no mechanism exists for in-loop improvement: once defined, a harness evolves only through human iteration between releases.

Concurrently, Claude Code introduced Dynamic Workflows [anthropic2026dynamicworkflows], enabling the model to generate task-specific harness scripts at runtime. While this represents a step toward adaptive harnesses, it operates within a single session without persistent trace-based optimization, cross-session evolution, or harness–model co-training. HarnessX addresses both gaps by treating harness adaptation as a multi-round, trace-driven learning problem with typed composition for variant isolation, structured observability for pathology detection, and a shared replay buffer that closes the loop between harness evolution and model training.

2.2 Self-Evolving Agents

Research on self-evolving agents investigates how an agent system can improve without retraining the underlying foundation model. Early work focused on the single most easily editable aspect: the prompt. Approaches like APE [zhou2022large], OPRO [yang2024large], EvoPrompt [guo2024connecting], Promptbreeder [fernando2024promptbreeder] treat instruction formulation as a black-box optimization problem, while ProTeGi [pryzant2023automatic] and TextGrad [yuksekgonul2024textgrad] introduce gradient-inspired textual feedback to make the optimization process explicit. DSPy [khattab2023dspy] and MIPRO [opsahl2024optimizing] extend this approach by compiling a declarative LM program, whose prompts are optimized against labeled data. These approaches establish instructions as a learnable component, but harness-level features (tools, memory, control flow) remain outside the optimization scope.

Another line of work improves agents by accumulating and reusing prior execution experience in memory: Memento [zhou2025memento] improves agents through case-based memory without fine-tuning the model, while MIA [qiao2026memory] unifies non-parametric and parametric memory within a single Manager-Planner-Executor framework: a non-parametric store of compressed trajectories and a parametric planner that evolves on the fly at test time, coupled by a bidirectional loop that continually converts experience between the two, demonstrating superiority across eleven benchmarks.

Subsequent works extend optimization to agent workflows. GPTSwarm [zhuge2024gptswarm], ADAS [hu2025automated], AFlow [zhang2025aflow], A2Flow [zhao2026a2flow], AgentSwift [li2026agentswift], ResMAS [zhou2026resmas], and EvoAgentX [wang2025evoagentx] search over collaboration strategies, agent ordering, and aggregation mechanisms. These works demonstrate that workflow structure is learnable and yields larger gains than prompt-only optimization. However, component-level artifacts (tool implementations, memory policies, node-internal prompts) remain static: the optimization scope covers inter-component relations but does not encompass the full harness.

A final group treats harness evolution explicitly. SICA [robeyns2025self] optimizes a SWE-bench agent’s source code directly, while Darwin Gödel Machine [lange2025darwin] proposes open-ended optimization over a database of agent variants. HyperAgents [zhang2026hyperagents] makes the optimization process itself adaptable; Meta-Harness [lee2026meta] improves sampling efficiency via a file-system-based interface. AHE [lin2026agentic] and Life-Harness [xu2026adapting] emphasize observability, explainability, and source-code rewriting. Collectively, these works establish the harness as an evolutionary target and demonstrate that observability is essential for stable self-improvement. However, their designs lack a unifying theoretical framework that connects observed failure modes to principled defenses.

The heuristic-learning theory [weng2026learning_beyond_gradients] partially addresses this gap by mapping RL concepts to symbolic self-optimization updates. In this framework, observable traces correspond to proper credit assignment, falsifiable change manifests correspond to reward shaping, and proposal-critique cycles provide structured exploration. HarnessX instantiates this paradigm, formalizing the correspondence as the operational mirror between RL and symbolic harness evolution (Section 4.1).

3 Harness Composition

The gap identified in Section 2.1 is the absence of an infrastructure layer that exposes the harness as a typed, substitutable entity. Primitive libraries leave composition to application code, orchestrators expose a fixed set of patterns, and product harnesses are opaque end-to-end. Without a compositional substrate, every behavioral change or cross-team handoff requires re-implementation. HarnessX addresses this via a unified design principle: the harness is a first-class value, the processor is a typed atomic component, and composition proceeds via processor insertion at typed hook points. We formalize the harness (Section 3.1), its building block, the processor (Section 3.2), and the nine-dimensional processor taxonomy (Section 3.3). Definitions are intentionally concise: their role is to establish the vocabulary and expose the edit surface on which harness evolution (Section 4) operates.

Hook
Event type
Permitted modifications

task_start
TaskStartEvent
system prompt

step_start
StepStartEvent
structural history edits

before_model
BeforeModelEvent
last user content; one user-message append

after_model
ModelResponseEvent
response content, tool calls

before_tool
ToolCallEvent
tool input, approval flag

after_tool
ToolResultEvent
tool result

step_end
StepEndEvent
read-only

task_end
TaskEndEvent
read-only

Table 1: Hook points and their permitted modifications.

3.1 The Harness as a First-Class Object

A harness in HarnessX is the pair ℋ=(ℳ,𝒞)\mathcal{H}=(\mathcal{M},\mathcal{C}), where ℳ\mathcal{M} is a model configuration and 𝒞\mathcal{C} is a harness configuration. The two address disjoint concerns: ℳ\mathcal{M} records which model serves which role (main, judge, evaluator) and the fallback policy for each role; 𝒞\mathcal{C} records how the agent behaves independently of model identity. They combine into an executable agent via agent = model_config.agentic(harness_config): an agent in HarnessX is a processor pipeline bound to a model, both independently substitutable.

The harness configuration itself decomposes as 𝒞=(𝐏,𝐒)\mathcal{C}=(\mathbf{P},\mathbf{S}). 𝐏:ℋ​𝑜𝑜𝑘→List​[𝑃𝑟𝑜𝑐𝑒𝑠𝑠𝑜𝑟]\mathbf{P}:\mathcal{H}\!\mathit{ook}\to\mathrm{List}[\mathit{Processor}] is a hook-indexed list of processors, where ℋ​𝑜𝑜𝑘\mathcal{H}\!\mathit{ook} is the eight-element set of lifecycle events in Table 1. 𝐒\mathbf{S} is a fixed set of orthogonal slot resources: tool registry, tracer, workspace, sandbox provider, and plugin list. Slots are singletons, shared across all processors in a configuration; processor state is instance-private. 𝐏\mathbf{P} implements all per-step behavior; 𝐒\mathbf{S} houses the shared infrastructure that processors depend on but do not own.

We call 𝒞\mathcal{C} a first-class object because it is independently serializable, comparable, hashable, and substitutable. Two agents sharing 𝒞\mathcal{C} but differing in ℳ\mathcal{M} execute the same processor pipeline, with behavior differing only in model responses; two agents sharing ℳ\mathcal{M} but differing in 𝒞\mathcal{C} are behaviorally distinct. This reification is the precondition for programmatic evolution (Section 4).

3.2 The Processor Abstraction

Every per-step behavior in HarnessX is implemented as a processor, an object satisfying the protocol async def process(self, event: Event) -> AsyncIterator[Event]. A processor consumes one event and yields zero or more, producing exactly one of five outcomes: pass-through (yield unchanged), transform (yield modified), split (yield multiple same-type events, processed independently downstream), intercept (yield nothing, blocking propagation), or interrupt (raise an exception, which halts the loop). This restricted interface enables compositionality: every processor at a given hook consumes and yields the same event type, so processors compose by sequential application and can be inserted or removed without affecting type correctness of the surrounding pipeline.

As listed in Table 1, processors attach to one of eight hook points emitted by the run loop. The run loop validates hook contracts after each invocation: a violation (e.g., modifying a read-only field) raises an exception immediately rather than silently propagating corrupted state. Each processor carries three class-level metadata fields that govern composition: _singleton_group names a mutual-exclusion class, ensuring at most one processor per group; _order is an ordering hint within a hook (with constants PRE, NORMAL, POST); and _after is a list of soft dependencies on other singleton groups.

This design makes harness evolution a first-class operation: AEGIS can insert a new processor at a specific hook, replace an existing one by matching its singleton group, or remove a processor entirely—all without touching other processors at the same or different hooks. Because the type contract (input event type == output event type) is enforced per-hook, any such substitution preserves the well-typedness of the overall pipeline. The metadata fields further constrain composition: _singleton_group prevents conflicting duplicates, and _order ensures that newly inserted processors interact predictably with existing ones. These guarantees are the mechanism by which variant isolation (Section 4.5) operates—each variant differs only in which processors occupy which hooks, and the type system ensures that no variant can silently violate the pipeline contract during evolution.

3.3 The Nine-Dimensional Taxonomy

We organize the behavioral space along nine dimensions: model selection (D1) decides which model serves which role; context assembly (D2) determines what is presented to the model at each step; memory management (D3) governs what carries across steps and sessions; tool ecosystem (D4) controls which tools the agent can invoke; execution environment (D5) determines where tool-induced side-effects materialize; evaluation and reward (D6) specifies how outcomes are judged; control and safety (D7) enforces rules that keep the agent from looping, overspending, or drifting from intent; observability (D8) records each event, model call, and tool invocation; and the training bridge (D9) converts execution trajectories into reinforcement-learning records. Figure 2 illustrates the full taxonomy along with representative processors and the hooks at which they typically attach in a standard configuration.

In practice, AEGIS edits span all nine dimensions during evolution: D2 (context assembly) and D4 (tool ecosystem) are the most frequent edit targets (Section 6.2), while D8 (observability) provides the trace substrate on which AEGIS itself reasons, and D9 (training bridge) supplies trajectory records for co-evolution (Section 5), closing the optimization loop.

RL concept
Symbolic-space dual
AEGIS realization

Policy π\pi

Harness-update procedure πevo\pi_{\mathrm{evo}}

Four-stage pipeline (Section 4.3)

State sts_{t}

(ℋt,𝒯t)(\mathcal{H}_{t},\mathcal{T}_{t})
Harness configuration + trace store

Action ata_{t}

Typed harness edit
Builder operation + change manifest

Feedback

Trace τ\tau + verifier score rr

Observability layer

Update
ℋt+1←U​(ℋ~t,𝒯t,rt)\mathcal{H}_{t+1}\leftarrow U(\widetilde{\mathcal{H}}_{t},\mathcal{T}_{t},r_{t})
Deterministic acceptance gate

Table 2: Operational mirror: RL concepts and their symbolic-space duals in AEGIS.

4 Harness Adaptation

The composition layer (Section 3) provides a typed, substitutable harness; as illustrated in Figure 2, AEGIS is the system that evolves it. The key insight is that harness evolution maps structurally onto reinforcement learning in a symbolic space: harness configurations are states, typed edits are actions, and execution traces plus verifier scores constitute feedback. This mapping is predictive: it identifies three failure modes analogous to known RL pathologies (reward hacking, catastrophic forgetting, under-exploration) that motivate AEGIS’s architectural defenses and are empirically confirmed in Section 6.6.

We formalize the correspondence (Section 4.1), analyze the pathologies it predicts (Section 4.2), derive the four-stage pipeline as a defense architecture (Section 4.3), present the adaptation loop (Section 4.4), and introduce variant isolation for stable multi-variant evolution (Section 4.5).

Figure 2: The AEGIS evolution loop. A single meta-agent ℳ\mathcal{M} drives all four stages (Digester, Planner, Evolver, Critic), selectively invoking each based on whether sufficient signal exists to continue. A deterministic gate ships or rejects the candidate edit.

4.1 The Operational Mirror

We formalize harness evolution as an MDP over symbolic artifacts. Table 2 summarizes the mapping; we first state three definitions that ground the correspondence.

Definition 1 (Harness Configuration).

A harness configuration is a tuple ℋ=(c1,c2,…,c9)\mathcal{H}=(c_{1},c_{2},\ldots,c_{9}), where each ci∈𝒞ic_{i}\in\mathcal{C}_{i} instantiates one of the nine behavioral dimensions (Section 3.3): model selection (c1c_{1}), context assembly (c2c_{2}), memory management (c3c_{3}), tool ecosystem (c4c_{4}), execution environment (c5c_{5}), evaluation and reward (c6c_{6}), control and safety (c7c_{7}), observability (c8c_{8}), and training bridge (c9c_{9}). Each 𝒞i\mathcal{C}_{i} is the set of valid processor configurations for dimension ii, constrained by hook-type contracts and singleton-group exclusion (Section 3.2).

Definition 2 (Harness Edit).

A harness edit is a function e:ℋ→ℋe:\mathcal{H}\to\mathcal{H} that modifies one or more dimensions while preserving type contracts. The action space ℰ\mathcal{E} is discrete but open-ended: each edit is a code-level artifact (new processor source, modified prompt template, reconfigured tool registry, or control-flow rewrite) generated by the meta-agent LLM, not selected from a pre-enumerated set. Combinatorial explosion is managed not by exhaustive search but by the LLM’s generative capacity—the Planner proposes edits from trace-grounded hypotheses—and by type constraints that prune invalid compositions at generation time.

Definition 3 (Operational Mirror).

The operational mirror is the tuple (ℋ,ℰ,ℛ,𝒯)(\mathcal{H},\mathcal{E},\mathcal{R},\mathcal{T}), where ℋ\mathcal{H} is the harness-configuration space (states), ℰ\mathcal{E} is the code-level edit space (actions), ℛ:ℋ×ℰ→ℝ\mathcal{R}:\mathcal{H}\times\mathcal{E}\to\mathbb{R} maps a configuration–edit pair to a scalar reward (verifier scores aggregated over an adaptation batch), and 𝒯\mathcal{T} is the trace store that provides structured feedback beyond the scalar signal. This tuple forms an MDP at the harness level: harness configurations are states, typed edits are actions, execution traces plus verifier scores constitute feedback, and a deterministic acceptance gate governs state transitions.

MDP instantiation.

Let ℋt\mathcal{H}_{t} denote the harness configuration at iteration tt (the model ℳ\mathcal{M} is fixed throughout evolution), and let
𝒯t\mathcal{T}_{t} denote the trace store accumulated from all previous executions. We
define the symbolic state as st=(ℋt,𝒯t)s_{t}=(\mathcal{H}_{t},\mathcal{T}_{t}). A harness-update
policy πevo\pi_{\mathrm{evo}} selects an action
at∼πevo(⋅∣st)a_{t}\sim\pi_{\mathrm{evo}}(\cdot\mid s_{t}), where at∈ℰa_{t}\in\mathcal{E} is a code-level edit drawn
from the builder algebra. Applying this edit yields a candidate harness
ℋ~t=at​(ℋt)\widetilde{\mathcal{H}}_{t}=a_{t}(\mathcal{H}_{t}). Running the candidate on an adaptation batch (with the fixed model ℳ\mathcal{M}) produces new traces Δ​𝒯t\Delta\mathcal{T}_{t} and per-task verifier scores rtr_{t}. A deterministic acceptance operator
U​(ℋ~t,𝒯t,rt)U(\widetilde{\mathcal{H}}_{t},\mathcal{T}_{t},r_{t}) then either commits the candidate
(ℋt+1=ℋ~t\mathcal{H}_{t+1}=\widetilde{\mathcal{H}}_{t}) or rejects it
(ℋt+1=ℋt\mathcal{H}_{t+1}=\mathcal{H}_{t}), enforcing the seesaw constraint: the candidate must not regress any previously solved task recorded in 𝒯t\mathcal{T}_{t}. In both cases, the trace store grows:
𝒯t+1=𝒯t∪Δ​𝒯t\mathcal{T}_{t+1}=\mathcal{T}_{t}\cup\Delta\mathcal{T}_{t}.

This MDP operates at the harness level: within a single task, ℋt\mathcal{H}_{t} (together with the fixed ℳ\mathcal{M}) determines the agent’s behavior; across iterations, the harness-update policy πevo\pi_{\mathrm{evo}} modifies the harness. AEGIS realizes πevo\pi_{\mathrm{evo}} as a four-stage pipeline (Digester, Planner, Evolver, Critic) that maps sts_{t} to candidate edits through trace compression, adaptation planning, edit generation, and candidate assessment.

4.2 Pathologies in Symbolic Space

The mirror is not merely an analogy; it converts reinforcement-learning concepts into design requirements. We refer to three well-documented failure modes in RL, namely reward hacking [guo2025deepseek], catastrophic forgetting [kirkpatrick2017overcoming], and under-exploration [ladosz2022exploration], collectively as RL pathologies. Once harness adaptation is cast as an MDP over symbolic artifacts, these pathologies reappear in amplified form, shaped by two properties of the symbolic setting: (1) a language-model evolver can construct structured exploits that numerical parameter perturbations cannot express, and (2) edits to shared components propagate non-locally through the harness. Each pathology below motivates a corresponding architectural defense in Section 4.3.

Reward hacking.

In standard RL, reward hacking [guo2025deepseek] exploits loopholes in the reward signal without genuine task completion. Symbolic harness evolution amplifies this risk because the evolver can target the verification protocol directly: embedding benchmark answers into prompts, exploiting format regularities in the verifier, or introducing a processor that rewrites outputs to match verifier expectations.

Catastrophic forgetting.

Catastrophic forgetting [kirkpatrick2017overcoming] occurs when improving performance on one region of the task distribution harms another. In symbolic harness evolution, an edit that repairs failure pattern AA can silently regress pattern BB, because effects propagate through shared context, tools, memory policies, and control rules. Without explicit regression checking, an evolver conditioned only on failing-task traces cannot distinguish local gain from global regression.

Under-exploration.

Under-exploration [ladosz2022exploration] manifests as a bias toward low-risk local edits: prompt rephrasing, tool-description tuning, or minor control-flow tweaks. These edits are cheap to generate and frequently pass gating without regressing solved tasks, biasing subsequent Planner hypotheses toward the same edit neighborhood. Structural changes (decomposing one agent into several, replacing the control strategy, or adopting a new memory architecture) require deliberate hypothesis formation and rarely emerge from trace-conditional local repair. Without a mechanism to propose edits beyond the immediate failure neighborhood, the system plateaus once local edits are exhausted.

Summary.

Symbolic harness evolution inherits the structural risks of RL (reward hacking, catastrophic forgetting, and under-exploration), and AEGIS addresses each with a dedicated mechanism: the Critic (reward hacking), the deterministic gating layer (catastrophic forgetting), and the Planner (under-exploration).

Input: Initial harness ℋ0\mathcal{H}_{0}, meta-agent ℳ\mathcal{M}, budget TT, patience PP, threshold α\alpha

Output: Evolved harness ℋt+1\mathcal{H}_{t+1}, trace store 𝒯t+1\mathcal{T}_{t+1}

1
𝒯0←∅\mathcal{T}_{0}\leftarrow\emptyset;

2 𝑖𝑑𝑙𝑒←0\mathit{idle}\leftarrow 0;

3
for t=0,1,…,T−1t=0,1,\ldots,T{-}1 do

4
Sample batch BtB_{t};

5    run ℋt\mathcal{H}_{t} on BtB_{t} to get traces Δ​𝒯t\Delta\mathcal{T}_{t};

6    𝒯t+1←𝒯t∪Δ​𝒯t\mathcal{T}_{t+1}\leftarrow\mathcal{T}_{t}\cup\Delta\mathcal{T}_{t};

/* Digester (selective)  */

7
(𝑒𝑣𝑖𝑑𝑒𝑛𝑐𝑒t,at)←ℳ.Digester​(Δ​𝒯t,𝒯t)(\mathit{evidence}_{t},\;a_{t})\leftarrow\mathcal{M}.\textsc{Digester}(\Delta\mathcal{T}_{t},\;\mathcal{T}_{t});
