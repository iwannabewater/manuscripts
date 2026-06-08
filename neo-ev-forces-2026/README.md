# 蔚小理 2026 发展现状与前景分析

This project contains a deep-research paper on NIO, XPENG and Li Auto as of 2026-05-30 Asia/Shanghai.

## Outputs

- `analysis.md`: long-form Chinese analysis with source IDs.
- `index.html`: Kami-styled paper source.
- `neo-ev-forces-2026.pdf`: rendered PDF output.
- `data/`: structured CSV/TSV snapshots used in the analysis.
- `sources/`: fetched Markdown source snapshots.

## Build

```bash
python3 -c "from weasyprint import HTML; HTML('index.html', base_url='.').write_pdf('neo-ev-forces-2026.pdf')"
```
