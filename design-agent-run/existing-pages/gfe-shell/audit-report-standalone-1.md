# GFE-SHELL standalone design audit (header/nav, login, root redirect)

Independent audit by the agent's `design-critic` persona (read-only; code, screenshots in `../screenshots/before/`, `../measurements-before.json`).
Standalone mode: missing briefs, flows and records are backfill, not findings.

**overallVerdict: blocker**

The root redirect (`app/page.tsx`) and the signed-out return path (`login/page.tsx:22`, sanitized `from`) pass.

## Blockers
1. **The page scrolls sideways at 320px with 200% text (every page, +54px).**
   - Seen in imports-320-text200: "ATARI" overlaps the ADMIN badge, and the menu button is clipped.
   - Root cause: `RoleBadge.tsx:52`. Its base class `inline-flex` overrides the `hidden` passed at `layout.tsx:118`, so the badge meant to be `hidden sm:inline-flex` shows on phones.
   - Second cause: `layout.tsx:101,111`. The wordmark is `shrink-0` and `nowrap`, and the right-hand cluster has no `min-w-0`.
   - Fix: remove `inline-flex` from the RoleBadge base so the caller sets `display`, and add `min-w-0` to the right cluster. **[mechanical]**
2. **Touch targets under 44px.**
   - `HeaderSelectionChip.tsx:54`: the clear "×" is 16px.
   - Desktop Games / Sessions links (`NavClient.tsx:76-77`) are about 24px.
   - The + Add game / + Add build pills are about 30px.
   - Button `sm` (`buttonClasses.ts`) makes Admin and Sign out about 30px.
   - Fix: add `min-h-11` to each; on the chip, give the 16px glyph a 44px hit area. **[mechanical]**
3. **Login h1 contrast.** The gradient ends at `--color-accent` (1.91:1 on white), which is also a brand exclusion (`login/page.tsx:42`). Fix: end it at `--color-accent-text`, or use solid `--color-ink`. **[mechanical]**
4. **Values off the token scales.**
   - Font sizes: `text-[0.65rem]` (RoleBadge, NotificationBell) and `text-[0.7rem]` (HeaderSelectionChip, Button sm).
   - Spacing: 6, 10 and 2px values.
   - Login: the h1 `clamp`, the card's `borderRadius: "20px"`, and an inline `fontSize` on the button.
   - Fix: move each to its nearest token. **[mechanical]**
5. **Two primary actions on one screen.** The header's Admin / Questions link uses `variant:'primary'` (`NavClient.tsx:123,130,235,245`). Fix: switch it to `secondary`. **[mechanical]**

## Major
6. **Wrong menu roles.** `role="menu"` / `menuitem` (`NavClient.tsx:171,181…`) are used without arrow-key handling. Fix: use a list of links in a labelled `<nav>`. **[mechanical]**
7. **Focus colour missing.** The hamburger, ink links, Add pills and the wordmark link have no token focus ring. **[mechanical]**
8. **Primary hover is opacity-only.** Fix: use a hover background token. **[mechanical]**
9. **RoleBadge text is 10.4px,** below the 11px minimum. Fix: 12px mono. **[mechanical]**
10. **The mobile menu can't scroll in landscape.** Fix: `max-h` plus `overflow-y-auto`. **[mechanical]**
11. **The login Google button restyles Button inline.** Fix: use `buttonClasses({secondary, lg, fullWidth})`; the Google logo colours are exempt. **[mechanical]**

## Minor
12. **Link name doesn't match its visible text.** It's named "Home" but shows "ATARI Game Feedback" (WCAG 2.5.3). **[mechanical]**
13. **Two unlabelled `<nav>` landmarks.** **[mechanical]**
14. **Truncated email.** It relies on `title` alone; let it wrap in the mobile menu. **[mechanical]**
15. **Login breakout width.** `100vw` plus a negative margin can scroll sideways when a scrollbar is present. **[mechanical]**

## Needs a human
- **Current-page state in the nav** (`aria-current` plus a style). How it should look is a design decision. **[decision]**
- **Duplicate "+ Add game"** on /games (nav and page), and whether Add game / Add build belong in the global chrome. **[decision]**
- **Wordmark colour.** "ATARI" is mint text. Accept the logotype exemption, or switch to `--color-accent-text`. **[decision]**
- **Role badge on phones.** Move it into the mobile menu, or drop it below `sm`. **[decision]**
