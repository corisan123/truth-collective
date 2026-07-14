# Playbook 02 — Menu Diagnosis and Safe Rebuild (No SQL)

## Diagnosis, ranked by likelihood

1. Caching, most likely. Staging headers confirm Hostinger's server-level
   LiteSpeed cache with `max-age=604800` (7 days), a layer separate from the
   LiteSpeed Cache plugin inside WordPress. A menu that appears to disappear
   after saving is a classic caching symptom. Two cache layers must both be
   purged, not just one.
2. Leftover corruption from the earlier SQL edits, the "ghosts." Possible if the
   cache purge test below does not resolve it.
3. A staging sync, backup, or migration tool silently restoring an older
   database snapshot on a schedule. Confirm none is active before ruling this in.

## Step 1 — Purge both cache layers now

- hPanel (Hostinger) → Websites → this site → Performance → Cache → Purge Cache.
- WordPress admin → LiteSpeed Cache plugin → Toolbox → Purge All.

## Step 2 — Confirm admin is excluded from caching

- LiteSpeed Cache plugin → Cache tab → confirm no setting caches wp-admin pages.
- If Object Cache (Redis or Memcached) is enabled, confirm it does not cache
  admin-ajax requests, and that TTL is short if it applies at all.

## Step 3 — Isolation test before rebuilding

1. Purge both caches (Step 1).
2. Create one new menu named `Primary Navigation Test`.
3. Add exactly one item (Home).
4. Save.
5. Purge both caches again.
6. Close the tab completely. Open a new private/incognito browser window.
7. Log in and open Appearance → Menus.
8. Confirm the one item is still there.

If it holds: caching was the cause. Proceed to the full rebuild in Step 4 with a
cache purge immediately after every save.

If it does not hold: this is data corruption, not cache. Do not keep editing the
same menu. Go to Step 5.

## Step 4 — Full rebuild (cache was the cause)

1. Purge both caches.
2. In the same `Primary Navigation Test` menu (or a fresh one), add every item
   from the target structure in `docs/page-inventory.md`.
3. Set every parent and sub-parent relationship using drag position and the
   Menu Structure indentation, not a separate parent field. WordPress menus
   nest by indentation in this screen.
4. Assign the menu to the theme's Primary location under Manage Locations.
5. Save once.
6. Purge both caches immediately.
7. Verify in a private window before declaring it done.

## Step 5 — Full rebuild (corruption, not cache)

1. Do not attempt to repair the damaged menu.
2. Create a brand new menu with a new, different name than any prior attempt.
3. Rebuild fully per Step 4, steps 2 through 7.
4. If the new menu also fails to hold after a confirmed cache purge, this is
   beyond a safe self-serve fix. Do not resort to SQL. Contact Hostinger support
   and ask them to check for corrupted `nav_menu_item` posts or a scheduled
   restore task running against the database. This is the one case where
   escalating to hosting support is correct, since it avoids SQL entirely.

## Never do

- Never edit `wp_posts`, `wp_postmeta`, `wp_terms`, or `wp_term_relationships`
  directly.
- Never trust a menu save without a private-window verification afterward.
