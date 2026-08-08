# Additional CSS — ordered inventory (staging)

**Source:** Appearance → Customize → Additional CSS (Daniel paste).  
**Rule:** Keep blocks in **file order**. Do not reorder. Prior Cursor checked conflicts against what already existed; out-of-order reading misleads.

## Status

| Block | Status |
|-------|--------|
| Book-page related CSS (before product/explore stacks) | Awaiting paste |
| STAGING PATCH 01A / 01C / 01G | Seen headers; leave on |
| TC Explore Hub Overlay Animation + add-ons | Awaiting full ordered chunk |
| STAGING PATCH 02A — overlay buttons + stars | **SKIP — known good** |
| Protected extract: `.tc-overlay-card-product` aspect-ratio + button height | `css-chunks/02a-product-overlay-protected.css` |
| STAGING PATCH 02-PRODUCT OVERFLOW FIX | `css-chunks/02-product-overflow-fix.css` — present but failing on site; diagnose before disable |
| 02-PRODUCT POLISH + TC PRODUCT OVERLAY BUTTONS | `css-chunks/02-product-polish-and-buttons.css` — buttons SSoT; leave unless proven conflicting |
| Later 02-PRODUCT / hero / grade patches | Awaiting paste |

## Paste log

(Daniel will paste large chunks after book-page code. Store under `diagnostics/css-chunks/` as received.)
