#!/usr/bin/env python3
"""Create a reproducible, skills-only ChatGPT Plugin ZIP.

Run: python3 scripts/build_plugin_distribution.py
Always compare the packaged skills against their canonical source files first.
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
    "LICENSE": "LICENSE",
}
SUPPORT = ["plugin.json", "README_PLUGIN.md"]
SKILL_DIRS = [
    "project-hub", "brief-discovery-specialist",
    "creative-exploration-specialist", "product-innovation-specialist",
    "proposal-development-specialist",
]


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def main() -> None:
    manifest = json.loads((PKG / "plugin.json").read_text(encoding="utf-8"))
    assert manifest["name"] == "civilization-ai-specialists"
    version = manifest["version"]
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise SystemExit("Plugin version must be MAJOR.MINOR.PATCH")

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

    print(f"BUILT {output}")
    print(f"VERSION {version}")
    print(f"SHA256 {hashlib.sha256(output.read_bytes()).hexdigest()}")
    for p, s in FILES.items():
        print(f"VERIFIED {p} == {s} ({git_blob_sha(payload[p])})")


if __name__ == "__main__":
    main()
