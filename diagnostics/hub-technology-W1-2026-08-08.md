# Technology Hub — W1 start (2026-08-08)

**Page:** id `111` · https://tcstaging.truth-collective.com/technology-hub/  
**Pipeline:** Plan B + 10Web look mocks (screenshots only) → Claude copy → Cursor REST/Custom HTML  

## REST snapshot
- Content length ~70KB
- `tc-explore-hub`: **28**
- `tc-overlay-card`: **28** (combo present — crop/flicker risk; do not wipe stacks)
- `tc-overlay-card-product`: 0

## Bad / stale hrefs in hub content
| URL | Status |
|-----|--------|
| `/best-office-workspace-products-tools/` | **404** |
| `/featured-productivity-tools/` | **404** |
| `/recommended-books/` | often 301 → 2026 path (verify) |
| `/recommended-books/self-help-and-mental-wellness/` | often 301 |
| `/technology-2/` | verify target |
| `/smart-lighting/` | likely OK |

## REST-hub-technology-S — DONE (Daniel Approve 2026-08-08)

Backup: `diagnostics/backups/page-111-technology-hub-before-REST-hub-technology-S-2026-08-08.html`

| Before | After |
|--------|--------|
| `/recommended-books/` | `/recommended-books-2026/` (id 38) |
| `/best-office-workspace-products-tools/` (107 gone) | `/office-workspace-products-and-tools/` (5939) |
| `/featured-productivity-tools/` (109 gone) | `/productivity-tools/` (5680) |
| `/technology-2/` | `/technology-hub/` (111) |
| `/recommended-books/self-help-and-mental-wellness/` | `/self-help-and-mental-wellness/` (86) |
| `/smart-lighting/` | unchanged (already good) |

Public targets all **200**.

## Next
1. Daniel: 10Web mock using **combined page-specific prompt** (not generic) → screenshots  
2. Cursor: gold template extract from healthiest Technology tile  
3. Claude: hub intro voice when ticketed  

**Do not:** connect 10Web builder to overwrite staging/live.
