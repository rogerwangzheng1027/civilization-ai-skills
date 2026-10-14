# CIVILIZATION AI Specialists | Plugin package

This plugin is a **packaging layer only**. The canonical source of truth is the original repository main branch:

https://github.com/rogerwangzheng1027/civilization-ai-skills

The package contains exact Git blobs from the five original SKILL.md files, plus the original shared LANGUAGE_CONTROL.md, PROJECT_STATE_TEMPLATE.md, QUICK_START.md and LICENSE. **Do not independently edit packaged skill copies**. Always update the canonical files first, then refresh the package and verify that the Git blob SHAs match.

## Five skills

- `skills/project-hub/SKILL.md` — v1.8
- `skills/brief-discovery-specialist/SKILL.md` — v1.23
- `skills/creative-exploration-specialist/SKILL.md` — v2.5
- `skills/product-innovation-specialist/SKILL.md` — v1.4
- `skills/proposal-development-specialist/SKILL.md` — v1.13

Project Hub remains the single source for shared SOURCE × STATUS, Handoff, and version/update protocols. Every Specialist retains its own distinct methodology. The shared language rules are at `skills/LANGUAGE_CONTROL.md`, preserving original relative Markdown links.

## Personal installation

In ChatGPT install Plugin Creator, invoke `@plugin-creator` in Work mode, and ask it to install a personal skills-only plugin from this folder, keeping all five original SKILL.md files unchanged. No custom MCP server is required.

For repo-local ChatGPT Desktop/Codex use, the marketplace at `.agents/plugins/marketplace.json` points to `./plugins/civilization-ai-specialists`. Open that repository as a trusted project, refresh/restart, then install from the `CIVILIZATION Personal Plugins` marketplace if supported by your client.

**Updating**: The content here is a Git snapshot, **not** a live auto-sync with main. Repackage after source changes. Follow the Project Hub's VERSION / UPDATE PROTOCOL, including explicit consent before replacing an in-use skill.

## Source integrity (Git blob SHA)

```text
project-hub/SKILL.md                 f510b475dd75aa4b24f0834f1d21a7b9c7e40d84
brief-discovery-specialist/SKILL.md 1032ac4ff2363ba8b1d5f6567073e3d95be56f1b
creative-exploration-specialist/SKILL.md 23ec8c86d41f4cda835efc7b17e8e843c7cf4aac
product-innovation-specialist/SKILL.md 93eb011997b492e8926a1ba3ad94af5cd377c967
proposal-development-specialist/SKILL.md 59477177654f34538f0b3835f290f5b5f517b831
LANGUAGE_CONTROL.md                  a0e8cf9f83947c33c59f2ec69954afc4f234bc29
project-hub/PROJECT_STATE_TEMPLATE.md d21ecc1181cafb9edcefd84057609dc4dd0b1fa1
```
