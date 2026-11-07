# CIVILIZATION AI Specialists | Plugin package

> **看清真实市场，打破惯性思维。**

**Brief Discovery** independently understands market competition, consumer choice, and the brand's real position before diagnosing the client's Brief. **Creative Exploration** starts from the same real problem and evidence to invent distinctive solutions before validating them. The system supports clear professional judgment, not post-hoc justification.

This plugin is a **packaging layer only**. The canonical source of truth is the original repository main branch:

https://github.com/rogerwangzheng1027/civilization-ai-skills

The package contains exact Git blobs from the five original SKILL.md files, plus the original shared LANGUAGE_CONTROL.md, PROJECT_STATE_TEMPLATE.md, QUICK_START.md and LICENSE. **Do not independently edit packaged skill copies**. Always update the canonical files first, then refresh the package and verify that the Git blob SHAs match.

## Five skills

- `skills/project-hub/SKILL.md` — v1.12
- `skills/brief-discovery-specialist/SKILL.md` — v1.28
- `skills/creative-exploration-specialist/SKILL.md` — v3.1
- `skills/product-innovation-specialist/SKILL.md` — v1.7
- `skills/proposal-development-specialist/SKILL.md` — v1.16

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
project-hub/SKILL.md                          8a8b006e4c8144f7b64588ce675e2e4369fd2e17
project-hub/PROJECT_STATE_TEMPLATE.md         059917a36ed86350a1529e22094db0217c426cfd
brief-discovery-specialist/SKILL.md           3492bf8cc87803c640423bc3c530e3923fc72000
creative-exploration-specialist/SKILL.md      0913cf161b9b785ebe56c5978fb4f7685f29ecf5
product-innovation-specialist/SKILL.md        f1c3657b1eb8149f3a5802e585ecd553cad5ea9b
proposal-development-specialist/SKILL.md      192134914abd2c8f1a2f048fedb0af0fef344a79
LANGUAGE_CONTROL.md                           a0e8cf9f83947c33c59f2ec69954afc4f234bc29
QUICK_START.md                                7c1e2d85abd2ef2a61874dba0e612f912337eeca
INSTALL_CHATGPT.md                            6588a530ccc26581217f56d79805210ce388f798
LICENSE                                       baee873b679e36a4123c83b8a29e0fb17fad14eb
```
