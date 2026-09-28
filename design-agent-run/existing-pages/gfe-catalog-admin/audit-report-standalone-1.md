# GFE-CATALOG-ADMIN standalone design audit (/games/new, /games/[id]/edit, /builds/new)

Independent audit by the agent's `design-critic` persona (read-only; code, screenshots in `../screenshots/before/`, `../measurements-before.json`).
Standalone mode: missing briefs, flows and records are backfill, not findings.

**overallVerdict: blocker**

**Scope:** `AddCatalogForm.tsx`, `EditGameForm.tsx`, `AddBuildForm.tsx` and the three pages. GroupingFields (GFE-SORT) and the header are excluded.

## Blockers
1. **The Studio and Game native selects** are 26px tall with no dropdown arrow (`AddCatalogForm.tsx:107-109`, `AddBuildForm.tsx:88`).
   - Cause: `selectBase = inputClasses() + ' appearance-none'` drops the padding and the arrow.
   - Fix: use the NativeSelect pattern (`SessionsFilters.tsx` `SELECT_CLASS`), `min-h-11`, and an inline-svg chevron. **[mechanical]**
2. **Every text input and textarea is 42px** (Input primitive `px-3 py-2`). Fix: `min-h-11` in `inputClasses` / `Input.tsx`. **[mechanical]**
3. **The "← Cancel" link is 18px tall** (`AddCatalogForm.tsx:375-387`, `AddBuildForm.tsx:511-522`, EditGameForm). **[mechanical]**
4. **At 320px with 200% text, the submit button runs off the edge.**
   - Cause: Button `whitespace-nowrap` inside a non-wrapping footer.
   - Fix: `flex-wrap` on the footer; `whitespace-normal w-full sm:w-auto` on the submit. **[mechanical]**
5. **Off-token values.**
   - Spacing: `gap-2.5`, `p-3` + `mt-0.5`, `px-2.5`, `gap-1.5`.
   - Colour: raw `text-white`.
   - Motion: `duration-300`.
   - Radius: `--radius-xl`, which isn't a manifest radius, on the form cards.
   - Fix: 8/12/4px, `--color-accent-ink`, `--dur-state`, `--radius-lg`. **[mechanical]**

## Major
6. **The form cards rebuild the Card primitive inline.** **[mechanical]**
7. **At 320px with 200% text,** the card's `p-6` inside the page padding leaves about an 80px column: labels wrap one word per line and placeholders are cut off. Fix: `p-4 sm:p-6`. **[mechanical]**
8. **Font weight 600,** on labels and the step row. Fix: 700/500. **[mechanical]**
9. **/games/new has 13 fields in one ungrouped column,** over `maxInlineInputs` 7. The primary action is about five phone screens down. **[decision]**
10. **Org visibility looks different on new and edit:** a mint checkbox panel, "Visible to all testers (org-wide)", versus a Toggle, "Visible to all studios". **[decision]**, the label and the default.

## Minor
11. **Form labels use Archivo,** but the manifest's `formLabel` role says mono. **[decision]**, see Needs a human.
12. **The visibility panel's mint tint** sits beside the mint primary. Fix: `--color-surface-2` with a hair border. **[mechanical]**

## Needs a human
1. **Form-label typeface:** the manifest says mono Label; DESIGN_SYSTEM.md uses Label for status chips. Decide which is right, then regenerate CLAUDE.md.
2. **"Create game & upload"** shows even when no zip is attached. Should the label depend on the zip?
3. **Three ways to make a game playable** (zip, Play URL, Hosted game link). The two URL fields look alike: merge them, or separate them clearly?
4. **Grouping or deferring fields (#9),** and settling the visibility control (#10).

**Passes:** every field is labelled, required fields have a text backup, focus rings are visible, loading states exist (`aria-busy`), and Banners are used correctly.
