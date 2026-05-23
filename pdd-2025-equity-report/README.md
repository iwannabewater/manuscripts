# PDD Holdings 2025 Equity Report

拼多多集团 / PDD Holdings 2025 年报中文个股研报，覆盖投资结论、2025 财报拆解、利润桥、现金流与资产负债表、估值、竞争位置、催化剂和风险。

## Files

- `index.html`: 可读、可打印的报告源码。
- `pdd-2025-equity-report.pdf`: PDF 成品。
- `sources.md`: 来源说明、核验口径与边界。
- `data/source-map.tsv`: 正文来源编号与 URL 映射。
- `data/financials-2023-2025.csv`: 年报核心财务数据。
- `data/valuation-assumptions.csv`: 估值模型关键输入。
- `fonts/`: PDF 使用的本地中文字体。

## Rebuild

```bash
cd pdd-2025-equity-report
python3 - <<'PY'
from weasyprint import HTML
HTML('index.html', base_url='.').write_pdf('pdd-2025-equity-report.pdf')
PY
```

## Verify

```bash
python3 - <<'PY'
from pathlib import Path
text = Path('index.html').read_text()
for bad in ['{{', '}}', '占位', 'TBD', 'Lorem', 'DATA NEEDED', 'undefined', 'NaN', '十亿元', '虚线']:
    assert bad not in text, bad
PY
pdftotext pdd-2025-equity-report.pdf - | rg '\\{\\{|占位|TBD|Lorem|DATA NEEDED|undefined|NaN|十亿元|虚线'
pdfinfo pdd-2025-equity-report.pdf
```

## Scope

本文为研究示例，不构成投资建议、证券买卖推荐、招揽或承诺。估值为作者基于公开信息的模型估算；PDD 未披露 Temu 独立利润表、GMV、买家数或区域单位经济模型，因此涉及业务拆分的判断均保留披露折价。
