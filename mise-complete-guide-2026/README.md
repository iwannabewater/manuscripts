# mise Complete Guide 2026

署名：Winston
资料口径：截至 2026-06-02
交付形态：Kami 中文技术长文，A4 PDF

本目录收录《mise 完整使用指南：开发环境、工具链与工程任务的统一管理》。手册面向需要管理多语言运行时、项目环境变量、常用工程任务和 CI 工具链的开发者，也适合正在从 `asdf`、`nvm`、`pyenv`、`direnv` 或零散脚本迁移的团队。

## Files

| 文件 | 说明 |
|---|---|
| `index.html` | Kami 排版源文件 |
| `mise-complete-guide-2026.pdf` | PDF 成品 |
| `guide.md` | 完整教程 Markdown 版 |
| `CHEATSHEET.md` | 可独立使用的命令与配置速查表 |
| `sources.md` | 官方来源、资料口径、冲突处理与边界说明 |
| `research-notes.md` | 调研摘要、证据判断与写作提纲 |
| `data/source-map.tsv` | 正文章节与来源页面映射 |
| `sources/official-docs/` | mise 官方仓库 Markdown 快照 |
| `sources/raw/` | 官网、GitHub API 与交叉验证页面快照 |
| `assets/mise-logo.svg` | mise 官方 logo |
| `fonts/` | PDF 使用的本地中文与等宽字体 |

## Scope

本文解释 mise 的稳定主线：安装、激活、`mise.toml`、工具管理、后端、环境变量、任务、锁文件、CI、安全边界、迁移与排障。实验性能力会明确标注，不把 `hooks`、monorepo root、SOPS 或 direct age encryption 写成默认路径。

## Rebuild

```bash
cd mise-complete-guide-2026
python3 build_paper.py
weasyprint index.html mise-complete-guide-2026.pdf
```

`index.html` 和 PDF 成品保持自足。修改 Markdown 后重新生成 HTML 时，额外需要本地 Kami 长文模板。
