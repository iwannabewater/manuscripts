# 小红书 FY2025 Equity Report Sources

Source check date: 2026-05-23.

小红书是未上市公司，未见公开年度申报文件或投资者关系财报页面。本文优先使用 Bloomberg、Financial Times 披露的投资者更新或交易文件信息，以及监管部门官方网站；对员工期权与单笔老股交易，使用最接近事件的财经媒体报道，并在正文降低证据权重。所有作者推算与来源事实分离保存在 `data/`。

## Evidence Ladder

| Level | Meaning | Items in this report |
|---|---|---|
| A | 政府公告或媒体查阅的基金文件，可对应具体文档/行为 | 2025 年 3 月与 6 月 GSR 文件隐含估值；网信部门处置 |
| B | 主流财经媒体据知情人士披露的公司或交易数字 | FT / Bloomberg 的利润数据与 2024 老股出售；2025 年 1 月洽售 |
| C | 单一媒体获悉的部分老股出售或员工方案 | 2025 年末 US$50bn 老股出售；期权授予与回购报价 |

可信层级衡量可复核程度，不是对事件真实性的否定。私营公司报告若把 C 级标记与 A 级文件当成同一价格口径，会夸大可兑现价值。

## Core Sources

| ID | Source | Date | Used for | Boundary |
|---|---|---:|---|---|
| S01 | Financial Times, *China's Instagram-like app Xiaohongshu makes first profit*; reproduction by Chin@Strategy | 2024-03-24 | FY2022/FY2023 收入、净利润和 2023 MAU | 数字非公开报表，FT 据四名知情人士 |
| S02 | Financial Times, *China's Instagram-like Xiaohongshu hits $1bn in quarterly sales* | 2024-10-13 | 1Q2024 收入及净利润、2024 老股交易背景 | FT 据两名知情人士 |
| S03 | Bloomberg, *China's Instagram-Style Xiaohongshu Crosses $1 Billion in Profit* | 2024-12-12 | FY2024 净利润超过 US$1bn 的预测 | 公司告知投资者的预期，不是经审计实际值 |
| S04 | Bloomberg, *TikTok Rival Xiaohongshu Expects Profit to Triple to $3 Billion* | 2025-09-05 | FY2025 净利润 US$3bn 预测 | 投资者更新预测；截至核验日未见正式确认 |
| S05 | Bloomberg, *Chinese Social Media App Xiaohongshu's $26 Billion Valuation Bolsters GSR Fund* | 2025-06-04 | GSR 文件截至 2025 年 3 月隐含 US$26bn 估值 | 基金持仓映射，不是公司融资 |
| S06 | Bloomberg, *China's Xiaohongshu Hits $31 Billion Value in GSR Books* | 2025-09-04 | GSR 文件截至 2025 年 6 月隐含 US$31bn 估值 | 基金持仓映射，不是持续成交市场 |
| S07 | Reuters, *Stake sale talks value China's TikTok-rival Xiaohongshu at $20 billion, Bloomberg News reports* | 2025-01-16 | 股东洽售至少 US$20bn、2024 US$17bn 背景 | 洽谈估值，不代表完成交易 |
| S08 | 投资界，*独家｜小红书卖老股，估值3500亿* | 2026-02-04 | 2025 年末部分老股 US$50bn 出售报道、估值时间线回溯 | 单笔交易且公司未确认，正文仅作上行情景 |
| S09 | 36氪快讯，*小红书期权授予价上调，25美元/股* | 2025-10-18 | 2025 年 3/6/10 月授予参考价及 US$2 行权价 | 转述财联社，未见公司方案全文 |
| S10 | IT之家，*消息称小红书启动新一轮期权回购：在职员工25.5美元，离职21美元* | 2026-05-11 | 2025 两轮及 2026 年 5 月回购报价、最新 US$30 参考价 | 媒体所称员工方案，未见公开公司公告 |
| S11 | 北京商报转述小红书数据，东方财富转载，*小红书月活跃用户已超过3.5亿* | 2025-08-29 | MAU 超 3.5 亿、每月寻求购买用户 1.7 亿 | 公司提供运营指标，非财务核验 |
| S12 | 亿邦动力，新浪科技转载，*小红书首次系统发布电商经营方法论* | 2026-04-10 | Rise100 商家 2025 GMV 同比增长超 2.6 倍 | 头部样本指标，不代表全平台 |
| S13 | 上海证券报·中国证券网，*1.84亿人在小红书读书* | 2026-04-23 | 2025 图书零售业在平台 GMV 增长超 30% | 单一类目指标 |
| S14 | 中央网信办，*网信部门依法查处小红书平台破坏网络生态案件* | 2025-09-11 | 监管风险事件与处置措施 | 官方事件披露，不提供财务影响量化 |
| S15 | 新浪科技，*新一轮5亿美元融资后估值200亿美金 小红书：以老股东增持为主* | 2021-11-08 | 2021 年融资与超过 US$20bn 的投后估值 | 当时媒体报道及公司回应，非公开融资文件 |

## Method Boundaries

- 报告将 `FY2024E` 与 `FY2025E` 标为媒体报道的预测/投资者更新数字；不用“年报”或“已实现”表述替代。
- `US$31bn` 为 Bloomberg 根据 GSR 基金文件计算的权益价值标记；`US$50bn` 为投资界报道的单笔老股出售标记。两者不是可交易股票市值。
- 员工“授予参考价”“回购价”“行权价”按媒体用语记录。由于没有完全摊薄股数、期权批次及回购总额，本文不从每股价格计算公司总估值。
- 估值敏感性只用利润和 P/E 做透明情景测试；由于未披露现金流、净现金、SBC 与股本，本文不编造 DCF、每股目标价或可比公司精确溢价。
- 图表中小数、变化率与倍数均由 `data/*.csv` 所列源数字计算，四舍五入至一位小数或整数亿美元。
- 报告为研究示例，不构成投资建议、私募份额招揽、员工期权行权或税务意见。
