# REST-hub-technology-R4c — APPLIED 2026-08-09

**Page:** Technology Hub `111`  
**Backup:** `diagnostics/backups/page-111-before-REST-hub-technology-R4c-2026-08-09.html`

## Why
Daniel still saw left-stuck content after R4b. Astra/full-bleed rules (`calc(-50vw + 50%)` / `100vw` on alignfull) were still pulling content off the left edge on desktop.

## Fix
1. Page-scoped **R4c** CSS: neutralize all `.alignfull` / `.alignwide` / hero shell / Kadence alignfull breakouts on `page-id-111`
2. Strip `alignfull` from How-To Kadence columns  
3. Title banner image `alignfull` → `alignwide`

## Also (user UI)
Windows 11 Snap Layouts hover menu only shows split grids. Full window = click Maximize (or Win+Up), not a snap tile.
