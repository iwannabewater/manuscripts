# 字节跳动 FY2025 Equity Report Sources

Source check date: 2026-05-23.

字节跳动为未上市公司，本文未检索到面向公众的 FY2025 经审计年度报告、完整资本结构或投资者关系财务页面。本文优先采用 Bloomberg、Reuters、财新所报道的公司沟通、交易备忘或知情人士数字；TikTok 美国结构采用官方公告；员工期权/权益回购的 2026 年报价为媒体转述内部邮件，单独降低证据等级。作者计算与来源事实分离保存在 `data/`。

## Evidence Ladder

| Level | Meaning | Items in this report |
|---|---|---|
| A | 公司或相关实体的公开官方材料 | TikTok USDS Joint Venture 成立与 ByteDance 19.9% 持股 |
| B | 主流财经媒体查阅材料或据多名知情人士报道 | FY2022-FY2025 经营数字；投资人/员工回购；二级交易与拟议出售 |
| C | 财经/科技媒体转述内部员工方案 | 2025 年 10 月、2026 年 4 月在职与离职员工回购报价 |

可信层级衡量公开可复核程度。不同层级、不同持有人类别或不同交易状态的报价不能被视为同一公开市场价格。

## Core Sources

| ID | Source | Date | Used for | Boundary |
|---|---|---:|---|---|
| S01 | Bloomberg, *ByteDance Profit Jumps 60%, Taking It Past Archrival Tencent* | 2024-04-10 | FY2022/FY2023 收入及 EBITDA | 知情人士数字；EBITDA 不是净利润 |
| S02 | Reuters 转述 The Information, *ByteDance's Revenue From International Operations Rose 63% to $39 Billion in 2024* | 2025-04-10 | FY2024 收入 US$155bn、净利润 US$33bn | 私营公司媒体报道，非公开财报 |
| S03 | Reuters, *ByteDance sets valuation above $330 billion for new share buyback* | 2025-08-27 | 2Q2025 收入约 US$48bn、同比增长 25%；员工回购 US$200.41 | 季度报道数字及拟实施回购 |
| S04 | Bloomberg, *TikTok Owner ByteDance on Track for $50 Billion Profit in 2025* | 2025-12-19 | 前九个月净利润约 US$40bn、全年利润约 US$50bn 展望 | 年末前知情人士展望，不是审计全年利润 |
| S05 | 财新，*字节跳动2025年国内营收同比增20% 投入AI致净利润下滑七成* | 2026-04-20 | 国内/海外收入增速、海外占比、IFRS 净利润下滑及李亮回应 | 小范围投资人沟通与管理层回应报道 |
| S06 | Bloomberg, *ByteDance to Buy Back $3 Billion in Shares as IPO Plans Stall* | 2022-09-16 | 投资人回购约 US$300bn、每股略低于 US$177 | 投资人回购，不代表员工权益价格 |
| S07 | Bloomberg, *ByteDance Offering to Buy Back Employees' Shares for $155 Apiece* | 2022-10-12 | 员工 RSU 回购 US$155/股 | 内部备忘报道 |
| S08 | Reuters, *TikTok owner ByteDance offers to buy back shares from staff at $160 apiece* | 2023-11-15 | 员工 RSU/股份回购 US$160/股 | 员工方案，口径不等同投资人回购 |
| S09 | Reuters, *ByteDance offers investors share buyback, valued at $268 billion* | 2023-12-06 | 投资人回购 US$160/股、估值约 US$268bn | 同一每股价格可对应不同方案口径 |
| S10 | Reuters, *TikTok parent ByteDance's valuation hits $300 billion, sources say* | 2024-11-16 | 投资人回购 US$180.70/股、约 US$300bn | 投资人回购标记 |
| S11 | Reuters, *TikTok parent ByteDance valuation rises in latest share buyback* | 2025-03-04 | 美国员工回购 US$189.90/股、约 US$315bn；历史 US$171/181 | 员工计划且覆盖地域受限 |
| S12 | IT之家经新浪科技转载，*字节跳动新一轮期权回购价格再创新高* | 2026-04-15 | 在职 US$229.50、离职 US$201.96；上一轮 US$200.41/180.37 | 转述内部邮件；未见公开方案原文 |
| S13 | Reuters, *ByteDance valued at $550 billion in proposed share sale by General Atlantic* | 2026-02-25 | 拟议交易 US$550bn；2025 年二级交易 US$480bn 回溯 | US$550bn 尚属拟议交易 |
| S14 | TikTok Newsroom, *Announcement from the new TikTok USDS Joint Venture LLC* | 2026-01-23 | 新合资公司成立、ByteDance 保留 19.9% | 官方公告未提供 ByteDance 财务桥 |
| S15 | ByteDance, *Resources* | accessed 2026-05-23 | 官方品牌材料核对 | 不提供财务或估值数据 |

## Method Boundaries

- `FY2025` 经营增速与利润均按报道原始口径标记。Bloomberg 的“约 US$50bn 利润展望”与财新所报 `IFRS` 净利润同比下滑超过 70% 不可直接合并；两者冲突本身是本报告的核心风险。
- 主流媒体使用 `share repurchase`、`restricted stock units (RSU) or options` 等描述，中文媒体常称“期权回购”。本文保留来源术语并统称“员工权益回购”，不假设所有批次法律权利相同。
- 员工、投资人和二级市场交易标记的持有人、权利类别、规模及流动性不同。本文不从员工每股报价机械推导整体估值。
- `US$550bn` 为拟议股份出售标记，不作为已完成交易；基础观察区间采用 `>US$330bn` 员工流动性标记与 `US$480bn` 报道二级交易标记。
- 盈利敏感性采用 US$30bn / US$40bn / US$50bn 的可持续利润情景与 8x / 10x / 11x 倍数，仅用于检验估值要求，不等同盈利预测或目标价。
- 因缺少经审计现金流、净现金、股份类别和完全摊薄股本，本文不编造 DCF 或每股目标价。
- 本报告为研究材料，不构成证券、私募份额、员工权益处置或税务建议。
