# macOS Developer Handbook 2026

面向开发者的新机上手与长期维护手册。内容从 macOS 原生操作开始，逐步落到 Homebrew、Brewfile、Ghostty、mise、uv、OrbStack、Mole、权限治理、备份恢复和可复现 SOP。

正文资料口径截至 `2026-06-02`，平台状态于 `2026-06-09` 复核。稳定工作站基线仍为 macOS Tahoe 26.5；WWDC26 已发布 macOS 27 与 Xcode 27 beta，beta 环境应与日常主力机分开评估。文中软件分为默认安装、按痛点安装和谨慎处理三层，不主张把推荐列表一次性装满。

## Deliverables

- `index.html`：可读、可打印的排版源文件。
- `macos-developer-handbook-2026.pdf`：正式 PDF 成品。
- `guide.md`：handbook 正文。
- `CHEATSHEET.md`：可独立打印的快捷参考。
- `sources.md`：来源、方法与边界。
- `research-notes.md`：社区信号与取舍记录。
- `data/source-map.tsv`：逐条可复查的公开来源。

## Build

```bash
python3 build_paper.py
weasyprint index.html macos-developer-handbook-2026.pdf
python3 build_paper.py
weasyprint index.html macos-developer-handbook-2026.pdf
python3 build_paper.py --public-html
```

第二轮构建用于把 PDF 页码回填到目录中，最后一步输出公开 HTML。正式发布前还应运行 `pdffonts`、`pdftotext` 和逐页渲染检查。
