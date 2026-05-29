# PDD Holdings 2026 Q1 Earnings Analysis

拼多多集团 / PDD Holdings 2026 年一季度财报深度分析，覆盖财务拆解、股价暴跌原因、Goldman Sachs 及其他券商反应、Temu 与新拼姆战略、长期竞争位置和关键风险。

## Files

- `index.html`: Kami 排版源文件，可直接在浏览器中预览。
- `pdd-2026-q1-earnings-analysis.pdf`: PDF 成品。
- `analysis.md`: 研究长文底稿。
- `sources.md`: 来源、核验口径与边界。
- `sources/`: 抓取后的来源 Markdown/HTML。
- `data/source-map.tsv`: 正文来源编号与 URL 映射。
- `data/pdd-q1-2026-financials.csv`: Q1 2026 与 Q1 2025 财务拆解。
- `data/pdd-price-reaction.csv`: 财报前后股价反应。
- `fonts/`: PDF 使用的本地中文字体。

## Rebuild

```bash
cd pdd-2026-q1-earnings-analysis
python3 - <<'PY'
from weasyprint import HTML
HTML('index.html', base_url='.').write_pdf('pdd-2026-q1-earnings-analysis.pdf')
PY
```

## Scope

本文为公开资料研究与写作示例，不构成投资建议、证券买卖推荐、招揽或收益承诺。PDD 未披露 Temu、拼多多主站、新拼姆的独立收入、GMV、利润或区域单位经济模型；涉及业务拆分和战略影响的判断均为基于公开披露的推断。
