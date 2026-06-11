# 中国互联网公司市值排名 2026

这是一份 A4 横版单页研究作品，以 2026-06-10 收盘数据比较中国互联网公司的上市市值，并将字节跳动、小红书的私营交易估值作为单独标记纳入同一观察框架。

## Files

- `index.html`: 可读、可打印的单页源码。
- `china-internet-market-cap-ranking-2026.pdf`: PDF 成品。
- `sources.md`: 来源、证据等级、样本边界与计算方法。
- `data/company-ranking.csv`: 排名、估值口径、证据日期与来源编号。
- `data/source-map.tsv`: 来源编号、URL 与支持事实映射。

## Rebuild

```bash
cd china-internet-market-cap-ranking-2026
../.venv/bin/python - <<'PY'
from weasyprint import HTML
HTML("index.html", base_url=".").write_pdf(
    "china-internet-market-cap-ranking-2026.pdf"
)
PY
```

## Scope

样本聚焦以互联网平台、数字内容、在线交易或互联网服务为核心的中国公司。上市公司按普通股与存托凭证对应的整体权益市值排序；私营公司按最近可辨认的股份交易或基金文件隐含估值标记，并明确交易状态与证据等级。报告不构成投资建议，也不把私营公司估值解释为公开市场价格。
