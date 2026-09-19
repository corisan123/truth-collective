# REST-hub-technology-R9b — APPLIED 2026-08-11

**Issue:** After R9 native-block conversion, category tiles stacked vertically. Not intentional for image replace.

**Cause:** Kadence `rowlayout` blocks were missing `"columns":2`, so desktop 2-across widths did not apply.

**Fix:**
- Set `"columns":2` on each explore row
- Page CSS forces `grid-template-columns: repeat(2, 1fr)` on `.tc-tech-explore-row` (1-col under 780px)

Native `wp:image` / Media Replace unchanged.
