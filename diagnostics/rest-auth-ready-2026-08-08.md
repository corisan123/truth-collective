# Staging REST auth — ready (2026-08-08)

**Site:** `https://tcstaging.truth-collective.com`  
**Auth method:** WordPress Application Password via REST Basic Auth  
**Username that works:** account **email** (`dreid1253@yahoo.com`), not the user slug  
**User:** id `1` · slug `dreid1253yahoo-com` · roles administrator  
**Capabilities confirmed:** `edit_pages`, `edit_others_pages`, `publish_pages`, `edit_theme_options`  
**Front page:** id `5` (`home`)

## Security
- Application Password is session-only for Cursor. **Do not commit credentials to git.**
- Daniel shared the main login password earlier in chat — **change that main password** in Users → Profile after REST is stable. Keep/revoke Application Passwords separately.
- Revoke App Password anytime: Users → Profile → Application Passwords → Revoke.

## Auth note
Using the WP user **slug** with the App Password returned `rest_not_logged_in`. Using the **email** + App Password returns 200.

## First proposed write (awaiting Daniel Approve)
Homepage id `5` — only bad internal link found in current `post_content` scan:

| Before | After | Why |
|--------|-------|-----|
| `/featured-productivity-tools/` (`data-id="109"` — invalid/deleted) | `/productivity-tools/` (`data-id="5680"`) | Target 404 → published Productivity Tools page 200 |

**Leadership CTA:** prior inventory flagged “Explore the Leadership Collection” → `/`. Current raw + rendered homepage: that phrase is **gone**; leadership explore hub already points to `/recommended-books-2026/leadership-books/` (200). No Leadership REST edit needed unless Daniel still sees the old CTA in browser cache.

## Rule
No REST writes until Daniel says **Approve** for a named ticket (e.g. `REST-home-productivity-link`).
