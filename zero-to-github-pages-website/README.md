# 从 0 到 GitHub Pages：一个网站项目的完整工程链路

署名：Winston  
资料口径：截至 2026-05-05  
交付形态：中文 A4 技术长文，HTML + PDF

本仓库收录《从 0 到 GitHub Pages：一个网站项目的完整工程链路》。正文从空目录开始，覆盖 Vite 初始化、本地构建、语义 HTML、Git 版本化、GitHub 仓库创建、GitHub Actions 部署、Pages 发布验证和常见故障排查。

## Files

| 文件 | 说明 |
|---|---|
| `index.html` | 手册排版源文件 |
| `zero-to-github-pages-website.pdf` | PDF 成品 |
| `sources.md` | 官方来源、资料口径与边界说明 |
| `data/source-map.tsv` | 来源页面与正文用途映射 |

## Scope

本文面向需要把静态网站部署到 GitHub Pages 的工程技术人员。正文重点讨论可复现的本地构建、可审查的远端发布和上线验证，不覆盖后端托管、数据库、身份认证、支付系统或企业级合规发布流程。

## Rebuild

```bash
cd zero-to-github-pages-website
weasyprint index.html zero-to-github-pages-website.pdf
```

## Archive

本目录按 `manuscripts` 仓库的作品归档约定保存，不作为独立网站仓库发布。
