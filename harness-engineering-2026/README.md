# Harness Engineering 2026

一份面向 Agent 系统设计者与工程团队的中文技术研究，覆盖 Harness 的定义、执行原理、组件边界、生态协议、自动优化研究，以及国内外厂商和开源社区的落地实践。

## Files

- `index.html`：Winston 长文档源文件，也是网页阅读入口。
- `harness-engineering-2026.pdf`：正式 PDF 成品。
- `sources.md`：来源、证据等级、冲突与事实边界。
- `data/source-map.tsv`：来源到正文用途的映射。
- `data/evidence-matrix.tsv`：关键主张、证据和限制条件。
- `sources/`：研究时通过 `read` 归档的公开证据快照。

## Scope

本文把 Harness 定义为模型与真实任务环境之间的执行系统，研究对象包括上下文、工具、状态、控制流、权限、沙箱、追踪、恢复和评测。单纯的聊天界面、模型训练框架和没有外部动作的提示模板不在核心范围内。

## Rebuild

```bash
make fonts
../.venv/bin/python -c "from weasyprint import HTML; HTML('index.html', base_url='.').write_pdf('harness-engineering-2026.pdf')"
make verify
make verify-network
```
