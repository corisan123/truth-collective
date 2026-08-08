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
| Locked classes on product blocks | **Stripped / missing** — live markup probe 2026-08-08: **0×** `tc-overlay-card-product`, only **4×** `tc-explore-hub`, **4×** `tc-overlay-card`, **4×** `tc-book-card` |
| Grade markup | Still in page as real HTML + leading `[4.7/5]` text nodes — but without parent overlay classes, layout collapses; editor shows Custom HTML as code boxes (expected in editor) |
| Media | Image `src` URLs still in HTML, but sample product file **404**: `…/uploads/2026/07/61of3rzFYwL._AC_SL1200_-966x1024.jpg` — media missing or path wrong after uploads restores |

This is **block markup damage** on this page (classes removed from product Sections/columns), not “delete all Additional CSS.”

## Restore timeline (Daniel 2026-08-08 — critical)

| When | What | Computers page |
|------|------|----------------|
| ~2026-07-28 content state | Reviewed yesterday during restore attempts | Damaged, **not this crushed** |
| Hostinger files restore used **2026-08-01**; DB **2026-07-28**; uploads Jul 28 + **Jul 24** | Exhausted angles; never fully healthy | — |
| After going to **2026-07-24** material | — | **Completely crushed** (worse than Jul 28 review) |

**Conclusion:** Jul 24 rollback is what destroyed this page’s product markup/classes. Do **not** restore older than Jul 28 for Computers. Prefer WP **Revisions** or a **page-only** recovery toward Jul 28-era markup — never another full Jul 24 path.

## Snippet from product row (Daniel — Jul 24-era block)

Kadence Image with `className` / div class `tc-explore-hub`, Amazon `amzn.to` link, drop shadow, radius 15. **No** `tc-overlay-card` on the image block (expected: explore on image; overlay on Section/column).

If parent Section lost `tc-overlay-card` / `tc-overlay-card-product`, you get exactly today’s pattern: explore class may remain on some images while product overlay behavior is dead.

Sample media in snippet: `…/uploads/2026/07/Facebook-Cover-AI-Agentic-Advances-1200-x-900-px-4-1024x768.png` (verify 200 vs 404 separately).

## Do not do yet
- Do not rebuild all 86 pages
- Do not paste Copilot/Claude full-page HTML
- Do not wipe Additional CSS to “fix” Computers
- Do not Hostinger restore again for this page
- Do **not** re-apply Jul 24 backups hoping Computers improves

## Revision note — user “10/26” 12:42 (Daniel 2026-08-08)

(Confirm calendar date: likely **7/26** given crash timeline; user typed 10/26.)

**In that revision:**
- Hero + other **images present in markup** (e.g. core `wp:image` hero `uploads/2026/03/Untitled-3200-x-1040-px-…`)
- Still **no overlay/explore product animation classes** beyond book-card pattern
- Includes older page-scoped `.tc-page--computers` CSS tokens (navy/gold/cream) in content — separate from Customizer Additional CSS stacks
- Watch image host: snippet showed `tcstaging.collective.com` (missing `truth-`) — if real, those URLs would 404 even when files exist on `tcstaging.truth-collective.com`

**Live now:** Daniel — **no images anywhere** on Computers. Matches probed **404** on `/uploads/2026/07/…` product files after Jul 24 uploads path. Revision proves markup once pointed at images; crush = **classes stripped + media missing/wrong host**, not “CSS deleted.”

**Do not Restore that revision yet** if it lacks overlay classes — you would keep missing animations and may not bring media files back (files live on disk / Hostinger, not inside the revision HTML alone).

## Next recovery order (Computers only)
1. **Revisions** — keep browsing; prefer a revision with **both** images in markup **and** `tc-overlay-card` / `tc-overlay-card-product` on product Sections. Do not Restore the 12:42 book-only revision yet.
2. **Media check (Hostinger File Manager):** do `uploads/2026/03/` and `uploads/2026/07/` product/hero files exist on disk? Jul 24 uploads restore may have removed later July files.
3. If no good revision: fix **one** product Section — re-add overlay class on Section + keep `tc-explore-hub` on image + point image at a file that returns HTTP 200.
4. Then repeat pattern; only then consider template HTML for the page family.
