<div align="center">
  <img src="docs/brand/aster-wordmark.svg" alt="ASTER Landing Design" width="760" />
<p><strong>Professional landing-page design intelligence for AI coding agents and modern IDE workflows.</strong></p>
<p>
    <a href="https://agentskills.io/specification"><img alt="Agent Skills" src="https://img.shields.io/badge/Agent%20Skills-compatible-315A94?style=flat-square"></a>
    <a href="./SKILL.md"><img alt="Version" src="https://img.shields.io/badge/version-1.0.0-153653?style=flat-square"></a>
    <a href="./LICENSE"><img alt="License MIT" src="https://img.shields.io/badge/license-MIT-214F6B?style=flat-square"></a>
    <a href="./references/05-frameworks.md"><img alt="Framework agnostic" src="https://img.shields.io/badge/framework-agnostic-2A496E?style=flat-square"></a>
  </p>
<p>
    <a href="#quick-start">Quick start</a> ·
    <a href="./INSTALLATION.md">Installation</a> ·
    <a href="./SKILL.md">Skill</a> ·
    <a href="./docs/BRAND-IDENTITY.md">Brand identity</a>
  </p>
</div>
---
Overview
ASTER Landing Design is a portable, vendor-neutral skill package for AI agents that create, personalize, refactor and audit high-quality landing pages.
It combines:
a corporate visual direction;
atmospheric layout composition;
Acrylic / Mica-like glass materials;
light and dark theme guidance;
and production-minded accessibility rules.
ASTER is not a UI framework, browser extension or design editor. It is an instruction system built around `SKILL.md` and a focused reference library.
---
Professional identity
<table>
<tr>
<td width="25%" align="center">
  <img src="docs/brand/aster-logo-icon-dark.svg" alt="ASTER icon dark" width="180" />
  <br/><sub>Primary icon · dark</sub>
</td>
<td width="25%" align="center">
  <img src="docs/brand/aster-logo-icon-light.svg" alt="ASTER icon light" width="180" />
  <br/><sub>Alternate icon · light</sub>
</td>
<td width="50%" valign="middle">
  The ASTER identity is centered on a refined <strong>stylized letter A</strong>, created to feel more professional, software-oriented and presentation-ready. The symbol replaces earlier decorative explorations and becomes the recommended mark for README, documentation headers and presentation surfaces.
</td>
</tr>
</table>
For logo rules, color direction and usage recommendations, see docs/BRAND-IDENTITY.md.
---
What this skill helps agents do
Area	Capabilities
Design	Create professional landing pages with original composition, strong hierarchy and a premium visual tone
Customization	Adapt palette, type, spacing, brand tone and CTAs without breaking the existing stack
Implementation	Work with React, Next.js, Vue, Nuxt, Svelte, Astro or plain HTML/CSS/JS
Quality	Review accessibility, responsiveness, interaction quality and consistency
Documentation	Explain layout decisions, tokens, components and verification steps
---
Core design language
1) Corporate, calm, technological
ASTER is designed for a more mature and credible presentation style. It favors dark navy foundations, refined blues, structured typography and disciplined use of motion and translucency.
2) Glass with restraint
The system supports Acrylic-like and Mica-like surfaces, but the effect must remain readable, elegant and useful. Glass is a supporting material, not a gimmick.
3) Stack-preserving implementation
The skill adapts to the project's existing framework and styling strategy instead of forcing a migration.
4) Real-world documentation quality
The repository presentation should feel like a serious software asset, with a clear identity, installation guidance, usage examples and practical references.
---
Quick start
If your platform supports Agent Skills installation:
```bash
npx skills add TersanPlay/ASTER-Landing-Design
```
Or clone the repository manually:
```bash
git clone https://github.com/TersanPlay/ASTER-Landing-Design.git
```
Then place the extracted skill folder in a supported skills directory as described in INSTALLATION.md.
Example prompt
> Use `aster-landing-design` to create a professional responsive landing page for my SaaS product. Keep my existing framework. Use ASTER visual foundations, a dark/light theme strategy, restrained glass surfaces and a clear conversion flow.
---
Package structure
```text
ASTER-Landing-Design/
├── SKILL.md
├── README.md
├── INSTALLATION.md
├── LICENSE
├── assets/
│   ├── aster-tokens.css
│   └── landing-starter.html
├── docs/
│   ├── BRAND-IDENTITY.md
│   └── brand/
│       ├── aster-logo-icon-dark.svg
│       ├── aster-logo-icon-light.svg
│       └── aster-wordmark.svg
├── examples/
│   └── prompts.md
├── references/
│   ├── 01-foundations.md
│   ├── 02-layouts.md
│   ├── 03-glass-materials.md
│   ├── 04-components.md
│   ├── 05-frameworks.md
│   ├── 06-quality-checklist.md
│   └── 07-content-and-copy.md
└── scripts/
    └── validate_skill.py
```
---
Included references
Foundations — spacing, typography, color roles, motion and geometry.
Layouts — landing-page structures and conversion patterns.
Glass materials — Acrylic / Mica-like surfaces and fallback behavior.
Components — UI contracts and composable building blocks.
Frameworks — implementation guidance per stack.
Quality checklist — acceptance criteria for design, accessibility and engineering.
Content and copy — writing structure, SEO and narrative hierarchy.
---
Validation
```bash
python scripts/validate_skill.py
```
This script verifies the expected structure of the ASTER skill package. It does not replace manual UI review, browser testing or accessibility verification.
---
Philosophy
> **Professional by default. Flexible by design. Clear in execution.**
ASTER aims to help agents produce landing pages that look credible, feel polished and remain implementable across modern frontend environments.
