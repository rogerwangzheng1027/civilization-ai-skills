# CIVILIZATION · AI 协作 Skills

> 把个人经验转化为团队可使用、可讨论、可持续迭代的工作方法。

这是一个源于 CIVILIZATION 内部实践、现公开供学习、教育、研究与非商业实践使用的 AI 协作工具库。

**AI 是顾问和共创伙伴，不是替团队做决定的领导，也不是代写作业的外包。**

> **Public Learning Edition / 公开学习版**  
> 本仓库公开的是可学习、可讨论、可持续迭代的通用方法与基础 Skill。CIVILIZATION 的客户案例、专有数据、内部评估机制及其他未公开实现细节不属于本公开仓库的一部分。

## 一个底层原则

> **一个 Skill 专门解决一个专业问题，并把它解决透；不追求大而全。**

共享协议可以统一，但不同工种不因为“复用方便”就塞进同一个超级 Prompt。

这也是当前结构从 1 Hub + 3 Coach 调整为 **1 Hub + 4 个专职 Coach** 的原因：传播创意与产品创新是两类任务、两类判断、两类交付，应由两个独立 Skill 承接。

## 当前工作流：1 Hub + 4 Specialist Coaches

| Skill | 当前版本 | 什么时候用 | 核心作用 |
| --- | --- | --- | --- |
| [Project Hub](./project-hub/SKILL.md) | v1.2 | 新项目、阶段切换、重要 Review 后 | 管理 `PROJECT_STATE.md`、共享证据协议、HOLD / DROP、Reopen 与交接；判断下一步进入哪个专职 Coach |
| [Brief Discovery Coach](./brief-discovery-coach/SKILL.md) | v1.18 | 刚收到 Brief、问题定义或关键前提不清楚 | 研究与拆 Brief，形成 Problem Landscape、Current Best Judgment、Strategy / Opportunity Territory |
| [Creative Exploration Coach](./creative-exploration-coach/SKILL.md) | v2.0 | 问题基本清楚，需要寻找传播创意解法 | 用真实跨界案例打开参考系，经 Human Spark / Follow the Spark / Selection 后，把 KEEP 的机制转译成具体 Idea |
| [Product Innovation Coach](./product-innovation-coach/SKILL.md) | v1.0 | 需要探索产品 / SKU / 配方 / 风味 / 功能 / 包装 / 规格等创新 | 用真实市场案例和可衡量结果筛选创新机制，形成可测试的产品创新方向与假设 |
| [Proposal Development Coach](./proposal-development-coach/SKILL.md) | v1.9 | 已有 Strategy / Idea / Innovation Direction，需要形成客户决策材料 | 用 Storyline 压力测试 Solution；只做受限 Repair，不从零补做上游发散 |

一句话记住：

> **Hub 管协议与交接；Brief 管问题；Creative 管传播 Idea；Innovation 管产品创新；Proposal 管成立、相信与决定。**

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

## 两个探索 Coach 为什么拆开

### Creative Exploration Coach v2.0

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
HUMAN SPARK
  ↓
FOLLOW THE SPARK
  ↓
SELECTION GATE: KEEP / HOLD / DROP
  ↓
IDEA TRANSLATION
  ↓
CREATIVE REVIEW
```

关键变化：

> **不是取消 Idea，而是推迟 Idea。**

ROUND 1 / ROUND 2 先让案例与人的联想打开空间；完成 Selection 后，ROUND 3 **必须**把 KEEP 的机制转译成具体 Idea。方向未筛选前，不自动拼成 IMC。

### Product Innovation Coach v1.0

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

市场证据强制拆成三件事：

> **RESULT SCOPE**：这个数字是谁的？SKU / PLATFORM / BRAND / CATEGORY  
> **EVIDENCE QUALITY**：证据有多强？A / B / C / D / E  
> **CAUSALITY CHECK**：结果多大程度能归因于该创新？

Product Innovation 不自动进入 Campaign / IMC。产品方向基本锁定、且明确需要传播探索时，再进入 Creative Exploration。

## 安装

### 支持 Skill 的 AI 工具

分别安装：

```text
project-hub/SKILL.md
brief-discovery-coach/SKILL.md
creative-exploration-coach/SKILL.md
product-innovation-coach/SKILL.md
proposal-development-coach/SKILL.md
```

**不要合并成一个超级 Prompt。**

### 不支持 Skill 安装的工具

把对应 `SKILL.md` 放进 Project / Workspace 的知识文件，或和项目材料一起上传，并明确说：

> 请严格按照我提供的 SKILL.md 工作。

共享项目状态模板：

[project-hub/PROJECT_STATE_TEMPLATE.md](./project-hub/PROJECT_STATE_TEMPLATE.md)

简短操作说明：

[QUICK_START.md](./QUICK_START.md)

## 五个 Skill 怎么开始

### 1. Project Hub

> 这是一个新项目。请建立 PROJECT_STATE.md，判断当前阶段，并告诉我下一步应该调用哪个 Coach。不要做专业分析。

### 2. Brief Discovery Coach

> 请按 Brief Discovery Coach 工作。先完整阅读材料并主动形成判断，不要先让我回答一堆问题。默认逐轮推进。

Brief 结束时应明确下一步属于：
- Creative Exploration
- Product Innovation
- 或其他专业环节

### 3. Creative Exploration Coach

> 请按 Creative Exploration Coach 开始 ROUND 1。先根据当前 Creative Problem 寻找跨界真实案例并拆机制，不要直接生成 Idea。案例之后停下来让我校准和补充联想。

ROUND 3 才把选中机制变成具体 Idea。

### 4. Product Innovation Coach

> 请按 Product Innovation Coach 开始 ROUND 1。寻找真实产品创新案例，优先验证市场结果，并区分 Result Scope、Evidence Quality 与 Causality。案例之后停下来让我校准。

ROUND 3 把选中机制变成可测试的产品创新方向，而不是传播方案。

### 5. Proposal Development Coach

> 请按 Proposal Development Coach 工作。先判断当前 Solution 和 Proposal 最大的问题，不要先整理 PPT。如果核心方向本身不成立，请触发对应 Reopen，不要在 Proposal 中从零造新 Idea。

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

证据统一使用 `SOURCE × STATUS`，不让 Working Hypothesis 在换 Agent / 换阶段后悄悄变成事实。

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
- **PDF / PPT 是按需交付，不是完成工作的指标。**
- **注意客户保密与素材权限。**

## 文件结构

```text
civilization-ai-skills/
├── README.md
├── QUICK_START.md
├── LICENSE
├── COMMERCIAL_USE.md
├── project-hub/
│   ├── SKILL.md
│   └── PROJECT_STATE_TEMPLATE.md
├── brief-discovery-coach/
│   └── SKILL.md
├── creative-exploration-coach/
│   └── SKILL.md
├── product-innovation-coach/
│   └── SKILL.md
└── proposal-development-coach/
    └── SKILL.md
```

## 协议同步规则

Project Hub 是共享协议唯一原文。

- Hub 修改共享标签、Handoff、Reopen、证据语言时，同步更新受影响 Coach。
- Coach 如要新增共享标签或交接字段，必须先或同时更新 Hub。
- 专业内部方法不写进 Hub，避免 Hub 变成超级 Skill。

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

- Project Hub **v1.2**
- Brief Discovery Coach **v1.18**
- Creative Exploration Coach **v2.0**
- Product Innovation Coach **v1.0**
- Proposal Development Coach **v1.9**

更新通用 Skill 时，优先根据真实工作流测试抽象规则；**具体客户、品牌、人物、Campaign、产品和项目内容不写入通用 Skill**。
