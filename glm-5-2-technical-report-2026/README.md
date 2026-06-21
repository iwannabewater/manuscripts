# GLM-5.2 Technical Report 2026

GLM-5.2 的中文深度技术解读，覆盖 1M 上下文、IndexShare/IndexCache、DSA、MTP 推测解码、slime、并行 OPD、critic-based PPO、反作弊、长时 Agent 评测、推理部署与开放权重边界。

## Files

- `index.html`: 可读与可打印的报告源码。
- `glm-5-2-technical-report-2026.pdf`: PDF 成品。
- `sources.md`: 一手来源、外部评测、口径冲突与边界。
- `data/source-map.tsv`: 正文来源编号与 URL 映射。
- `data/benchmark-summary.tsv`: 正文引用的关键评测数据与口径。

## Scope

报告以 Z.ai 官方发布博客、Hugging Face 模型卡与配置、GLM-5/IndexCache/Bebop 论文、slime 仓库和官方推理框架文档为主要事实依据，并用 Artificial Analysis、FrontierSWE、PostTrainBench、SWE-Marathon 补充独立评测。官方 benchmark、独立测量和本文工程推断在正文中分开标记。

本文没有对 744B 权重做本地推理，没有复现 1M token 服务吞吐，也没有把社交媒体体验当作性能证据。排行榜、价格、配额与框架版本按 2026-06-22 的页面状态记录。
