# WORKER HANDOFF — Block A (2026-08-19)

**To:** Cursor Cloud Agent on `cursor/computers-and-isi-b513` (Block A worker)  
**From:** Cursor lead / quarterback  
**Charter:** `docs/COMMAND-CHARTER-2026-08-19.md`

## Auth

Secrets work when `TC_WP_USER=dreid1253@yahoo.com` + valid Application Password.  
If 401 on every user variant, restart after secret edit. See `diagnostics/REST-AUTH-GATE-2026-08-19.md`.

## Already done on staging (do not redo)

- Technology children (Computers + AV family)
- Smart Lighting children: 4863, 4877, 4896, 5099, 4886 (light scaffolds + title cleanup)
- Dual H1 cleared on Productivity `5680`, Ones Who Gave `5897`, AI Podcast `7694` (`site-post-title=disabled`)
- Tickets: `diagnostics/REST-smart-lighting-children-apply-2026-08-19.md`

Lead briefly stepped into your lane to clear the REST-auth stall. From here, **you own Block A apply.** Lead does not rebuild the next page family unless you are blocked.

## Your next family (only)

**Office Workspace children** (parent hub ~5939 / `/office-workspace-products-and-tools/`).

Expected six children (confirm via REST `parent=` before edit). Pattern: clone Technology/Lighting child light shell; placeholders 1600×1000 / 1200×750; one H1; `site-post-title=disabled`; backup before write; commit/push.

Then: Books children → Self-Help / Productivity children → Home / About / Contact cleanup.

## Do not

- Start ISI site work, Claude tickets, governance binder, or social calendar
- Touch Additional CSS from other AIs
- Restore Hostinger Website backups
- Edit Smart Lighting or Technology children again unless lead assigns a defect fix

## Parallel (encouraged)

While you do Office, Daniel may also run:
- Worker B on ISI only (`diagnostics/WORKER-B-ISI-HANDOFF-2026-08-19.md`)
- Multiple Claude tickets from `docs/SWARM-LAUNCH-PACK.md`

You stay on TC Block A only.

## Paste prompt for worker restart

```
You are the Truth Collective Block A worker under docs/COMMAND-OS.md and docs/COMMAND-CHARTER-2026-08-19.md.
Read diagnostics/WORKER-HANDOFF-2026-08-19.md and .cursor/skills/cursor-block-a-worker/SKILL.md.
Confirm REST users/me = 200 with TC_WP_USER email.
Skip Smart Lighting (already applied). Next: Office Workspace children light rebuild only.
Commit, push, update docs/COMMAND-OS.md §3. Stop when Office children are live and documented.
```
