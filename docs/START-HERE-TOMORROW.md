# Start Here — Next Session

Greeting: you are BDM. Read `.cursor/rules/truth-collective.mdc` and `docs/`
first, then continue from this file.

## Where we left off (2026-07-14, end of a 13-hour day)

Big wins today, all verified live:
- Menu disappearing problem: SOLVED. Cause was LiteSpeed page cache, not
  corruption. Rebuilt and holding.
- All 8 `__trashed` office pages: reparented, verified, redirects working.
- Full hub-to-child reparenting across all 6 hubs: COMPLETE and verified.
- Hub placement rule locked; hub structure for all 6 hubs settled.

## Tomorrow, in order

1. FIRST, quick win (5 minutes): Fix the AI hub canonical.
   - Follow `docs/playbooks/01-ai-hub-canonical.md` exactly.
   - Why first: the AI hub is invisible to Google right now because its canonical
     points to a dead 404 URL. One field change fixes it and puts the hub back
     in the sitemap.

2. THEN, the three money pages (the real revenue work).
   - Best Executive Desk Setup: `/office-workspace-products-and-tools/executive-desk-setup/`
   - Best Executive Office Chairs and Seating: `/office-workspace-products-and-tools/executive-office-chairs-seating/`
   - Best Monitors and Premium Displays: `/technology-hub/monitor-display/`
   - BDM will audit each from staging and return a punch list per page.

## Small cleanups to fit in when convenient

- Remove the leftover "DRAFT 6 15 2026" text in the Video Technology page title.
- Confirm the 2 Self-Help URLs (the non-monetized Recovery/Resources page, and
  the 16-book curated page).
- Confirm the exact split of the 5 non-monetized pages so the count reconciles.

## Do not forget

- Never SQL. Menus and parents via WordPress UI only.
- Purge both caches (LiteSpeed plugin Purge All + hPanel Flush Cache) after any
  structural change, then verify in a private window.
- Do not install the WordPress 7.0.1 core update yet.

Rest well. Harrison comes first.
