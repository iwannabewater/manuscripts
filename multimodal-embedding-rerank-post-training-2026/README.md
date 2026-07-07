# 多模态 Embedding/Rerank 后训练 2026

本文是一份面向检索、搜索、推荐与知识库系统的技术研究读物，系统梳理截至 2026-07-07 公开资料中的多模态 embedding 与 rerank 后训练方案。

## 文件

- `index.html`：排版源文件与浏览器阅读版本。
- `multimodal-embedding-rerank-post-training-2026.pdf`：PDF 成品，由 `index.html` 渲染。
- `sources.md`：资料来源、证据等级、口径边界与不覆盖范围。
- `data/source-map.tsv`：声明与来源映射。
- `data/method-map.tsv`：训练方法、适用模型面、风险与证据映射。
- `data/feasibility-matrix.tsv`：SFT、RL、OPD 在 embedding 与 rerank 上的可行性矩阵。

## 证据日期

资料复核日期为 2026-07-07。涉及模型榜单、API 能力、产品限制、论文版本与工业结果的内容均按该日期解释。

## 复现

```bash
make fonts
.venv/bin/python -c "from pathlib import Path; from weasyprint import HTML; d=Path('multimodal-embedding-rerank-post-training-2026'); HTML(filename=str(d/'index.html'), base_url=str(d)).write_pdf(str(d/'multimodal-embedding-rerank-post-training-2026.pdf'))"
make verify
```
