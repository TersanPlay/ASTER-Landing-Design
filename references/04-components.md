# Component Architecture

Use existing project primitives first. New shared primitives should use accessible semantics, defined props, composable slots and predictable states.

## Component groups
Actions: Button, IconButton, LinkButton; inputs: Input, Textarea, Select, Checkbox, Radio, Switch; display: Badge, Avatar, Progress, Tooltip, Card; navigation: Navbar, Tabs, Breadcrumb, MobileMenu; overlay: Dialog, Drawer, Popover, Toast; feedback: Alert, Skeleton, EmptyState; composition: Container, Stack, Grid, Hero, FeatureGrid, CTA, Footer.

## Contract
Each component specifies variants, sizes, focus-visible state, hover/active states, disabled/loading behavior, semantic role, keyboard interaction and theme-aware styles. Use native HTML elements appropriately; avoid generic clickable divs.

## Demo components
For demonstration pages show actual functioning interactions: theme switch, tab switching, modal open/close, input focus, buttons with true actions. Avoid nonfunctional demo buttons.

## Accessibility
Focus trapping and escape behavior in dialogs; labels for inputs; aria-expanded for disclosure; logical heading structure; sufficient target sizing; no color-only status indication.

## Glass
GlassPanel is optional and must expose material (acrylic/mica), intensity (subtle/standard/strong), and an opaque fallback. It must not globally apply blur to every card.