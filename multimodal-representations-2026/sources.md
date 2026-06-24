# Multimodal Representations 2026 Sources

Source check date: 2026-06-25 (Asia/Shanghai).

本文优先使用论文原文、正式会议页面、官方研究博客、官方文档和开源仓库。厂商产品页只用于说明公开能力与安全边界，不反推未披露架构。论文中的 benchmark 数字只表示该论文实验设置下的结果；预印本与工业自报材料统一标注为前沿信号，不写成已经形成共识的结论。

## Evidence levels

- **A**：正式会议或期刊论文，或论文最终公开版本。
- **B**：研究团队预印本，已公开方法、实验与局限，但未必完成同行评审。
- **C**：官方研究博客、产品文档或开源仓库，可证明公开能力、代码与工程边界。
- **D**：厂商自报 benchmark、产品效果或工业实践信号，只作趋势材料，不作独立验证。

| ID | Level | Source | URL | Main use |
|---|---|---|---|---|
| S01 | A | DeViSE: A Deep Visual-Semantic Embedding Model | https://papers.nips.cc/paper/5204-devise-a-deep-visual-semantic-embedding-model | 早期视觉语义嵌入、零样本分类与语义空间思想 |
| S02 | A | ViLBERT: Pretraining Task-Agnostic Visiolinguistic Representations | https://arxiv.org/abs/1908.02265 | 双流 Transformer、共同注意力与任务无关视觉语言预训练 |
| S03 | A | LXMERT: Learning Cross-Modality Encoder Representations | https://arxiv.org/abs/1908.07490 | 物体关系编码、语言编码、跨模态编码与多任务预训练 |
| S04 | A | UNITER: UNiversal Image-TExt Representation Learning | https://arxiv.org/abs/1909.11740 | 图文联合表示、条件遮盖与词区对齐 |
| S05 | A | Learning Transferable Visual Models From Natural Language Supervision | https://arxiv.org/abs/2103.00020 | CLIP、4 亿图文对、双塔对比学习与零样本迁移 |
| S06 | A | Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision | https://arxiv.org/abs/2102.05918 | ALIGN、十亿级噪声 alt-text、规模与噪声取舍 |
| S07 | A | Sigmoid Loss for Language Image Pre-Training | https://arxiv.org/abs/2303.15343 | SigLIP、pairwise sigmoid loss 与大 batch 之外的效率路线 |
| S08 | A | BLIP: Bootstrapping Language-Image Pre-training | https://arxiv.org/abs/2201.12086 | 图文理解与生成统一、caption bootstrapping |
| S09 | A | BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models | https://arxiv.org/abs/2301.12597 | 冻结视觉编码器、冻结 LLM、Q-Former 桥接 |
| S10 | A | Flamingo: a Visual Language Model for Few-Shot Learning | https://arxiv.org/abs/2204.14198 | interleaved 图文序列、Perceiver Resampler、少样本视觉语言任务 |
| S11 | A | Image as a Foreign Language: BEiT Pretraining for All Vision and Vision-Language Tasks | https://arxiv.org/abs/2208.10442 | BEiT-3、Multiway Transformer、统一 masked modeling |
| S12 | A | CoCa: Contrastive Captioners are Image-Text Foundation Models | https://arxiv.org/abs/2205.01917 | 对比损失与 captioning 损失合并、图文 foundation model |
| S13 | A | PaLI: A Jointly-Scaled Multilingual Language-Image Model | https://arxiv.org/abs/2209.06794 | 多语言图文生成接口、视觉与语言组件共同扩展 |
| S14 | B | Language Is Not All You Need: Aligning Perception with Language Models | https://arxiv.org/abs/2302.14045 | Kosmos-1、从头训练的多模态大模型、交错图文与 OCR-free NLP |
| S15 | A | Visual Instruction Tuning | https://arxiv.org/abs/2304.08485 | LLaVA、视觉指令数据、视觉编码器到 LLM 的连接器 |
| S16 | A | ImageBind: One Embedding Space To Bind Them All | https://arxiv.org/abs/2305.05665 | 图像作为枢纽绑定六种模态、跨模态检索与算术 |
| S17 | A | data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language | https://arxiv.org/abs/2202.03555 | 跨语音、视觉、语言的统一自监督 latent prediction |
| S18 | A | Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture | https://arxiv.org/abs/2301.08243 | I-JEPA、非生成式预测表征与语义遮盖策略 |
| S19 | B | Revisiting Feature Prediction for Learning Visual Representations from Video | https://arxiv.org/abs/2404.08471 | V-JEPA、视频特征预测与无文本视觉表征 |
| S20 | A | 4M: Massively Multimodal Masked Modeling | https://arxiv.org/abs/2312.06647 | 多输入多输出、离散 token 化与 any-to-any masked modeling |
| S21 | B | Chameleon: Mixed-Modal Early-Fusion Foundation Models | https://arxiv.org/abs/2405.09818 | mixed-modal early fusion、文本图像统一 token 序列 |
| S22 | B | Qwen2.5-VL Technical Report | https://arxiv.org/abs/2502.13923 | 动态分辨率、文档/图表/长视频理解与视觉 Agent 功能 |
| S23 | B | VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks | https://arxiv.org/abs/2410.05160 | MMEB、VLM 转 embedding model、跨任务多模态嵌入评测 |
| S24 | B/D | PinCLIP: Large-scale Foundational Multimodal Representation at Pinterest | https://arxiv.org/abs/2603.03544 | 推荐/检索系统中的工业多模态表征与 serving 约束 |
| S25 | A | MME: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models | https://arxiv.org/abs/2306.13394 | 感知/认知子任务与 MLLM 定量评测 |
| S26 | A | MMBench: Is Your Multi-modal Model an All-around Player? | https://arxiv.org/abs/2307.06281 | 双语多选评测、CircularEval 与综合能力划分 |
| S27 | A | MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark | https://arxiv.org/abs/2311.16502 | 大学级多学科题、专业图像类型与专家推理评测 |
| S28 | A | HallusionBench: An Advanced Diagnostic Suite | https://arxiv.org/abs/2310.14566 | 视觉幻觉、语言偏置和图像上下文推理诊断 |
| S29 | C/D | GPT-4V(ision) system card | https://openai.com/index/gpt-4v-system-card/ | 公开系统卡中的多模态风险、限制与安全边界 |
| S30 | C/D | Hello GPT-4o | https://openai.com/index/hello-gpt-4o/ | 原生文本、音频与图像交互的产品形态信号 |

## Conflicts and interpretation boundaries

- **共享向量空间不等于通用智能。** CLIP、ALIGN、SigLIP 和 ImageBind 证明共享嵌入空间能支撑检索、零样本分类和跨模态组合 [S05-S07, S16]；MMMU、HallusionBench 等评测说明，图文对齐强并不自动带来专业推理、空间定位或抗幻觉能力 [S27, S28]。
- **语言监督不是唯一方向。** CLIP/ALIGN 说明自然语言能提供开放词表监督 [S05, S06]；data2vec、I-JEPA、V-JEPA 说明 latent prediction 也能学习强表征，且不必依赖文本、负样本或重建像素 [S17-S19]。正文据此把“语言是最方便的接口”写成工程判断，不写成理论必然。
- **早融合、晚融合和桥接模块没有绝对优劣。** ViLBERT、LXMERT、UNITER 走跨注意力联合编码 [S02-S04]；CLIP/ALIGN 走双塔 [S05, S06]；BLIP-2、Flamingo、LLaVA 走冻结骨干加连接器或 resampler [S09, S10, S15]；Chameleon、4M 走统一 token 或 any-to-any 路线 [S20, S21]。正文按任务延迟、生成需求和数据形态给取舍，不写排名。
- **厂商能力页不能反推内部表征。** GPT-4V system card 和 GPT-4o 产品页只证明公开交互形态和风险披露 [S29, S30]；正文不根据产品体验推断未公开架构。
- **2026 年工业预印本是趋势信号。** PinCLIP 说明多模态表征进入推荐/检索生产系统时要处理训练目标与 serving 效率冲突 [S24]，但它是单公司场景，不等同于所有推荐系统的通用最优方案。

## Deliberately excluded claims

- 不声称多模态模型“理解世界”已经解决；文中只讨论表征如何把不同观测映射到可计算接口。
- 不把任一 benchmark 的排名写成模型真实能力的完整证明。
- 不声称视觉语言模型可以可靠替代 OCR、检测器、检索系统或专业标注链路；是否替代取决于误差成本、可解释性和延迟预算。
- 不把闭源模型的公开产品能力写成已验证的架构结论。
