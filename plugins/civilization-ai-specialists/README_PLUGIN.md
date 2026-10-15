# CIVILIZATION AI Specialists | Plugin package

This plugin is a **packaging layer only**. The canonical source of truth is the original repository main branch:

https://github.com/rogerwangzheng1027/civilization-ai-skills

The package contains exact Git blobs from the five original SKILL.md files, plus the original shared LANGUAGE_CONTROL.md, PROJECT_STATE_TEMPLATE.md, QUICK_START.md and LICENSE. **Do not independently edit packaged skill copies**. Always update the canonical files first, then refresh the package and verify that the Git blob SHAs match.

## Five skills

- `skills/project-hub/SKILL.md` — v1.9
- `skills/brief-discovery-specialist/SKILL.md` — v1.24
- `skills/creative-exploration-specialist/SKILL.md` — v2.5.1
- `skills/product-innovation-specialist/SKILL.md` — v1.4
- `skills/proposal-development-specialist/SKILL.md` — v1.14

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
project-hub/SKILL.md                          025575c884d0b850f84e77942ba58a49acc87c21
project-hub/PROJECT_STATE_TEMPLATE.md         1051ba6be86923a5b602bbd5bc036738c8cba941
brief-discovery-specialist/SKILL.md           f142607f55d0a80de3599432e482be95e855bf64
creative-exploration-specialist/SKILL.md      d881bdd0999a17a89ecca33803034d414b523b7f
product-innovation-specialist/SKILL.md        93eb011997b492e8926a1ba3ad94af5cd377c967
proposal-development-specialist/SKILL.md      f8d1c5eff57c320ed378f65edd4b7b39d323943d
LANGUAGE_CONTROL.md                           a0e8cf9f83947c33c59f2ec69954afc4f234bc29
QUICK_START.md                                f07a45fae0b2b6d971913c060eb804cb0dd9228a
INSTALL_CHATGPT.md                            6588a530ccc26581217f56d79805210ce388f798
LICENSE                                       baee873b679e36a4123c83b8a29e0fb17fad14eb
```
