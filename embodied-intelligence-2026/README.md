# 具身智能入门与技术栈全景报告 2026

这是一个独立长文档项目，面向希望从零建立具身智能全局认知的技术读者。交付物包括：

- `index.html`: 可阅读、可打印的 Kami 长文档源文件
- `embodied-intelligence-2026.pdf`: 已构建 PDF
- `sources.md`: 资料清单
- `data/source-map.tsv`: 事实来源映射

## 构建

在本目录执行：

```bash
python3 -c "from weasyprint import HTML; HTML('index.html', base_url='.').write_pdf('embodied-intelligence-2026.pdf')"
```

字体文件已随目录放在 `fonts/`，用于稳定中文 PDF 渲染。
