# Corrections — scale, missing pages, and who was inside WordPress

**Prepared:** 12 October 2026  
**Why this file exists:** Daniel Reid rejected the prior counsel summaries on this branch for understating damages, using WordPress page-count as if it were letter-page count, treating Technology Hub as if it were the whole site, and writing as if 10Web’s role inside WordPress during the migrate was unproven. Those objections are accepted. This file replaces that language.

**Sources read this turn (all five PDFs plus the GitHub testimony branch):**

- `docs/legal/source-pdfs/Cursor-BDM-summary-of-10web-destruction-2026-10-07.pdf` (same BDM testimony as PR #6)
- `docs/legal/source-pdfs/Systems-copied-with-10web-found-2026-10-10.pdf`
- `docs/legal/source-pdfs/WP-error-debug-log-2026-10-10.pdf`
- `docs/legal/source-pdfs/Hostinger-error-log-2026-10-10.pdf`
- `docs/legal/source-pdfs/Hostinger-raw-backup-history-2026-10-10.pdf`
- GitHub branch `cursor/10web-lawsuit-testimony-2672` (compare against default)

**Not a legal opinion.** Language below is corrected to match the documents and Daniel’s measurement rule.

---

## 1. What was wrong in the earlier summaries on this branch

| Earlier language | Why it is wrong |
| --- | --- |
| “65 pages” as the size of the site | That is the WordPress **URL / post** count (hub + child + sub-child pages). It is not the volume of content. Counsel hearing “65 pages” will picture a brochure. |
| Damage discussed mainly as Technology Hub / Computers | The 8 August diagnosis and the BDM testimony cover **sitewide** information architecture: Technology, Office, Smart Lighting, catalogs, media, overlays, menus, production 404s. REST work on page 111 does not bound the destruction. |
| “Unproven” / “this agent has not seen the files” after Daniel had already generated the BDM testimony and Hostinger dumps | Those files were on PR #6 and on his CPU. This Sep 19 recovery run had not ingested them until this turn. That is a gap in **this chat**, not an absence of documents. |
| Listing Cursor August rebuilds in a way that can be read as a competing cause of the July/August destruction | Cursor REST writes on this recovery project began **after** the 8 August diagnosis. They are later recovery loss. They are not a second vendor inside WordPress during 25 July–7 August. |
| “65 pages and X were damaged” | False as a damages sentence. Most of the 65 WordPress pages were content-heavy. Many that still exist are gutted. Some child / sub-child pages are gone from WP so REST cannot rebuild them from live posts. |

Do not reuse the discarded sentences.

---

## 2. Universal size language (US Letter)

Daniel’s rule, now the rule for this packet:

A WordPress “page” is a URL. It is not a printed page. The comparable unit is **US Letter (8.5 by 11 inches; Daniel said 8 x 11)**.

| Unit | Figure | Source |
| --- | --- | --- |
| WordPress content pages pre-migration (hub / child / sub-child) | **65+** | BDM testimony §1.1; July handoff |
| Letter-size pages of content **per** WordPress page | **55 to 100+** | Owner measurement of saved pre-migration pages on his CPU |
| Letter-size equivalent for the whole site | **3,575 minimum to 6,500+** (65 × 55 to 65 × 100, plus the “65+” and “100+” tails) | Owner conversion, 12 Oct 2026 |
| Staging disk | ~6.73 GB | BDM testimony §1.1 |
| Staging database | ~235 MB (`u867403816_jdn2C`) | BDM testimony §1.1 |

Counsel language to use:

> Pre-migration staging was 65-plus WordPress URLs. Each of those URLs held between about 55 and more than 100 US Letter pages of products, descriptions, and editorial copy. The working site was on the order of 3,575 to 6,500-plus letter-size pages, not a 65-page brochure.

The 55–100 band is Daniel’s count from pre-migration pages saved on his CPU. This agent has not independently printed all 65 URLs. To pin one number inside that band, send a Print-to-PDF of **one** heavy catalog URL (Computers is the worst child) from the 23 July `-db.gz` or from a pre-migration HTML save. Until that sample lands, use the range, not a single midpoint.

---

## 3. Damage is sitewide. Missing child and sub-child pages are part of it.

REST can only rewrite WordPress posts that still exist. It cannot resurrect a child or sub-child that is no longer a post.

### 3.1 What the 8 August / BDM record already said (not Tech Hub only)

BDM testimony §6.2 (PDF pages 9–11), and `STAGING-RECOVERY-HANDOFF.md`:

- Information architecture / links destroyed on **Technology and Office** trees
- Menu items present while destinations failed
- Hub tiles pointing at wrong short slugs while some nested pages still existed
- Media library / product images wrong, cropped, or 404 (Computers July uploads)
- Custom overlay / explore / hero systems dead or wrong **sitewide** (flicker on every page)
- Layout scramble on money pages (Computers; EXPLORE split on Office / Analog Writing)
- Smart Lighting: mixed crop, white-on-white copy
- Fake 10Web Builder sites; `10web_tmp` under uploads
- Production `/technology-hub/` still 404 as of 7 Oct 2026

### 3.2 Child / sub-child pages this recovery agent still cannot recover from live REST

Documented on this branch, still true:

- **Emerging Technologies** — no dedicated WordPress page. Tech Hub tile left unlinked.
- **AI Wearables** — no dedicated WordPress page. Tech Hub tile left unlinked.
- 8 August Tech Hub inventory: **16 tiles** on the parent versus **8** published children still in WP.
- 23 September REST census: **59 published** WordPress pages and **10 drafts**, against **65+** content-heavy URLs pre-migration.
- Computers (page 359): products lived **in the page**, not as WooCommerce posts. Live overlay classes were **0**. Catalog photos 404. The 19 August light rebuild replaced photos with SVG placeholders. That is not a restored catalog.
- Pages that still return 200 can still be **empty shells** (heading-only, stripped classes, stale hrefs). A 200 is not an undamaged page.

“Unrecoverable by the Cursor agent inside REST” means: if the child/sub-child is not in `wp_posts` (or its content is gone from revisions), REST has nothing to apply. Rebuild-from-memory is not recovery of the pre-migration page.

### 3.3 Specific document still needed to name every missing URL

A pre-migration **sitemap or Pages list of all 65-plus titles and parents**. This agent can then mark each URL as: exists-intact / exists-gutted / missing. Ask for that list (or a Rank Math sitemap from before 25 July). Until it arrives, do not pretend the missing-page count is a finished census. Do not shrink the damages to Technology Hub while waiting.

---

## 4. Who was inside WordPress during the migrate

**Vendor:** The only third-party admitted inside WordPress during 25 July–7 August 2026 is **10Web**.

| Actor | During 25 Jul–7 Aug migrate window | After 8 Aug diagnosis |
| --- | --- | --- |
| 10Web | Demanded WP admin `support@10web.io` (27–28 Jul emails). 30 Sep letter admits WP admin, Migration Assistant, and Updraft use. 10WEB Manager plugin on the site. Manager REST API logged 25 Jul and 3 Aug (error log). | Manager still **Active v1.20.21** on 8 Aug and still Active on **10 Oct 2026** (Site Health PDF). |
| Daniel Reid | Site owner. Created the admin they demanded. Deleted fake AI pages. Emailed daily after they went silent. | Hostinger restores; later recovery with Cursor. |
| Cursor / BDM | Git checklists and drop-in HTML. BDM testimony: “I do not log into WordPress or Hostinger myself. Daniel executes clicks.” | This recovery run used REST **after** 8 Aug. Those writes are recovery, not the migrate. |
| Any other AI or person | **No document in this packet names another WP admin during the migrate.** | Claude/Task were drafters. Not WP admins in the logs. |

Correct framing: there is no competing vendor story for the migrate window. 10Web asked to enter WordPress, entered, left Manager on the site, and later denied destroying it. Daniel was the owner. Cursor was not a second login.

Later Hostinger restores and Cursor light rebuilds **must still be listed** as additional change after the crash. They are not a substitute 10Web defense.

---

## 5. Neutral summary of each PDF just ingested

### P-01 — Cursor / BDM summary of 10Web destruction (20 pages)

The 7 October BDM technical testimony (PR #6). Pre-migration scale (~6.73 GB, ~235 MB DB, **65+ hub/child/sub-child pages**). Locked `tc-*` systems. Prep rules. Failed migrate, fake Builder sites, Nazeli access demand versus 30 Sep denial. Damages list is **sitewide** (IA, media, overlays, money pages, backups, support silence). BDM does not log into WP. This is the Cursor-during-and-after-migrate declaration Daniel pointed at.

### P-02 — “Systems copied with 10web found” (6 pages)

WordPress Site Health / debug info, timestamp **10 October 2026 13:07 UTC**, path `public_html/tcstaging`. It lists **10WEB manager v1.20.21** among 19 active plugins, Astra 4.13.2, Kadence Blocks 3.7.2, Rank Math Pro, UpdraftPlus 1.26.4, LiteSpeed, one user. It proves 10Web’s Manager plugin was **still Active on staging 11 weeks after migrate start**. It is not a dump of 10Web copying Additional CSS. Do not caption it as a theft log. Caption it as continued 10Web plugin presence.

### P-03 — WP error debug log (11 pages) and P-04 — Hostinger error log (11 pages)

Same `error_log` family for `tcstaging` (153.5K), exported 10 October 2026. They are not two independent novels.

What they **do** show, dated:

- **25 July 2026 20:00:05 UTC** — `10web-manager/includes/class-rest-api.php` line 444, undefined `sftp_credentials`. That is 10Web Manager’s REST class firing on staging **on the owner-stated migrate-start day**.
- **3 August 2026 15:57:07 UTC** — the same 10Web Manager REST warning again.
- **7 August 2026 14:15 UTC** — fatals and missing files: Rank Math Pro `rank-math-pro.php` not found; Kadence `Shutdown_Collection.php` not found; ActionScheduler class missing. PHP `include_path` still contains **four 10web-manager vendor/pear paths**. That is the same calendar day as the formal incident letter in ticket `#375660`.
- **8 Aug, 19 Aug, 1 Oct, 10 Oct** — Rank Math schema query against the wrong table (`wp_usermeta` / `meta_id`).

What they **do not** say in so many words: the string “10Web destroyed the website.” Do not invent that quote. Do say: 10Web Manager executed on staging on 25 July and 3 August, and on 7 August core plugins 10Web had been working around were missing files while 10Web Manager remained on the include path.

Pre-25 July rows are mostly `nav-menus.php` property-on-false warnings (3–21 July). Those are menu-editor warnings, not a 10Web confession.

### P-05 — Hostinger raw backup history (35 pages)

Updraft “known backups” dump dated 10 October 2026. **16** timestamps. **Oldest: 15 September 2026.** No June, July, or August 2026 filenames. The SHA256 values in that dump **do not match** the Drive hashes for 12 July or 23 July `-db.gz`.

How to use this without lying:

- It proves the **server’s current Updraft history does not contain** the pre-25 July databases Daniel still has on Drive.
- Updraft retention can rotate old backups out. A 10 October dump that starts at 15 September can be ordinary rotation for recent dailies. It is **not**, by itself, a signed 10Web delete log.
- Pair it with the **August** fact that `backup_2026-07-28-1945_…-db.gz` was **missing from disk when a restore was needed**. That gap is contemporaneous with the crash, not with October rotation.
- Pair it with Drive copies dated 12 July and 23 July that still hash. Those nights exist off-server. They do not exist in this server history.

---

## 6. What to ask for next (specific, not vague “unproven”)

1. Print-to-PDF of **Computers** (or one other heavy catalog URL) from a pre-migration save, so letter-page count for that URL can be counted on paper.  
2. Pre-migration **list of all 65-plus WordPress titles and parents** (Rank Math sitemap or Pages export).  
3. The remaining 10Web threads (sample is 1 of 53).  
4. Hostinger **Website Backup / restore-history** UI for 24 Jul / 28 Jul / 1 Aug (this dump is Updraft known-backups, not Hostinger’s own snapshot log).  
5. Upload of `backup_2026-07-23-1930_…-db.gz` for offline SQL read (not a restore).

---

## 7. Counsel sentences that replace the discarded ones

Use:

> The site was not 65 brochure pages. It was 65-plus WordPress URLs whose printed content runs about 55 to 100-plus US Letter pages each, on the order of 3,575 to 6,500-plus letter pages, plus ~6.73 GB of files and a ~235 MB database.

> Destruction was sitewide: hub parents, sub-parents, children, and sub-children; catalogs; media; custom overlay/explore systems; menus and permalinks. Some child and sub-child pages are still missing from WordPress. REST rebuild cannot create those URLs from posts that are gone. Pages that still exist are often gutted shells.

> The only vendor documented inside WordPress during the migrate is 10Web: they demanded admin access, their Manager plugin ran on 25 July and 3 August, they admit Updraft and Migration Assistant, and Manager was still Active on 10 October 2026. No other AI or person is named as a WP admin in that window. Cursor’s later REST recovery is a separate, later layer.

Do not use:

> 65 pages were damaged.  
> Only Technology Hub was destroyed.  
> There is no proof 10Web was in WordPress.  
> Cursor might have been the migrate actor.
