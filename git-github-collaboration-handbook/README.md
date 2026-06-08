# Git & GitHub Collaboration Handbook

署名：Winston
资料口径：截至 2026-05-30
交付形态：横向 A4 工程手册

本目录收录《算法 / 开发工程师 Git 与 GitHub 协作编码标准流程手册》。手册面向算法工程师、后端 / 前端 / 全栈开发工程师、开源贡献者和团队维护者，覆盖从 0 到 1 上手、日常开发、分支策略、Issue、PR、Code Review、Contributor 管理、发布、回滚与高级 Git 操作。

## Files

| 文件 | 说明 |
|---|---|
| `index.html` | 手册排版源文件 |
| `git-github-collaboration-handbook.pdf` | PDF 成品 |
| `sources.md` | 官方来源、资料口径与边界说明 |
| `data/source-map.tsv` | 来源页面与正文用途映射 |

## Scope

本文基于 Git、GitHub、Google Engineering Practices、Meta Engineering、OpenAI 官方开源仓库贡献说明与 CloudWeGo / ByteDance 开源项目贡献说明等公开材料编写。本文不是任何公司的内部流程复刻，不代表 Google、Meta、OpenAI 或 ByteDance 官方立场；它把公开可验证的工程原则整理成一套适合 GitHub 协作编码的团队 SOP。

## Rebuild

```bash
cd git-github-collaboration-handbook
weasyprint index.html git-github-collaboration-handbook.pdf
```
