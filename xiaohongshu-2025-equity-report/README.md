# 小红书 FY2025 Equity Report

小红书 / rednote 私营公司权益研究报告，覆盖 2025 年业绩披露边界、商业化信号、2021-2025 年老股与基金文件估值变化、2025-2026 年员工期权授予及回购价格，以及基于交易锚和盈利敏感性的估值观察。

## Files

- `index.html`: 可读、可打印的报告源码。
- `xiaohongshu-2025-equity-report.pdf`: PDF 成品。
- `sources.md`: 来源说明、可信层级与研究边界。
- `data/source-map.tsv`: 正文来源编号与 URL 映射。
- `data/performance-disclosures.csv`: 已披露或报道的业绩数据与状态。
- `data/valuation-history.csv`: 权益估值标记时间线。
- `data/option-pricing-history.csv`: 期权授予参考价与回购价历史。
- `data/valuation-sensitivity.csv`: 盈利倍数情景的可复算输入与结果。
- `fonts/`: PDF 使用的本地中文字体。

## Rebuild

```bash
cd xiaohongshu-2025-equity-report
python3 - <<'PY'
from weasyprint import HTML
HTML('index.html', base_url='.').write_pdf('xiaohongshu-2025-equity-report.pdf')
PY
```

## Scope

小红书未上市，且截至 2026-05-23 未检索到公司公开发布的 FY2025 经审计报表或招股文件。本文区分公司向投资者提供而由媒体报道的预测、基金文件隐含估值、单笔老股交易报道与员工期权回购报价；估值区间为作者观察框架，不构成投资、私募份额买卖或员工期权处置建议。
