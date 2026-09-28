# Audit — GFE-SORT revision 3 (implementation mode)

Independent audit by the agent's `design-critic` persona (artifact paths only, read-only), run against
atari-game-feedback-engine **`63a5ade`** (db71013..HEAD, 5 commits).

**overallVerdict: blocker.** Under the harness this goes to a person, and no auto-revise was run.

## Resolved since round 2
- GameCard actions are 44px (`GameCard.tsx` `ACTION_CLASS`, `ArchiveGameControl.tsx`).
- Tree text is 15px (`adp-body`), and the sort-button gap is 8px.
- SortButtons and DashboardSidebar have gap reports. Sort is routed `extend` of SortPillGroup (0.74).
- /games has pagination (GamesPager, 44px).
- On phones, search is on the page, outside the drawer (phone-01).
- Filter rows and tree leaves are 8px apart.
- The desktop sidebar scrolls on its own.
- SortButtons takes an `options` prop.
- The dashboard search matches the /games search.
- The CatalogShell buttons use `buttonClasses`.
- A star that fails to save shows a visible "Not saved".
- A failed tree read says so.
- The builds badge is neutral.
- Records:
  - the scope report was re-run (scope-2);
  - there are glance tests for /sessions and the dashboard;
  - AC1–AC14 have evidence;
  - the stars question is answered.
- Font weights are only 500, 700 and 800.
- The design index lists DashboardSidebar, and GFE-SHELL owns the dashboard code path.

## Blockers
1. **Components not approved.** All 10 verification reports are `awaiting-reviewer`. Only the human designer can close this.
2. **No `dynamicBehavior`** for CriticalFlag and GroupingFields. TitleGroup (grid only) and CatalogTree (no narrowest or 200% case) are thin.

## Major
- **The platform filter is case-sensitive in the UI.** A `?platform=msn` link left "MSN 5" unticked, added a phantom "msn 0" row, and the chip read "msn" (desktop-03). The cause is exact-string matching (`GameFilterPanel.tsx`, `lib/game-search.ts`).
- **A collapsed title group is pinned first but shows no star** (desktop-00, phone-01; `TitleGroup.tsx`).
- **The 200% text case isn't evidenced.** `phone320-text200-cards.png` and `-list.png` were the same file, and neither showed a card.
- **SortButtons hard-codes its copy** (the "Sort" label and the pinning note).
- **The critical flag and the dashboard's sentiment label disagree.** PopopoP has a red "!", but its dashboard says "Sentiment: Mixed" at 55% negative. That label is GFE-SHELL's.

## Minor
- No task time estimates.
- AC6 had `linkedTask: "T3"`; it should be `"T4"`.
- The verification artifact's version in the index was still 2.
- AC11 cited desktop-03, which shows no pinning.

## Needs a human
- The human designer has to sign, or return, the 10 component verification reports.
- The GFE-SHELL owner has to fix the header overlap at 200% text.
- The author should confirm one ordering: under the Critical sort, starred games that aren't critical still come ahead of critical ones.

---

## Design lead's response (commit `2e72dde`, patch now 6 commits)

Fixed:
- **Platform case.**
  - Added `sameFilterValue` (`lib/game-search.ts`), used by `toggleGameFilter`, the panel's selection and stale-value checks, and the chip label.
  - A `?platform=msn` link now ticks MSN, shows no phantom row, and the chip reads "MSN" (desktop-03, retaken).
  - Regression tests added in `game-filter-panel.test.tsx` and `game-sort-helpers.test.ts`.
- **Title-group star.**
  - TitleGroup shows GameCard's static star when any version has a starred build (desktop-00, retaken).
- **200% evidence.**
  - Retook the screenshots full-page at a 200% root font size. The five images are now distinct.
  - Measured per surface in `design-output.yaml` → `mobileCheck.textScale200`:
    - cards, list and drawer: 0 overflowing elements;
    - sessions: the table scrolls inside its own scroller;
    - dashboard: one GFE-SHELL button ("Re-analyze feedback").
- **SortButtons copy.** It now takes `label` and `note` props, with the current strings as defaults.
- **Records.**
  - `dynamicBehavior` filled in for CriticalFlag, GroupingFields, TitleGroup and CatalogTree.
  - AC6 now links to T4.
  - The index lists the verification artifact as version 3.
  - AC11 evidence now cites desktop-00 and desktop-05.
  - Task time estimates added (`design-output.yaml` → `taskTimes`).
- **Sentiment label.** The disagreement is flagged to GFE-SHELL in `design-index.yaml`.

Left for people: the component sign-off, the GFE-SHELL header, and the Critical-vs-starred ordering question.

Verified after the fixes:
- frontend: 1757 tests, tsc and eslint clean, story coverage OK (106 components);
- `flow_check`: OK;
- edge-case sweep: COMPLETE;
- harness: brief, scope, flow and design pass.
