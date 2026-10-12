# Local CPU backups: review first. Staging restore only after a matching set passes.

**Prepared:** 12 October 2026  
**Lanes (locked):** Truth Collective = Cursor **Cloud** + REST, staging only, until TC is stable. ISI Consulting = Cursor **Desktop** only. Those two must not mix.

**Question:** Can Daniel open a local pre-migrate backup, review it, and if it looks good, give it to Cloud so Cloud stops rebuilding child pages and only does styling with Claude?

**Short answer:** Opening and reviewing a copy on the PC is the right next step. Using it as a full stop-rebuild on Hostinger staging is only safe after a **complete same-timestamp set** is proven healthy. Do not restore onto live. Do not restore a single slice. Do not stop REST rebuild on a backup that has not passed that check.

---

## 1. Lanes

| Place | Work | Forbidden |
| --- | --- | --- |
| Cursor Cloud (this run) | Truth Collective staging via REST | ISI files, ISI engines, Desktop writes to staging |
| Cursor Desktop | ISI Consulting only | Truth Collective REST, staging, Additional CSS, WP admin |

Do not bring ISI `math.js` / engine-bus into TC. Do not open TC staging from Desktop until Daniel lifts this lock after TC is stable.

---

## 2. Yes: open a local copy and review it (read-only)

The WordPress/Updraft copies on the **server** are gone or rotated. The remaining originals are on the PC / Drive. Reviewing those copies does **not** write to staging or live.

**Safe ways to look:**

1. **Do not** click Hostinger Website Backup Restore (that path hits **live**).  
2. **Do not** click Updraft Continue on staging.  
3. On the PC, pick **one timestamp** and gather **every** slice with that stamp: `-db` + `-uploads` (+ `-uploads2` if split) + `-plugins` + `-themes` + `-others`.  
4. Best windows: **23 July 2026 19:30** (Drive `-db.gz` already hashed) and **24 July 2026 16:59** (closest to migrate; two ~392 MB files in the folder shot).  
5. Open the `-db.gz` as a file (gunzip / 7-Zip). Search the SQL for `tc-overlay-card`, `amzn.to`, Emerging Technologies, Computers. That is a content check, not a website view.  
6. Open the uploads zip and confirm `wp-content/uploads/2026/07/` product JPGs exist.  
7. Optional visual review: install the **full matching set** into **Local WP / Local by Flywheel on the PC only**. Never point that install at Hostinger. If that local site looks like the pre-migrate catalogs, the set is a candidate.

Sending the **23 July `-db.gz`** (~19 MB) into this Cloud chat is useful. Cloud can count pages, classes, and Amazon codes in SQL. Cloud cannot ingest two 392 MB upload zips through the 20-file chat cap.

---

## 3. Issues with “give it to Cloud and stop rebuilding”

| Issue | Why it matters |
| --- | --- |
| Incomplete set | The 30 June file already sent was `-others` only (LiteSpeed crumbs). Restoring crumbs does nothing. Restoring **uploads without the matching db** already crushed Computers (Hostinger 24 Jul uploads restore). |
| Size / path | Cloud REST cannot load a full WordPress dump. Chat cannot take ~800 MB of uploads. A real restore is Daniel in Hostinger (staging files + DB), or a local PC WordPress, not a REST paste. |
| Wrong night | 12 July and 30 June are real but earlier than the migrate-ready site. Prefer 23 Jul 19:30 or 24 Jul 16:59. |
| Dirty 24 Jul | If 10Web had already installed Manager or started a migrate that evening, 16:59 might not be clean. SQL/class counts decide. |
| Live vs staging | Website Backup Restore targets **live**. Live stays untouched. |
| Stopping REST too soon | If the restored staging is still missing children, Cloud would freeze a gutted tree and call it done. Inventory first (page tree, overlay class counts, July image 200s), then styling. |
| Additional CSS | Customizer CSS survived the crash. A full files restore might replace it. Snapshot Additional CSS before any staging restore. |
| 10WEB Manager | A pre-25 Jul set might not include Manager; a 24 Jul evening set might. After restore, check plugins. Do not leave Manager Active. |
| Claude styling | Copy/tighten only after structure matches the backup. Otherwise Claude writes onto empty shells. |

---

## 4. When Cloud **should** stop the REST rebuild

Only after **all** of these:

1. One timestamp, all slices, hashes written down.  
2. Database search shows content-heavy pages (65-plus URLs or close), `tc-overlay-card` / product classes, catalogs, child titles that are missing on live REST today.  
3. Matching uploads contain July 2026 product files.  
4. Optional: local PC WordPress of that set looks like pre-migrate.  
5. Daniel restores that **same** set onto **staging only** (files + DB together), not live, not Website Backup Restore.  
6. Cloud re-runs REST census: published tree, class counts, sample image URLs.  
7. Snapshot Additional CSS. Deactivate 10WEB Manager if it returned.

Then Cloud’s job becomes: compare restored staging to the Vercel/PDF visual lock, styling and Claude copy only. No more inventing missing children by hand.

Until step 6 passes, Cloud keeps the current lock: do not Hostinger-restore; do not stop looking for catalogs in revisions and local SQL.

---

## 5. What to do this week (order)

1. Keep ISI in Desktop. Keep TC in this Cloud run.  
2. On the PC, open **23 July `-db.gz`** (already hashed). If it is heavy, send that one file here.  
3. Hash the 24 July zips (`Get-ChildItem ...\*.zip | Get-FileHash`).  
4. Do not restore anything onto Hostinger until Cloud or a local WP install has seen a complete set.  
5. Do not give Cloud “the whole backup” as 20 random files from plugins (that was the Code Snippets batch).
