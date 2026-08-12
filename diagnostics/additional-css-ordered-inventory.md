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
| Overlay+Explore combined fix + 02-GRADE | `css-chunks/02-overlay-explore-combined-and-grade.css` — combo layer; high relevance to dual-class pages |
| Later 02-PRODUCT / hero / grade patches | Awaiting paste |

## Paste log

(Daniel will paste large chunks after book-page code. Store under `diagnostics/css-chunks/` as received.)

**End of Customizer CSS (live homepage 2026-08-08):** after `End STAGING PATCH 02-GRADE` (+ mobile row padding) comes **only** `TC Membership Toggle — light / Vercel-aligned`. That is expected footer, not proof the rest was deleted. Live HTML still contains Explore Hub + 02A + overflow + grade **above** membership.

**Missing-content check:** If Daniel’s 2-day-old save has blocks that search cannot find in Additional CSS now, restore from that save into a text file and diff — do not paste blindly over the working 02A/membership sections. Page **HTML** (Custom HTML blocks) is separate from this CSS file.
