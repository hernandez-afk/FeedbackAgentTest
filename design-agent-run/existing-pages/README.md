# Existing pages: Design System Agent standalone pass

Every page that shipped before the agent, in seven areas (GFE-SHELL, GFE-CAPTURE,
GFE-REVIEW, GFE-DASHBOARD, GFE-CATALOG-ADMIN, GFE-IMPORTS, GFE-ADMIN). Each area is
registered in `../design-system/design-index.yaml` as a backfill project.

## How it ran
1. Screenshots and a critic audit per area. `<area>/audit-report-standalone-1.md`;
   evidence in `screenshots/before/` and `measurements-before.json`.
2. The agent was updated (Sep 30: lite mode, tools do the checking). The rest follows it:
   - The Fuji manifest gained `harness.mode: lite`, `typography.styles` and
     `spacing.roles`. `CLAUDE.md` was regenerated from the new template.
   - Every page was rendered with the agent's `tools/screenshots.py`. The app needs a
     sign-in, so a preload gave the tool's browser a saved session. The agent's code was
     not changed.
3. Fixes: `existing-pages.patch`, 10 commits for atari-game-feedback-engine, applied on top
   of `../game-sort/game-sort.patch`:
   - 1 commit of shared Fuji primitives: 44px buttons and inputs, wrapping labels, token
     hover, and `selectClasses`;
   - 1 commit per area;
   - 1 commit of follow-ups, and 1 for the tool findings on Games and Sessions.
4. After: `screenshot-sets/after/<page>/`, with the tool output and the screenshots.

## Result (tool blockers, 14 pages)
63 before → 18 after, once the primitives commit and every area were fixed. The 18
left are tool limitations: the rule is met, but the tool measures a smaller element.
- A checkbox or switch inside a 44px `<label>`: the tool measures the 16–20px box, not
  the label.
- `sr-only` inputs under 44px answer pills.

The remaining tool "majors" are either false positives or design-system decisions:
- **Fluid headings:** h1 is 28px at 320px and 34px on desktop by design, and the tool
  reads that as two sizes.
- **Mixed button sizes on one screen:** sm, md and lg together. Fuji's size policy allows
  lg for form submits; the agent's consistency check doesn't. The design-system owner
  decides.

## Not finished (paused at the user's request)
- The critic pass with the new `critic.md` was stopped before it returned.
- GFE-SORT's own pages were re-rendered with the tool and fixed. Build pills, the page's
  Add game link and the Manage builds toggle are now 44px, and the sessions email wraps.
  What's left is tool limitations: stretched-link titles, sr-only labels and fluid headings.

## Needs a human
Every **[decision]** item in the seven audit reports. Also:
- approving the proposed `Select` component and the primitive changes;
- the md button text size (13px, off the scale) and the kicker size (11px);
- the form-label typeface.
