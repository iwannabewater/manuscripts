---
source_url: https://arxiv.org/html/2603.28052
fetched_for: learn/canonical-article
source_check_date: 2026-06-20
---

[fetch] tier=local status=ok extractor=stdlib hint="install readability-lxml + html2text for cleaner output"
# Meta-Harness: End-to-End Optimization of Model Harnesses

> Source: https://arxiv.org/html/2603.28052

Back to arXiv

License: CC BY 4.0

arXiv:2603.28052v1 [cs.AI] 30 Mar 2026

Meta-Harness: End-to-End Optimization of Model Harnesses

Yoonho Lee

Stanford
&Roshen Nair

Stanford
&Qizheng Zhang

Stanford
&Kangwook Lee

KRAFTON

Omar Khattab

MIT
&Chelsea Finn

Stanford

Abstract

The performance of large language model (LLM) systems depends not only on model weights, but also on their harness: the code that determines what information to store, retrieve, and present to the model.
Yet harnesses are still designed largely by hand, and existing text optimizers are poorly matched to this setting because they compress feedback too aggressively: they are memoryless, condition only on scalar scores, or restrict feedback to short templates or summaries.
We introduce Meta-Harness, an outer-loop system that searches over harness code for LLM applications.
It uses an agentic proposer that accesses the source code, scores, and execution traces of all prior candidates through a filesystem.
On online text classification, Meta-Harness improves over a state-of-the-art context management system by 7.7 points while using 4×\times fewer context tokens.
On retrieval-augmented math reasoning, a single discovered harness improves accuracy on 200 IMO-level problems by 4.7 points on average across five held-out models.
On agentic coding, discovered harnesses surpass the best hand-engineered baselines on TerminalBench-2.
Together, these results show that richer access to prior experience can enable automated harness engineering.

Project page w/ interactive demo: https://yoonholee.com/meta-harness/

Optimized harness: https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact

Figure 1: (Left) On text classification, Meta-Harness outperforms the best prior hand-designed harnesses (ACE) and existing text optimizers (TTT-Discover, OpenEvolve), matching the next-best method’s final accuracy after just 4 evaluations. (Right) On TerminalBench-2, Meta-Harness outperforms all reported Claude Haiku 4.5 harnesses.

1 Introduction

Changing the harness around a fixed large language model (LLM) can produce a 6×\times performance gap on the same benchmark [46].
The harness—the code that determines what to store, retrieve, and show to the model—often matters as much as the model itself.
This sensitivity has led to growing interest in harness engineering, the practice of refining the code around an LLM to improve the overall system’s performance [35; 20; 9; 8].
But despite its importance, harness engineering remains largely manual: practitioners inspect failures, adjust heuristics, and iterate on a small number of designs.
In this paper, we ask whether this process itself can be automated.

A natural starting point is recent work on text optimization, since harness engineering also involves iteratively improving text and code artifacts using feedback from prior attempts [37; 38; 34; 25; 1].
However, these methods are poorly matched to harness engineering because they typically operate with short-horizon or heavily compressed feedback: some condition only on the current candidate [30; 50; 52], others rely primarily on scalar scores [34; 11], and others restrict feedback to short templates or LLM-generated summaries [1; 25].
This is a pragmatic scalability choice, not evidence that longer-range dependencies are uninformative.
Harnesses act over long horizons: a single choice about what to store, when to retrieve it, or how to present it can affect behavior many reasoning steps later.
Compressed feedback often removes the information needed to trace downstream failures to earlier harness decisions.
Across the tasks studied by several representative text optimizers, the available context per optimization step ranges from only 100 to 30,000 tokens (Table 1), far below the diagnostic footprint of harness search.
More broadly, work on retrieval and memory-augmented language models suggests that useful context should often be accessed adaptively rather than monolithically packed into a single prompt [27; 47; 36; 55].

Figure 2:

Meta-Harness search loop.
(1) An agent reads a filesystem containing all prior candidates’ source code, execution traces, and scores, and proposes a new harness.
(2) We evaluate the proposed harness on evaluation tasks.
(3) All logs (proposed code, reasoning traces, evaluation scores) are stored in the filesystem in a new directory, and the loop repeats.

Method

History

Log content

MTok/iter

OPRO [50]

Window

past (solution, score) pairs

0.0020.002

TextGrad [52]

Last

textual feedback on current artifact

0.0150.015

AlphaEvolve [34]

Window

program database + eval. scores

0.0220.022

GEPA [1]

Summary

reflective feedback from rollout traces

0.0080.008

Feedback Descent [25]

Summary

comparison + textual feedback

0.0120.012

TTT-Discover [54]

Window

prev. solution fragment

0.0260.026

Meta-Harness

Full

all logs and scores

10.010.0

Table 1:
Comparison of text optimization methods and their settings.
Each row represents a method collapsed across tasks.
Mtok/iter is our best estimate of the full context generated from one evaluation of a text artifact in the largest setting considered in each paper.
This paper considers settings that yield orders-of-magnitude more context per artifact evaluation.

We address this limitation with Meta-Harness, an agentic harness for optimizing harnesses via end-to-end search (Figure 2).
Its proposer is a coding agent, i.e., a language-model-based system that can invoke developer tools and modify code.
The choice of coding agent (rather than raw LLM) matters because the amount of experience quickly exceeds context limits, so the proposer must decide what to inspect and validate edits through direct interaction with the codebase.
Its key design choice is to expose full history through a filesystem, enabling selective diagnosis of raw prior code and execution traces rather than optimization from compressed per-candidate summaries.
For every previous candidate harness, the filesystem stores the source code, evaluation scores, and execution traces, which the proposer retrieves via standard operations such as grep and cat rather than ingesting them as a single prompt.
In practice, the proposer reads a median of 82 files per iteration in our most demanding setting, referencing over 20 prior candidates per step (Appendix A).
In the settings we study, a single evaluation can produce up to 10,000,000 tokens of diagnostic information, roughly three orders of magnitude beyond the largest feedback budgets used in prior text optimization settings (Table 1).

We evaluate Meta-Harness on online text classification, mathematical reasoning, and agentic coding.
On online text classification, harnesses discovered by Meta-Harness improve over Agentic Context Engineering (ACE, Zhang et al. [58]) by 7.7 points while using 4×\times fewer context tokens, and match the next-best text optimizer’s final performance after 6060 proposals with only four (Figure 1).
On retrieval-augmented math reasoning, a single discovered harness improves accuracy on 200 IMO-level problems by 4.7 points on average across five held-out models.
On TerminalBench-2, the discovered harness surpasses Terminus-KIRA and ranks #1 among all Haiku 4.5 agents.

2 Related Work

At a high level, Meta-Harness brings ideas from the broader literature on credit assignment and meta-learning [39; 45; 2; 16; 43; akyürek2023learningalgorithmincontextlearning] in a new regime enabled by recent advances in coding agents.
Rather than updating model weights, the system assigns credit at the harness level: it uses experience from past rollouts to deliberately reason about which steps and components are responsible for failures, then rewrites the external code that governs future behavior.
More specifically, the method lies at the intersection of several recent research threads; it is most directly related to work on adaptive access to external context, executable code search, and text optimization.

External memory and adaptive access.
Several prior works note the benefits of treating large knowledge sources or long inputs as external resources that a language model accesses adaptively, rather than consuming them in a single pass.
Specifically, retrieval-augmented generation [27], interleaved retrieval and reasoning [47], memory-based agents [36], or recursive language models [55] are mechanisms for adaptive access to external context.
Meta-Harness uses a similar access pattern, but in the more demanding setting of harness engineering, where the proposer selectively inspects a large external history of code, scores, and execution traces to improve context-management procedures themselves.

Executable code search. Recent methods search over executable code for functions, workflows, or agent designs.
Early work proposes using large models as mutation and crossover operators in evolutionary program search [26].
Later methods evolve designated functions within fixed program scaffolds [38], use meta-agents to program new agents from prior discoveries [19], or search over workflow graphs for agentic systems [57].
Another line of work searches over memory designs for continual-learning agents, where memory persists across task streams [56; 49].
In contrast, Meta-Harness searches over domain-specific harnesses, including prompt construction, retrieval, and state update strategies that reset between tasks.
Its outer loop is deliberately minimal: instead of relying on a fixed scaffold, an archive of prior discoveries, or a persistent memory mechanism, it gives the proposer unrestricted filesystem access to prior experience.
This lets the agent decide what information to inspect and enables search over full harness implementations rather than a predefined space of context-management procedures.

Text optimization methods. Meta-Harness is also closely related to methods such as ProTeGi, TextGrad, OPRO, GEPA, AlphaEvolve/OpenEvolve, and Feedback Descent, which iteratively improve prompts or other text artifacts using feedback from prior attempts [37; 30; 52; 50; 1; 34; 42; 25].
However, these methods are less well suited to harness engineering, where optimization targets a complete executable procedure, and the relevant environmental feedback is distributed across code, scores, and execution traces in a way that is hard to summarize up front.
Rather than reacting only to aggregate scores or summaries, the proposer in Meta-Harness can reason over failed examples and their execution traces to propose targeted edits.
See Table 1 for a comparison of problem scale considered in those papers and ours, and Figures 1 and 4 for a direct comparison with OpenEvolve, GEPA, and TTT-Discover in our problem setting.

3 Meta-Harness: A Harness for Optimizing Harnesses

This section describes Meta-Harness, our outer-loop procedure for searching over task-specific harnesses.
Meta-Harness is built on the idea that harness optimization benefits from allowing a proposer to selectively inspect prior code and execution traces via filesystem access, rather than optimizing from lossy summaries or an additional hand-designed search structure.
At a high level, it repeatedly proposes, evaluates, and logs new harnesses.

Meta-Harness is itself a harness in the broad sense (hence the name), since it determines what information the proposer model sees during search.
Unless otherwise noted, we use harness to refer to the task-specific programs being optimized.

Objective.
A harness is a stateful program that wraps a language model and determines what context the model sees at each step.
The goal is simple: find the harness that makes the underlying model perform best on the target task distribution.
Formally, let MM denote a fixed language model and 𝒳\mathcal{X} a task distribution.
For a harness HH and task instance x∼𝒳x\sim\mathcal{X}, we execute a rollout trajectory τ∼pM​(H,x)\tau\sim p_{M}(H,x).
The harness constructs prompts for MM, the model responds, and the harness updates its state after each interaction.
A task-specific reward function r​(τ,x)r(\tau,x) scores the trajectory.
The objective of harness optimization is to find the harness that maximizes the expected final reward:

H∗=arg​maxH⁡𝔼x∼𝒳,τ∼pM​(H,x)​r​(τ,x),H^{*}=\operatorname*{arg\,max}_{H}\mathbb{E}_{x\sim\mathcal{X},\tau\sim p_{M}(H,x)}\;r(\tau,x),

When multiple objectives are relevant (e.g., accuracy and context cost), we evaluate candidates under Pareto dominance and report the resulting frontier.
In practice, this search has traditionally been carried out by human engineers and researchers, who iteratively refine prompts, context-management rules, and tool-use logic by hand.

Meta-Harness search loop.
Meta-Harness uses a single coding-agent proposer with access to a growing filesystem 𝒟\mathcal{D} that serves as its feedback channel111Based on earlier exploration, we think this workflow only became practical recently, following major improvements in coding-agent capabilities around early 2026..
Here, a coding agent is a language-model-based system that can invoke developer tools and modify code.
Unlike prior systems that externalize the improvement logic in a hand-designed search loop, Meta-Harness delegates diagnosis and proposal to the coding agent itself: it decides which prior artifacts to inspect, which failure modes to address, and whether to make a local edit or a more substantial rewrite.
Equivalently, the proposer is not a raw next-token model operating on a fixed prompt assembled by the outer loop; it is an agent that retrieves information, navigates prior artifacts, and edits code as part of the search itself.
Each evaluated harness contributes a directory containing its source code, scores, and execution traces (such as prompts, tool calls, model outputs, and state updates).
The filesystem is typically far larger than the proposer’s context window, so the proposer queries it through terminal tools such as grep and cat rather than ingesting it as a single prompt.
At each iteration, the proposer first inspects prior code, scores, and execution traces, then reasons about likely failure modes before generating a new harness.

Meta-Harness maintains a population ℋ\mathcal{H} and a Pareto frontier over evaluated harnesses, but imposes no parent-selection rule: the proposer is free to inspect any prior harness and its execution trace when proposing new ones.
We run evolution for a fixed number of iterations and perform a final test-set evaluation on the Pareto frontier. This simplicity is deliberate: by leaving diagnosis and edit decisions to the proposer rather than hard-coding search heuristics, Meta-Harness can improve automatically as coding agents become more capable.
The proposer never sees test-set results; its only feedback comes from the search set, the subset of task instances used to evaluate candidate harnesses during search and generate the feedback signal for improvement, and from execution traces logged during those search runs.

Advantages of code-space search.
Harness optimization occurs in code space, where small changes to retrieval, memory, or prompt-construction logic can affect behavior many steps later, making local search heuristics poorly matched to the problem.
By inspecting execution traces, the proposer can often infer why a harness failed and which earlier design choices likely contributed to the failure, not just that it failed, as illustrated by the search trajectories in Appendices A and A.2. There, we see that the proposer reads broadly across prior code and logs, then uses those traces to identify confounded edits, isolate likely causal changes, and shift toward safer modifications after repeated regressions.
The proposer can therefore modify the harness at the level of algorithmic structure, ranging from changes to retrieval, memory, or prompt-construction logic to full program rewrites, rather than filling in templates or applying predefined mutation operators.
In practice, it often starts from a strong prior harness, but this is an emergent strategy rather than a hard-coded rule.
Although the search space is large, representing harnesses as programs provides a natural regularization bias: coding models tend to propose coherent algorithms rather than brittle, hard-coded solutions, which biases the search toward reusable context-management procedures.
This action space is closely aligned with the read–write–execute workflows on which frontier coding assistants are trained.

Practical implementation.
In our experiments, each harness is a single-file Python program that modifies task-specific prompting, retrieval, memory, and orchestration logic.
In our experiments, the proposer PP is Claude Code [4] with Opus-4.6.
The proposer is guided by a minimal domain-specific skill that describes where to write new harnesses, how to inspect previous harnesses and their execution traces, and what files it can and cannot modify.
The base model MM varies by domain and is always frozen; see Section 4 for details.
In our experiments, a typical run evaluates roughly 60 harnesses over 20 iterations.
We provide additional tips for implementing Meta-Harness in a new domain in Appendix D.

Algorithm 1  Meta-Harness outer loop over harnesses

1:Input: tasks 𝒳\mathcal{X}, LLM MM, proposer PP, iterations NN

2:Initialize: population ℋ\mathcal{H} ⊳\triangleright Initial set of valid harnesses

3:Initialize: filesystem 𝒟←∅\mathcal{D}\leftarrow\emptyset ⊳\triangleright stores code, scores, traces

4:for H∈ℋH\in\mathcal{H} do

5:  EH←Evaluate​(H,M,𝒳)E_{H}\leftarrow\textrm{Evaluate}(H,M,\mathcal{X})

6:  𝒟←𝒟∪{(H,EH)}\mathcal{D}\leftarrow\mathcal{D}\cup\{(H,E_{H})\}

7:for t=1​…​Nt=1\ldots N do

8:  Proposer PP queries filesystem 𝒟\mathcal{D} ⊳\triangleright inspects prior harnesses and scores

9:  Proposer PP proposes kk new harnesses {H1,…,Hk}\{H_{1},\dots,H_{k}\}

10:  for HH in {H1,…,Hk}\{H_{1},\dots,H_{k}\} do

11:   if HH passes interface validation then

12:     𝒟←𝒟∪{(H,Evaluate​(H,M,𝒳))}\mathcal{D}\leftarrow\mathcal{D}\cup\{(H,\textsc{Evaluate}(H,M,\mathcal{X}))\}

13:return Pareto frontier of harnesses stored in 𝒟\mathcal{D}

4 Experiments
