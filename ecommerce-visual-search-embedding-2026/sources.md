# E-commerce Visual Search Embedding 2026 Sources

Source check date: 2026-07-05 (Asia/Shanghai).

本文优先使用论文原文、正式会议页面、官方研究博客、官方文档和开源仓库。厂商产品页只用于说明公开能力与安全边界，不反推未披露架构。论文中的 benchmark 数字只表示该论文实验设置下的结果；预印本与工业自报材料统一标注为前沿信号，不写成已经形成共识的结论。

## Evidence levels

- **A**：正式会议或期刊论文，或论文最终公开版本。
- **B**：研究团队预印本，已公开方法、实验与局限，但未必完成同行评审。
- **C**：官方研究博客、产品文档或开源仓库，可证明公开能力、代码与工程边界。
- **D**：厂商自报 benchmark、产品效果或工业实践信号，只作趋势材料，不作独立验证。

## Method

本报告采用一手材料研究法。核心材料包括会议工业论文、作者技术报告或预印本、公司官方工程说明、上市公司监管披露。检索后逐篇核对摘要、方法、实验范围和线上声明，再按公司与技术方向交叉整理；结构化映射见 `data/source-map.tsv` 与 `data/pipeline-map.tsv`。

论文中的线上提升均按论文所述场景引用。不同平台的业务目标、流量分配、对照组和统计方法未必相同，指标不能横向排序。预印本出现的部署或收益表述，正文均标为作者报告，不作独立验证后的事实陈述。

## Primary Sources

| ID | Level | Source | URL | Main use |
|---|---|---|---|---|
| S01 | A | Representation Learning with Contrastive Predictive Coding | https://arxiv.org/abs/1807.03748 | InfoNCE 对比学习目标函数来源 |
| S02 | A | Distinctive Image Features from Scale-Invariant Keypoints (SIFT) | https://link.springer.com/article/10.1023/B:VISI.0000029664.99615.94 | 手工局部特征与倒排索引传统方法 |
| S03 | A | FaceNet: A Unified Embedding for Face Recognition and Clustering | https://arxiv.org/abs/1503.03832 | Triplet loss 与度量学习范式 |
| S04 | A | Learning Transferable Visual Models From Natural Language Supervision (CLIP) | https://arxiv.org/abs/2103.00020 | 图文对齐、对比学习与共享向量空间 |
| S05 | A | Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision (ALIGN) | https://arxiv.org/abs/2102.05918 | 噪声 alt-text 规模化图文对齐 |
| S06 | A | The Design and Implementation of a Real Time Visual Search System on JD E-commerce Platform | https://arxiv.org/abs/1908.07389 | 电商图搜工业系统 pipeline 与工程权衡 |
| S07 | A | Sigmoid Loss for Language Image Pre-Training (SigLIP) | https://arxiv.org/abs/2303.15343 | Pairwise sigmoid loss 与训练效率 |
| S08 | A | Scaling Cross-Domain Content-Based Image Retrieval for E-commerce Snap and Search Application | https://arxiv.org/abs/2204.11593 | 跨域 CBIR 与域间差异问题 |
| S09 | A | Graph Convolutional Neural Networks for Web-Scale Recommender Systems (PinSage) | https://arxiv.org/abs/1806.01973 | 图嵌入召回与行为协同信号 |
| S10 | B | KARMA: Knowledge-Action Regularized Multimodal Alignment for Personalized Search at Taobao | https://arxiv.org/abs/2603.22779 | 多模态对齐进入个性化搜索主链路 |
| S11 | B | AIGQ: An End-to-End Hybrid Generative Architecture for E-commerce Query Recommendation | https://arxiv.org/abs/2603.19710 | 混合生成架构与查询推荐 |
| S12 | A | A Generative Re-ranking Model for List-level Multi-objective Optimization at Taobao | https://arxiv.org/abs/2505.07197 | 列表级多目标生成式重排 |
| S13 | A | DINOv2: Learning Robust Visual Features without Supervision | https://arxiv.org/abs/2304.07193 | 自监督视觉骨干与纯视觉表征 |
| S14 | A | Block-SCL: Blocking Matters for Supervised Contrastive Learning in Product Matching | https://arxiv.org/abs/2207.02008 | 监督对比学习与细粒度商品匹配 |
| S15 | A | JDsearch: A Personalized Product Search Dataset with Real Queries and Full Interactions | https://arxiv.org/abs/2305.14810 | 电商搜索数据集与评测基准 |
| S16 | A | Monolith: Real Time Recommendation System With Collisionless Embedding Table | https://arxiv.org/abs/2209.07663 | 实时推荐 embedding 基础设施 |
| S17 | B | Large Language Model based Long-tail Query Rewriting in Taobao Search | https://arxiv.org/abs/2311.03758 | LLM 查询改写与长尾搜索 |
| S18 | A | Adaptive Domain Scaling for Personalized Sequential Modeling in Recommenders (ADS) | https://arxiv.org/abs/2502.05523 | 个性化序列建模与域扩展 |
| S19 | B | VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks | https://arxiv.org/abs/2410.05160 | VLM 转 embedding model 与 MMEB 评测 |
| S20 | C | Multimodal Learning with Online Text Cleaning for E-commerce Product Search (Amazon) | https://www.amazon.science/publications/multimodal-learning-with-online-text-cleaning-for-e-commerce-product-search | 多模态商品搜索与在线文本清洗 |
| S21 | C | Web-scale Semantic Product Search with Large Language Models (Amazon) | https://www.amazon.science/publications/web-scale-semantic-product-search-with-large-language-models | LLM 语义匹配与 Web-scale 搜索 |
| S22 | B | RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment | https://arxiv.org/abs/2304.06767 | 奖励排序微调与 RL 后训练路线 |
| S23 | A | Large-Scale Product Retrieval with Weakly Supervised Representation Learning | https://arxiv.org/abs/2208.00955 | 弱监督表征学习与大规模商品检索 |
| S24 | B/D | PinCLIP: Large-scale Foundational Multimodal Representation at Pinterest | https://arxiv.org/abs/2603.03544 | 工业多模态表征与 serving 约束 |
| S25 | B | REVISION: Reflective Intent Mining and Online Reasoning Auxiliary for E-commerce Visual Search System Optimization | https://arxiv.org/abs/2510.22739 | 图搜系统优化与意图挖掘 |
| S26 | B | From Pixels to Purchase: Building and Evaluating a Taxonomy-Decoupled Visual Search Engine for Home Goods E-commerce | https://arxiv.org/abs/2601.11769 | 分类解耦图搜引擎与评测 |
| S27 | B | Gemini Embedding 2: A Native Multimodal Embedding Model from Gemini | https://arxiv.org/abs/2605.27295 | 原生多模态 embedding 前沿 |
| S28 | B | LaME: Learning to Think in Latent Space for Multimodal Embedding via Information Bottleneck | https://arxiv.org/abs/2606.13061 | 信息瓶颈与 latent 空间嵌入 |
| S29 | C | PDD Holdings FY2025 Form 20-F | https://www.sec.gov/Archives/edgar/data/1737806/000110465926050727/pdd-20251231x20f.htm | 监管披露与搜索推荐治理 |
| S30 | A | ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction | https://arxiv.org/abs/2112.01488 | Late interaction 文本检索 |
| S31 | A | ColPali: Efficient Document Retrieval with Vision Language Models | https://arxiv.org/abs/2407.01449 | 视觉文档检索与 token 级匹配 |
| S32 | A | MagicLens: Self-Supervised Image Retrieval with Open-Ended Instructions | https://arxiv.org/abs/2403.19651 | 指令条件化图像检索 |
| S33 | A | MME: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models | https://arxiv.org/abs/2306.13394 | 多模态理解评测 |
| S34 | A | MMMU: A Massive Multi-disciplinary Multimodal Understanding and Reasoning Benchmark | https://arxiv.org/abs/2311.16502 | 多学科多模态推理评测 |
| S35 | B | UniNote: A Unified Embedding Model for Multimodal Representation and Ranking | https://arxiv.org/abs/2605.29287 | 统一表征与排序 |

## Conflicts and interpretation boundaries

- **共享向量空间不等于图搜已解决。** CLIP/ALIGN/SigLIP 证明图文对齐能支撑检索 [S04, S05, S07]；但电商图搜的 SKU 粒度、域间差异和意图模糊是 CLIP 预训练不直接解决的问题 [S08, S26]。正文据此把"多模态 embedding 进入图搜"写成范式迁移，不写成问题已闭合。
- **工业自报收益不能横向比较。** 京东 [S06]、淘宝 [S10-S12]、Amazon [S20-S21] 的线上收益来自不同业务场景、对照组和统计方法。正文引用时标为作者报告，不跨平台排序。
- **SFT 证据更稳定与 RL 部分有效不是矛盾。** SFT 优化对比损失，信号密集且机制清晰 [S10, S14, S19, S24]；RL 优化排序指标，信号稀疏且 reward hacking 风险高 [S22]。正文按任务类型分场景评估，不写成全局结论。
- **2025-2026 预印本是趋势信号。** REVISION [S25]、From Pixels to Purchase [S26]、Gemini Embedding 2 [S27]、LaME [S28]、UniNote [S35] 均为预印本，正文标为前沿信号，不写成共识。
- **拼多多/Temu 与 SHEIN 证据不足。** PDD 20-F 披露涉及搜索推荐治理 [S29] 但不含可归因模型架构；SHEIN 未公开可核验论文。正文不推测其内部技术路线。

## Deliberately excluded claims

- 不声称多模态 embedding 已完全替代传统方法；精确查重场景指纹哈希仍更快更准。
- 不把任一 benchmark 的排名写成模型真实能力的完整证明。
- 不声称 RL 是多模态 embedding 的标配后训练；按任务类型分场景评估。
- 不把闭源模型的公开产品能力写成已验证的架构结论。
- 不把厂商自报的线上收益写成独立验证的事实。
