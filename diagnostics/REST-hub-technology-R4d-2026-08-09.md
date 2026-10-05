# REST-hub-technology-R4d — APPLIED 2026-08-09

**Page:** Technology Hub `111`  
**Backup:** `diagnostics/backups/page-111-before-REST-hub-technology-R4d-2026-08-09.html`

Daniel: three-across grid works; tiles still cropping.

## Fix
Category tile images only (`tc-tech-cat-tile__media img`):
- `object-fit: cover` → **`contain`** (full image visible, cream letterbox if needed)
- aspect-ratio `4/3` → `3/2`
- gentler hover scale

Does **not** change sitewide Explore/Overlay crop CSS (separate later ticket).
