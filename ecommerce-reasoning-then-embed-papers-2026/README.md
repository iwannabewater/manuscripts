# 电商图搜多模态表征 Paper List 2026：工业部署、推理增强与低延迟

交付内容：

- `index.html`：可阅读、可打印的中文清单源文件
- `ecommerce-reasoning-then-embed-papers-2026.pdf`：正式 PDF 成品
- `sources.md`：来源、证据等级、口径与不确定性
- `data/paper-list.tsv`：15 篇论文清单
- `data/source-map.tsv`：来源到正文事实的映射
- `data/reading-paths.tsv`：按角色/场景的连读路径

与《电商图搜召回 Paper List 2026》的关系：并列读物。本文围绕电商图搜多模态表征精读，其中严格 Reasoning-then-Embed 仅为方法族之一；不覆盖也不替换更广的图搜召回 paper list。

重新生成 PDF：

```bash
cd ecommerce-reasoning-then-embed-papers-2026
../.venv/bin/python -c "from weasyprint import HTML; HTML('index.html', base_url='.').write_pdf('ecommerce-reasoning-then-embed-papers-2026.pdf')"
```

核验：

```bash
make verify
make verify-network
pdfinfo ecommerce-reasoning-then-embed-papers-2026/ecommerce-reasoning-then-embed-papers-2026.pdf
pdffonts ecommerce-reasoning-then-embed-papers-2026/ecommerce-reasoning-then-embed-papers-2026.pdf
```
