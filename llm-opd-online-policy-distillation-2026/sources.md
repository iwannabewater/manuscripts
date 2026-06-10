# 大模型 OPD 技术概览 2026：来源说明

证据复核时间：2026-06-12 01:24，北京时间。公开材料覆盖口径截至 2026-06-10。本文把 OPD 译作“在线/在策略蒸馏”，对应当前论文和技术报告中更常见的 on-policy distillation。

## 证据分层

| 等级 | 含义 | 使用方式 |
|---|---|---|
| A | 原始论文、官方技术报告、官方模型卡或官方仓库说明 | 可支撑定义、算法机制、实验结果和厂商自述训练流程 |
| B | 研究机构博客、综述论文、社区复现材料 | 可支撑趋势、方法分类和工程解释，但不当作独立验证 |
| C | 媒体、社交平台、个人解读 | 仅用于发现线索；除非另有主来源，不进入正文事实链 |

## 主来源

| ID | 来源 | 日期 | 等级 | 本文使用的事实边界 |
|---|---|---:|---|---|
| S01 | Thinking Machines Lab, [On-Policy Distillation](https://thinkingmachines.ai/blog/on-policy-distillation/) | 2025-10-27 | B | OPD 的工程定义、student rollout 加 teacher token-level feedback 的训练闭环、reverse KL 实现和 Qwen3 表格复述。 |
| S02 | Qwen Team, [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) | 2025-05-14 | A | Qwen3 后训练中包含 distillation、RL 与 on-policy distillation 对比；Table 21 报告 OPD 在 Qwen3-8B 上以更低 GPU hours 取得更高 AIME 与 GPQA 指标。 |
| S03 | Song and Zheng, [A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626) | 2026-04-01, v3 2026-05-18 | B | OPD 作为解决 off-policy 静态模仿 exposure bias 的方法谱系；按反馈信号、teacher access 和 loss granularity 分类。 |
| S04 | Xiaomi MiMo Team, [MiMo-V2-Flash Technical Report](https://arxiv.org/abs/2601.02780) | 2026-01-06 | A | MiMo-V2-Flash 自述 Multi-Teacher On-Policy Distillation, MOPD, 由领域教师提供 dense token-level reward。 |
| S05 | GLM-5 Team, [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/abs/2602.15763) | 2026-02-17 | A | GLM-5 自述 On-Policy Cross-Stage Distillation 用于缓解多阶段 RL 后的能力遗忘，前阶段 checkpoints 作为 teachers。 |
| S06 | Yang et al., [Nemotron-Cascade 2](https://arxiv.org/abs/2603.19220) | 2026-03-19, v2 2026-03-22 | A | Nemotron-Cascade 2 自述 multi-domain on-policy distillation 从最强中间教师恢复 benchmark regressions 并维持收益。 |
| S07 | DeepSeek-AI, [DeepSeek-V4-Pro Model Card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-05 | A | DeepSeek-V4 公开模型卡自述 post-training 包含领域专家独立训练与 unified model consolidation via on-policy distillation。 |
| S08 | Li et al., [Fast and Effective On-policy Distillation from Reasoning Prefixes](https://arxiv.org/abs/2602.15260) | 2026-02-16 | A | Prefix OPD 只蒸馏学生生成前缀，报告匹配 full OPD 同时降低 2x-47x training FLOP。 |
| S09 | Jia et al., [Asymmetric On-Policy Distillation](https://arxiv.org/abs/2605.06387) | 2026-05-07, v3 2026-05-13 | A | AOPD 指出标准 OPD 的高方差、零优势区梯度消失和探索瓶颈，并给出非正优势区域的局部散度最小化。 |
| S10 | Xing et al., [Trust Region On-Policy Distillation](https://arxiv.org/abs/2606.01249) | 2026-05-31, v2 2026-06-03 | A | TrOPD 指出 teacher 和 student 分布差距大时 OPD 可能不稳定，并用 trust region、outlier estimation 与 teacher-prefix off-policy guidance 缓解。 |
| S11 | Zhao et al., [Self-Distilled Reasoner](https://arxiv.org/abs/2601.18734) | 2026-01-26, v3 2026-03-20 | A | On-policy self-distillation 方向，作为 teacher-free 或 self-teacher 路线的代表，不用于证明外部 teacher OPD 的效果。 |
| S12 | OpenClaw-RL Team, [OpenClaw-RL: Train Any Agent Simply by Talking](https://arxiv.org/html/2603.10165v1) | 2026-03 | A | Hindsight-Guided OPD 把 next-state signals 转为 token-level directional supervision，说明 OPD 向 agentic online learning 扩展。 |

## 口径与不确定性

- 本文不把“OPD 已经取代 RL”作为结论。更稳妥的判断是：OPD 正在成为 SFT、RLVR、RLHF 之后的一个高性价比补强阶段，尤其适合压缩、能力合并和纠错。
- 各论文使用的模型规模、teacher access、任务集、tokenizer、teacher logits 可得性和成本核算差异很大。跨论文的百分比和 FLOP 数字不能直接相加。
- 技术报告中的厂商 benchmark 属于官方自述，证据等级为 A 但不是第三方独立复核。
- DeepSeek-V4 的公开材料以 Hugging Face 模型卡和技术报告链接为主。本文只使用模型卡中可见的 post-training 描述，不引入社交媒体二次解读。
