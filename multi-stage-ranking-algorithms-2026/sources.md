# Sources and Research Method

资料核验日期：2026-05-27
研究主题：国内外头部互联网平台在召回、粗排、精排、混排与重排阶段的公开算法路线和工程经验

## Method

本报告只将论文原文、会议工业论文页面与公司官方工程说明作为平台技术事实的来源。检索阶段先定位各平台能够明确对应到在线漏斗层位的材料，随后读取全文或官方正文，抽取阶段位置、模型机制、服务约束、实验声明和披露边界，并按漏斗阶段和平台两个方向交叉校验。引用与正文用途的结构化映射见 `data/source-map.tsv`。

报告使用四级证据口径：

| 等级 | 可以支持的陈述 | 使用方式 |
|---|---|---|
| A | 某平台明确公开了阶段、模型、生产部署或线上实验口径 | 同行评审工业论文或官方工程说明可作为平台案例主证据 |
| B | 作者在公开预印本中报告部署、流量或线上结果 | 正文注明为作者报告，不把指标作为独立复核事实 |
| C | 官方材料说明排序行为、产品机制或数据集，但不披露完整模型 | 只用于说明行为边界、评测资产或公开空白 |
| D | 可解释方法或行业演进，但不能证明特定平台已部署 | 仅作方法背景，不外推公司状态 |

不同平台的展示面、业务目标、候选规模、实验分桶和统计口径不一致，线上提升不能横向比较。`Retrieval`、`candidate generation`、`matching` 在正文中统一归入召回；`first-stage ranking`、`pre-ranking` 归入粗排；最终页面排序中的多目标、去重、多样性和策略修正归入混排/重排。

## Evidence Matrix

| 平台或业务 | 可直接归属的阶段 | 核心公开证据 | 严谨边界 |
|---|---|---|---|
| Alibaba 淘宝/天猫与广告 | 召回、粗排、精排、重排 | MIND、COLD、DIN/DIEN/SIM、MOPPR、CMR、SORT-Gen | 覆盖最完整，但不同论文对应搜索、推荐或广告业务，不合并为单一系统 |
| 京东商品搜索 | 召回、精排 | Semantic Retrieval to Pairwise Ranking | 证明商品搜索两阶段，不代表首页推荐全链路 |
| ByteDance/抖音推荐 | 实时系统、精排 | Monolith、RankMixer | RankMixer 的全流量和指标属于预印本作者声明 |
| 快手 | 召回、重排 | KuaiFormer、NAR4Rec、Dual-Rerank | 新重排论文均以预印本和作者报告表述 |
| 美团 | 精排/排序、重排 | MTGR、NSGR | 公开证据来自预印本，部署范围按作者陈述限定 |
| 腾讯广告 | 召回、评测资产 | GPU 检索模型、TencentGR | 可证明广告召回研究与公开数据集，不证明完整级联链路 |
| Google/YouTube | 召回、精排 | YouTube DNN、multitask ranking、Google Play Wide & Deep | 工业论文是多阶段范式的重要基线 |
| Meta/Instagram/Ads | 召回、粗排、精排、重排、知识迁移 | Explore 官方架构、GEM 官方工程稿 | Explore 与 Ads 是不同业务面，GEM 不等同于 Explore 全链路改造 |
| Pinterest | 召回、精排 | PinSage、PinnerSage、TransAct、PinRec | PinRec 作为生成召回探索按论文口径使用 |
| LinkedIn Feed | 候选选择、精排 | two-pass 官方稿、LLM retrieval 论文、新 Feed 官方稿 | 2026 新架构以官方发布范围为限 |
| Amazon | 商品召回/语义匹配 | Semantic Product Search、官方历史稿 | 不据此推演当前商城完整排序架构 |
| Airbnb Search | 召回、精排、列表多样性 | embedding ranking、deep ranking、diversity、EBR | 两边市场库存与可售约束不可直接套用到内容流 |
| Netflix | 页面与行内排序行为 | 官方帮助中心 | 官方页不披露召回、粗排模型，故只作产品层边界证据 |

## Primary Sources

### 海外平台

- `S01` Covington et al., *Deep Neural Networks for YouTube Recommendations*, RecSys 2016. https://research.google.com/pubs/archive/45530.pdf
- `S02` Cheng et al., *Wide & Deep Learning for Recommender Systems*, DLRS 2016. https://arxiv.org/abs/1606.07792
- `S03` Zhao et al., *Recommending What Video to Watch Next: A Multitask Ranking System*, RecSys 2019. https://research.google/pubs/recommending-what-video-to-watch-next-a-multitask-ranking-system/
- `S04` Meta Engineering, *Scaling the Instagram Explore recommendations system*, 2023. https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/
- `S05` Meta Engineering, *Meta's Generative Ads Model (GEM)*, 2025. https://engineering.fb.com/2025/11/10/ml-applications/metas-generative-ads-model-gem-the-central-brain-accelerating-ads-recommendation-ai-innovation/
- `S06` Ying et al., *Graph Convolutional Neural Networks for Web-Scale Recommender Systems*, KDD 2018. https://arxiv.org/abs/1806.01973
- `S07` Pancha et al., *PinnerSage: Multi-Modal User Embedding Framework for Recommendations at Pinterest*, KDD 2020. https://arxiv.org/abs/2007.03634
- `S08` Xia et al., *TransAct: Transformer-based Realtime User Action Model for Recommendation at Pinterest*, KDD 2023. https://arxiv.org/abs/2306.00248
- `S09` Badrinath et al., *PinRec: Outcome-Conditioned, Multi-Token Generative Retrieval for Industry-Scale Recommendation Systems*, 2025. https://arxiv.org/abs/2504.10507
- `S10` LinkedIn Engineering, *Community-focused Feed optimization*, 2020. https://www.linkedin.com/blog/engineering/feed/community-focused-feed-optimization
- `S11` Ramanujam et al., *Large Scale Retrieval for the LinkedIn Feed Using Causal Language Models*, AAAI 2026. https://ojs.aaai.org/index.php/AAAI/article/view/41445
- `S12` LinkedIn Engineering, *Engineering the next generation of LinkedIn's Feed*, 2026-03-12. https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed
- `S13` Mohan et al., *Semantic Product Search*, KDD 2019. https://www.amazon.science/publications/semantic-product-search
- `S14` Amazon Science, *The history of Amazon's recommendation algorithm*, 2019. https://www.amazon.science/the-history-of-amazons-recommendation-algorithm
- `S15` Grbovic and Cheng, *Real-time Personalization using Embeddings for Search Ranking at Airbnb*, KDD 2018. https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb
- `S16` Haldar et al., *Improving Deep Learning For Airbnb Search*, KDD 2020. https://www.kdd.org/kdd2020/accepted-papers/view/improving-deep-learning-for-airbnb-search.html
- `S17` Abdool et al., *Managing Diversity in Airbnb Search*, KDD 2020. https://www.kdd.org/kdd2020/accepted-papers/view/managing-diversity-in-airbnb-search.html
- `S18` Airbnb Engineering, *Embedding-Based Retrieval for Airbnb Search*, 2026. https://airbnb.tech/ai-ml/embedding-based-retrieval-for-airbnb-search/
- `S19` Netflix Help Center, *How Netflix's Recommendations System Works*. https://help.netflix.com/en/node/100639

### 国内平台

- `S20` Zhou et al., *Deep Interest Network for Click-Through Rate Prediction*, KDD 2018. https://arxiv.org/abs/1706.06978
- `S21` Zhou et al., *Deep Interest Evolution Network for Click-Through Rate Prediction*, AAAI 2019. https://arxiv.org/abs/1809.03672
- `S22` Li et al., *Multi-Interest Network with Dynamic Routing for Recommendation at Tmall*, CIKM 2019. https://arxiv.org/abs/1904.08030
- `S23` Pi et al., *Search-based User Interest Modeling with Lifelong Sequential Behavior Data for CTR Prediction*, CIKM 2020. https://arxiv.org/abs/2006.05639
- `S24` Wang et al., *COLD: Towards the Next Generation of Pre-Ranking System*, DLP-KDD 2020. https://arxiv.org/abs/2007.16122
- `S25` Zheng et al., *Multi-Objective Personalized Product Retrieval in Taobao Search*, KDD 2022. https://arxiv.org/abs/2210.04170
- `S26` Chen et al., *Controllable Multi-Objective Re-ranking with Policy Hypernetworks*, KDD 2023. https://arxiv.org/abs/2306.05118
- `S27` Meng et al., *A Generative Re-ranking Model for List-level Multi-objective Optimization at Taobao*, SIGIR 2025. https://arxiv.org/abs/2505.07197
- `S28` Li et al., *From Semantic Retrieval to Pairwise Ranking: Applying Deep Learning in E-commerce Search*, 2021. https://arxiv.org/abs/2103.12982
- `S29` Liu et al., *Monolith: Real Time Recommendation System With Collisionless Embedding Table*, RecSys ORSUM 2022. https://arxiv.org/abs/2209.07663
- `S30` Zhu et al., *RankMixer: Scaling Up Ranking Models in Industrial Recommenders*, 2025. https://arxiv.org/abs/2507.15551
- `S31` Liu et al., *KuaiFormer: Transformer-Based Retrieval at Kuaishou*, 2024. https://arxiv.org/abs/2411.10057
- `S32` Ren et al., *Non-autoregressive Generative Models for Reranking Recommendation*, 2024. https://arxiv.org/abs/2402.06871
- `S33` Zhang et al., *Dual-Rerank: Fusing Sequential Dependencies and Utility for Generative Reranking*, 2026. https://arxiv.org/abs/2604.07420
- `S34` Han et al., *MTGR: Industrial-Scale Generative Recommendation Framework in Meituan*, 2025. https://arxiv.org/abs/2505.18654
- `S35` Wang et al., *Next-Scale Generative Reranking: A Tree-based Generative Rerank Method at Meituan*, 2026. https://arxiv.org/abs/2604.05314
- `S36` *An Efficient Embedding Based Ad Retrieval with GPU-Powered Feature Interaction*, 2025. https://arxiv.org/abs/2511.22460
- `S37` Pan et al., *Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation*, 2026. https://arxiv.org/abs/2604.04976

## Boundary

报告不是公司内部系统复刻，也不把论文作者的业务声明视作第三方审计后的结果。多篇国内新工作仍为预印本，正文只使用其公开的方法、阶段定位和作者报告的上线范围。Netflix 的官方说明能确认多层页面排序与信号类型，却不能支持其召回或粗排模型结构。腾讯公开数据集可以说明问题规模和评测设计，不能单独证明生产链路已采用相同模型。
