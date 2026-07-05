# 京东 DOPD 论文 Review 2026

本目录是对 arXiv:2606.30626 `DOPD: Dual On-policy Distillation` 的独立论文 review。它与既有 `llm-opd-online-policy-distillation-2026` one-pager 不共用产物，也不覆盖旧 OPD 文稿。

## Files

- `index.html`: 正文与排版源文件。
- `jd-dopd-paper-review-2026.pdf`: 由 `index.html` 渲染得到的 PDF 成品。
- `sources.md`: 证据层级、来源边界和不确定性说明。
- `data/source-map.tsv`: 正文 claim 到来源的映射。
- `data/dopd-experiment-summary.csv`: 论文主要实验结果的结构化摘录。
- `data/dopd-routing-map.csv`: DOPD 四类 token 路由策略的结构化摘录。
- `sources/`: arXiv PDF、HTML 和文本抽取的本地证据快照。

## Scope

复核时间为 2026-07-07。正文只使用公开论文、arXiv 页面、官方模型资料和明确标注的背景材料，不把作者实验视为第三方复现。所有涉及性能、数据规模、模型配置和实验设计的数字，均回到论文表格或正文段落进行核对。
