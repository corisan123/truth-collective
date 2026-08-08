# Computers page damage — 2026-08-08

**URL:** `/technology-hub/computers-digital-devices/`  
**Editor title:** Computers and Digital Devices  
**Slug:** `computers-digital-devices`  
**Parent:** Technology Hub  
**Revisions:** 20 (editor shows last edited ~11 days ago / published Mar 16)

## Daniel’s report + screenshots

### Still present (intro row only)
- Section class: `tc-book-card`
- Paragraph class: `tc-leadership-body`
- Intent: hide body until hover, then drop down (book-card motion)

### Missing on product blocks
- **No** `tc-overlay-card` / `tc-overlay-card-product` / `tc-explore-hub` (and related) on product Sections/images
- Product grid therefore cannot inherit Additional CSS overlay/explore/button rules — even though those rules still exist in Customizer (~57KB snapshot)

### Front-end symptoms (live)
- Broken / missing product images (alt empty; filenames shown)
- Grade markup appearing as **literal text** / white code boxes: `<div class="tc-grade-block">…`
- Overlaps: title vs grade vs EXPLORE remnants
- Uneven card heights; some dark / some white (Logitech card)
- Tall empty space in intro cards

### Editor symptoms
- Same raw grade HTML visible in content
- Outline still has Kadence Row → Section → Custom HTML + Image (Adv) + headings for products
- Structure partially intact; **classes and/or HTML block integrity** damaged

## Root cause (certainty)

| Layer | Status |
|-------|--------|
| Additional CSS (sitewide) | Still present (not the sole cause) |
| Locked classes on product blocks | **Stripped / missing** (Daniel confirmed) |
| Grade Custom HTML | Escaped or degraded to visible source text |
| Media | Broken refs or unloadable URLs on this page (check uploads before re-upload) |

This is **block markup damage** on this page (restore / 10Web / editor corruption), not “delete all Additional CSS.”

## Do not do yet
- Do not rebuild all 86 pages
- Do not paste Copilot/Claude full-page HTML
- Do not wipe Additional CSS to “fix” Computers
- Do not Hostinger restore again for this page

## Next recovery order (Computers only)
1. **Revisions** — open Computers → Revisions; try a revision from before visual collapse; preview; restore only if product classes (`tc-overlay-card-product` etc.) return.
2. If no good revision: fix **one** product Section — re-add classes + one Custom HTML grade + one image URL (Cursor-directed).
3. Then repeat pattern; only then consider template HTML for the page family.
