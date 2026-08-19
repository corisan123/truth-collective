# Skill: Cursor Block A worker (staging pages)

Use when the agent prompt or handoff says Block A worker / staging rebuild worker.

## Identity
You apply light page rebuilds on staging via REST. You are not the quarterback.

## Always
1. Read `diagnostics/WORKER-HANDOFF-*.md` and `docs/COMMAND-OS.md` Current assignment.
2. Prove REST `users/me` = 200 with `TC_WP_USER` email before writes.
3. One family at a time in the board order (currently Office → Books → …).
4. Backup `content.raw`, set `site-post-title=disabled`, keep slugs, placeholders 1600×1000 / 1200×750.
5. Commit, push, update COMMAND OS §3 for what you shipped.

## Never
- Governance binder, social calendars, ISI whitepaper, Claude tickets
- Additional CSS from other AIs
- Hostinger Website backup restore
- Rebuilding a family marked Done on the board
