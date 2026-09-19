# Vercel + 10Web comparison pack — ingested 2026-09-19

**Upload:** `vercel AND 10weB COMPARISON (2026_09_02 19_57_57 UTC).pdf`  
**Repo copy:** `docs/brand-references/vercel-and-10web-comparison-2026-09-02.pdf` (28 pages)  
**Older 8-page pack kept as:** `docs/brand-references/vercel-and-10web-comparison.pdf`  
**Role:** Visual / motion gold. Reference only. Do not port Tailwind, v0, or 10Web markup.

Daniel’s own captions in this file override Claude’s 2026-09 visual ticket where they disagree.

## Motion rules taken from this PDF

**Hub / large tiles (pp. 8–10)**  
- High-res image is the whole tile.  
- At rest: title sits **on the image, at the bottom**.  
- On hover: image lifts; title **rises toward the middle**; transparent **EXPLORE** sits under the title.  
- Entire image is the link. EXPLORE is a look-alike, not a required click target.  
- Prefer Vercel overlay polish over crushed-dark WP hover (p. 1: current staging still too dark after Claude hover work).

**Toggle membership (pp. 3–5)**  
- 10Web toggle motion is the better of the two samples.  
- Four looks; destination changes with the toggle. Staging toggle page 8176 already aims at Vercel-light; keep 10Web toggle feel.

**Product cards (pp. 13–15)**  
- 10Web overlay on hover: Trusted Choice + View Product.  
- Click-through detail: spare words, light frame, not a wall of copy.

**Small / sub-child tiles (pp. 16–17)**  
- No long descriptions on the image.  
- Hover: two transparent controls, **Details | Reviews** (Reviews = TC Grade 3.5–5, everything except books).  
- Live staging already has a known-good **View + TC Grade** pair (`02A`). Do not invent a third button system. Map Details → View (affiliate), Reviews → TC Grade.

**Editorial tiles (pp. 18–19)**  
- Greyscale at rest → full color on hover.  
- Does **not** apply to product photos or book covers.

**Hero / cover (p. 20)**  
- Image is present on load. Copy and CTA animate into center.  
- Optional video placeholder at top (Vercel called this gold).  
- Class on TC: `tc-explore-hero`.

## What this is not

- Not a page to clone into WordPress.  
- Not permission to paste Claude/10Web/v0 CSS.  
- Not a product sitemap. Robotics / fake trees stay out.

## Conflict close-out vs Claude 2026-09 directive

| Claude said | This PDF says | Winner |
| --- | --- | --- |
| Title below the image at rest | Title on the image, bottom at rest | **PDF** |
| EXPLORE is a real button | Transparent EXPLORE; whole image linked | **PDF** |
| Overlay too dark must lighten | p.1: staging hover still too dark | **Agree — lighten via Additional CSS** |
| Grayscale from ISI | pp. 18–19 editorial only | **PDF** (hubs/editorial, not products/books) |
