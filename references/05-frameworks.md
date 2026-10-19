# Framework-Agnostic Implementation

Determine the existing stack before touching code. Do not migrate frameworks unless explicitly requested.

## HTML/CSS/JS
Use semantic sections, CSS custom properties, scoped classes and progressive enhancement. Keep starter dependency-free.

## React / Vite
Prefer TypeScript and composable components. Keep tokens separated from view state; use stable keys and appropriate hooks. Adopt existing styling conventions.

## Next.js
Use app or pages router already present, image/font optimization where appropriate; reserve client components for interactive features. Avoid hydration mismatches for theme preference.

## Vue / Nuxt
Use SFC conventions, semantic props and existing composables; avoid React-style patterns.

## Svelte / SvelteKit
Follow rune/store conventions used by project and maintain semantic markup.

## Astro
Keep primarily static content server-rendered and hydrate only necessary interactive islands.

## CSS systems
Use preexisting Tailwind, CSS Modules, vanilla CSS, Sass, or utility frameworks rather than introducing a replacement solely for ASTER. Integrate semantic tokens through CSS custom properties in all approaches.

## Assets and testing
Use locally controlled assets where available. Optimize background effects and animation, test keyboard input and at least mobile/tablet/desktop widths. Run actual project scripts before claiming success.