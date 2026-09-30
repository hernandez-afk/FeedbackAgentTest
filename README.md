# Design System Agent × Game Feedback Engine

A test run of the [Design System Agent](https://github.com/hernandez-afk/Design-System-Agent) on the
[Game Feedback Engine](https://github.com/Atari-Inc/atari-game-feedback-engine). The input was the page brief
*"Modified Game Sort on Game Feedback Engine"* plus Andreas Beijer's sidebar design. The agent's loop ran three times:
brief → scope → flow → design → audit → build.

**Clickable prototype:** `design-agent-run/game-sort/prototype.html`. It's also published as a private artifact: https://claude.ai/artifact/Pu7DLi3qRM54iodmC3njTA

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
    ticket-brief.yaml            optimized brief; edge-case sweep COMPLETE (9 entities, 12/12 lenses)
    user-flow.yaml               flow_check.py: OK (7 core tasks)
    scope-overlap-report.yaml    re-run against the index: the dashboard is shared with GFE-SHELL
    component-gap-report.yaml    reuse check; new components are "proposed"
    component-verification-reports.yaml   per-component states + dynamic behaviour (awaiting a human designer)
    design-output.yaml           revision 3: decisions, glance tests, mobile check, 14 acceptance criteria with evidence
    audit-report*.md             the independent critic's audits
    screenshots/                 the real app on seeded data: 1440, 390 and 320 px, and 320 px at 200% text
    prototype.html               clickable prototype on sample data
    game-sort.patch              the implementation: 6 commits for atari-game-feedback-engine
```

Apply the implementation from an `atari-game-feedback-engine` checkout:
`git am design-agent-run/game-sort/game-sort.patch`, then `alembic upgrade head`.

## What was built

**Everywhere in the catalogue:** Andreas's sidebar. It's beside the games list and beside every game dashboard. On phones it opens as a drawer.
- **Search**
- **Sort:** A to Z, Newest, Active (most sessions in 30 days), Critical
- **Filters** (games list only): Platform, Project, Studio, each with counts
- **Starred builds:** a list of the builds you've starred.
- **Browse tree:** Project → Platform → Title → game. A game with a starred build shows a ⭐. Reviewers also see a red **!** on games whose reviews have turned overly negative.

**Stars (on builds)**
- Star any build with the ☆ beside its **Continue** button, or on its row on /sessions.
- Games with a starred build are always listed first on /games, whatever the sort.
- Sessions on a starred build are always listed first on /sessions.
- Stars are private to each user.

**Games page**
- **Cards / List** view.
- Pages of 50 games, with Previous / Next.
- Removable filter chips.
- Versions of one title (e.g. Asteroids → Asteroids Arezion (MSN), Asteroids Classic Azerion (MSN)) collapse into one entry that expands.

**Add / edit game:** new **Project** and **Title** fields. They suggest existing names, and typing a new name creates it.

**Sessions page:** a **Platform** filter, and a ☆ on each row.

**Rules the author set**
- "MSN" and "msn" are one platform.
- Developer is the studio.
- Project is what the game is intended for.

**Critical warning:** a game is flagged when its latest sentiment report is at least 40% negative across at least 5 reviews. You confirmed the 40%. Only reviewers see it.

**Backend** (Postgres, one migration)
- New tables: `project`, `franchise` (shown as "Title") and `build_favorite`.
- New and extended routes:
  - `GET /api/games/navigation`
  - `GET /api/games/facets` (adds projects)
  - `PUT` / `DELETE /api/games/{game_id}/builds/{build_id}/favorite`
  - new filters and sorts on `GET /api/games`; starred builds pin first there and on `GET /api/sessions`

**Verified locally**
- Frontend: 1757 tests, tsc and eslint clean, story coverage OK.
- At 320px with text at 200%, nothing inside the page body overflows (screenshots `phone320-text200-*`).
- Backend: 2203 pytest tests passed; ruff SAST, mypy, a single migration head, and the downgrade guards.

## Existing pages

The agent also ran over every page that shipped before it:
- **Records:** `design-agent-run/existing-pages/` holds the audits, the screenshots and `existing-pages.patch` (12 commits, applied after `game-sort.patch`).
- **Result:** tool blockers across 14 pages went from 63 to 18, and all 18 are tool limitations.
- **Critic pass:** its blocker is fixed. The layout decisions it raised are in `critique-after.md`.
- **Gallery:** before and after screenshots of every page: https://claude.ai/artifact/HhMFv9E7gTMzNducpZdjUz

## Still with the author

- **Critical sort vs stars:** under the Critical sort, games with a starred build still come first, even when they aren't critical ("shown first … whatever the sort"). Say if Critical should override stars.

- **Component approval:** the new components need a human designer's sign-off (`component-verification-reports.yaml`).
- **Fuji gaps found by the agent:**
  - The mint focus ring is only 1.75:1 against the page background. WCAG AA needs 3:1.
  - There's no Checkbox or Breadcrumb component.
- **Header at 200% text:** the site header nav (pre-existing, GFE-SHELL) overflows at 320px. Flagged in the design index for its owner, along with the dashboard's "Sentiment: Mixed" label, which disagrees with the critical flag.
