# CIVILIZATION AI Specialists | Plugin package

> **看清真实市场，打破惯性思维。**

**Brief Discovery** independently understands market competition, consumer choice, and the brand's real position before diagnosing the client's Brief. **Creative Exploration** starts from the same real problem and evidence to invent distinctive solutions before validating them. The system supports clear professional judgment, not post-hoc justification.

This plugin is a **packaging layer only**. The canonical source of truth is the original repository main branch:

https://github.com/rogerwangzheng1027/civilization-ai-skills

The package contains exact Git blobs from the five original SKILL.md files, plus the original shared LANGUAGE_CONTROL.md, PROJECT_STATE_TEMPLATE.md, QUICK_START.md and LICENSE. **Do not independently edit packaged skill copies**. Always update the canonical files first, then refresh the package and verify that the Git blob SHAs match.

## Five skills

- `skills/project-hub/SKILL.md` — v1.11
- `skills/brief-discovery-specialist/SKILL.md` — v1.27
- `skills/creative-exploration-specialist/SKILL.md` — v3.0
- `skills/product-innovation-specialist/SKILL.md` — v1.6
- `skills/proposal-development-specialist/SKILL.md` — v1.15

Project Hub remains the single source for shared SOURCE × STATUS, Handoff, and version/update protocols. Every Specialist retains its own distinct methodology. The shared language rules are at `skills/LANGUAGE_CONTROL.md`, preserving original relative Markdown links.

## Personal installation

In ChatGPT open Plugin Creator and upload the latest ZIP from [GitHub Releases](https://github.com/rogerwangzheng1027/civilization-ai-skills/releases). Keep all five original SKILL.md files unchanged. No custom MCP server is required.

For repo-local ChatGPT Desktop/Codex use, the marketplace at `.agents/plugins/marketplace.json` points to `./plugins/civilization-ai-specialists`. Open that repository as a trusted project, refresh/restart, then install from the `CIVILIZATION Personal Plugins` marketplace if supported by your client.

**Updating**: Changes to canonical Skill files or shared source documents on main automatically sync exact original bytes, update this checked-in package snapshot, increment the Plugin package patch version and publish an immutable ZIP Release. Installed personal Plugins never automatically upgrade; explicit approval is required under the Project Hub VERSION / UPDATE PROTOCOL.

## Version verification

The package root contains `VERSION_MANIFEST.json`, generated from the actual canonical `SKILL.md` headers at release time.

Use it to answer:

> **What is actually installed in this Plugin package?**

Then cross-check against the five installed `SKILL.md` headers.

Do **not** infer installed versions from memory, README text, or conversation context.

Checking whether GitHub has a newer version is a separate operation. It requires actual access to the canonical GitHub `main` branch. If GitHub cannot be accessed, return:

> **VERSION CHECK: NOT AVAILABLE**

Never claim that GitHub was checked when it was not actually read.

`INSTALL_CHATGPT.md` in this package contains copy-ready prompts for both installed-version verification and remote-version verification.

## Source integrity (Git blob SHA)

```text
project-hub/SKILL.md                          3296ad45a7b0f99809a559e89001bf4b5ba8da63
project-hub/PROJECT_STATE_TEMPLATE.md         1051ba6be86923a5b602bbd5bc036738c8cba941
brief-discovery-specialist/SKILL.md           e54b9934e097a6757ebf5428c26801fe6a17bad6
creative-exploration-specialist/SKILL.md      f2f25b393faf5a9912dc9bec00b126529a00e8b7
product-innovation-specialist/SKILL.md        7ac0f58ba818638d7f55a6e3426316d1c49b8de1
proposal-development-specialist/SKILL.md      7c0d81ea4c8c3aae4f67c7b436e1d33611296cf0
LANGUAGE_CONTROL.md                           a0e8cf9f83947c33c59f2ec69954afc4f234bc29
QUICK_START.md                                7c1e2d85abd2ef2a61874dba0e612f912337eeca
INSTALL_CHATGPT.md                            6588a530ccc26581217f56d79805210ce388f798
LICENSE                                       baee873b679e36a4123c83b8a29e0fb17fad14eb
```
