# REST-hub-technology-R9e — APPLIED 2026-08-11

**Issue:** Hero still showed “Attempt Recovery”; Replace control missing.

**Why:** `wp:cover` was REST-injected with attrs that failed block validation (`dimRatio` vs dim class mismatch / nonstandard cover save HTML). Invalid cover = no Media Replace UI.

**Fix:** Replaced hero `wp:cover` with a valid **group + `wp:image`** stack:
- Click the hero photo → **Replace** works
- Brand / title / CTA overlay via page CSS

**Daniel:** Close the Technology Hub editor tab completely, reopen the page, hard refresh. Do not click Attempt Recovery on the old cover — it should be gone.
