# Design System Agent × Game Feedback Engine

A test run of the [Design System Agent](https://github.com/hernandez-afk/Design-System-Agent) against the
[Game Feedback Engine](https://github.com/Atari-Inc/atari-game-feedback-engine). The input was the page brief
*"Modified Game Sort on Game Feedback Engine"*. The run follows the agent's harness end to end:
brief → scope → flow → design → audit → build.

## What's here

```
design-agent-run/
  design-system/                 the agent's view of Fuji (the GFE design system)
    design-system-manifest.yaml  Fuji tokens + components as an agent manifest (check_compatibility: MINIMUM)
    CLAUDE.md                    generated project context (version-stamped)
    design-index.yaml            GFE-SORT registered, with codePaths
  game-sort/
    page-brief.md                the PDF brief, transcribed verbatim
    brief-optimization-report.yaml   every change to the brief, conflicts, open questions
    ticket-brief.yaml            optimized brief + edge-case sweep (13/13 lenses)
    scope-overlap-report.yaml    scope check (new project, shared patterns inherited)
    user-flow.yaml               flow_check.py: OK
    component-gap-report.yaml    reuse check; 2 proposed components
    design-output.yaml           decisions, 3-3-3 walk, mobile check, acceptance results
    audit-report.md              independent critic's audit (design-critic persona)
    screenshots/                 real app, seeded data: 1440, 390 and 320 px
    game-sort.patch              the implementation, as a git patch for atari-game-feedback-engine
```

Apply the implementation: `git am design-agent-run/game-sort/game-sort.patch`, run from an
`atari-game-feedback-engine` checkout.

## What was built (in the patch)

**/games**
- Filter panel with **Platform** and **Studio** filters, each option showing its game count.
  - From 1024px up it's a left column beside the games.
  - On phones it's collapsed behind a "Filters (n)" button.
- Every active filter shows as a removable chip, plus a "Clear filters" link.
- A **Cards / List** switch. The list view has one compact row per game with title, platform, studio, date added, builds, and View dashboard / Import documents / Edit.
- A **Most active** sort: games with the most sessions in the last 30 days come first.
- The game card's header line now shows platform · studio · date added.
- Filters, sort and view are all in the URL, so a filtered view can be shared as a link.

**/sessions**
- A **Platform** dropdown that works together with the existing Game / Build / Status / Severity filters.

**Backend** (all additive)
- `GET /api/games` accepts `platform` and `studio` filters and `sort=activity`, and returns `studio_name` and `created_at`.
- New `GET /api/games/facets` returns the filter options with counts, limited to what the caller is allowed to see.
- `GET /api/sessions` accepts `platform`.

**Verified locally**
- Backend: 2194 tests passed, ruff SAST and mypy clean. That includes 15 new tests.
- Frontend: 1743 tests passed, tsc and eslint clean, story coverage OK. That includes 5 new test files.

## Waiting on the brief author

The agent's gates need a person at a few points. These are open:

1. **Platform names are free text.** "MSN" and "msn" show up as two options. Should platforms be a managed list, or grouped ignoring case?
2. **"Game developer"**: is that the studio (already a filter), a person, or an outside developer company?
3. **"Project"**: is that a franchise, a release programme (e.g. Atari Recharged), or a code name?
4. **"Recently got the most responses"**: is 30 days the right window, and is `/games` the right place for it?
5. **"From Andreas Beijer"**: is there a design file to stay consistent with?

**Separate brief needed:** developer, project, and the title → product → product version
hierarchy (e.g. Asteroids → Asteroids Arezion → MSN) don't exist in the data model yet. The edge-case
sweep splits them into their own brief, *Catalogue metadata*. The filter panel is built so each one
becomes one more filter group once the data exists.

**Findings about Fuji itself** (from `check_compatibility.py`):
- The mint focus ring is only 1.75:1 against the page background. WCAG AA needs 3:1.
- There is no Checkbox or Breadcrumb component.
- Buttons at size `sm` are about 28px tall, under the 44px touch-target minimum.
