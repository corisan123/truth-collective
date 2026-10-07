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

When a GAP file is saved, do not rewrite the proof outline’s theory. Add the row and, if it **changes** a finding number in `00-DEMONSTRATIVE-PROOF-OUTLINE.md` §2, append a dated note.
