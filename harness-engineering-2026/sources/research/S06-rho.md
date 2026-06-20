---
source_url: https://arxiv.org/html/2606.05922
fetched_for: learn/canonical-article
source_check_date: 2026-06-20
---

[fetch] tier=local status=ok extractor=stdlib hint="install readability-lxml + html2text for cleaner output"
# Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference

> Source: https://arxiv.org/html/2606.05922

Back to arXiv

License: CC BY-NC-SA 4.0

arXiv:2606.05922v2 [cs.AI] 10 Jun 2026

Evolving Agents in the Dark:

Retrospective Harness Optimization via Self-Preference

Wenbo Pan1   Shujie Liu2   Chin-Yew Lin2   Jingying Zeng2   Xianfeng Tang2

Xiangyang Zhou2   Yan Lu2   Xiaohua Jia1

1City University of Hong Kong   2Microsoft Research Asia

Abstract

AI agents rely on a harness of skills, tools, and workflows to solve complex problems.
Continually improving this harness is essential for adapting to new tasks.
However, existing optimization methods typically require ground-truth validation sets, yet such labeled data is difficult to acquire in practical deployment settings.
To address this problem, we introduce Retrospective Harness Optimization (RHO), a self-supervised method that optimizes the agent harness using only past trajectories.
Specifically, RHO selects a diverse coreset of challenging tasks from past trajectories and re-solves them in parallel.
The agent analyzes these rollouts using self-validation and self-consistency, then generates candidate harness updates and selects the most effective one by its own pairwise self-preference.
We evaluate RHO across three diverse domains, spanning software engineering, technical work, and knowledge work.
Notably, a single optimization round improves the pass rate on SWE-Bench Pro from 59% to 78% without any external grading.
Furthermore, our analysis demonstrates that RHO effectively targets prior failure modes. As a result, the optimized harness alters the agent’s behavior patterns and sustains higher accuracy during long-horizon sessions.
Code is available at https://github.com/wbopan/retro-harness and the project website at https://paper-rho.wenbo.io.

Evolving Agents in the Dark:

Retrospective Harness Optimization via Self-Preference

Wenbo Pan1   Shujie Liu2   Chin-Yew Lin2   Jingying Zeng2   Xianfeng Tang2

Xiangyang Zhou2   Yan Lu2   Xiaohua Jia1

1City University of Hong Kong   2Microsoft Research Asia

1 Introduction

Figure 1: RHO versus validation-feedback harness optimization.
Validation-feedback methods iterate against a labeled validation set, whereas RHO optimizes from past trajectories in a single retrospective pass with no ground-truth labels.

A harness enables an AI agent to complete complex tasks by providing it with available skills, workflows, and tools.
One important research question is how to improve the harness continuously.
Specifically, after an agent is deployed, we aim to continually evolve its harness by learning from past experiences, which in turn improves its performance on future tasks.

Prior work has proposed various methods for evolving the agent harness (Zhou et al., 2022; Yang et al., 2023; Khattab et al., 2023; Yuksekgonul et al., 2024; Agrawal et al., 2025; Hu et al., 2024; Lee et al., 2026).
However, these methods rely on scoring against a validation set to guide the improvements.
In practical deployment scenarios, it is often difficult to collect a validation set that accurately estimates the distribution of future tasks to validate the updated harness.
On the other hand, the continuous operation of an agent naturally produces a rich set of trajectories from past tasks.
This leads to our central question. Can we improve the agent harness to enhance future performance when we only have access to past trajectories?

To address this problem, we propose Retrospective Harness Optimization (RHO), a self-supervised method that optimizes the harness through a retrospective analysis of past trajectories.
This method employs the agent’s internal self-preference over trajectories to guide the optimization process.
Figure 1 contrasts RHO with conventional validation-feedback optimization, which iterates against a labeled validation set.

Figure 2: The RHO pipeline. Coreset Selection picks a small, difficulty-diverse subset of past tasks with a determinantal point process (DPP). Group Rollout re-solves each task GG times and diagnoses within-trajectory failures (self-validation) and cross-trajectory disagreements (self-consistency). Harness Proposal samples NN candidate harnesses and keeps the one whose rollouts are most preferred over the baseline. No ground-truth labels are used.

Figure 2 illustrates this process.
Specifically, given a large set of past trajectories, RHO first selects a diverse and challenging coreset of tasks.
Then the agent re-attempts each task in the coreset multiple times to generate parallel trajectories.
Building on this, we extract two diagnostic signals, namely self-validation within a trajectory and self-consistency across parallel trajectories.
These signals are then used to instruct the generation of harness updates.
Finally, by using the agent’s pairwise self-preference, we select the most promising harness from the newly generated proposals.

We evaluate the effectiveness of RHO across three agent domains that span software engineering, technical work, and knowledge work.
RHO consistently improves the agent’s performance across all three domains.
Notably, by running a single round of retrospective harness optimization on software-engineering trajectories, we improve the pass rate on SWE-Bench Pro (Deng et al., 2025) from 59% to 78%, without depending on grading against a validation set.

Furthermore, we provide a detailed analysis on how the retrospective optimization process improves performance.
We observe that RHO designs specific skills and tools targeting typical failure modes encountered in past tasks. These components reshape the agent’s action patterns and help it sustain higher accuracy in long-horizon sessions.
Additionally, we quantitatively analyze the contributions of the diagnostic signals during the retrospective process.
This analysis demonstrates that each step in RHO progressively isolates signals that contribute to performance improvements.

Our contributions are as follows:

⋄\diamond

We propose retrospective harness optimization, which addresses the gap of improving the full harness (including memory, context, skills, and tools) exclusively from unlabeled trajectories.

⋄\diamond

We evaluate RHO across three scenarios and show that retrospective analysis consistently outperforms straightforward experience accumulation and surpasses validation-feedback-driven evolution under a comparable budget.

⋄\diamond

We provide a quantitative analysis of the impact of harness optimization on agent performance, showing that gathering effective improvement signals leads to targeted changes in the harness and optimizes the agent’s behavior.

2 Related Work

Harness optimization.

Harness optimization improves an agent by editing the prompts, program parameters, or workflow code that surround a fixed model.
One line optimizes prompts or pipeline parameters against a labeled metric, spanning LLM-as-optimizer search (Yang et al., 2023), declarative pipeline compilation (Khattab et al., 2023), textual-gradient updates (Yuksekgonul et al., 2024), and reflective prompt evolution (Agrawal et al., 2025).
A more agentic line lets a meta-agent rewrite the agent’s own code, where ADAS searches the space of agentic system designs (Hu et al., 2024) and Meta-Harness searches over harness code using the execution traces and scores of prior candidates (Lee et al., 2026).
Although these methods differ in the surface they edit, all of them steer the search with a labeled validation metric.
RHO departs from this paradigm, requiring no validation feedback and improving the harness in a single retrospective pass over unlabeled past trajectories.

Agent self-improvement.

A second line improves agents from their own past experience, using the agent’s self-judgment over trajectories in place of ground-truth labels.
Dynamic Cheatsheet maintains a self-curated memory of reusable strategies and code snippets at test time (Suzgun et al., 2025), while ReasoningBank distills generalizable reasoning strategies from self-judged successes and failures (Ouyang et al., 2025).
MemMA coordinates the memory cycle with multiple agents and repairs its memory bank against self-generated probe questions (Lin et al., 2026), Sleep-time Compute precomputes useful context offline before queries arrive (Lin et al., 2025), and M⋆ evolves the memory system itself as an executable program, discovering a task-specific memory harness per task family (Pan et al., 2026a).
Concurrent to our work, SkillOS instead trains a skill curator with reinforcement learning from outcome and judge rewards, updating a skill repository from accumulated experience (Ouyang et al., 2026).
These methods enrich an agent’s stored memory, context, or skill list while leaving the rest of the harness untouched.
RHO instead optimizes the full harness, including executable tools and instructions, rather than memory alone.
Appendix A gives a detailed comparison with related work.

3 Problem Setting

We define a harness hh as a persistent collection of tools, prompts, and skills that an agent can use to solve a task.
Given a task tt and a harness hh, an agent can attempt the task using a loop of reasoning, acting, and observing.
This multi-step process generates a trajectory τ\tau, which records the information read by the agent, its chain of thought, the tools used, and the final output.
We denote this execution process with a prompted agent operation as τ=solve​(h,t)\tau=\mathrm{solve}(h,t).
As the agent executes multiple tasks, it produces a dataset of trajectories 𝒟={τ1,τ2,…,τn}\mathcal{D}=\{\tau_{1},\tau_{2},\ldots,\tau_{n}\}.
These trajectories often contain instances of failure and useful insights that can be used to improve the harness.
Consequently, we ask whether the agent can retrospectively analyze past trajectories to optimize its harness and improve its future performance.
To quantify this, we define a latent utility function U​(t,τ)U(t,\tau) that measures the quality of a trajectory.
We formalize the optimization as a function optimize​(h,instruction)\mathrm{optimize}(h,\text{instruction}) that returns a modified harness h′h^{\prime}.
The goal is to find an optimal harness h⋆h^{\star} that maximizes the expected utility on future tasks:

h⋆=arg⁡maxh′⁡𝔼t,τ∼solve​(h′,t)​[U​(t,τ)].h^{\star}=\arg\max_{h^{\prime}}\;\mathbb{E}_{t,\,\tau\sim\mathrm{solve}(h^{\prime},t)}\left[U(t,\tau)\right].

Problem.
However, estimating this utility function accurately is difficult in practice.
To evaluate the true utility of a harness, we would need a representative validation set of future tasks and a mechanism to calculate the success rate of the agent using this specific harness.
In our setting, the function UU is latent and cannot be directly observed.

Our Approach.
Because the utility UU is latent, we cannot directly optimize it.
Instead, we substitute this latent utility with a self-preference estimator.
Specifically, we instruct the agent to compare multiple trajectories on the same task to compute a self-preference ranking.
We define a ranking function as (rank,rationale)=rank​(t,τ1,τ2,…,τm)(\text{rank},\text{rationale})=\mathrm{rank}(t,\tau_{1},\tau_{2},\ldots,\tau_{m}).
This function yields a preference ordering over the given trajectories and provides a rationale that explains why the agent prefers certain executions over others.
The next section details how we organize the operations of solving, ranking, and optimizing to improve the latent harness utility.

Algorithm 1  A single round of RHO. One backbone instantiates every operator (the difficulty judge\mathrm{judge}, solve\mathrm{solve}, optimize\mathrm{optimize}, and rank\mathrm{rank}), differing in its inputs and consulting no ground-truth label.

1:past trajectories 𝒟={(ti,τi)}i\mathcal{D}{=}\{(t_{i},\tau_{i})\}_{i} and harness h0h_{0}, with coreset size kk, group size GG, candidate count NN, and DPP weight θ\theta

2:updated harness h⋆h^{\star}

3:  Stage 1   Coreset Selection

4:ri←judge​(ti,τi)∀(ti,τi)∈𝒟r_{i}\leftarrow\mathrm{judge}(t_{i},\tau_{i})\ \ \forall\,(t_{i},\tau_{i})\in\mathcal{D}

5:𝒟core←DPP-Greedy​({(ti,ri)};θ,k)\mathcal{D}_{\mathrm{core}}\leftarrow\textsc{DPP-Greedy}\bigl(\{(t_{i},r_{i})\};\,\theta,k\bigr)

6:  Stage 2   Group Rollout

7:for t∈𝒟coret\in\mathcal{D}_{\mathrm{core}} in parallel do

8:  {τt,g}g=1G←solve​(h0,t)\{\tau_{t,g}\}_{g=1}^{G}\leftarrow\mathrm{solve}(h_{0},t)  ⊳\triangleright k×Gk{\times}G rollouts

9:  τt(0)←τt,1\tau_{t}^{(0)}\leftarrow\tau_{t,1}  ⊳\triangleright fixed baseline rollout

10:  It←rankval​(t,{τt,g})∪rankcon​(t,{τt,g})I_{t}\leftarrow\mathrm{rank}_{\mathrm{val}}\bigl(t,\{\tau_{t,g}\}\bigr)\cup\mathrm{rank}_{\mathrm{con}}\bigl(t,\{\tau_{t,g}\}\bigr)

11:end for

12:I←⋃t∈𝒟coreItI\leftarrow\bigcup_{t\in\mathcal{D}_{\mathrm{core}}}I_{t}

13:  Stage 3   Best-of-NN Harness Proposal

14:for j=1,…,Nj=1,\dots,N in parallel do

15:  hj←optimize​(h0,I)h_{j}\leftarrow\mathrm{optimize}\bigl(h_{0},\,I\bigr)

16:  τt(j)←solve​(hj,t)∀t∈𝒟core\tau_{t}^{(j)}\leftarrow\mathrm{solve}(h_{j},t)\ \ \forall\,t\in\mathcal{D}_{\mathrm{core}}  ⊳\triangleright N×kN{\times}k re-solves

17:  Sj←1k​∑t∈𝒟corerank​(t,τt(j),τt(0))S_{j}\leftarrow\tfrac{1}{k}\sum_{t\in\mathcal{D}_{\mathrm{core}}}\mathrm{rank}\bigl(t,\,\tau_{t}^{(j)},\,\tau_{t}^{(0)}\bigr)

18:end for

19:j⋆←arg⁡maxj⁡Sjj^{\star}\leftarrow\arg\max_{j}S_{j}

20:return hj⋆h_{j^{\star}} if Sj⋆>0S_{j^{\star}}>0, else h0h_{0}

4 Retrospective Harness Optimization

We propose RHO, a self-supervised method that improves a harness using only past trajectories.
Specifically, our pipeline (Figure 2) consists of three stages, namely coreset selection, group rollout, and best-of-NN harness proposal.
First, we select a representative subset of past tasks to define the optimization target.
Next, we sample a group of parallel rollouts for each task in this coreset and extract harness improvement signals from them.
Finally, we generate NN candidate harnesses based on these signals and retain the most preferred one using pairwise self-preference.
The full algorithm is detailed in Algorithm 1.

4.1 Coreset Selection

Given a large set of past trajectories, we need to extract the most critical signals to guide the harness optimization.
Optimizing the harness on every individual trajectory is computationally prohibitive, and it further risks diluting important signals with trivial ones.
To address this, we first select a coreset 𝒟core\mathcal{D}_{\mathrm{core}} from the full set 𝒟\mathcal{D} to represent the trajectories that require optimization the most.
Specifically, we require the coreset to capture both challenging and diverse scenarios.
This requirement encourages our optimization to cover a wide range of failure modes when addressing the most difficult problems.
To accomplish this, we introduce a Determinantal Point Process (DPP) kernel (Kulesza and Taskar, 2012) to rank all past trajectories by difficulty while satisfying a diversity constraint.
In practice, we employ a language model judge to analyze every trajectory τi\tau_{i} and extract a difficulty score rir_{i} alongside a textual description.
This description details the specific challenges of the problem and potential failure modes.
We then compute the embedding of this description and use the cosine similarity between embeddings as the similarity metric Si,jS_{i,j} for any two trajectories τi\tau_{i} and τj\tau_{j}.
By considering both the difficulty scores rr and the trajectory similarity matrix SS, we construct a kernel matrix

K=diag​(r~)​S​diag​(r~),K=\mathrm{diag}(\widetilde{r})\,S\,\mathrm{diag}(\widetilde{r}),

where r~i\widetilde{r}_{i} is a scaled version of the trajectory’s difficulty score rir_{i}:

r~i=(max⁡(ri,ϵ)/maxj⁡max⁡(rj,ϵ))α,\widetilde{r}_{i}=\big(\max(r_{i},\epsilon)\,/\,\max_{j}\max(r_{j},\epsilon)\big)^{\alpha},

α=θ/(2​(1−θ)).\alpha=\theta/\big(2(1-\theta)\big).

With this kernel function KK, DPP selects a subset YY with probability proportional to the kernel determinant det(KY)\det(K_{Y}), using parameter θ\theta to adjust the relative importance of difficulty and diversity via α\alpha. With θ=1\theta=1, the trajectories are ranked purely by difficulty and θ=0\theta=0 (uniform weights) ranked purely by similarity diversity.
Using θ=0.7\theta=0.7, we select kk trajectories into a coreset 𝒟core\mathcal{D}_{\mathrm{core}} that covers difficult, diverse failure modes for the subsequent stages.

4.2 Group Rollout

Inspired by previous work that uses relative advantages within a group as reward signals for reinforcement learning (Shao et al., 2024), we generate a set of trajectories by running GG parallel agent solves on each coreset task.
Subsequently, the agent compares these group trajectories to identify underperforming runs.
The agent then uses contrastive signals within the group to formulate instructions for optimizing the harness.
Specifically, we perform this self-preference analysis along two dimensions.

•

Self-validation (rankval\mathrm{rank}_{\mathrm{val}}). This dimension examines the correctness of the agent within each trajectory.
The agent inspects each trajectory against the required task and environment observations to determine whether the objective is efficiently achieved, exploiting the partial ability of models to recognize the limits of their own knowledge (Pan et al., 2025).
During this process, it flags incorrect tool invocations, false assumptions, and premature stopping. These flagged aspects are then extracted as areas of improvement for the relatively underperforming runs.

•

Self-consistency (rankcon\mathrm{rank}_{\mathrm{con}}). This dimension examines whether the behavior of the agent remains consistent across different trajectories.
Because low self-consistency typically indicates high uncertainty (Wang et al., 2022; Farquhar et al., 2024), we instruct the agent to analyze contradictions among trajectories.
The agent identifies consequential disagreements, such as divergent plans, tool sequences, or final answers, and generates optimization instructions to encourage more consistent behavior.

These rankval\mathrm{rank}_{\mathrm{val}} and rankcon\mathrm{rank}_{\mathrm{con}} analyses yield structured evaluations in JSON format, and for each task their union forms the improvement instruction It=rankval​(t,{τt,g})∪rankcon​(t,{τt,g})I_{t}=\mathrm{rank}_{\mathrm{val}}\bigl(t,\{\tau_{t,g}\}\bigr)\cup\mathrm{rank}_{\mathrm{con}}\bigl(t,\{\tau_{t,g}\}\bigr).
As a result, we merge {It}\{I_{t}\} across all tasks in the coreset to form the final harness improvement instructions.

Table 1: Held-out pass rate after harness optimization. The Architecture column indicates which harness surface each method edits. Δ\Delta is the absolute change over Vanilla Codex on the same held-out split.

Harness
SWE-Bench Pro
Terminal-Bench 2
GAIA-2

Method
Architecture
Pass
𝚫\boldsymbol{\Delta}
Pass
𝚫\boldsymbol{\Delta}
Pass
𝚫\boldsymbol{\Delta}

Vanilla Codex
None
0.59
n/a
0.71
