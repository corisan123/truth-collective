# Image sizes — Technology Hub category tiles (2026-08-09)

## Target box (staging R5–R7)
- Layout: **2 across** on desktop  
- Frame ratio: **16:10**  
- CSS fill: `object-fit: cover` (image fills the box; edges may clip if the asset is wrong shape)

## Export size for Daniel (use this)
| Use | Pixels | Aspect | Format | Notes |
|-----|--------|--------|--------|-------|
| **Hub category tile (standard)** | **1600 × 1000** | 16:10 | JPG or WebP | One distinct photo per category; subject centered; keep important content away from edges |
| Retina optional | 1920 × 1200 | 16:10 | JPG/WebP | Only if file stays under ~400KB |
| Do not use | Random collage dumps / mixed ratios | — | — | Current `Untitled-…` mix (1188 tall, 2552 wide, etc.) is why boxes look wrong |

### How to prep from your 5000+ library
1. Pick **one** clear photo per category (8 total for Tech Hub).  
2. Crop/export to **exactly 1600 × 1000**.  
3. Keep the main subject in the center ~70% of the frame.  
4. Upload to Media Library → replace each tile image on `/technology-hub/`.  

Same rule can reuse later for other hubs’ category grids.

## Why they look bad now
Tile files on staging are many different shapes. The box is fixed 16:10. Mismatched sources always letterbox or crop oddly.

## Animation (R7)
Scroll **slide-up + fade** on hero split, stats row, and category tiles (IntersectionObserver). Respects `prefers-reduced-motion`. Not 10Web code — motion only, page-scoped on Technology Hub.
