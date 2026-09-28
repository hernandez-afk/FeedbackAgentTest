# GFE-IMPORTS standalone design audit (/imports, /games/[gameId]/imports)

Independent audit by the agent's `design-critic` persona (read-only; code, screenshots in `../screenshots/before/`, `../measurements-before.json`).
Standalone mode: missing briefs, flows and records are backfill, not findings.

**overallVerdict: blocker**

**Passes:** categories 1, 5, 6, 7 and 11, plus the confirm-before-destructive-action checks. The dialog traps and restores focus. Failed rows show a badge and text. A failed read shows an error Banner.

## Blockers
1. **Content overflows sideways at 320px with 200% text** (`games/[gameId]/imports/page.tsx:74-88`, game-imports-320-text200).
   - The header text block has no `min-w-0`.
   - "Everything" at h1 size is wider than the column.
   - The link is `whitespace-nowrap`.
   - Fix: add `min-w-0 break-words`, `overflow-wrap:anywhere` on the h1, and a wrapping link. **[mechanical]**
2. **Touch targets under 44px.**
   - Button `sm` (31px) and `md` (38px) are used across `ImportQueuePanel.tsx` and `ImportDialog.tsx`.
   - The "Import a corrected file" link (`PriorImportsList.tsx:92,139`).
   - Fix: `min-h-11` on the `sm` and `md` sizes; make the link `inline-flex min-h-11`. **[mechanical]**
3. **More than one accent-filled action per screen.**
   - The `utility` variant is accent-filled like `primary`.
   - Pick phase: Clear all, each row's Remove, and Import N items are all filled.
   - Done phase: Prior imports and See it in the dashboard are both filled.
   - Fix: make the non-commit actions `secondary`. **[mechanical]**

## Major
4. **The dialog panel can't scroll** (`ImportDialog.tsx:333`). Fix: `max-h-[calc(100dvh-2rem)] overflow-y-auto`. **[mechanical]**
5. **The upload shows only a text percentage** (`ImportQueuePanel.tsx:594-597`); the designed byte bar was never built. Fix: add a progressbar per sending row. **[mechanical]**
6. **Primary and utility hover are opacity-only.** **[mechanical]**
7. **The game select** uses `--color-surface`, not `--color-field`, and has no focus ring (`ImportQueuePanel.tsx:347`). **[mechanical]**
8. **Long game titles break the running-phase header** (`ImportQueuePanel.tsx:529-538`). **[mechanical]**
9. **The prior imports list has no pagination** (`PriorImportsList.tsx`, `backend/imports.py:950-957`). **[decision]**: it needs an API change.

## Minor
10. **EmptyState and drop-zone text squeezed** to one word per line at 200% text (stacked `px-6` inside `px-4`). **[mechanical]**
11. **Select placeholder cut off** at 200% text. **[mechanical]**
12. **The empty state uses `adp-h1`**, the same level as the page h1. Fix: `compact`. **[mechanical]**
13. **The inline "Add the game" link is 16px tall.** **[mechanical]**

## Needs a human
- #9: pagination strategy for prior imports.
- **"Nothing imported yet"** describes the client queue but reads as the game's history. Suggest "No files chosen yet". **[decision]**
- **Duplicate "Import something"** actions on an empty game-imports page. **[decision]**
- **Retrying a failed row** clears the whole queue. Should there be a per-row "Send again"? **[decision]**
- #2, #3 and #6 are fixes to the shared `buttonClasses.ts`: a design-system change.
