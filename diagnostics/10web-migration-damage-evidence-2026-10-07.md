# Technical evidence memo — 10Web migration period damage

**Prepared:** 7 October 2026  
**Preparer:** Cursor Cloud recovery agent working on staging `https://tcstaging.truth-collective.com` (repo `truth-collective`, branch `cursor/wp-rest-repair-98f8`).  
**Owner-stated migration start:** 25 July 2026.  
**10Web ticket recorded in recovery notes:** `#375660` (logged as RCA / compensation, not as a completed repair).  
**Plugin recorded 8 August 2026:** **10WEB manager still Active, v1.20.21.**

This memo is a technical compilation of contemporaneous recovery notes, public HTTP probes, WordPress REST reads, and git-tracked diagnostics. It is **not** a legal opinion, not an expert-witness declaration, and not an attribution of legal causation. Counsel should treat quoted owner statements as owner testimony and treat Cursor-measured counts as engineering observations.

---

## 1. What this memo can and cannot prove

**Can prove from this workspace and public HTTP**

- Staging and production URLs, HTTP status codes, and selected HTML/CSS fingerprints on the dates those probes were run.
- WordPress page IDs, revision IDs, class counts, `amzn.to` counts, and media 404s recorded in dated diagnostic files.
- That Additional CSS (Appearance → Customize) survived byte-identical from 8 August through 23 September 2026.
- That a 10Web working folder `10web_tmp` existed under uploads (HTTP 403 on `.htaccess`) and was later gone from File Manager after a 24 July uploads restore.
- That a 10Web host `kind-louse.10web.cloud` existed; 8–9 Aug recovery froze it as “do not port.” Owner testimony on 7 Oct 2026: that host was **10Web’s fake Builder website** from the failed migrations, not a Truth Collective design mock.
- That recovery work after the crash (Hostinger restores; Cursor “light rebuilds”) caused **additional** measurable data loss. Those later acts are **not** 10Web acts and must be listed separately.

**Cannot prove from this workspace alone**

- The exact clock time 10Web first wrote to production on 25 July 2026 (that date is the owner’s statement; repo notes say “10Web crash” / “just before the 10Web crash”).
- A verified unique SKU count of “4000+ products.” That figure is owner testimony. REST inventory in September 2026 counted affiliate codes and revisions in the **hundreds** on published/draft pages plus **2324** media items; it did not complete a SKU census.
- Lost revenue, SEO ranking dollars, or medical damages.
- That every visual defect after July is caused only by 10Web (CSS vs markup vs restore vs later rebuilds are mixed).
- From this VM: the inside-WordPress “pull through” session itself (no 10Web staff chat attached here). Owner testimony of that step is recorded in `diagnostics/10web-kind-louse-wp-access-testimony-2026-10-07.md`.

---

## 2. Environment (facts)

| Item | Recorded value | Source |
| --- | --- | --- |
| Staging URL | `https://tcstaging.truth-collective.com` | `STAGING-RECOVERY-HANDOFF.md` |
| Staging files | Hostinger `public_html/tcstaging` | same |
| Staging DB | `u867403816_jdn2C` | same |
| Production | Hostinger `public_html` (no `tcstaging`); `https://truth-collective.com` | same |
| CSS method | Appearance → Customize → Additional CSS (not Code Snippets) | handoff, 8 Aug |
| Products | In-page Gutenberg/Kadence blocks. **No WooCommerce product CPT** | lock 19 Sep; REST 23 Sep |
| 10Web plugin | 10WEB manager **Active v1.20.21** as of 8 Aug 2026 | handoff |
| 10Web ticket | `#375660` | handoff |
| 10Web sandbox | `kind-louse.10web.cloud` (8–9 Aug freeze: do not port; owner 7 Oct: fake Builder site from failed migrations) | freeze note; 7 Oct testimony |

---

## 3. Chronology (dated)

| Date | Event | Evidence class |
| --- | --- | --- |
| 26 May 2026 | Additional CSS block “TC Explore Hub Overlay Animation” already in Customizer | CSS dump / audit |
| 1 Jun 2026 | Additional CSS “TC Explore Hero” homepage animation | same |
| 19 Jul 2026 | AI Mastery Book Collection page `96` last edited (pre-crash family) | Additional CSS audit 19 Sep |
| **25 Jul 2026** | **Owner-stated start of 10Web migration** | owner statement (this query / recovery narrative) |
| ~late Jul 2026 | Owner: Computers page had been built to ~90/100 Rank Math, animated, with product images and overlays, **completed just before the 10Web crash** | `diagnostics/computers-page-2026-08-08.md` (owner report logged by Cursor) |
| 24 Jul 2026 backup / later restore of that backup | Hostinger **uploads** restore from **24 Jul**; also files restore 1 Aug; DB restore **28 Jul** | handoff “Already done” table |
| 28 Jul 2026 | Staging DB restore from 28 Jul. Computers WP revisions `8271` (11:34) still contain overlay classes and 24 `amzn.to` + 40 photos | computers-page note; `computers-products-status-2026-09-19.md` |
| 28 Jul 11:43 | Page revision visually nearly as ruined as Jul 24 path; only ~4 of 30+ product cards still had both overlay + explore classes | computers-page 8 Aug, owner+editor |
| After Jul 24 uploads restore | `10web_tmp` **gone** from File Manager (8 Aug). Product files under `uploads/2026/07/` often **HTTP 404** | handoff Q1; `media-library-broken-thumbs-2026-08-09.md`; computers-page |
| 1 Aug 2026 | Hostinger **files** restore of `tcstaging` from 1 Aug | handoff |
| 8 Aug 2026 | First systematic Cursor diagnosis. Additional CSS ~57,615 chars present. No `10web`/`tenweb`/`twbb` markers in public HTML of home, Tech Hub, Computers, Speakers, Audio & Video. 10WEB manager still Active. Ticket #375660. Sitewide flicker. Hub tiles cropped; Office tile 404s from stale hrefs; Computers worst | handoff; `css-inventory-2026-08-08.md`; `homepage-audit-2026-08-08.md` |
| 8 Aug rev `8273` | Computers still has 24 Amazon codes, ~24 named cards, **40 real photos**, 8 explore-hub, 10 overlay-card | `computers-products-status-2026-09-19.md` |
| 10 Aug 2026 | Owner: 10Web not responding; 4–5 days per half-built page not viable; 10Web taken out of critical path | `THROUGHPUT-RESET-2026-08-10.md` |
| 12 Aug 2026 | Cursor “hub light” REST batch on hub **parents** (Office, Books, Self-Help, Productivity, editorial hubs, podcast). Did **not** touch Computers | `hub-light-batch-apply-2026-08-12.json`; computers status |
| 19 Aug 2026 | Cursor Computers **light rebuild**: 21 cards kept, photos swapped to SVG placeholders, explore class stripped. **This is recovery-agent data loss, not a 10Web write.** | computers status 19 Sep |
| 19 Sep 2026 | Additional CSS SHA `7e8c981ed33f52075707d54039c20817b9f6743623f27a30a3558ee1e966d6bb`, 57,615 chars, **byte-identical** to 8 Aug. Crash did **not** truncate Customizer CSS | `additional-css-audit-2026-09-19.md` |
| 23 Sep 2026 | Same Additional CSS re-pulled from homepage `wp-custom-css`; still identical. Tech Hub parent hover/copy pass applied on staging only | `additional-css-website-settings-review-2026-09-23.md` |
| 7 Oct 2026 | Public HTTP recheck (this memo): production `/` **200**; production `/technology-hub/` **404**; production Computers **404**. Staging `/` and `/technology-hub/` **200** | live HEAD this date |

---

## 4. Damage observed in the crash / restore window (late July–8 August)

These are the defects logged **before** Cursor’s August 12/19 light rebuilds. Sources: owner screenshots as described in notes, plus public HTML/CSS probes on 8 August.

### 4.1 Sitewide (not one page)

- **Global flicker** on every page, not only hubs (owner, locked 8 Aug). Notes attribute competing overlay/hover CSS and stacked `tc-explore*` / STAGING PATCH rules after markup and CSS no longer matched.
- **EXPLORE pill split** (`EXPLOR` / `E`) on Office / Analog Writing hover.
- **Cropped images, grey-bar overlays, titles in the wrong place** on hub child tiles.
- **Stale in-content links → 404** while the destination **page still existed**. Example measured 8 Aug:
  - `/file-cabinets-credenza/` → **404**
  - `/office-workspace-products-and-tools/office-file-cabinets-credenzas-essentials/` → **200** (page `6482` published)
  - Menus often had the correct nested URL; **image/block hrefs inside page content were the stale ones**.
- Other hub hrefs still pointed at dead parent `best-office-workspace-products-tools/...`.
- **23 WordPress patterns** still existed (REST 8 Aug); owner notes many pattern **URL links broke** after the crash.
- Mobile described as “horrible”; overlap with migration start **unconfirmed** in notes. Not used as a counted claim here.

### 4.2 Technology Hub parent (page `111`)

8 Aug owner inventory: **16 tiles, links dead, heavy crop**. Intended behavior (pre-damage and Additional CSS) was full-bleed image, title on the photo at the bottom, title rising and EXPLORE appearing on hover. Observed after rollback: crop, grey bars, titles off the image / overlapping EXPLORE.

Pre-10Web markup (Aug 8 page backup `page-111-technology-hub-before-REST-hub-technology-S-2026-08-08.html`): `tc-overlay-card` on the Kadence **column**, `tc-explore-hub` on the **image**. That is the working class split Additional CSS was written for.

### 4.3 Computers (page `359`) — worst child catalog case with numbers

Owner: page finished (Rank Math ~90, animations, photos, overlays) immediately before the crash.

**8 Aug live probe (post-crash, post-restores):**

| Check | Result |
| --- | --- |
| Product overlay classes | **0×** `tc-overlay-card-product` |
| `tc-explore-hub` | **4×** (should have been on product images in the finished build) |
| `tc-overlay-card` | **4×** |
| Grade markup | Rendered as **literal HTML text** / white code boxes (`<div class="tc-grade-block">`) |
| Product images | `src` still in HTML; sample file **404**, e.g. `uploads/2026/07/61of3rzFYwL._AC_SL1200_-966x1024.jpg` |
| Intro book-card classes | Still present (`tc-book-card`, `tc-leadership-body`) |

**WordPress revisions (engineering counts, 19 Sep memo):**

| Snapshot | Unique `amzn.to` | Named cards | Real photos | SVG placeholders |
| --- | --- | --- | --- | --- |
| Rev `8271` — 28 Jul 11:34 | 24 | ~24 | 40 | 0 |
| Rev `8273` — 8 Aug | 24 | ~24 | 40 | 0 |
| Live after 19 Aug light rebuild | 21 | 21 short titles | 0 | 22 |

The **19 Aug** row is Cursor recovery, not 10Web. The **28 Jul / 8 Aug** rows are the post-crash recoverable catalog. The finished Rank Math ~90 fully classed page was **not found** as a complete WP revision on 8 Aug (only ~4 of 30+ cards still dual-classed in the 28 Jul 11:43 revision). That means: product copy largely survived; the **finished overlay markup and many media files did not** survive as a single restorable revision.

### 4.4 Other hubs (8 Aug screenshot inventory, qualitative)

| Area | Logged symptom |
| --- | --- |
| Smart Lighting | Mixed crop; **white-on-white** descriptions (unreadable) |
| Tablets | Uneven cards; unwanted buttons |
| Speakers | Black bars |
| Audio & Video | Mixed; some links work |
| Office | EXPLORE split; File Cabinets tile 404 from short URL |

### 4.5 Media

`diagnostics/media-library-broken-thumbs-2026-08-09.md`: newest attachments under `uploads/2026/07/` returned **HTTP 404** for both full file and thumbnail. Standing note: July-era uploads path damage after restores. **Do not** treat this as “all media deleted”; Media Library entries can remain while disk files 404.

### 4.6 10Web residue and owner account of how the mash happened

**Owner testimony (7 Oct 2026, this Cloud run)** — not independently timed from this VM:

1. Several 10Web migrations returned **failed / disconnected**.
2. 10Web **humans** then said they needed **access inside WordPress** to pull the site through to their side.
3. **That** is when the damage occurred: **fragments of the real Hostinger WP the owner had provided, mashed with portions of the fake Builder site** hosted as `kind-louse.10web.cloud`.
4. `kind-louse` was **not** a Truth Collective design sample. It was 10Web’s **fake website** created during those migrations.

**Engineering that already sat in the repo (does not prove the WP-access hour, does not disprove it):**

- 8–9 Aug freeze: public `kind-louse.10web.cloud` preview; **do not port** 10Web page code, Tailwind, invented nav / fake category trees (Robotics mega-menu), rainbow infographic. That reject list is the same class of content as an AI Builder “fake site.”
- 3 Aug 10Web chat index (PR #5 timeline, owner-supplied export): owner told 10Web **“AI Builder created fake site again”** and asked for **human** migration of `tcstaging` with **no AI Builder / do not publish AI site**.
- 8 Aug Tech Hub screenshot inventory: **16 tiles** on a hub whose real published children were **8**. Extra tiles are consistent with foreign IA mixed onto the page; they are **not** a signed proof of a specific 10Web staff login.
- Folder `wp-content/uploads/10web_tmp` was probed (HTTP 403 on `.htaccess`) then **absent** in File Manager on 8 Aug after the 24 Jul uploads restore.
- Public page HTML on 8 Aug had **no** `10web` / `tenweb` / `twbb` markers. A mash can still exist as **wrong blocks, wrong links, invented categories, and CSS/markup mismatch** without leftover 10Web tags in the HTML.
- 10WEB **Manager plugin still Active v1.20.21** on 8 Aug (the usual WP-side install for 10Web to reach the site).

### 4.7 Production vs staging (still true 7 Oct 2026)

Public HEAD this date:

| URL | Status |
| --- | --- |
| `https://truth-collective.com/` | **200** (title “Home Page”) |
| `https://truth-collective.com/technology-hub/` | **404** |
| `https://truth-collective.com/technology-hub/computers-digital-devices/` | **404** |
| `https://tcstaging.truth-collective.com/` | **200** |
| `https://tcstaging.truth-collective.com/technology-hub/` | **200** |

Production Technology Hub returning 404 while staging returns 200 is a **live-site availability** fact as of 7 Oct 2026. This memo does not claim which restore or plugin write created the production 404; it records the split.

---

## 5. What was **not** destroyed by the crash

These facts cut against an “everything was wiped” claim and should be stated.

- **Additional CSS (Customizer) survived.** 57,615 characters, 1,682 lines, SHA-256 `7e8c981ed33f52075707d54039c20817b9f6743623f27a30a3558ee1e966d6bb`. Identical on 8 Aug, 19 Sep, and 23 Sep. The pre-10Web hover rules (`tc-overlay-card`, `tc-explore-hub`, `tc-explore-hero`, product overlay 02A) are still in the database.
- **Pages were not mass-deleted.** File Cabinets and Computers **View** URLs returned 200; 404s were often **wrong hrefs**.
- **Locked animation 02A** (product View + TC Grade buttons) is recorded as still working on a product page after the crash (“days to perfect; product page still fine after 10Web crash”).
- **Homepage content still present** 8 Aug (mission, hubs, guides); not an empty home page.
- **23 patterns** still in REST.
- Product **affiliate URLs and titles** on Computers largely remained in revisions even when photos and classes did not.

---

## 6. Damage that is **not** 10Web (must be excluded from a 10Web claim)

If these are presented as 10Web acts, the record will contradict itself.

| Later act | Date | Effect |
| --- | --- | --- |
| Hostinger **24 Jul uploads** restore applied after the crash | logged 8 Aug | Computers **worse** than the 28 Jul review. Product `/uploads/2026/07/` files 404. Notes: “Jul 24 restore crushed this page.” |
| Hostinger DB restore 28 Jul + files restore 1 Aug | handoff | Exhausted restore angles; site never fully healthy. Further full-site restores forbidden. |
| Cursor hub-parent **light rebuild** | 12 Aug | Replaced hub parent layouts (Office, Books, Self-Help, Productivity, editorial, podcast). Structure recovery, not a 10Web write. |
| Cursor Computers **light rebuild** | 19 Aug | 21 cards, **0 real photos**, 22 SVG placeholders, explore class **8 → 0**. Lost three named products vs rev 8273. Explicitly tagged `TC STAGING: Computers page light rebuild 2026-08-19`. |
| Cursor Aug 19 Tech children shells | Additional CSS audit | Speakers, tablets, monitors, etc. converted toward light templates; live `amzn.to` on most Tech children later measured at **0** while **fattest WP revisions still hold catalogs** (example: Speakers page `6741` revision raw length ~251k with 64 `amzn.to` on 23 Sep inventory). |

**Owner labor claim:** six-plus months adding products, books, and items; “4000+ products.” Cursor did not complete a unique-SKU census. September REST found catalogs **recoverable in revisions** (examples recorded 23 Sep: Speakers 64 Amazon codes, lighting security 54, chairs 37, filing 47, lighting controls 45, book children 20–31). Those numbers support “large in-page catalogs were built and then stripped from live markup,” not a verified 4000 SKU total.

---

## 7. Residual state on 7 October 2026 (staging)

Last Cursor REST writes: **23 September 2026**.

- Technology Hub parent `111`: overlay on column, explore on image, hover title `top: 28px`, Who/Why/Best filled. Modified `2026-09-23T14:32:26`.
- Computers `359`: modified `2026-09-23T13:43:26`; public HTML still contains **72** `amzn.to` strings after the 23 Sep structure pass. Catalog/photo recovery from rev `8273` is **not** signed off as complete.
- Other hub parents and homepage are not signed off.
- Production Technology Hub remains **404**.
- Rebuild is unfinished. 10Web was taken out of the critical path on 10 Aug because it was **not responding**, per `THROUGHPUT-RESET-2026-08-10.md`.

---

## 8. Evidence file index (repo)

| File | What it is |
| --- | --- |
| `STAGING-RECOVERY-HANDOFF.md` | Restore table, ticket #375660, plugin version, Phase 1 HTTP table, flicker, 10web_tmp |
| `diagnostics/computers-page-2026-08-08.md` | Computers class counts, 404 sample, Rank Math / crash narrative, revision hunt |
| `diagnostics/computers-products-status-2026-09-19.md` | Revision vs live Amazon/photo counts |
| `diagnostics/css-inventory-2026-08-08.md` | ~57KB Additional CSS; no 10Web HTML markers |
| `diagnostics/additional-css-audit-2026-09-19.md` | SHA proof CSS not crash-truncated |
| `diagnostics/additional-css-live-from-settings-2026-09-23.md` | Re-pull, same SHA |
| `diagnostics/css-chunks/additional-css-from-homepage-2026-08-08.css` | Full Customizer CSS snapshot |
| `diagnostics/media-library-broken-thumbs-2026-08-09.md` | July 2026 upload 404s |
| `diagnostics/homepage-audit-2026-08-08.md` | Home not empty; same CSS payload |
| `diagnostics/homepage-links-S0b-2026-08-08.md` | 404 vs 200 link table |
| `diagnostics/patterns-inventory-2026-08-08.md` | 23 patterns; broken pattern URLs |
| `diagnostics/hub-technology-10web-freeze-2026-08-08.md` | `kind-louse.10web.cloud`; 7 Oct owner correction: fake Builder site |
| `diagnostics/10web-kind-louse-wp-access-testimony-2026-10-07.md` | Owner: failed/disconnected migrations → WP access → mash with kind-louse |
| `diagnostics/cursor-10web-conversation-hunt-2026-10-07.md` | July Cursor was Cloud Agent; this run does not hold that transcript |
| `diagnostics/THROUGHPUT-RESET-2026-08-10.md` | 10Web not responding; out of critical path |
| `diagnostics/backups/page-111-technology-hub-before-REST-hub-technology-S-2026-08-08.html` | Pre-rebuild Tech Hub markup with overlay+explore split |
| `diagnostics/backups/page-359-rev8273-2026-08-08-raw.html` | Computers catalog revision used as recovery source |
| `docs/TC-LOCK-2026-09-19.md` | Visual lock; 10Web captures = evidence not a model |

Owner-held items **not in this repo** that counsel typically needs: 10Web contract, ticket `#375660` thread, Hostinger backup timestamps, pre-25-Jul full-site backup, Rank Math screenshots, medical/work log, Semrush/analytics, the `kind-louse` / 10Web builder project export, and the **July Cursor conversation** (prep / during / after). This Sep 19 Cloud run does **not** hold that transcript. Hunt result: `diagnostics/cursor-10web-conversation-hunt-2026-10-07.md`. Strongest Cloud URL to try: `bc-b360733d-fbaa-412a-bff6-bcacdceab1dd` (PR #2, 14 Jul 2026).

---

## 9. One-sentence technical summary

Between the owner-stated 25 July 2026 10Web migration start and the 8 August 2026 diagnosis, Truth Collective’s WordPress **Customizer CSS survived intact**, but **page block markup, locked animation classes, in-content permalinks, July 2026 upload files, pattern links, and production Technology Hub availability** were observably damaged; Hostinger restores (especially the 24 July uploads path) made Computers worse; later Cursor light rebuilds caused **further** catalog stripping that must not be billed as 10Web’s write.
