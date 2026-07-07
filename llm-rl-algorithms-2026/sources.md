# Sources
本课件截至 2026-06-26 整理。公式与算法解读以论文原文、公开技术报告和官方仓库为主要来源。论文或技术报告中的 benchmark 提升默认视为作者报告结果，除非正文明确说明独立复现。
| ID | Source | URL | Used for |
|---|---|---|---|
| TRPO | Trust Region Policy Optimization | https://arxiv.org/abs/1502.05477 | TRPO 约束策略改进与 PPO 背景 |
| GAE | High-Dimensional Continuous Control Using Generalized Advantage Estimation | https://arxiv.org/abs/1506.02438 | GAE 优势估计公式 |
| PPO | Proximal Policy Optimization Algorithms | https://arxiv.org/abs/1707.06347 | PPO clipped surrogate |
| DRHF | Deep Reinforcement Learning from Human Preferences | https://arxiv.org/abs/1706.03741 | 早期人类偏好奖励建模 |
| IGPT | Training language models to follow instructions with human feedback | https://arxiv.org/abs/2203.02155 | InstructGPT 的 SFT、RM、PPO 流程 |
| HH | Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback | https://arxiv.org/abs/2204.05862 | Anthropic helpful harmless RLHF |
| CAI | Constitutional AI: Harmlessness from AI Feedback | https://arxiv.org/abs/2212.08073 | RLAIF 与宪法反馈 |
| RRHF | RRHF: Rank Responses to Align Language Models with Human Feedback | https://arxiv.org/abs/2304.05302 | 排序式 SFT 类方法 |
| RAFT | RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment | https://arxiv.org/abs/2304.06767 | best-of-K 奖励排序微调 |
| SLIC | SLiC-HF: Sequence Likelihood Calibration with Human Feedback | https://arxiv.org/abs/2305.10425 | margin ranking 与 CE 正则 |
| DPO | Direct Preference Optimization | https://arxiv.org/abs/2305.18290 | DPO 推导、隐式奖励、BT 损失 |
| REST | Reinforced Self-Training | https://arxiv.org/abs/2308.08998 | ReST 生成、过滤、微调循环 |
| REMAX | ReMax: A Simple, Effective, and Efficient Reinforcement Learning Method for Aligning Large Language Models | https://arxiv.org/abs/2310.10505 | 贪心解码基线的 critic-free PG |
| IPO | A General Theoretical Paradigm to Understand Learning from Human Preferences | https://arxiv.org/abs/2310.12036 | IPO 与 ΨPO 框架 |
| KTO | KTO: Model Alignment as Prospect Theoretic Optimization | https://arxiv.org/abs/2402.01306 | KTO 二元反馈与前景理论价值函数 |
| GRPO | DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models | https://arxiv.org/abs/2402.03300 | GRPO 定义与数学推理 RL |
| RLOO | Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs | https://arxiv.org/abs/2402.14740 | RLOO 与 REINFORCE-style RLHF |
| ORPO | ORPO: Monolithic Preference Optimization without Reference Model | https://arxiv.org/abs/2403.07691 | odds-ratio preference objective |
| NASH | Nash Learning from Human Feedback | https://arxiv.org/abs/2403.08635 | 博弈与 mirror descent 视角 |
| REWARDBENCH | RewardBench: Evaluating Reward Models for Language Modeling | https://arxiv.org/abs/2403.13787 | 奖励模型评估风险 |
| SIMPO | SimPO: Simple Preference Optimization with a Reference-Free Reward | https://arxiv.org/abs/2405.14734 | 长度归一化 reference-free DPO 变体 |
| ONLINE-DPO | Online DPO | https://arxiv.org/abs/2406.05534 | 在线采样偏好优化 |
| TPO | Thought Preference Optimization | https://arxiv.org/abs/2410.10630 | thought-level preference |
| TULU3 | Tulu 3: Pushing Frontiers in Open Language Model Post-Training | https://arxiv.org/abs/2411.15124 | 开放后训练 recipe |
| RPP | REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Normalization | https://arxiv.org/abs/2501.03262 | 全局归一化 critic-free PPO |
| KIMI | Kimi k1.5: Scaling Reinforcement Learning with LLMs | https://arxiv.org/abs/2501.12599 | 长上下文、长思维链 RL recipe |
| R1 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | https://arxiv.org/abs/2501.12948 | R1-Zero、rule-based rewards、两阶段 RL |
| DAPO | DAPO: An Open-Source LLM Reinforcement Learning System at Scale | https://arxiv.org/abs/2503.14476 | Clip-Higher、Dynamic Sampling、token-level loss、overlong shaping |
| DRGRPO | Understanding R1-Zero-Like Training: A Critical Perspective | https://arxiv.org/abs/2503.20783 | Dr.GRPO 对长度偏置与难度偏置的修正 |
| VAPO | VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks | https://arxiv.org/abs/2504.05118 | value-model augmented PPO 与长 CoT 稳定化 |
| MINIMAX | MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention | https://arxiv.org/abs/2506.13585 | CISPO 与 off-policy 多轮更新 |
| GSPO | Group Sequence Policy Optimization | https://arxiv.org/abs/2507.18071 | sequence-level ratio 与 Qwen3 MoE 稳定训练 |
| NCA | Noise Contrastive Alignment of Language Models with Explicit Rewards | https://arxiv.org/abs/2402.05369 | NCA/InfoNCA 与显式标量奖励偏好优化 |
| BCO | Binary Classifier Optimization for Large Language Model Alignment | https://arxiv.org/abs/2404.04656 | 二元 thumbs-up/down 反馈优化 |
| SPIN | Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models | https://arxiv.org/abs/2401.01335 | self-play fine-tuning 与自我改进 |
| SPPO | Self-Play Preference Optimization for Language Model Alignment | https://arxiv.org/abs/2405.00675 | 自博弈偏好优化与 Nash 均衡 |
| SAPO | Self-Augmented Preference Optimization: Off-Policy Paradigms for Language Model Alignment | https://arxiv.org/abs/2405.20830 | off-policy self-augmented preference optimization |
| AOT | Distributional Preference Alignment of LLMs via Optimal Transport | https://arxiv.org/abs/2406.05882 | optimal transport 与 distribution-level preference alignment |
| APO | Anchored Preference Optimization and Contrastive Revisions | https://arxiv.org/abs/2408.06266 | anchored preference optimization 与 AI revisions |
| CALDPO | Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment | https://arxiv.org/abs/2412.14516 | implicit reward calibration |
| RAR | Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains | https://arxiv.org/abs/2507.17746 | rubric-based rewards beyond binary verifiers |
| TRGRPO | Token-Regulated Group Relative Policy Optimization for Stable Reinforcement Learning in Large Language Models | https://arxiv.org/abs/2511.00066 | token probability weighting for GRPO stability |
| SSPO | SSPO: Subsentence-level Policy Optimization | https://arxiv.org/abs/2511.04256 | subsentence-level ratio between token and sequence clipping |
| RLVRR | From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation | https://arxiv.org/abs/2601.18533 | reference-based reward chains for open-ended generation |
| DHPO | Orchestrating Tokens and Sequences: Dynamic Hybrid Policy Optimization for RLVR | https://arxiv.org/abs/2601.05607 | hybrid token-level and sequence-level importance ratios |
| BAPO | Buffer Matters: Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning | https://arxiv.org/abs/2602.20722 | off-policy buffer reuse and batch adaptation for RLVR |
| LUSPO | Length-Unbiased Sequence Policy Optimization: Revealing and Controlling Response Length Variation in RLVR | https://arxiv.org/abs/2602.05261 | length bias correction for GSPO-style sequence objectives |
| URLVR | How Far Can Unsupervised RLVR Scale LLM Training? | https://arxiv.org/abs/2603.08660 | unsupervised RLVR limits and confidence-correctness collapse risk |
| ARROL | Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR | https://arxiv.org/abs/2603.24840 | online rollout pruning for sparse group advantages |
| ASYMGRPO | Asymmetric Advantage Modulation Calibrates Entropy Dynamics in RLVR | https://arxiv.org/abs/2604.04894 | positive and negative advantage channels for productive entropy |
| MCPO | MCPO: Mastery-Consolidated Policy Optimization for Large Reasoning Models | https://arxiv.org/abs/2604.16972 | mastered-prompt consolidation and hinge-KL regularization |
| STRACE | Beyond Uniform Credit Assignment: Selective Eligibility Traces for RLVR | https://arxiv.org/abs/2605.05965 | critic-free selective eligibility traces and non-uniform credit |
| SCRL | From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning | https://arxiv.org/abs/2605.22074 | verifiable subproblem curriculum for hard reasoning credit assignment |
| SRAR | Step-wise Rubric Rewards for LLM Reasoning | https://arxiv.org/abs/2605.17291 | step-wise rubric attribution and per-step reward normalization |
| GRAIL | GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards | https://arxiv.org/abs/2606.04889 | gradient-saliency token reweighting without PRM labels |
| MAXPO | On Advantage Estimates for Max@K Policy Gradients | https://arxiv.org/abs/2606.06080 | Max@K policy gradients and leave-two-out baseline |
| ACPO | What are Key Factors for Updates in RL for LLM Reasoning? | https://arxiv.org/abs/2606.22570 | analysis-driven adaptive clipping from update dynamics |
| EXTRA | ExTra: Exploratory Trajectory Optimization for Language Model Reinforcement Learning | https://arxiv.org/abs/2606.24994 | novelty rewards and entropy-guided prefix regeneration |
| TAC | Transferability for General Reasoning: An Automated Curriculum for Multi-Domain RLVR | https://arxiv.org/abs/2606.25178 | transferability-aware curriculum for multi-domain RLVR |
| ROLLPIPE | RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning | https://arxiv.org/abs/2606.26997 | disaggregated rollout-training pipeline for on-policy RLVR systems |
