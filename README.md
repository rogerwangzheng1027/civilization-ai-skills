# CIVILIZATION · AI Specialists

> **看清真实市场，打破惯性思维。**  
> *Understand the real market. Break habitual thinking.*

**一套帮助团队找准问题、发现新解法的 AI 专家协作系统。**

我们不希望 AI 只是顺着客户的 Brief 寻找证据，也不希望它把阶段性洞察包装成一个逻辑漂亮、创意平庸的 Idea。

- **Brief Discovery｜不被既定问题限制判断。** 先看市场如何变化、对手如何竞争、消费者为何选择，再回头判断客户真正需要解决什么。
- **Creative Exploration｜不被既定思路限制想象。** 从同一个真实问题和事实材料出发，先开放发明不同的 Idea，再检查它是否有新意、属于品牌、能否解决问题。

在此基础上，由 **1 个 Project Hub + 4 个专业 Specialist** 分工协作，继续完成产品创新、提案发展与状态交接。专业研究提供可靠事实，开放创意探索新的可能；**不为预设判断找证据，不为平庸想法补逻辑。**

> **AI 先做实质工作，人负责判断、选择和纠偏。**

### 1 Hub + 4 Specialists

- **Project Hub**｜我现在在哪里，下一步该找谁？
- **Brief Discovery**｜市场与消费者正在发生什么？客户为什么提出这道题？真正的问题在哪里？
- **Creative Exploration**｜还有什么我们没有想到？
- **Product Innovation**｜产品本身还能怎么变？
- **Proposal Development**｜怎么把已有 Solution 发展成一份完整提案？

> **Public Learning Edition / 公开学习版**  
> 本仓库公开的是可学习、可讨论、可持续迭代的通用方法与基础 Skill。CIVILIZATION 的客户案例、专有数据、内部评估机制及其他未公开实现细节不属于本公开仓库的一部分。

## 一个底层原则

> **看清真实市场，打破惯性思维；一个 Skill 专门解决一个专业问题，并把它解决透。**

共享协议可以统一，但不同工种不因为“复用方便”就塞进同一个超级 Prompt。

### Reality Check & Challenge Protocol

> **Reality over Plausibility. Challenge must create value, not complexity.**

在关键判断上区分真实行为与合理推断，寻找能够改变决策的反证、竞争性解释和最小验证。默认只在内部轻量执行；仅当可能影响问题定义、方向选择或重大投入时深入挑战。**不新增角色、常规研究轮次或默认交付物；反驳不是目的，判断增量才是目的。** 统一规则以 Project Hub 为唯一原文；Brief 在诊断时、Creative 在想法产生后、Innovation 在 Selection 时、Proposal 在 Solution 检验时各按需执行。

这也是当前结构从原先三个专业 Skill 调整为 **1 Hub + 4 个专业 Specialist** 的原因：传播创意与产品创新是两类任务、两类判断、两类交付，应由两个独立 Skill 承接。

## 当前工作流：1 Hub + 4 Specialists

| Skill | 当前版本 | 什么时候用 | 核心作用 |
| --- | --- | --- | --- |
| [Project Hub](./project-hub/SKILL.md) | v1.12 | 新项目、阶段切换、重要 Review 后 | 管理项目状态、共享协议与交接；判断当前在哪里、下一步该找哪个专业 Specialist |
| [Brief Discovery Specialist](./brief-discovery-specialist/SKILL.md) | v1.28 | 刚收到 Brief、问题定义或关键前提不清楚 | **先研究市场、竞争、用户行为与品牌资产**；再理解客户目标和提出 Brief 的动机；最后诊断现实与客户期待的落差，形成有证据的解题判断与机会方向 |
| [Creative Exploration Specialist](./creative-exploration-specialist/SKILL.md) | v3.1 | 问题基本清楚，需要寻找传播创意解法，或已有 Idea Seed 需要继续做强 | 从原始问题和真实材料直接展开 OPEN CREATIVE LEAP，先给有差异的 Idea Seed；之后检验问题价值与品牌归属，按需深化或使用案例研究 |
| [Product Innovation Specialist](./product-innovation-specialist/SKILL.md) | v1.7 | 需要探索产品 / SKU / 配方 / 风味 / 功能 / 包装 / 规格等创新 | 用真实市场案例和可衡量结果筛选创新机制，形成可测试的产品创新方向与假设 |
| [Proposal Development Specialist](./proposal-development-specialist/SKILL.md) | v1.16 | 已有 Strategy / Idea / Innovation Direction，需要形成完整提案文件 | 用 Storyline 压力测试并发展 Solution；证据状态必须保留到标题与文案，最终形成可直接进入 PPT / PDF 的提案内容 |

一句话记住：

> **Hub 管导航与交接；Brief 管问题和 Brand Logic；Creative 从真实问题发明、筛选和深化传播 Idea；Innovation 管产品创新；Proposal 管提案文件的发展与成稿。**

### 推荐不等于选择

AI 应该主动给出 **CURRENT BEST JUDGMENT**，必要时可以沿最值得推进的方向继续做深；但 **AI Recommendation ≠ SELECTED**。

只有用户 / 团队 / 客户明确选择，或上游 Project State 已可靠记录为已选时，才进入 `SELECTED DIRECTIONS`。用户只说“继续”不算选择。

## Brief Discovery v1.28：先理解市场竞争，再理解 Brief

**先研究市场怎样运作、主要品牌怎样竞争、消费者怎样选择；再理解客户为什么提出这个 Brief，最后诊断问题。** 不围绕客户预设的竞争对手、TA、品类结论与解决方案去找佐证。

```text
OUTSIDE-IN MARKET SYSTEM
  → 市场演进、消费者选择、渠道与价格竞争
  → 主要竞争者的定位 / 用户 / Offer / 营销 / 竞争表现
  → 本品牌的相对竞争位置
                  ↓
INDEPENDENT PROBLEM LANDSCAPE
  → 不受客户预设诊断影响，先识别真正值得解的问题
                  ↓
CLIENT INTENT + REALITY × INTENT GAP
  → 客户为什么现在提这道题？看对了什么、忽略了什么？
                  ↓
STRATEGIC JUDGMENT + NEXT HANDOFF
  → 形成有证据边界的问题定义、机会和决策建议
```

**竞争分析不是品牌名单 + Slogan + 新品新闻。** 必须在真实市场与购买情境中理解足以改变判断的主要品牌：其定位与品牌资产、目标及实际用户（如有数据）、主力产品与创新、价格渠道、代表性营销动作、竞争优势和真实表现。比较的是不同品牌如何争夺消费者选择，而不是把资料卡并排。研究对象、数量和篇幅由实际市场决定，不规定固定的六栏报告或竞品数量；缺数据保留 OPEN，不补造消费者认知或销售结果。

三轮内部节奏保持，**用户不用先回答问卷**。对小型任务保持适度深度，但不能用简短结论代替实际研究。关键竞品分析应在 Brief Gap 判断之前完成；ROUND 2 只补会改变决策的更深问题，不倒过来决定该搜谁。

引用外部理论、研究模型或专业术语时核对原义与适用条件。品牌 Restage / Repositioning / Brand Platform 等任务按需形成 Brand Logic，但必须从消费者、竞争与品牌事实综合出来；**Human Spark 不是预选答案，也不是给 Creative 强制继承的一条推导链**。

## 新增的增长与产品创新判断

- **Growth Diagnosis（Brief）**：需要时核对数据来源、口径及可比性，从增长结果找到真正的Growth Job，不把相关性伪装成因果。
- **Product Deconstruction（Innovation）**：先拆既有产品如何创造价值，再研究市场赢家实际改了什么，而不是套用固定品类模型。
- **Consumer Value Expansion（Innovation）**：产品组合扩张不等于消费者价值扩张；同时检查新用户、老用户、新场景与品牌内部互食。
- **Option Integrity & Concept Test（Innovation）**：区分产品、概念、表达Option，设计能检验真实差异的验证方案；功能成分需独立核实含量、法规及功效依据。
- **Direct Review & Artifact QA（Hub / Proposal）**：单页、单句、单表格任务直接处理；实际文件交付前检查证据、排版、可编辑性及渲染结果。

上述都是**按需触发的内部能力**，不是新增的轮次、表单或第五个Specialist；公开Skill不写任何特定客户案例作为默认答案。

## 工作流不是唯一线性的

```text
Project Hub
  ↓
Brief Discovery
  ├─→ Creative Exploration
  │      ↓
  │   Proposal Development
  │
  └─→ Product Innovation
         ├─→ R&D / Technical Validation
         ├─→ Consumer / Prototype Test
         ├─→ Business / Channel Validation
         ├─→ Proposal Development
         └─→ Creative Exploration
              （产品方向基本锁定后，需要传播探索时）
```

### Review 后怎么判断

- **KEEP**：Solution 成立，只需继续发展表达、证据或执行。
- **REPAIR**：方向基本成立，但局部连接缺失；留在 Proposal 做受限 Repair。
- **CREATIVE REOPEN**：需要重新打开传播创意可能性。
- **INNOVATION REOPEN**：需要重新打开产品创新可能性。
- **BRIEF REOPEN**：客户目标、问题定义、关键前提或 Strategy Territory 被改变。

## 两个探索 Specialist 为什么拆开

### Creative Exploration Specialist v3.1

本次重构默认工作方式：**Problem First → Open Creative Leap → First Cut → Reality Test → Select / Develop**。

```text
SAME PROBLEM + SAME FACTUAL MATERIALS
                 ↓
OPEN CREATIVE LEAP｜先发明不同的 Idea Seed
                 ↓
FIRST CUT｜是否有惊喜、可能解决问题、品牌能否拥有？
                 ↓
REALITY TEST｜再查消费者、竞争、品牌依据与执行条件
                 ↓
SELECTION / IDEA DEVELOPMENT｜选中后才做强
```

**Human Spark / Human Insight / Creative Spark 仅作可选的、保留 SOURCE × STATUS 的研究材料**；不再要求 Case Landscape → Insight → Spark → Idea 的固定演绎。没有创意突破，就换一个机制重新发明，不用策略文案给平庸 Idea 辩护。

- 默认 **IDEA FIRST**：Brief 的真实问题、材料与约束是起点；先展示可感知的 Big Idea / 内容 / Activation 创意种子，而不是先交一套合理性的叙事。
- **CASE RESEARCH / RESEARCH ATLAS**：用户明确要求案例研究、或事实问题确有研究必要时按需启动；正式案例仍需真图、链接、来源与交付 QA，不能以案例包装自嗨方案。
- **IDEA SEED DEVELOPMENT**：已有选中的 Seed 时直接打磨；是否做完整 Campaign Platform / IMC 由任务决定。
- 筛选强调真实差异、问题解决潜力和 Brand Right，证据与可行性在 Idea 初筛后集中校验，不用伪造数据或编造消费者洞察。

第一轮停在有真实差异的 Idea Seed 供用户校准，而不是停在案例搜集之后。AI 可以条件性推荐并继续，但 Selection Authority 仍归用户 / 团队 / 客户。

### Product Innovation Specialist v1.7

新增轻量 **Promise → Experience → Proof Fit** 一致性检查：不把概念利益直接当实际体验或产品事实，区分已知不可行与尚待验证。跨职能交接统一使用 Hub 的 `CROSS-WORKSTREAM SIGNALS`。

专门研究：
- Product / SKU
- Formula / ingredient
- Flavor
- Function / benefit
- Format / texture
- Pack / portion / specification
- Process / proposition / product-line innovation

核心流程：

```text
INNOVATION CASE LANDSCAPE
  ↓
SPARK CALIBRATION
  ↓
FOLLOW THE SPARK
  ↓
SELECTION GATE: KEEP / HOLD / DROP
  ↓
INNOVATION TRANSLATION
  ↓
TESTABLE HYPOTHESIS / PROOF NEEDED
```

市场证据强制拆成三件事，并按具体 Claim 单独继承 Project State 的 SOURCE × STATUS：

> **RESULT SCOPE**：这个数字是谁的？SKU / PLATFORM / BRAND / CATEGORY  
> **EVIDENCE QUALITY**：证据有多强？A / B / C / D / E  
> **CAUSALITY CHECK**：结果多大程度能归因于该创新？

Product Innovation 不自动进入 Campaign / IMC。产品方向基本锁定、且明确需要传播探索时，再进入 Creative Exploration。

v1.7 继续保留 Result Scope / Evidence Quality / Causality 这些硬规则，但用户可见输出会先把产品机会讲成人话：谁为什么会想买、产品到底改了什么、吃到 / 用到时有什么不同，再补 Consumer Job、Innovation Mechanism 与证据。Product 内部的用户校准环节也统一改为 Spark Calibration，避免与 Brief 的 Human Spark 混淆。

## 安装

**ChatGPT 同事安装（推荐）**：先看 [CIVILIZATION AI Specialists 一页安装说明](./INSTALL_CHATGPT.md)，下载单插件 ZIP 后在个人 ChatGPT 的 Plugin Creator 上传。固定版本的 ZIP 不会自动覆盖已安装的版本。

安装后先读取 Plugin 根目录的 `VERSION_MANIFEST.json`，再与五个实际 `SKILL.md` 标题版本交叉验证。**不要让模型依据旧对话、README 或记忆猜“当前版本”。** 检查 GitHub 远端最新版是另一件事；如果当前环境无法实际访问 GitHub，应返回 `VERSION CHECK: NOT AVAILABLE`，不能声称“已核对 GitHub”。


### 支持 Skill 的 AI 工具

分别安装：

```text
project-hub/SKILL.md
brief-discovery-specialist/SKILL.md
creative-exploration-specialist/SKILL.md
product-innovation-specialist/SKILL.md
proposal-development-specialist/SKILL.md
```

**不要合并成一个超级 Prompt。**

### 不支持 Skill 安装的工具

把对应 `SKILL.md` 放进 Project / Workspace 的知识文件，或和项目材料一起上传，并明确说：

> 请严格按照我提供的 SKILL.md 工作。

共享项目状态模板：

[project-hub/PROJECT_STATE_TEMPLATE.md](./project-hub/PROJECT_STATE_TEMPLATE.md)

简短操作说明：

[QUICK_START.md](./QUICK_START.md)

## 五个 Skill 怎么使用

### 1. Project Hub

> 这是一个新项目。请建立 PROJECT_STATE.md，判断当前阶段，并告诉我下一步应该调用哪个 Specialist。不要做专业分析。

### 2. Brief Discovery Specialist

> 请按 Brief Discovery Specialist v1.28 工作。先根据项目范围独立研究市场发展、竞争趋势、消费者行为及品牌背景与资产；再完整阅读 Brief、会议材料，理解客户真正的需求和提出这道题的动机；最后分析与现实的关键落差，形成有证据的判断。不要先让我回答一堆问题，默认逐轮推进。

Brief 结束时应明确下一步属于：
- Creative Exploration
- Product Innovation
- 或其他专业环节

### 3. Creative Exploration Specialist

> 请按 Creative Exploration Specialist v3.1 工作。从当前 Brief 的原始问题、事实材料和约束直接发散真正不同、可想象的 Idea Seed；先看是否令人眼前一亮、能否解决问题，再做品牌与证据检验。不要要求先完成 Human Insight、Creative Spark 或案例推导，也不要把普通创意包装成 IMC。

ROUND 3 把选中机制变成具体 Idea Seed；如果已经有 KEEP 的 Idea 雏形，也可以直接进入 Concept Development，先优化 Concept，再决定是否发展 Execution / IMC。

### 4. Product Innovation Specialist

> 请按 Product Innovation Specialist v1.7 开始 ROUND 1。寻找真实产品创新案例，优先验证市场结果，并区分 Result Scope、Evidence Quality 与 Causality。案例之后停下来做 Spark Calibration；输出方向时先讲清谁为什么会想买、产品哪里变了、体验哪里不同。

ROUND 3 把选中机制变成可测试的产品创新方向，而不是传播方案。

### 5. Proposal Development Specialist

> 请按 Proposal Development Specialist v1.16 工作。基于已确认的 Strategy / Idea / Innovation Direction，先检查 Solution 是否足以支撑提案，再形成 Proposal Spine、Storyline、Page Plan 和关键文案，最终发展成完整提案文件。如果核心方向本身不成立，再触发对应 Reopen。客户可见文字要讲人话，内部框架不要原样倒给客户。

## `PROJECT_STATE.md` 是共享记忆

核心字段：

- CLIENT ASK
- CURRENT PROBLEM DEFINITION
- CURRENT BEST JUDGMENT
- LOCKED
- LIVE HYPOTHESES
- SELECTED DIRECTIONS
- HOLD
- DROPPED / SUPERSEDED
- REVIEW CHANGES
- OPEN QUESTIONS / DECISION BLOCKERS
- EVIDENCE NOTES
- NEXT HANDOFF

证据统一使用 `SOURCE × STATUS`；SOURCE 不明时使用 `UNKNOWN`，不得猜 CLIENT / TEAM。材料存在、数字真实、因果成立、适用于本项目是不同 Claim，分别判断 STATUS。

### HOLD 的含义

**HOLD ≠ Supporting Layer。**

下游不得为了“都用上”而把 HOLD 或 DROP 自动改造成 Content / Social / extra SKU / packaging layer。重新打开必须有用户要求、新证据或 Review 变化。

## 协作原则

- **AI 先做实质工作，人负责判断和纠偏。**
- **专业问题由专业 Skill 承接。** 不用一个 Skill 同时解决 Creative 与 Product Innovation。
- **真实案例是刺激，不是模板。**
- **先选择，再体系化。** `Systemization is downstream of selection.`
- **Proposal 只修不从零造。** 缺 Idea 就 Creative Reopen；缺 Product Innovation Direction 就 Innovation Reopen。
- **Storyline 是诊断工具，不只是排版工具。**
- **底层判断可以很严谨，表面语言不要很费劲。** Brief / Creative / Product Innovation / Proposal 的用户可见文字共同参考 [LANGUAGE_CONTROL.md](./LANGUAGE_CONTROL.md)，其中吸收了 Khazix Writer 的去 AI 化、自然语言化原则。
- **PDF / PPT 是按需交付，不是完成工作的指标。**
- **注意客户保密与素材权限。**

## 文件结构

```text
civilization-ai-skills/
├── README.md
├── QUICK_START.md
├── LANGUAGE_CONTROL.md
├── LICENSE
├── COMMERCIAL_USE.md
├── project-hub/
│   ├── SKILL.md
│   ├── PROJECT_STATE_TEMPLATE.md
│   └── test-prompts.json
├── brief-discovery-specialist/
│   ├── SKILL.md
│   └── test-prompts.json
├── creative-exploration-specialist/
│   ├── SKILL.md
│   └── test-prompts.json
├── product-innovation-specialist/
│   ├── SKILL.md
│   └── test-prompts.json
├── proposal-development-specialist/
│   ├── SKILL.md
│   └── test-prompts.json
└── tests/
    └── protocol-consistency.json
```

## 协议同步规则

Project Hub 是共享协议唯一原文。

- Hub 修改共享标签、Handoff、Reopen、证据语言时，同步更新受影响 Specialist。
- Specialist 如要新增共享标签或交接字段，必须先或同时更新 Hub。
- 专业内部方法不写进 Hub，避免 Hub 变成超级 Skill。

### 版本与更新

公开正式版本以 GitHub 仓库 main branch 为 Canonical Source：

> https://github.com/rogerwangzheng1027/civilization-ai-skills

版本检查规则统一定义在 **Project Hub v1.12 的 VERSION / UPDATE PROTOCOL**。四个 Specialist 只继承，不重复维护。

历史正式版本已经用 Git Tags 归档；版本命名、当前版本与回退说明见：

[VERSION_HISTORY.md](./VERSION_HISTORY.md)

若已知距上次版本检查超过 7 天、版本来源不明，或用户明确要求检查最新版，且当前环境可以访问仓库，则先检查更新。发现新版本时必须提示差异，**不得静默覆盖当前 Skill**。

> Skill 本身不能后台定时运行；真正的每周主动检查需要外部 Automation / Scheduler。

## License & 使用边界

**Free to learn. Not free to commercialize.**

除非文件中另有标注，本仓库中由仓库所有者原创的文字、Skill、Prompt、模板和方法表达采用 **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International（CC BY-NC-SA 4.0）** 许可。

在该许可下，你可以阅读、学习、研究、非商业改编与分享；公开分享时需要保留适当署名，并以相同许可方式分享衍生作品。

**本仓库不授予商业使用许可。** 如果使用目的主要面向商业优势或金钱补偿，例如：

- 用于付费咨询、客户项目或商业交付；
- 用于收费课程、培训、工作坊或认证；
- 嵌入收费软件、SaaS、Agent、平台或其他商业产品 / 服务；
- 将本仓库的 Skill、Prompt 或实质性改编版本直接部署进商业机构的生产工作流，以支持商业项目或收入活动；
- 重新包装、分发或销售本仓库内容或其实质性衍生版本；

请先获得单独的书面商业授权。

商业机构的员工仍可以阅读、学习、研究和评估本仓库；是否属于商业使用，取决于具体使用目的和场景，而不是使用者是否来自商业机构。

本许可不授予 **CIVILIZATION** 名称、品牌标识或其他商标 / 品牌资产的使用权。

完整法律条款见 [LICENSE](./LICENSE)。更通俗的边界说明见 [COMMERCIAL_USE.md](./COMMERCIAL_USE.md)。

> CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/

## 当前版本

- Project Hub **v1.12**
- Brief Discovery Specialist **v1.28**
- Creative Exploration Specialist **v3.1**
- Product Innovation Specialist **v1.7**
- Proposal Development Specialist **v1.16**

更新通用 Skill 时，优先根据真实工作流测试抽象规则；**具体客户、品牌、人物、Campaign、产品和项目内容不写入通用 Skill**。
