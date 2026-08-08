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

## Hard lessons (Daniel — locked)

- ChatGPT once had SQL lines deleted; Cursor+Daniel repaired some fallout. **Never** free-form SQL again.
- Homepage links can look correct (slug/URL) but fail (“hidden ghosts”). Multi-day repair of corrupted blocks **failed**. **Policy: do not spend days repairing ghost blocks. Delete the corrupted block and rebuild** with Cursor HTML + Angie apply.
- Computers revision hunt closed — no full finished revision. Same rule: rebuild page-by-page, not restore roulette.
- Daniel will **not** repeat four-day ghost repair. Helpers must not ask him to.

## Two phases (positive path — 2026-08-08)

### Phase S — Stable (Angie + Cursor first)
Prove control with small read-only / one-link tasks. No whole-page rewrites. No Hostinger restores. Leave 10Web alone unless Daniel asks.

### Phase R — Rebuild (after Phase S proves stable)
Page-by-page (or one card / one section at a time): Cursor supplies Custom HTML using locked `tc-*` classes; Claude may rewrite long copy; Angie or Daniel pastes. Corrupted blocks → **delete and replace**, not endless patch.

## Forbidden (Angie must not do)

- Hostinger restores, Updraft Continue, DB imports, SQL edits
- Deactivate/delete **10WEB manager** (unless user later asks)
- Edit live site
- Rewrite whole pages or regenerate layouts in Phase S
- Delete or rewrite all Additional CSS in one pass
- “Improve” or replace product images without Cursor naming the file
- Bulk find-replace across the whole site without an explicit Cursor list
- Multi-day “find the ghost” investigations

## Allowed (one at a time, Cursor-directed)

**Phase S**
- Report / list links on **one** page (read-only): href, visible label, works Y/N if Angie can tell
- Change **one** block link URL on **one** page
- Confirm Additional CSS still only in Customizer (read-only)
- Later: disable **one named CSS block** after Cursor names it

**Phase R** (only after Cursor opens it)
- Delete **one** named corrupted block
- Insert **one** Cursor-provided Custom HTML / class fix on **one** section
- Re-add locked classes on **one** Section or image (`tc-overlay-card`, `tc-explore-hub`, etc.)

## Task queue

| # | Status | Task |
|---|--------|------|
| A2 | done | CSS lives in Appearance → Additional CSS only |
| Computers | closed | Revision hunt stopped; rebuild later |
| **S0** | **partial (Daniel)** | Homepage: first **three** major child blocks still had locked CSS classes; **hrefs were stripped**. Daniel re-linked all three — **they work now.** Pattern: classes can survive while links are removed. |
| S0b | next (Angie) | Read-only: list remaining homepage hub/child links below those three (label + href). No edits. |
| S1 | queued | From list: next dead/missing link — one only |
| S2 | queued | Fix that **one** link OR delete/replace that **one** ghost block |
| R0 | later | First rebuild page/card after Phase S feels stable to Daniel |

## Correct File Cabinets permalink (still valid)

`https://tcstaging.truth-collective.com/office-workspace-products-and-tools/office-file-cabinets-credenzas-essentials/`

## Wrong href example (Office hub tile)

`https://tcstaging.truth-collective.com/file-cabinets-credenza/`
