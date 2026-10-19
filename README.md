<div align="center">

# ✳ ASTER
### LANDING DESIGN · UNIVERSAL AGENT SKILL

**Build remarkable landing pages. Keep your stack. Own your aesthetic.**

A framework-agnostic design intelligence package for AI coding agents, combining atmospheric art direction, reusable foundations, frosted-glass materials and production-minded accessibility.

[![Agent Skills](https://img.shields.io/badge/Agent_Skills-compatible-315A94?style=flat-square)](https://agentskills.io/specification)
[![Version](https://img.shields.io/badge/version-1.0.0-153653?style=flat-square)](SKILL.md)
[![License MIT](https://img.shields.io/badge/license-MIT-214F6B?style=flat-square)](LICENSE)
[![Framework agnostic](https://img.shields.io/badge/framework-agnostic-2A496E?style=flat-square)](references/05-frameworks.md)

[Get started](#quick-start) · [Explore design language](#design-language) · [Installation](INSTALLATION.md) · [Skill specification](SKILL.md)

</div>

![ASTER desktop design preview](docs/images/aster-desktop-preview.svg)

> **Visual preview:** the image above is an original, conceptual ASTER composition, **not** a captured browser screenshot or a claim of pixel-perfect implementation. A dependency-free working demo ships in [assets/landing-starter.html](assets/landing-starter.html).

---

## One design language. Many possibilities.

ASTER Landing Design helps AI agents **create, personalize, refactor and audit** high-quality landing pages. It is a portable **Agent Skill**, not a React dependency, no-code editor, browser extension or proprietary visual framework. The agent reads [SKILL.md](SKILL.md) and loads focused references when needed.

| Design | Engineering | Experience |
| :--- | :--- | :--- |
| Editorial hero composition | Existing framework preserved | Responsive by default |
| Atmospheric depth and gradients | Semantic CSS design tokens | Keyboard and focus states |
| Acrylic / Mica-like glass | Stack-specific integration guidance | Reduced-motion / transparency fallbacks |
| Light and dark themes | Reusable component contracts | Accessibility and QA checklist |

## See the language in action

<table>
<tr>
<td width="67%" valign="top">

**Desktop · atmospheric composition**

![Desktop atmospheric ASTER concept](docs/images/aster-desktop-preview.svg)

A hero-led visual direction with strong hierarchy, diffuse illumination and layered workspace surfaces.

</td>
<td width="33%" valign="top">

**Mobile · considered reflow**

![Mobile ASTER concept](docs/images/aster-mobile-preview.svg)

A vertically composed interface that keeps hierarchy, touch targets and glass material readability intact.

</td>
</tr>
</table>

*Both visuals are design previews authored for the README. They are not screenshots of the runnable starter. For source-based browser captures, see [Screenshot production](#screenshot-production).*

## Design language

### 01 — Atmospheric, not ornamental

Dark navy bases, restrained electric blues, editorial whitespace and softly focused illumination establish atmosphere without sacrificing content readability.

### 02 — Glass with purpose

ASTER provides three optical intensities and two conceptual material families:

| Material | Primary use | Typical behavior |
| :--- | :--- | :--- |
| **Mica-like** | Persistent app shells and navigation | Subtle, relatively opaque surfaces |
| **Acrylic-like** | Floating UI, popovers and overlays | Backdrop blur and separation |
| **Subtle** | Quiet layering | 10px blur reference |
| **Standard** | Balanced panels | 22px blur reference |
| **Strong** | Distinct floating layers | 36px blur reference |

Always use adequate text contrast and opaque fallbacks. The names describe CSS interpretations inspired by current desktop UI conventions, not proprietary Microsoft implementations. See [Glass Materials](references/03-glass-materials.md).

### 03 — Adaptable foundations

ASTER establishes semantic roles for background, foreground, surface, border, focus and actions. Its starter palette is a design proposal—not colors claimed to be extracted from DeepSeek's source code.

```css
@import "./aster-tokens.css";

.product-panel {
  color: var(--aster-color-fg);
  background: var(--aster-color-surface);
  border: 1px solid var(--aster-color-border);
  border-radius: var(--aster-radius-lg);
}
```

### 04 — Original compositions

Use ASTER as a **system of decisions**, not a template that duplicates the same hero or three-card layout for every site. Adapt visual rhythm, information architecture and sections to the audience, proposition and primary CTA.

## Quick start

Install via an Agent Skills-compatible installer, if your platform supports it:

```bash
npx skills add TersanPlay/ASTER-Landing-Design
```

Alternatively clone and copy the skill folder into your agent's supported skills directory:

```bash
git clone https://github.com/TersanPlay/ASTER-Landing-Design.git
```

Consult [INSTALLATION.md](INSTALLATION.md) for manual paths, discovery and troubleshooting. Agent Skills support varies by IDE; installation and automatic invocation are not universal guarantees.

**Prompt example**

> Use `aster-landing-design` to create an original, responsive landing page for my developer product. Keep the existing framework. Use atmospheric depth, accessible dark/light themes, an Acrylic-like menu overlay, Mica-like navigation and a clear primary CTA. Review the result against the skill's QA checklist.

## Inside the skill

```text
ASTER-Landing-Design/
├── SKILL.md                     # Agent instructions & workflow
├── README.md                    # Project overview
├── INSTALLATION.md              # Supported installation approaches
├── LICENSE
├── assets/
│   ├── aster-tokens.css         # Semantic colors, glass, themes
│   └── landing-starter.html     # Functional HTML starter
├── docs/images/                 # Editorial design previews
│   ├── aster-desktop-preview.svg
│   └── aster-mobile-preview.svg
├── examples/
│   └── prompts.md               # Practical prompt library
├── references/
│   ├── 01-foundations.md        # Tokens, typography, geometry
│   ├── 02-layouts.md            # Page structures & conversion
│   ├── 03-glass-materials.md    # Acrylic / Mica / transparency
│   ├── 04-components.md         # Component contracts
│   ├── 05-frameworks.md         # React, Vue, Svelte, Astro, HTML
│   ├── 06-quality-checklist.md  # Accessibility, responsive QA
│   └── 07-content-and-copy.md   # Content structure and SEO
└── scripts/
    └── validate_skill.py       # Offline structural validation
```

## Compatible workflows

ASTER's instructions can guide work in **React, Next.js, Vue, Nuxt, Svelte, SvelteKit, Astro and plain HTML/CSS/JavaScript**. Existing styling systems such as Tailwind, CSS Modules and vanilla CSS should be preserved rather than replaced without consent.

Use this skill to:
- **Create** a differentiated landing page from a clear brief.
- **Customize** an existing product identity without breaking its functionality.
- **Refine** hierarchy, responsiveness, interaction and motion.
- **Audit** against accessibility, performance and UX criteria.
- **Document** design decisions and reusable tokens for ongoing maintenance.

## Try the working starter

The repository contains a small interactive landing starter with a responsive composition, glass panel and theme toggle. No build tool is required.

```bash
git clone https://github.com/TersanPlay/ASTER-Landing-Design.git
cd ASTER-Landing-Design/assets
# Open landing-starter.html in your browser
```

Keep `aster-tokens.css` in the same directory as the HTML file.

### Screenshot production

For authentic screenshots, run the starter in a browser and capture desktop (e.g. 1440×900) and mobile (e.g. 390×844) viewports. Replace or supplement the conceptual SVG previews with these PNGs and clearly label the source, viewport and capture date. Do not present vector mockups as browser captures.

## Quality is a requirement

A completed ASTER output should have functional CTAs, responsive layouts without horizontal overflow, correctly labelled forms, visible keyboard focus, sufficient contrast, purposeful motion and reduced-transparency fallback behavior. Run actual build, lint and test scripts when available and report any unverified items.

See the [full quality checklist](references/06-quality-checklist.md) and [component contracts](references/04-components.md).

## Validation

```bash
python scripts/validate_skill.py
```

This verifies the skill's expected file structure and entrypoint metadata. It does **not** certify visual fidelity, browser support, runtime correctness or accessibility compliance.

## Philosophy

> **Atmosphere attracts. Structure guides. Clarity converts.**

ASTER is an independent, original design approach informed by modern software interface conventions. It is not affiliated with DeepSeek, Microsoft or any other platform.

---

<div align="center">

**ASTER Landing Design · Agent Skill v1.0.0**

[Skill](SKILL.md) · [Installation](INSTALLATION.md) · [Reference Library](references/01-foundations.md) · [MIT License](LICENSE)

</div>
