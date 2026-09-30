<!-- design-system-manifest: Fuji v1.0.0 -->
<!-- Generated from the manifest with the design agent's templates/CLAUDE.md (Sep 2026 version); regenerate when its version changes. Loaded every turn, so keep it short: detail stays in the manifest, which the tools read. -->

# Design system: Fuji

All UI follows this, even quick edits. New pages and features: use the **design-agent** skill.

**Color:** background `#f7f5f1` · surface `#ffffff` · border `rgba(22,21,26,0.09)` · text `#16151a` / `rgba(22,21,26,0.64)` · primary `#00d4aa` (text on it `#07271f`) · secondary `#2b63f0` (max 1) · success/warning/error/info `#007a63`/`#9b6a00`/`#bf4b36`/`#2b63f0` · hover/active/focus `#00d4aa`/`#0a9c7e`/`#00d4aa`

**Type:** Archivo (display), Archivo (body), JetBrains Mono (UI/mono). Styles: page-title h1-28/34/800; section-heading h2-18/20/800; body body-15/500; caption mono-12/500; control mono-12/700; stat stat-28/36/800

**Spacing:** scale [4, 8, 12, 16, 20, 24, 32, 40, 48, 64]. Roles: card-padding 24 (Card); control-padding-x 16 (Button); field-padding-x 12 (Input, Select, Textarea); stack-related 8; stack-group 24; section 32; page-gutter 16. Radius radius-sm 8, radius-button 10, radius-banner 12, radius-lg 16, radius-modal 20, radius-pill 9999.

**Layout:** 12 cols, gutter 24px; breakpoints sm 640, md 768, lg 1024, xl 1280; phone first, verified at 320px and 200% text.

**Components:** Select — pending, don't reuse; Button (primary/secondary/destructive/utility); Input (default/error); Textarea (default); Toggle (default); SortPillGroup (default); NativeSelect (default); Card (default); GameCard (default); Badge (neutral/info/positive/negative/mixed); Label (default); StatusDot (default); InlineAlert (info/success/warning/error); InlineError (default); Toast (default); Skeleton (default/SkeletonCard); EmptyState (default/compact); Collapsible (default); Dialog (confirm-destructive); Breadcrumb — pending, don't reuse; Pagination (default); Tabs (default)

**Never:** pure red for errors (use --color-negative coral); mint (--color-accent) over ~10% of a screen by area; mint (--color-accent) as text on light surfaces (1.91:1) — use --color-accent-text; chart data painted in --color-accent (the 'two greens' bug) — use --color-chart-1..6; raw greys (#888, #999) — they don't flip in dark mode; new Terminal legacy token usage; color as the only signal for a state. Icons: inline-svg only.

**Rules:**
- Only these tokens, roles, styles and components. The same kind of element looks the same everywhere.
- One primary action per screen.
- Touch targets ≥ 44px, text ≥ 11px, WCAG-AA contrast, and never color alone for a state.
- Every core task is understood in 3 s, reached in ≤ 3 taps, and done in ≤ 3 min.
- Before editing UI, `python3 .claude/design-agent/tools/design_context.py <file>` shows the design that owns it, and the hook shows it on the first edit. Contradicting that design's decision is a design change: raise it, don't just edit.
- Critiques are `where: what → fix (rule)`, never a bare preference.
