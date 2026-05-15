# Sources

作者：Winston
资料口径：截至 2026-05-15
主题：世界模型（World Models）的发展史、主流算法、产业落地与趋势

## Method

本报告优先采用论文原文、公司官方技术报告、官方模型页、官方博客、开源仓库和研究项目页。对 2025-2026 年新发布的产业模型，只把公开材料中明确声明的能力、定位、输入输出和开放方式写入正文；不把未公开训练数据、未披露线上指标或营销性比较当作事实。新闻材料仅用于补充产业动向，不作为核心技术结论。

世界模型横跨强化学习、视频生成、机器人、自动驾驶、3D 生成和智能体系统，术语使用差异很大。本文将“世界模型”限定为：能够学习环境状态、动态、动作后果、可观测未来或交互式模拟，并服务于预测、规划、控制、评估、生成数据或空间构建的模型。纯图像生成、纯语言模型和普通数字孪生不单独视为世界模型，除非它们显式建模时间、动作或可交互环境。

## Primary Sources

### 概念源流与模型式强化学习

- Dyna, integrated learning/planning/reacting architecture: https://explore.openaire.eu/search/publication?pid=10.1145%2F122344.122377
- World Models, Ha and Schmidhuber: https://arxiv.org/abs/1803.10122
- PlaNet, Learning Latent Dynamics for Planning from Pixels: https://arxiv.org/abs/1811.04551
- MuZero, Nature paper: https://www.nature.com/articles/s41586-020-03051-4
- MuZero, Google DeepMind blog: https://deepmind.google/blog/muzero-mastering-go-chess-shogi-and-atari-without-rules/
- DreamerV3: https://arxiv.org/abs/2301.04104
- Mastering diverse control tasks through world models, Nature: https://www.nature.com/articles/s41586-025-08744-2
- TD-MPC2: https://arxiv.org/abs/2310.16828
- MBPO, When to Trust Your Model: Model-Based Policy Optimization: https://arxiv.org/abs/1906.08253
- EfficientZero: https://arxiv.org/abs/2111.00210
- IRIS, Transformers are sample-efficient world models: https://arxiv.org/abs/2209.00588

### JEPA、预测表征与基础世界模型

- A Path Towards Autonomous Machine Intelligence, Yann LeCun: https://openreview.net/pdf?id=BZ5a1r-kVsf
- I-JEPA: https://arxiv.org/abs/2301.08243
- V-JEPA: https://arxiv.org/abs/2404.08471
- Meta V-JEPA blog: https://ai.meta.com/blog/v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture/
- Meta V-JEPA 2 blog: https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/
- facebookresearch/jepa repository: https://github.com/facebookresearch/jepa

### 视频、交互式环境与世界基础模型

- OpenAI Sora technical report, Video generation models as world simulators: https://openai.com/index/video-generation-models-as-world-simulators/
- Google DeepMind Genie: https://deepmind.google/research/publications/genie-generative-interactive-environments/
- Genie paper: https://arxiv.org/abs/2402.15391
- Google DeepMind Genie 3 model page: https://deepmind.google/models/genie/
- NVIDIA Cosmos platform: https://www.nvidia.com/en-us/ai/cosmos/
- NVIDIA Cosmos launch blog: https://blogs.nvidia.com/blog/cosmos-world-foundation-models/
- Cosmos World Foundation Model Platform paper: https://arxiv.org/abs/2501.03575
- Cosmos-Predict1 research page: https://research.nvidia.com/labs/cosmos-lab/cosmos-predict1/
- Runway GWM-1: https://runwayml.com/research/introducing-runway-gwm-1
- Runway available models: https://help.runwayml.com/hc/en-us/articles/48649877897107-Available-Models-on-Runway
- World Labs Marble docs: https://docs.worldlabs.ai/
- UniSim, Learning Interactive Real-World Simulators: https://arxiv.org/abs/2310.06114
- UniSim, Google DeepMind page: https://deepmind.google/research/publications/47545/

### 机器人、自动驾驶与物理 AI

- GAIA-1, Wayve technical report: https://arxiv.org/abs/2309.17080
- Wayve GAIA-1 official page: https://wayve.ai/press/wayve-releases-gaia-1-technical-report/
- Wayve Scaling GAIA-1: https://wayve.ai/thinking/scaling-gaia-1/
- GAIA-2: https://arxiv.org/abs/2503.20523
- Waymo World Model: https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/
- Waymo Waymax simulator: https://waymo.com/blog/2023/10/waymo-advances-ai-research-with-our-multifunctional-waymax-simulator
- World Models for Autonomous Driving survey: https://arxiv.org/abs/2501.11260
- FOCUS object-centric world models for robotic manipulation: https://arxiv.org/abs/2307.02427
- RoboDreamer: https://arxiv.org/abs/2404.12377
- IRASim project page: https://gen-irasim.github.io/
- IRASim GitHub: https://github.com/bytedance/IRASim
- World Model for Robot Learning survey: https://huggingface.co/papers/2605.00080

### 国内公开材料与 3D / 空间智能

- Tencent HunyuanWorld-1.0 GitHub: https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0
- Tencent HunyuanWorld 1.0 technical report: https://3d-models.hunyuan.tencent.com/world/HY_World_1_technical_report.pdf
- Tencent HunyuanWorld 1.5 technical report: https://3d-models.hunyuan.tencent.com/world/world1_5/HYWorld_1.5_Tech_Report.pdf
- Tencent Hunyuan 3D engine global launch: https://www.tencent.com/en-us/articles/2202235.html
- Alibaba Wan2.2 official release: https://www.alibabacloud.com/en/press-room/alibaba-releases-wan2-2-to-uplift-cinematic
- Huawei Intelligent World Cloud Computing 2024 report: https://www-file.huawei.com/-/media/corp2020/pdf/giv/striding-towards-the-intelligent-world/2024/intelligent_world_cloud_computing_2024_en.pdf

## Boundary

本文不复述全部模型式强化学习或视频生成论文，也不评测各商业模型优劣。涉及“第一”“最强”“实时”等公开声明时，正文只保留来源方的可核实表述，并明确其上下文。世界模型的工程价值高度依赖任务、数据、闭环验证和安全边界，本报告不能替代具体机器人、自动驾驶、游戏或工业系统的实测结论。
