# Ecommerce Visual Search Recall Papers 2026

交付内容：

- `index.html`：可阅读、可打印的中文研究读物源文件。
- `ecommerce-visual-search-recall-papers-2026.pdf`：正式 PDF 成品。
- `sources.md`：来源、证据等级、事实边界、口径和不确定性说明。
- `data/paper-list.tsv`：论文清单、任务、方法、收益和稳定性判断。
- `data/source-map.tsv`：来源到正文事实的映射。
- `data/method-taxonomy.tsv`：方法族、核心公式、适用场景和工程风险。

重新生成 PDF：

```bash
cd ecommerce-visual-search-recall-papers-2026
../.venv/bin/python -c "from weasyprint import HTML; HTML('index.html', base_url='.').write_pdf('ecommerce-visual-search-recall-papers-2026.pdf')"
```

核验：

```bash
make verify
make verify-network
pdfinfo ecommerce-visual-search-recall-papers-2026/ecommerce-visual-search-recall-papers-2026.pdf
pdffonts ecommerce-visual-search-recall-papers-2026/ecommerce-visual-search-recall-papers-2026.pdf
```
