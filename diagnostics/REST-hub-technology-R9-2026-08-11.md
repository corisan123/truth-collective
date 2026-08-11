# REST-hub-technology-R9 — APPLIED 2026-08-11

**Problem:** R8/R8b put tiles/cover inside Custom HTML. Daniel cannot Media → Replace images inside HTML blocks.

**Fix:** Native blocks for media + copy:
- Cover = `wp:cover` (click image → Replace)
- Welcome prose = real paragraph/heading blocks
- Eight category tiles = Kadence columns with class `tc-explore-hub` + real `wp:image` (`wp-image-####`)
- Custom HTML kept **only** for page CSS (+ light stats strip)

**How Daniel inserts pics**
1. Pages → Technology Hub → Edit  
2. Click cover or a tile image  
3. Replace → upload **1600×1000**  
4. Update / Save  

**Still later:** Patterns library pass so reused overlays/grades match this look.
