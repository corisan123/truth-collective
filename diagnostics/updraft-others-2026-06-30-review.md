# Updraft `others` zip — 30 June 2026 19:30

**Reviewed:** 12 October 2026  
**File received:** `backup_2026-06-30-1930_The_Truth_Collective_11b0badf493f-others.zip` (178,006 bytes / 174 KB on disk; 181,420 bytes uncompressed; 30 entries; zip is complete).  
**Listing:** `diagnostics/backup-listings/backup_2026-06-30-1930-others-listing.txt`  
**Folder exhibit:** `docs/legal/exhibits/exhibit-pc-updraft-folder-2026-10-12.png`

## What this archive is

An **UpdraftPlus “others” slice**. Updraft splits a full backup into `db` / `plugins` / `themes` / `uploads` / `others`. This zip is only leftover `wp-content` items that are not plugins, themes, or media.

Contents:

| Path | Role |
| --- | --- |
| `litespeed/` | LiteSpeed Cache crumbs (`qc.last.*`, debug `index.php`, robots.txt) |
| `jetpack-waf/` | Jetpack WAF stubs (May 14 2026) |
| `fonts/montserrat/*.woff2` | Montserrat webfonts (May 18 2026) |
| `object-cache.php` | LiteSpeed object-cache drop-in |
| `.litespeed_conf.dat` | LiteSpeed config blob |
| `mcp.log` | Hostinger Tools MCP: `wordpress.website.updated` (7 June 2026 15:28). Two identical events. Not a 10Web log. |
| `upgrade-temp-backup/` | Empty WordPress upgrade temp |
| `index.php` | Standard silence file |

Internal zip timestamps: 30 June 2026 23:46 UTC. Filename `1930` matches evening local time.

**Not in this zip:** database, `wp-content/uploads`, themes, plugins, Additional CSS, page HTML, `tc-*` CSS, product images.

## Screenshot of the folder (PC)

Windows listing shows **sets** of Updraft zips, not one file:

- **24 Jul 2026 5:00–5:01 PM** — two ~392 MB zips (almost certainly `uploads`) plus a **10,774 KB** zip (boxed) and a 50,111 KB zip. This is the day-before-migrate window.
- **23 Jul 2026 7:30 PM** — 19,827 KB
- **12 Jul 2026 7:30 PM** — 17,391 KB
- **30 Jun 2026 7:30–8:00 PM** — several ~330–406 MB zips plus a 10,774 KB zip (same size as the boxed 24 Jul file) and a 47,132 KB zip

Those ~392 MB archives are the ones that would hold media. This `-others` file is the small leftover slice from the **30 Jun 19:30** set. It is **not** the boxed 10,774 KB file (that file is from **24 Jul 16:59** and is the size of a typical `plugins` slice, not `others`). The 10,774 KB size also appears on the 30 Jun row; same size does not mean same bytes.

## Truth limits

- This file **does not** prove the 24–25 July migrate-source site is intact inside it.
- It **does** prove Daniel still has **local Updraft copies dated before 25 Jul 2026** on the PC. If Hostinger/Updraft **on the server** later lacked healthy copies, that is a separate fact from “no copies exist anywhere.”
- Do not restore any of these into live or staging until the matching **db + uploads** from the **same timestamp** are identified.

## Next zip to send (keep under 20 files; one zip is enough)

Best: `backup_2026-07-24-1659_The_Truth_Collective_…` that is **not** 392 MB (the 10,774 KB boxed file, or a file whose name ends in `-db` / `-plugins` / `-themes`).  
Or: the matching `-db` from `2026-06-30-1930` so this `others` slice has a database to pair with.
