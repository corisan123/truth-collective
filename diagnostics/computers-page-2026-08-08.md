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

## Build history (Daniel 2026-08-08 — critical)

1. **Early stub only:** hero image + a few paragraphs (what “7/26” / “3/26” revision tops look like — same hero size).
2. **Then** Daniel built the page to ~**90/100 Rank Math**, fully animated, product images, overlays — **completed just before the 10Web crash**.
3. Crash / restores damaged that finished build. **Jul 24** made it worse than the Jul 28 review.

### Diff locked: 7/26 stub → 7/28 11:43 (Daniel compare)

| | **7/26 (Removed)** | **7/28 11:43 (Added)** |
|--|--------------------|-------------------------|
| Hero | Core `wp:image` id 856, `Untitled-3200-x-1040-px-…`, width 1173px | New image id **8233**, wide/full, `Facebook-Cover-AI-Agentic-Advances-and-Emerging-Technologies-1000-x-1000-px-1.png`, alt set |
| Intro copy | Loose 17px paragraphs | Centered **h1** + colored **h2** banner (“Tools That Keep Up…”) |
| Structure | Almost none | Kadence **rowlayout** 3 columns |
| Classes | None of the locked card system | **`tc-book-card`** on columns + **`tc-leadership-body`** on paragraphs (hover drop-down intro cards) |
| Below | — | Kadence spacer/stripes divider; next row starts product section titles (“Gaming Computers”, “Desktops For Professionals”) |

**What occurred:** This is the jump from **stub → real page build start** (hero swap, H1/H2, intro book-cards, divider, product section headings). Overlay/product animation classes are **not** in this slice of the diff yet — they come further down the 7/28 page (or a later revision the same day) as product rows were filled in.

**Recovery implication:** 7/28 11:43 is the right **family** of revisions (post-stub). Still verify the **full** 7/28 revision includes product rows with `tc-overlay-card` / `tc-explore-hub` before Restore — do not stop at the intro-only portion of the compare view.

### Mid-build markers Daniel found in same era (2026-08-08)

**A. Page-scoped “explore tiles” CSS (not the later hub system)**  
Added under `.tc-page--computers`:
- `.tc-explore` — 1-col grid, 3-col from 720px
- `.tc-tile` — min-height 220px, radius 12px, soft gradient, transform/shadow transition  

This is an **earlier Computers-page pattern** (CSS tied to `.tc-page--computers` + `.tc-explore` / `.tc-tile`). It is **not** the same as locked **`tc-explore-hub` on Kadence images** + Customizer overlay stacks. Seeing “explore” here only proves mid-build experimentation, not that product overlay cards are complete.

**B. Near bottom of same build wave**  
- Placeholder: **“Product shortlist coming next”** + note that product cards were **not started** in the source PDF yet — waiting on product list / affiliate links.
- Then more shell: disclosure, Kadence row, **“Latest Advancements in CPU Architecture”**, etc.
- UI shows **UpdraftPlus** + **“Restore This Autosave”** — do **not** click that unless Cursor says so. Autosave/Updraft ≠ “restore finished Rank Math page.” Prefer WP **Revisions** of the finished build.

**Meaning:** This snapshot is **page shell mid-flight** (intro cards + explore-tile CSS + CPU section), **before** product shortlist/cards. Keep scrolling to a **later** revision after products were dropped in (search `tc-overlay-card-product` or `amzn.to` + `tc-explore-hub`).

**Hero+paragraphs revision = pre-build stub. DO NOT RESTORE IT.**  
Restoring that would **delete** the finished Computers page and roll back to “just started.”

Correct target: a revision (or current markup repair) of the **post-build** page — product grid + `tc-overlay-card` / `tc-overlay-card-product` + `tc-explore-hub` + working media.

**Live now:** full product copy still largely present but crushed; images 404 / classes stripped. Crush = **finished-page markup damaged + media missing**, not “page was never built.”

## Revision note — stub at 12:42 / 7/26-style top

- Hero URL (correct host): `…/uploads/2026/03/Untitled-3200-x-1040-px-1024x333.png` → **HTTP 200** on staging
- No product overlay animation classes (expected for stub)
- Optional older `.tc-page--computers` CSS in content — not the recovery gold

## Next recovery order (Computers only)
1. **Revisions** — skip all stub (hero + few paragraphs only). Hunt for a **fat** revision: many blocks, product rows, overlay classes. Never Restore the stub.
2. **Media check (Hostinger File Manager):** `uploads/2026/07/` product files — Jul 24 uploads may have removed them; hero in `2026/03/` still on disk.
3. If no good full revision: repair **current** finished page — one product Section at a time (re-add classes + fix image URL to a 200 file).
4. Then repeat pattern; only then consider template HTML for the page family.
