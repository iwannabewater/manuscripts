---
source_url: https://arxiv.org/html/2605.27922
fetched_for: learn/canonical-article
source_check_date: 2026-06-20
---

[fetch] tier=local status=ok extractor=stdlib hint="install readability-lxml + html2text for cleaner output"
# Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

> Source: https://arxiv.org/html/2605.27922

Back to arXiv

License: CC BY 4.0

arXiv:2605.27922v1 [cs.AI] 27 May 2026

Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

Yilun Yao1,
Xinyu Tan111footnotemark: 1,
Chao-Hsuan Liu111footnotemark: 1,
Yaoming Li1,
Zhengyang Wang1,
Wenhan Yu1,

Zhewen Tan1,
Yuxuan Tian1,
Guangxiang Zhao2,
Lin Sun2,
Xiangzheng Zhang2,
Tong Yang1

1Peking University   2Qiyuan Tech

These authors contributed equally.

Abstract

LLM agents are increasingly deployed as executable systems that use tools, modify workspaces, and produce concrete artifacts.
In such workflows, performance depends not only on the base model, but also on the harness: the system layer that manages context, tools, state, constraints, permissions, tracing, and recovery.
However, existing benchmarks typically abstract away execution, compare complete agent systems, or hold the harness fixed, making execution-layer variation difficult to study.
We introduce Harness-Bench, a diagnostic benchmark for evaluating configuration-level harness effects in realistic agent workflows.
Harness-Bench evaluates representative harness configurations across multiple model backends under shared task environments, budgets, and evaluation protocols, while preserving each harness’s native execution behavior.
The benchmark contains 106 sandboxed offline tasks constructed from practical agent-use patterns and manually reviewed for realism, solvability, oracle-checkability, and integrity.
Each run records final artifacts, execution traces, usage statistics, and validator outputs, enabling analysis beyond final completion.
Across 5,194 execution trajectories, we observe substantial variation in completion, process quality, efficiency, and failure behavior across model–harness pairings.
These results suggest that agent capability should be reported at the model–harness configuration level rather than attributed to the base model alone.
Our analysis further identifies recurring execution-alignment failures, where plausible reasoning becomes decoupled from tool feedback, workspace state, evidence, or verifiable output contracts.
Harness-Bench provides a reproducible foundation for diagnosing and improving reliable, efficient, and auditable agent execution stacks.
111Our code and data are available at https://github.com/Qihoo360/harness-bench. Additional resources and updates can be found on our project website at http://www.harness-bench.ai/.

1 Introduction

Large language models are increasingly deployed as agents that act in external environments, using tools, modifying workspaces, and producing artifacts that satisfy concrete user requirements (Yao et al., 2022; Schick et al., 2023). In such executable workflows, practical performance depends not only on the underlying model, but also on the system layer that turns model capability into executable action.
We refer to this layer as a harness: the mechanism that organizes context, tools, state, permissions, constraints, and recovery to mediate between model outputs and external actions.
Harnesses are therefore central to agent system design: they shape how model capability is exposed, constrained, and realized, affecting completion, cost, safety, robustness, and auditability (Yang et al., 2024).

Existing benchmarks have advanced LLM and agent evaluation across static reasoning, executable environments, and standardized workflow settings. Static benchmarks such as MMLU (Hendrycks et al., 2021), GSM8K (Cobbe et al., 2021), BIG-bench (Srivastava et al., 2023), and HELM (Liang et al., 2023) measure text-based model capabilities, while agent benchmarks such as SWE-bench (Jimenez et al., 2024), WebArena (Zhou et al., 2024), OSWorld (Xie et al., 2024), and Terminal-Bench (Merrill et al., 2026) evaluate complete systems in executable environments. Workflow-oriented and assistant-agent benchmarks such as AgentBench (Liu et al., 2024), GAIA (Mialon et al., 2024), and Claw-Eval (Ye et al., 2026) further compare model backends under shared execution setups. However, the harness itself remains largely unmeasured: existing benchmarks either abstract away execution, conflate the harness with the full agent system, or fix the harness when comparing models. As a result, we lack a diagnostic protocol for studying how model–harness configurations affect success, token cost, robustness, and traceability in realistic workflows.

We introduce Harness-Bench, a diagnostic benchmark for studying configuration-level harness effects in realistic agent workflows. Recent work on agent-computer interfaces and agent-evaluation infrastructure reflects growing interest in execution-layer design (Jimenez et al., 2024; Kapoor et al., 2025). However, existing efforts typically evaluate a particular agent system, standardize evaluation infrastructure, or compare heterogeneous agent stacks, rather than systematically varying harness configurations across shared task environments and model backends. To our knowledge, Harness-Bench is among the first benchmarks to make the harness a primary axis of evaluation under common external task conditions. Rather than forcing all systems into an identical internal implementation, Harness-Bench fixes the task environment, budget, timeout, and evaluator while preserving each harness’s native execution behavior. The resulting measurements should therefore be interpreted as configuration-level diagnostics of model–harness pairings, not as causal decompositions of individual harness mechanisms. Each run records execution evidence, enabling analysis beyond final completion scores.

Harness-Bench contains 106 realistic, end-to-end agent tasks constructed from practical agent-use patterns and common user requests, each executed in its own sandboxed offline environment with task-specific configuration and evaluation criteria. The task suite is manually reviewed for realism, difficulty, solvability, and evaluation reliability. These environments emulate practical agent settings while avoiding dependence on live services, reducing benchmark drift and making runs reproducible and independently scorable. The tasks require agents to complete concrete workflows rather than isolated tool calls. They span diverse execution demands, including workspace/tool operation, software engineering, data analysis, evidence-grounded knowledge work, and permission-sensitive, stateful, or long-horizon operational workflows. This design preserves realism while providing enough difficulty and diversity to expose meaningful differences across harnesses.

We make three main contributions.
(1) Benchmark asset.
We introduce Harness-Bench, a suite of 106 sandboxed offline tasks for evaluating realistic end-to-end agent workflows with task manifests, fixtures, evaluators, and execution traces.
(2) Evaluation protocol.
We define a model–harness evaluation protocol that fixes external task conditions, budgets, timeouts, and evaluators while preserving each harness’s native execution behavior, enabling configuration-level comparison across representative harnesses and model backends.
(3) Diagnostic analysis.
Across 5,194 execution trajectories, we analyze completion, process quality, efficiency, and recurring failure symptoms. Our results show that performance varies across model–harness pairings and support reporting agent capability at the configuration level rather than attributing it to the base model alone.

2 Related Work

LLM and agent benchmarks.

LLM evaluation has progressed from static language and reasoning benchmarks to executable agent benchmarks. Static benchmarks such as MMLU (Hendrycks et al., 2021), GSM8K (Cobbe et al., 2021), BIG-bench (Srivastava et al., 2023), and HELM (Liang et al., 2023) measure model capabilities in text-based settings, while agent benchmarks such as SWE-bench (Jimenez et al., 2024), Terminal-Bench (Merrill et al., 2026), WebArena (Zhou et al., 2024), and OSWorld (Xie et al., 2024) evaluate agents in software, terminal, web, and operating-system environments. More recent workflow-agent benchmarks, including AgentBench (Liu et al., 2024), GAIA (Mialon et al., 2024), and Claw-Eval (Ye et al., 2026), further emphasize multi-step execution, external state, traceability, safety, robustness, and cost-aware evaluation.
ClawMark (Meng et al., 2026) pushes this direction to long-horizon, multimodal coworker settings, coupling multi-turn and multi-day tasks with persistent tool-backed services and drifting external state.
ClawBench (Zhang et al., 2026) instead stress-tests agents on everyday online workflows over many live production websites, highlighting gaps between sandboxed web benchmarks and real-site complexity.
These benchmarks are essential for measuring model or end-to-end agent capability, but they do not directly evaluate the harness as the variable of interest: they either abstract away execution, evaluate a complete submitted agent stack, or hold the execution setup fixed to compare models. Harness-Bench is complementary: it controls external task conditions while varying harness configurations, enabling diagnostic comparison of completion, token cost, execution safety, robustness, and traceability.

Harnesses and harness engineering.

Recent agent systems increasingly treat the model as one component of a larger execution stack.
Work on agent-computer interfaces (Yang et al., 2024),
tool-use protocols such as the Model Context Protocol (Anthropic, 2024), stateful and multi-agent frameworks (Wu et al., 2024), tracing, guardrails, memory, budget control, and recovery mechanisms reflects growing
attention to the infrastructure that turns model outputs into external actions.
Concrete systems such as OpenClaw (OpenClaw, 2026), NanoBot (HKUDS, 2026), Hermes (Nous Research, 2026), and other agent execution frameworks instantiate these choices differently, exposing different tools, context policies, state-management strategies, permission boundaries, and recovery behaviors.
While this work shows that harness design is central to practical agent performance, existing evaluations usually study a particular system or compare models within a fixed execution setup.
Harness-Bench instead provides a controlled, large-scale benchmark for evaluating harness effects across representative harnesses, multiple model backends, and realistic end-to-end workflows.

3 The Harness-Bench Benchmark

Harness-Bench is a diagnostic benchmark for studying model–harness configurations in executable agent workflows. Each evaluation consists of a task, a model backend, a harness configuration, a sandboxed environment, and an evaluator. The benchmark fixes external task conditions while varying the harness surrounding the model, and records both final artifacts and execution traces.

Figure 1: Overview of the Harness-Bench evaluation pipeline. Each task is instantiated in a sandbox and executed by a model–harness configuration. Harness-Bench records artifacts, traces, usage statistics, and validator outputs, then combines completion, process, and security signals into a diagnostic score.

We use harness to denote the system layer that conditions model calls and turns model outputs into actions in an external workspace. A harness may include prompt templates, action formats, context construction, tool invocation, workspace access, permissions, budget control, tracing, and recovery. These mechanisms are often coupled in real agent systems, so Harness-Bench evaluates complete harness configurations rather than isolating individual mechanisms.

Compactly, we write

Agent=Model+Harness.\text{Agent}=\text{Model}+\text{Harness}.

The environment is external to the agent and includes the task workspace, files, local services, and resources exposed during execution. The evaluator is also external: it observes the completed run and assigns outcome- and process-level scores.

3.1 Harness-Level Evaluation Setting

For each task and model backend, Harness-Bench fixes the user-facing task, initial sandbox state, budget, timeout, and evaluator, while varying the harness configuration. This setting makes the model-surrounding execution layer the primary axis of comparison under shared external conditions.

We do not force all systems into a common internal policy or runtime. Instead, each harness runs with its native execution behavior under the same task resources and evaluation protocol. The resulting measurements should therefore be interpreted as configuration-level diagnostics of model–harness pairings, not as causal decompositions of individual harness mechanisms.

This design is complementary to outcome- and evidence-grounded agent benchmarks such as SWE-bench (Jimenez et al., 2024), AgentBench (Liu et al., 2024), and Claw-Eval (Ye et al., 2026). By varying the harness and recording artifacts, traces, and usage statistics, Harness-Bench supports analysis of completion, tool use, state management, permission handling, robustness, and token cost.

3.2 Task Suite Design and Validation

Category

#

Software Engineering & Codebase Maintenance

22

Data, BI & Finance Analytics

14

Workspace, Tool Use & Multimodal Operations

15

Knowledge, Evidence & Retrieval

13

Office & Business Communication

12

Vertical Professional Workflows

12

Long-running Autonomy & State Adaptation

11

SRE, DevOps & Release Ops

7

Total

106

Figure 2: Task suite overview. Harness-Bench contains 106 sandboxed offline tasks across eight workflow categories.

Harness-Bench contains 106 local, sandboxed tasks designed to evaluate end-to-end agent workflows rather than isolated tool calls. Each task requires a deliverable and is paired with an oracle or rubric that checks completion from the final workspace state and, when needed, the execution trace.

Local execution avoids dependence on live services, reducing benchmark drift and improving reproducibility. Sandboxing ensures that each model–harness pair starts from the same initial state. Each task is specified by a manifest containing the prompt or prompt sequence, fixtures, evaluator, timeout, workflow category, tags, and optional runtime hooks.

The suite covers eight workflow categories, including software engineering, data analysis, workspace and tool operations, evidence-grounded knowledge work, office workflows, vertical professional workflows, long-running state adaptation, and DevOps or release operations. Figure 2 summarizes the task distribution.

Each candidate task is manually reviewed before inclusion. We retain tasks only when they satisfy four criteria: Realism, reflecting a plausible user workflow; Solvability, meaning the task can be completed using the provided sandbox resources; Oracle-checkability, meaning success can be verified by deterministic checks or a specified rubric; and Integrity, meaning agents cannot obtain credit by reading hidden answers, modifying protected fixtures, or bypassing constraints.

3.3 Run Protocol and Evidence Collection

As shown in Figure 1, Harness-Bench uses a setup–execution–judge pipeline. In setup, the benchmark renders the task specification, constructs the runtime environment, and initializes a fresh sandbox. In execution, the configured agent attempts the task under the specified budget and workspace constraints. During this phase, Harness-Bench records model requests and responses, tool calls, workspace changes, and usage statistics, and reconstructs them into a unified trace. For multi-round tasks, Harness-Bench preserves session context across rounds while applying any task-defined state updates.

In the judge phase, the evaluator inspects the final workspace and execution evidence. Reference artifacts, hidden answers, and evaluator scripts are not exposed to the agent during execution. Conceptually, a run is

R=Run​(M,H,E,T),TaskScore=Eval​(R;J),R=\mathrm{Run}(M,H,E,T),\qquad\mathrm{TaskScore}=\mathrm{Eval}(R;J),

where MM is the model, HH is the harness configuration, EE is the sandboxed environment, TT is the task, and JJ is the evaluator.

Each run produces four sources of evidence: the final workspace state, execution trace, usage statistics, and validator outputs. These support completion scoring, process diagnostics, cost analysis, permission checks, and failure analysis.

3.4 Scoring and Metrics

Harness-Bench scores each run using both the final outcome and the execution trace. Completion is measured with task-specific deterministic validators when possible and rubric-based judgment when necessary. The trace is evaluated with LLM-based process rubrics (Zheng et al., 2023) covering robustness, tool-use appropriateness, and consistency. Explicit security or permission violations are handled by a binary gate.

For task ii, the overall score is

TaskScorei=Securityi⋅Completioni⋅Processi,\mathrm{TaskScore}_{i}=\mathrm{Security}_{i}\cdot\mathrm{Completion}_{i}\cdot\mathrm{Process}_{i},

where Securityi∈{0,1}\mathrm{Security}_{i}\in\{0,1\} and

Processi=Robustnessi+ToolUsei+Consistencyi3.\mathrm{Process}_{i}=\frac{\mathrm{Robustness}_{i}+\mathrm{ToolUse}_{i}+\mathrm{Consistency}_{i}}{3}.

All non-binary scores are normalized to [0,1][0,1].

Completioni\mathrm{Completion}_{i} measures task-specific output quality. Securityi\mathrm{Security}_{i} is set to 0 if the run violates explicit permission or security constraints, such as unauthorized access, secret exposure, or forbidden actions; otherwise it is set to 11.

The process score is computed from the reconstructed trace. Robustnessi\mathrm{Robustness}_{i} measures whether the agent handles tool or environment failures. ToolUsei\mathrm{ToolUse}_{i} measures whether tools are selected and applied appropriately. Consistencyi\mathrm{Consistency}_{i} measures whether actions, observations, intermediate state, and final outputs remain consistent with the workspace state and user constraints.

The multiplicative score is intentionally conservative: high aggregate credit requires task completion, no explicit security violation, and reliable execution behavior. Because the aggregate depends partly on rubric-based process assessment, we also report completion, security, robustness, tool use, consistency, token usage, and turns separately. We interpret the aggregate score as a diagnostic benchmark measure rather than a standalone deployment guarantee.

4 Experiments

We evaluate Harness-Bench as a diagnostic protocol for model–harness configurations.
Rather than isolating individual harness mechanisms, we measure complete harness configurations under shared external task conditions and interpret the results as descriptive benchmark measurements under this protocol.

Factor

Treatment in Harness-Bench

Task prompt and fixtures

Fixed for each task

Initial sandbox state

Fixed for each task

Budget, timeout, evaluator

Fixed for each task

Model backend

Varied in the factorial matrix

Harness configuration

Varied in the factorial matrix

Prompting and action format

Native to each harness

Tool interface and state policy

Native to each harness

Retry and recovery behavior

Native to each harness

Permissions and tools

Minimal required set enabled

Table 1: Controlled and varying factors in the main evaluation. Harness-Bench fixes external task conditions while preserving each harness’s native execution behavior.

4.1 Setup

Harness-Bench contains 106 tasks.
Our main evaluation uses 6 configurable harnesses and 8 API model backends, forming a full factorial matrix over tasks, models, and harnesses.
The complete list of harnesses and model backends is provided in Appendix B.
This matrix produces 5,088 execution trajectories.
We additionally evaluate Codex as a model-bound coding agent under its default model configuration, adding 106 trajectories.
We report Codex separately because it does not expose the same configurable model-backend interface as the other harnesses.
Overall, our experiments analyze 5,194 trajectories.

Each trajectory corresponds to one complete task attempt under a fixed task, model backend, and harness configuration.
For each harness, we start from its default configuration and enable only the permissions and tools required to complete the task suite.
All runs use the same task-specific initial workspace, budget, timeout, and evaluator, while preserving each harness’s native prompting, tool interface, state management, and recovery behavior.
All trajectories are evaluated using the outcome oracle and trajectory-level process rubric defined in Section 3.4.
For LLM-based process assessment, we use claude-sonnet-4.6 as a fixed external judge across all trajectories.
Table 1 summarizes the controlled and varying factors in our evaluation protocol.

Harness
Score(%)
Comp.(%)
Secur.(%)
Process
Efficiency
