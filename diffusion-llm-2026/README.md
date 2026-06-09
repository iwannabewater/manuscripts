# Diffusion LLM 2026

交付内容：

- `index.html`：可阅读、可打印的 Kami 长文档源文件。
- `diffusion-llm-2026.pdf`：正式 PDF 成品。
- `sources.md`：来源说明与事实边界。
- `data/source-map.tsv`：来源到正文用途的映射。

重新生成 PDF：

```bash
python3 -c "from weasyprint import HTML; HTML('index.html', base_url='.').write_pdf('diffusion-llm-2026.pdf')"
```

核验建议：

```bash
make verify
pdfinfo diffusion-llm-2026.pdf
pdftotext diffusion-llm-2026.pdf - | head
```
