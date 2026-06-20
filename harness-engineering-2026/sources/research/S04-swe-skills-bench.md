---
source_url: https://arxiv.org/html/2603.15401
fetched_for: learn/canonical-article
source_check_date: 2026-06-20
---

[fetch] tier=local status=ok extractor=stdlib hint="install readability-lxml + html2text for cleaner output"
# SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?

> Source: https://arxiv.org/html/2603.15401

Back to arXiv

License: arXiv.org perpetual non-exclusive license

arXiv:2603.15401v1 [cs.SE] 16 Mar 2026

SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?

Tingxu Han 111Work done during a research visit at MBZUAI.

Nanjing University

Mohamed bin Zayed University of Artificial Intelligence

txhan@smail.nju.edu.cn

&Yi Zhang

South China University of Technology

202330580551@mail.scut.edu.cn

&Wei Song

The University of New South Wales

wei.song1@unsw.edu.au

&Chunrong Fang 333Corresponding Author.

Nanjing University

fangchunrong@nju.edu.cn

&Zhenyu Chen

Nanjing University

zychen@nju.edu.cn

&Youcheng Sun

Mohamed bin Zayed University of Artificial Intelligence

youcheng.sun@mbzuai.ac.ae

&Lijie Hu 333Corresponding Author.

Mohamed bin Zayed University of Artificial Intelligence

lijie.hu@mbzuai.ac.ae

Abstract

Agent skills, structured procedural knowledge packages injected at inference time, are increasingly used to augment LLM agents on software engineering tasks.
However, their real utility in end-to-end development settings remains unclear.
We present SWE-Skills-Bench, the first requirement-driven benchmark that isolates the marginal utility of agent skills in real-world software engineering (SWE).
It pairs 49 public SWE skills with authentic GitHub repositories pinned at fixed commits and requirement documents with explicit acceptance criteria, yielding approximately 565 task instances across six SWE subdomains.
We introduce a deterministic verification framework that maps each task’s acceptance criteria to execution-based tests, enabling controlled paired evaluation with and without the skill.
Our results show that skill injection benefits are far more limited than rapid adoption suggests: 39 of 49 skills yield zero pass-rate improvement, and the average gain is only +1.2%+1.2\%. Token overhead varies from modest savings to a 451%451\% increase while pass rates remain unchanged. Only seven specialized skills produce meaningful gains (up to +30%+30\%), while three degrade performance (up to −10%-10\%) due to version-mismatched guidance conflicting with project context.
These findings suggest that agent skills are a narrow intervention whose utility depends strongly on domain fit, abstraction level, and contextual compatibility.
SWE-Skills-Bench provides a testbed for evaluating the design, selection, and deployment of skills in software engineering agents.
SWE-Skills-Bench is available at https://github.com/GeniusHTX/SWE-Skills-Bench.

††footnotetext: Pre-print with preliminary results, work in progress.

1 Introduction

Figure 1: Illustration of how agent skills are used in a software engineering workflow. Given a natural-language requirement, the LLM-based agent selects the most relevant skill from its skill library, including skills such as writing code, running tests, debugging, creating pull requests, and deploying, and injects it into the context window. The agent then executes a series of SWE actions to produce the final software artifacts (such as code) that fulfill the requirement.

LLM-based agents have been increasingly deployed across a wide range of software engineering (SWE) tasks, from automated code generation and bug fixing Jimenez et al. (2024) to CI/CD pipeline configuration and infrastructure management Yang et al. (2024); Song et al. (2025).
Agent Skills are structured markdown packages that encode procedural knowledge,standard operating procedures, code templates, and domain conventions,for consumption by LLM-based agents Anthropic (2025b); Fang et al. (2025); Wang et al. (2024a, b); Xu and Yan (2026).
At inference time, a skill is simply injected into the agent’s context window as a reference document.
Unlike fine-tuning or retrieval-augmented generation, no model modification or external retrieval pipeline is required (Figure 1 illustrates how agent skills work given a software engineering task).
The ecosystem has grown explosively: over 84,192 skills were created in just 136 days Li et al. (2026).

Despite this rapid adoption, no existing benchmark evaluates SWE skills in real-world software development scenarios.
TerminalBench Merrill and others (2026) evaluates CLI tasks in multi-file repositories, but does not include a skill-augmentation condition.
HumanEval Chen and others (2021) and BigCodeBench Zhuo and others (2025) target self-contained function completion without multi-file context or skill augmentation.
SkillsBench Li et al. (2026) is the first cross-domain benchmark to evaluate agent skills as first-class artifacts under paired skill conditions and deterministic verification. However, it is not specifically designed for software engineering: SWE constitutes only 16 of its 84 tasks, and its primary goal is to measure broad cross-domain skill efficacy rather than requirement satisfaction in real-world development workflows.

A principled benchmark for SWE skill utility must answer a deceptively simple question: Does the skill help the agent satisfy the task’s requirements?
Software engineering is inherently requirement-driven Sommerville (2015); Zave (1997); Pohl (2010): a task succeeds when every acceptance criterion stated in its specification is met, and unit tests serve as the executable encoding of those criteria.
We therefore adopt a requirement-driven evaluation methodology: each task is anchored to a requirement document that defines scope and acceptance criteria, and deterministic verifiers based on unit tests are systematically derived from those criteria, establishing full traceability from requirements to test verdicts.

Building on this methodology, we present SWE-Skills-Bench, a benchmark designed to isolate the marginal utility of agent skills for software engineering.
We curate 49 SWE skills from public repositories, pair each with an authentic GitHub project pinned at a fixed commit, and evaluate under controlled with-skill vs. without-skill conditions.
All task instances are verified by deterministic, execution-based checks with no reliance on LLM-as-judge evaluation.

Our main contributions are as follows:

•

Benchmark. We build SWE-Skills-Bench, a benchmark of 49 real-world SWE skills with ∼11{\sim}11 task instances per skill (∼565{\sim}565 total). Tasks are sourced from public skill repositories and evaluated on fixed-commit GitHub projects in containerized environments.

•

Requirement-driven test harness. We design an automated unit-testing mechanism that translates each SWE requirement into executable test cases, deterministically verifying whether the specified requirement is fulfilled under both with-skill and without-skill conditions.

•

Empirical findings. 1 Skill injection yields limited marginal gains: 39 of 49 skills produce ΔP=0\Delta_{P}=0, and the average pass-rate improvement is a modest +1.2%+1.2\%.
2 Token overhead is decoupled from correctness: even among skills with zero delta, the token overhead ratio ρ\rho ranges from −78%-78\% to +451%+451\%, indicating that skills reshape the agent’s reasoning path without necessarily improving outcomes.
3 A small subset of 7 skills encoding specialized procedural knowledge—financial risk formulas, cloud-native traffic management, and GitLab CI patterns—delivers meaningful gains up to +30%+30\%.
4 Three skills produce negative deltas (up to −10%-10\%) when their version-specific conventions conflict with the target project’s framework, demonstrating that skill injection carries a structural risk of context interference.
These results establish that SWE skill utility is highly domain-specific and context-dependent, favoring targeted skill design over blanket adoption.

2 Related Benchmarks & Datasets

We organize related work into two threads: SWE- and Skill-related benchmarks.
Generally, SWE-related benchmarks does not include skills in their evaluation, Skill-related benchmarks does focus on SWE tasks.
To the best of our knowledge, we are the first benchmark to evaluate agent skills in software engineering.
Table 1 summarizes the key differences.

SWE-related Benchmarks.
This line of work can be further divided into SWE real-world benchmarks and code generation benchmarks.
SWE real-world benchmarks focus on realistic, project-level software engineering tasks with execution-based verification.
SWE-Bench Verified Jimenez et al. (2024) is a human-validated subset of 500 instances from SWE-Bench, drawn from 12 Python repositories and evaluated via fail-to-pass tests.
TerminalBench Merrill and others (2026) evaluates agents on 200 realistic CLI tasks in containerized environments and provides methodological inspiration for our evaluation setup. However, these benchmarks do not isolate the marginal benefit of injecting procedural skill documents.
Code generation benchmarks, in contrast, mainly evaluate models on self-contained coding problems (often algorithmic or snippet-level) without full project context. HumanEval Chen and others (2021) comprises 164 hand-crafted programming challenges at the function level, and therefore does not capture multi-file reasoning, dependency management, or end-to-end SWE workflows.

Skills Benchmarks.
SkillsBench Li et al. (2026) takes an important first step toward benchmarking skills as first-class artifacts by comparing agent performance across different skill conditions. Nevertheless, it is not SWE-specific: software engineering forms only a limited subset of its task suite, and the benchmark is not designed around the central success criterion in real-world development—whether explicit requirements are satisfied in repository-grounded workflows. Our work addresses this gap by constructing a requirement-driven benchmark focused exclusively on SWE, where each skill is paired with fixed-commit repositories, explicit requirements, and deterministic execution-based verification.

Table 1: Comparison of SWE-Skills-Bench with existing benchmarks. “Skill Cond.” indicates whether the benchmark includes agent skills. “Det. Verifier” indicates whether deterministic (non-LLM) verification is included. “SWE-Focused” indicates whether the benchmark is specifically designed for software engineering tasks.

Benchmark
Size
Skill Cond.
Real Projects
Det. Verifier
SWE-Focused

SWE-Bench Verified Jimenez et al. (2024)

500
None
Yes
Yes
Yes

TerminalBench Merrill and others (2026)

200
None
Yes
Yes
Yes

HumanEval Chen and others (2021)

164
None
No
Partial
No

SkillsBench Li et al. (2026)

84
Yes
Yes
Yes
Partial

SWE-Skills-Bench
565
Yes
Yes
Yes
Yes

Figure 2: The distribution of the curated skills and generated tasks.

Figure 3: Overview of the SWE-Skills-Bench construction pipeline. We begin with 84,192 public skills and narrow them down through three filtering stages: category selection, semantic filtering, and feasibility screening. This process yields 49 SWE skills (Stage 1). Next, for each skill, we identify a matching GitHub project and generate 565 task instances of the form (R,E,P,S)(R,E,P,S) (Stage 2). For each criterion in the requirements document PP, we build deterministic verifiers using pytest unit tests (Stage 3). Finally, we run a paired evaluation that compares agent performance with and without the SKILL.md file, allowing us to measure the effectiveness of the skill (Stage 4).

3 SWE-Skills-Bench Construction

Constructing SWE-Skills-Bench requires answering three key questions in sequence: which skills to benchmark, how to pair each skill with authentic task instances, and how to verify that the stated requirements are fulfilled.
Our pipeline proceeds in four stages (Figure 3): (1) curating a representative set of SWE skills from large public repositories, (2) generating task instances by pairing each skill with a fixed-commit GitHub project and a requirement document, (3) designing deterministic verifiers that are traceable to the acceptance criteria in each requirement document.

3.1 Skill Curation

The skill ecosystem is vast (84,192 skills created in 136 days Li et al. (2026)) but highly heterogeneous in quality, scope, and evaluability. We curate a deterministic, unit-testable subset through a three-stage filtering pipeline. First, we scan the mcpmarket category leaderboard and select six of the nine core categories that best align with software-engineering workflows and are amenable to unit-test evaluation: Developer Tools, Security & Testing, API Development, Data Science & ML, Deployment & DevOps, and Analytics & Monitoring. Second, we apply semantic filtering to exclude generative or subjective skills, retaining only those that target concrete SWE actions such as fix, build, and develop. Third, we exclude candidates whose associated repositories are prohibitively large or incur high environment and setup costs. This pipeline yields 49 skills distributed across the six categories: Deployment & DevOps (13), Analytics & Monitoring (12), API Development (10), Data Science & ML (9), Security & Testing (4), and Developer Tools (1).
Figure 2(a) illustrates the distribution.

Figure 4: The pipeline of task instance generation.

3.2 Task Instance Generation

As shown in Figure 4, for each curated skill ss, we construct approximately 10 task instances following a three-step procedure.

Project matching. We identify an authentic, open-source GitHub project whose technology stack aligns with the skill’s domain. The repository is pinned at a fixed commit to ensure reproducibility. Note that we also create a docker container for running each project.

Requirement authoring.
Each requirement PP is authored to be specific to its target repository and skill-triggering conditions. To maximize structural clarity and eliminate ambiguity, every PP adheres to a standardized template comprising: (i) Background, providing the necessary task context; (ii) Requirement, defining the core objective; (iii) File Operations, specifying the files to be modified or created; and (iv) Acceptance Criteria, offering deterministic success metrics.
Figure 7 illustrates the prompt utilized to author the requirement and Figure 8 an example of the generated requirement.

Skill placement. During the container preparation phase, the system removes the .claude/skills directory from the repository to eliminate interference from pre-existing skills. The activation of skill SS is governed by a file-level injection mechanism: the skill document SS is copied into the ~/.claude directory only when the experimental condition requires its use; otherwise, it is omitted. The agent automatically detects and integrates any skills present in this environment. Importantly, the requirement document PP never references SS, ensuring that the agent’s behavior is governed strictly by the physical presence of the skill configuration.

Totally, for each skill, we generate around 10 instances where detailed distributions in Figure 2(b).

3.3 Requirement-driven Verification

The core principle of SWE-Skills-Bench is requirement-driven verification. Rather than relying on subjective judgments, we convert every acceptance criterion in the requirement document PP into objective, deterministic tests, ensuring that each test outcome is directly traceable to a specific requirement.
We provide PP (together with repository metadata such as repo path, language, and available test commands) to a fixed “professional test engineer” prompt template, which instructs the model to (i) enumerate testable behaviors from each acceptance criterion, (ii) instantiate representative and edge-case scenarios, and (iii) encode them into a deterministic pytest test file with strong discriminative power (i.e., tests must run the produced code and verify concrete outputs/structures rather than keyword-level heuristics). The prompt also enforces structural constraints such as a minimum number of test cases and per-test docstrings.
The prompt template is shown in Figure 6.

Concretely, for each instance we create a container from a base image, clone the target repository into the container workspace, and complete environment setup. We then pass the task document (i.e., the requirement document PP) through the above prompt template to drive test generation, and use the task document as the prompt to Claude Code for implementation.

3.4 Task Formulation

Each task instance is a tuple (R,E,P,S)(R,E,P,S): a GitHub repository RR pinned at a fixed commit and the corresponding containerized running environment, a natural-language requirement document PP that specifies tasks, and optionally a skill document SS. The agent (claude code specifically) must produce code changes, configuration files, or execution artifacts that satisfy the requirements in PP given the code repository RR and environment EE.

In our evaluation methodology, every acceptance criterion in the requirement document PP is mapped to deterministic verifier, establishing full traceability from requirements to test verdicts.

4 Results of SWE-Skills-Bench

Table 2: Evaluation results across all 49 skills. Pass+\text{Pass}^{+} and Pass−\text{Pass}^{-} denote pass rates with and without skill injection, respectively. Δ​P\Delta P is the skill utility delta, C+C^{+} and C−C^{-} are average token costs, ρ\rho is the token overhead ratio, and CE\mathrm{CE} is cost efficiency. Best viewed in color.

Skills

#\#Tasks

Pass+\textbf{Pass}^{+}
Pass−\textbf{Pass}^{-}
𝚫​𝑷\boldsymbol{\Delta P}
𝑪+\boldsymbol{C^{+}}
𝑪−\boldsymbol{C^{-}}
𝝆\boldsymbol{\rho}
CE

add-uint-support
12
100.0%
100.0%
0.0%
880K
414K
+112.6%
—

analytics-events
10
100.0%
100.0%
0.0%
321K
157K
+104.6%
—

analyze-ci
11
100.0%
100.0%
