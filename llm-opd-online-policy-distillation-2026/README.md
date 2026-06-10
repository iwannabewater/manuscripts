# 大模型 OPD 技术概览 2026

本目录是一份关于大模型 OPD, 即 on-policy distillation, 在线或在策略蒸馏的中文一页纸技术报告。

## 文件

- `index.html`: 排版源文件和网页版本。
- `llm-opd-online-policy-distillation-2026.pdf`: PDF 成品。
- `sources.md`: 证据日期、来源口径、证据分层和不确定性说明。
- `data/source-map.tsv`: 正文主张与来源 ID 的结构化映射。
- `data/opd-method-map.csv`: OPD 方法谱系与工程用途摘要。

## 复现

在仓库根目录运行：

```bash
make fonts
.venv/bin/python -c "from pathlib import Path; from weasyprint import HTML; d=Path('llm-opd-online-policy-distillation-2026'); HTML(filename=str(d/'index.html'), base_url=str(d)).write_pdf(str(d/'llm-opd-online-policy-distillation-2026.pdf'))"
make verify
```
