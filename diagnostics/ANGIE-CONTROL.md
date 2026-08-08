# Angie control protocol (staging only)

**Site:** https://tcstaging.truth-collective.com  
**Operator:** User pastes Cursor-written prompts into Angie.  
**Controller:** Cursor writes every prompt. No free-form “fix the site” asks.

## Rules for every Angie task

1. **Staging only** — never touch live `public_html` (non-tcstaging).
2. **One task per prompt.** No “also fix CSS / images / all hubs.”
3. Prefer **Plan Mode / Brief** — Angie must show a plan and **wait for Approve**.
4. User pastes Angie’s plan back to Cursor if unsure; Approve only if it matches the allowlist below.
5. After each approved change: user checks **one URL** and reports **worked / failed / worse**.

## Forbidden (Angie must not do)

- Hostinger restores, Updraft Continue, DB imports
- Deactivate/delete **10WEB manager** (unless user later asks)
- Edit live site
- Rewrite whole pages or regenerate layouts
- Delete or rewrite all Additional CSS in one pass
- “Improve” or replace product images
- Bulk find-replace across the whole site without an explicit Cursor list

## Allowed (one at a time, Cursor-directed)

- Change **one** block link URL on **one** page
- Report / list stale links on one page (read-only)
- Locate `tc-explore` / STAGING PATCH CSS in Additional CSS or Code Snippets (read-only first)
- Later: disable **one named CSS block** after Cursor names it

## Task queue

| # | Status | Task |
|---|--------|------|
| A0 | next | Read-only: confirm Office hub File Cabinets tile href |
| A1 | queued | Fix that **one** link to the correct permalink |
| A2 | done (Daniel 2026-08-08) | `tc-explore` / STAGING PATCH live in **Appearance → Customize → Additional CSS** only. Code Snippets never used. |
| A3+ | later | More hub links / CSS — only after A1 proves control |

## Correct File Cabinets permalink

`https://tcstaging.truth-collective.com/office-workspace-products-and-tools/office-file-cabinets-credenzas-essentials/`

## Wrong href currently on Office hub tile

`https://tcstaging.truth-collective.com/file-cabinets-credenza/`
