# The Design System Agent, installed in the Game Feedback Engine

`design-agent-install.patch` is 3 commits for atari-game-feedback-engine. Apply it after
`../game-sort/game-sort.patch` and `../existing-pages/existing-pages.patch`:

```
git am design-agent-run/game-sort/game-sort.patch \
       design-agent-run/existing-pages/existing-pages.patch \
       design-agent-run/install/design-agent-install.patch
pip install pyyaml jsonschema   # the hooks and tools
npm i -g playwright             # only for tools/screenshots.py
```

## What it adds to the repo
- **The agent:** installed with its own `install.sh` (the 30 Sep version):
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
