# Sources

作者：Winston  
资料口径：截至 2026-05-15  
主题：生成式推荐（Generative Recommendation, GR）的发展史、主流算法、产业落地与趋势

## Method

本报告优先采用论文原文、会议页面、公司官方技术文档、官方 GitHub 仓库和产品帮助中心。对 2025-2026 年较新的产业论文，只把公开摘要、任务定义、数据规模、开源链接和作者声明作为可引用事实；不把尚未充分复现的结果当作行业定论。公司内部部署信息只在公开论文、工程博客或官方材料明确说明时写入正文。

推荐系统与生成式模型更新很快，正式工程选型前应复核目标论文版本、代码仓库状态、模型许可、数据许可、业务指标口径、线上约束、隐私合规、延迟预算、召回库规模和安全治理要求。

## Primary Sources

### 经典推荐与深度推荐

- Amazon item-to-item collaborative filtering: https://ieeexplore.ieee.org/document/1167344
- Matrix Factorization Techniques for Recommender Systems: https://www.cs.columbia.edu/~blei/fogm/2025F/readings/KorenBellVolinsky2009.pdf
- Wide & Deep Learning for Recommender Systems: https://research.google/pubs/wide-deep-learning-for-recommender-systems/
- Deep Neural Networks for YouTube Recommendations: https://research.google.com/pubs/archive/45530.pdf
- DeepFM: https://www.ijcai.org/Proceedings/2017/239
- Neural Collaborative Filtering: https://arxiv.org/abs/1708.05031
- Deep Interest Network (DIN): https://arxiv.org/abs/1706.06978
- Deep Interest Evolution Network (DIEN): https://ojs.aaai.org/index.php/AAAI/article/view/4545
- MIND at Tmall: https://arxiv.org/abs/1904.08030
- SIM lifelong behavior modeling: https://arxiv.org/abs/2006.05639
- SASRec: https://arxiv.org/abs/1808.09781
- BERT4Rec: https://arxiv.org/abs/1904.06690
- PinSage: https://arxiv.org/abs/1806.01973
- DLRM: https://arxiv.org/abs/1906.00091
- TorchRec: https://github.com/meta-pytorch/torchrec
- Monolith, ByteDance real-time recommendation: https://arxiv.org/abs/2209.07663

### 生成式推荐与语义 ID

- Generative Recommendation: Towards Next-generation Recommender Paradigm: https://arxiv.org/abs/2304.03516
- Recommender Systems with Generative Retrieval (TIGER): https://arxiv.org/abs/2305.05065
- Better Generalization with Semantic IDs: https://arxiv.org/abs/2306.08121
- Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations: https://arxiv.org/abs/2402.17152
- Meta generative-recommenders repository: https://github.com/meta-recsys/generative-recommenders
- Generative Recommendation with Semantic IDs: A Practitioner's Handbook: https://arxiv.org/abs/2507.22224
- Semantic IDs for Joint Generative Search and Recommendation: https://arxiv.org/abs/2508.10478
- Variable-Length Semantic IDs for Recommender Systems: https://arxiv.org/abs/2602.16375
- DAS: Dual-Aligned Semantic IDs Empowered Industrial Recommender System: https://arxiv.org/abs/2508.10584
- PinRec at Pinterest: https://arxiv.org/abs/2504.10507
- Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation: https://arxiv.org/abs/2604.04976

### LLM、扩散与基础模型推荐

- P5, Recommendation as Language Processing: https://arxiv.org/abs/2203.13366
- Chat-REC: https://arxiv.org/abs/2303.14524
- TALLRec: https://arxiv.org/abs/2305.00447
- GenRec, Large Language Model for Generative Recommendation: https://arxiv.org/abs/2307.00457
- LLM-Rec: https://arxiv.org/abs/2307.15780
- LLMRec: https://arxiv.org/abs/2311.00423
- GEMRec, Towards Generative Model Recommendation: https://arxiv.org/abs/2308.02205
- A Review of Modern Recommender Systems Using Generative Models: https://arxiv.org/abs/2404.00579
- A Survey on Diffusion Models for Recommender Systems: https://arxiv.org/abs/2409.05033
- Diffusion Models in Recommendation Systems: https://arxiv.org/abs/2501.10548
- Foundation Model-Powered Recommender Systems survey: https://arxiv.org/abs/2504.16420
- A Survey on Generative Recommendation: Data, Model, and Tasks: https://arxiv.org/abs/2510.27157

### 国内外产业落地材料

- Netflix recommendation system help page: https://help.netflix.com/en/node/100639
- Amazon Science two-tower video recommendation: https://www.amazon.science/publications/exploring-heterogeneous-metadata-for-video-recommendation-with-two-tower-model
- Pinterest PinRec: https://arxiv.org/abs/2504.10507
- Meta AI Drives Performance, GEM ads ranking model: https://about.fb.com/news/2026/01/2026-ai-drives-performance/
- ByteDance Monolith: https://arxiv.org/abs/2209.07663
- Alibaba DIN: https://arxiv.org/abs/1706.06978
- Alibaba DIEN: https://ojs.aaai.org/index.php/AAAI/article/view/4545
- Alibaba MIND at Tmall: https://arxiv.org/abs/1904.08030
- Taobao AIGQ query recommendation: https://arxiv.org/abs/2603.19710
- Taobao generative re-ranking: https://arxiv.org/abs/2505.07197
- Kuaishou OneMall: https://arxiv.org/abs/2601.21770
- Kuaishou DiffusionGS: https://arxiv.org/abs/2508.17754
- Kuaishou KuaiLive dataset: https://arxiv.org/abs/2508.05633
- TencentGR industrial all-modality benchmark: https://arxiv.org/abs/2604.04976

## Boundary

本报告不复述所有推荐系统论文，也不提供可直接上线的业务指标承诺。文中公司实践均来自公开资料；未公开的生产细节、真实业务收益、模型参数、训练数据和流量分配不做推测。趋势判断部分是基于公开论文、工程系统约束和产业方向的综合判断，不能替代具体公司的实验结论。
