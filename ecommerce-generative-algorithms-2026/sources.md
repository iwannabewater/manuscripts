# Sources and Research Method

资料核验日期：2026-05-27
研究主题：大型电商平台在多模态大模型、后训练、生成式推荐、智能搜索与图像检索上的公开技术路线

## Method

本报告采用一手材料研究法。核心材料包括会议工业论文、作者技术报告或预印本、公司官方工程说明、上市公司监管披露，以及监管机关发布的公告。检索后逐篇核对摘要、方法、实验范围和线上声明，再按公司与技术方向交叉整理；结构化映射见 `data/source-map.tsv`。

报告区分五种证据强度：

| 等级 | 可支持的论断 | 典型来源 |
|---|---|---|
| A | 特定系统、实验口径与部署结果确有公开陈述 | 同行评审工业论文或官方工程说明 |
| B | 作者报告线上实验或部署，但仍需把结果视为其公开声明 | 预印本、公司技术报告 |
| C | 公司承认产品能力、排序因素或治理机制存在 | 官方政策、合规披露、监管文件 |
| D | 可用于解释方法，不证明目标公司生产部署 | 通用基础论文、相邻业务论文 |
| E | 不进入事实结论，只作为进一步核查线索 | 二手报道、招聘描述、非官方解读 |

论文中的线上提升均按论文所述场景引用。不同平台的业务目标、流量分配、对照组和统计方法未必相同，指标不能横向排序。预印本出现的部署或收益表述，正文均标为作者报告，不作独立验证后的事实陈述。

## Evidence Matrix

| 平台 | 直接公开技术证据 | 可以严谨陈述的范围 | 公开不足之处 |
|---|---|---|---|
| Alibaba 淘宝/天猫 | SORT-Gen、BEQUE、AIGQ、KARMA | 查询推荐、长尾改写、多模态个性化搜索与生成式重排均有公开系统材料 | 部分 2026 工作仍为预印本，长期经营效果不可外推 |
| 京东 | 实时图搜、JDsearch、LLM 查询重写 | 图像检索基础设施、真实搜索数据与作者报告的 LLM 改写落地 | 未发现统一生成式推荐主链路的公开系统说明 |
| PDD（拼多多/Temu） | 2025 Form 20-F | 母公司披露中可确认搜索/推荐及自动化处理相关治理和竞争问题 | 未发现可归因于拼多多或 Temu 具体产品的 MLLM、后训练或生成推荐架构论文 |
| 抖音电商相关 ByteDance 工作 | ADS；RankMixer 与 SUMMA 作为相关系统证据 | ADS 直接覆盖抖音电商服务；排序扩展和多模态搜广可说明集团技术能力边界 | SUMMA 不等同于抖音电商推荐部署 |
| Amazon | Rufus、语义商品搜索、MML-TP、GENIUS | 对话式购物、低延迟语义匹配与多模态/生成检索研究 | GENIUS 的公开结果不能写成 Amazon 商城已部署 |
| Shopee | LightSAGE、Compass 系列、EcomEval、RGAlign-Rec | 广告召回已有部署论文；领域大模型、评估与对话推荐有技术报告/预印本 | 新模型线上范围以作者陈述为限 |
| SHEIN | Ranking Policy、欧盟委员会公告 | 平台公开的排序/个性化因素，以及推荐透明度治理要求 | 未公开可核验的模型架构、训练方法或效果 |

## Primary Sources

### Alibaba 淘宝/天猫

- `S01` Meng et al., *A Generative Re-ranking Model for List-level Multi-objective Optimization at Taobao*, SIGIR 2025. https://arxiv.org/abs/2505.07197
- `S02` Cao et al., *AIGQ: An End-to-End Hybrid Generative Architecture for E-commerce Query Recommendation*, preprint, 2026. https://arxiv.org/abs/2603.19710
- `S03` *KARMA: Knowledge-Action Regularized Multimodal Alignment for Personalized Search at Taobao*, 2026. https://arxiv.org/abs/2603.22779
- `S04` *Large Language Model based Long-tail Query Rewriting in Taobao Search*, 2023. https://arxiv.org/abs/2311.03758

### 京东

- `S05` Li et al., *The Design and Implementation of a Real Time Visual Search System on JD E-commerce Platform*, 2019. https://arxiv.org/abs/1908.07389
- `S06` Liu et al., *JDsearch: A Personalized Product Search Dataset with Real Queries and Full Interactions*, SIGIR 2023. https://arxiv.org/abs/2305.14810
- `S07` *Relevance Matters: A Multi-Task and Multi-Stage Large Language Model Approach for E-commerce Query Rewriting*, preprint, 2026. https://arxiv.org/abs/2603.02555

### 抖音电商与 ByteDance 相关系统

- `S08` Chai et al., *Adaptive Domain Scaling for Personalized Sequential Modeling in Recommenders*, SIGIR 2025. https://arxiv.org/abs/2502.05523
- `S09` *RankMixer: Scaling Up Ranking Models in Industrial Recommenders*, preprint, 2025. https://arxiv.org/abs/2507.15551
- `S10` *SUMMA: A Multimodal Large Language Model for Advertisement Summarization*, CIKM 2025. https://arxiv.org/abs/2508.20582
- `S11` *Monolith: Real Time Recommendation System With Collisionless Embedding Table*, RecSys ORSUM 2022. https://arxiv.org/abs/2209.07663

### Amazon

- `S12` Amazon Science, *The technology behind Amazon's GenAI-powered shopping assistant, Rufus*. https://www.amazon.science/blog/the-technology-behind-amazons-genai-powered-shopping-assistant-rufus
- `S13` Muhamed et al., *Web-scale Semantic Product Search with Large Language Models*, PAKDD 2023. https://www.amazon.science/publications/web-scale-semantic-product-search-with-large-language-models
- `S14` Hu et al., *Multimodal Learning with Online Text Cleaning for E-commerce Product Search*. https://www.amazon.science/publications/multimodal-learning-with-online-text-cleaning-for-e-commerce-product-search
- `S15` Kim et al., *GENIUS: A Generative Framework for Universal Multimodal Search*, CVPR 2025. https://www.amazon.science/publications/genius-a-generative-framework-for-universal-multimodal-search

### Shopee

- `S16` Nguyen et al., *LightSAGE: Graph Neural Networks for Large Scale Item Retrieval in Shopee's Advertisement Recommendation*, RecSys 2023. https://arxiv.org/abs/2310.19394
- `S17` *COMPASS: Large Multilingual Language Model for South-East Asia*, 2024. https://arxiv.org/abs/2404.09220
- `S18` *Compass-v3: Scaling Domain-Specific LLMs for Multilingual and Multimodal E-Commerce*, technical report, 2025. https://arxiv.org/abs/2509.09121
- `S19` *EcomEval: Towards Reliable Evaluation of Large Language Models for Multilingual and Multimodal E-Commerce Applications*, technical report, 2025. https://arxiv.org/abs/2510.20632
- `S20` *RGAlign-Rec: Ranking-Guided Alignment for Latent Query Reasoning in Recommendation Systems*, preprint, 2026. https://arxiv.org/abs/2602.12968

### PDD 与 SHEIN 的披露边界

- `S21` PDD Holdings, *2025 Form 20-F*. https://investor.pddholdings.com/static-files/e15edea4-5e6d-4740-808a-63a3dd1b2ce4
- `S22` SHEIN, *SHEIN's Marketplace User Ranking Policy*, effective 2025-02-07. https://roe.shein.com/ranking-policy-a-1979.html
- `S23` European Commission, *Commission launches investigation into Shein under the Digital Services Act*, 2026-02-17. https://digital-strategy.ec.europa.eu/en/news/commission-launches-investigation-shein-under-digital-services-act

### 方法基础

- `S24` Rajput et al., *Recommender Systems with Generative Retrieval*, 2023. https://arxiv.org/abs/2305.05065
- `S25` Zhai et al., *Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations*, ICML 2024. https://arxiv.org/abs/2402.17152
- `S26` Rafailov et al., *Direct Preference Optimization*, NeurIPS 2023. https://arxiv.org/abs/2305.18290
- `S27` Shao et al., *DeepSeekMath*, 2024. https://arxiv.org/abs/2402.03300

## Boundary

公开论文无法说明未披露的生产特征、流量配比、风控规则、完整训练数据或长期因果收益。本报告不把相邻业务线成果直接等同于目标平台上线状态，不使用公开不足的平台作算法成熟度负面排名，也不将通用方法论文当作公司部署证明。报告的工程路线是基于公开证据作出的可检验归纳，实施时仍需以自身日志、合规要求、延迟预算与线上实验为准。
