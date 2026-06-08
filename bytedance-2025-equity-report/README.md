# 字节跳动 FY2025 Equity Report

字节跳动 / ByteDance 私营公司权益研究报告，覆盖 2025 年经营表现与利润口径冲突、2022-2026 年股份回购及二级交易估值变化、员工权益回购价格，以及基于交易锚和可持续盈利敏感性的估值观察。

## Files

- `index.html`: 可读、可打印的报告源码。
- `bytedance-2025-equity-report.pdf`: PDF 成品。
- `sources.md`: 来源说明、可信层级与研究边界。
- `data/source-map.tsv`: 正文来源编号与 URL 映射。
- `data/performance-disclosures.csv`: 已披露或报道的业绩数据与状态。
- `data/valuation-history.csv`: 权益估值标记时间线。
- `data/option-pricing-history.csv`: 员工期权 / RSU / 股份回购报价历史。
- `data/valuation-sensitivity.csv`: 可持续盈利倍数情景的可复算输入与结果。

## Rebuild

```bash
cd bytedance-2025-equity-report
python3 - <<'PY'
from weasyprint import HTML
HTML('index.html', base_url='.').write_pdf('bytedance-2025-equity-report.pdf')
PY
```

## Scope

字节跳动未上市，且截至 2026-05-23 未检索到公司公开发布的 FY2025 经审计年度报表或招股文件。本文区分媒体获得的经营沟通数字、国际会计准则利润口径报道、员工权益回购方案、投资人回购和二级份额交易；估值区间为作者观察框架，不构成投资、私募份额买卖、员工期权处置或税务建议。
