# Staging CSS inventory (from live homepage HTML, 2026-08-08)

Source: Customizer Additional CSS / enqueued styles containing `tc-explore` (~57KB on homepage).
No `10web` / `tenweb` / `twbb` markers found in HTML of home, Technology Hub, Computers, Speakers, or Audio & Video.

## Section headers found

### Confirmed in Customizer by Daniel (2026-08-08)
- `STAGING PATCH 01A — TC BOOK CARD H5 TITLE CONTROL` — book cards / H5 spacing only; leave on for now
- `STAGING PATCH 01C-PRODUCT — LOCK IMAGE HEIGHT ON PRODUCT CARDS ONLY` — `tc-product-card` image height; can crop products; candidate later, not first if hub EXPLORE is the symptom
- `STAGING PATCH 01G — FORCE CARD LABEL ONTO ITS OWN LINE` — **intended fix** for title overlap; leave on. If overlap persists, later patches (Explore Hub / 02-PRODUCT) are likely overriding or fighting it.
- `TC Explore Hub Overlay Animation, 2026-05-26` — start of Explore Hub stack (many follow-on add-ons). Not “delete all explore.” Crop often = **overlay + explore used together** + later patches overriding each other. Disable **one add-on layer** at a time after end markers are known.
- `STAGING PATCH 02A — OVERLAY BUTTON ANCHOR + INLINE STAR RENDER FIX` — **KNOWN GOOD. SKIP.** Two-button overlay system (`.tc-overlay-buttons` / `.tc-affiliate-btn` / `.tc-grade-btn`); days to perfect; product page still fine after 10Web crash. Do not disable or “improve.”
- `STAGING PATCH 02-PRODUCT OVERFLOW FIX` — **intended grid fix** (`min-width:0` + width-driven `aspect-ratio:1/1` on `.tc-overlay-card-product`). Daniel: **not working properly now**; later tall-not-wide cards. Archived `css-chunks/02-product-overflow-fix.css`. Do not delete yet — next check is whether broken pages still have the class/Kadence wrappers, or a later rule overrides.
- `STAGING PATCH 02-PRODUCT POLISH` — title white+shadow at rest + product scrim; button stretch match. Sits below overflow fix; claims not to alter it. Archived with buttons block.
- `TC PRODUCT OVERLAY BUTTONS - SINGLE SOURCE OF TRUTH` — final product two-button grid (View + TC Grade/stars); zeroes `.tc-grade-block` margin push-out. **Authoritative for product buttons** over earlier 02A button-height snippets if they still sit above in the file.
- `TC OVERLAY-CARD + EXPLORE-HUB COMBINED FIX` — only when `tc-explore-hub` image sits inside `tc-overlay-card`; moves following `p` to bottom on desktop hover so it clears EXPLORE pill. **Core combo-conflict layer.** Archived `css-chunks/02-overlay-explore-combined-and-grade.css`.
- `STAGING PATCH 02-GRADE` — hub `.tc-overlay-card` grade at top at rest; opacity 0 on hover. Leave until hub grade/EXPLORE overlap is re-tested.
- **After 02-GRADE (mobile):** `@media (max-width: 767px)` forces `.entry-content .kt-row-column-wrap` left/right padding 20px. **Sitewide Kadence rows**, not overlay-scoped. Flag for later mobile fix; do not change now.
- **02A / product-card settled behavior (Daniel paste 2026-08-08)** — do not regress:
  1. Card near-square for 600×600 product images, cover fill, slight crop  
  2. Title 18px bold navy at rest, white on hover, heavy shadow removed  
  3. Grade button stacked: “TC Grade” (Playfair) over gold stars, no numeral  
  4. Both buttons matching transparent blue, reduced height  
  5. Buttons hidden at rest, fade up on hover (desktop); always shown on mobile

### Architecture note (Daniel 2026-08-08)
- Originally: `tc-overlay-card` = Section; `tc-explore-hub` = images (EXPLORE is JS/CSS look-alike; whole image linked).
- Combined use caused crop conflicts → many separate append-only patches + required image sizes.
- Inventory must list each Explore/Overlay header separately before any disable.

### From live HTML earlier
- `/* End TC Row-Stretch Override */`
- `/* End TC Gold Star Rating Base64*/`
- `/* End TC Technology Hub Explore Button Wrapper Control */`
- `/* End TC Technology Hub Editorial Intro Sections Final */`
- `/* TC Explore Hub Overlay Animation, 2026-05-26. No collisions with locked classes. Paste at the bottom of Astra Additional CSS. */`
- `/* TC Explore Hero Animation, 2026-06-01. Class: tc-explore-hero. Append at bottom of Additional CSS. */`
- `/* End TC Explore Hero */`
- `/* TC Explore Hero render fix, 2026-06-01. Append-only. Gives the absolutely positioned hero image a containing-block height. Overlay selector corrected to live class. Scoped to tc-explore-hero only. */`
- `/* End TC Explore Hero render fix */`
- `/* TC Explore Hero tuning, 2026-06-01. Append-only. Whole scene no crop via 16:9 ratio, H1 sized down (tag kept), text re-spaced under the sconces, reveal slowed and staggered. Scoped to tc-explore-hero only. */`
- `/* End TC Explore Hero tuning */`
- `/* End STAGING PATCH 02A */`
- `/* End STAGING PATCH 02-PRODUCT CONSOLIDATED */`
- `/* End STAGING PATCH 02-PRODUCT OVERFLOW FIX */`
- `/* End STAGING PATCH 02-PRODUCT POLISH */`
- `/* End TC PRODUCT OVERLAY BUTTONS */`
- `/* End TC PRODUCT GRADE STARS - REAL BUG FIX */`
- `/* End STAGING PATCH 02-GRADE */`
- `/* TC Membership Toggle — light / Vercel-aligned */`

## Live page signal counts

| Page | `tc-explore*` hits | Notes |
|------|-------------------|-------|
| Technology Hub | high | child tiles crop; links reported broken |
| Computers | high | worst damage; overlays/ratings collapsed |
| Speakers | highest | black bars / uneven crops |
| Audio & Video | high | mixed; some links work |

## Next fix (not restore)

1. Disable/remove conflicting Additional CSS blocks: `tc-explore-hub`, `tc-explore-hero`, STAGING PATCH 02-PRODUCT*, product overlay buttons.
2. Then fix wrong hub/product URLs in block content.
3. Check Plugins for any remaining 10Web plugin; rename `object-cache.php` if present.