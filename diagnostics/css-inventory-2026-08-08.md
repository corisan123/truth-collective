# Staging CSS inventory (from live homepage HTML, 2026-08-08)

Source: Customizer Additional CSS / enqueued styles containing `tc-explore` (~57KB on homepage).
No `10web` / `tenweb` / `twbb` markers found in HTML of home, Technology Hub, Computers, Speakers, or Audio & Video.

## Section headers found

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