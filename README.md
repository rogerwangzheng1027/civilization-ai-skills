# CIVILIZATION · AI 协作 Skills

> 把个人经验转化为团队可使用、可讨论、可持续迭代的工作方法。

这是 CIVILIZATION 的内部 AI 协作工具库。目标不是让 AI 多生成，而是让它在关键阶段承担研究、挑战、创意刺激、判断与提案发展工作，让团队更早拥有可讨论、可验证、可继续推进的观点。

**AI 是顾问和共创伙伴，不是替团队做决定的领导，也不是代写作业的外包。**

## 当前工作流：1 个 Hub + 3 个 Coach

| Skill | 当前版本 | 什么时候用 | 核心作用 |
| --- | --- | --- | --- |
| [Project Hub](./project-hub/SKILL.md) | v1.1 | 新项目开始、阶段切换、重要 Review 后 | 建立 / 读取 `PROJECT_STATE.md`，管理项目状态、证据标签和交接，判断下一步调用哪个 Coach |
| [Brief Discovery Coach](./brief-discovery-coach/SKILL.md) | v1.17 | 刚收到 Brief、问题定义还不清楚、关键前提需要验证 | 研究与拆 Brief，形成 Problem Landscape、Current Best Judgment、Strategy / Opportunity Territory，为 Kickoff 准备判断 |
| [Creative Exploration Coach](./creative-exploration-coach/SKILL.md) | v1.8 | 问题基本清楚，希望通过跨界案例发现新的创意解法 | 以真实案例为主要刺激，拆可迁移机制，通过 Human Spark / Follow the Spark 继续探索，再用 KEEP / HOLD / DROP 筛选值得发展的方向 |
| [Proposal Development Coach](./proposal-development-coach/SKILL.md) | v1.8 | 已有 Strategy / Solution / Idea，希望压实逻辑并发展成 Proposal | 用 Storyline 压力测试 Solution；必要时做 Local Creative Repair；帮助客户理解、相信并作出决定 |

一句话记住：

> **Hub 管状态与交接；Brief 管问题；Creative 管新的可能性与筛选；Proposal 管成立、相信与决定。**

## 最常见的项目流程

```text
Project Hub
  ↓ 建立 / 读取 PROJECT_STATE.md
Brief Discovery Coach
  ↓ 更新问题定义、判断、证据与方向
核心团队 Kickoff
  ↓
Creative Exploration Coach
  ↓ 案例刺激 → 人的联想 → 二次探索 → 方向筛选
Proposal Development Coach
  ↓ Solution 压力测试 / Local Repair / Storyline
客户 Review
  ↓
Project Hub
  ↓ 判断 KEEP / REPAIR / CREATIVE REOPEN / BRIEF REOPEN
```

### Review 后怎么判断

- **KEEP**：Solution 成立，只需继续发展 Storyline、Evidence、表达与执行。
- **REPAIR**：Strategy Territory / Idea Family 基本成立，但 Human Motivation、Creative Leap、Brand Action、Engagement Mechanic、Idea Bridge 等局部连接缺失；留在 Proposal 做 Local Creative Repair。
- **CREATIVE REOPEN**：需要重新打开明显不同的创意可能性；回 Creative Exploration。
- **BRIEF REOPEN**：新信息改变客户目标、真问题、关键前提或 Strategy Territory；回 Brief Discovery。

## 安装

### 支持 Skill 的 AI 工具

分别安装四个 `SKILL.md`：

```text
project-hub/SKILL.md
brief-discovery-coach/SKILL.md
creative-exploration-coach/SKILL.md
proposal-development-coach/SKILL.md
```

不要把四个 Skill 合并成一个超级 Prompt。它们承担不同阶段的判断职责。

### 不支持 Skill 安装的工具

把对应 `SKILL.md` 放进 Project / Workspace 的知识文件，或在对话中与项目材料一起上传，并明确说：

> 请严格按照我提供的 SKILL.md 工作。

`PROJECT_STATE.md` 是跨 Skill / 跨 Agent 的共享项目记忆。模板见：

[project-hub/PROJECT_STATE_TEMPLATE.md](./project-hub/PROJECT_STATE_TEMPLATE.md)

更简短的操作说明见：

[QUICK_START.md](./QUICK_START.md)

## 四个 Skill 怎么开始

### 1. Project Hub

新项目可直接说：

> 这是一个新项目。请建立 PROJECT_STATE.md，判断当前阶段，并告诉我下一步应该调用哪个 Coach。不要做策略分析。

Hub 只管理状态与交接，不替代三个 Coach 做分析。

### 2. Brief Discovery Coach

上传客户 Brief、会议纪要、已有研究与 `PROJECT_STATE.md`，可说：

> 请按 Brief Discovery Coach 工作。先完整阅读材料并主动形成判断，不要先让我回答一堆问题。默认逐轮推进；如果我明确要求，也可以一次跑完。

### 3. Creative Exploration Coach

Creative v1.8 的核心流程是：

```text
CASE LANDSCAPE
  ↓
HUMAN SPARK
  ↓
FOLLOW THE SPARK
  ↓
SELECTION GATE: KEEP / HOLD / DROP
  ↓
SELECT & TRANSLATE
```

它不再默认“搜完案例就直接生成完整 Campaign”。ROUND 1 先用跨界真实案例打开新的参考系，拆 `真实行为 / 成立条件 / 不可迁移条件 / 可迁移机制`；然后必须停下，让人的联想决定第二轮探索。方向未筛选前，不自动拼成 IMC。

可直接说：

> 请按 Creative Exploration Coach 开始 ROUND 1。先根据当前 Creative Problem 寻找跨界真实案例并拆行为机制，不要直接生成 Idea。案例之后停下来让我校准和补充联想。

### 4. Proposal Development Coach

当已经有值得发展的 Strategy / Solution / Idea 时，可说：

> 请按 Proposal Development Coach 工作。先判断当前 Solution 和 Proposal 最大的问题，不要先整理 PPT。如果故事讲不通，请先判断 KEEP / REPAIR / CREATIVE REOPEN / BRIEF REOPEN。

## `PROJECT_STATE.md` 是工作流的共享记忆

它应该记录当前最重要的判断，而不是变成一份长报告：

- CLIENT ASK
- CURRENT PROBLEM DEFINITION
- CURRENT BEST JUDGMENT + reason + what would change my mind
- LOCKED
- LIVE HYPOTHESES
- SELECTED DIRECTIONS
- HOLD / DROPPED / SUPERSEDED
- REVIEW CHANGES
- OPEN QUESTIONS / DECISION BLOCKERS
- EVIDENCE NOTES
- NEXT HANDOFF

证据统一使用 `SOURCE × STATUS` 双轴，不让工作假设在换 Agent / 换阶段后悄悄升级成事实。

## 协作原则

- **AI 先做实质工作，人负责判断和纠偏。** 不把工作流变成员工填问卷。
- **真实案例是 Creative Exploration 的刺激，不是模板。** 重点拆为什么成立、哪些条件不可迁移、真正可带走的机制是什么。
- **先选择，再体系化。** `Systemization is downstream of selection.` 不要因为多个方向各有一点价值，就自动把它们安排成 Content / Social / Media / Activation 一整套。
- **Storyline 是诊断工具，不只是排版工具。** Proposal 讲不通时，先检查 Solution 是否缺了一环。
- **PDF / PPT 是按需交付形式，不是完成工作的指标。**
- **注意客户保密与素材权限。** 未获批准的 Brief、报价、用户数据、真实项目案例等，不放入本仓库或未经授权的平台。

## 文件结构

```text
civilization-ai-skills/
├── README.md
├── QUICK_START.md
├── project-hub/
│   ├── SKILL.md
│   └── PROJECT_STATE_TEMPLATE.md
├── brief-discovery-coach/
│   └── SKILL.md
├── creative-exploration-coach/
│   └── SKILL.md
└── proposal-development-coach/
    └── SKILL.md
```

## 当前版本

- Project Hub **v1.1**
- Brief Discovery Coach **v1.17**
- Creative Exploration Coach **v1.8**
- Proposal Development Coach **v1.8**

更新通用 Skill 时，优先根据真实工作流测试抽象方法规则；**具体客户、品牌、人物、Campaign、产品和项目内容不写入通用 Skill**。
