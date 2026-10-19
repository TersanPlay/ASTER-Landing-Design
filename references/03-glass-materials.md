# Glass Materials — Acrylic / Mica-like

These are CSS interpretations inspired by contemporary desktop frosted-glass interfaces, not Microsoft-native proprietary materials.

## Usage
- Mica-like: subtle, persistent application shells and sidebars; often more opaque, without strong background blur.
- Acrylic-like: temporary overlays, popovers, menus and floating control panels where backdrop separation is useful.
- Opaque: default for dense data tables, body text and critical controls.

## Intensity tokens
Subtle: 10px backdrop blur; standard: 22px; strong: 36px. Increase opacity or underlying scrim alongside blur so text contrast remains robust.

## Safe CSS
```css
.aster-glass {
  background: rgba(18, 35, 59, .74);
  border: 1px solid rgba(208, 228, 255, .16);
  box-shadow: 0 16px 48px rgba(0, 0, 0, .18);
  -webkit-backdrop-filter: blur(var(--glass-blur, 22px)) saturate(145%);
  backdrop-filter: blur(var(--glass-blur, 22px)) saturate(145%);
}
@supports not (backdrop-filter: blur(1px)) {
  .aster-glass { background: #15243a; }
}
@media (prefers-reduced-transparency: reduce) {
  .aster-glass { background: #15243a; -webkit-backdrop-filter: none; backdrop-filter: none; }
}
```

Provide light-theme analogues using appropriately opaque white surfaces. Test against actual background imagery and gradients, including scrolling. Never put low-contrast content directly over busy translucent backdrops. Fall back to opacity rather than expensive animated blurs on constrained devices.