# CIVILIZATION AI Specialists｜ChatGPT 个人安装

> 给同事的安装说明。**只需要下载一个 ZIP，再把它交给 ChatGPT 的 Plugin Creator。**
>
> 这是两步安装，不是打开网页就会自动安装。每个人需在自己的 ChatGPT 账号里操作；需要具有 Plugin Creator 使用权限。

## 1. 下载独立的正式 ZIP（不要解压）

**当前固定版本：v1.0.0**

[下载 CIVILIZATION AI Specialists v1.0.0 插件 ZIP](https://github.com/rogerwangzheng1027/civilization-ai-skills/releases/download/civilization-ai-specialists-v1.0.0/CIVILIZATION-AI-Specialists-v1.0.0.zip)

若直链不可用，请先访问 [GitHub Releases](https://github.com/rogerwangzheng1027/civilization-ai-skills/releases) 查看发布状态。**不要误用仓库首页的 Code → Download ZIP**：那是整个源代码仓库，不是可直接安装的单插件 ZIP。

## 2. 在 ChatGPT 里安装

打开 ChatGPT，进入 Plugin Creator（在已开放 Plugin Creator 的账号中通过 Plugins 或 @Plugin Creator 打开），**上传刚下载的 ZIP**，发送下面这一句话：

> 请从我上传的 ZIP 创建并安装一个**私有的个人 Plugin**，名称为 **CIVILIZATION AI Specialists**。保留插件中五份 SKILL.md 的完整原文和独立结构，包含 LANGUAGE_CONTROL.md 与 PROJECT_STATE_TEMPLATE.md，不要合并 Skill，不要添加 MCP Server。安装后请列出五个 Skill，确认可以独立调用。若账户或权限不支持安装，请说明具体限制，不要报告虚假的安装成功。

根据 Plugin Creator 的确认提示完成个人安装。

## 3. 安装后试用

- `请用 CIVILIZATION Project Hub 为一个新项目建立 Project State，只判断下一步应该找哪个 Specialist。`
- `请用 Brief Discovery Specialist 研究市场、竞争、消费者和品牌，再诊断我的 Brief。`
- `请用 Creative Exploration Specialist 调研真实案例，发展 Human Insight 和 Creative Spark，先筛选方向，不要马上拼完整 IMC。`
- `请用 Product Innovation Specialist 调研产品创新案例及结果证据，提出可测试的创新方向。`
- `请用 Proposal Development Specialist 把已确认的 Solution 发展成可以交付的完整提案。`

## 四个重要说明

1. **五个是一个插件里的五个独立 Skills**。Project Hub 管共享状态与 Handoff；四个 Specialist 保留各自专业方法。
2. **Skill 原文以 GitHub main 分支为 source of truth**。ZIP 是固定发布快照，绝不意味着安装后自动同步 main。
3. **更新必须先提示版本差异、得到用户确认，再做替换**。正在使用的项目默认继续采用当前版本。具体遵循 Project Hub 的 VERSION / UPDATE PROTOCOL。
4. **安装失败并不必然是仓库问题**。若找不到 Plugin Creator，通常需要检查本人 ChatGPT 账户是否提供此功能。暂时无法安装时，可在支持知识文件的项目中分别提供五个原始 SKILL.md，并明确指示按原文工作。不要把五个 Skill 合并成超级 Prompt。

## 版本与维护

- [原始仓库](https://github.com/rogerwangzheng1027/civilization-ai-skills)
- [Plugin 打包目录](https://github.com/rogerwangzheng1027/civilization-ai-skills/tree/main/plugins/civilization-ai-specialists)
- [Project Hub 版本协议](https://github.com/rogerwangzheng1027/civilization-ai-skills/blob/main/project-hub/SKILL.md)
- [历史版本与标签](https://github.com/rogerwangzheng1027/civilization-ai-skills/blob/main/VERSION_HISTORY.md)

维护者发布新版本时：先更新原始 SKILL.md，再同步其原文到打包目录；运行 `python3 scripts/build_plugin_distribution.py` 校验，升级 `plugin.json` 的版本号，然后手动触发 GitHub Actions 的 `Publish Personal Plugin ZIP`。旧版本 ZIP 保留，不会被覆盖。
