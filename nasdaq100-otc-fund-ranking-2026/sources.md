# 来源与核验口径

## 研究口径

- 研究对象：境内公开销售的人民币场外公募 QDII、ETF 联接或指数基金份额，标的为纳斯达克 100。
- 核验截止：`2026-06-17`。净值和交易状态多以 `2026-06-16` 为最近净值日，基金规模统一采用页面披露的 `2026-03-31` 季末规模。
- 推荐含义：在合规渠道、公开费用和当前可执行限额约束下的筛选结论，不是收益承诺、个性化适当性意见或税务建议。
- 证据优先级：监管机构、指数机构、基金管理人公告和产品页优先；销售平台展示页用于统一横向字段。若两者冲突，以基金管理人公告和法律文件解释。
- 数据处理：同一基金的 A、C、I、E、F 类分开记录；主榜优先长期持有场景下的 A 类或低销售服务费份额；暂停申购份额列入观察名单，不列为当前买入首选。

## 监管、指数与市场结构

| 编号 | 来源 | 用途 |
|---|---|---|
| S1 | 国家外汇管理局，《合格境内机构投资者（QDII）投资额度审批情况表》，发布日期 2026-05-29。[原文](https://www.safe.gov.cn/safe/2018/0425/16849.html) | QDII 额度是场外纳指基金限购和暂停申购的一级约束。 |
| S2 | Nasdaq, *Nasdaq-100 Index Methodology*, 2026。[PDF](https://indexes.nasdaq.com/docs/Methodology_NDX.pdf) | 确认 Nasdaq-100 的指数范围、非金融公司口径和修正市值加权方法。 |
| S3 | Nasdaq, *Overview for NDX*。[网页](https://indexes.nasdaqomx.com/Index/Overview/NDX) | 确认指数覆盖 100 家 Nasdaq 上市大型非金融公司。 |
| S4 | Invesco, *QQQM Invesco NASDAQ 100 ETF fact sheet*。[PDF](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/qqqm-invesco-nasdaq-100-etf-fact-sheet.pdf) | 用 0.15% 费用率作为境外低费率 Nasdaq-100 ETF 参照。 |
| S5 | Invesco, *Invesco QQQ ETF*。[网页](https://www.invesco.com/qqq-etf/en/home.html) | 用 0.18% 费用率和大型 ETF 交易属性作为境外参照。 |

## 候选基金数据

| 编号 | 来源 | 用途 |
|---|---|---|
| S6 | 天天基金 / 东方财富基金档案页，例如 [016452 费率页](https://fundf10.eastmoney.com/jjfl_016452.html)。 | 统一抓取交易状态、日累计申购上限、规模、成立日期、管理人、费率。 |
| S7 | 天天基金 / 东方财富阶段涨幅接口，例如 [016452 阶段涨幅](https://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jdzf&code=016452)。 | 统一抓取今年来、近 1 年、近 3 年等阶段收益，用作阶段跟踪复核。 |
| S8 | 南方基金，南方纳斯达克 100 指数发起（QDII）产品页。[A 类](https://www.nffund.com/main/nffund/personal-financing/detail.shtml?fundCode=016452) | 复核基金管理人、产品名称、基金类型和风险收益边界。 |
| S9 | 摩根基金，摩根纳斯达克 100 指数型发起式证券投资基金（QDII）公告。[PDF](https://www.cifm.com/fund/019172/announce/202601/P020260108659599256222.pdf) | 复核人民币 A/C 代码、开放日和境外市场节假日暂停逻辑。 |
| S10 | 汇添富基金，汇添富纳斯达克 100ETF 发起式联接（QDII）人民币 A 产品页。[网页](https://www.99fund.com/main/products/pofund/018966/fundgk.shtml) | 复核 ETF 联接结构、管理人和产品资料。 |
| S11 | 华安纳斯达克 100ETF 联接（QDII）A，东方财富基金档案页。[网页](https://fundf10.eastmoney.com/040046.html) | 复核老牌产品的规模、成立日期和交易状态。 |
| S12 | 广发纳斯达克 100ETF 联接人民币（QDII）A，广发基金产品页。[网页](https://www.gffunds.com.cn/funds/?fundcode=270042) | 复核基金全称、业绩比较基准和 ETF 联接结构。 |
| S13 | 易方达纳斯达克 100ETF 联接（QDII-LOF）暂停申购公告，公告日 2026-03-18。[网页](https://www.efunds.com.cn/Mobile/c/793/793529.shtml) | 说明观察名单中暂停申购产品不能写成当前可买。 |
| S14 | 嘉实纳斯达克 100ETF 发起联接（QDII）C 人民币，嘉实基金产品页。[网页](https://www.jsfund.cn/main/fund/016533/fundManager.shtml) | 复核嘉实产品的官方展示和阶段表现。 |
| S15 | 天弘纳斯达克 100 指数发起（QDII）A，天弘基金产品页。[网页](https://www.thfund.com.cn/fundinfo/018043) | 复核天弘产品基本资料。 |
| S16 | 华夏纳斯达克 100ETF 发起式联接（QDII）A，华夏基金产品页。[网页](https://www.chinaamc.com/fund/015299/index.shtml) | 复核华夏产品基本资料。 |

## 数据文件

- `data/fund-screen-2026-06-17.json`：41 个候选人民币相关份额的抓取结果。字段包括代码、名称、管理人、交易状态、日限额、规模、费率、阶段收益和来源 URL。
- `data/fund-ranking-2026-06-17.csv`：主榜排序。执行分满分 100，权重为费用 35%、申购可执行性 25%、规模 20%、阶段跟踪复核 10%、成立时间 10%。

## 不覆盖范围

- 不覆盖美元份额、场内 ETF 本体、主动股票型“纳斯达克精选”产品。
- 不评估单个投资者的风险承受能力、税务后果、汇率敞口比例或资产配置比例。
- 不把媒体估算、社区讨论或销售平台热榜当作独立投资结论。二级资料只用于发现线索，不作为核心证据。
