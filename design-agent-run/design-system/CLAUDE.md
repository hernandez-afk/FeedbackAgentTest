<!-- design-system-manifest: Fuji v1.0.0 -->
<!-- Generated from design-system-manifest.yaml (templates/CLAUDE.md of the Design System Agent).
     Regenerate whenever the manifest's version changes. The manifest is the source of truth;
     in atari-game-feedback-engine, DESIGN_SYSTEM.md and tokens/*.json remain canonical, and
     this file is the agent-facing summary of them. -->

# Design system: Fuji

Every UI change in the Game Feedback Engine follows these rules, including quick edits that don't run the full design agent. The full data is in `design-system-manifest.yaml`; the written rulebook is `DESIGN_SYSTEM.md` in the app repo. For new screens or features, use the **design-generation** skill.

## Tokens

Use only these values, always through their CSS variables (`var(--color-*)`, `--radius-*`, `--dur*`). Never hard-code a color, spacing, size, radius or duration. Tokens are edited only in `tokens/primitive.json` + `tokens/semantic.json`.

**Color roles**
- Neutrals: background `#f7f5f1` (`--color-bg`), surface `#ffffff` (`--color-surface`), border `rgba(22,21,26,0.09)` (`--color-hair`), text `#16151a` (`--color-ink`), muted text `rgba(22,21,26,0.64)` (`--color-ink-faint`)
- Accents: primary `#00d4aa` (`--color-accent`; text on it: `#07271f` `--color-accent-ink`), secondary `#2b63f0` (`--color-info`; at most 1 on screen at once)
- Status: success `#007a63`, warning `#9b6a00`, error `#bf4b36`, info `#2b63f0`
- Interaction: hover `#00d4aa`, active `#0a9c7e`, focus `#00d4aa` (focus ring)
- Contrast: WCAG-AA

**Typography**
- Display `Archivo`, body `Archivo`, UI `JetBrains Mono`; weights [500, 700, 800]
- Scale: base 15px × 1.25, steps [mono-12, body-15, h2-18/20, h1-28/34, stat-28/36, display-32/60]; line height 1.5
- Roles: heading = `.adp-h1` / `.adp-h2` (Archivo 800, ink) · readable subtext = `.adp-body` in `--color-ink-sub` (Archivo 500) · form label = `.adp-mono` / `Label` (JetBrains Mono, sub ink). Display vs mono is the distinction; never mix within one role.

**Spacing & layout**
- Spacing scale (px): [4, 8, 12, 16, 20, 24, 32, 40, 48, 64]; base unit 4px
- Radius: radius-sm 8 (chips) · radius-button 10 (buttons, inputs) · radius-banner 12 (banners, toasts) · radius-lg 16 (cards, panels) · radius-modal 20 (modals) · radius-pill 9999 (pills, toggle track)
- Grid: 12 columns, 24px gutter, max width 1280px, alignment tolerance 0px
- Breakpoints (design mobile first): sm 640, md 768, lg 1024, xl 1280

**Motion**
- Durations: micro 160ms, state 200ms, page 320ms
- Easing: entrance `cubic-bezier(.4,0,.2,1)`, exit `cubic-bezier(.4,0,.2,1)`, transition `cubic-bezier(.4,0,.2,1)`; respect reduced motion: true (global rule in globals.css)

**Components.** Reuse these before building anything new:
- Button / buttonClasses (`@/components/primitives/Button`): primary, secondary, destructive, utility
- Input (`@/components/primitives/Input`): default, error · Textarea · Toggle
- SortPillGroup (GamesCatalogBrowser inline pattern): default
- NativeSelect (SessionsFilters SELECT_CLASS pattern): default
- Card (`@/components/primitives/Card`), GameCard (`@/components/GameCard`), Badge (neutral, info, positive, negative, mixed), Label, StatusDot
- Banner (InlineAlert: info, success, warning, error), InlineError, Toast, Skeleton (default, SkeletonCard), EmptyState (default, compact)
- Collapsible, Pagination (sessions), Tabs (DashboardTabs), Dialog (confirm-destructive pattern)
- Pending review — don't reuse: Breadcrumb (not in Fuji)

## Brand rules

- Never:
  - pure red for errors (use `--color-negative` coral)
  - mint (`--color-accent`) over ~10% of a screen by area
  - mint as text on light surfaces (1.91:1) — use `--color-accent-text`
  - chart data painted in `--color-accent` — use `--color-chart-1..6`
  - raw greys (#888, #999) — they don't flip in dark mode
  - new Terminal legacy token usage
  - color as the only signal for a state
- Icons: inline-svg only (`aria-hidden`, `stroke="currentColor"`)
- Decisions: `ask-major-only`. Details inside the token set are decided and logged; layout paradigm and information-architecture shape are asked, with 2–3 options and trade-offs.
- One primary action per screen. Secondary actions never get primary-accent styling.
- New components or variants go through a gap report and a verification report. Never invent one inline.

## The design harness

Every design goes through the same loop, with a gate at each stage: brief → scope → flow → design → audit → approval → build → verify (`HARNESS.md`). `python3 .claude/design-agent/tools/harness.py status` shows where each design is; `next --project <ID>` says what to do.

## New pages

Start from a page brief (`templates/page-brief.md`): purpose, ranked goals, tasks with where they start, what the page depends on (who creates each thing, and where its data comes from), content with amounts, states, and testable acceptance criteria. Check it with `python3 .claude/design-agent/tools/brief_lint.py <brief>`. The design agent sweeps it for edge cases (`skills/edge-case-sweep.md`), optimizes it to fit this design system, and shows every change for approval before designing. It then maps the user flow: how users get to the page and where they go next. A new link on another design's page is that design's change: it's proposed to its owner, never edited in quietly.

## Working on existing UI

- **Before changing UI code, know which design owns it.** Run `python3 .claude/design-agent/tools/design_context.py <file>`, or rely on the hook, which shows it on the first edit. Follow that design's decisions and components.
- **Changing a decision is a design change, not a code change.** If your edit would contradict a decision (a different filter pattern, a new layout), stop and raise it. Don't just edit.
- **Designs that share a pattern stay the same.** If the design context says it shares a pattern with another design, change both or neither.
- **UI that no design owns needs a scope check before it ships.** It may belong to an existing design.
- **Off-token values get sent back.** The token lint runs after every edit. Replace the value with a token; don't add it to the allow-list to get past the check.

## Critique criteria

Use these whenever you review, critique or change a design, not only in formal audits.

**Principles** (full text in `design-principles.md`): simplicity is architecture · hierarchy drives everything · consistency is non-negotiable · alignment is precision · whitespace is a feature · responsive is the real design · design the feeling · no cosmetic fixes without structural reasoning.

**3-3-3 rule**, for every core task:
- understood in 3 s at `sm`
- reached in ≤ 3 clicks
- finished in ≤ 3 min

Never meet the click limit by cramming.

**Wickens' 13 display principles:**
- Perception: legible (≥ 11px) · no more than 5 unlabeled levels · follow convention · two cues for critical states · similar-looking means similar
- Mental model: pictorial realism · the moving part
- Attention: low access cost · related info close together · multiple channels
- Memory: show, don't make people remember · preview consequences · consistency

**Mobile at all times:**
- Design the phone first and verify at 320px: no sideways scrolling.
- Everything still works with text at 200%.
- Touch first: targets ≥ 44px and ≥ 8px apart; nothing is hover-only.
- On phones, the primary action is within thumb reach.
- Respect safe areas and the on-screen keyboard.

**Every component is dynamic:**
- Fluid: sized by its container and content, with min/max limits. No fixed size above 64px.
- Works in any container width, with short, long (+40% translated), empty or overflowing content, by touch, pointer and keyboard.
- Content comes in through props, never hard-coded.

**Accessibility:** AA; touch targets ≥ 44px; visible focus; semantic HTML.

**Density:** paginate lists over 50 items; group forms over 7 fields; details go on a drill-down view.

**Severity:**
- **Blocker:** off-token value, invented component, more than one primary action, skipped decision or scope check, contrast or touch-target failure
- **Major:** hurts usability or consistency
- **Minor:** polish

**How to write a critique.** Every point uses the form `[Screen/Component]: [what's wrong] → [what it should be] → [why it matters]`, citing a token, principle or rubric category. Implementation notes give the exact component, property, old value → new value. Never write a bare preference like "make it pop" or "feels cleaner".
