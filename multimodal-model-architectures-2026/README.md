# Multimodal Model Architectures 2026

交付内容：

- `index.html`：可阅读、可打印的 Winston 中文长文档源文件。
- `multimodal-model-architectures-2026.pdf`：正式 PDF 成品。
- `sources.md`：来源、证据等级、事实边界与研究方法。
- `data/source-map.tsv`：来源到正文用途的映射。
- `data/model-taxonomy.tsv`：代表性模型、结构类型、训练目标、接口与适用场景映射。

重新生成 PDF：

```bash
cd multimodal-model-architectures-2026
../.venv/bin/python -c "from weasyprint import HTML; HTML('index.html', base_url='.').write_pdf('multimodal-model-architectures-2026.pdf')"
```

核验：

```bash
make verify
make verify-network
pdfinfo multimodal-model-architectures-2026/multimodal-model-architectures-2026.pdf
pdffonts multimodal-model-architectures-2026/multimodal-model-architectures-2026.pdf
```
