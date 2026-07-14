# Playbook 02 — Menu Diagnosis and Safe Rebuild (No SQL)

## Status update, 2026-07-14

Daniel confirmed he already purges the LiteSpeed Cache plugin inside WordPress
after every day's changes. That rules out the WordPress-side plugin cache as the
cause. It does not yet rule out the separate Hostinger hPanel edge cache layer,
confirmed present via live server headers (`max-age=604800`), since that is a
different purge button in a different location that a WordPress-only routine
would not touch. One hPanel purge is the last caching check before treating this
as data corruption. See Step 0 below.

## Diagnosis, ranked by likelihood

1. LiteSpeed Object Cache, confirmed ON via LiteSpeed Cache Settings, Cache tab
   (Public Cache ON, Private Cache ON, Object Cache ON, Cache REST API ON).
   This is now the leading hypothesis. Unlike Public/Private page cache, which
   never touches wp-admin, Object Cache intercepts WordPress's internal data
   lookups everywhere, including the Appearance and Menus screen itself. If it
   fails to invalidate on save, the admin screen can show stale, empty, or
   reverted menu data. This is a stronger fit for "disappears inside wp-admin"
   than any front-end cache layer.
2. The separate Hostinger hPanel edge cache layer, confirmed present via live
   server headers (`max-age=604800`), not purged by the WordPress plugin's
   Purge All button. Secondary check, explains front-end staleness more than
   the admin screen losing data.
3. Leftover corruption from the earlier SQL edits, the "ghosts." Fall back to
   this only if Step 0 below (Object Cache off) does not resolve it.
4. A staging sync, backup, or migration tool silently restoring an older
   database snapshot on a schedule. Confirm none is active if Step 0 and the
   new-menu rebuild both fail.

## Step 0 — The decisive test (do this first)

1. WordPress sidebar → LiteSpeed Cache → Cache (not Page Optimization) → tab [6] Object.
2. Turn Object Cache OFF. Save Changes.
3. Toolbox → Purge All.
4. Create a one-item test menu in WordPress, save.
5. Open a private browser window, log in, check Appearance and Menus.

If it holds now: Object Cache was the cause. Leave Object Cache off until
launch. The small performance gain from object caching is not worth a caching
layer that can silently erase admin work. Revisit after launch with a proper
purge-on-save discipline if desired.

If it still does not hold after Object Cache is off and cache is purged, this is
corruption, not cache. Move straight to Step 5, corruption path.

## Step 0b — Secondary cache check, only if Step 0 alone does not fully resolve it

1. Log into Hostinger hPanel directly, not WordPress admin.
2. Websites → this site → Performance (or Speed) → Cache → Purge Cache.
3. Repeat the one-item test menu check.

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
