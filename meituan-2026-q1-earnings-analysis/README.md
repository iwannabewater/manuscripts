# 美团 2026 Q1 财报深度分析

本目录收录美团 2026 年第一季度财报分析的研究稿、数据底表、来源索引、HTML 论文版和 PDF 成品。

## 交付文件

- `analysis.md`：完整研究稿。
- `index.html`：A4 论文版。
- `meituan-2026-q1-earnings-analysis.pdf`：打印级 PDF。
- `sources.md`：来源与使用边界。
- `data/`：财务、业务、同行与监管时间线底表。
- `sources/`：归档后的官方材料和外部资料。
- `raw/`：本地抓取日志、原始 PDF 与改写前草稿备份，不进入版本库。

## 时间边界

美团在 2026 年 6 月 1 日港股收盘后披露财报。本文截至北京时间 2026 年 6 月 2 日凌晨完成，因此没有把 6 月 1 日收盘价写成财报后的市场反应。财报后首个港股交易日表现仍待观察。

## 生成 PDF

```bash
python3 - <<'PY'
from pathlib import Path
from weasyprint import HTML

root = Path("meituan-2026-q1-earnings-analysis")
HTML(filename=str(root / "index.html"), base_url=str(root.resolve())).write_pdf(
    str(root / "meituan-2026-q1-earnings-analysis.pdf")
)
PY
```

本文不构成投资建议。
