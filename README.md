# ASTER Landing Design · Universal Agent Skill

**Version:** 1.0.0 · **License:** MIT · **Language:** Instructions in English; content generation can be in any user-requested language.

A portable, vendor-neutral skill for AI coding agents and IDEs that support the [Agent Skills specification](https://agentskills.io/specification). It enables the agent to create, customize, migrate, and audit original landing pages using ASTER Hybrid Design System foundations, glass materials, layout patterns and accessibility rules. It is **not** a browser extension, framework package or guaranteed feature in every IDE. A platform must support loading `SKILL.md` or receive its instructions manually.

## Contents

```
aster-landing-design/
├── SKILL.md                   # Agent entrypoint and workflow
├── references/                # Foundations, layouts, glass, components, frameworks, QA, copy
├── assets/
│   ├── aster-tokens.css       # Portable CSS variables and glass recipes
│   └── landing-starter.html   # Dependency-free starter (keep CSS alongside it)
├── scripts/validate_skill.py  # Offline format and reference validation
├── examples/prompts.md        # Copy-ready user requests
├── INSTALLATION.md            # Installation and troubleshooting
└── LICENSE
```

## Install

1. Download/extract the folder `aster-landing-design` intact.
2. Copy it to a skills directory recognized by your agent, at the project or user level (examples in [INSTALLATION.md](INSTALLATION.md)).
3. Restart/rescan the IDE/agent if necessary.
4. Ask: **“Use aster-landing-design to create a responsive landing page for my project.”**
5. If the platform does not support Agent Skills, attach/paste `SKILL.md` and the relevant `references/` files as custom instructions.

## Quick demo

Copy `assets/landing-starter.html` **and** `assets/aster-tokens.css` into the same folder, then open `landing-starter.html` in a browser. The page is a static reference, not a full website template or a dependency of the skill.

## Validation

`python scripts/validate_skill.py` (or `python3 scripts/validate_skill.py`). This checks skill metadata, matching directory name, reference links, required files and basic starter structure. It does **not** replace visual QA, accessibility testing or framework builds.

## Using in an existing ASTER project

Read the project's existing token and UI packages; treat them as the canonical implementation. Use the skill for design decision-making, not to duplicate the package CSS. The portable assets are a fallback when no ASTER packages are installed.

## Provenance

Original ASTER conventions informed by modern interface design including DeepSeek Harness and Windows-style glass material concepts. This skill is not sponsored by, endorsed by or affiliated with DeepSeek or Microsoft and includes no copied official brand assets.