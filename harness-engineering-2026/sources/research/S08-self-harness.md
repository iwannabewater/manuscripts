---
source_url: https://arxiv.org/html/2606.09498
fetched_for: learn/canonical-article
source_check_date: 2026-06-20
---

[fetch] tier=local status=ok extractor=stdlib hint="install readability-lxml + html2text for cleaner output"
# Self-Harness: Harnesses That Improve Themselves

> Source: https://arxiv.org/html/2606.09498

Back to arXiv

License: CC BY 4.0

arXiv:2606.09498v1 [cs.CL] 08 Jun 2026

Self-Harness: Harnesses That Improve Themselves

Hangfan Zhang,  Shao Zhang,  Kangcong Li,  Chen Zhang,

Yang Chen,  Yiqun Zhang,  Lei Bai,   Shuyue Hu11footnotemark: 1

Shanghai Artificial Intelligence Laboratory

{zhanghangfan,zhangshao,hushuyue}@pjlab.org.cn
Corresponding Authors

Abstract

The performance of LLM-based agents is jointly shaped by their base models and the harnesses that mediate their interaction with the environment. Because different models exhibit distinct behaviors, effective harness design is inherently model-specific. Yet agent harnesses are still largely engineered by human experts, a paradigm that scales poorly as modern LLMs become increasingly diverse and rapidly evolving. In this paper, we introduce Self-Harness, a new paradigm in which an LLM-based agent improves its own operating harness, without relying on human engineers or stronger external agents. We operationalize Self-Harness as an iterative loop with three stages: Weakness Mining, which identifies model-specific failure patterns from execution traces; Harness Proposal, which generates diverse yet minimal harness modifications tied to these failures; and Proposal Validation, which accepts candidate edits only after regression testing. We instantiate Self-Harness on Terminal-Bench-2.0 using a minimal initial harness and three base models from diverse families: MiniMax M2.5, Qwen3.5-35B-A3B, and GLM-5. Across all three models, Self-Harness consistently improves performance, with held-out pass rates increasing from 40.5% to 61.9%, 23.8% to 38.1%, and 42.9% to 57.1%, respectively. Qualitative analyses further show that Self-Harness does not simply add generic instructions, but effectively turns model-specific weaknesses into concrete, executable harness changes. These results suggest a path toward LLM-based agents that are not merely shaped by their harnesses, but can also participate in reshaping them.

For a conscious being, to exist is to change, to change is to mature, to mature is to go on creating oneself endlessly.

—Henri Bergson, Creative Evolution

1 Introduction

To date, LLM-based agents are not shaped by their base model alone, but also by their harness: the surrounding system that situates the model and mediates its interaction with the environment.
Although there is no universally accepted definition, a harness may include system prompts, tools, runtime mechanisms, verification rules, orchestration logic, and failure-recovery procedures. The same base model can thus exhibit substantially different performance under different harnesses [28, 5, 8].

From early frameworks such as ReAct [29] to product- and platform-level systems such as Claude Code, Codex, and OpenHands, harnesses have largely been engineered by human experts [9, 16, 24, 36, 35].
While effective, this human-centered paradigm does not scale well with the diversity and rapid evolution of modern LLMs. Different models can exhibit distinct behavioral patterns, tool-use habits, error modes, and sensitivities to prompting [22, 21, 18]; consequently, a harness that works well for one model may be suboptimal for another [22, 5, 8]. As new models continue to be released at a rapid pace, manually redesigning and tuning a model-specific harness for each model becomes increasingly costly and untenable.

Figure 1: Three paradigms of harness improvement. In human harness engineering, human engineers manually revise the agent harness. In Meta-Harness, a stronger external agent guides the improvement of a weaker target agent. In Self-Harness, the agent improves its own operating harness.

In this paper, we explore a novel paradigm, Self-Harness: enabling an LLM-based agent to improve the very harness through which it operates (Figure 1). Unlike recent approaches that use stronger external agents to improve the harnesses of weaker ones [5, 8], Self-Harness seeks to internalize this improvement loop within the target agent itself. This paradigm reduces dependence on external guidance that may be costly, unavailable for frontier models, or mismatched to the target model’s failure modes. More broadly, in Bergson’s terms, this points toward a technical analogue of self-creation: a system not merely changed from without, but continually “going on creating itself.”

We operationalize Self-Harness as an improvement loop that repeatedly turns behavioral evidence into harness updates (Figure 2). The loop consists of three stages. Weakness Mining: Starting from an initial harness, the agent with a fixed model is run on a set of tasks, producing execution traces with verifiable outcomes. The agent then clusters failed traces, allowing it to reason about model-specific failure patterns rather than isolated mistakes. Harness Proposal: Based on these failure patterns, the agent generates a small set of diverse yet minimal harness modifications, each tied to a specific failure mechanism. This constraint ensures that proposed edits remain targeted rather than overly general. Proposal Validation: Candidate modifications are evaluated through regression tests, and an edit is promoted only if it improves performance without causing measurable degradation on held-out tasks. If multiple candidate modifications pass the regression tests, they are merged into the next version of the harness, which then serves as the starting point for the next iteration.

In our experiments, we instantiate Self-Harness with a minimal initial harness (Figure 3) and three base models from diverse families: MiniMax M2.5, Qwen3.5-35B-A3B, and GLM-5 [2, 20, 14].
On Terminal-Bench-2.0, Self-Harness consistently improves performance across all three models (Figure 4). For held-in tasks, which provide execution traces to the evaluation system, the pass rate is increased from 43.0% to 50.0% for MiniMax M2.5, from 15.1% to 36.0% for Qwen3.5-35B-A3B, and from 47.7% to 57.0% for GLM-5.
For held-out tasks, whose execution traces are never used as inputs to the evaluation system, the improvements remain substantial. The pass rate is increased from 40.5% to 61.9% for MiniMax M2.5, from 23.8% to 38.1% for Qwen3.5-35B-A3B, and from 42.9% to 57.1% for GLM-5.
These results indicate that Self-Harness can evolve an initial harness into model-specific ones better suited to different base models. Moreover, it can discover broadly useful harness modifications that generalize to unseen tasks rather than merely overfitting to observed evaluation failures.

Qualitative analyses further show that Self-Harness does more than simply make the prompt longer or add generic instructions. Instead, it introduces targeted changes that reflect the recurring problems each model encounters during execution, turning model-specific weaknesses into concrete harness-level interventions. For MiniMax M2.5, the changes encourage the agent to create required output files earlier, handle structured tool outputs more carefully, and stop unproductive tool-use loops before they become too long. For Qwen3.5-35B-A3B, the changes focus on checking dependencies in advance, avoiding repeated failed commands, breaking cycles of endless exploration, and reminding the agent to produce the required artifacts after tool errors. For GLM-5, the changes mainly help the agent preserve environment settings across shell commands and move more quickly from exploration to implementation and testing. Notably, Self-Harness can also introduce broader structural mechanisms, such as subagent-based decomposition and middleware creation, that go beyond local failure repair and improve the overall organization of problem solving.

To summarize, our key contributions are as follows:

•

We propose Self-Harness, a novel paradigm for harness improvement that enables an LLM-based agent to design and refine the harness through which it operates, tailoring it to its own base model without human engineering effort or guidance from a stronger external agent.

•

We operationalize Self-Harness as an iterative loop that turns each model’s behavioral evidence into model-specific harness updates: it evaluates execution traces to identify recurring failure patterns, generates diverse yet minimal candidate edits, and promotes only those that pass regression tests.

•

Experiments on Terminal-Bench-2.0 show that Self-Harness improves performance across 3 models from diverse families, with absolute gains of up to 21.4 percentage points and relative improvements of up to 138%; qualitative analyses further confirm that different models benefit from distinct harness changes, suggesting that Self-Harness can turn model-specific weaknesses into concrete harness changes.

2 Background and Related Work

From prompts to agent harnesses.

Prompt engineering and context engineering show that fixed models can be steered by instructions, demonstrations, retrieved evidence, memory, tool state, and dynamically constructed inputs [10, 25, 21, 6, 17, 12, 26, 7]. Agentic systems extend this control surface from a single input to an execution environment: the model acts, observes consequences, uses tools, receives feedback, and follows runtime policies. ReAct, SWE-agent, Claude Code, and SemaClaw/OpenClaw illustrate how such surrounding mechanisms shape long-horizon agent behavior and software-engineering performance [29, 28, 9, 36].

We use harness for this surrounding system layer: prompts, tools, memory, verification rules, permission policies, adapters, and runtime mechanisms that mediate between the model and the environment. Many important agent failures are failures of this layer rather than failures of an isolated model response: an agent may report success without checking an artifact, retry an unproductive action pattern, lose the source of truth in a long context, or lack a recovery action. These behaviors emerge from the interaction between instructions, observations, tools, and runtime control, so improving them requires changing more than prompt text.

Self-improving agents and automated agent design.

A growing line of work studies systems that adapt their inputs, memories, contexts, or workflows over time [23, 32, 34, 31]. Reflexion stores verbal feedback for later attempts [23], agentic context engineering evolves contexts for later model calls [34], and STOP studies recursive self-improvement for code generation [31]. These methods show that fixed models can benefit from accumulated feedback, but the adapted object is usually a response strategy, memory, context, or generated program rather than a declared agent harness state.

A second line optimizes agent designs from outside the evaluated agent. Automated Design of Agentic Systems searches over agent designs, language agents can be represented as optimizable graphs, and Meta-Harness directly optimizes harness code using source code, scores, and traces from prior candidates [3, 37, 5]. These systems motivate harness-level optimization, but they frame improvement as an external search or optimization process rather than as a bounded edit proposed by the evaluated model under its current harness.

Finally, scientific discovery and self-evolving agent systems such as The AI Scientist, AI Scientist-v2, AlphaEvolve, Alita, Godel Agent, and Darwin Godel Machine automate broader loops of research, algorithm design, or capability expansion [11, 27, 15, 19, 30, 33, 1]. Self-Harness is closest in spirit to this self-improvement literature and to automated harness optimization, but it studies a narrower controlled setting: whether the same fixed model, operating under the current harness, can propose a bounded candidate change to the harness that governs its own future behavior.

3 Self-Harness: An Iterative Loop for Model-Specific Harness Improvement

Human harness engineering improves agent harnesses through expert inspection and manual revision, while external optimizer approaches treat harness design choices as a searchable space. Self-Harness studies a middle ground in which a fixed model iteratively improves the harness around itself through an explicit self-improvement loop driven by execution evidence. In each iteration, the evaluation system runs the current harness and mines recurring failure patterns from clustered execution traces to produce structured evidence. Given this evidence, the same model is invoked in a proposer role to generate a set of diverse yet minimal candidate harness modifications, each targeting a specific failure mechanism without replacing the overall control architecture. Candidate edits are then validated through regression testing on held-out tasks, and an explicit acceptance rule promotes only those edits that improve performance without introducing unacceptable regressions.

3.1 Preliminary

We use harness to denote the non-parametric scaffolding that governs how a fixed language model is deployed as an agent. A harness includes the instructions, the available tools, memory and state-management mechanisms, etc. The harness does not modify the model parameters; instead, it specifies the execution protocol through which the model observes a task, takes actions, invokes tools, checks intermediate artifacts, and produces a final answer.

Formally, let MM be a fixed language model and let hh denote an agent harness. Given a task instance xx, running MM under harness hh produces an execution trace τ\tau and an output yy. The trace records the messages, tool calls, and verifier outcomes. An evaluator then maps the task, trace, and output to a behavioral outcome, such as pass/fail. In this work, the model MM and evaluator ℰ\mathcal{E} are held fixed, while the harness is treated as the object of improvement. Self-Harness therefore operates over a lineage of harnesses h0,h1,…h_{0},h_{1},\ldots, where each transition corresponds to a bounded edit to the execution protocol rather than an update to the model weights.

Figure 2:
Overview of one Self-Harness optimization loop. The current harness hth_{t} with fixed model is evaluated on tasks to collect execution traces, which are clustered into verifier-grounded failure patterns. The same model is then invoked under the current harness as a proposer, using the mined failure patterns to generate bounded candidate harness edits. Candidate edits are evaluated by regression tests on held-in and held-out splits. Accepted candidates are merged to update the harness to ht+1h_{t+1}, while rejected candidates are logged without changing the active harness. Throughout the loop, the model weights and evaluator remain fixed; only the surrounding harness is modified.

Algorithm 1  Self-Harness

1:fixed model MM, initial harness h0h_{0}, held-in split DinD_{\mathrm{in}}, held-out split DhoD_{\mathrm{ho}}, evaluator ℰ\mathcal{E}, proposal width KK, rounds TT

2:final harness hTh_{T}

3:for t=0,1,…,T−1t=0,1,\ldots,T-1 do

4:  (Pin​(ht),Pho​(ht),Rt)←Evaluate​(M,ht,Din,Dho,ℰ)(P_{\mathrm{in}}(h_{t}),P_{\mathrm{ho}}(h_{t}),R_{t})\leftarrow\textsc{Evaluate}(M,h_{t},D_{\mathrm{in}},D_{\mathrm{ho}},\mathcal{E})

5:  Bt←BuildEvidenceBundle​(Rt)B_{t}\leftarrow\textsc{BuildEvidenceBundle}(R_{t})
⊳\triangleright from held-in verifier-grounded failures

6:  𝒫t←ParallelPropose​(M,ht,Bt,K)\mathcal{P}_{t}\leftarrow\textsc{ParallelPropose}(M,h_{t},B_{t},K)
⊳\triangleright 𝒫t={(Δj,aj)}j=1K\mathcal{P}_{t}=\{(\Delta_{j},a_{j})\}_{j=1}^{K}

7:  𝒜t←∅\mathcal{A}_{t}\leftarrow\varnothing

8:  for all (Δj,aj)∈𝒫t(\Delta_{j},a_{j})\in\mathcal{P}_{t} do

9:   ht(j)←Δj​(ht)h_{t}^{(j)}\leftarrow\Delta_{j}(h_{t})

10:   (Pin​(ht(j)),Pho​(ht(j)),Rt(j))←Evaluate​(M,ht(j),Din,Dho,ℰ)(P_{\mathrm{in}}(h_{t}^{(j)}),P_{\mathrm{ho}}(h_{t}^{(j)}),R_{t}^{(j)})\leftarrow\textsc{Evaluate}(M,h_{t}^{(j)},D_{\mathrm{in}},D_{\mathrm{ho}},\mathcal{E})

11:   Δin(j)←Pin​(ht(j))−Pin​(ht)\Delta_{\mathrm{in}}^{(j)}\leftarrow P_{\mathrm{in}}(h_{t}^{(j)})-P_{\mathrm{in}}(h_{t})

12:   Δho(j)←Pho​(ht(j))−Pho​(ht)\Delta_{\mathrm{ho}}^{(j)}\leftarrow P_{\mathrm{ho}}(h_{t}^{(j)})-P_{\mathrm{ho}}(h_{t})

13:   if Δin(j)≥0\Delta_{\mathrm{in}}^{(j)}\geq 0 and Δho(j)≥0\Delta_{\mathrm{ho}}^{(j)}\geq 0 and max⁡(Δin(j),Δho(j))>0\max(\Delta_{\mathrm{in}}^{(j)},\Delta_{\mathrm{ho}}^{(j)})>0 then

14:     𝒜t←𝒜t∪{(ht(j),Δj,aj,Δin(j),Δho(j))}\mathcal{A}_{t}\leftarrow\mathcal{A}_{t}\cup\{(h_{t}^{(j)},\Delta_{j},a_{j},\Delta_{\mathrm{in}}^{(j)},\Delta_{\mathrm{ho}}^{(j)})\}

15:     Accept​(Δj)\textsc{Accept}(\Delta_{j}) ⊳\triangleright passed acceptance rule

16:   else

17:     Reject​(Δj)\textsc{Reject}(\Delta_{j})

18:   end if

19:  end for

20:  if 𝒜t=∅\mathcal{A}_{t}=\varnothing then

21:   ht+1←hth_{t+1}\leftarrow h_{t} ⊳\triangleright no accepted candidate

22:  else

23:   ht+1←MergeAccepted​(ht,𝒜t)h_{t+1}\leftarrow\textsc{MergeAccepted}(h_{t},\mathcal{A}_{t}) ⊳\triangleright accepted edits are merged

24:  end if

25:end for

26:return hTh_{T}

3.2 Weakness Mining: Identifying Failure Patterns from Clustered Execution Traces

The first stage of Self-Harness converts behavioral failures into structured evidence for harness revision. At round tt, we run the fixed model MM under the current harness hth_{t} on a held-in split DinD_{\mathrm{in}}. For each task instance xi∈Dinx_{i}\in D_{\mathrm{in}}, the run produces an output yiy_{i} and an execution trace τi\tau_{i}. The evaluator ℰ\mathcal{E} then assigns an outcome zi=ℰ​(xi,τi,yi)z_{i}=\mathcal{E}(x_{i},\tau_{i},y_{i}), such as pass or fail. This yields a trace record

ri=(xi,τi,yi,zi),r_{i}=(x_{i},\tau_{i},y_{i},z_{i}),

and a round-level record set
Rt={ri}i=1|Din|R_{t}=\{r_{i}\}_{i=1}^{|D_{\mathrm{in}}|}. Since both MM and ℰ\mathcal{E} are fixed, changes in these records across rounds can be attributed to changes in the harness.

A central role of the evaluation system is to avoid treating failures as isolated anecdotes. We therefore focus on the subset of failed records

Ft={ri∈Rt∣zi=fail}.F_{t}=\{r_{i}\in R_{t}\mid z_{i}=\mathrm{fail}\}.

and cluster them by verifier-grounded failure signatures. For each failed record rir_{i}, the evaluation system analyzes the trace as evidence for why the evaluator rejected the run. It identifies the terminal failure reason exposed by the verifier, the agent-side behavior connected to that terminal failure, and the causal status of that behavior within the trace. This attribution step prevents the clustering procedure from conflating superficial symptoms with reusable failure mechanisms: two runs may share the same verifier outcome, such as a timeout or missing artifact, while requiring different harness changes because the underlying agent behaviors differ.

We write this attribution as a failure signature

ϕ​(ri)=(ci,qi,mi),\phi(r_{i})=(c_{i},q_{i},m_{i}),

where cic_{i} denotes the terminal verifier-level cause, qiq_{i} denotes the causal status of the relevant agent behavior, and mim_{i} denotes the abstract agent mechanism exposed by the trace. Failures are clustered by exact agreement of this signature:

Cϕ={ri∈Ft∣ϕ​(ri)=ϕ}C_{\phi}=\{r_{i}\in F_{t}\mid\phi(r_{i})=\phi\}

Thus, the clustering is deterministic and evaluator-grounded: two failed cases are grouped together only when they agree on what the verifier ultimately rejected, how the agent behavior contributed to that rejection, and which reusable behavioral mechanism was involved. The goal is not to discover latent semantic similarity among traces, but to aggregate failures that plausibly admit the same harness-level intervention.

For each cluster CϕC_{\phi}, the evaluation system constructs a structured failure pattern containing its cluster size, representative task instances, shared trace symptoms, verifier evidence, and the inferred agent mechanism. Clusters are then ordered by their support and estimated actionability, so that the proposer is exposed first to recurring mechanisms that are more likely to map to a high-value harness modification.

The output of this stage is an evidence bundle BtB_{t} summarizing the dominant failure patterns observed under hth_{t}. Importantly, BtB_{t} does not prescribe a harness edit. It separates verifier-level failure from agent-level mechanism, allowing the proposer to target a specific reusable weakness rather than patching a coarse outcome such as timeout, assertion failure, or missing output. This keeps the evaluator distinct from the optimizer while ensuring that subsequent candidate modifications are grounded in explicit cross-case evidence.

3.3 Harness Proposal: Exploring Diverse yet Minimal Candidate Modifications

Given the evidence bundle BtB_{t}, the proposal stage translates recurring failure patterns into candidate harness edits. The proposer is not an external optimizer with unrestricted access to the search space. Instead, we invoke the same fixed model MM with current harness hth_{t} in a proposer role and provide it with a bounded proposal context: the editable surfaces of the current harness, the verifier-grounded failure patterns from the evaluation system, records of passing behaviors that should be preserved, and summaries of previously attempted edits. This context exposes the proposer to structured cross-case evidence rather than raw execution logs, encouraging it to reason about reusable failure mechanisms rather than individual task failures.

Self-Harness uses parallel proposal generation to explore several candidate improvements from the same evidence. The proposer generates KK mutually distinct proposal bundles,

𝒫t={(Δj,aj)}j=1K,\mathcal{P}_{t}=\{(\Delta_{j},a_{j})\}_{j=1}^{K},

where each edit Δj\Delta_{j} maps the current harness to a candidate harness

ht(j)=Δj​(ht).h_{t}^{(j)}=\Delta_{j}(h_{t}).

and aja_{j} is an audit record describing the targeted failure pattern, the edited harness surface, the expected behavioral effect, and the regression risks. Each proposal must be grounded in a primary failure mechanism and mapped to a concrete editable surface. The candidates are required to be materially distinct: they should not merely restate the same cluster, surface, or mechanism with different wording. This parallel proposal step broadens exploration while keeping each candidate branch individually interpretable.

The proposer first selects target failure patterns from BtB_{t}. A pattern is considered a suitable target only if it is both supported by evidence and plausibly addressable by an editable harness surface. This addressability criterion is important because not every failure cluster implies a useful harness modification: some clusters reflect task-specific difficulty, unstable outcomes, or model capability limits rather than a missing execution rule. When multiple clusters are plausible, the proposer favors mechanisms that are concrete, recurrent, and likely to be mitigated by a narrow change to the execution protocol; weakly supported or non-addressable patterns are excluded rather than forced into a patch.

Diversity is encouraged across proposal branches, while minimality is enforced within each branch. A proposal may target a different failure mechanism, choose a different harness surface, or express a different hypothesis about how to improve execution. However, each individual edit is constrained to modify only the surface needed to address its selected mechanism, preserve unrelated harness behavior, and avoid broad rewrites of the agent control architecture.

3.4 Proposal Validation: Ensuring Robust Improvement through Regression Testing

A candidate harness edit is not adopted immediately after it is proposed. Instead, each candidate branch is treated as a new harness variant and evaluated under the same evaluator used to diagnose the current harness. For a proposal Δj\Delta_{j}, let ht(j)=Δj​(ht)h_{t}^{(j)}=\Delta_{j}(h_{t}) denote the resulting candidate harness. We evaluate both the current harness hth_{t} and the candidate harness ht(j)h_{t}^{(j)} on the held-in split DinD_{\mathrm{in}} and the held-out split DhoD_{\mathrm{ho}}. The held-in split measures whether the proposal addresses the evidence that motivated it, while the held-out split serves as a regression test for behaviors that were not visible to the proposer.

Let Pin​(h)P_{\mathrm{in}}(h) and Pho​(h)P_{\mathrm{ho}}(h) denote the number of passed tasks for harness hh on DinD_{\mathrm{in}} and DhoD_{\mathrm{ho}}, respectively. We define the split-wise improvements of candidate ht(j)h_{t}^{(j)} over the current harness as

Δin(j)=Pin​(ht(j))−Pin​(ht),\Delta_{\mathrm{in}}^{(j)}=P_{\mathrm{in}}(h_{t}^{(j)})-P_{\mathrm{in}}(h_{t}),

and

Δho(j)=Pho​(ht(j))−Pho​(ht).\Delta_{\mathrm{ho}}^{(j)}=P_{\mathrm{ho}}(h_{t}^{(j)})-P_{\mathrm{ho}}(h_{t}).

A candidate is accepted only if it improves at least one split without degrading the other:

Δin(j)≥0,Δho(j)≥0,max⁡(Δin(j),Δho(j))>0.\Delta_{\mathrm{in}}^{(j)}\geq 0,\quad\Delta_{\mathrm{ho}}^{(j)}\geq 0,\quad\max\left(\Delta_{\mathrm{in}}^{(j)},\Delta_{\mathrm{ho}}^{(j)}\right)>0.

This rule implements a conservative promotion criterion. Proposals that only trade off one split against the other are rejected, even if their total pass count increases. When evaluation is stochastic, we repeat candidate evaluation and apply the same rule to aggregate pass counts across repeats. This reduces the chance that a harness edit is promoted due to a single favorable run. If multiple compatible candidates satisfy the rule in the same round, their edits are merged into the next harness; rejected candidates remain logged but do not change the active harness. In addition to the pass-count rule, validation rejects proposals that do not modify any editable surface or fail execution before a valid evaluation result is obtained. For each evaluated candidate, the system records the changed surfaces, split-wise outcomes, evaluation repeats, proposal summary, and accept/reject decision, making each transition in the harness lineage auditable.

4 Experiments

We evaluate whether Self-Harness can improve agent performance by modifying only the harness around a fixed language model. Our experiments use Terminal-Bench-2.0, which tests terminal interaction in containerized environments. Across multiple model backends, we start from the same minimal DeepAgent-based harness and let Self-Harness propose, validate, and promote bounded edits using held-in execution evidence and held-out regression gates.

⬇

1def build_system_prompt() -> str:

2    return """

3You are running inside a Terminal Bench 2 Harbor task environment.

4

5Use the built-in filesystem and shell tools to inspect the workspace, make

6concrete edits, and verify outcomes against the actual task environment.

7

8Do not assume synthetic datasets, domain-specific tools, or hidden fixtures

9unless you discover them in the repo or runtime.

10""".strip()

11

12

13BASELINE_SYSTEM_PROMPT = build_system_prompt()

14

15

16def build_memory_sources() -> list[str]:

17    return ["/AGENTS.md"]

18

19

20def build_subagents() -> list[dict[str, Any]]:
