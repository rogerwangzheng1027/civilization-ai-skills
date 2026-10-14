#!/usr/bin/env python3
"""Synchronize canonical Skills to the Plugin's checked-in distribution snapshot.

Usage: python3 scripts/sync_plugin_sources.py 1.0.3
Never writes to the five original SKILL.md source files.
"""
from __future__ import annotations

import hashlib
import json
import re
import runpy
import shutil
import sys
from pathlib import Path

if len(sys.argv) != 2 or not re.fullmatch(r"\d+\.\d+\.\d+", sys.argv[1]):
    raise SystemExit("Usage: python3 scripts/sync_plugin_sources.py MAJOR.MINOR.PATCH")
version = sys.argv[1]
root = Path(__file__).resolve().parents[1]
pkg = root / "plugins" / "civilization-ai-specialists"
settings = runpy.run_path(str(root / "scripts" / "build_plugin_distribution.py"), run_name="plugin_sync_only")
files = settings["FILES"]
slugs = settings["SKILL_DIRS"]

for destination, source in files.items():
    target = pkg / destination
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(root / source, target)

manifest_path = pkg / "plugin.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
if manifest.get("name") != "civilization-ai-specialists":
    raise SystemExit("Unexpected plugin identity; refusing to continue")
manifest["version"] = version
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

readme_path = pkg / "README_PLUGIN.md"
doc = readme_path.read_text(encoding="utf-8")
lines = doc.splitlines()
for slug in slugs:
    original = (root / slug / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"^# CIVILIZATION[^\n]*?\bv(\d+(?:\.\d+)*)\s*$", original, re.MULTILINE)
    if not match:
        raise SystemExit("Skill header version missing: " + slug)
    prefix = "- " + chr(96) + "skills/" + slug + "/SKILL.md" + chr(96) + " — v"
    matching = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(matching) != 1:
        raise SystemExit("README version line invalid: " + slug)
    lines[matching[0]] = prefix + match.group(1)

heading = "## Source integrity (Git blob SHA)"
text = "\n".join(lines) + "\n"
if text.count(heading) != 1:
    raise SystemExit("README source integrity section invalid")
prefix = text.split(heading, 1)[0]
shas = []
for source in files.values():
    raw = (root / source).read_bytes()
    sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    shas.append(f"{source:<45} {sha}")
readme_path.write_text(
    prefix + heading + "\n\n" + chr(96) * 3 + "text\n"
    + "\n".join(shas) + "\n" + chr(96) * 3 + "\n",
    encoding="utf-8",
)
print("SYNCED", len(files), "canonical source files at package version", version)
