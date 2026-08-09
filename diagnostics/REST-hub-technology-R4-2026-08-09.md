# REST-hub-technology-R4 — READY (blocked on auth) 2026-08-09

**Page:** Technology Hub `111`  
**Goal:** Stop the tall old vertical category stack. Keep cream split hero. Install a cream **3-column** grid of the **eight real children** only.

## Why
Daniel: getting better, but still vertically stacked and old looking. 10Web mood board moved things around; we borrow the airy horizontal feel, not 10Web HTML.

## What R4 does
1. Upgrades page-scoped CSS `TECH-HUB-CREAM-R3` → `TECH-HUB-CREAM-R4` (hero rules kept + grid rules).
2. Replaces **Technology Hub Categories** through just before **Final Thoughts** with the cream tile grid.
3. Tiles use `tc-tech-cat-tile` (page-scoped). **No** `tc-overlay-card` on these tiles (avoids Explore+Overlay crop combo).
4. Gold text **Explore** label; gentle lift + image darken; scroll rise motion (respects reduced motion).
5. One distinct working image per tile (Computers child media is mostly 404 — tile uses a working hub image until selective uploads restore).

## Files
- `diagnostics/scaffolds/REST-hub-technology-R4-category-grid.html`
- `diagnostics/scaffolds/REST-hub-technology-R4-section-only.html`
- `diagnostics/scaffolds/REST-hub-technology-R4.css`
- `diagnostics/scaffolds/REST-hub-technology-R4-tiles.json`
- `diagnostics/scaffolds/apply-REST-hub-technology-R4.py`
- Diagnosis: `diagnostics/hub-technology-layout-vertical-stack-2026-08-09.md`

## Apply (when App Password works)
```bash
export TC_WP_USER='dreid1253@yahoo.com'
export TC_WP_APP_PASSWORD='xxxx xxxx xxxx xxxx xxxx xxxx'
python3 diagnostics/scaffolds/apply-REST-hub-technology-R4.py
```

## Blocked
Staging Application Password currently returns **401** on `/wp-json/wp/v2/users/me` and `pages/111?context=edit`. Need a new Application Password from Users → Profile (staging only).

## View-check after apply
Hard refresh: https://tcstaging.truth-collective.com/technology-hub/  
Expect: navy/cream hero unchanged in spirit; below it a 3-col cream grid (2-col tablet, 1-col phone) of eight categories — not the old Printers/Robots/Smart Home essay stack.
