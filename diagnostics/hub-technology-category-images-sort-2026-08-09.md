# Technology Hub — eight category images sorted (2026-08-09)

**Page:** `/technology-hub/` eight `tc-tech-cat-tile` images  
**Locked export target:** **1600 × 1000** (16:10), no baked-in captions/ad copy  
**Method:** Downloaded live tile files, inspected each visually.  
**Claude rule applied:** text belongs in HTML (title / blurb / Explore), never inside the photo.

## Quick answer for Claude / Daniel

| # | Category | Pile | Why |
|---|----------|------|-----|
| 1 | Computers and Digital Devices | **Salvage** | Clean single desk photo; **no baked text**. Portrait (1000×1188) → crop to 1600×1000. |
| 2 | Monitors and Displays | **Salvage** | 4-up product collage, no ad copy. **Extract one** shot (prefer the ultrawide monitor alone) to 1600×1000. Do not keep the collage. |
| 3 | Audio and Video | **Salvage** | Side-by-side collage. **Extract left** conference-room photo only (cleaner). Drop busy cubicle half. |
| 4 | Headphones and Headsets | **Salvage** | Side-by-side collage, no ad overlays. **Extract one** panel (studio headphones **or** boom headset) to 1600×1000. |
| 5 | Desk Speakers | **Needs new** | Baked marketing line (“It can be placed under the table…”) + dimension callouts. Cropping still leaves Amazon-flyer tone. |
| 6 | Projectors and Microphones | **Needs new** | 3-panel collage; dashboard UI text + busy projector showroom. Optional: mics-only panel is cleaner, but not a true category hero as-is. Prefer a new single clean shot. |
| 7 | Digital Smart Tablets | **Salvage** | 5-up collage; one panel is pure ad copy (“Just like using a traditional pencil…”). **Extract** the clean white reMarkable product shot (architectural sketch) → 1600×1000. Discard the feature-icon strip. |
| 8 | Interactive Digital Displays | **Needs new** | Collage includes baked slogan “MORE THAN A SCREEN…” + icon row + neon thumbnail grid. Wrong tone even after partial crop. |

**Tally:** **5 salvageable** · **3 need new photos**

## Aspect vs target (current files)

Target aspect **1.60** (1600÷1000).

| # | Current px | Aspect | Notes |
|---|------------|--------|-------|
| 1 | 1000×1188 | 0.84 | Too tall |
| 2 | 1900×1080 | 1.76 | Wide collage |
| 3 | 1024×514 | 1.99 | Very wide dual |
| 4 | 2552×1080 | 2.36 | Very wide dual |
| 5 | 1200×1000 | 1.20 | Tall-ish + ad graphics |
| 6 | 1900×1080 | 1.76 | Collage |
| 7 | 1366×768 | 1.78 | Collage |
| 8 | 1900×1080 | 1.76 | Collage + slogan |

## What Cursor should **not** do next
- Another CSS-only formatting pass on these eight files  
- Keep multi-image collages and hope `object-fit` fixes them  

## Fastest path for Daniel
1. In Canva (or similar), for piles **Salvage**: open the current file → crop/extract **one** clean photo → export **1600×1000** JPG/WebP → replace Media on that tile.  
2. For piles **Needs new**: pick one premium single product/lifestyle shot from the 5000+ library → export **1600×1000** with subject centered → upload/replace.  
3. Tell Cursor when the eight files are replaced; Cursor swaps `src` on the eight tiles (or Daniel replaces in Media if same attachment IDs).

## Previews (agent local)
Downloaded under `/tmp/tech-hub-tiles/` during audit (not required in git).
