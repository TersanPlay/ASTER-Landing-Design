---
name: aster-landing-design
description: Create, customize, refactor, and audit professional responsive landing pages using the ASTER Hybrid Design System. Use for marketing sites, product launches, SaaS, portfolios, AI products, design-system showcases, dark/light themes, atmospheric backgrounds, frosted glass Acrylic/Mica-like materials, React/Next.js/Vue/Svelte/Astro or accessible static HTML/CSS. Preserve existing project conventions while applying ASTER tokens, layouts, and quality gates.
license: MIT
compatibility: Any AI coding agent or IDE that supports Agent Skills (SKILL.md); framework-agnostic Markdown/CSS. Code execution or browser preview is optional but recommended.
metadata:
  author: ASTER Contributors
  version: "1.0.0"
  category: frontend-design
---

# ASTER Landing Design — Agent Skill

Generate original, production-minded landing pages with the ASTER Hybrid Design System. This skill is independent of DeepSeek or Microsoft. References to Acrylic/Mica describe visual inspiration, not native Microsoft materials. Never copy third-party brand assets, proprietary source, or exact protected visuals.

## Activation and brief

Use when asked to **create, customize, redesign, improve, migrate, extend, document, or audit** a landing page. Treat an existing codebase as the source of truth for framework, build commands, routing, naming, and components. For absent details, choose sensible defaults and disclose them; ask only when a missing requirement changes the essential output (e.g., cannot identify the product or target audience).

Gather or infer: product/name, audience, conversion goal/CTA, content/sections, brand assets, preferred palette and theme, framework, localization, page constraints, target breakpoint, and accessibility requirements. Do not invent real performance numbers, logos, testimonials, partners, regulatory approvals, or customer claims. Use clearly labeled illustrative placeholders if needed.

## Mandatory execution sequence

1. **Inspect**: Read README/package manifest, route entry point, current styles, assets, design tokens and user requirements before changing code. Preserve repository setup. If no repository, select user's preferred stack; default to semantic HTML/CSS/JS for portability or React/TypeScript when interactive composition is needed.
2. **Plan**: Define the page's intended user journey (problem → value → evidence → features → CTA). Select sections from `references/02-layouts.md`; record primary CTA and its real destination/action.
3. **Foundations**: Load `references/01-foundations.md`. Apply semantic color/spacing/typography tokens rather than hardcoded per-component values. Dark and light surfaces must each be intentional, not naive inversions.
4. **Materials**: Read `references/03-glass-materials.md` whenever using translucent UI. Mica-like for persistent shells, Acrylic-like for transient overlays; Glass is optional and never makes content difficult to read. Prefer CSS fallbacks.
5. **Implement**: Use existing components first. Create accessible, reusable primitives only as required. Follow `references/04-components.md` for props, states, semantics and interaction details. Compose sections with distinctive but controlled typography and visual rhythm; avoid repetitive identical card grids.
6. **Adapt**: Consult `references/05-frameworks.md` for the detected framework. Never rewrite a user app into another stack without a request. Keep assets local when appropriate; avoid new heavy dependencies just for effects.
7. **Verify**: Apply `references/06-quality-checklist.md`. Check 320/375/768/1024/1440 px, overflow, image loading, keyboard navigation, focus, semantic landmarks, contrast, reduced-motion, reduced-transparency, visible CTA, runtime errors. Execute existing lint/test/build when tools allow. Clearly report anything untested; never claim a build passed if not run.
8. **Handoff**: Explain changed files, how to run, what was verified, and open limitations. Provide a concise customization guide, including token override points. Do not claim deployment or publication unless actually performed.

## Core visual grammar

- **Atmospheric depth**: layered radial gradients, restrained luminous emphasis, subtle grid/noise textures only when they serve hierarchy.
- **Editorial hierarchy**: strong hero headline, restrained supporting copy, generous whitespace, disciplined max-width; headings should carry meaning, not just decoration.
- **Surface materials**: opaque and Mica-like by default; Acrylic-like glass where background separation is useful; emphasize robust contrast over visual novelty.
- **Useful motion**: subtle reveal/hover effects with reduced-motion fallback; never gate content visibility on animation.
- **Product storytelling**: show plausible UI demos or illustrations rather than generic visual filler. Never misrepresent mock data as real.
- **Brand adaptability**: support a palette and radius family without hardcoding DeepSeek identity, ASTER wordmark, or one product archetype.

## Output contract

Every substantial implementation must deliver: a responsive page, working CTA or an explicitly labeled placeholder, reusable foundation tokens, accessibility fallbacks, and a short validation report. When asked only for a plan, deliver a specification rather than editing files. When asked to edit a given project, edit it rather than returning detached snippets. If browser/testing access is unavailable, state that plainly.

## File map (read only what applies)

- `references/01-foundations.md`: semantic tokens, color, type, motion, grids.
- `references/02-layouts.md`: layout recipes, section anatomy and conversion flows.
- `references/03-glass-materials.md`: Acrylic/Mica-like CSS, constraints, fallbacks.
- `references/04-components.md`: component inventory, semantics, interactions.
- `references/05-frameworks.md`: framework-specific adaptation principles.
- `references/06-quality-checklist.md`: acceptance criteria and handoff checks.
- `references/07-content-and-copy.md`: message architecture, copy and localization.
- `assets/aster-tokens.css`: importable theme foundation.
- `assets/landing-starter.html`: dependency-free runnable illustrative starter.
- `examples/prompts.md`: example user prompts and customization requests.
- `scripts/validate_skill.py`: portable package integrity checks.