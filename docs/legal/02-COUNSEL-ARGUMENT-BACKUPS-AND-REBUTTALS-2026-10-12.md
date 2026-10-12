# Counsel argument — 10Web, WP access, and why restores did not return the migrate-source site

**Prepared:** 12 October 2026  
**Compiler:** Cursor Cloud Agent `bc-3c3a1616-bd53-407e-8562-11da050498f8`  
**Owner:** Daniel Reid, `contact@truth-collective.com`  
**Tickets:** `#375660` (escalation `#380201`)  
**Not a legal opinion, not an expert affidavit, not a damages model.**  
Every sentence below is either a document this agent has seen, a measurement logged in this repo, or labeled **owner testimony**. If a fact is not in those three buckets, it is not stated as fact.

**12 Oct correction (controlling):** Do not use “65 pages” as the size of the site. Use US Letter scale (about 3,575 to 6,500-plus letter pages). Do not treat Technology Hub as the bound of destruction. Child and sub-child pages remain missing or gutted; REST cannot revive posts that are gone. The only vendor documented inside WordPress during the migrate is 10Web. Do not say CSS classes were intact: Additional CSS **text** remained; class-to-Gutenberg/Kadence **binding** broke. Full replacement language: `03-CORRECTIONS-SCALE-MISSING-PAGES-ACTOR-2026-10-12.md` and `04-CSS-CLASS-BINDING-VS-STYLESHEET-2026-10-12.md`.

---

## 0. What arrived today (the zip you just sent)

**File:** `backup_2026-06-30-1930_The_Truth_Collective_11b0badf493f-others.zip`  
**On disk here:** 178,006 bytes (174 KB). Uncompressed: 181,420 bytes. 30 entries. Complete zip.

This is an **UpdraftPlus `others` slice**, not a website restore package. Updraft splits one backup into `db` / `plugins` / `themes` / `uploads` / `others`. This archive holds leftover `wp-content` crumbs only:

- LiteSpeed Cache drop-in `object-cache.php` and `.litespeed_conf.dat`
- Jetpack WAF stubs dated 14 May 2026
- Montserrat webfonts dated 18 May 2026
- `mcp.log` (Hostinger Tools MCP: `wordpress.website.updated`, 7 June 2026)
- empty `upgrade-temp-backup/`

Internal zip timestamps: 30 June 2026 23:46 UTC. Filename `1930` matches evening local time.

**Not in this zip:** the WordPress database, `wp-content/uploads`, themes, plugins, Additional CSS, page HTML, `tc-*` classes, or product images.

This 174 KB file is **not** the boxed **10,774 KB** archive in the Windows listing. The boxed file is a different slice from the **24 Jul 2026 16:59** set.

Full listing: `diagnostics/backup-listings/backup_2026-06-30-1930-others-listing.txt`.  
Review note: `diagnostics/updraft-others-2026-06-30-review.md`.

**Do not restore this zip (or any of these zips) into staging or live.**

---

## 1. The case in six sentences (use this as the cover)

10Web was hired to polish and copy an existing Hostinger staging WordPress site (`tcstaging.truth-collective.com`), not to regenerate it with AI Builder. Their automated migrator failed and disconnected; their AI flow created fake Builder sites (`active-bluegill.10web.cloud`, later `kind-louse.10web.cloud`) after Daniel forbade AI Website Builder in writing. Nazeli Sargsyan then **required** a temporary WordPress admin (`support@10web.io`) so 10Web could migrate **from our end** (27-28 July 2026 emails). After that access window, staging was not the pre-migration build (8 August 2026 diagnosis: overlay classes stripped, July media 404s, stale hub permalinks, `10web_tmp`, 10WEB Manager still Active). Hostinger and Updraft restores logged success but **did not return** the working migrate-source site; a 24 July uploads restore made Computers worse; an Updraft 28 July `db.gz` was **missing from disk**. On 30 September 2026 10Web admitted the migration was not completed, recast the access **they had demanded** as Daniel providing and authorizing Migration Assistant, admitted they **used Updraft**, denied destroying the site or backups, and refused a three-month refund.

That is the 10Web case this file can support. It is documentary and technical. It is not a verdict.

---

## 2. Most damaging evidence (ranked, with sources)

Use these in this order. Do not lead with SKU counts or medical facts. Lead with documents 10Web wrote.

| Rank | What it shows | Why it hurts 10Web | Source |
| --- | --- | --- | --- |
| 1 | 10Web **demanded** WP admin, then later said Daniel **provided** it | Documentary contradiction on who required the write window | PR #6 exhibits p17/p18 vs 30 Sep letter |
| 2 | Automated migrate **failed / disconnected**; product told him to contact support | The paid migrator did not complete; humans then entered WP | Daniel 26 Jul on the Nazeli thread (p18); ticket `#375660` |
| 3 | AI Builder fake sites (`active-bluegill`, `kind-louse`) after a written ban | They generated a foreign site instead of copying his | p18; 3 Aug chat index; 8-9 Aug freeze note |
| 4 | 10WEB Manager **Active v1.20.21** on 8 Aug; folder `uploads/10web_tmp` existed then vanished after the 24 Jul uploads restore | Write residue on the Hostinger tree they were not supposed to rebuild | `STAGING-RECOVERY-HANDOFF.md` |
| 5 | 8 Aug measured staging: Computers **0** product overlay classes; July upload files **404**; hub hrefs 404 while pages still existed; Tech Hub **16** tiles vs **8** real children | Condition after the access window, before Cursor August rebuilds | 8 Aug diagnostics on this branch |
| 6 | 30 Sep letter: migrate **not successfully completed**; refund refused; DNS-unchanged used as a shield | Incomplete service plus a defense that does not address staging-file writes | T-03 |
| 7 | Backup safety net failed **and** 10Web admits they used Updraft while holding WP admin | Restores did not return the migrate-source; they had the backup plugin | Handoff restore table; BDM testimony; T-03; local PC listing 12 Oct |
| 8 | Customizer **stylesheet text** still 57,615 chars (SHA identical 8 Aug-23 Sep). That is **not** intact class binding. Remaining `tc-*` names often sit on the wrong Gutenberg or Kadence node, so hover/overlay does not fire. About three pages still work. | Stops the defense “CSS was fine.” Pairs with Kadence fatal + 10Web Manager on 7 Aug | `04-CSS-CLASS-BINDING-VS-STYLESHEET-2026-10-12.md` |

Rank 1 plus Rank 2 plus Rank 3 plus Rank 6 is the strongest **document** package. Rank 5 is the strongest **condition** package. Rank 7 is the backup theory. Rank 7 is **not** closed as "10Web deleted every Hostinger file." See §4.

---

## 3. Point-by-point rebuttal of the 30 September letter

Nazeli 30 Sep 2026 16:09 GMT+4 (exhibit T-03). Each row: their claim, then the truthful counter.

### 3.1 "Daniel provided WordPress administrator access and expressly authorized Migration Assistant"

**Counter:** On 27-28 July Nazeli wrote that **to proceed** Daniel must create a temporary administrator using `support@10web.io`, send login URL and credentials, and that 10Web would **access the existing WordPress dashboard** and migrate **from our end**. That is a vendor demand after **their** automation failed, not an unsolicited customer request. Authorization extracted as a condition of continuing a failed paid migrate is not the same story as "the customer insisted we enter WordPress." The 30 Sep letter does not quote 10Web's own demand language.

### 3.2 "Our records do not support that 10Web destroyed the site or deleted backups"

**Counter:** This is a denial, not a proof. What the record **does** support:

- They had WP admin (they admit the access; July emails show they required it).
- They admit they **used Updraft**.
- 10WEB Manager was still Active on staging on 8 August.
- `10web_tmp` existed under staging uploads, then was gone after a 24 July uploads restore.
- Public staging on 8 August was not the pre-migration Computers / hub build.
- Hostinger restores of files (1 Aug), DB (28 Jul), and uploads (28 Jul and 24 Jul) logged success and **did not** return the working site.
- Updraft archive `backup_2026-07-28-1945_…-db.gz` was **missing from disk** when a restore was attempted (handoff hard rule: do not Continue).

None of those facts require a confession. Together they show: 10Web had write access, used the backup plugin, left plugin residue, and the rollback copies that remained on the **server** were not the working migrate-source.

**What this still does not prove:** a File Manager log naming a 10Web user as the actor who deleted a specific `backup_*.zip` on disk. That remains **GAP G-58 / G-59**.

### 3.3 "We used Updraft only to create a new backup for migration; we did not restore over source"

**Counter:** Creating a new Updraft archive when the plugin holds only X copies **drops the oldest remaining archive**. 10Web’s own sentence is the deletion mechanism for the healthy checklist backups Daniel had just verified. A new backup taken **after** Manager / Migration Assistant / AI writes also snapshots the **damaged** tree. After about 3 August, scheduled backups of that damaged tree kept rotating until the 10 October dump showed nothing before 15 September.

Creating a backup also does not explain why a 24 July uploads restore **crushed Computers worse**, or why the 28 July Updraft `db.gz` was already **missing from disk in August**.

### 3.4 "We did not change DNS; the source remained live"

**Counter:** DNS is irrelevant to staging-file damage. `tcstaging` is a Hostinger subdirectory. Manager, Migration Assistant, and wp-admin writes do not need a DNS cutover. The safety rule (do not publish / do not touch live DNS) was **our** rule. Leaving DNS alone does not mean `public_html/tcstaging` was untouched.

### 3.5 "Admin access was later revoked, so we could not continue"

**Counter:** Revoking access **after** the damage window does not undo writes during the window. 10WEB Manager still Active on 8 August is evidence the plugin relationship outlived the "we could not continue" sentence.

### 3.6 "Migration was not successfully completed" (they admit this)

**Use this.** Incomplete migrate is not a defense. It is the service failure. They then entered WordPress "from our end" **because** the migrator failed. The incomplete job is the damage window, not a reason they owe nothing.

### 3.7 One-month subscription extension "is not an admission"

**Note only.** Counsel can treat a paid extension after a failed migrate as a commercial fact. This agent does not spin it into an admission. The useful admission is already in the same letter: migrate **not successfully completed**.

---

## 4. Backup replacement — checklist copies, 10Web’s new Updraft saves, damaged-site rotation

Controlling write-up: `05-BACKUP-RETENTION-REPLACEMENT-2026-10-12.md`.

### 4.1 Owner testimony (12 October 2026, this Cloud run)

Finding a save from the day before 25 July is hard. Daniel and Cursor/Claude spent about six days locating the July Cursor conversation and any remnants. Older CPU copies (30 June, 12 July) water down the 7/25-ready site; they do not show the building that continued up to migrate day.

To fulfill the Cursor migrate checklist and free disk, that same Cursor agent told him to **delete older automated plugin backups** after he **opened and verified** new pre-migration backups as intact. That Layer 1 deletion is owner + Cursor, not 10Web.

10Web then entered WordPress. By their own 30 September admission they **used Updraft to create a new backup**. The plugin only holds X archives. Each new save drops the oldest. Daniel: every 10Web save while they were inside WordPress deleted the oldest healthy checklist backup he had just kept (Layer 2). After about **3 August**, scheduled plugin backups continued, now of the **damaged** site (Layer 3). When 10Web stopped, the healthy server copies the checklist had required were gone, replaced by damaged-site archives.

Treat Layers 2–3 as the 10Web-side mechanism. Disclose Layer 1.

### 4.2 Facts that support that testimony without over-claiming it

1. **Local copies still exist on the PC.** Windows listing 12 October 2026 shows dated Updraft sets:

   | Timestamp on disk | Visible sizes (KB) | Likely Updraft role (by size, names truncated) |
   | --- | --- | --- |
   | 24 Jul 2026 5:00-5:01 PM (`1659`) | 392,197; 392,691; **10,774 (boxed)**; 50,111 | two ~383 MB = uploads splits; 50 MB = likely `db`; 10.5 MB = likely `plugins` (not this 174 KB `others`) |
   | 23 Jul 2026 7:30 PM | 19,827 | **named:** Drive `-db.gz` `c9570a105596` (see F17) |
   | 12 Jul 2026 7:30 PM | 17,391 | **named:** Drive `-db.gz` `a2f57e449b46` (see F17) |
   | 30 Jun 2026 7:30-8:00 PM (`1930`) | several 330,566-406,397; 10,774; 47,132 | uploads splits; 10.5 MB likely `plugins`; ~46 MB likely `db` |

   Exhibit: `docs/legal/exhibits/exhibit-pc-updraft-folder-2026-10-12.png`.

   Those dates are **before** the owner-stated 25 July migrate start. The 24 July 16:59 set is the day-before-migrate window.

2. **This 30 June `others` zip is a real Updraft archive** with matching nonce `11b0badf493f` and matching `1930` time. It proves the local folder is not a random pile of CSS. It does **not** prove the 24 July uploads are healthy. It contains no pages.

3. **Server-side restore copies did not return the migrate-source.** Handoff table: files restore from 1 August, DB from 28 July, uploads 28 July and 24 July. All logged success. Site still broken. 24 July uploads restore: Computers **worse** than the 28 July revision review; July 2026 product files 404. That is the definition of "not representative of the site I allowed them to migrate."

4. **A needed Updraft DB file was missing on the server.** `backup_2026-07-28-1945_…-db.gz` File not found. Actor unknown. 10Web admits using Updraft during the WP-admin window. Capability + missing file is **not** identity. It is why G-59 matters.

5. **10Web had the tools.** WP admin + Updraft + 10WEB Manager is enough to create new archives, run restores, and write `wp-content`. Their letter confirms Updraft use.

6. **Drive copies of two pre-migrate databases are now fingerprinted.** PowerShell SHA256 on `C:\Users\dreid\My Drive\UpdraftPlus\*.gz` found only:

   - 12 Jul 19:30 `-db.gz` `a2f57e449b46` → `D2F31A9413BE076C04028C79C3BF2A0B875DEBD7545CA6DDE2E36296C777D581`
   - 23 Jul 19:30 `-db.gz` `c9570a105596` → `03FD3A90954285632778C47B0B033E66171C3263117114971EE4D85DAD04284A`

   Those hashes are how counsel later compares Drive vs Hostinger. Same hash = same bytes. Different hash = rewritten file. Missing server file = Drive copy is the remaining original for that night. The `.gz` files themselves have **not** been opened in this run, so page/SKU content inside them is not yet counted. 30 Jun and 24 Jul DB slices did not appear in `*.gz` (they are likely `.zip`).

### 4.3 Mechanism (retention replacement, not a mystery delete button)

Layer 1 (disclose): Daniel, on Cursor’s checklist, deleted older automated backups after verifying new pre-migrate copies.

Layer 2: 10Web admits creating new Updraft backups while they were the only vendor in WordPress. A full slot of X drops the oldest. That is how the healthy checklist copies leave the server.

Layer 3: From about 3 August, automated backups of the damaged site keep filling those X slots. The 10 October dump (oldest 15 September; no June/July/August; Drive July hashes absent) is Layer 3’s remainder.

Explanation A from the prior draft still holds in parallel: some Hostinger restores were already snapshots of a written tree. A and the three layers can all be true. This agent has **not** opened the 12 Jul or 23 Jul `-db.gz` files, so SQL health of those Drive copies is not yet counted. They remain the off-server fingerprints of nights before 25 July.

### 4.4 Do not say these sentences

- "This 174 KB zip proves 10Web wiped every backup."
- "The Drive SHA256 hashes prove 10Web deleted the server files" (they fingerprint local copies; comparison to the server has not been run).
- "Daniel never deleted any backup" (he deleted older-than-checklist automated copies for storage, after verifying new ones).
- "10Web had to click Delete on every file" (retention replacement from their admitted new Updraft saves plus later damaged-site dailies is enough).
- "10Web deleted Hostinger's own snapshot system" (not shown; Hostinger restore is a separate product from Updraft).
- "No copies exist anywhere" (false: they exist on the PC).
- "The 24 July 392 MB files are proven healthy migrate-source" (not opened).
- "Cursor counted 4000 unique SKUs destroyed" (owner testimony; this agent did not census 4000).
- "Every defect on staging today is a 10Web write" (Cursor 12 Aug / 19 Aug light rebuilds and the 24 July uploads restore must be listed separately).

---

## 5. Other actors that must be disclosed (or the file collapses)

| Actor | What they did | How to label it |
| --- | --- | --- |
| 10Web | Failed migrate; fake Builder sites; demanded WP admin; Manager plugin; `10web_tmp`; used Updraft; 30 Sep denial | The claim |
| Hostinger restore UI + Daniel restore choices | 24 Jul uploads restore crushed Computers; 28 Jul DB and 1 Aug files restores did not heal | Separate. Motive: try to undo 10Web. Result: more media loss. Not a 10Web click unless restore-history says so |
| This recovery project (Cursor) | 12 Aug hub-parent light rebuilds; 19 Aug Computers placeholders | Recovery-agent data loss. Disclose. Not 10Web |
| Cursor migrate checklist + Daniel | Delete older automated plugin backups to free disk after verifying new pre-migrate copies | Layer 1. Disclose. Not 10Web. The copies 10Web’s new saves then rotated out were the **verified** ones, not those older files. |
| Earlier live-site crash | Owner: Claude, months before 10Web | Separate incident. Do not merge |

If counsel bills (Hostinger restore + Cursor rebuild) as 10Web destruction, 10Web will use this repo against the claim. Keep the three layers.

---

## 6. What "definitive" means here

**Definitive on these points:**

- 10Web's migrator failed.
- 10Web required WP admin after that failure.
- 10Web (or its AI) created fake Builder sites Daniel forbade.
- After that period, staging was not the pre-migration build (8 Aug measurements).
- 10Web later denied fault in language that omits their own access demand.
- Restores from the copies then present on the **server** did not return the working site.
- Local Updraft archives dated 30 June, 12 July, 23 July, and 24 July 2026 still exist on Daniel's PC.
- Google Drive holds SHA256-fingerprinted Updraft **database** copies from 12 July and 23 July 2026.

**Not definitive (yet):**

- Identity of who deleted `backup_2026-07-28-1945_…-db.gz` on the server.
- That the SQL inside the 12 Jul / 23 Jul `-db.gz` files is the healthy migrate-source (not opened).
- Byte-level proof that the local 24 July uploads zips are the healthy migrate-source.
- Legal liability, damages dollars, or "culpability" as a verdict.

Closing those gaps is mechanical: upload the 23 July `-db.gz` for offline SQL inspection; hash the Drive `*.zip` files; export Hostinger restore history; screenshot `wp-content/updraft` on the server if anything remains; Print-PDF the July Cloud Agent thread.

---

## 7. Next zip (one file, do not restore)

Best next send, under the 20-file cap:

1. Drive file `backup_2026-07-23-1930_The_Truth_Collective_c9570a105596-db.gz` (last hashed DB before migrate). Offline SQL read only. **Do not restore.**  
2. Or paste the `*.zip` SHA256 list from the same Drive folder (24 Jul and 30 Jun live there if they were copied).  
3. Still useful: the boxed 24 Jul **10,774 KB** archive, or that set’s `-db`.

Skip the ~392 MB files until a database slice from that timestamp is identified.

Stay on this Cloud run for backup forensics. The destruction-conversation files (BDM testimony, Nazeli PDFs) live on PR #6 / `https://cursor.com/agents/bc-9792f378-7057-4b87-8755-73c8af5e2672`.
