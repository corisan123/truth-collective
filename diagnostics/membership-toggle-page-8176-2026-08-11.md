# Membership Toggle page (draft 8176) — 2026-08-11

**URL:** https://tcstaging.truth-collective.com/?page_id=8176&preview=true  
**WP:** page `8176` — title `Toggle Page` — status **draft** — slug `toggle-page`  
**Scaffold HTML/JS:** `diagnostics/scaffolds/page-8176-membership-toggle.html`  
**Styles (from Additional CSS / page CSS):** `diagnostics/scaffolds/page-8176-membership-toggle-styles.css`  
**Backup:** `diagnostics/backups/page-8176-toggle-preview-2026-08-11.html`

## What it is
Locked gold **Preview / Full content** membership gate Cursor built (Vercel/10Web light look):

- Toggle: Preview ↔ Full content  
- Visitor card: teaser editorial + MailerLite join (name optional + email)  
- Member gate: unlock form until joined  
- Unlocked panel: full editorial placeholder + session email + Reset  
- Session via `localStorage` (`tc_member_session`)  
- MailerLite action same list as Quarterly Review signup:  
  `https://assets.mailerlite.com/jsonp/2310667/forms/190738396377777459/subscribe`

## vs Quarterly Review signup (`6747`)
| | Toggle page `8176` | Signup pattern `6747` |
|--|-------------------|------------------------|
| Job | Email-gate a long editorial | Simple newsletter subscribe card |
| UI | Preview/Full toggle + unlock | Single “Join the Quarterly Review” card |
| Classes | `tc-membership` / `tc-toggle` | `tcj-signup` / `tcj-*` |

Keep both. Do not collapse them into one block.

## Status
Draft demo page. Not published. Styles currently live in site CSS (extracted snapshot saved). Ready to reuse when Daniel places a real editorial inside `.tc-unlocked`.
