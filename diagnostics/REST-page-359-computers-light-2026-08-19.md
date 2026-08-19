# Computers page light rebuild (2026-08-19)

**Page:** `359` `/technology-hub/computers-digital-devices/`  
**Scaffold:** `diagnostics/scaffolds/REST-page-359-computers-light.html`  
**Apply:** `diagnostics/scaffolds/apply-REST-page-359-computers-light.py`

## Why rebuild (not restore)
Revision hunt closed 2026-08-08. Jul 24 crush + stripped overlay classes + 404 product media. Daniel has replacement images.

## What this scaffold does
- Delete-first light shell matching Tech Hub / Smart Lighting factory
- Nine cleaned categories, 21 graded products
- Locked classes retained: `tc-overlay-card`, `tc-overlay-card-product`, `tc-grade-block`, `tc-product-card`
- **No** `tc-explore-hub` on product images (avoids overlay+explore crop combo)
- Page-scoped readable cards (cream / navy / gold)
- Amazon short links retained for Associates reapply at launch
- Placeholder product images use Computers hub tile (`8313`) until Media Replace

## Daniel next
1. Restore Cursor secrets `TC_WP_USER` + `TC_WP_APP_PASSWORD` (missing in this cloud run)
2. Run apply script OR Approve REST apply
3. Media Replace each product image 1600×1000
4. Reapply Amazon Associates after public launch; verify short links

## Amazon note
Associates canceled for 180-day inactivity. Links stay on page for relaunch. Editorial grades unchanged.
