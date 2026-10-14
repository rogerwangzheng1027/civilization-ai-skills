# CIVILIZATION · AI Specialists

> **AI 专家协作系统**  
> *A human-led AI specialist workflow for professional collaboration.*

这是一套源于 CIVILIZATION 内部实践的 AI 协作方法，由 **1 个 Project Hub + 4 个专业 Specialist** 组成，帮助团队先研究市场与品牌现实、理解客户真正的商业动机，再拆解 Brief、探索创意、寻找产品创新机会，并发展完整提案。

它不是让 AI 替人交作业，而是让 AI 成为研究、思考、探索和推进问题的专业协作伙伴。

> **AI 先做实质工作，人负责判断和纠偏。**

### 1 Hub + 4 Specialists

- **Project Hub**｜我现在在哪里，下一步该找谁？
- **Brief Discovery**｜市场与消费者正在发生什么？客户为什么提出这道题？真正的问题在哪里？
- **Creative Exploration**｜还有什么我们没有想到？
- **Product Innovation**｜产品本身还能怎么变？
- **Proposal Development**｜怎么把已有 Solution 发展成一份完整提案？

> **Public Learning Edition / 公开学习版**  
> 本仓库公开的是可学习、可讨论、可持续迭代的通用方法与基础 Skill。CIVILIZATION 的客户案例、专有数据、内部评估机制及其他未公开实现细节不属于本公开仓库的一部分。

## 一个底层原则

> **一个 Skill 专门解决一个专业问题，并把它解决透；不追求大而全。**

共享协议可以统一，但不同工种不因为“复用方便”就塞进同一个超级 Prompt。

这也是当前结构从原先三个专业 Skill 调整为 **1 Hub + 4 个专业 Specialist** 的原因：传播创意与产品创新是两类任务、两类判断、两类交付，应由两个独立 Skill 承接。

## 当前工作流：1 Hub + 4 Specialists

| Skill | 当前版本 | 什么时候用 | 核心作用 |
| --- | --- | --- | --- |
| [Project Hub](./project-hub/SKILL.md) | v1.7 | 新项目、阶段切换、重要 Review 后 | 管理项目状态、共享协议与交接；判断当前在哪里、下一步该找哪个专业 Specialist |
| [Brief Discovery Specialist](./brief-discovery-specialist/SKILL.md) | v1.23 | 刚收到 Brief、问题定义或关键前提不清楚 | **先研究市场、竞争、用户行为与品牌资产**；再理解客户目标和提出 Brief 的动机；最后诊断现实与客户期待的落差，形成有证据的解题判断与机会方向 |
| [Creative Exploration Specialist](./creative-exploration-specialist/SKILL.md) | v2.5 | 问题基本清楚，需要寻找传播创意解法，或已有 Idea Seed 需要继续做强 | 用真实跨界案例打开参考系，筛选并发展 Idea；选中后先做 Concept Development，再进入 Execution / IMC |
| [Product Innovation Specialist](./product-innovation-specialist/SKILL.md) | v1.3 | 需要探索产品 / SKU / 配方 / 风味 / 功能 / 包装 / 规格等创新 | 用真实市场案例和可衡量结果筛选创新机制，形成可测试的产品创新方向与假设 |
| [Proposal Development Specialist](./proposal-development-specialist/SKILL.md) | v1.13 | 已有 Strategy / Idea / Innovation Direction，需要形成完整提案文件 | 用 Storyline 压力测试并发展 Solution，形成 Proposal Spine、Page Plan、关键文案与可直接进入 PPT / PDF 的提案内容 |

一句话记住：

> **Hub 管导航与交接；Brief 管问题和 Brand Logic；Creative 管 Human Insight、Creative Spark 与传播 Idea；Innovation 管产品创新；Proposal 管提案文件的发展与成稿。**

## Brief Discovery v1.23：先理解现实，再理解 Brief

**不要先用客户的 Brief 定义市场，再回头寻找能证明它的资料。** 新版要求 AI 在评价 Brief 前，先建立相对独立的外部现实基准，然后才理解客户需求及其背后的商业动机。

```text
OUTSIDE-IN RESEARCH｜研究市场发展、竞争趋势、用户行为和品牌资产
    ↓
CLIENT INTENT｜理解客户真正的目标、提出 Brief 的原因与约束
    ↓
REALITY × INTENT GAP｜对照客户预期与现实，发现关键落差
    ↓
STRATEGIC JUDGMENT｜形成 Problem Landscape 与有证据边界的 Strategy / Opportunity Territory
```

三个 ROUND 保留，**AI先主动研究，用户只在关键判断处校准**。外部研究的四个视角是必做的基础功课，但研究深度按项目需要调整；不会要求每个项目都做行业白皮书。

品牌主张、产品计划、目标用户或沟通方向等 **只在客户实际提出、且对决策重要时** 才进行 Gap Diagnosis。不会假设每个 Brief 都有既定定位，也不会机械要求每个项目检查未来12个月的产品规划。深度品牌考古、医学或技术研究同样按实际问题触发，不是固定清单。

新版明确要求，在进入 Strategy Selection 前回答：**外部研究究竟让我们发现了什么，改变了什么判断？** 没有新发现时继续查证最重要的盲区，或诚实保留证据缺口；不为“有洞察”制造结论。

如果任务本身就是 Brand Restage / Repositioning / Brand Platform / Proposition，Brief 不再因为客户没有现成定位就跳过品牌逻辑。它会按需形成一条 **Brand Logic Bridge**：

```text
Human Spark
  ↓
Brand Belief
  ↓
Brand Role
  ↓
Product / Offering Truth
  ↓
Competitive Contrast
  ↓
Positioning Difference
```

Human Spark 是对真实 human tension 的策略综合，不是假装成消费者原话；Brand Belief 也不是 Human Insight。

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

### Creative Exploration Specialist v2.5

专门研究：
- Campaign / Communication
- Social / Creator
- Activation / Experience
- Content / Media
- Brand behavior / Engagement mechanic

核心流程：

```text
CASE LANDSCAPE
  ↓
SPARK CALIBRATION
  ↓
HUMAN INSIGHT → CREATIVE SPARK
  ↓
FOLLOW THE SPARK
  ↓
SELECTION GATE: KEEP / HOLD / DROP
  ↓
IDEA TRANSLATION
  ↓
CONCEPT DEVELOPMENT
  ↓
CREATIVE REVIEW
```

关键变化：

> **不是取消 Idea，而是推迟 Idea。**

ROUND 1 先用案例打开空间，用户做 Spark Calibration；ROUND 2 不只是继续找案例，而要把研究推进到更具体的 **Human Insight → Creative Spark**。Creative Spark 是「这里可能有件值得做的事」，还不是 Idea。**正式案例必须同时带真实执行视觉 + 可追溯来源链接**，缺图或缺链接的案例只进入 TO SOURCE / BACKUP。

Selection Gate 保留三个 Viability Checkpoints，但它们是检查点，不是三道必须全部清零的拦截门。证据仍是 AMBER 时可以条件性继续；只有方向建立在虚假事实、不可获得资源、明显法规风险或品牌根本接不住的前提上，才真正停止。用户只说「继续」时，AI 应给出推荐判断并在没有明确否决项时继续往下，不把用户困在无限研究循环里。

完成 Selection 后，ROUND 3 对 KEEP 或条件性推进的方向先形成**参与结构 / 品牌动作真正不同的候选 Idea**。选中 Idea Seed 后进入 **Concept Development**：先把 Human Truth、Brand Right、Task / Moment Role、Concept Meaning、Expression System 与 Creative Requirements 做强；已有角色、联名、包装、活动等只作为 Execution Hypotheses，不因已经具体就自动向下发展。只有 Concept Ready 后才进入完整 Execution / IMC。

### Product Innovation Specialist v1.3

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
HUMAN SPARK
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

## 安装

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

> 请按 Brief Discovery Specialist v1.23 工作。先根据项目范围独立研究市场发展、竞争趋势、消费者行为及品牌背景与资产；再完整阅读 Brief、会议材料，理解客户真正的需求和提出这道题的动机；最后分析与现实的关键落差，形成有证据的判断。不要先让我回答一堆问题，默认逐轮推进。

Brief 结束时应明确下一步属于：
- Creative Exploration
- Product Innovation
- 或其他专业环节

### 3. Creative Exploration Specialist

> 请按 Creative Exploration Specialist v2.5 开始 ROUND 1。先根据当前 Creative Problem 寻找跨界真实案例并拆机制，不要直接生成 Idea。案例之后停下来做 Spark Calibration；下一轮继续找 Human Insight 和 Creative Spark，再进入 Selection。

ROUND 3 把选中机制变成具体 Idea Seed；如果已经有 KEEP 的 Idea 雏形，也可以直接进入 Concept Development，先优化 Concept，再决定是否发展 Execution / IMC。

### 4. Product Innovation Specialist

> 请按 Product Innovation Specialist 开始 ROUND 1。寻找真实产品创新案例，优先验证市场结果，并区分 Result Scope、Evidence Quality 与 Causality。案例之后停下来让我校准。

ROUND 3 把选中机制变成可测试的产品创新方向，而不是传播方案。

### 5. Proposal Development Specialist

> 请按 Proposal Development Specialist v1.13 工作。基于已确认的 Strategy / Idea / Innovation Direction，先检查 Solution 是否足以支撑提案，再形成 Proposal Spine、Storyline、Page Plan 和关键文案，最终发展成完整提案文件。如果核心方向本身不成立，再触发对应 Reopen。客户可见文字要讲人话，内部框架不要原样倒给客户。

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
- **底层判断可以很严谨，表面语言不要很费劲。** Brief / Creative / Proposal 的用户可见文字共同参考 [LANGUAGE_CONTROL.md](./LANGUAGE_CONTROL.md)，其中吸收了 Khazix Writer 的去 AI 化、自然语言化原则。
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

版本检查规则统一定义在 **Project Hub v1.7 的 VERSION / UPDATE PROTOCOL**。四个 Specialist 只继承，不重复维护。

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

- Project Hub **v1.7**
- Brief Discovery Specialist **v1.23**
- Creative Exploration Specialist **v2.5**
- Product Innovation Specialist **v1.3**
- Proposal Development Specialist **v1.13**

更新通用 Skill 时，优先根据真实工作流测试抽象规则；**具体客户、品牌、人物、Campaign、产品和项目内容不写入通用 Skill**。
