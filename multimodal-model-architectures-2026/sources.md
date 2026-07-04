# Multimodal Model Architectures 2026 Sources

Source check date: 2026-07-07 (Asia/Shanghai).

本文优先使用论文原文、正式会议页面、官方研究博客和官方开源仓库。官方博客和仓库只用于说明公开能力、组件命名、工程接口和 release 状态；不据此反推未公开训练数据或闭源系统内部结构。预印本、官方自报 benchmark 与工业开源模型统一作为技术路线证据，不写成跨场景最优结论。

## Evidence levels

- **A**：正式会议、期刊论文，或论文最终公开版本。
- **B**：研究团队预印本，公开方法、实验与局限，但未必完成同行评审。
- **C**：官方研究博客、官方文档或官方开源仓库，可证明公开能力、组件接口与工程边界。
- **D**：厂商自报 benchmark、产品能力或工业实践信号，只作为趋势材料，不作独立验证。

| ID | Level | Source | URL | Main use |
|---|---|---|---|---|
| S01 | A | Learning representations by back-propagating errors | https://www.nature.com/articles/323533a0 | 反向传播、MLP 训练机制与可学习特征的历史起点 |
| S02 | A | Multilayer feedforward networks are universal approximators | https://doi.org/10.1016/0893-6080%2889%2990020-8 | MLP 表达能力边界与“能表示”和“能学好”的区分 |
| S03 | A | Attention Is All You Need | https://arxiv.org/abs/1706.03762 | Transformer、自注意力、序列并行建模与后续 ViT/VLM 的共同底座 |
| S04 | A | Deep Residual Learning for Image Recognition | https://arxiv.org/abs/1512.03385 | 残差连接、深层视觉骨干与 CNN 特征迁移 |
| S05 | A | An Image is Worth 16x16 Words | https://arxiv.org/abs/2010.11929 | ViT patch token 化、全局自注意力视觉编码器与大数据预训练依赖 |
| S06 | A | Training data-efficient image transformers & distillation through attention | https://arxiv.org/abs/2012.12877 | DeiT、蒸馏 token 与小数据训练 ViT 的工程意义 |
| S07 | A | MLP-Mixer: An all-MLP Architecture for Vision | https://arxiv.org/abs/2105.01601 | token-mixing/channel-mixing、全 MLP 视觉骨干与归纳偏置对比 |
| S08 | A | Swin Transformer: Hierarchical Vision Transformer using Shifted Windows | https://arxiv.org/abs/2103.14030 | 层级视觉 Transformer、窗口注意力、密集预测与通用视觉骨干 |
| S09 | A | BEiT: BERT Pre-Training of Image Transformers | https://arxiv.org/abs/2106.08254 | masked image modeling 与视觉 token 预测 |
| S10 | A | Masked Autoencoders Are Scalable Vision Learners | https://arxiv.org/abs/2111.06377 | MAE、非对称编码器-解码器、高遮盖率与自监督预训练 |
| S11 | A | Emerging Properties in Self-Supervised Vision Transformers | https://arxiv.org/abs/2104.14294 | DINO、自蒸馏、ViT 自监督特征与 kNN/检索能力 |
| S12 | B | DINOv2: Learning Robust Visual Features without Supervision | https://arxiv.org/abs/2304.07193 | 通用视觉特征、数据 curated pipeline、蒸馏与无标签视觉表征 |
| S13 | A | ViLBERT | https://arxiv.org/abs/1908.02265 | 双流视觉语言 BERT、co-attention 与早期 region-level VLP |
| S14 | A | LXMERT | https://arxiv.org/abs/1908.07490 | object relationship encoder、language encoder、cross-modality encoder |
| S15 | A | UNITER | https://arxiv.org/abs/1909.11740 | 联合图文编码、条件遮盖、ITM 与词区对齐 |
| S16 | A | Learning Transferable Visual Models From Natural Language Supervision | https://arxiv.org/abs/2103.00020 | CLIP、双塔图文对比学习、自然语言监督与零样本分类 |
| S17 | A | Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision | https://arxiv.org/abs/2102.05918 | ALIGN、十亿级噪声 alt-text、规模与噪声的取舍 |
| S18 | A | Sigmoid Loss for Language Image Pre-Training | https://arxiv.org/abs/2303.15343 | SigLIP、pairwise sigmoid loss 与 batch/global softmax 解耦 |
| S19 | B | SigLIP 2 | https://arxiv.org/abs/2502.14786 | 多语言图文 encoder、caption/self-supervised/online curation 组合 recipe |
| S20 | A | BLIP | https://arxiv.org/abs/2201.12086 | MED 架构、caption bootstrapping、理解与生成统一 |
| S21 | A | BLIP-2 | https://arxiv.org/abs/2301.12597 | 冻结视觉编码器、冻结 LLM、Q-Former 与两阶段桥接 |
| S22 | A | CoCa | https://arxiv.org/abs/2205.01917 | 对比损失与 captioning 损失合并的 encoder-decoder 设计 |
| S23 | A | PaLI | https://arxiv.org/abs/2209.06794 | 多语言生成式 VLM、视觉与语言组件共同扩展 |
| S24 | B/C | PaliGemma | https://arxiv.org/abs/2407.07726 | SigLIP encoder + Gemma decoder、开放 VLM transfer 模型 |
| S25 | B/C | Gemma explained: PaliGemma architecture | https://developers.googleblog.com/gemma-explained-paligemma-architecture/ | PaliGemma 公开架构、SigLIP 与 Gemma 组合说明 |
| S26 | A | Visual Instruction Tuning | https://arxiv.org/abs/2304.08485 | LLaVA、视觉编码器到 LLM 的投影连接与视觉指令数据 |
| S27 | A | ImageBind | https://arxiv.org/abs/2305.05665 | 图像枢纽、多模态共享 embedding 与跨模态检索 |
| S28 | B | 4M: Massively Multimodal Masked Modeling | https://arxiv.org/abs/2312.06647 | 多输入多输出、离散 token 化、any-to-any masked modeling |
| S29 | B | Chameleon | https://arxiv.org/abs/2405.09818 | mixed-modal early fusion、统一 token 序列与图文生成 |
| S30 | A | ColBERT | https://arxiv.org/abs/2004.12832 | late interaction、多向量检索与离线预编码 |
| S31 | B/C | ColPali | https://arxiv.org/abs/2407.01449 | 视觉文档检索、VLM multi-vector embedding 与 late interaction |
| S32 | B | VLM2Vec | https://arxiv.org/abs/2410.05160 | 把 VLM 转成通用多模态 embedding 模型、MMEB 评测 |
| S33 | A/C | Billion-scale similarity search with GPUs / Faiss | https://arxiv.org/abs/1702.08734 | 向量检索系统、GPU k-selection、PQ/IVF 工程边界 |
| S34 | A | HNSW | https://arxiv.org/abs/1603.09320 | 图索引、近似最近邻、多层 navigable small world 结构 |
| S35 | C | OpenAI CLIP blog | https://openai.com/index/clip/ | CLIP 公开能力与自然语言监督产品化说明 |
| S36 | C | OpenAI CLIP GitHub | https://github.com/openai/CLIP | CLIP 官方代码与模型 release 状态 |
| S37 | C | Google Research big_vision | https://github.com/google-research/big_vision | ViT、MLP-Mixer、LiT、SigLIP/SigLIP2 公开训练代码库 |
| S38 | C | Salesforce BLIP GitHub | https://github.com/salesforce/BLIP | BLIP 官方代码、模型与公开接口 |
| S39 | C | Salesforce LAVIS | https://github.com/salesforce/LAVIS | BLIP-2/LAVIS 统一接口、特征抽取与任务支持 |
| S40 | A | A ConvNet for the 2020s | https://arxiv.org/abs/2201.03545 | ConvNeXt、现代化 ConvNet 与视觉 Transformer 的对照 |

## Conflicts and interpretation boundaries

- **MLP 能表达，不代表它最适合视觉。** Universal approximation 说明前馈网络有足够表达能力 [S02]；MLP-Mixer 说明在大规模数据和现代正则下，全 MLP 也能成为视觉骨干 [S07]。但 CNN、ViT、Swin 和 ConvNeXt 仍通过归纳偏置、层级结构或注意力机制改变样本效率、密集预测和计算形态 [S04-S08, S40]。正文据此把 MLP 写成基本算子和对照组，不写成视觉模型的终局。
- **双塔、跨注意力、桥接器和早融合服务不同接口。** ViLBERT/LXMERT/UNITER 证明跨模态联合编码适合细粒度关系推理 [S13-S15]；CLIP/ALIGN/SigLIP 证明双塔适合离线编码、图搜和零样本分类 [S16-S18]；BLIP-2、PaliGemma、LLaVA 证明桥接器适合复用冻结骨干和 LLM [S21, S24-S26]；4M/Chameleon 证明统一 token 路线有 any-to-any 潜力 [S28, S29]。正文不把这些路线排成单一优劣表，而按接口、延迟、数据和错误成本选择。
- **图文对齐不是完整视觉理解。** CLIP、ALIGN、SigLIP 的核心能力是把图像和文本投到可比较空间 [S16-S18]；BLIP、CoCa、PaLI、PaliGemma 等生成式 VLM 能输出语言，但输出语言并不自动证明定位、计数、OCR、图表理解或复杂推理可靠 [S20-S26]。正文把“可检索”“可对话”“可执行”分开。
- **开源仓库和官方博客是工程证据，不是训练细节证明。** CLIP、BLIP、LAVIS、big_vision 等仓库可证明公开代码、权重或接口 [S36-S39]；未公开数据配方、过滤规则、闭源产品内部结构不在本文断言范围内。
- **2024-2026 的 embedding/VLM 预印本是前沿信号。** ColPali、VLM2Vec、SigLIP2、PaliGemma 等说明图搜、文档检索、多语言和 VLM-to-vector 正在合流 [S19, S24, S31, S32]；它们不能直接替代垂直行业线上 A/B 结果。

## Deliberately excluded claims

- 不声称某个模型家族在所有多模态任务上“最好”。
- 不把论文 benchmark 写成线上业务收益。
- 不把开源 checkpoint 的可运行性写成可直接生产上线。
- 不推断闭源商业模型的内部架构。
- 不讨论图像生成扩散模型的采样细节；本文只在 Chameleon/4M 相关处讨论统一 token 或 any-to-any 路线。
