# 10Web migration — read-only probe log (2026-10-05)

Cloud agent run: **10web migration**. No WordPress writes. No plugin changes.

## HTTP probes

```
GET https://tcstaging.truth-collective.com/ → 200
GET https://tcstaging.truth-collective.com/wp-content/plugins/10web-manager/ → 403
GET https://truth-collective.com/wp-content/plugins/10web-manager/ → 404
GET https://tcstaging.truth-collective.com/wp-content/plugins/tenweb-speed-optimizer/ → 404
```

## Homepage HTML

- Staging homepage response: no matches for `10web`, `tenweb`, or `10-web` in HTML (grep on public document).

## REST (staging)

- `GET /wp-json/wp/v2/pages?per_page=1` without auth: **200** (public published pages).
- With environment `TC_WP_USER` + injected 18-character secret:
  - `GET .../users/me` → **401**
  - `GET .../plugins` → **401**
  - `GET .../pages?per_page=1&context=edit` → **401** (`rest_forbidden_context`)

Conclusion: Application Password in this environment is missing, revoked, or not tied to an administrator. Staging structural work requires a new App Password per `docs/TC-STANDING-BRIEF.md` §14.

## Historical baseline (not re-verified today)

From `STAGING-RECOVERY-HANDOFF.md` (2026-08-08):

- 10WEB Manager **Active** v1.20.21 on staging; user pause on deactivate/delete.
- `10web_tmp` absent under uploads (staging and live File Manager).
- ~57KB `tc-explore*` / STAGING PATCH CSS in Additional CSS (recovery issue, not 10Web HTML markers).
