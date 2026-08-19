# REST auth gate note (2026-08-19)

**Staging:** `https://tcstaging.truth-collective.com`  
**Probe:** `GET /wp-json/wp/v2/users/me?context=edit`

## Working credentials (this Cloud Agent run)

| Secret | Value that works |
|--------|------------------|
| `TC_WP_USER` | `dreid1253@yahoo.com` (email, not slug) |
| `TC_WP_APP_PASSWORD` | Application Password from WP Profile (spaces OK; length ~29 with spaces) |

Auth result here: **HTTP 200**, user id `1`, slug `dreid1253yahoo-com`.

Slug variants (`daniel`, `dreid1253`, `admin`) return **401** `rest_not_logged_in` even with a valid password.

## If another agent still gets 401

1. Confirm `TC_WP_USER` is exactly `dreid1253@yahoo.com`.
2. Confirm `TC_WP_APP_PASSWORD` is the full Application Password (all groups). Do not commit it to git.
3. **Restart / re-run** the agent after editing secrets. Secrets inject at start.
4. Only if still 401: WP Admin → Users → Profile → Application Passwords → create a new one (name e.g. `Cursor Cloud`), paste into the Cursor secret `TC_WP_APP_PASSWORD`, revoke the old one, then re-run.

This is not a Hostinger File Manager permission issue.

## Do not

- Put the Application Password in the repo or tickets beyond placeholders
- Use Website backup restore to fix REST auth
