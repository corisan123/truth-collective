# Playbook 04 — Reparent the 8 Trashed Office Pages (No SQL)

## Status update

The menu rebuild held after the Object Cache off + Flush Cache sequence. Cache
was confirmed as the cause of the earlier disappearing menu, not database
corruption. Continue purging both layers after every future structural change.

## The 8 pages, matched by slug to Daniel's titles

| # | Daniel's title | Slug (unchanged by this fix) | Current broken URL |
| --- | --- | --- | --- |
| 1 | Best Analog Writing Tools | `best-analog-writing-tools` | `/best-office-workspace-products-tools__trashed/best-analog-writing-tools/` |
| 2 | Best Monitor Setup and Display | `monitor-display` | `/best-office-workspace-products-tools__trashed/monitor-display/` |
| 3 | Cable Management, Executive Enterprise Setups 2026 | `cable-management` | `/best-office-workspace-products-tools__trashed/cable-management/` |
| 4 | Premier Audio and Video Workspace 2026 | `audio-and-video` | `/best-office-workspace-products-tools__trashed/audio-and-video/` |
| 5 | Executive Style Desks and Setup | `executive-desk-setup` | `/best-office-workspace-products-tools__trashed/executive-desk-setup/` |
| 6 | Premium Quality Projectors and Microphones for 2026 | `projectors-and-microphones` | `/best-office-workspace-products-tools__trashed/projectors-and-microphones/` |
| 7 | Top Ranked Executive Office Chairs and Seating | `executive-office-chairs-seating` | `/best-office-workspace-products-tools__trashed/executive-office-chairs-seating/` |
| 8 | Top Quality Office File Cabinets, Credenzas, and Filing Essentials | `office-file-cabinets-credenzas-essentials` | `/best-office-workspace-products-tools__trashed/office-file-cabinets-credenzas-essentials/` |

New parent for all 8: **Office Workspace Products and Tools**
(`/office-workspace-products-and-tools/`).

## Why the Parent dropdown shows blank on these pages

Confirmed by Daniel on the first page (Best Analog Writing Tools): the Parent
dropdown in Quick Edit shows no parent selected. This is expected and does not
block the fix. WordPress appends `__trashed` to a page's own slug automatically
when that page is sent to trash, to free the clean slug. These 8 pages are
children whose parent post was trashed this way, likely a page originally
titled close to "Best Office Workspace Products and Tools" or similar, now
sitting in the Trash. The Quick Edit Parent dropdown only lists non-trashed
pages, so it cannot display or select that now-invalid parent, and shows blank.

This does not block anything. Select the new parent, **Office Workspace
Products and Tools**, in that same dropdown regardless of the blank starting
state, and click Update as planned. This overwrites the broken link to the
ghost parent.

After all 8 are reparented, check Pages, Trash, for the leftover ghost parent
page (likely matching the `best-office-workspace-products-tools` slug root).
Once confirmed no page still needs it, permanently delete it from the Trash to
remove the ghost.

## Exact steps, repeat for each of the 8 pages

1. Go to Pages in the WordPress admin.
2. Find the page by its title from the table above.
3. Hover over the title, click Quick Edit.
4. Find the Parent dropdown.
5. Select **Office Workspace Products and Tools**.
6. Click Update.
7. Watch for the RankMath notice that a slug or URL change occurred. RankMath
   auto-creates a redirect when this happens, the same behavior already seen on
   this site. Confirm it fired for this page before moving to the next one.

Repeat for all 8. Do this one page at a time, do not batch-edit, so each
RankMath redirect notice can be confirmed individually.

## Canonical URL, per page, checked right after its own parent change

Do not delete or pre-edit the Canonical URL field before reparenting. Changing
the Parent and clicking Update changes the page's URL automatically, and
RankMath auto-creates a 301 redirect from the old `__trashed` URL to the new one.
Leave that redirect in place.

After each page's parent change, open its RankMath panel, Advanced tab,
Canonical URL:

- If the field is empty, nothing to do. An empty field means RankMath uses the
  page's own current URL automatically, so it already reflects the new address.
- If the field has text in it matching the old `__trashed` URL, clear it back to
  empty so it falls back to automatic. Do not hand-type the new URL unless a
  hardcoded canonical is specifically wanted.
- Save again only if this field was changed.

## After all 8 are reparented

1. Go to RankMath, Redirections.
2. Confirm 8 new redirect entries exist, each old `__trashed` URL to the new
   `/office-workspace-products-and-tools/{slug}/` URL, status 301.
3. If any is missing, add it manually in Redirections rather than leaving a dead
   link.
4. Purge cache both ways: LiteSpeed Cache plugin, Toolbox, Purge All, and
   hPanel, WordPress, Overview, Flush Cache.
5. Open each of the 8 new URLs in a private window and confirm HTTP 200 and the
   correct page content.
6. Open each of the 8 old `__trashed` URLs in a private window and confirm they
   301 redirect to the new URL.

## Add them back into the menu

In Appearance and Menus, add all 8 pages under **Office Workspace Products and
Tools** as children, using the same indentation you used for the other nested
sections (Recommended Books and its categories, for example). Save. Purge cache
both ways again. Verify in a private window.

## Update the source of truth once done

Report back the 8 new confirmed URLs. `docs/page-inventory.md` and
`docs/site-structure.md` will be updated to remove this as an open launch
blocker.
