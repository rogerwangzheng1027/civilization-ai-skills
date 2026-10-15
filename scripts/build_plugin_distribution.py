#!/usr/bin/env python3
"""Create a reproducible, skills-only ChatGPT Plugin ZIP.

Run: python3 scripts/build_plugin_distribution.py
Always compare packaged skills against canonical source files and verify
VERSION_MANIFEST.json before producing the ZIP.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "plugins" / "civilization-ai-specialists"
FILES = {
    "skills/project-hub/SKILL.md": "project-hub/SKILL.md",
    "skills/project-hub/PROJECT_STATE_TEMPLATE.md": "project-hub/PROJECT_STATE_TEMPLATE.md",
    "skills/brief-discovery-specialist/SKILL.md": "brief-discovery-specialist/SKILL.md",
    "skills/creative-exploration-specialist/SKILL.md": "creative-exploration-specialist/SKILL.md",
    "skills/product-innovation-specialist/SKILL.md": "product-innovation-specialist/SKILL.md",
    "skills/proposal-development-specialist/SKILL.md": "proposal-development-specialist/SKILL.md",
    "skills/LANGUAGE_CONTROL.md": "LANGUAGE_CONTROL.md",
    "QUICK_START.md": "QUICK_START.md",
    "INSTALL_CHATGPT.md": "INSTALL_CHATGPT.md",
    "LICENSE": "LICENSE",
}
SUPPORT = ["plugin.json", "README_PLUGIN.md", "VERSION_MANIFEST.json"]
SKILL_DIRS = [
    "project-hub",
    "brief-discovery-specialist",
    "creative-exploration-specialist",
    "product-innovation-specialist",
    "proposal-development-specialist",
]
CANONICAL_SOURCE = "https://github.com/rogerwangzheng1027/civilization-ai-skills"
VERSION_RE = re.compile(r"^# CIVILIZATION[^\n]*?\bv(\d+(?:\.\d+)*)\s*$", re.MULTILINE)


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def canonical_skill_versions() -> dict[str, str]:
    versions: dict[str, str] = {}
    for slug in SKILL_DIRS:
        text = (ROOT / slug / "SKILL.md").read_text(encoding="utf-8")
        match = VERSION_RE.search(text)
        if not match:
            raise SystemExit("Skill header version missing: " + slug)
        versions[slug] = match.group(1)
    return versions


def validate_version_manifest(plugin_version: str) -> None:
    path = PKG / "VERSION_MANIFEST.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    expected_skills = canonical_skill_versions()

    if data.get("schema_version") != 1:
        raise SystemExit("VERSION_MANIFEST schema_version must be 1")
    if data.get("plugin") != "civilization-ai-specialists":
        raise SystemExit("VERSION_MANIFEST plugin identity mismatch")
    if data.get("plugin_version") != plugin_version:
        raise SystemExit(
            f"VERSION_MANIFEST plugin_version {data.get('plugin_version')} "
            f"!= plugin.json {plugin_version}"
        )
    if data.get("canonical_source") != CANONICAL_SOURCE:
        raise SystemExit("VERSION_MANIFEST canonical_source mismatch")
    if data.get("skills") != expected_skills:
        raise SystemExit(
            "VERSION_MANIFEST skill versions do not match canonical SKILL.md headers:\n"
            f"manifest={data.get('skills')}\ncanonical={expected_skills}"
        )
    if data.get("verification_rule") != (
        "Read VERSION_MANIFEST.json or the actual installed SKILL.md files. "
        "Never infer installed or GitHub versions from memory, README text, or conversation context."
    ):
        raise SystemExit("VERSION_MANIFEST verification_rule mismatch")


def main() -> None:
    manifest = json.loads((PKG / "plugin.json").read_text(encoding="utf-8"))
    assert manifest["name"] == "civilization-ai-specialists"
    version = manifest["version"]
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise SystemExit("Plugin version must be MAJOR.MINOR.PATCH")

    validate_version_manifest(version)

    payload: dict[str, bytes] = {}
    for destination, source in FILES.items():
        canonical = (ROOT / source).read_bytes()
        packaged = (PKG / destination).read_bytes()
        if canonical != packaged:
            raise SystemExit(
                f"SOURCE MISMATCH: {destination} != {source}\n"
                f"canonical Git blob {git_blob_sha(canonical)}; "
                f"package Git blob {git_blob_sha(packaged)}\n"
                "First refresh the package with the exact canonical original; "
                "review and bump package version before releasing."
            )
        payload[destination] = packaged

    for path in SUPPORT:
        payload[path] = (PKG / path).read_bytes()

    expected_skills = {f"skills/{name}/SKILL.md" for name in SKILL_DIRS}
    actual_skills = {path for path in payload if path.endswith("/SKILL.md")}
    if actual_skills != expected_skills:
        raise SystemExit(f"Skill inventory mismatch: {sorted(actual_skills)}")

    if "mcp.json" in payload:
        raise SystemExit("This distribution must not bundle an MCP server.")

    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    output = dist / f"CIVILIZATION-AI-Specialists-v{version}.zip"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path, raw in sorted(payload.items()):
            info = zipfile.ZipInfo(path, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, raw, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    with zipfile.ZipFile(output) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == set(payload)
        assert json.loads(z.read("plugin.json"))["name"] == manifest["name"]
        version_manifest = json.loads(z.read("VERSION_MANIFEST.json"))
        assert version_manifest["plugin_version"] == version

    print(f"BUILT {output}")
    print(f"VERSION {version}")
    print(f"SHA256 {hashlib.sha256(output.read_bytes()).hexdigest()}")
    print("VERSION_MANIFEST VERIFIED", json.dumps(canonical_skill_versions(), ensure_ascii=False))
    for p, s in FILES.items():
        print(f"VERIFIED {p} == {s} ({git_blob_sha(payload[p])})")


if __name__ == "__main__":
    main()
