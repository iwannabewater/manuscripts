# E-commerce Visual Search Embedding 2026

交付内容：

- `index.html`：可阅读、可打印的 Winston 中文长文档源文件。
- `ecommerce-visual-search-embedding-2026.pdf`：正式 PDF 成品。
- `sources.md`：来源、证据等级、事实边界与研究方法。
- `data/source-map.tsv`：来源到正文用途的映射。
- `data/pipeline-map.tsv`：表征范式、训练信号、适用场景与风险映射。

重新生成 PDF：

```bash
cd ecommerce-visual-search-embedding-2026
../.venv/bin/python -c "from weasyprint import HTML; HTML('index.html', base_url='.').write_pdf('ecommerce-visual-search-embedding-2026.pdf')"
```

核验：

```bash
make verify
make verify-network
pdfinfo ecommerce-visual-search-embedding-2026/ecommerce-visual-search-embedding-2026.pdf
pdffonts ecommerce-visual-search-embedding-2026/ecommerce-visual-search-embedding-2026.pdf
```
