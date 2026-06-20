---
source_url: https://arxiv.org/html/2606.12344
fetched_for: learn/canonical-article
source_check_date: 2026-06-20
---

[fetch] tier=local status=ok extractor=stdlib hint="install readability-lxml + html2text for cleaner output"
# Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks

> Source: https://arxiv.org/html/2606.12344

Back to arXiv

License: arXiv.org perpetual non-exclusive license

arXiv:2606.12344v1 [cs.LG] 10 Jun 2026

Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks

Mengyu Zheng

TokenRhythm Technologies

Kai Han

TokenRhythm Technologies

Boxun Li

Infinigence AI

Haiyang Xu

Infinigence AI

Yuchuan Tian

Peking University

TokenRhythm Technologies

Wei He

TokenRhythm Technologies

Hang Zhou

TokenRhythm Technologies

Jianyuan Guo

City University of Hong Kong

Hailin Hu

TokenRhythm Technologies

Lin Ma

SEE Fund

Chao Xu

Peking University

Guohao Dai

Shanghai Jiaotong University

Infinigence AI

Lixue Xia

Infinigence AI

Yunchao Wei

Beijing Jiaotong University

Yunhe Wang

TokenRhythm Technologies

Yu Wang

Tsinghua University

{mengyu.zheng, kai.han, yunhe.wang}@tokenrhythm.ai yu-wang@mail.tsinghua.edu.cn

Abstract

General-purpose agents such as OpenClaw are increasingly used as autonomous tool users, but their coding ability is difficult to measure under SWE-bench: a generic agent does not by itself satisfy the clean Docker workspace, patch, and prediction contract required for scoring. We introduce Claw-SWE-Bench, a multilingual SWE-bench-style benchmark and adapter protocol that makes heterogeneous agent harnesses, or claws, comparable under fair settings including a fixed prompt, runtime budget, workspace contract, patch extraction procedure, and evaluator. The full benchmark contains 350 GitHub issue-resolution instances across 8 languages and 43 repositories, drawn from SWE-bench-Multilingual and SWE-bench-Verified-Mini after future-commit cleanup. We also release Claw-SWE-Bench Lite for faster validation, which is an 80-instance subset selected by a cost-aware, rank-aware procedure over 17 calibration columns. On the full benchmark, OpenClaw with a minimal direct-diff adapter scores only 19.1%19.1\% Pass@1, whereas the full adapter reaches 73.4%73.4\% with the same GLM 5.1 backbone, showing that adapter design is essential for enabling OpenClaw-style harnesses to perform coding tasks effectively. Across an OpenClaw ×\times nine-model sweep and a five-claw ×\times two-model sweep, model choice changes Pass@1 by 29.429.4 pp and harness choice by 27.427.4 pp under fixed models; systems with similar accuracy can differ substantially in total API cost. Claw-SWE-Bench therefore treats harness and cost accounting as first-class axes of SWE-style coding-agent evaluation, providing both a full benchmark and a low-cost reference set for reproducible comparison.
The data is available at https://github.com/opensquilla/claw-swe-bench and https://huggingface.co/datasets/TokenRhythm/Claw-SWE-Bench.

1 Introduction

General-purpose agents exemplified by OpenClaw [steinberger_openclaw] have rapidly expanded into productivity tools, browser automation, computer-use tasks, and scientific assistance. Yet it remains unclear whether such agents can serve as effective coding agents on real software-engineering tasks. Existing public evaluations mostly cover open-ended productivity tasks, workplace collaboration tasks [ding_wildclawbench_2026, zai_zclawbench, meng2026clawmarklivingworldbenchmarkmultiturn], or broad agent leaderboards [pinchbench, ye2026clawevaltrustworthyevaluationautonomous, clawbench_general, clawprobench2026]; direct evidence about their repository-level coding ability is still limited.

The natural way to test this ability is to use a SWE-bench-style benchmark [jimenez_swebench_2024], because SWE-bench has become the de facto standard for repository-level coding agents. However, leading SWE-bench-style reports often package the prompt template, agent loop, tool interface, per-instance timeout, patch extraction strategy, and stopping logic into a single released system, together with a particular model and task set. The resulting resolved rate therefore conflates three causally distinct factors: the evaluated LLM, the harness that turns the LLM into an agent, and the task instances being solved. To determine whether OpenClaw and other general harnesses can perform coding tasks, and to compare such systems in an attributable way, this conflation must be separated. This is the technical problem addressed by this paper.

Prior SWE-bench-style evaluations have not isolated the harness dimension. Single-harness systems such as SWE-agent [swe_agent], AutoCodeRover [zhang_autocoderover], OpenHands [wang_openhands], and mini-SWE-agent [mini_swe_agent] report per-system numbers, but their scaffolds, prompts, budgets, and termination policies vary with the system, making cross-system differences hard to attribute to harness design. Multilingual extensions [swe_smith] and human-verified Python subsets [swebench_verified_mini] expand the task dimension while retaining the same single-harness reporting pattern. Three closer lines of work partially identify this issue but do not treat the harness as a controlled variable. HAL [kapoor_hal] advocates holistic accuracy–cost–latency evaluation, but releases only one harness and therefore cannot identify harness ×\times model interactions. SWE-Bench Pro [deng_swebench_pro] uses unified scaffolding for long-horizon tasks, but the scaffolding is used to compare models under one harness rather than to compare harnesses. SWE-Effi [fan_swe_effi] explicitly notes scaffold–model entanglement, but changes scaffold without fixing prompt, timeout, and concurrency; its scaffold ×\times model dependency remains a caveat rather than a controlled measurement. The unresolved challenge is that no SWE-bench-style benchmark has made the agent harness a controlled experimental variable.

Figure 1: Resolve-rate–cost Pareto frontier.
Data are from the five-claw ×\times two-model sweep in Table 3. Each point is one claw–model combination on the full 350-instance evaluation; the vertical axis is Pass@1 / resolved rate, and the horizontal axis is full-run total API cost (USD, log scale). The black line connects non-dominated operating points.

This conflation also hides resource cost. A real coding agent is not a single model call: it repeatedly reads files, edits code, runs commands, and waits for remote model responses. The same Pass@1 can correspond to very different token usage, wall-clock duration, and interaction length. Reporting only resolved rate rewards systems that rely on longer exploration or higher budgets, and can lead to misinterpreting systems that are cheaper or faster but more brittle. A coding-agent benchmark therefore needs to report accuracy together with end-to-end cost under a fixed outer budget. Cost determines whether a full evaluation, regression test, or system iteration is actually affordable, and affects whether small teams and academic groups can participate in such benchmarking.

Figure 1 illustrates this point using the full 350-instance sweep over five claws and two models. Each point is one claw–model combination under the same evaluation protocol, with Pass@1 on the vertical axis and total API cost on the horizontal axis; the black curve marks the Pareto frontier, where no other combination is both cheaper and more accurate. Accuracy and cost do not move in lockstep. We therefore treat cost-aware reporting as part of the benchmark design rather than an auxiliary log appended after resolved rate.

We introduce Claw-SWE-Bench, a multilingual SWE-bench-style benchmark that treats the agent harness as a controlled experimental variable. The benchmark decomposes the evaluation stack into a fixed base – prompt template, task set, execution container, per-instance timeout, patch extraction, and evaluator – plus a replaceable harness slot. Harnesses enter this slot through a shared adapter protocol exposing a small set of lifecycle methods (the full interface is described in §2.2). The workload contains 350 real GitHub issue-resolution instances across 8 programming languages and 43 repositories, drawn from SWE-bench-Multilingual [swe_smith] and SWE-bench-Verified-Mini [swebench_verified_mini], and evaluated with the upstream SWE-bench evaluator. All systems share the same outer budget and report total API cost, average wall-clock duration, and cache hit rate alongside Pass@1, so accuracy and end-to-end cost can be interpreted in the same table and on the same Pareto plane.

To lower the barrier to use, we also release Claw-SWE-Bench Lite, an 80-instance low-cost subset for users who need to evaluate model coding ability or iterate on harness design without repeatedly paying for the full 350-instance, multi-harness ×\times multi-model grid. Lite is not a convenient showcase sample; it is designed to preserve the scale, language distribution, key rankings, and cost structure of the full set under limited budget, enabling shorter feedback loops for model replacement, adapter debugging, prompt adjustment, and regression testing. Lite uses the cost-aware, rank-aware selection method in §3.2, optimizing resolve-rate parity, pairwise ranking stability, and cost parity over 17 calibration columns. The final 80-instance Lite subset reduces full-run cost to about 22.9%22.9\% of full-350; over the 17 calibration columns, the mean Pass@1 values on full-350 and Lite-80 are 0.6390.639 and 0.6430.643, a difference of about 0.40.4 pp. A K-sweep shows that the minimum acceptable per-language size falls in K∗∈[8,10]K^{*}\in[8,10]; we release the conservative and stable K=10K{=}10 point. Lite does not replace the full benchmark, but provides a practical entry point for screening, regression evaluation, and result checking under constrained budgets.

Using this protocol and Lite subset, Claw-SWE-Bench provides a common task set, budget, and scoring pipeline for measuring differences in harness coding ability and run cost under comparable conditions. We conduct two complementary studies: a model sweep that fixes openclaw and evaluates nine LLMs, and a claw sweep that fixes two representative models (GLM 5.1 and Qwen 3.6-flash) and evaluates five claws. First, a general-purpose OpenClaw harness achieves competitive Pass@1 on real issue-resolution tasks, showing that a general harness can enter SWE-bench-style coding evaluation through an adapter. Second, harness choice is a first-order factor: under a fixed model, the claw spread reaches 12.512.5 pp on GLM 5.1 and 27.427.4 pp on Qwen 3.6-flash, large enough to reorder leaderboard conclusions if the harness is not specified. Finally, accuracy and cost are not simply aligned; comparable SWE-style results require explicit control and disclosure of harness, budget, cost metric, and cache accounting.

2 Claw-SWE-Bench

The first question in this paper is whether a general-purpose agent such as OpenClaw can enter a SWE-bench-style evaluation of real coding tasks. To make this question experimentally testable, we first specify the SWE-bench [jimenez_swebench_2024] scoring contract. Given the problem_statement, target repo, and base_commit for a real GitHub issue, a system must submit a diff patch that can be applied to the repository checkout. The official evaluation harness does not read an interaction trace or a final natural-language answer. It reads a prediction file in which each instance contains at least instance_id, model_name_or_path, and a string-valued model_patch. The evaluator then prepares the repository in the Docker evaluation environment for that instance, applies the patch to the checkout under /testbed, and runs repository-level tests to determine whether the instance is resolved. In short, the core SWE-bench interface is an evaluator-facing patch prediction, not a generic agent session.

Coding harnesses such as SWE-agent [swe_agent] are designed around this contract. OpenClaw, by contrast, is normally run as a more general agent interaction and therefore cannot be treated as a SWE-bench evaluation target without adaptation. First, the SWE-bench Docker image is primarily a reproducible target-repository, dependency, and test environment; it does not itself provide the agent lifecycle, tool configuration, API access, session state, or workspace management required by OpenClaw. These runtime dependencies and state must be brought inside a controlled container boundary while ensuring that the agent’s actual code edits occur in /testbed. Second, general-purpose agents often signal completion through final text, structured messages, or internal logs, whereas the SWE-bench evaluator reads only the model_patch field. Explanatory answers are not directly scorable. Third, a general agent can create session files, metadata, caches, or other non-solution artifacts during execution; if these enter git diff, they contaminate the patch submitted to the evaluator.

These limitations do not imply that OpenClaw lacks coding ability. They imply that native OpenClaw cannot directly enter the SWE-bench scoring pipeline. The premise we first challenge is that SWE-bench-style coding tasks must be solved only by purpose-built coding harnesses. General-purpose agents can participate in real issue resolution if an adapter constrains their behavior to concrete repository edits and converts the final repository state into an evaluator-readable patch. Once this access problem is solved, the next step is to define a unified evaluation standard that compares the coding ability and run cost of different claws or harnesses under the same tasks, budgets, and scoring pipeline.

We therefore propose Claw-SWE-Bench, a multilingual SWE-style benchmark and execution protocol for evaluating coding-agent harnesses. It combines 350 real GitHub issue-resolution tasks across 8 programming languages with a unified adapter layer, allowing heterogeneous “claws” – agent harnesses that wrap LLMs into autonomous coding systems – to run under the same evaluation protocol.

Claw-SWE-Bench achieves this in two layers. The first layer is the adapter: it connects the native execution style of a general or specialized harness to the repository-editing and patch-prediction process required by SWE-bench, making these systems eligible for the same class of coding tasks. The second layer is a shared orchestrator: it fixes the task set, repository state, task prompt, Docker runtime, outer budget, patch extraction, prediction format, and downstream SWE-bench evaluation, elevating the harness from an incidental implementation detail to an experimental variable. Under this control, differences in Pass@1, wall-clock duration, and turn traces can be attributed to model or harness dimensions rather than to inconsistent evaluation protocols. The rest of this section describes the workload source, adapter protocol, and standardized execution pipeline.

Figure 2: Contract mismatch between OpenClaw-style harnesses and SWE-bench.
The adapter converts a general agent interaction into a SWE-bench-scored patch prediction, while outer controls ensure fairness, comparability, and traceable cost.

2.1 Workload Source and Composition

The full Claw-SWE-Bench workload is built from two upstream SWE-bench-derived sources. SWE-bench-Multilingual [swe_smith] contributes 300 non-Python instances covering Java, Go, Rust, JavaScript/TypeScript, C/C++, Ruby, and PHP. SWE-bench-Verified-Mini [swebench_verified_mini] contributes 50 human-validated Python instances. Together, the full benchmark contains 350 real GitHub issue-resolution tasks across 8 programming languages and 43 repositories.

Each instance preserves the upstream SWE-bench task format and evaluation assets, including problem_statement, repo, base_commit, the corresponding Docker evaluation image, and the repository-level tests used for scoring. This combination serves two purposes. First, the benchmark remains compatible with SWE-bench’s patch-based evaluation. Second, multilingual tasks and human-validated Python tasks jointly provide broader real-software-engineering coverage, so harness comparisons are not limited to one language or one upstream subset. All model–harness combinations are run on the same 350 instances, allowing resolved-rate and cost differences to be interpreted under a fixed workload.

2.2 Adapter Protocol

The adapter protocol is the first layer of Claw-SWE-Bench. It does not require different harnesses to use the same internal agent loop; instead, it standardizes the interface between a harness and the benchmark lifecycle. Each supported harness implements the same abstract methods: create_agent, send_task, backup_session, delete_agent, and get_docker_args. The shared orchestrator drives a run only through these methods, without needing to know which harness is underneath. This design decouples the benchmark lifecycle from agent implementation: container management, prompt instantiation, patch collection, prediction writing, metadata recording, resume support, and evaluation are implemented by the benchmark layer, while each harness adapter only connects its agent to that lifecycle and provides the code needed to drive the agent inside the container.

At runtime, the shared orchestrator enforces the access boundary shown in Figure 2. Container startup, repository reset, prompt instantiation, patch collection, prediction writing, metadata recording, and evaluation are handled uniformly by the benchmark layer. The adapter provides harness-specific hooks to create or configure the agent, dispatch the instantiated task, save run artifacts, and clean harness state. This boundary is deliberate: the benchmark layer owns the task-facing environment and evaluator-facing patch format, while the internal agent loop remains part of the harness being studied.

Crucially, candidate patches are collected from repository state rather than parsed from an agent’s final message. An agent expresses a solution only by editing files in the repository. This makes the output contract independent of whether the harness natively produces JSON, plain text, a final narrative response, or no structured response at all.

All harnesses are launched through the same command-line entry point, run_infer.py. The evaluator specifies the harness name, dataset configuration, model identifier, run identifier, timeout, worker count, and optional instance filters. Dataset metadata is loaded from configured SWE-bench sources, and each instance is represented by the fields required by the protocol: instance_id, repo, base_commit, and problem_statement. A harness registry maps string IDs (openclaw, hermes, nanobot, zeroclaw, and generic) to adapter classes. Adding a new claw only requires implementing the adapter interface and registering it in the harness map; the dataset loader, Docker workspace manager, prompt builder, patch collector, prediction writer, and evaluator remain unchanged.

2.3 Standardized Execution Pipeline

The adapter determines whether heterogeneous harnesses can enter a common evaluation protocol. Outside that boundary, Claw-SWE-Bench further fixes the evaluation-stack components that would otherwise confound harness comparisons.

Runtime and workspace.
Each task runs inside its corresponding SWE-bench evaluation Docker image, with the repository reset to the instance’s base_commit and mounted at /testbed. For the seven non-Python languages from SWE-bench-Multilingual, we also handle future-commit visibility during workspace preparation. While inspecting the containers, we found that some images still exposed Git commits after base_commit; if left unchanged, an agent could inspect future fixes through git log or git show, which is incompatible with the patch-based evaluation contract. The runner therefore removes reachable future commits so that the agent can only read, edit, and run code within the history boundary of the issue. All harnesses share the same outer budget: a 3600-second wall-clock timeout, one run per instance, and fixed worker concurrency. Harness-specific dependencies can be supplied through Docker arguments or bind mounts, but the repository state, evaluation image, and outer budget perceived by the agent are fixed. These budget controls prevent longer exploration time from being mistaken for stronger harness design and make cost metrics comparable across harnesses. Because different harnesses define a “turn” differently, wall-clock duration is the primary comparable resource metric; turn count is treated as a diagnostic trace. Token statistics are available for some harnesses but not exposed uniformly by all systems, so they are not the sole cross-harness metric.

Prompt instantiation.
Every instance is instantiated from the same task-prompt template. The prompt includes the problem statement and base commit, instructs the agent to work in /testbed, forbids git add and git commit, and asks the agent not to modify test files. Thus the task-facing input message is held fixed across harnesses. The protocol does not attempt to standardize a harness’s internal system prompt, tool schema, parser hints, memory strategy, or stopping rule; these remain part of harness design and therefore part of the experimental variable.

Patch and scoring contract.
Candidate solutions are collected from repository state rather than parsed from the agent’s final response. After a harness terminates, times out, or returns an error, the runner computes the diff against the base commit, removes known non-solution artifacts, and writes a SWE-bench-compatible prediction. This centralized patch-submission process allows heterogeneous harnesses to be compared even when their native outputs differ: JSON, plain text, natural-language summaries, and missing structured responses are all reduced to the same evaluator-facing patch format. Evaluation is then performed by the official SWE-bench harness.

To separate “placing OpenClaw inside Docker” from “reliably satisfying the SWE-bench scoring contract,” we also define a minimal bare adapter as a diagnostic baseline. The bare adapter provides only minimal integration: it enters the corresponding Docker workspace for each instance, sends the issue description to OpenClaw, and disables network retrieval that would clearly violate fairness. It does not perform full workspace alignment, future-commit cleanup, shared phase prompting, Git-based patch extraction, or patch cleaning; instead, it asks the model to output a unified diff directly in the final response. By contrast, the full adapter used in the main experiments requires the agent to edit files under /testbed, after which the runner exports model_patch from the final repository state. This comparison tests the necessity of the adapter, not the attribution of individual adapter components.

3 Claw-SWE-Bench Lite

The full 350-instance benchmark is the standard evaluation surface in this paper, but it is not suitable as the feedback loop for every development iteration. A full-350 run requires substantial token usage, API cost, wall-clock time, and log inspection effort. During adapter debugging, prompt modification, model replacement, or regression testing, repeatedly running the full set can make evaluation itself the bottleneck. Claw-SWE-Bench Lite is therefore designed as a low-cost companion to the full benchmark rather than as a replacement leaderboard: with 80 instances, it approximates the Pass@1 scale, per-language distribution, cross-claw relative behavior, and run-cost structure of full-350, allowing researchers to triage system changes with a shorter feedback loop before returning to full-350 for final reporting.

3.1 Lite Subset Definition

Lite-80 selects 10 instances from each of the 8 languages in full-350. The 70 non-Python instances come from SWE-bench-Multilingual, and the 10 Python instances come from SWE-bench-Verified-Mini [swebench_verified_mini], matching the source of the Python portion of the full set. In addition to language balance, Lite enforces a fixed within-language difficulty-quartile quota of 2/3/3/22/3/3/2 over Q1/Q2/Q3/Q4Q_{1}/Q_{2}/Q_{3}/Q_{4}, avoiding implicit resampling of any language toward unusually easy or unusually hard tasks. The final subset covers 34 of the 43 repositories in full-350 (79%79\%), preserving a substantial amount of repository diversity.

Lite is not a simple random sample. It is fitted to full-350 behavior over 17 calibration columns. These columns include 9 OpenClaw model columns and 8 cross-claw columns from 4 non-openclaw claws (hermes, nanobot, zeroclaw, and generic) evaluated on two shared models, GLM 5.1 and Qwen 3.6-flash. This calibration pool spans both model variation and claw variation. Lite’s objective therefore goes beyond preserving an average resolved rate: it aims to preserve the comparability scale of different systems on the full benchmark.

(a) Per-language parity (17-column mean)

(b) Cross-claw parity

(c) K-sweep sensitivity envelope

Figure 3: Lite-80 parity with full-350. (a) Per-language comparison between full-350 and Lite-80 Pass@1, averaged uniformly over the 17 calibration columns. (b) Cross-claw Pass@1 comparison between full-350 and Lite-80 over 5 claws ×\times 2 shared models. (c) K-sweep sensitivity envelope; the minimum acceptable KK falls in [8,10][8,10] across scenarios, and the release uses the conservative stable point K=10K{=}10, or 10 instances per language.

3.2 Cost-Aware, Rank-Aware Selection

We formulate Lite selection as a binary selection problem over the 350 full-set instances. The variable xi∈{0,1}x_{i}\in\{0,1\} indicates whether instance ii is included in Lite. Hard constraints require selecting 10 instances per language and satisfying the fixed 2/3/3/22/3/3/2 difficulty-quartile quota within that language. Difficulty quartiles are computed from the mean resolved rate over the calibration pool, so they reflect relative difficulty under multiple models and claws rather than under a single system.

The objective controls three sources of bias. The first term is resolve-rate parity: over the 17×817\times 8 grid of calibration columns by language, it minimizes the L1 difference between the Lite-estimated rate and the true full-350 rate. The second term is a pairwise ranking hinge: when two calibration columns differ by more than RANK_EPS=0.03\textrm{RANK\_EPS}=0.03 on full-350, a penalty is applied if Lite reverses the order or falls within a 0.050.05 margin (λ=1.0\lambda=1.0). The third term is cost parity: for each calibration column, it minimizes the log-cost discrepancy between Lite and full-350 (cost_alpha=1\textrm{cost\_alpha}=1), preventing the subset from matching resolved rate while being biased toward unusually cheap or expensive instances. Optimization uses per-language 200-restart within-quartile 1-swap local search, which keeps all hard constraints satisfied throughout the search and avoids reliance on an external solver.

3.3 Validation Results and the 80-Instance Scale

Figure 3 summarizes the main validation results for Lite-80. Across the 17 calibration columns, mean Pass@1 is 0.6390.639 on full-350 and 0.6430.643 on Lite-80, a difference of about +0.4+0.4 pp. Per-language deviations are small overall: Go, JS/TS, PHP, and Python are all within 11 pp; the two largest deviations are C/C++ (+2.94+2.94 pp) and Ruby (+2.65+2.65 pp). In the 5 claws ×\times 2 models cross-claw check, which is closer to how leaderboards are used, the mean absolute Lite–full difference is 1.881.88 pp and the maximum difference is 3.683.68 pp (nanobot ×\times Qwen 3.6-flash). These results indicate that Lite-80 does not merely fit one local OpenClaw model, but preserves a cross-model and cross-claw evaluation scale.

The cost side must also be checked. Lite-80’s actual per-instance cost is close to that of full-350; because the number of instances falls from 350 to 80, a full Lite run costs about 22.9%22.9\% of a full run. Broken down by resource type, the full-run ratios for input tokens, output tokens, cache-read tokens, and wall-clock duration are approximately 22.2%22.2\%, 23.6%23.6\%, 22.6%22.6\%, and 23.0%23.0\%, respectively. Lite therefore provides an evaluation surface at roughly one quarter of the cost, rather than lowering cost by selecting anomalously cheap examples.

The choice of 80 instances also comes from an explicit K-sweep rather than a convenient round number. We scan subset size in units of KK instances per language and repeat selection and validation across different margin, restart, seed, and mirror-parity scenarios. Sensitivity analysis finds that the minimum acceptable size lies in K∗∈[8,10]K^{*}\in[8,10]: two scenarios pass at K=8K{=}8, three require K=9K{=}9, and four structural-perturbation scenarios require K=10K{=}10. We release Kmax∗=10K^{*}_{\max}=10, or 8 languages ×\times 10 instances = 80 instances. At this size, the resolve gates (R-A/R-B/R-C), cost gates (C-A/C-B/C-C), and operational composite gate all pass. Lite-80 is therefore the smallest conservative stable release point under the sensitivity envelope: smaller KK values can work in some configurations, but are not robust enough to serve as the default reusable low-cost benchmark.

4 Experimental Setup

We use Claw-SWE-Bench to study two sources of variation in SWE-style coding-agent evaluation: the LLM, and the claw that wraps the LLM into an autonomous coding system. We report two complementary experimental grids rather than an exhaustive claw ×\times model grid over all 350 instances. First, we fix a reference claw and sweep the model axis. Second, we fix two representative models and sweep the claw axis. Finally, we validate whether the Lite subset preserves the trend of the full set.

Claws.
We evaluate five claws: openclaw [steinberger_openclaw], hermes-agent [nous_hermes_agent], zeroclaw [zeroclaw_labs], nanobot [hkuds_nanobot], and a GenericAgent [generic_agent_2026]. In this paper, a claw is the harness-specific agent loop running inside the standardized Claw-SWE-Bench protocol. All claws receive the same task prompt, run in the same SWE-bench Docker workspace, and obey the same outer budget.

Models.
The model sweep uses openclaw with nine LLMs spanning a broad capability and cost range: GPT 5.5 [openai_gpt_55], Claude Opus 4.7 [anthropic_claude_opus_47], GLM 5.1 [zai_glm_51], DeepSeek-V4 Pro [deepseek_v4_pro], DeepSeek-V4 Flash [deepseek_v4_flash], Kimi 2.6 [moonshot_kimi_k26], Qwen 3.6-flash [alibaba_qwen36_flash], MiniMax M2.7 [minimax_m27], and Seed 2.0-mini [bytedance_seed_20_mini]. The claw sweep uses two representative models: GLM 5.1, a stronger mid-tier model, and Qwen 3.6-flash, a lower-cost small model. This two-model claw sweep exposes both high-capability behavior, where ceiling effects may reduce visible claw differences, and small-model behavior, where harness brittleness and stopping policy often matter more. Model inference is routed through external API providers; provider mappings and model identifiers are listed in the reproducibility appendix.

Evaluation metrics.
The primary metric is Pass@1, defined as the fraction of instances whose submitted patch is marked Resolved by the SWE-bench evaluator:

Pass@1=#​Resolved#​Instances.\textsc{Pass@1}=\frac{\#\textsc{Resolved}}{\#\textsc{Instances}}.

In addition to accuracy, we report two classes of efficiency metrics. The first class is end-to-end run cost, including Total Cost (USD) for the full 350-instance run and mean wall-clock duration. Total Cost comes from the corresponding API provider or cache-proxy billing logs and measures the actual resource cost of a full evaluation; duration is recorded by the outer runner and includes remote API latency. The second class is cache-use diagnostics. We report Cache Hit Rate:

CacheHit=#​CacheReadTokens#​InputTokens+#​CacheReadTokens.\textsc{CacheHit}=\frac{\#\textsc{CacheReadTokens}}{\#\textsc{InputTokens}+\#\textsc{CacheReadTokens}}.

Cache hit rate affects actual API cost and should therefore be disclosed with cost, but it is not a coding-capability metric: it depends on provider cache policy, adapter call paths, and context-reuse strategy.

Lite held-out validation.
In addition to the full-350 main experiments, we use OpenSQuILLA as a held-out system to check whether Lite-80 reproduces the aggregate evaluation scale of the full benchmark. OpenSQuILLA is not used to construct or calibrate the Lite subset. The experiment only compares OpenSQuILLA’s Pass@1 on Lite-80 and full-350. Both runs use the same adapter protocol, outer budget, and SWE-bench evaluator, and we measure approximation quality by the percentage-point gap between the Lite-80 rate and the full-350 rate.

Runtime configuration.
All experiments use the same outer runtime configuration. Each instance runs in its SWE-bench evaluation image, with the repository checkout located at /testbed. The instantiated task prompt, patch collector, evaluator, and aggregation code are shared across all claws and models. A per-instance wall-clock timeout of 3600 seconds, one run per instance, and worker concurrency fixed at 3. Experiments run on a 16-core CPU server with 61 GiB of memory and no local GPU; all model inference is performed through remote APIs.

Adapter diagnostic.
Beyond the main experiments, we run a bare-vs-full adapter diagnostic with GLM 5.1. Both conditions use the same full-350 workload and SWE-bench evaluator. The bare adapter provides only minimal Docker access and fairness restrictions, and asks the model to output a unified diff directly. The full adapter uses workspace preparation, the shared prompt, Git-based patch extraction, and patch cleaning from our protocol. This diagnostic quantifies the effect of the complete adapter on scorable evaluation, and should not be interpreted as a single-component ablation.

Leak-fix evaluation protocol.
The main experiments use results after cleaning future-commit visibility. Specifically, for the seven non-Python SWE-bench-Multilingual task languages, each instance preparation removes reachable Git history later than base_commit and then runs under the same adapter protocol. The Python portion comes from SWE-bench-Verified-Mini and is not affected by this Multilingual container issue. Except for the before/after cleanup comparison reported in §5.3, all Multilingual results in the following tables and figures use the cleanup setting.

5 Results

Except for the Lite held-out validation, all main results below report single-run aggregates on the full 350 instances, with worker concurrency fixed at 3. Unlike SWE-bench-style tables that report only resolved rate, we also report Total Cost, mean wall-clock duration, token usage, turn count, and Cache Hit Rate, so coding ability and practical evaluation cost can be interpreted in the same coordinate system. For OpenClaw ×\times GLM 5.1, we use the cost and cache accounting from the 9-model leak-fix result table; for OpenClaw ×\times Qwen 3.6-flash, we use the cache-fixed 5-claw cross table and add the mean turn count.

5.1 The Adapter Makes a General Agent Scorable

We first test whether the adapter is merely an engineering wrapper or a necessary condition for OpenClaw to be reliably scored by SWE-bench. Table 1 compares the same GLM 5.1 backbone under the bare adapter and the full adapter. The bare adapter can place OpenClaw in the SWE-bench Docker environment and send the task, but still asks the model to write a unified diff directly in its final response. The full adapter instead lets the model edit repository files through tools and has the runner export the patch from Git state.

Table 1: Diagnostic comparison between the bare adapter and the full adapter. Both use the same GLM 5.1 backbone and the full-350 workload; the bare adapter is a minimal directly scorable baseline, not a component ablation of the full adapter. Apply Failed is the fraction of instances whose submitted patch cannot be applied to the repository by the SWE-bench evaluator.

Configuration
Resolved
Pass@1
Apply Failed

Bare adapter
67/350
19.1
69.1%

Full adapter
257/350
73.4
<1.5%<1.5\%

The results show that minimal access is insufficient to create a reliable SWE-bench evaluation target. The bare adapter reaches only 19.1%19.1\% resolved rate. The main bottleneck is not that the model cannot edit code at all, but the fragility of directly generating unified-diff text: line numbers, context, hunk headers, or trailing newlines can make the patch fail to apply. The full adapter shifts the output responsibility from “the model writes patch text” to “the model edits repository files and the runner exports the patch,” reducing apply failures below 1.5%1.5\% and raising resolved rate to 73.4%73.4\%. The following experiments therefore measure model and claw differences under a unified scoring contract, rather than testing whether a native agent can hand-write a SWE-bench-compatible diff.

5.2 Variation Along the LLM Axis

To isolate the contribution of the LLM, we fix OpenClaw as the reference claw and sweep nine models on the full 350-instance set. Table 2 reports aggregate results. The highest resolved rate is achieved by GPT 5.5, at 78.0%78.0\% (273/350), followed by Claude Opus 4.7 at 77.1%77.1\% (270/350). The lowest cell is Seed 2.0-mini, at 48.6%48.6\% (170/350). Thus, under the same OpenClaw scaffold, changing only the model produces a 29.429.4 pp Pass@1 spread, confirming that model choice remains a major source of coding-agent performance.

Accuracy ranking, however, is not cost ranking. GPT 5.5 has the highest Pass@1, but its full 350-instance run costs $​1399.1\mathdollar 1399.1; Claude Opus 4.7 is only 0.90.9 pp lower, with cost $​1082.0\mathdollar 1082.0. By contrast, DeepSeek-V4 Pro reaches 71.7%71.7\% Pass@1 at total cost $​81.3\mathdollar 81.3, while DeepSeek-V4 Flash reaches 70.3%70.3\% at only $​8.2\mathdollar 8.2. Qwen 3.6-flash reaches 66.0%66.0\% Pass@1 at $​71.5\mathdollar 71.5; GLM 5.1 reaches 73.4%73.4\% under cache-fixed cost accounting at $​277.0\mathdollar 277.0. These results show that cost-aware reporting is not an auxiliary log but a necessary dimension for interpreting benchmark results: similar resolved rates can correspond to evaluation costs that differ by orders of magnitude.

Table 2: LLM-axis variation: OpenClaw ×\times 9 models on the full 350-instance Claw-SWE-Bench. Cost is total API cost for the full run (USD); In/Out are total input/output tokens (millions); Turns is average turns; Cache is cache hit rate. Rows are sorted by Pass@1; the best Pass@1 and lowest Cost are in bold.

Model
Type
Resolved
Pass@1
Cost
Dur
