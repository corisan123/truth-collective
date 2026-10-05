# REST-hub-technology-R9d — APPLIED 2026-08-11

**Issue:** Editor showed “Block contains unexpected or invalid content” / Attempt Recovery on each tile image.

**Why:** R9 injected hand-built **Kadence** row/column HTML via REST. The block editor validates against Kadence’s exact schema; mismatched attrs = invalid block on every tile.

**Fix:**
- Replaced Kadence explore rows with **core** `wp:columns` + `wp:column` + `wp:image` (valid Media Replace blocks)
- Kept `tc-explore-hub` class + page CSS for title-on-image / EXPLORE
- Restored fuller Claude Welcome (4 paragraphs); removed cover one-liner

**Daniel:** Hard refresh editor (or leave page and reopen). Invalid blocks should be gone. Click image → Replace for 1600×1000 uploads.
