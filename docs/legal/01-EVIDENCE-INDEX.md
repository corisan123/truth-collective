# Evidence index — neutral summaries

**Prepared:** 7 October 2026  
**Rule:** one row = one artifact. Summary is what the file **contains**, not a closing argument.  
**Locations:** this branch `cursor/wp-rest-repair-98f8`; PR #5 `cursor/10web-migration-a537`; PR #6 `cursor/10web-lawsuit-testimony-2672`.  
**Missing files** (PC / Drive only) are listed in **Group G** as empty slots.

IDs: **T-** 10Web vendor · **C-** Cursor/repo · **S-** staging technical 8 Aug · **R-** later recovery (not 10Web) · **O-** owner PDFs not in git.

---

## Group T — 10Web vendor (in git)

| ID | File | Date | Neutral summary |
| --- | --- | --- | --- |
| T-01 | PR #6 `docs/legal/exhibits/exhibit-10web-demands-admin-access-p17.png` | 28 Jul 2026 (email 15:53 GMT+4); also shows 27 Jul apology | Nazeli Sargsyan, 10Web Care. To proceed with migration: (1) create temporary WP admin using `support@10web.io` and send login URL/credentials; (2) remove existing test website or buy a slot; (3) grant temporary 10Web Dashboard access. States they will then proceed **from our end**. Header on the PDF: “sample of one email thread out of 53.” |
| T-02 | PR #6 `docs/legal/exhibits/exhibit-10web-demands-admin-access-p18.png` | 27 Jul 2026 Nazeli; 26 Jul 2026 Daniel | Nazeli: account has hosted site `active-bluegill.10web.cloud`; one hosting slot; create temporary WP admin; **we will access the existing WordPress dashboard and attempt the migration from our end.** Daniel (26 Jul): migrate failed yesterday; **AI bot made 2 fake websites pages**, deleted them; UI said if reconnect fails contact support; **15+ hours**. |
| T-03 | PR #6 `docs/legal/exhibits/exhibit-10web-sept30-denial.png` | 30 Sep 2026 16:09 GMT+4 | Nazeli “investigation results.” Subject site written as `#tcstaging.truth-collective.com`. Asserts records do not support that 10Web destroyed the site or deleted backups. States after automated migration failed, **Daniel provided WP admin and expressly authorized Migration Assistant**. States 10Web used Updraft only to create a **new backup** for migrate, did not restore over source, did not change DNS. States later admin access **revoked** so they could not continue. Admits migration **not successfully completed**. Refuses damages and 3-month refund; mentions 1-month subscription extension as not an admission. |
| T-04 | PR #5 `docs/10WEB-SUPPORT-TRANSCRIPT-TIMELINE.md` | Index 5 Oct 2026 from owner-pasted 10Web AI/Marta/Nazeli log | Chronological index of 10Web chatbot + live chat 24 Jul–4 Aug. Sales promises (preserve code/URLs/affiliates). Marta 1-site limit / Manager plugin. Disconnect. 3 Aug owner: not AI Builder, human migrate `tcstaging`, do not publish. 4 Aug merge `#375660`. **Not** the full 53-thread corpus. |
| T-05 | PR #6 `docs/legal/BDM-10WEB-MIGRATION-TESTIMONY.md` | 7 Oct 2026 | First-person technical narrative by Cursor assistant “BDM.” Pre-migration scale (~6.73 GB / ~235 MB DB / 65+ pages). Custom `tc-*` systems. Safety rules conveyed. Failed migrate, fake sites, Nazeli access demand vs 30 Sep denial, “disconnected” as product failure, before/after damage list, point-by-point denial table. AI assistant declaration; Daniel executes clicks. |
| T-06 | PR #6 `docs/legal/exhibits/exhibit-site-complexity-diagram.jpg` | Owner exhibit, filed 7 Oct | Diagram of staging complexity (hubs/children/custom layer). Visual aid, not a measurement log. |

---

## Group C — Cursor / git contemporaneous (pre and during)

| ID | File | Date | Neutral summary |
| --- | --- | --- | --- |
| C-01 | GitHub PR #2 `cursor/lock-in-master-brief-and-components-b1dd` | 14–18 Jul 2026 | Cloud Agent `bc-b360733d`. Master Brief, hub structure, LiteSpeed/cache, overlay/explore class rules. **Prep**, eleven days before owner-stated 10Web start. |
| C-02 | Branch `cursor/image-fix-and-membership-toggle-2672` commits | 25–26 Jul 2026 | Cloud Agent git (`Cursor Agent` author). Operating rules 25 Jul; Computers drop-in HTML and “Rebuild Computers page as a clean Amazon hub” 26 Jul. **No PR**, so **no bcId** in GitHub. Same calendar days as migrate start. |
| C-03 | `docs/brand-references/TC_Cursor_Migration_Brief.docx` | In repo | Staging→live preserve-only migration brief (Hostinger), not 10Web’s product manual. |
| C-04 | `diagnostics/cursor-10web-conversation-hunt-2026-10-07.md` | 7 Oct 2026 | This Cloud run cannot load the July transcript. Owner later found the thread; cloud icon = Cloud Agent; Export Transcript will not work. |
| C-05 | `diagnostics/HOW-TO-SAVE-FOUND-CURSOR-CHAT-2026-10-07.md` | 7 Oct 2026 | Path B: Print-PDF, copy `bc-` URL, do not Continue/archive. |
| C-06 | PR #5 `docs/CURSOR-CHAT-PRESERVATION-10WEB-CRASH.md` | 5 Oct 2026 | Earlier hunt: Cloud list then showed oldest 19 Aug; Desktop forensic copy instructions. Later PR #5 body: late July work was Cloud Agent `bc-b360733d`. |
| C-07 | PR #5 `docs/CURSOR-10WEB-RELAY-EVIDENCE-SEARCH.md` | 5 Oct 2026 | Search terms for Cursor-drafted paste-to-10Web prompts (Charlie, Marta, AI Builder, preserve). |

---

## Group S — Staging condition on 8 August 2026 (technical)

| ID | File | Date | Neutral summary |
| --- | --- | --- | --- |
| S-01 | `STAGING-RECOVERY-HANDOFF.md` | From 8 Aug 2026 | Restore table (files 1 Aug, DB 28 Jul, uploads 28 Jul and **24 Jul**). Hard rules: no live restore, no restore roulette. 10WEB Manager Active v1.20.21. Ticket `#375660`. `10web_tmp` gone after Jul 24 uploads restore. Flicker, EXPLORE split, stale hub hrefs. CSS vs markup diagnosis. |
| S-02 | `diagnostics/css-inventory-2026-08-08.md` | 8 Aug 2026 | ~57KB Additional CSS still present. **No** 10web/tenweb/twbb markers in sampled public HTML. Locked 02A still “known good” after crash. Overlay+explore combo noted as crop layer. |
| S-03 | `diagnostics/computers-page-2026-08-08.md` | 8 Aug 2026 | Computers live: 0 product overlay class; 4 explore-hub; grade HTML as text; July image 404. Owner: Rank Math ~90 finished just before crash. Jul 24 restore **crushed** page worse than 28 Jul review. Revision hunt. |
| S-04 | `diagnostics/media-library-broken-thumbs-2026-08-09.md` | 9 Aug 2026 | Newest `uploads/2026/07/` often HTTP 404; June samples often 200. Imagify invalid key separate. Do not Jul 24 full restore. |
| S-05 | `diagnostics/hub-technology-10web-freeze-2026-08-08.md` | 8–9 Aug 2026 | `kind-louse.10web.cloud` freeze: do not port 10Web/Tailwind/fake category trees. Real Tech Hub children = 8. Owner 7 Oct: kind-louse was fake Builder site. |
| S-06 | `diagnostics/homepage-audit-2026-08-08.md` | 8 Aug 2026 | Homepage not empty; same CSS payload. |
| S-07 | `diagnostics/homepage-links-S0b-2026-08-08.md` | 8 Aug 2026 | 404 vs 200 link table; pages exist, hrefs stale. |
| S-08 | `diagnostics/THROUGHPUT-RESET-2026-08-10.md` | 10 Aug 2026 | Owner: 10Web not responding; taken off critical path. |
| S-09 | `diagnostics/10web-migration-damage-evidence-2026-10-07.md` | 7 Oct 2026 | This agent’s dated technical memo: Additional CSS SHA identical 8 Aug–23 Sep; split 10Web-period vs Hostinger restore vs Cursor rebuilds; production Tech Hub 404 on 7 Oct. |

---

## Group R — Later recovery (disclose; not 10Web writes)

| ID | File | Date | Neutral summary |
| --- | --- | --- | --- |
| R-01 | Hub-parent light rebuilds | 12 Aug 2026 | Cursor REST replaced several hub **parent** layouts. Recovery, not a 10Web act. |
| R-02 | Computers light rebuild | 19 Aug 2026 | 21 cards; photos swapped to SVG placeholders; explore class stripped. Tagged on page. Further catalog loss. |
| R-03 | This Cloud run Tech Hub S1 | 23 Sep 2026 | Hover/class/copy pass on page 111 only. Staging. |

---

## Group O — Owner / BDM narrative filed this week

| ID | File | Date | Neutral summary |
| --- | --- | --- | --- |
| O-01 | `diagnostics/10web-kind-louse-wp-access-testimony-2026-10-07.md` | 7 Oct 2026 | Owner: several failed/disconnected migrates; humans required inside WP; damage = mash of provided fragments + kind-louse fake site. July Cursor was Cloud Agent. |
| O-02 | `diagnostics/WHAT-SEPT30-VS-JULY-EMAILS-PROVE-2026-10-07.md` | 7 Oct 2026 | Technical read of T-01–T-03: access demand vs later denial. Lists what those images do and do not prove. |
| O-03 | PR #5 `docs/legal/TC-10WEB-MIGRATION-INCIDENT-BRIEF-2026-10-05.md` | 5 Oct 2026 | Draft factual brief from Daniel’s submissions that day. Includes medical/housing context in later commits on that branch — **privilege/sensitivity: counsel review before wide share**. |
| O-04 | PR #5 `docs/exhibits/CLAUDE-2026-08-09-10WEB-DAMAGE-AND-SPECS.md` | 9 Aug 2026 statements, filed 5 Oct | Claude’s 9 Aug record of owner: destroyed inside WP; cannot roll back; pre-10Web backups damaged. Separate AI, not 10Web. |
| O-05 | Owner 12 Oct 2026 (this Cloud run) | 12 Oct 2026 | Testimony: 10Web accessed Updraft; healthy pre-25 Jul backups were not what later remained on the server; Hostinger restores therefore replayed damaged copies. Local PC still holds dated Updraft zips. |

---

## Group B — Local Updraft / backup-folder files (12 Oct 2026)

Do **not** restore these into staging or live.

| ID | File | Date | Neutral summary |
| --- | --- | --- | --- |
| B-01 | First 20 files from alleged 24 Jul backup folder (Code Snippets `menu.scss`, `manage.css`, webpack `editor.js`, etc.) | Uploaded 12 Oct 2026; plugin bytes dated in-plugin | Code Snippets plugin **admin** assets. Zero `tc-*` / `amzn.to`. Not Additional CSS. Review: `diagnostics/backup-folder-first-batch-2026-10-12.md`. |
| B-02 | `backup_2026-06-30-1930_The_Truth_Collective_11b0badf493f-others.zip` | Archive time 30 Jun 2026 23:46 UTC | Complete Updraft **others** slice, 174 KB / 30 entries. LiteSpeed, Jetpack WAF, Montserrat, `object-cache.php`, Hostinger Tools `mcp.log`. No DB, uploads, themes, plugins, or pages. Listing: `diagnostics/backup-listings/backup_2026-06-30-1930-others-listing.txt`. |
| B-03 | `docs/legal/exhibits/exhibit-pc-updraft-folder-2026-10-12.png` | Screenshot 12 Oct 2026 of files dated 30 Jun-24 Jul 2026 | Windows Explorer: Updraft-named zips including 24 Jul 16:59 two ~392 MB files, boxed 10,774 KB, 50,111 KB; 23 Jul 19,827 KB; 12 Jul 17,391 KB; 30 Jun several ~330-406 MB plus 10,774 KB and 47,132 KB. Names truncated in the shot. |
| B-04 | `docs/legal/02-COUNSEL-ARGUMENT-BACKUPS-AND-REBUTTALS-2026-10-12.md` | 12 Oct 2026 | Ranked damaging evidence, 30 Sep rebuttals, backup-wipe theory with truth limits. Not a verdict. |
| B-05 | Drive `backup_2026-07-12-1930_The_Truth_Collective_a2f57e449b46-db.gz` | Filename date 12 Jul 2026 19:30 | Updraft **database** `.gz`. SHA256 `D2F31A9413BE076C04028C79C3BF2A0B875DEBD7545CA6DDE2E36296C777D581`. Path `C:\Users\dreid\My Drive\UpdraftPlus\`. File not opened in this run. |
| B-06 | Drive `backup_2026-07-23-1930_The_Truth_Collective_c9570a105596-db.gz` | Filename date 23 Jul 2026 19:30 | Updraft **database** `.gz`, last hashed DB before 25 Jul migrate. SHA256 `03FD3A90954285632778C47B0B033E66171C3263117114971EE4D85DAD04284A`. File not opened in this run. Transcript: `docs/legal/exhibits/exhibit-updraft-db-gz-powershell-hashes-2026-10-12.txt`. |
| B-07 | `docs/legal/exhibits/exhibit-pc-updraft-jul23-highlighted-2026-10-12.png` | Screenshot 12 Oct 2026, Explorer page 1 of 13 | Five rows: highlighted 23 Jul 19:30 **19,827 KB** (db); four 24 Jul 16:59 files 50,111 / 10,774 / 392,691 / 392,197 KB. Decode: `diagnostics/HOW-TO-OPEN-JULY-23-AND-24-BACKUPS-ON-PC.md` §6. |
| B-08 | CPU folder `10web-manager` dated 25 Jul 2026 (plugin root + CSS; not a site backup) | Owner found 12 Oct 2026; folder date 25 Jul 2026 | **10WEB manager v1.20.21**. `config.json` has `TENWEB_MIGRATION_DEBUG=1` and `TENWEB_MIGRATION_UPLOAD_ARCHIVE_S3=1`. Same version later Active on staging. Review: `diagnostics/10web-manager-folder-2026-07-25-review.md`. |
| B-09 | First 20 files from alleged 24 Jul save opened in Notepad++ (`nppPluginList.dll`, `Monokai.xml`, `Hello Kitty.xml`, …) | Uploaded 12 Oct 2026 | **Notepad++ plugins and styler themes.** Zero WP/TC/10Web content. Review: `diagnostics/notepadpp-themes-batch-2026-10-12.md`. |
| B-10 | `pasted confirmed clean css code_files` (`frame.html`, `root-j88guhss.css`, `sdk.js.download`, conversation/code-block CSS) | Owner: saved 24 Jul 2026 | **ChatGPT.com Webpage-Complete chrome.** Not Additional CSS. Sibling `.html` (no `_files`) might hold the pasted CSS in the chat transcript. Review: `diagnostics/chatgpt-save-files-batch-2026-10-12.md`. |
| B-11 | Drive PowerShell listing of `C:\Users\dreid\My Drive\UpdraftPlus\` | 12 Oct 2026 | Named suffixes. 24 Jul `93bbf2b8c244` = plugins/themes/uploads, **no db**. 23 Jul `c9570a105596-db.gz` only. 30 Jun files **no db**. USB D/F/G/H/I/J: no extra hits in that run. `diagnostics/DRIVE-UPDRAFT-POWERSHELL-INVENTORY-2026-10-12.md`. |
| P-01 | `docs/legal/source-pdfs/Cursor-BDM-summary-of-10web-destruction-2026-10-07.pdf` | 7 Oct 2026 | Same BDM testimony as PR #6 T-05. 65-plus hub/child/sub-child URLs; sitewide damages; 10Web demanded WP admin. |
| P-02 | `docs/legal/source-pdfs/Systems-copied-with-10web-found-2026-10-10.pdf` | 10 Oct 2026 13:07 UTC | WordPress Site Health for `tcstaging`. **10WEB manager v1.20.21 Active.** 19 plugins. Not a CSS-copy dump. |
| P-03 | `docs/legal/source-pdfs/WP-error-debug-log-2026-10-10.pdf` | Export 10 Oct 2026 | `tcstaging` error_log. 10Web Manager REST 25 Jul and 3 Aug; 7 Aug missing Rank Math Pro / Kadence files. |
| P-04 | `docs/legal/source-pdfs/Hostinger-error-log-2026-10-10.pdf` | Export 10 Oct 2026 | Same log family as P-03 (11 pages). |
| P-05 | `docs/legal/source-pdfs/Hostinger-raw-backup-history-2026-10-10.pdf` | Dump 10 Oct 2026 | Updraft known backups: 16 timestamps, oldest 15 Sep 2026. No June/July/August. Drive Jul hashes absent. |
| P-06 | `docs/legal/03-CORRECTIONS-SCALE-MISSING-PAGES-ACTOR-2026-10-12.md` | 12 Oct 2026 | First correction pass. Superseded on damages wording by P-07. |
| P-07 | `docs/legal/04-CSS-CLASS-BINDING-VS-STYLESHEET-2026-10-12.md` | 12 Oct 2026 | Splits stylesheet text vs class names vs class-to-Kadence/Gutenberg binding. “Classes intact” withdrawn. Book census owner figures. Kadence fatal + 10Web Manager same 7 Aug log. |
| P-08 | `docs/legal/05-BACKUP-RETENTION-REPLACEMENT-2026-10-12.md` | 12 Oct 2026 | Three layers: checklist deletion of older plugin backups; 10Web’s admitted new Updraft saves dropping oldest slots; post-3 Aug damaged-site automation. Off-server July copies remain. |
| P-09 | `docs/legal/06-SCALE-LABOR-ENGINE-AND-EDITORIAL-2026-10-12.md` | 12 Oct 2026 | Corrects 4,000 vs affiliate-link confusion. Editorial/Ones Who. Stage I–VI engine snapshot. 110-day engine as a damages category. |
| P-10 | `docs/legal/07-DAMAGES-SITEWIDE-LETTER-SCALE-2026-10-12.md` | 12 Oct 2026 | Controlling damages: US Letter 3,575 to 6,500-plus; every hub; REST-unrecoverable children; 10Web exclusive migrate-window actor; five named PDFs. |
| P-11 | `diagnostics/wp-page-tree-2026-10-12.md` | 12 Oct 2026 | Live REST tree: 59 published, 10 drafts. Named missing: Emerging Technologies, AI Wearables. Drafts include Truth Untold 3–5 and 7–10. |
| P-12 | `docs/legal/08-EVALUATION-ENGINE-REPO-SCAN-2026-10-12.md` | 12 Oct 2026 | Authorship: Copilot/Task = governance content; Cursor Desktop = complex JS/HTML engine. Copilot.fun folder is Task-era save + host JS. Desktop TC engine files not in this checkout. ISI JS tree is a separate company unless owner says otherwise. |
| E-07 | `evaluation-engine/TC_Evaluation_Engine_v1.xlsx` | 3 Aug 2026 on July Cloud branch; copied here 12 Oct | Eight-tab scoring workbook: Intake → Engineering or Editorial → Results TC Grade. Not JavaScript. |
| E-01 | `source-pdfs/II-Master-Engineering-Driven-Evaluation-System-update-2026-08-02.pdf` | July 2026 / updated 2 Aug 2026 | Master engineering evaluation whitepaper Draft 2.1.1. ISO/UL/IEEE/JEDEC. Tiers 1–4. Per-category addenda. |
| E-02 | `source-pdfs/Stage-I-Evaluation-Benchmarking-and-Governing-Bodies.docx` | Ingested 12 Oct 2026 | Stage I: map products to governing bodies before scoring. |
| E-03 | `source-pdfs/Stage-III-Qualitative-Eval-Process.pdf` | v2.1, Aug 2026 | 21-point qualitative track for books and **non-monetized** editorial (Ones Who, wellness, podcasts). Research 5–6 per 1 selected in this doc; owner later said 10-plus for products. |
| E-04 | `source-pdfs/Stage-V-Technology-Hub-Evaluation-System.pdf` | v2.1 | Technology Hub engineering process. Mission-critical weight 50–60%. |
| E-05 | `source-pdfs/Stage-VI-Workspace-Evaluation-Standards.docx` | Ingested 12 Oct 2026 | Workspace hub: BIFMA/ANSI desks, chairs, monitor arms. |
| E-06 | `source-pdfs/Standards-Governance-Compliance-Division-2026-10-12.docx` | Ingested 12 Oct 2026 | Top-level hub governance. Three layers. Evidence over opinion. Same bar for non-monetized content. |

---

## Group G — Not in git (fill these rows)

Put files in `Documents\TC-10WEB-LAWSUIT\01-source-pdfs\` then add ID, date, 4-line summary here.

| ID | Placeholder | Status |
| --- | --- | --- |
| G-01 | 10Web sample email thread 1 of 53 (full PDF, not only p17/p18 screenshots) | **GAP** |
| G-02 … G-53 | Remaining 10Web threads as PDF | **GAP** |
| G-54 | 30 Sep “investigation results” original PDF | **GAP** (screenshot is T-03) |
| G-55 | “Truth Collective 10Web migration destruction” PDF | **GAP** |
| G-56 | “Handoff rules 10Web destruction” PDF | **GAP** |
| G-57 | Grok / evidence findings summary PDF | **GAP** |
| G-58 | Hostinger restore-history export Jul 24 / 28 / Aug 1 | **GAP** |
| G-59 | Updraft missing `db.gz` File Manager screenshot | **GAP** |
| G-60 | Recovered Cloud Agent Print-PDF + `bc-` URL | **GAP** |
| G-61 | WP Users list showing `support@10web.io` if it existed | **GAP** |
| G-62 | 10Web contract / invoices / plan screenshots | **GAP** |
| G-63 | Pre-migration Computers / Tech Hub screenshots or Rank Math | **GAP** |
| G-64 | GSC live index / production 404 captures | **GAP** |
| G-65 | 24 Jul 16:59 boxed 10,774 KB zip (or `-db` / `-plugins` / `-themes` from that timestamp) | **GAP** — screenshot exists (B-03); file not yet uploaded |
| G-66 | 30 Jun 19:30 matching `-db` to pair with B-02 | **GAP** |
| G-67 | Hostinger `wp-content/updraft/` listing to compare SHA256 of B-05 / B-06 | **GAP** |
| G-68 | Print-to-PDF of one heavy pre-migration catalog URL (Computers) to count US Letter pages | **GAP** — asked 12 Oct |
| G-69 | Pre-migration list of all 65-plus WordPress titles and parents (sitemap or Pages export) | **GAP** — asked 12 Oct |
| G-70 | Permalinks of the three pages that still have full working CSS class binding | **GAP** — asked 12 Oct |
| G-71 | Pre-migration book-category list (20-plus URLs) to support ~1000 → ~200 remaining | **GAP** |
| G-72 | Updraft “retain this many backups” setting (the number X) | **GAP** — asked 12 Oct |
| G-73 | July Cursor Print-PDF page instructing deletion of older plugin backups for migrate storage | **GAP** |

When a GAP file is saved, do not rewrite the proof outline’s theory. Add the row and, if it **changes** a finding number in `00-DEMONSTRATIVE-PROOF-OUTLINE.md` §2, append a dated note.
