# GFE-REVIEW standalone design audit (/sessions/[id])

Independent audit by the agent's `design-critic` persona (read-only; code, screenshots in `../screenshots/before/`, `../measurements-before.json`).
Standalone mode: missing briefs, flows and records are backfill, not findings. The seeded session is empty, so the populated states were audited from code.

**overallVerdict: blocker**

**Passes:** the delete confirm dialog (focus trap, Cancel gets default focus, Escape), the stall and failure notices, signals shown with text plus colour, reduced motion, and the back link.

## Blockers
1. **Tap targets under 44px** (`VideoReviewer.tsx`):
   - seek slider 20px (:443);
   - Play, Mute and Full screen 32px (:522, :538, :547);
   - moment chips 32px (:581);
   - BackLink 31px;
   - Delete trigger (sm).
   - **[mechanical]**
2. **Font sizes off the scale:** 11, 11.5 and 10.5px (`VideoReviewer.tsx`), and 14px (`text-sm`; `PlayerLoadNotice.tsx:56`). **[mechanical]**
3. **Spacing off the scale:** `gap-2.5`, `space-y-3.5`, `px-2.5`, `2px 6px` and `pt-0.5`. **[mechanical]**
4. **Raw colour and radii.**
   - `background: 'black'`.
   - `5px` and `1px` radii.
   - `var(--radius-md)` is undefined, so "Try again" renders square.
   - **[mechanical]**
5. **The " / total" timecode** is about 4.2:1 over a bright frame (calculated). **[mechanical]**

## Major
1. **No token focus ring** on the slider, transport buttons and chips. **[mechanical]**
2. **No hover state** on the transport buttons and chips. **[mechanical]**
3. **No loading indicator:** while loading, the player shows a black frame reading "0:00 / 0:00". **[mechanical]**
4. **Long email, answer text and chip labels can overflow** at 320px. **[mechanical]**
5. **The no-recording text touches its border** at 200% text. **[mechanical]**
6. **Marker colours use `--color-negative` and `--color-mixed`** for neutral moments. Fix: `--color-chart-1..4`. **[mechanical]**
7. **No `<h1>` and no game name,** so the page's purpose isn't clear at a glance. **[decision]**, the wording.
8. **Reviewer copy is hard-coded inside VideoReviewer.** **[decision]**

## Minor
1. **Font weight 600** in PlayerLoadNotice. **[mechanical]**
2. **Unicode glyphs (‖ ▶ ♪ ✕ ⛶)** instead of inline SVG; ✕ for "muted" reads as "close". **[mechanical]**
3. **The loading skeleton doesn't match the page layout.** **[mechanical]**
4. **The design index is missing VideoReviewer and the other components.** **[mechanical]**

## Needs a human
- **Major 7:** the heading's content.
- **Major 8:** where the reviewer copy lives.
- **Transport sizing:** 44px controls make the overlay bar taller. Choose an auto-hiding overlay or a bar below the video.
