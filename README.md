# Design System Agent × Game Feedback Engine

A test run of the [Design System Agent](https://github.com/hernandez-afk/Design-System-Agent) on the
[Game Feedback Engine](https://github.com/Atari-Inc/atari-game-feedback-engine). The input was the page brief
*"Modified Game Sort on Game Feedback Engine"* plus Andreas Beijer's sidebar design. The agent's loop ran twice:
brief → scope → flow → design → audit → build.

**Clickable prototype:** `design-agent-run/game-sort/prototype.html`. It's also published as a private artifact.

## What's here

```
design-agent-run/
  design-system/                 Fuji (the GFE design system) as the agent sees it
    design-system-manifest.yaml  check_compatibility: MINIMUM (gaps listed below)
    CLAUDE.md                    generated project context (version-stamped)
    design-index.yaml            GFE-SORT registered: surfaces, codePaths, navigation
  game-sort/
    page-brief.md                the PDF brief, verbatim, plus the author's round-2 answers
    reference-andreas-beijer/    the reference design the author supplied
    brief-optimization-report.yaml   every change to the brief; answers recorded
    ticket-brief.yaml            optimized brief; edge-case sweep COMPLETE (9 entities, 13/13 lenses)
    scope-overlap-report.yaml    scope check
    user-flow.yaml               flow_check.py: OK (7 core tasks)
    component-gap-report.yaml    reuse check; new components are "proposed"
    component-verification-reports.yaml   per-component states + dynamic behaviour (awaiting a human designer)
    design-output.yaml           decisions, 3-3-3 walk, mobile check, 14 acceptance criteria
    audit-report*.md             the independent critic's audits
    screenshots/                 the real app on seeded data: 1440, 390 and 320 px
    prototype.html               clickable prototype on sample data
    game-sort.patch              the implementation: 3 commits for atari-game-feedback-engine
```

Apply the implementation from an `atari-game-feedback-engine` checkout:
`git am design-agent-run/game-sort/game-sort.patch`, then `alembic upgrade head`.

## What was built

**Everywhere in the catalogue:** Andreas's sidebar. It's beside the games list and beside every game dashboard. On phones it opens as a drawer.
- **Search**
- **Sort:** A to Z, Newest, Active (most sessions in 30 days), Starred, Critical
- **Filters** (games list only): Platform, Project, Studio, each with counts
- **Browse tree:** Project → Platform → Title → game. Each game has a ⭐ and, for reviewers, a red **!** when its reviews have turned overly negative.

**Games page**
- **Cards / List** view.
- Removable filter chips.
- Versions of one title (e.g. Asteroids → Asteroids Arezion (MSN), Asteroids Classic Azerion (MSN)) collapse into one entry that expands.

**Add / edit game:** new **Project** and **Title** fields. They suggest existing names, and typing a new name creates it.

**Sessions page:** a **Platform** filter.

**Rules the author set**
- "MSN" and "msn" are one platform.
- Developer is the studio.
- Project is what the game is intended for.

**Critical warning:** the game's latest sentiment report is at least 40% negative across at least 5 reviews. Only reviewers see it.

**Backend** (Postgres, one migration)
- New tables: `project`, `franchise` (shown as "Title") and `game_favorite`.
- New and extended routes:
  - `GET /api/games/navigation`
  - `GET /api/games/facets` (adds projects)
  - `PUT` / `DELETE /api/games/{id}/favorite`
  - new filters and sorts on `GET /api/games`

**Verified locally**
- Frontend: 1751 tests, tsc and eslint clean, story coverage OK.
- Backend: pytest, ruff SAST, mypy, a single migration head, and the downgrade guards.

## Still with the author

- **Stars on games or builds?** Stars are on games, as in Andreas's tree. The criterion says "game builds".
- **Critical threshold:** 40% negative across 5+ reviews is a starting point. Tell me if you want different numbers.
- **Component approval:** the new components need a human designer's sign-off (`component-verification-reports.yaml`).
- **Fuji gaps found by the agent:**
  - The mint focus ring is only 1.75:1 against the page background. WCAG AA needs 3:1.
  - There's no Checkbox or Breadcrumb component.
  - Card-view `sm` buttons are about 28px tall, under the 44px touch-target minimum.
