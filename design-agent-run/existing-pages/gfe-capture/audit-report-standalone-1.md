# GFE-CAPTURE standalone design audit (tester capture flow)

Independent audit by the agent's `design-critic` persona (read-only; code, screenshots in `../screenshots/before/`, `../measurements-before.json`).
Standalone mode: missing briefs, flows and records are backfill, not findings.

**Evidence gaps:**
- The play screen wasn't captured: the seeded game showed "not available".
- The uploading, complete and error states weren't captured.
- /brief was audited from code only.

**overallVerdict: blocker**

## Blockers
1. **Touch targets under 44px across the flow.**
   - Button `md` is 38px: Continue, Continue to play, Continue without video, Submit for another game, Done.
   - Button `sm` is 31px: Attach screenshots, Retry.
   - Scale and choice pills are about 32px tall and 36px wide.
   - The "Give feedback without playing" link has no padding.
   - Fix: 44px heights on the primitives and pills. **[mechanical]**
2. **Sideways scroll at 320px with 200% text.**
   - /upload overflows by 121px ("Attach screenshots", "Continue without video").
   - On thank-you, "Submit for another game" runs past both edges of its button.
   - Cause: `whitespace-nowrap` in `BUTTON_BASE_CLASS`. **[mechanical]**
3. **Font sizes off the scale.**
   - `text-[0.7rem]` in upload, thank-you, ScaleAnswer, VideoUploader and the `sm` button; `text-[0.8125rem]` in the `md` button.
   - The upload step label is hand-built, while feedback uses `.adp-kicker` for the same role. **[mechanical]**
4. **The required "*"** uses `--color-negative` (3.08:1) (`QuestionField.tsx:45`). Fix: `--color-negative-text`. **[mechanical]**

## Major
5. **/game/[slug] "not available" card is a dead end:** no action and no way back. Fix: "Back to games". **[mechanical]**
6. **/brief renders nothing while it fetches.** Fix: a Skeleton. **[mechanical]**
7. **Scale end captions run together** at 200% text ("1 · NothingExpert"). **[mechanical]**
8. **Invalid `<p>` inside `<dl>`** in the thank-you summary. **[mechanical]**
9. **The feedback screen has no h1.** **[mechanical]**
10. **The Session ID is truncated to one character** at 320px. **[mechanical]**
11. **Primary hover is opacity-only.** **[mechanical]**
12. **Screenshot thumbnails are 96px fixed;** the maximum is 64px. **[mechanical]**

## Minor
13. **"or click to browse" on phones.** Fix: "or choose a file". **[mechanical]**
14. **Pill selection is shown by colour alone.** Fix: add a check glyph or a weight change. **[mechanical]**

## Needs a human
- **"Continue to play" is below the fold on phones.** Options: a sticky action, the CTA before the brief, or a collapsed brief. **[decision]**
- **Thank-you says "Your recording and feedback have been submitted"** even when there was no video. **[decision]**
- **"Submit for another game" and "Done" run the same code.** **[decision]**
- **The brief is rendered on both /brief and /game/[slug].** Which one owns it? **[decision]**
- **Screenshots can't be removed or previewed before upload.** **[decision]**
- **The indicator says "Step 1 of 2" / "2 of 2",** but the flow has four screens. **[decision]**
