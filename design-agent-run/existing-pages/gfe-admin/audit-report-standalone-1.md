# GFE-ADMIN standalone design audit (/admin, /admin/questions)

Independent audit by the agent's `design-critic` persona (read-only; code, screenshots in `../screenshots/before/`, `../measurements-before.json`).
Standalone mode: missing briefs, flows and records are backfill, not findings. Categories 5, 6, 7 and 12 pass.

**overallVerdict: blocker**

## Blockers
1. **Two primary actions on /admin:** "Add user" and "Add studio" (`admin/page.tsx:512-513, 822, 851`). **[decision]**: which one is the page's primary.
2. **Touch targets under 44px:** 16 on /admin and 115 on /admin/questions.
   - `sm` buttons are 31px.
   - Checkboxes are 16px.
   - Reorder arrows are `h-6 w-7`.
   - The chip "×" is 20px.
   - Fix: 44px hit areas. **[mechanical]**
3. **Sideways scroll at 320px with 200% text.**
   - /admin: +125px, from the nowrap "Manage feedback questions →" link.
   - /admin/questions: +186px, from the "Create question" lg button and the "Full catalog (all questions)" select.
   - **[mechanical]**
4. **Inline `fontSize: 0.7rem`** (`QuestionAuthoringForm.tsx:783`). **[mechanical]**
5. **Spacing off the scale:** `py-2.5`, `gap-0.5` and `mt-0.5`. **[mechanical]**
6. **Raw `bg-white`** on the hand-built flag switch (`admin/page.tsx:914`). **[mechanical]**
7. **The required "*"** uses `--color-negative` (3.08:1). Fix: `--color-negative-text`. **[mechanical]**

## Major
1. **The flag switch copies Toggle,** and the selects are hand-rolled three different ways. Fix: `Toggle` and one NativeSelect class. **[mechanical]**
2. **The question-form selects are 26px** with text against the edge, while the page selects are 44px. **[mechanical]**
3. **/admin/questions never shows its `?error=` / `?ok=` results.** Suppress and retire succeed or fail silently. Fix: render the Banners as /admin does. **[mechanical]**
4. **Remove user runs at once,** with no confirm or undo (`admin/page.tsx:732-737`). **[decision]**
5. **The chip remove "×"** has no visible focus. **[mechanical]**
6. **Primary hover is opacity-only** (primitive). **[mechanical]**
7. **Reorder arrows are 2px apart;** the minimum spacing is 8px. **[mechanical]**
8. **Save and Remove look alike on phone.** **[decision]**

## Minor
1. **Truncated email, question wording and studio select,** with no way to see the full text. **[mechanical]**
2. **`aria-label="Remove suppression"`** doesn't name the scope. **[mechanical]**
3. **The suppression chip shows a raw build id** instead of the build label. **[mechanical]**
4. **The questions list isn't paginated** (about 30 rows today). **[decision]**

## Needs a human
- **Type scale conflict:** sm button text (11.2px), md (13px) and the kicker (11px) aren't on `typography.scale.steps`, but they're defined in approved primitives.
- **Primary 1:** Add user or Add studio as the page's one primary action.
- **Major 4:** a confirm or an undo for Remove user.
- **Major 8:** how to separate Save and Remove.
- **Minor 4:** pagination for the questions list.
- **Flag toggles** apply immediately with no pending state. Should they get one?
- **Retire** has no confirm; Activate restores it. Is that enough?
