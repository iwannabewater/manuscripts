# RAG Frontiers 2026

交付内容：

- `index.html`：可阅读、可打印的 Kami 长文档源文件。
- `rag-frontiers-2026.pdf`：正式 PDF 成品。
- `sources.md`：来源、证据等级、事实边界与研究方法。
- `data/source-map.tsv`：来源到正文用途的映射。
- `data/method-map.tsv`：经典、Advanced 与 Frontier RAG 方法地图。
- `sources/raw/` 与 `sources/full/`：研究时归档的公开证据快照。

重新生成 PDF：

```bash
cd rag-frontiers-2026
../.venv/bin/python -c "from weasyprint import HTML; HTML('index.html', base_url='.').write_pdf('rag-frontiers-2026.pdf')"
```

核验：

```bash
make verify
make verify-network
pdfinfo rag-frontiers-2026.pdf
pdffonts rag-frontiers-2026.pdf
```
