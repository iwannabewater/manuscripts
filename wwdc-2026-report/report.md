# WWDC 2026 闭幕后全景报告

## Siri AI 进入开发者测试，Apple 把模型、代理、系统服务与开发工具收进同一套平台

**版本**：2.0
**时间边界**：北京时间 2026 年 6 月 16 日
**证据范围**：Apple Newsroom、Apple Developer、操作系统产品页、WWDC26 视频索引与官方会话摘要

> 一句话结论：WWDC26 交付的是一套从个人上下文、应用动作、模型路由、端侧推理、私有云、编码代理延伸到分发治理的系统工程。Siri AI 已进入开发者测试，但消费者版本、地区覆盖、语言扩展和服务器额度仍需按 beta 产品管理。

---

## 01. 执行摘要

### 八个核心结论

1. **WWDC26 已于 6 月 12 日闭幕，发布主线完整指向软件平台。** Apple 公布 iOS 27、iPadOS 27、macOS 27 Golden Gate、watchOS 27、visionOS 27 和 tvOS 27，没有发布新硬件。大会把 Siri AI、Apple Intelligence、开发者工具、系统可靠性、儿童安全和服务更新放在同一套平台叙事中。[S01][S02][S03][S19][S20]

2. **Siri AI 已经可测试，尚未完成大众交付。** 6 月 8 日开放的是 iOS、iPadOS、macOS、visionOS 开发者测试，watchOS 将在后续 beta 加入。消费者版本计划于 2026 年稍后以英语 beta 推出。Apple 没有承诺它会随秋季 OS 27 正式版同步成为稳定版本。[S03][S04][S21]

3. **Apple 把 AI 从助手功能扩成系统平台。** 新架构连接个人上下文、屏幕与相机内容、Spotlight 语义索引、App Intents、网页知识、端侧模型、Private Cloud Compute 和第三方模型。Siri 是面向用户的入口，Foundation Models、Core AI、MLX、Evaluations 和 Xcode 代理构成开发者侧的完整链路。[S04][S16][S17][S21][S23]

4. **模型开放程度明显提高，平台控制仍然牢固。** Foundation Models 的模型无关架构可连接 Apple 模型、PCC 和包括 Gemini、Claude 在内的第三方提供商。Xcode 27 可使用 Anthropic、Google、OpenAI 的编码代理，并支持 Agent Client Protocol 和 MCP。模型可以更换，但上下文、权限、应用动作、评估、设备与分发仍由 Apple 平台组织。[S16][S17][S23]

5. **可靠性修复不是陪衬。** Apple 同时处理 Liquid Glass 可读性、搜索、邮件相关性、网络切换、AirDrop、照片载入、应用启动和 iPad 外置存储性能。Siri 要读取个人内容并执行应用动作，搜索、索引、网络和界面层的稳定性直接决定 AI 的任务完成率。[S03][S07][S08][S09]

6. **Keynote 之外的技术密度更高。** 截至 6 月 16 日，WWDC26 视频索引有 137 个去重条目，其中 134 个可播放，3 个仍标记为即将上线。索引覆盖代理安全、gRPC、Linux 容器、MetricKit、Trust Insights、WebKit、Metal 4、OpenUSD、相机、音视频和无障碍等生产级主题。[S18][S28][S29][S30][S31][S32][S33]

7. **服务与 App Store 更新会改变产品设计。** Maps、Find My、Music、Fitness+、Wallet、Podcasts、Apple TV 和 Apple Sports 都获得更新。App Store 则向年度承诺订阅、组织采购、群组席位、跨开发者套餐、留存消息和更灵活的营销素材扩展。[S24][S25]

8. **可用性仍然高度分层。** OS 兼容、Apple Intelligence 硬件、Siri AI 测试资格、消费者 beta、语言、地区和服务器额度是不同条件。中国暂时不能使用新 Siri AI 和其他新 Apple Intelligence 功能；欧盟的 iOS、iPadOS 与 watchOS 首发也暂不提供 Siri AI。[S03][S04][S21]

### 最值得记住的数字

| 数字 | 含义 | 证据级别 |
|---|---|---|
| 6 月 8 日至 12 日 | WWDC26 举行时间 | 官方事实 [S01][S02] |
| 超过 1,000 人 | Apple Park 现场开发者、设计师与学生规模 | 官方事实 [S02] |
| 350 / 50 | Swift Student Challenge 获奖者 / Distinguished Winners | 官方事实 [S02] |
| 超过 100 个 | Apple 对新视频会话规模的正式表述 | 官方事实 [S01][S02] |
| 137 / 134 / 3 | 6 月 16 日视频索引去重条目 / 已上线 / 即将上线 | 页面测量 [S18] |
| 29 / 18 / 13 | AI 与机器学习 / App Services / SwiftUI 与 UI 框架条目数 | 页面测量 [S18] |
| 30% / 70% / 80% | Apple 宣称的应用启动、照片载入、AirDrop 最高提升 | 官方基准 [S03] |
| 30% / 2 倍 | Xcode 27 安装体积缩减 / Xcode Cloud 最高提速 | 官方宣称 [S23] |
| 12 组 | 2026 Apple Design Awards 获奖应用与游戏 | 官方结果 [S27] |

---

## 02. 大会事实与证据边界

Apple 于 3 月 23 日宣布 WWDC26 在 6 月 8 日至 12 日举行，全球开发者可在线参与，并在 6 月 8 日于 Apple Park 举办特别活动。5 月 18 日公布的正式日程包括 Keynote、Platforms State of the Union、视频会话、Group Labs 和开发者论坛问答。[S01][S02]

现场活动接待超过 1,000 名开发者、设计师和学生。Swift Student Challenge 有 350 名获奖者，其中 50 名 Distinguished Winners 获邀参加 Cupertino 三日活动。Apple Design Awards 有 36 个入围作品，最终从六个类别中选出 12 个获奖者。[S02][S27]

### 发布与验证节奏

| 阶段 | 日期 | 已确认状态 |
|---|---|---|
| 大会宣布 | 2026-03-23 | 日期、线上形式、Apple Park 活动确认 |
| 日程公布 | 2026-05-18 | Keynote、PSOTU、视频、实验室和现场规模确认 |
| 开发者测试 | 2026-06-08 | OS 27 beta 与部分 Siri AI 能力开放 |
| 大会闭幕 | 2026-06-12 | 正式活动结束 |
| 本报告复核 | 2026-06-16 | 新闻稿、产品页、开发者页和视频索引重新检查 |
| 公共测试 | 2026 年 7 月计划 | Apple 称 public beta 将于“下个月”提供 |
| 系统正式更新 | 2026 年秋季计划 | OS 27 作为免费软件更新提供 |
| Siri AI 消费者 beta | 2026 年稍后 | 首发英语，未承诺与秋季系统同步 |

### 视频索引如何计数

Apple 正式表述为“超过 100 个新视频会话”。本报告另行测量 Apple Developer 的 WWDC26 视频索引：按独立播放链接去重，共得到 137 个条目，其中 134 个可播放，3 个显示 available soon。[S18]

这 137 个条目包含正式技术会话、Keynote 与 PSOTU、每日回顾、ASL 版本和 Group Lab 页面，不等同于 137 场标准技术会话。尚未上线的三个条目是 Icon Composer for Beginners Group Lab、Machine Learning & AI Group Lab 和 SwiftData Group Lab。大会已经结束，不代表所有索引页面已经冻结。[S18]

**证据日期**：除明确写明其他日期外，本文对动态页面的判断截至北京时间 2026 年 6 月 16 日。Apple 后续仍可能修改 beta 状态、文档、地区条件和索引内容。

---

## 03. 总体判断：平台工程，而非单点发布

Apple Developer 的总览把 WWDC26 更新按智能能力、开发工具、平台框架和分发服务组织。综合正式发布与会话内容，可以拆成四条相互依赖的主线。[S12]

### 第一条：让 Siri 获得可执行的系统上下文

Siri AI 能读取用户授权范围内的个人内容，理解屏幕、截图、PDF、相机和 Vision Pro 视野，并在 Messages、Music、Reminders 等应用中执行动作。它从瞬时语音入口变成有历史记录、可固定、可跨设备继续的独立应用。[S04][S21]

### 第二条：让开发者提供数据、动作和模型

App Intents 和语义实体让系统理解应用内容与能力。Foundation Models 负责模型与工具编排，Core AI 负责自有模型的端侧部署，MLX 面向训练与研究，Evaluations 和 Instruments 负责验证。Xcode 27 把编码代理接入工程上下文。[S16][S17][S23]

### 第三条：修复 AI 所依赖的基础系统

Apple 重做搜索基础、邮件相关性、网络切换和部分性能路径，并调整 Liquid Glass 的对比度和可读性。这些改进与 AI 并非两套议题。个人上下文依赖索引，应用操作依赖稳定接口，云端推理依赖网络，视觉理解依赖清晰的系统状态。[S03][S07][S08][S09]

### 第四条：把治理与商业模型同步升级

儿童账户、网站审批、联系人权限、暴力内容干预、年龄范围接口、订阅组织化和跨开发者套餐都在扩张。Apple 既开放模型和代理，也在强化权限、审核、家庭治理和平台交易结构。[S05][S06][S25]

综合以上四条线，Apple 选择把 AI 能力嵌入操作系统、芯片、隐私架构、开发工具和分发渠道。成败不会由一次模型演示决定，而取决于真实任务的完成率、第三方应用接入率和跨地区交付速度。

---

## 04. Siri AI：能力、架构与交付边界

### 4.1 用户能得到什么

Apple 公布的 Siri AI 能力可分为七组。[S04][S21]

| 能力 | 具体表现 |
|---|---|
| 自然对话 | 开放式问题、连续追问、头脑风暴和自然往返交流 |
| 个人上下文 | 在消息、邮件、照片、笔记等个人内容中查找信息 |
| 屏幕与视觉理解 | 理解当前屏幕、截图、PDF、相机或 Vision Pro 视野 |
| 应用操作 | 基于当前任务在系统与第三方应用中执行动作 |
| 实时网页知识 | 访问网页信息并组织回答 |
| 跨设备连续性 | 独立 Siri 应用保存会话，通过 iCloud 私密同步 |

Apple 表示，Siri 可通过广泛知识从网页获取最新信息。下一代 Apple Foundation Models 由 Apple 与 Google 合作、结合 Gemini 模型技术定制；Image Playground 的照片级生成模型运行在 Private Cloud Compute 上。Siri、Apple Intelligence 和底层模型供应关系需要分开理解，不能把所有能力都归给单一模型。[S04][S21][S23]

### 4.2 入口随设备变化

- iPhone 可从 Dynamic Island 下滑进入，也可在 Camera 中使用 Siri mode。
- iPad 和 Mac 可从屏幕内容、截图、PDF 与 Spotlight 进入。
- Apple Watch 可继续其他设备上的会话。
- Apple Vision Pro 可注视现实或数字对象后提问，并把 Siri 窗口固定在空间中。[S04][S07][S08][S09][S10][S11]

独立 Siri 应用是产品形态上的关键变化。会话可以回看、固定和跨设备继续，复杂任务不再依赖一次性的语音交互。

### 4.3 四层系统架构

Siri AI 可以概括为四层：

1. **交互层**：语音、键盘、相机、截图、视线、Spotlight、上下文菜单。
2. **系统编排层**：判断任务需要个人上下文、应用动作、网页信息还是模型推理。
3. **数据与能力层**：Spotlight 语义索引、App Toolbox、App Intents、屏幕实体、系统应用与第三方应用。
4. **模型执行层**：端侧 Apple Foundation Models，以及需要更强推理时使用的 Private Cloud Compute。

Apple 表示，当请求交给 Private Cloud Compute 时，个人数据不会被存储，也不会向 Apple 或其他人开放，外部专家可以验证系统软件。Spotlight 索引和 App Toolbox 主要在设备上工作。[S04]

这是一项架构承诺，不是独立审计结论。后续仍需要安全研究、网络流量分析和真实设备测试验证数据最小化、日志处理、失败降级与区域合规。

### 4.4 App Intents 决定第三方体验上限

第三方应用要进入 Siri 的个人上下文和动作体系，主要依赖 App Intents。[S16][S23]

- Entity schemas 把应用内容贡献给 Spotlight 语义索引，并保留来源归属。
- Intent schemas 让用户用自然语言执行动作，不必为每种表达预设固定短语。
- View Annotations 把当前界面映射为实体，使用户可以指代屏幕中的对象。
- App Intents Testing 通过真实系统路径验证 Siri、Shortcuts 和 Spotlight 集成。
- 匿名应用数据与上下文可用于改进意图匹配，同时需要遵守平台隐私边界。

Siri 的实际质量不只取决于模型。实体定义、动作粒度、权限确认、错误恢复和测试覆盖会直接决定任务是否成功。

### 4.5 交付时间表仍按 beta 推进

6 月 8 日开放的是 iOS、iPadOS、macOS、visionOS 开发者测试，watchOS 将在后续 beta 加入。消费者版本计划于 2026 年稍后以英语 beta 提供。中国暂不开放，欧盟的 iOS、iPadOS 与 watchOS 首发也暂不提供。[S03][S04][S21]

Apple 还说明，依赖大型服务器模型的部分能力会有每日使用上限，多数 iCloud+ 套餐可获得更高额度。对产品团队而言，AI 功能设计必须考虑额度耗尽、网络不可用、外部提供商失败和地区禁用时的降级路径。[S03][S21]

---

## 05. 开发者 AI 栈：模型、代理、评估与隐私

### 5.1 Foundation Models 成为模型编排层

Foundation Models framework 继续提供原生 Swift API。新的模型无关架构可连接：

- Apple 端侧 Foundation Models
- Private Cloud Compute 上的 Apple 模型
- Gemini、Claude 等第三方模型提供商
- 通过协议接入的其他模型与工具[S16][S17][S23]

多模态 prompt 可同时传入图像与文本。模型还可以调用 Vision 的 OCR、条码识别等端侧工具。Dynamic Profiles 支持在连续会话中替换模型、工具和指令。[S16][S17]

这套设计降低了模型替换成本，但没有消除供应商差异。延迟、价格、隐私条款、内容策略、上下文长度和地区可用性仍需要单独评估。

### 5.2 Private Cloud Compute 的开发者供给

Apple Intelligence 开发者页给出的条件是：应用加入 App Store Small Business Program，且首次 App Store 下载总量低于 200 万次，可在 PCC 上使用新一代 Apple Foundation Models，并免收云 API 费用。[S16]

机器学习总览页只简写为低于 200 万次首次下载。[S17] 本报告采用条件更完整的口径。最终配额、资格核验、地区、服务等级和协议仍需以正式开发者条款为准。

### 5.3 Core AI 与 MLX 的分工

Core AI 面向开发者自带模型的端侧部署，强调 Swift API、提前编译、硬件专用化、推理内存控制、零拷贝数据路径和有状态执行。MLX 更偏向研究、训练和微调，支持 Metal 4、GPU Neural Accelerators，以及多台 Mac 通过 Thunderbolt 上的 RDMA 进行分布式训练和推理。[S17][S23]

| 需求 | 主要工具 |
|---|---|
| 使用 Apple Intelligence 内置模型 | Foundation Models |
| 接入外部云模型 | 模型无关协议与提供商适配 |
| 调用 PCC 上的 Apple 模型 | Foundation Models + PCC |
| 部署自有端侧模型 | Core AI |
| 在 Mac 上研究、训练、微调 | MLX |
| 让 Siri 理解应用内容和动作 | App Intents |
| 验证生成质量和代理行为 | Evaluations + Instruments |

### 5.4 Evaluations 把概率系统纳入工程流程

新的 Evaluations framework 用于系统测试 prompt、工具调用和智能功能，并支持 hill-climbing 等优化路径。Instruments 增加代理式体验的性能与行为分析。[S16][S17][S23]

官方安全会话进一步把代理风险归纳为 prompt injection、不安全输出处理和 excessive agency，并建议输入验证、输出约束、最小权限和明确的用户确认。[S28]

生产级 AI 功能至少需要四类测试：

1. 确定性测试：权限、工具参数、状态转换和失败恢复。
2. 统计评估：答案质量、召回率、拒答和幻觉比例。
3. 对抗测试：提示注入、越权工具调用、恶意内容和数据泄露。
4. 运行评估：延迟、能耗、内存、网络、额度与供应商故障。

---

## 06. Xcode 27、Swift 6.4 与 SwiftUI

### 6.1 Xcode 27：代理进入原生工程上下文

Xcode 27 支持来自 Anthropic、Google、OpenAI 的编码代理。Agent Client Protocol 扩展代理接入方式，MCP 继续用于工具和上下文连接。GitHub 与 Figma 提供直接安装入口。[S13][S23]

其他关键更新包括：

- 代理生成原型、实现代码、修复问题并处理重复任务。
- 翻译代理新增语言、更新 String Catalog 和复数规则。
- Device Hub 集中管理真机与模拟器，便于检查状态和复现问题。
- Instruments 强化 Swift Concurrency、Time Profiler、System Trace 和运行对比。
- Xcode 27 仅支持 Apple silicon，统一安装器体积缩减约 30%。[S23]
- Xcode Cloud 构建最高提速 2 倍。[S23]

编码代理缩短了局部实现时间，也扩大了审查面。仓库权限、可调用工具、生成差异、测试证据和回滚路径必须成为团队规范。

### 6.2 Swift 6.4：减少跨平台与性能路径摩擦

Swift 6.4 的主要更新包括：[S14][S23]

- `anyAppleOS` 简化平台可用性表达。
- `@diagnose` 提供更细粒度的警告控制。
- `defer` 支持异步代码，确保返回或抛错时执行清理。
- 新迭代协议支持 `Span`、`InlineArray` 等 noncopyable 类型。
- Foundation 的 URL 解析最高快 4 倍。
- Swift Testing 与 XCTest 互操作，便于增量迁移。

### 6.3 SwiftUI：大型界面、文档和构建效率

Apple 将这批能力标为 SwiftUI 2027 releases。[S15]

- `WritableDocument` 与 `ReadableDocument` 支持异步、增量磁盘读写。
- `Subprogress` 支持进度报告。
- `DocumentCreationSource` 支持多个文档创建入口。
- 新工具栏 API 控制可见性、溢出菜单、固定操作与滚动收起。
- 通用可重排容器支持 `List`、`LazyVGrid` 等布局，并扩展到 watchOS。
- `AsyncImage` 默认遵循 HTTP 缓存头。
- `@State` 中的类按视图生命周期惰性初始化。
- `ViewBuilder` 调整改善 Xcode 27 构建时间。

### 6.4 图形、游戏与机器学习硬件

Metal 4 引入神经加速能力，Game Porting Toolkit 4、Steam Asset Converter 和 Apple 提供的 Unity 插件降低游戏迁移与上架成本。MLX 可利用 Thunderbolt RDMA 连接多台 Mac。[S17][S23]

这组更新说明 Apple 对专业工作负载的重点已经从单机峰值扩展到工具链、资产转换、分布式计算和商店交付。

---

## 07. Keynote 之外：137 个索引条目的技术全景

WWDC 的发布价值通常集中在 Keynote，工程价值则分散在技术会话。6 月 16 日的索引分类如下。[S18]

| 分类 | 条目数 | 主要主题 |
|---|---:|---|
| AI & Machine Learning | 29 | Foundation Models、Core AI、MLX、代理、安全、评估 |
| App Services | 18 | Siri、App Intents、Spotlight、StoreKit、地图、健康 |
| SwiftUI & UI Frameworks | 13 | 文档、工具栏、重排、动画、组件 |
| Essentials | 12 | Keynote、PSOTU、每日回顾、入门 |
| Graphics & Games | 11 | Metal 4、游戏移植、图形调试 |
| Swift | 10 | Swift 6.4、并发、测试、性能 |
| Developer Tools | 8 | Xcode 27、Instruments、Cloud、设备 |
| System Services | 7 | 容器、文件、网络、后台任务 |
| Design | 7 | Liquid Glass、图标、空间与交互 |
| Spatial Computing | 5 | Reality Composer Pro、OpenUSD、流式传输 |
| 其他 8 类 | 17 | 相机、音视频、商店、无障碍、Web、安全 |

### 7.1 生产基础设施

**gRPC 与 Swift**：官方会话覆盖流式 RPC、服务代理、可观测性和跨语言服务，说明 Swift 服务端与多语言基础设施的连接继续成熟。[S30]

**Linux 容器与 macOS**：`swift-container` 可在 macOS 上运行 Linux 容器和容器编排工作负载，为本地开发、测试和工具集成提供更原生的路径。[S29]

**MetricKit**：新内容覆盖启动与退出、CPU、内存、磁盘、网络、`os_signpost` 和 Hangtracer。性能数据正在从单次 Instruments 分析扩展到真实用户环境的持续观察。[S31]

### 7.2 代理安全与数据治理

代理安全会话要求团队把 prompt injection、不安全输出和过度授权视为产品风险。Trust Insights 则帮助开发者分析数据用途、第三方 SDK、required reason API 和隐私政策结构，可生成 XML 与 PDF 报告。[S28][S32]

两者共同给出一条清楚的工程原则：AI 权限与传统数据权限必须在同一套威胁模型中管理。模型能否调用工具、工具能访问什么、结果如何展示，都需要可审计。

### 7.3 Web、空间计算与媒体

Safari 27 与 WebKit 更新包括可定制 Web App 工具栏、Relevant Interests、2D 图形性能、CSS Grid Lanes、HTML `select`、Web Inspector、Payment Request API、SVG 和 DCI-P3。[S33]

空间计算会话覆盖 Reality Composer Pro 3、OpenUSD、USDKit、动态光照、角色动画和 foveated streaming。相机与媒体会话涉及 Center Stage、RAW、高分辨率采集、Now Playing 和 tvOS Dynamic Type。[S18]

### 7.4 团队如何选择会话

不要按索引顺序观看全部内容。更有效的方法是先按项目风险选题：

- 做 AI 产品：Foundation Models、App Intents、Evaluations、代理安全。
- 做大型客户端：Swift 6.4、SwiftUI、Instruments、MetricKit。
- 做跨平台后端：gRPC、容器、可观测性。
- 做游戏或空间应用：Metal 4、Game Porting Toolkit、OpenUSD、RCP 3。
- 做 Web 与商店业务：Safari 27、StoreKit、App Store 分发与营销。

---

## 08. OS 27 平台更新

### 8.1 跨平台共同层

六个平台共享的方向包括：

- 下一代 Apple Intelligence 与 Siri AI
- Liquid Glass 可读性和一致性修正
- 搜索、邮件、网络和基础性能
- 儿童安全与 Screen Time
- iCloud Shared Albums 跨 Android、Windows 参与
- 自然语言 Shortcuts 与 Calendar 输入
- 无障碍、字幕和图像描述

### 8.2 iOS 27

iOS 27 的重点包括 Camera 中的 Siri mode 与 Visual Intelligence、Photos 的 Spatial Reframing 与 Extend、Safari 标签页自动分组和页面变化提醒、Passwords 弱密码与泄露密码处理、Messages 与 Mail 上下文建议、自然语言 Shortcuts、围绝经期健康支持、HomeKit Secure Video AI 摘要与 4K，以及跨平台 Shared Albums。[S07]

iOS 27 支持 iPhone 11 系列及以后机型，以及 iPhone SE 第二代及以后机型。系统升级资格不等于 Apple Intelligence 或 Siri AI 资格。[S07]

### 8.3 iPadOS 27

iPadOS 27 强化截图视觉理解、Apple Pencil 圈选、Notes 内容整理、自然语言描述 Shortcuts、外置盘性能和 Calendar 自然语言输入。官方示例可让 Shortcut 调用 Windowed Apps，并把 Safari 与 Notes 平铺。Apple 宣称外置盘浏览与传输最高快 5 倍。[S08]

### 8.4 macOS 27 Golden Gate

macOS 27 把 Ask Siri 接入 Spotlight，支持对截图、图像和 PDF 使用 Visual Intelligence，并统一工具栏、侧栏、窗口和菜单栏层级。系统支持超宽显示器 5K 120Hz，改进 AirDrop、网络文件浏览、Safari 起始页和 Mail 搜索。[S09]

兼容范围全面转向 Apple silicon，包括 2026 MacBook Neo，以及 Apple 列出的 2020 年后多款 MacBook、Mac mini、iMac、Mac Studio 和 Mac Pro。[S09]

### 8.5 watchOS 27

watchOS 27 重新组织动态应用网格和 Siri 建议，加入单手手势、独立 Workout Buddy、西班牙语支持、跑步机距离改进、围绝经期 Cycle Tracking、统一 Find My 和自定义 Wallet 二维码或条码卡片。[S10][S24]

### 8.6 visionOS 27

visionOS 27 支持注视对象后询问 Siri、固定 Siri 窗口、全景照片空间化、曲面窗口、Mac 3D 模型预览与编辑、增强 Quick Look、Reality Composer Pro 3 和 Safari Web Environments。Apple 宣称 Vision Pro 启动并连接 Wi-Fi 的速度最高提升 3 倍。[S11]

### 8.7 tvOS 27

tvOS 27 的价值主要体现在服务、媒体与无障碍体验。Apple Music 的 Automix 扩展到电视与 HomePod，tvOS 支持 Hi-Res Lossless，Apple TV 与 Apple Sports 获得直播和比分体验更新，开发者会话还覆盖 Dynamic Type 与 Now Playing。[S18][S24]

---

## 09. Apple 服务：AI 进入高频场景

WWDC26 的服务更新没有单独占据 Keynote 主线，却是 AI 从演示走向高频使用的重要部分。[S24]

| 服务 | 主要更新 | 关键边界 |
|---|---|---|
| Apple Maps | AI 增强的 Flyover；美国推出 Local Lists | Flyover 只覆盖部分城市，Local Lists 首发限美国 |
| Find My | 自定义位置共享时长、暂停到当天结束；Watch 合并三个查找应用 | Precision Finding 受设备条件限制 |
| Apple Wallet | 扫描账单并用 Apple Cash 拆账；实体卡转 Pass；增强酒店钥匙 | 拆账仅限美国并依赖合格设备与 Siri AI |
| Apple Podcasts | 视频播客扩展到 Mac 与 tvOS；画中画、转录、章节和节目内搜索 | 内容与地区可用性由节目和设备决定 |
| iCloud Shared Albums | 全分辨率、更多文件类型、表情回应、临时相册与网页参与 | 无 Apple 设备的用户通过网页参与 |
| Apple Music | 歌词翻译与读音扩展；AutoMix 进入 tvOS 和 HomePod；tvOS 支持 Hi-Res Lossless | 曲目、语言和外接音频设备条件不同 |
| Apple TV / Sports | 覆盖 MLB、MLS、F1 等赛事；Sports 扩展到 170 多个国家和地区 | 赛事版权和功能仍按市场分层 |
| Apple Fitness+ | Strong Through Menopause 三周计划；Busy Philipps 的 Time to Walk | 属于 Fitness+ 内容更新 |

这批更新的共同点是把智能能力放进地图、支付、媒体和共享流程。体验质量取决于数据授权、地区资格、内容版权、设备和订阅，不只取决于模型本身。

---

## 10. 性能、搜索、网络与 Liquid Glass

Apple 给出的性能数字需要和测试条件一起阅读。[S03]

| 指标 | Apple 宣称最高提升 | 测试条件摘要 |
|---|---:|---|
| iPhone / iPad 应用启动 | 30% | iPhone 11 Pro Max，旧版与预发布系统对比 |
| 新照片载入 | 70% | iPhone 15，50,000 项照片库 |
| AirDrop | 80% | iPhone 16 Plus，未连接 Wi-Fi，传输多张照片 |
| iPad 外置盘 | 5 倍 | 11 英寸 iPad Pro M4、APFS USB4 SSD、10,000 个 JPG |
| Vision Pro 启动与 Wi-Fi | 3 倍 | 产品页宣称，实际表现依环境而变 |

这些数字不能推导出“所有设备整体快 30%”。它们是特定任务、设备和预发布软件下的最高结果。真正值得跟踪的是 CPU scheduler、搜索基础、网络切换和文件系统路径是否在多代设备上持续改善。

搜索方面，Apple 重建 Spotlight、Photos 和 Mail 的基础，目标是提高稳定性、效率、内容覆盖和新内容进入索引的速度。Mail 增加 Top Hits 相关性排序。搜索质量与 Siri 个人上下文已经共用同一条系统基础。[S03]

Liquid Glass 保留，但提高折射一致性和对比度，图标更锐利，用户可在 ultraclear 与 fully tinted 之间调节。macOS 还恢复统一工具栏和更清楚的侧栏层级。[S03][S07][S09]

---

## 11. 儿童安全与平台治理

Apple 将儿童安全拆成内容、通信和使用时间三个问题。[S05]

### 内容与访问

- Setup Assistant 可从必要应用、推荐应用集或自选应用开始。
- Ask to Buy 继续控制应用下载与内购。
- Ask to Browse 要求儿童访问新网站前向家长申请。

### 通信安全

- 家长可要求儿童添加新联系人前取得批准。
- Communication Safety 从裸露内容扩展到血腥与暴力图片、视频。
- 未满 18 岁用户默认启用相关保护，具体规则受地区影响。

### 时间与习惯

- Time Allowances 按 Entertainment、Games、Social Media 设定总时长。
- Schedules 控制不同日期和时段可用的应用。
- Screen Time 显示平均用量、高频应用并支持即时调整。

开发者需要配合 SensitiveContentAnalysis、PermissionKit、Declared Age Range API 和更新后的年龄分级问卷。[S05]

这套治理结构保留家长决策权，也把内容识别、年龄范围、联系人权限和审核责任分配给系统与开发者。涉及未成年人的产品应把这些接口纳入核心流程，而不是在上架前补做合规。

---

## 12. App Store：营销、订阅与组合销售

WWDC26 的 App Store 更新可分为四组。[S06][S25]

### 12.1 营销素材

- Creative Assets 计划于秋季进入产品页头部、搜索结果、App Store 推荐位和 Apple Ads。
- Asset Library 计划于秋季集中管理图像、视频、app previews 和截图。
- 素材可独立于应用版本提交，并提前获得未来产品页或广告活动所需的审核。
- Mac App Store 取消 Intel 支持要求的改动标记为 coming soon。

### 12.2 发现与推荐

- Personalized Collections 根据兴趣、使用和下载记录组织推荐，目前只在部分国家和地区面向有限应用开放。
- App Notes 解释推荐原因。
- 游戏可通过 Featuring Nominations 提交活动和限时优惠，计划于夏季先在美国 Apple Games 上线。

### 12.3 订阅与席位

- 按月付费、承诺 12 个月的订阅方案已可配置，覆盖除美国和新加坡外的市场，并要求相应系统至少为 26.4。[S25]
- Volume purchasing 计划于秋季提供，面向组织和教育采购。[S25]
- Group purchases 计划于年内稍后提供，由购买者分配席位。[S25]
- Bundles 和 Suites 提供组合订阅结构，申请与配置细节计划于夏季稍后公布。[S25]
- Retention Messaging 计划于秋季进入取消流程。[S25]

原稿把 Group purchases 写成“冬季”，闭幕后官方指南采用“later this year”的更宽口径。本版按指南修正，不推断具体季度。[S25]

### 12.4 审核效率

App Store Connect 网页端和 API 计划于夏季稍后支持把多个内购项目合并为一次提交，也可与 In-App Events、custom product pages 和产品页优化测试一起送审。营销素材则能独立于应用版本提交。对活动频繁、订阅层级复杂的产品，这会减少版本发布与商业运营之间的耦合。[S25]

---

## 13. 兼容性与可用性矩阵

### 13.1 七种条件必须分开

| 层级 | 代表问题 | 典型门槛 |
|---|---|---|
| OS 27 升级 | 设备能否安装新系统 | iOS 27 支持 iPhone 11 起 |
| Apple Intelligence | 能否运行本轮 AI 功能 | 芯片、内存和设备代际限制 |
| Siri AI 开发者测试 | 当前能否开发和测试 | 6 月 8 日起四个平台，watchOS 稍后 |
| Siri AI 消费者 beta | 普通用户何时能用 | 2026 年稍后，首发英语 |
| 最强端侧模型 | 能否运行最高规格模型 | 更高代芯片和内存门槛 |
| 地区与语言 | 功能是否在当地开放 | 中国、欧盟和语言条件不同 |
| 服务器额度 | 云端能力能否持续调用 | 每日上限与 iCloud+ 额度 |

### 13.2 Apple Intelligence 与 Siri AI 设备

Apple 列出的主要范围包括：[S03][S04][S21]

- iPhone 16 系列及以后
- iPhone 15 Pro、iPhone 15 Pro Max
- iPad mini A17 Pro
- M1 及以后 iPad
- MacBook Neo A18 Pro
- M1 及以后 Mac
- Apple Vision Pro
- Apple Watch Series 9 及以后
- Apple Watch Ultra 2 及以后
- Apple Watch SE 3，且附近配对 iPhone 需支持 Apple Intelligence

### 13.3 最强端侧模型设备

最高规格端侧模型及其驱动的表现力语音和高级听写，需要更高配置：[S04]

- iPhone Air
- iPhone 17 Pro、iPhone 17 Pro Max
- M4 及以后、至少 12GB 统一内存的 iPad
- M3 及以后、至少 12GB 统一内存的 Mac
- M5 Apple Vision Pro

### 13.4 语言与地区

Apple Intelligence 支持英语、丹麦语、荷兰语、法语、德语、意大利语、挪威语、葡萄牙语、西班牙语、瑞典语、土耳其语、越南语、简体中文、繁体中文、日语和韩语。具体功能会因语言与地区而异。[S03]

Siri AI 消费者 beta 首发仍是英语。中国暂不开放新 Siri AI 和其他新 Apple Intelligence 功能。欧盟首发时，Mac 与 Apple Vision Pro 可在满足语言条件时使用 Siri AI，iOS、iPadOS 与 watchOS 暂不提供。[S03][S04][S21]

**判断规则**：支持中文不等于中国地区可用，也不等于 Siri AI 首发支持中文。语言、地区、设备、功能和额度需要逐项核对。

---

## 14. Apple Design Awards 2026

Apple 从 36 个入围作品中选出 12 个获奖者，覆盖六个类别。[S27]

| 类别 | 应用获奖者 | 游戏获奖者 |
|---|---|---|
| Delight and Fun | grug | Is This Seat Taken? |
| Inclusivity | Guitar Wiz | Pine Hearts |
| Innovation | NBA: Live Games & Scores | Blue Prince |
| Interaction | Moonlitt: Moon Phase Tracker | Sago Mini Jinja’s Garden |
| Social Impact | Primary: News in Depth | Consume Me |
| Visuals and Graphics | Tide Guide: Charts & Tables | Cyberpunk 2077: Ultimate Edition |

获奖名单本身不是平台趋势的完整样本，但能反映 Apple 公开强调的设计标准：清楚的核心交互、无障碍、技术与内容的结合、社会价值，以及对平台图形能力的有效使用。

---

## 15. 对用户、开发者与 Apple 的意义

### 15.1 对普通用户

近期最确定的收益来自 OS 27 的性能、搜索、网络、界面可读性、儿童安全和服务更新。Siri AI 的潜在价值更大，交付不确定性也更高。普通用户应把它视为 2026 年稍后开始扩展的英语 beta，而不是秋季即可稳定使用的全球功能。

### 15.2 对产品与工程团队

未来两个季度的重点应放在系统接入与风险基线，而非简单添加聊天框：

1. 盘点可由 Spotlight 和 Siri 理解的实体。
2. 用 App Intents 暴露少量高价值、可逆的动作。
3. 用 View Annotations 建立屏幕对象与实体映射。
4. 在端侧、PCC 和外部模型之间定义路由与降级。
5. 为所有代理工具设置最小权限和用户确认。
6. 用 Evaluations、App Intents Testing、Instruments 和 MetricKit 建立持续验证。
7. 检查儿童账户、年龄范围、联系人和内容安全接口。
8. 重新评估年度承诺、组织采购、群组席位和跨开发者组合。

### 15.3 对 Apple

Apple 的优势是垂直整合：设备、芯片、系统索引、应用动作、端侧模型、私有云、IDE 和分发渠道可以共同优化真实任务。

压力同样明确。Siri AI 仍处于开发者测试与消费者 beta 节奏，地区与硬件分层复杂，部分能力依赖服务器额度和外部模型。Apple 需要证明这套系统在真实设备上稳定、快速、可解释，并兑现隐私承诺。

### 15.4 三个成败标准

1. Siri 能否在复杂个人上下文中稳定找到正确内容并执行正确动作。
2. 第三方应用是否愿意、也是否容易通过 App Intents 和模型协议接入。
3. Apple 能否按承诺扩展语言、地区与设备，同时维持隐私、延迟和成本。

如果这三点成立，Siri AI 的价值会表现为系统任务完成率。若长期缺失任何一项，独立应用和更强模型也难以补足系统协作。

---

## 16. 仍需追踪的问题

截至北京时间 2026 年 6 月 16 日，以下事项尚无完整答案：

- Siri AI 消费者 beta 的具体日期。
- 英语之外的语言扩展顺序与时间。
- 中国地区的监管进展和可用范围。
- 欧盟 iOS、iPadOS、watchOS 版本的开放时间。
- 每日 AI 使用上限、iCloud+ 提升额度和地区价格规则。
- PCC 开发者模型的最终配额、资格审核和服务协议。
- 外部模型的计费、隐私提示、日志政策和失败降级。
- 不同设备上端侧模型的质量、延迟、内存和耗电差异。
- Siri AI 在第三方应用中的动作覆盖率与错误恢复能力。
- 组织采购、群组购买、Bundles 和 Suites 的精确上线日期。
- 三个 available soon 的 Group Lab 页面何时上线。
- Apple 性能基准在旧设备、低电量和长期使用中的实际表现。

---

## 17. 建议阅读与观看顺序

时间有限时，按以下顺序进入官方材料：

1. WWDC26 软件总览，建立全局视图。[S03]
2. Siri AI 与 Apple Intelligence 新闻稿，理解能力、架构和开放节奏。[S04][S21]
3. Platforms State of the Union，理解开发者平台的整体连接方式。[S20]
4. Apple Intelligence 和机器学习开发者页，理解模型、App Intents、Core AI、MLX 与 Evaluations。[S16][S17]
5. Xcode 27、Swift 6.4 与 SwiftUI 页面，理解工程工作流变化。[S13][S14][S15]
6. App Store 指南和服务新闻稿，理解商业与高频用户入口。[S24][S25]
7. 根据项目风险选择代理安全、gRPC、容器、MetricKit、Trust Insights 和 WebKit 会话。[S28][S29][S30][S31][S32][S33]
8. 最后使用视频索引补齐具体框架，不必线性观看全部条目。[S18]

---

## 附录：证据等级与写作规则

- **官方事实**：Apple Newsroom、Apple Developer、产品页直接陈述。
- **官方基准**：Apple 在特定软硬件和测试条件下公布的结果。
- **官方平台数据**：Apple 自报的用户量、内容量和平台规模，未作独立审计。
- **页面测量**：对 Apple 页面进行去重计数或结构化整理，注明方法与日期。
- **分析判断**：基于官方事实形成的解释，不代表 Apple 表态。
- **未知事项**：官方尚未给出精确日期、配额、地区或实测结果。

完整链接和使用边界见 `sources.md`，核心主张与证据映射见 `data/claim-map.tsv`。
