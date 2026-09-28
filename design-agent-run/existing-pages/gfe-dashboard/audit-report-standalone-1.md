# GFE-DASHBOARD standalone design audit (/games/[gameId]/dashboard)

Independent audit by the agent's `design-critic` persona (read-only; code, screenshots in `../screenshots/before/`, `../measurements-before.json`).
Standalone mode: missing briefs, flows and records are backfill, not findings. The catalogue sidebar (GFE-SORT) and the header are excluded.

**overallVerdict: blocker**

## Blockers
1. **Touch targets under 44px.**
   - Analyze feedback and Analyze videos (sm, 31px).
   - Download feedback (CSV) (md, 38px).
   - Build and Tester selects (40px).
   - Tabs (about 38px).
   - **[mechanical]**
2. **Sideways scroll at 320px with 200% text** (confirmed): "Analyze feedback" and "Download feedback (CSV)" spill out.
   - Cause: Button `whitespace-nowrap`, plus `items-end` on the action columns.
   - Fix: wrap the buttons, and `items-stretch sm:items-end`. **[mechanical]**
3. **Font sizes off the scale:** 17px and 24px (`DashboardHeader.tsx:173,215`) and 11.2px (`EnrichmentAction`, `RunVisionAnalysis`, `buttonClasses` sm). **[mechanical]**
4. **Spacing off the scale:** `mt-3.5`, `mt-0.5`, `gap-1.5`/`mt-1.5`, `gap-3.5`, `py-2.5` and `py-1.5` across the header, KPIs, panels and tabs. **[mechanical]**

## Major
5. **"Sentiment: Mixed" (amber) over a 55%-negative split,** while the sidebar shows the critical "!".
   - The header uses the average score (±0.15); the flag uses 40% negative over 5 or more reviews.
   - **[decision]**
6. **The secondary Button turns its text mint on hover,** a brand exclusion (`buttonClasses.ts:33`). Fix: `--color-accent-text`. **[mechanical]**
7. **Tabs don't change on hover.** **[mechanical]**
8. **The select value is clipped** at 200% text. **[mechanical]**
9. **"Analyze feedback" shows only "Starting…",** with no spinner. **[mechanical]**
10. **One metric, two labels:** "Video coverage" and "Sessions with video". **[decision]**
11. **The monogram tile is 74px fixed;** `maxFixedSizePx` is 64. **[mechanical]**

## Minor
12. **Empty states name a "Run AI analysis" button** that doesn't exist; it's "Analyze feedback". **[mechanical]**
13. **Header actions are misaligned on phones.** **[mechanical]**
14. **At 320px, the tab row hides tabs off-screen** with no hint that more exist. **[decision]**
15. **The header and the Executive tab repeat the same stats.** **[decision]**

**Passes:** tab semantics and keyboard support, state never shown by colour alone, no raw hex in markup.

## Needs a human
- **#5, sentiment vs the critical flag.** Choose one:
  - (a) derive the header label from the negative share;
  - (b) show the CriticalFlag badge in the header;
  - (c) change the flag's rule. This changes GFE-SORT, so its owner has to agree.
- **Report vs KPI counts:** the AI narrative says "20 feedback entries" next to "Total feedback 0". Should a report that doesn't match the live counts show as stale?
- **#10, #14, #15:** metric wording, narrow-screen tabs, and which set of duplicate stats to drop.
- **Only the Executive tab was captured.** The other four tabs were checked from code only.
