# Multimodal Representations 2026

交付内容：

- `index.html`：可阅读、可打印的 Winston 中文长文档源文件。
- `multimodal-representations-2026.pdf`：正式 PDF 成品。
- `sources.md`：来源、证据等级、事实边界与研究方法。
- `data/source-map.tsv`：来源到正文用途的映射。
- `data/model-map.tsv`：代表性方法、训练目标、结构路线与适用场景映射。

重新生成 PDF：

```bash
cd multimodal-representations-2026
../.venv/bin/python -c "from weasyprint import HTML; HTML('index.html', base_url='.').write_pdf('multimodal-representations-2026.pdf')"
```

核验：

```bash
make verify
make verify-network
pdfinfo multimodal-representations-2026/multimodal-representations-2026.pdf
pdffonts multimodal-representations-2026/multimodal-representations-2026.pdf
```
