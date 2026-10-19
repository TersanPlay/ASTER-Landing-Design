#!/usr/bin/env python3
"""Validate core ASTER Agent Skill package structure without external dependencies."""
from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
required = [
    "SKILL.md", "README.md", "INSTALLATION.md", "LICENSE",
    "references/01-foundations.md", "references/02-layouts.md",
    "references/03-glass-materials.md", "references/04-components.md",
    "references/05-frameworks.md", "references/06-quality-checklist.md",
    "references/07-content-and-copy.md",
    "assets/aster-tokens.css", "assets/landing-starter.html",
    "examples/prompts.md",
]
missing = [name for name in required if not (root / name).is_file()]
skill = root / "SKILL.md"
metadata_ok = skill.is_file() and skill.read_text(encoding="utf-8").startswith("---\nname: aster-landing-design")
if missing or not metadata_ok:
    print("ASTER skill validation: FAIL")
    if missing:
        print("Missing:", ", ".join(missing))
    if not metadata_ok:
        print("SKILL.md frontmatter missing or invalid")
    sys.exit(1)
print("ASTER skill validation: PASS")
