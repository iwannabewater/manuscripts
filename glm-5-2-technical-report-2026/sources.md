# Sources

## Source Policy

模型架构、训练方法、许可、配置和官方 benchmark 优先使用 Z.ai、模型仓库、论文和项目文档。Artificial Analysis、FrontierSWE、PostTrainBench 与 SWE-Marathon 作为外部测量使用，不替代官方架构事实。Jie Tang 的公开发言只用于解释开放权重的建设者立场，不作为独立性能证据。

正文中的来源编号对应 `data/source-map.tsv`。所有页面于 2026-06-22 重新核验。发布方自评、外部评测与作者分析分开表述。

## Primary Sources

1. **[S01] Z.ai, `GLM-5.2: Built for Long-Horizon Tasks`**, 2026-06-17.
   https://z.ai/blog/glm-5.2
   5.2 新增能力、IndexShare、MTP 消融、1M 服务、slime、并行 OPD、critic-based PPO、反作弊与官方 benchmark。

2. **[S02] zai-org, `GLM-5.2 Model Card`**.
   https://huggingface.co/zai-org/GLM-5.2
   权重、MIT 许可、官方 benchmark、支持框架与引用关系。

3. **[S03] zai-org, `GLM-5.2 config.json`**.
   https://huggingface.co/zai-org/GLM-5.2/blob/main/config.json
   78 层、256 路由专家、top-8、top-2048、四层 index share 与 1,048,576 配置最大序列长度。

4. **[S04] GLM-5 Team, `GLM-5: from Vibe Coding to Agentic Engineering`**, arXiv:2602.15763.
   https://arxiv.org/abs/2602.15763
   GLM-5 基座的 744B 总参数、每 token 约 40B 参与计算参数、DSA、共享参数 MTP、预训练与异步 Agentic RL。

5. **[S05] Bai et al., `IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse`**, arXiv:2603.12201.
   https://arxiv.org/abs/2603.12201
   跨层索引复用的动机、训练无关/训练感知方法与 30B DSA 实验。

6. **[S06] Li et al., `Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling`**, arXiv:2606.12370.
   https://arxiv.org/abs/2606.12370
   RL 阶段 MTP 熵界、概率拒绝采样、端到端 TV loss 与异步 RL 加速。

7. **[S07] THUDM/slime**.
   https://github.com/THUDM/slime
   训练、rollout、Data Buffer、SGLang 原生集成、Agentic RL 与 OPD 基础设施。

8. **[S08] Z.ai Developer Docs, `Thinking Mode`**.
   https://docs.z.ai/guides/capabilities/thinking-mode
   默认 thinking、interleaved thinking、preserved thinking 与客户端契约。

9. **[S09] Z.ai Developer Docs, `GLM Coding Plan Overview`**.
   https://docs.z.ai/devpack/overview
   支持模型、配额倍数、促销日期、峰谷时段与使用边界。

10. **[S10] vLLM Recipes, `zai-org/GLM-5.2`**.
    https://recipes.vllm.ai/zai-org/GLM-5.2
    FP8/BF16、H200/B200、完整 1M、MTP、reasoning effort 与调优建议。

11. **[S11] SGLang Documentation, `GLM-5.2`**.
    https://cookbook.sglang.io/autoregressive/GLM/GLM-5.2
    DSA backend、MTP、context parallelism、chunked prefill、BF16/FP8 内存与硬件矩阵。

12. **[S12] KTransformers, `GLM-5.2 Tutorial`**.
    https://github.com/kvcache-ai/ktransformers/blob/main/doc/en/kt-kernel/GLM-5.2-Tutorial.md
   CPU-GPU 异构专家卸载、SGLang/KT-Kernel 启动参数与显存溢出（OOM）调节项。

## Independent Evaluation And Expert Context

13. **[S13] Artificial Analysis, `GLM-5.2 is the new leading open weights model on the Artificial Analysis Intelligence Index`**, 2026-06-17.
    https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index
    Intelligence Index v4.1、GDPval-AA v2、token 用量、每任务成本、价格与开放权重同类比较。

14. **[S14] Artificial Analysis, `GLM-5.2 (max) Model Page`**.
    https://artificialanalysis.ai/models/glm-5-2
    当前 intelligence、速度、价格、上下文、参数元数据与指标说明。

15. **[S15] FrontierSWE**.
    https://www.frontierswe.com/
    当前排行榜、harness、平均排名、Dominance、实现/研究/性能任务明细。

16. **[S16] PostTrainBench**.
    https://posttrainbench.com/
    10 小时单 H100 后训练任务、当前排名、6 月 17 日重跑变更、污染与奖励投机（reward hacking）分析。

17. **[S17] SWE-Marathon**.
    https://www.swe-marathon.org/
    20 个多小时软件工程任务与整体成功率边界。GLM-5.2 的 13 分取自 Z.ai 官方表。

18. **[S18] Jie Tang, GLM-5.2 release commentary**, 2026-06-13.
    https://x.com/jietang/status/2065784751345287314
    建设者对开放、可访问与可构建性的立场。

19. **[S19] Tsinghua KEG, `Jie Tang Academic Homepage`**.
    https://keg.cs.tsinghua.edu.cn/jietang/
    清华大学教授与 ACM/AAAI/IEEE Fellow 身份核验。

## Conflicts And Resolution

- **PostTrainBench 排名**：Z.ai 博客发布时称 GLM-5.2 第二。PostTrainBench 在 2026-06-17 把 Opus 4.8 Max 从单次 37.2% 更新为两次平均 34.1%，GLM-5.2 随后升到当前第一。正文采用评测方当前状态，并说明时间变化。
- **参数量**：GLM-5 报告与 Artificial Analysis 文章写 744B/40B，vLLM 写约 743B/39B，Artificial Analysis 模型页写 753B/40B。正文采用官方报告的约 744B/40B，外部口径保留在边界说明。
- **IndexShare / IndexCache**：Z.ai 使用 IndexShare 描述 GLM-5.2 的四层共享实例，链接论文题名为 IndexCache。正文同时保留两种名称并解释层级关系。
- **开放表述**：官方使用 open-source。本文采用更窄的「MIT 许可开放权重」，因为训练数据、完整配方与算力预算未全部公开。
- **框架版本**：模型卡列表中的 Transformers 版本文本与 `config.json` 记录存在可疑差异。正文不依赖该版本号，部署时以各框架当前 recipe 为准。

## Verification Notes

- 所有 benchmark 数字均带来源和 harness 边界；不同 benchmark 不比较绝对分数。
- 论文中的 30B IndexCache 速度与 Qwen 系列 Bebop 速度只解释方法，不写成 GLM-5.2 实测。
- 1.49 TB BF16 与约 744 GB FP8 为按 744B 参数做的理论权重体积估算，不含 KV cache 和运行时开销；SGLang 文档独立给出 BF16 约 1.5 TB。
- 本文没有运行 GLM-5.2 权重、重跑 benchmark 或复现 1M token 服务。

## Out Of Scope

- 未使用无法追溯的泄露、匿名爆料或单次聊天截图。
- 未把供应商 benchmark 当作第三方复现。
- 未覆盖模型安全、红队、偏见与多语言能力的完整评估。
- 未给出生产 SLA、GPU 租赁报价或长期价格预测。
