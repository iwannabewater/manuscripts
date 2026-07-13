# 电商图搜 · Reasoning-then-Embed 论文读单 2026：来源说明

证据复核时间：2026-07-13，北京时间。

本文是一份 **Reasoning-then-Embed** 主线读单，按「电商图搜直接相关 → 通用推理表征可迁移 → CIR 修改意图 → 低延迟前沿」组织 15 篇核心工作。它与仓库中的《电商图搜召回 Paper List 2026》并列：后者覆盖更广的召回系统论文，本文只收与「先推理、后表征」相关的精读集合。

## 证据分层

| 等级 | 含义 | 使用方式 |
|---|---|---|
| A | arXiv 论文/技术报告、正式会议论文（如 WSDM 2026） | 支撑题名、方法、作者报告的离线/线上数字、状态 |
| B | 系列演进说明、跨论文归纳 | 用于阅读路径与系统拼法，不写成独立实验结论 |
| C | 社区二次解读 | 本文不使用 |

## 主来源

| ID | 来源 | 日期/状态 | 等级 | 事实边界 |
|---|---|---|---|---|
| S01 | [MOON3.0](https://arxiv.org/abs/2604.00513) | arXiv:2604.00513 | A | 属性推理→256 维；MBE3.0 相对 MOON2.0 增益 |
| S02 | [TIGER-FG](https://arxiv.org/abs/2605.18434) | arXiv:2605.18434 | A | 文本引导隐式 grounding；R@1；Query 参数量 |
| S03 | [Pailitao-VL](https://arxiv.org/abs/2602.13704) | arXiv:2602.13704 | A | ID 原型 embedding；listwise reranker；GMV 与延迟作者报告 |
| S04 | [MOON Embedding](https://arxiv.org/abs/2511.11305) | arXiv:2511.11305 | A | 搜索广告全链路部署；CTR 累计约 +20% 为系列收益 |
| S05 | MOON / MOON2.0 系列 | 演进底座 | B | 生成式表征、模态不平衡、噪声与 many-to-one；连读至 MOON3.0 |
| S06 | [TGQ-Former 文](https://arxiv.org/abs/2605.17366) | arXiv:2605.17366 | A | 元数据引导视觉 token；H@100 +6.04% |
| S07 | [REVISION](https://arxiv.org/abs/2510.22739) | WSDM 2026 Full · arXiv:2510.22739 | A | 意图挖掘与无点击；摘要无统一百分比 |
| S08 | [Think Then Embed](https://arxiv.org/abs/2510.05014) | arXiv:2510.05014 | A | Reasoner→Embedder；MMEB-V2 |
| S09 | [UME-R1](https://arxiv.org/abs/2511.00405) | arXiv:2511.00405 | A | 双 embedding；相对 DUME / VLM2Vec-V2 |
| S10 | [Embed-RL](https://arxiv.org/abs/2602.13823) | arXiv:2602.13823 | A | Embedder-Guided RL；T-CoT |
| S11 | [MMEmb-R1](https://arxiv.org/abs/2604.06156) | arXiv:2604.06156 | A | pair-aware；约 2.5× 延迟改善 |
| S12 | [Think When Needed](https://arxiv.org/abs/2605.14448) | arXiv:2605.14448 | A | 路由门控；参数与 token 开销 |
| S13 | [CIR-CoT](https://arxiv.org/abs/2510.08003) | arXiv:2510.08003 | A | CIR CoT 管线；FashionIQ/CIRR/CIRCO |
| S14 | [MCoT-MVS](https://arxiv.org/abs/2603.17360) | arXiv:2603.17360 | A | 视觉选择受 CoT 控制；CIR SOTA |
| S15 | [TTE-Flash](https://arxiv.org/abs/2605.16638) | arXiv:2605.16638 | A | latent think tokens |
| S16 | [LaME](https://arxiv.org/abs/2606.13061) | arXiv:2606.13061 | A | latent reason tokens / 信息瓶颈 |

## 口径与不确定性

- **预印本**：2026 年多数条目仍是 arXiv 预印本。读单强调方法与公开实验，不默认正式录用。
- **作者报告的线上收益**：Pailitao-VL GMV、MOON Embedding CTR 等按论文/技术报告作者表述收录；非独立审计，不可直接线性迁移到其他平台。
- **系列归因**：MOON Embedding 报告的约 20% CTR 是系列多次迭代系统收益，正文明确不能单独归因于 MOON3.0 或单一召回模型。
- **REVISION**：正式会议论文，但摘要未给出统一无点击下降百分比，正文不杜撰数字。
- **通用 RTE 指标**：MMEB-V2 等通用榜成绩用于迁移判断，不写成「已在电商图搜稳定 work」。

## 本地数据

- `data/paper-list.tsv`：15 篇清单、层、收益、模态、推荐原因
- `data/source-map.tsv`：来源到事实的映射
- `data/reading-paths.tsv`：五条连读路径
