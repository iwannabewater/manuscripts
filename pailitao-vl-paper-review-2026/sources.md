# Pailitao-VL Paper Review 2026：来源说明

证据复核时间：2026-07-08，北京时间。本文评审对象为 arXiv:2602.13704v2 `Pailitao-VL: Unified Embedding and Reranker for Real-Time Multi-Modal Industrial Search`。论文 v1 于 2026-02-14 提交，v2 于 2026-03-05 修订；本文以 v2 PDF、HTML 与 TeX 源包为准。

## 证据分层

| 等级 | 含义 | 使用方式 |
|---|---|---|
| A | 原始论文、arXiv 页面、arXiv TeX 源包、正式会议论文或官方技术报告 | 可支撑题名、作者、版本、公式、实验数字、方法定义和公开模型事实 |
| B | 研究团队主页、索引页面或二级研究材料 | 只用于发现线索，不作为核心方法或实验结论的独立证据 |
| C | 社交平台、媒体、自动摘要站点和社区解读 | 本文不使用 C 级证据支撑正文结论 |

## 主来源

| ID | 来源 | 日期 | 等级 | 本文使用的事实边界 |
|---|---|---:|---|---|
| S01 | Chen et al., [Pailitao-VL arXiv page](https://arxiv.org/abs/2602.13704) | 2026-03-05 | A | 题名、作者、v1/v2 日期、主题分类、摘要、DOI 与公开来源入口。 |
| S02 | Chen et al., [Pailitao-VL PDF](https://arxiv.org/pdf/2602.13704) | 2026-03-05 | A | 方法正文、公式、表 1 到表 5、训练配置、线上 A/B 作者报告；本地归档见 `sources/`。 |
| S03 | Chen et al., [Pailitao-VL HTML](https://arxiv.org/html/2602.13704) | 2026-03-05 | A | 用于交叉核对章节结构、公式位置和表格位置。 |
| S04 | Chen et al., [Pailitao-VL TeX source](https://arxiv.org/e-print/2602.13704) | 2026-03-05 | A | TeX 原始表格、prompt 模板、公式和参考文献键；本地解包见 `sources/latex/`。 |

## 背景来源

| ID | 来源 | 日期 | 等级 | 本文使用的事实边界 |
|---|---|---:|---|---|
| S05 | Jiang et al., [VLM2Vec](https://arxiv.org/abs/2410.05160) | 2024-10-07 | A | VLM 转 embedding、MMEB 与对比训练背景。 |
| S06 | Li et al., [Qwen3-VL-Embedding and Qwen3-VL-Reranker](https://arxiv.org/abs/2601.04720) | 2026-01-08 | A | 论文使用的强基线和多模态 embedding/reranker 训练背景。 |
| S07 | Deng et al., [ArcFace](https://arxiv.org/abs/1801.07698) | 2019 | A | Additive angular margin loss 的几何动机和分类式度量学习背景。 |
| S08 | Zhang et al., [Visual Search at Alibaba](https://arxiv.org/abs/2102.04674) | 2021-02-09 | A | Alibaba 早期电商视觉搜索系统约束和工业背景。 |

## 本地归档

- `sources/pailitao-vl-2602.13704.pdf`
- `sources/pailitao-vl-2602.13704.txt`
- `sources/pailitao-vl-2602.13704-source.tar`

## 口径与不确定性

- 论文报告的 2% 平台全流量 GMV 增益、6% 标准化品类 GMV 增益、20% SKU-price comparison 场景 GMV 增益，均按作者报告处理；本文不将其写作独立复现或审计结果。
- 论文没有披露线上 A/B 的流量分桶、统计显著性区间、回滚策略、品类分层细节和长期留存影响，因此本文只讨论短期线上效果信号和工程可用边界。
- 本文未找到 Pailitao-VL 的公开训练代码、数据集和模型权重。实现分析基于论文公式、prompt、训练配置和系统描述，不能替代代码级复现。
- 原型 ID 库和 MLLM agent 数据治理是方法成立的关键。若原型簇纯度不足，ID 分类会把噪声固化成监督信号；若业务域变化导致原型分布漂移，线上稳定性需要重新校准。
- Chunkwise listwise reranker 的跨 chunk 合并依赖绝对相关性分数校准。若校准头跨品类或跨 query 分布不稳定，混合排序可能保留局部排序错误并放大到全局列表。
