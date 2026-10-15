# CIVILIZATION AI Specialists｜ChatGPT 个人安装

> 给同事的安装说明。**只需要下载一个正式 ZIP，再把它交给 ChatGPT 的 Plugin Creator。**
>
> 这是个人安装，不是打开 GitHub 链接就会自动安装。每个人需在自己的 ChatGPT 账号里操作，并且账号需要具有 Plugin Creator 使用权限。

## 1. 下载正式 ZIP（不要解压）

打开 [GitHub Releases](https://github.com/rogerwangzheng1027/civilization-ai-skills/releases)，选择最新的：

> `civilization-ai-specialists-vX.Y.Z`

在 Assets 中下载：

> `CIVILIZATION-AI-Specialists-vX.Y.Z.zip`

**不要使用仓库首页的 Code → Download ZIP。** 那是整个源码仓库，不是可直接安装的 Plugin ZIP。

## 2. 在 ChatGPT 里安装

打开 Plugin Creator，上传刚下载的 ZIP，并发送：

> 请从我上传的 ZIP 创建并安装一个**私有的个人 Plugin**，名称为 **CIVILIZATION AI Specialists**。保留插件中五份 SKILL.md 的完整原文和独立结构，包含 LANGUAGE_CONTROL.md、PROJECT_STATE_TEMPLATE.md、VERSION_MANIFEST.json 和 INSTALL_CHATGPT.md；不要合并 Skill，不要添加 MCP Server。安装后请直接读取 VERSION_MANIFEST.json 和五个 SKILL.md，报告实际安装的 Plugin 版本和五个 Skill 版本。若账户或权限不支持安装，请说明具体限制，不要报告虚假的安装成功。

根据 Plugin Creator 的确认提示完成安装。

## 3. 安装后必须做一次版本自检

不要只问：

> “我是不是最新版？”

模型可能根据旧对话、README 或记忆回答。

请复制下面这段：

> 请做一次 **CIVILIZATION AI Specialists 安装自检**。  
> 1. 先直接读取当前已安装 Plugin 根目录的 `VERSION_MANIFEST.json`。  
> 2. 再直接读取五个已安装 `SKILL.md` 的标题版本号做交叉验证。  
> 3. 报告 Plugin package version，以及 Project Hub、Brief Discovery、Creative Exploration、Product Innovation、Proposal Development 五个实际加载版本。  
> 4. 不要依据记忆、README、对话上下文或你认为的“最新版”推断。  
> 5. 如果你无法读取安装文件，请明确返回 **INSTALLED VERSION CHECK: NOT AVAILABLE**，不要猜。

### 以当前正式包为例

一个正常安装的正式包会同时满足：

- `VERSION_MANIFEST.json` 中的五个 Skill 版本；
- 五个实际 `SKILL.md` 的标题版本；
- Plugin package version；

三者互相一致。

**Plugin package version 与单个 Skill version 是两套版本号。**  
例如 Plugin 可能是 `v1.0.5`，而 Creative 仍然是 `v2.5.1`。

## 4. 要检查 GitHub 是否有更新，必须真的访问 GitHub

如果要检查远端最新版，请使用下面这段：

> 请实际访问 CIVILIZATION AI Specialists 的 canonical GitHub 仓库 main branch，并直接读取以下五个文件的标题版本号：  
> `project-hub/SKILL.md`  
> `brief-discovery-specialist/SKILL.md`  
> `creative-exploration-specialist/SKILL.md`  
> `product-innovation-specialist/SKILL.md`  
> `proposal-development-specialist/SKILL.md`  
> 同时读取最新 GitHub Release 的 Plugin package version。  
> **不要用当前已安装 Plugin、README、记忆或对话上下文代替 GitHub 实际读取。**  
> 如果当前环境不能访问 GitHub，请明确返回 **VERSION CHECK: NOT AVAILABLE**，不要声称“已核对 GitHub”。

### 两种版本检查不要混在一起

- **Installed Version Check**：我现在实际装了什么？
- **Remote Version Check**：GitHub 现在最新是什么？

只有两边都能真实读取，才能判断是否需要升级。

## 5. 安装后试用

- `请用 CIVILIZATION Project Hub 为一个新项目建立 Project State，只判断下一步应该找哪个 Specialist。`
- `请用 Brief Discovery Specialist 研究市场、竞争、消费者和品牌，再诊断我的 Brief。`
- `请用 Creative Exploration Specialist 调研真实案例，发展 Human Insight 和 Creative Spark，先筛选方向，不要马上拼完整 IMC。`
- `请用 Product Innovation Specialist 调研产品创新案例及结果证据，提出可测试的创新方向。`
- `请用 Proposal Development Specialist 把已确认的 Solution 发展成可以交付的完整提案。`

## 6. 更新已经安装的个人 Plugin

已安装的 Personal Plugin **不会因为 GitHub 发布新版而自动升级**。

正确更新方式：

1. 到 [GitHub Releases](https://github.com/rogerwangzheng1027/civilization-ai-skills/releases) 下载最新 ZIP；
2. 在 Plugin Creator 中选择**更新原来的 Plugin**，不要重新创建一个同名插件；
3. 查看版本差异；
4. 明确确认后升级；
5. 再运行一次“安装后版本自检”。

正在进行中的项目默认继续采用当前方法版本，除非团队决定切换。

## 7. 四个重要说明

1. **五个是一个 Plugin 里的五个独立 Skills。** Project Hub 管共享状态与 Handoff；四个 Specialist 保留各自专业方法。
2. **GitHub main 是 canonical source of truth。** Release ZIP 是一个不可变发布快照，不代表安装后自动同步 main。
3. **VERSION_MANIFEST.json 是安装包的机器可读版本清单。** 它用于验证“这个包里到底是什么版本”，不能代替远端 GitHub 检查。
4. **安装失败不必然是仓库问题。** 若找不到 Plugin Creator，通常需要检查本人 ChatGPT 账户是否提供此功能。暂时无法安装时，可分别提供五个原始 SKILL.md 给支持知识文件的 Project / Workspace；不要把五个 Skill 合并成超级 Prompt。

## 版本与维护

- [原始仓库](https://github.com/rogerwangzheng1027/civilization-ai-skills)
- [GitHub Releases](https://github.com/rogerwangzheng1027/civilization-ai-skills/releases)
- [Plugin 打包目录](https://github.com/rogerwangzheng1027/civilization-ai-skills/tree/main/plugins/civilization-ai-specialists)
- [Project Hub 版本协议](https://github.com/rogerwangzheng1027/civilization-ai-skills/blob/main/project-hub/SKILL.md)
- [历史版本与标签](https://github.com/rogerwangzheng1027/civilization-ai-skills/blob/main/VERSION_HISTORY.md)

**自动发布**：在 `main` 更新原始 Skill 或共享源文件后，GitHub Actions 会自动同步原文、生成 `VERSION_MANIFEST.json`、验证五个 Skill 的真实版本、递增 Plugin patch version，并发布新版 ZIP。

> **发布成功 ≠ 用户已升级。**  
> GitHub Release 是远端新版本；Personal Plugin 仍需要用户明确确认后更新。
