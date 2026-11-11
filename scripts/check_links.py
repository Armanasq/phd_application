#!/usr/bin/env python3
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MDCODE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
errors = []
for path in sorted(ROOT.rglob("*.md")):
    if "/.git/" in str(path):
        continue
    for raw in MDCODE.findall(path.read_text(encoding="utf-8")):
        link = raw.strip().split(" ", 1)[0].strip("<>")
        if not link or link.startswith(("https://","http://","mailto:","#","data:","javascript:")):
            continue
        target = unquote(link.split("#", 1)[0])
        if not target:
            continue
        full = (path.parent / target).resolve()
        if not full.is_relative_to(ROOT.resolve()) or not full.exists():
            errors.append(f"{path.relative_to(ROOT)} -> {link}")
if errors:
    print("FAIL: broken local Markdown links\n" + "\n".join(errors))
    sys.exit(1)
print("PASS: internal Markdown file links resolved")
