# Critic pass (after fixes)

One pass with the updated agent's `skills/design-agent/critic.md`. The critic saw each page's
tool output and its two 320px screenshots. Pages: `screenshot-sets/after/`.

| Area | Verdict | What drove it |
|---|---|---|
| GFE-SHELL | major-issues | No primary sign-in action; h1 clipped at 200% |
| GFE-CAPTURE | major-issues | Unavailable-game state is a dead end below a long brief; 1-5 scale wraps at 320; long form |
| GFE-REVIEW | minor-issues | Tall empty "no recording" box; static meta chips look like buttons |
| GFE-DASHBOARD | major-issues | No primary action; five filters before the tabs; repeated empty states |
| GFE-CATALOG-ADMIN | major-issues | Visibility control differs between new and edit; field order; mint drop zone differs from others |
| GFE-IMPORTS | major-issues | Duplicate "Import something"; game picker below the drop zone |
| GFE-ADMIN | blocker | Remove user had no confirm; very long flag and question lists |
| GFE-SORT | blocker | Tool finding on title links (a tool limitation, see below); sessions table on phones; many card buttons |

## Fixed after the critique (commit `3c59542`)
- **Remove user** confirms first, with a message naming the email. The ADMIN blocker is cleared.
- **Continue with Google** is primary on /login, and the h1 wraps at 200% text.
- **Analyze feedback** is primary on the dashboard when there's no current report.
- On **/feedback**, the card uses p-4 on phones, so the 1-5 scale fits on one line at 320px.

## The critic's own errors (checked against the code)
- **GFE-SORT title links:** the "blocker" is a stretched link. `after:absolute after:inset-0`
  makes the whole card the target, so this is a tool limitation.
- **"v1" 40×44:** read from a screenshot taken before the `min-w-11` fix in `95917d9`.
- **"Thankyou!":** the code says "Thank you!". This was a misreading of the screenshot.
- **Admin checkboxes:** each one is inside a `min-h-11` label.

## Tool limitations the critic confirmed (for the agent's author)
- `.sr-only` inputs and labels are reported as tiny or clipped.
- A checkbox or switch inside a 44px `<label>` is measured by its box, not by the label.
- Stretched-link titles are measured by the link box, not by the card they cover.
- Fluid `clamp()` headings are reported as two sizes.

## For a person to decide (layout and structure; not changed)
- **Capture:** put the play action and the unavailable state above the brief; chunk the long feedback form.
- **Dashboard:** put the filters in a Collapsible; add a scroll cue on the tabs; show one empty state when there's no feedback.
- **Catalog admin:** use one visibility control and one label; required fields first; one drop-zone style everywhere.
- **Imports:** choose the game first, then drop files; one "Import something".
- **Admin:** one-line flag summaries (or split into tabs); paginate or group questions; keep Retire apart from Edit.
- **Games:** one primary per card versus one primary per screen; move secondary card actions into an overflow.
- **Sessions:** cards instead of the table on phones; collapse the filters.
- **Design system:** should page gutters and card padding grow with text size? (They're rem-based now.)
- **Design system:** button size mixing (sm/md/lg on one screen).
