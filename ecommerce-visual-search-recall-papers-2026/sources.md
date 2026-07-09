# 电商图搜召回 Paper List 2026：来源说明

证据复核时间：2026-07-09，北京时间。本文面向“电商图搜召回”整理 2021 到 2026 年公开论文、技术报告和头部平台公开研究，其中以 2025 下半年到 2026 年论文为主。本文将“图搜召回”定义为：以用户图片、裁剪图、商品图、图文组合、文本 query 到图文商品库的第一阶段召回，以及召回后的轻量融合和高精 rerank；纯文本搜索、广告排序、推荐排序只在它们能支持图搜召回系统判断时纳入。

## 证据分层

| 等级 | 含义 | 使用方式 |
|---|---|---|
| A | arXiv/ACL/ACM/CVPR/Amazon Science 等可核验论文或公司技术报告 | 支撑题名、年份、方法、公式、实验数字、线上 A/B 作者报告、部署状态 |
| B | 与主任务相关但不是纯图搜召回，或缺少线上公开细节的论文 | 用作方法背景、候选技术和工程启发 |
| C | 通用基础模型、通用 benchmark 或非电商场景方法 | 用作 baseline、teacher、评测或二阶段启发，不支撑“已在电商图搜稳定 work”的结论 |

## 主来源

| ID | 来源 | 日期 | 等级 | 本文使用的事实边界 |
|---|---|---:|---|---|
| S01 | Chen et al., [Pailitao-VL](https://arxiv.org/abs/2602.13704) | 2026-03-05 | A | 统一 embedding/reranker、原型 ID、listwise reranker、离线表格、延迟和线上 GMV 作者报告。 |
| S02 | Sun et al., [TIGER-FG](https://arxiv.org/abs/2605.18434) | 2026-05-18 | A | Image-to-multimodal retrieval、ECom-RF-IMMR、Recall@1 提升、公式和消融。 |
| S03 | Guo et al., [TGQ-Former](https://arxiv.org/abs/2605.17366) | 2026-05-17 | A | Text-guided Q-Former、H@100 提升、MLRM vs MLLM 的算力对比。 |
| S04 | Liang et al., [UniECS](https://arxiv.org/abs/2508.13843) | 2025-08-20 | A | 统一多模态电商搜索、M-BEER、门控融合、多项线上指标作者报告。 |
| S05 | Zhang et al., [OneRetrieval](https://arxiv.org/abs/2606.13533) | 2026-06-11 | A | 可编辑生成式多路召回、Keyword-Aligned Encoding、线上替换倒排和近全召回实验。 |
| S06 | Liu et al., [Efficient Generative Retrieval for E-commerce Search](https://arxiv.org/abs/2605.14434) | 2026-05-20 | A | CQ-SID、EG-GRPO、TmallAPP 线上 GMV/UCTCVR、QPS、延迟。 |
| S07 | Zhang et al., [Beyond Text: Text-Image Fusion for Scalable Two-Tower Retrieval](https://arxiv.org/abs/2603.04836) | 2026-07-06 | A | Target 双塔商品召回，图文 item tower 融合，nDCG@1 提升，CPU ANN 部署。 |
| S08 | Gaydhani et al., [Unified LTR for Multi-Channel Retrieval](https://arxiv.org/abs/2602.23530) | 2026-03-06 | A | 多通道召回融合、conversion-weighted label、Target.com conversion 和 latency。 |
| S09 | Zhang et al., [AFMRL](https://aclanthology.org/2026.findings-acl.704/) | 2026-07-02 | A | 属性生成、AGCL、RAR、GRPO、ACL Findings 2026 实验结果。 |
| S10 | Fu et al., [MOON Embedding](https://arxiv.org/abs/2511.11305) | 2025-11-18 | A | image-based search recall exchange rate、搜索广告全链路部署、线上 CTR 作者报告。 |
| S11 | Li et al., [Qwen3-VL-Embedding and Qwen3-VL-Reranker](https://arxiv.org/abs/2601.04720) | 2026-01-19 | A | 多阶段 embedding/reranker、distillation、MRL、MMEB-V2 结果。 |

## 工业与背景来源

| ID | 来源 | 日期 | 等级 | 本文使用的事实边界 |
|---|---|---:|---|---|
| S12 | Zhu et al., [Bringing Multimodality to Amazon Visual Search System](https://www.amazon.science/publications/bringing-multimodality-to-amazon-visual-search-system) | 2024 | A | Amazon 3-tower/4-tower 多模态视觉搜索，CTR 作者报告。 |
| S13 | Kumar et al., [Unsupervised Multi-Modal Representation Learning](https://www.amazon.science/publications/unsupervised-multi-modal-representation-learning-for-high-quality-retrieval-of-similar-products-at-e-commerce-scale) | 2023 | A | CL + ANNS、相似商品召回质量速度 Pareto。 |
| S14 | Hu et al., [De-noised Vision-Language Fusion](https://www.amazon.science/publications/de-noised-vision-language-fusion-guided-by-visual-cues-for-e-commerce-product-search) | 2024 | A | 商品搜索中的去噪图文融合。 |
| S15 | Lu et al., [MIEM](https://arxiv.org/abs/2311.17954) | 2023-11-29 | A | Shopee 图搜 item embedding 部署和 clicks/orders 作者报告。 |
| S16 | Zheng et al., [MAKE](https://arxiv.org/abs/2301.12646) | 2023-02-18 | A | Taobao Search V+L 预训练召回，modal adaptation 和线上部署。 |
| S17 | Zheng et al., [Delving into E-Commerce Product Retrieval with Vision-Language Pre-training](https://arxiv.org/abs/2304.04377) | 2023-04-17 | A | Taobao 商品召回通道，视觉预训练任务和负采样。 |
| S18 | Liu and Ramos, [Multimodal Semantic Retrieval for Product Search](https://arxiv.org/abs/2501.07365) | 2025-01-13 | A | Amazon 商品语义检索，3-tower/4-tower text-image product representation。 |
| S19 | Wu et al., [MOON3.0](https://arxiv.org/abs/2604.00513) | 2026-04-01 | A | reasoning-aware product representation、MBE3.0、contrastive + RL。 |
| S20 | Yuan et al., [FashionMV](https://arxiv.org/abs/2604.10297) | 2026-04-11 | A | 多视角商品级 composed image retrieval 数据集和 ProCIR。 |
| S21 | Li et al., [RMIR](https://www.amazon.science/publications/rmir-a-benchmark-dataset-for-reasoning-intensive-multimodal-image-retrieval) | 2026 | A | 复杂推理式多模态图像检索 benchmark，CVPR 2026。 |
| S22 | Zhang et al., [MagicLens](https://arxiv.org/abs/2403.19651) | 2024-03-28 | A | 指令条件化开放式图像检索背景。 |
| S23 | Radford et al., [CLIP](https://arxiv.org/abs/2103.00020) | 2021-02-26 | A | 图文对比学习基础范式。 |
| S24 | Zhai et al., [SigLIP](https://arxiv.org/abs/2303.15343) | 2023-03-27 | A | pairwise sigmoid loss 图文对齐背景。 |
| S25 | Jiang et al., [VLM2Vec](https://arxiv.org/abs/2410.05160) | 2024-10-07 | A | VLM 转多模态 embedding 和 MMEB。 |
| S26 | Faysse et al., [ColPali](https://arxiv.org/abs/2407.01449) | 2024-07-01 | A | late interaction 和多向量视觉检索启发。 |
| S27 | Chung et al., [Scaling Cross-Domain CBIR](https://arxiv.org/abs/2204.11593) | 2022-04-13 | A | 真实 snap and search 的跨域 CBIR 系统约束。 |
| S28 | Han et al., [Large-Scale Product Retrieval with Weakly Supervised Representation Learning](https://arxiv.org/abs/2208.00955) | 2022-08-01 | A | 伪属性、弱监督和商品检索竞赛经验。 |
| S29 | Lu et al., [Graph-based Multilingual Product Retrieval](https://www.amazon.science/publications/graph-based-multilingual-product-retrieval-in-e-commerce-search) | 2021 | A | 跨境商品召回，图注意力，多语种 recall/mAP 与线上业务提升。 |
| S30 | Meng et al., [VLM2Vec-V2](https://arxiv.org/abs/2507.04590) | 2025-07-07 | A | 多模态 embedding benchmark 扩展背景。 |

## 口径与不确定性

- 本文所有“线上提升”均按论文或公司研究页面的作者报告处理，不写作独立审计或可复现保证。未公开流量分桶、显著性区间、实验周期、长期留存和回滚策略的论文，稳定性评分会降一级。
- “能 work”在本文中不是“离线 SOTA”，而是同时看召回质量、在线业务指标、延迟、索引成本、数据治理、冷启、可回滚和多入口一致性。
- 生成式召回在 2026 年出现较强线上证据，但主要来自文本搜索和多通道召回融合，不等同于第一阶段图搜 ANN 可以被直接替代。
- MLLM 属性生成、CoT 和 RL 对细粒度召回有明确潜力，但若没有属性验真、hard negative 审核和线上 guardrail，容易把生成错误转为召回噪声。
- 电商图搜存在强平台差异：Pailitao、Taobao、Kuaishou、Shopee、Amazon、Target 的 query 入口、商品类目、商家图质量和排序目标不同。本文只给出可迁移的算法结构和风险判断，不假设任一平台收益能线性迁移。
