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