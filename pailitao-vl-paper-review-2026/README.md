# Pailitao-VL Paper Review 2026

本目录是对 Alibaba Group 论文 `Pailitao-VL: Unified Embedding and Reranker for Real-Time Multi-Modal Industrial Search` 的中文深度 review。评审对象为 arXiv:2602.13704v2，重点覆盖算法思路、公式、实现链路、实验收益、线上可用性与稳定工作边界。

## Files

- Public HTML: <https://whynotsleep.cc/manuscripts/pailitao-vl-paper-review-2026/>
- Public PDF: <https://whynotsleep.cc/manuscripts/pailitao-vl-paper-review-2026/pailitao-vl-paper-review-2026.pdf>
- `index.html`: 正文与排版源文件。
- `build_math.py`: 从 LaTeX 公式生成路径化 SVG 数学资产。
- `assets/math/`: PDF 与 HTML 共用的公式 SVG。
- `pailitao-vl-paper-review-2026.pdf`: 由 `index.html` 渲染得到的 PDF 成品。
- `sources.md`: 证据等级、来源边界和不确定性说明。
- `data/source-map.tsv`: 正文 claim 到来源的映射。
- `data/method-map.tsv`: Embedding 与 Reranker 方法组件、实现细节、收益和风险的结构化映射。
- `data/embedding-offline-results.csv`: 论文表 1 的结构化摘录。
- `data/reranker-offline-results.csv`: 论文表 2 的结构化摘录。
- `data/reranker-classification-results.csv`: 论文表 3 的结构化摘录。
- `data/reranker-ablation-results.csv`: 论文表 4 的结构化摘录。
- `data/reranker-efficiency.csv`: 论文表 5 的结构化摘录。
- `sources/`: arXiv PDF、TeX 源包与文本抽取的本地证据快照。

## Scope

证据复核时间为 2026-07-08，北京时间。本文只使用公开论文、arXiv 页面、arXiv TeX 源包和明确标注的背景论文，不把作者线上 A/B 和 GMV 指标表述为第三方复现结果。本文未获得 Pailitao-VL 的公开代码、训练数据、线上流量分桶或完整日志，因此所有稳定性判断均为基于论文披露信息的工程评审。

## Reproduce

```bash
make fonts
.venv/bin/python pailitao-vl-paper-review-2026/build_math.py
.venv/bin/python -c "from pathlib import Path; from weasyprint import HTML; d=Path('pailitao-vl-paper-review-2026'); HTML(filename=str(d/'index.html'), base_url=str(d)).write_pdf(str(d/'pailitao-vl-paper-review-2026.pdf'))"
make verify
```
