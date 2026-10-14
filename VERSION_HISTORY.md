# VERSION HISTORY｜版本历史

这个仓库采用两层版本管理：

> **main = 当前最新版**  
> **Git Tags = 已确认正式版本的不可变历史快照**

仓库包含 1 个 Project Hub 与 4 个独立 Specialist，因此每个组件分别维护自己的版本号与 Tag；不要求五个组件同步升版。

## 当前版本

| Component | Current |
| --- | --- |
| Project Hub | `project-hub-v1.8` |
| Brief Discovery | `brief-discovery-v1.23` |
| Creative Exploration | `creative-exploration-v2.5` |
| Product Innovation | `product-innovation-v1.4` |
| Proposal Development | `proposal-development-v1.13` |

## 已归档的正式版本

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

## Tagging principle

只为**可以从 Git 历史明确验证的正式版本节点**建立 Tag。

因此：

- 不因为版本号中间有缺口就补造 Tag；
- 一个版本如果在升到下一版前还有同版本修订，Tag 指向该版本的最后稳定状态；
- 已存在的 Tag 不自动移动或覆盖；
- 新版本仍先更新 `main`，确认正式后再加入 Tag manifest。

Tag manifest：

> `.github/version-tags.tsv`

自动建 Tag workflow：

> `.github/workflows/version-tags.yml`

当 manifest 增加新版本时，GitHub Actions 会创建缺失 Tag；已经存在的 Tag 会跳过，不会改写历史。

## 为什么不用每个 Skill 版本都建 GitHub Release

GitHub Release 是**整个仓库**的发布对象，而这个仓库里的五个组件各自独立升版。

如果每次某一个 Skill 升版都创建一个仓库级 Release，会让 Release 历史误以为整个系统同时升级。

因此当前建议：

> **组件版本 → Git Tag**  
> **多个组件协同形成重要系统节点 → GitHub Release**

未来如果要做系统级 Release，可采用类似：

`system-2026-10-14`

或在形成更稳定的整体版本规则后采用统一 System Version。

## 回退与比较

需要查看历史版本时，可以：

1. 在 GitHub 的 Tags 中选择对应版本；
2. 查看该 Tag 下当时的完整仓库状态；
3. 用 GitHub Compare 比较两个 Tag；
4. 如需恢复旧版本，优先基于 Tag 新建分支，不移动旧 Tag。

> **Tag 是历史快照，不是可修改的“版本指针”。**
