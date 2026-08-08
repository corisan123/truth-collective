# Homepage link inventory S0b — 2026-08-08

**Source:** Cursor live HTML parse (Angie could not see the site).  
**Daniel:** first three major child blocks re-linked and working.

## Flagged issues (positive next fixes)

| Issue | Detail | HTTP |
|-------|--------|------|
| Leadership CTA | Was “Explore the Leadership Collection” → `/`. **2026-08-08 REST recheck:** phrase gone; hub already → `/recommended-books-2026/leadership-books/` | **200** |
| Featured Productivity | `/featured-productivity-tools/` (`data-id=109` invalid) still on homepage — propose → `/productivity-tools/` (`5680`) | **404** |
| Podcast slug split | `/ai-mastery-podcast-collection/` (200) vs `/ai-mastery-collection-podcast/` (301) | split |
| Old books path | `/recommended-books/` | 301 → newer |
| Self-help old path | `/recommended-books/self-help-and-mental-wellness/` | 301 |
| Card alts | Image links often labeled “Home \| Truth Collective in 2026” | SEO/a11y |

**Hub tiles that return 200:** office, technology-hub, smart-lighting, productivity-tools, self-help-and-mental-wellness, recommended-books-2026, ones-who-gave-everything, the-truth-untold, tablets child.

## Card / Explore-style destinations (main hubs)

| Label (best) | href | HTTP |
|--------------|------|------|
| Smart Lighting (image) | `/smart-lighting/` | check below |
| Technology Hub (image) | `/technology-hub/` | |
| Productivity Tools (image) | `/productivity-tools/` | |
| Ones Who Gave Everything | `/ones-who-gave-everything/` | |
| Rev. Billy Graham | `/ones-who-gave-everything/reverend-billy-graham/` | |
| AI Mastery Podcast | `/ai-mastery-collection-podcast/` | |
| Truth Untold | `/the-truth-untold/` | |
| Explore buttons | smart-lighting, productivity, office, self-help, recommended-books-2026 | |

Full numbered parse saved in session; see git history / this file updates.
