# ASTER Foundations

## Principles
Create original, legible, editorial and adaptable interfaces. Prioritize semantic tokens, hierarchy and usability over decoration. Do not replicate DeepSeek or other vendors' trade dress.

## Color
Use a semantic mapping for each mode: background, foreground, surface, elevated, muted, border, primary, primary-foreground, focus, positive, warning, destructive. Never encode component behavior with fixed dark-only hex values. Example starting palette: void #080e19; navy #0e1b30; ocean #183354; cobalt #264e82; electric #3773f5; frost #f2f5fa. These are ASTER proposals, not extracted official CSS.

## Typography
Prefer a readable variable sans-serif (Inter/Geist/system UI) and monospace for technical snippets. Responsive display heading clamp(2.75rem, 6vw, 5rem), section heading clamp(1.8rem, 4vw, 3rem), body 1rem, captions 0.75–0.875rem. Maintain comfortable line length around 60–75 characters.

## Layout
4px base spacing rhythm, spacious editorial section intervals, fluid container max-width 1200–1280px, 12-column desktop grid, and resilient mobile stacks. Breakpoints should follow content rather than device brands.

## Geometry and elevation
Choose consistent radii: sm 6px, md 12px, lg 18px, xl 24px; pills reserved for relevant controls. Surfaces must use nuanced borders and shadows; avoid competing highlights.

## Motion
Meaningful 150–300ms microinteractions, no forced reveal animation, honor prefers-reduced-motion. Keep readability and performance intact.

## Theming
Provide light, dark and system preference where requested. All surface and foreground combinations must meet applicable WCAG 2.2 AA criteria; always verify contrast.