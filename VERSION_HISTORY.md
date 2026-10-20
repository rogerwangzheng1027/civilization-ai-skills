# VERSION HISTORY｜版本历史

这个仓库现在采用三层版本管理：

> **main = 当前最新版**  
> **System Release Tags = 可安装、可回退的完整系统快照**  
> **Component Tags = 早期与关键单项 Skill 版本的历史快照**

仓库包含 1 个 Project Hub 与 4 个独立 Specialist，各组件仍分别维护自己的方法版本号；完整安装包则由 Personal Plugin Release 自动保存为系统版本。

## 当前版本

| Component | Current |
| --- | --- |
| Project Hub | v1.10 |
| Brief Discovery | v1.25 |
| Creative Exploration | v2.6 |
| Product Innovation | v1.5 |
| Proposal Development | v1.15 |

当前完整系统快照：

> **`civilization-ai-specialists-v1.0.9`**

该 Release 已包含以上五个当前 Skill 版本，可用于安装、比较和整体回退。

**v1.0.9 / Creative v2.6**：定向升级案例研究能力。新增 Explore / Research Atlas 两种入口、Coverage Gap Audit、Brand Job → Consumer Value / Mechanism Dependency 深拆，以及正式 Casebook 的真实图片嵌入和离线文件 QA。**不引入候选案例固定三级分类**；保持 Human Insight → Creative Spark → Selection → Concept Development 原有方法不变。v1.0.7–v1.0.8 为本轮文档及 Skill 同步过程的历史快照。

**此前 v1.0.6**：升级 Growth Diagnosis / DATA CONTRACT、Product Deconstruction、Consumer Value Expansion、Product vs Concept vs Expression Option、功能成分与宣称预检、概念测试设计，以及 Hub 的局部任务入口和 Proposal 的 Evidence Trace / Artifact QA。

从 `v1.0.5` 起，Plugin 包新增 `VERSION_MANIFEST.json` 与安装后版本自检：安装版本与 GitHub 远端版本必须分开验证；无法实际读取 GitHub 时必须返回 `VERSION CHECK: NOT AVAILABLE`，不得根据旧对话、README 或记忆推断。

## 已归档的 Component Tags

### Project Hub

`project-hub-v1.1`  
`project-hub-v1.2`  
`project-hub-v1.3`  
`project-hub-v1.4`  
`project-hub-v1.5`  
`project-hub-v1.6`  
`project-hub-v1.7`  
`project-hub-v1.8`

### Brief Discovery

`brief-discovery-v1.14`  
`brief-discovery-v1.17`  
`brief-discovery-v1.18`  
`brief-discovery-v1.19`  
`brief-discovery-v1.20`  
`brief-discovery-v1.22`  
`brief-discovery-v1.23`

### Creative Exploration

`creative-exploration-v1.4`  
`creative-exploration-v1.8`  
`creative-exploration-v1.9`  
`creative-exploration-v1.9.1`  
`creative-exploration-v2.0`  
`creative-exploration-v2.1`  
`creative-exploration-v2.2`  
`creative-exploration-v2.3`  
`creative-exploration-v2.4`  
`creative-exploration-v2.5`

### Product Innovation

`product-innovation-v1.0`  
`product-innovation-v1.1`  
`product-innovation-v1.2`  
`product-innovation-v1.3`  
`product-innovation-v1.4`

### Proposal Development

`proposal-development-v1.8`  
`proposal-development-v1.9`  
`proposal-development-v1.10`  
`proposal-development-v1.11`  
`proposal-development-v1.12`  
`proposal-development-v1.13`

## System Releases

从 Personal Plugin Distribution 建立后，完整系统版本由自动 Release 保存：

> `civilization-ai-specialists-v1.0.x`

系统 Release 同时保存：
- 五个 canonical `SKILL.md` 的同步快照；
- Plugin package；
- 可下载 ZIP；
- 对应 source / snapshot commit。

因此后续不要求每次单个 Skill 升版都再创建一个 Component Tag；**完整系统回退优先使用 System Release Tag。**

## Tagging principle

历史 Component Tags 只保留**可以从 Git 历史明确验证的正式版本节点**：

- 不因为版本号中间有缺口就补造 Tag；
- 已存在的 Tag 不移动、不覆盖；
- 历史映射保留在 `.github/version-tags.tsv`。

未来的稳定回退点以 **System Release Tag** 为主，由 Personal Plugin Release workflow 自动生成。

## Plugin 安装包的单独版本

ChatGPT Plugin ZIP 使用独立版本 `civilization-ai-specialists-vX.Y.Z`。原始五个 Skill 或共享源文件在 `main` 更新后，GitHub Actions 自动校验、同步原文并发布新的 ZIP。这个分发版本**不等于**各 Skill 的专业方法版本，旧版 ZIP 保留，已经安装的个人 Plugin 需要使用者确认后更新。

## Component Version 与 System Release 的关系

组件版本用于说明某一个 Skill 的方法演进；System Release 用于保存一次可安装、可回退的完整组合。

> **Component Version = 方法版本**  
> **System Release = 分发与整体回退版本**

两者不要求同步升版。

## 回退与比较

需要查看历史版本时，可以：

1. 在 GitHub 的 Tags 中选择对应版本；
2. 查看该 Tag 下当时的完整仓库状态；
3. 用 GitHub Compare 比较两个 Tag；
4. 如需恢复旧版本，优先基于 Tag 新建分支，不移动旧 Tag。

> **Tag 是历史快照，不是可修改的“版本指针”。**
