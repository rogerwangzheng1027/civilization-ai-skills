# CIVILIZATION AI Specialists | Plugin package

This plugin is a **packaging layer only**. The canonical source of truth is the original repository main branch:

https://github.com/rogerwangzheng1027/civilization-ai-skills

The package contains exact Git blobs from the five original SKILL.md files, plus the original shared LANGUAGE_CONTROL.md, PROJECT_STATE_TEMPLATE.md, QUICK_START.md and LICENSE. **Do not independently edit packaged skill copies**. Always update the canonical files first, then refresh the package and verify that the Git blob SHAs match.

## Five skills

- `skills/project-hub/SKILL.md` — v1.10
- `skills/brief-discovery-specialist/SKILL.md` — v1.25
- `skills/creative-exploration-specialist/SKILL.md` — v2.6
- `skills/product-innovation-specialist/SKILL.md` — v1.5
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
project-hub/SKILL.md                          05fc52a73721dc64c736906eb29043867b9b977a
project-hub/PROJECT_STATE_TEMPLATE.md         1051ba6be86923a5b602bbd5bc036738c8cba941
brief-discovery-specialist/SKILL.md           27512ed6e669efac73cf037a4fc214063e3ca679
creative-exploration-specialist/SKILL.md      e6f2e4c6dadb36fe2a1cb4cf81626a8be6f91305
product-innovation-specialist/SKILL.md        e65f184c924e363ded14e56b77c25e165a9a8291
proposal-development-specialist/SKILL.md      7c0d81ea4c8c3aae4f67c7b436e1d33611296cf0
LANGUAGE_CONTROL.md                           a0e8cf9f83947c33c59f2ec69954afc4f234bc29
QUICK_START.md                                33c36f709b0b06314d1d17728f00a77980cdf6ed
INSTALL_CHATGPT.md                            6588a530ccc26581217f56d79805210ce388f798
LICENSE                                       baee873b679e36a4123c83b8a29e0fb17fad14eb
```
