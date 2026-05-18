# verl RL Training Framework 2026

这份文档系统整理 `verl` 大模型强化学习训练框架，目标是让读者从 0 到 1 理解其问题背景、HybridFlow 架构、Ray 单控制器、WorkerGroup、DataProto、Actor/Rollout/Ref/Critic 角色、训练循环、算法配置、扩展点与调试路线。

## 文件

- `index.html`：排版源文件，可在浏览器中阅读，也可用 WeasyPrint 生成 PDF。
- `verl-rl-training-framework-2026.pdf`：正式 PDF 成品。
- `sources.md`：资料来源、版本口径与事实边界。
- `data/source-map.tsv`：来源映射表。
- `fonts/`：本作品自足渲染所需字体。

## 版本口径

资料核对日期：2026-05-18。

主要技术事实来自 `verl-project/verl` 官方仓库、官方 ReadTheDocs 文档、当前 `main` 分支源码浅克隆，以及 HybridFlow / DAPO / DeepSeekMath 等论文页面。文档中凡涉及“当前主线”均按本次核对的 `main` commit `657cfa5` 表述；凡涉及发布标签，按远端标签列表中最新的 `v0.7.1` 表述。

