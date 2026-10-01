# The Design System Agent, installed in the Game Feedback Engine

`design-agent-install.patch` is 5 commits for atari-game-feedback-engine. Apply it after
`../game-sort/game-sort.patch` and `../existing-pages/existing-pages.patch`:

```
git am design-agent-run/game-sort/game-sort.patch \
       design-agent-run/existing-pages/existing-pages.patch \
       design-agent-run/install/design-agent-install.patch
pip install pyyaml jsonschema   # the hooks and tools
npm i -g playwright             # only for tools/screenshots.py
```

## What it adds to the repo
- **The agent:** installed with its own `install.sh`, first the 30 Sep version and then the 1 Oct update:
  - `.claude/skills/design-agent/` (the skill, critic and references);
  - `.claude/design-agent/` (tools, schemas, templates);
  - `.claude/agents/design-lead.md` and `.claude/agents/design-critic.md`.
- **Hooks** in `.claude/settings.json`:
  - At session start, it shows every design's stage.
  - Before the first edit to a UI file, it shows the design that owns it and that
    design's decisions.
  - After each edit, it sends back off-token values.
- **`.gitignore`:** tracks these files, as it already does for `.claude/gates/`, so
  every checkout and worktree gets them.
- **Design files at the repo root:** `design-system-manifest.yaml` (Fuji) and
  `design-index.yaml`.
  - Every one of the 133 UI files now has an owning design. There are nine designs,
    including `GFE-FUJI` for the primitives and global styles.
- **`CLAUDE.md`:** starts with the manifest's version stamp and ends with the generated
  Fuji section. The team's guide in between is unchanged.
- **`docs/design/agent/`:** the design records. The index points here.

## What the whole-system run found and fixed
- **Consistency check across every UI file:** 6px, 10px and 2px values moved to the
  4px scale, and weight 600 (not a Fuji weight) became 700. About 60 edits.
- **Screenshot tool at every width:**
  - At 768px the admin header ran 128px off the screen. The full nav now starts at
    1024px, and the menu covers the widths below that.
  - The menu icon's X animation was protected from the spacing sweep.
- **Verified:**
  - 1774 frontend tests, tsc and eslint clean, story coverage OK.
  - No page scrolls sideways at 320, 390, 768, 1024 or 1440px.
  - The hooks were exercised: before an edit, a GameCard edit is shown GFE-SORT's
    decisions; after an edit, `gap-[7px]` and a raw hex colour are caught.

## Left for the design-system owner
- **Consistency findings that remain** (`harness.py status`, one to five per design).
  All are on-scale values that differ between kinds of element, for example list rows
  in the sidebar tree versus admin tables, and bold `<p>` titles versus body text.
  Closing them means adding spacing roles and text styles to the manifest; that's the
  owner's call.
- **Card padding:** 16px on phones versus the 24px role. This depends on whether spacing
  should grow with text size.
- **Compatibility is MINIMUM, not Optimal:**
  - the focus ring contrast is 1.75:1;
  - the secondary accent is the same colour as info;
  - there's no ghost Button, Breadcrumb, Checkbox or RadioGroup component;
  - `Select` is proposed.

## The 1 Oct agent update (commits 4 and 5)

The update adds:
- checks against common AI design tropes;
- "say little" and "say once" checks, with the 3-3-3 rule measured;
- a limit of five pieces of information per card, plus findable navigation;
- rules for persistent bars;
- the Atari brand guidelines;
- `purpose_check.py`, `brand_check.py` and a 22-item critic.

Aligned to it:
- **Re-installed.** The hooks are unchanged.
- **Brand:** `brand/` holds the Atari Brand Guidelines V1.1 profile. It's declared
  `when-declared`, because Fuji (mint, Archivo) is not the Atari palette (Atari Red,
  Atari 1972 / Poppins). Switching it to `always` would be a rebrand, so that's the
  owner's call.
- **Manifest:** `contentPolicy` and `antiAiDesign` set to the agent's defaults.
- **`CLAUDE.md`:** the Fuji section was regenerated with `fill_claude_md.py` (in this folder).
- **Header:** the email, role badge and Admin/Questions link moved into an Account
  menu. The header bar holds only the logo, navigation and controls.
- **Pills:** selected pills are a mint tint, not a solid fill. Solid mint is reserved
  for the one primary action.
- **Sidebar:** the explanatory note is gone, since the sidebar is persistent chrome.
- **Verified:**
  - 1775 frontend tests pass; tsc and eslint are clean.
  - Every page was re-rendered with the new tool. The ambient-information findings
    went 19 → 0.

### Tool issues for the agent's author (seen on the real app)
- **Navigation in a closed drawer or nav:** every list inside a hidden nav is reported
  as "hidden options with no labelled control", even when the nav's own opener (an
  `aria-controls` / `aria-expanded` button) is found. That's about 90 findings here.
- **Primary-action detection:** it ignores alpha, so a 15% mint tint counts as primary.
  It also counts every `button[type=submit]` as primary, such as each row's Save and
  Remove.
- **Touch targets:** these are measured on the element, not the hit area. Affected:
  - an `sr-only` input inside a 44px label or pill;
  - a checkbox or switch inside a 44px `<label>`;
  - a stretched-link (`::after inset-0`) title.
- **Fluid `clamp()` headings** are reported as two sizes.
- **"Said twice":** a per-card link repeated on every card ("How to play & give
  feedback →") counts as repetition, and so does a date in a meta line ("3 figures").
- **Overflow at a breakpoint:** it's recorded in the screenshot set but not reported as a
  finding. The 768px header overflow was found by reading `overflowPx`.

### Left for a person (new rules, not changed)
- **Copy over 30 words:** about 30 text blocks, mostly admin help text and feature-flag
  descriptions. Shortening copy changes its meaning.
- **Primary action far down long forms:** Add game, Edit game, Add build, the feedback
  form and admin questions. These are the layout decisions from the critic review.
- **Session detail has no h1:** its wording is still open.
- **The dashboard says "No feedback or video yet" twice:** once in the header and once
  in the KPI row. This is part of the duplicate-stats decision.
