# Damages — sitewide, US Letter scale, missing children, exclusive migrate-window actor

**Prepared:** 12 October 2026 (this revision answers Daniel Reid’s objection that earlier memos on this branch understated size, omitted damages beyond Technology Hub, and treated 10Web’s role as if it were unproven).  
**Those objections are accepted.** This file is the controlling damages language. Do not reuse “65 pages were damaged” or “Tech Hub only.”

**Not a legal opinion.**

**Documents read for this file:** the five PDFs Daniel named (Cursor/BDM summary; Systems copied with 10web found; WP Error DEBUG log; Hostinger Error Log 10-10-2026; Hostinger Raw Backup History 10-10-2026); GitHub compare `cursor/10web-lawsuit-testimony-2672`; live WordPress REST census 12 October 2026 (59 published, 10 drafts); BDM testimony §6–§7.

---

## 1. Size language (US Letter, not WordPress URL count)

A WordPress “page” is a URL. Counsel uses **US Letter (8.5 by 11 inches; Daniel’s 8 x 11)** as the universal printed-page unit.

| Unit | Figure | Whose number |
| --- | --- | --- |
| WordPress URLs pre-migration (hub / sub-parent / child / sub-child) | **65+** | BDM testimony §1.1 |
| Letter-size pages of content **per** WordPress URL | **55 to 100+** | Owner, from pre-migration pages saved on the CPU |
| Site equivalent | **3,575 minimum to 6,500+** letter pages (65 × 55 to 65 × 100, plus the 65+ and 100+ tails) | Owner conversion, 12 Oct 2026 |
| On-page books / products / items on 24 Jul 2026 | **about 4,000 ±** | Owner census of presence on pages, not live `amzn.to` count |
| Staging disk / database | **~6.73 GB / ~235 MB** | BDM §1.1 |

Counsel sentence:

> The site was not a 65-page brochure. It was 65-plus WordPress URLs. Each URL held about 55 to more than 100 US Letter pages of products, descriptions, and editorial copy. Printed, that is about 3,575 to 6,500-plus letter-size pages, plus about 6.73 GB of files and a 235 MB database.

Do not write: “65 pages were damaged.” That sentence is false as a damages statement.

Post-crash HTML on this agent (for example Computers revision 8273, already after 10Web) is a **gutted remnant**. Word-count on that remnant is not a measure of the pre-migration letter-page size. To pin one URL inside the 55–100 band on paper, send a Print-to-PDF of that URL from a **pre-migration** save (Computers is the worst catalog child). Until that sample arrives, use Daniel’s range. Do not shrink it with post-crash REST.

---

## 2. Destruction is sitewide. REST cannot rebuild missing children.

This recovery agent’s REST API can only rewrite WordPress posts that still exist. If a sub-parent, child, or sub-child is gone from `wp_posts`, REST has nothing to apply. Rebuild-from-memory is not recovery of the pre-migration page.

Live REST on 12 October 2026: **59 published** pages, **10 drafts**. Pre-migration content-heavy URLs: **65+**. A 200 status is not an undamaged page. Many published URLs are shells (stripped classes, stale hrefs, missing catalogs).

### Technology Hub (parent 111) — one tree, not the whole site

Published children still in WP (8): Computers, Monitors, Audio and Video, Headphones, Desk Speakers, Projectors and Microphones, Digital Smart Tablets, Interactive Digital Displays.

**Still missing as dedicated posts (REST cannot create them from live data):**

- Emerging Technologies (tile existed; no child page)
- AI Wearables (tile existed; no child page)

8 August parent showed **16 tiles vs 8** published children. Drafts still in WP, not recovered catalogs: Video Technology Devices (1394), Premium Interactive Digital Displays (2962), Projectors/Screens/Video Collaboration (5938). Computers (359) still exists as a URL and is not a restored catalog (0 product overlay classes on 8 Aug; July images 404; later placeholder rebuild).

### Office Workspace (parent 5939)

Published children still in WP: Analog Writing, Executive Chairs, Executive Desks, Laptop Stands, Desk Essentials, File Cabinets. BDM §6.2: **mass 404s on the Office tree**, EXPLORE split on Analog Writing, hub tiles pointing at wrong short slugs while nested pages still existed. Existing URLs are not proof the pre-migration Office catalogs survived.

### Smart Lighting (parent 115)

Published children still in WP: Advanced Lighting, Smart AI Lighting, Bulbs and Strips, Controls, Security Lighting. 8 August: crop, white-on-white copy, same overlay/explore break as other hubs.

### Productivity (parent 5680)

Published child still in WP: Cable Management only. A hub of this size with one remaining child is a missing-children fact, not a complete tree.

### Recommended Books (parent 38)

Published children still in WP: Communication, Communication Advanced, Decision Making, Leadership, Voices of Influence, Project Management, Wealth. Drafts not recovered: Entrepreneurship (392), High Performance and Execution (92). Owner census: about **1,000 books / 20-plus categories** pre-migration; about **200 remaining**, all damaged, mostly older Gutenberg-only pages.

### Self-Help and Mental Wellness (parent 86) and related URLs

Published: Mental Wellness Books, Support/Recovery, Meditation, Self-Help books, Mental Wellness Support, Podcasts for wellness. Non-monetized editorial. Not an Amazon-link census.

### Editorial hubs (also damaged; not Tech Hub)

- The Ones Who Gave Everything (5897) plus Billy Graham child. Owner: 278-plus images, 300-plus people approved, each person-file hundreds of letter pages.
- The Truth Untold (2516): Parts 1, 2, 6 published; Parts 3–5 still **draft**; Parts 7–10 still **draft** (6043).
- AI Mastery Book Collection (96) and children; AI Mastery Podcast (7694).
- Homepage (5): hero motion broken; overlay+explore crop still present.

### Production

`https://truth-collective.com/technology-hub/` still **404** as of 7 October 2026. Staging is the copy 10Web was hired to migrate. Live production never received a working hub tree.

### BDM §6.2 damage categories (already sitewide, 7 October)

Information architecture and links destroyed on **Technology and Office** trees; media library / product images wrong, cropped, or 404; `10web_tmp` under uploads; custom overlay/explore/hero systems dead or wrong **on every page** (flicker); layout scramble on money pages; fake Builder sites; backup safety net failed; 10Web support silence then 30 September denial.

---

## 3. Who was inside WordPress during the migrate

**The only vendor documented inside WordPress between 25 July and 7 August 2026 is 10Web.**

There is no testimony, error-log actor, or Site Health user in this packet naming another AI or person as a WordPress administrator in that window. Cursor/BDM prepared checklists and paste-ready instructions. BDM: “I do not log into WordPress or Hostinger myself. Daniel executes clicks.” Daniel created the admin 10Web **demanded**, deleted fake AI pages, and emailed daily after they went silent. Later Hostinger restores and this recovery agent’s REST writes **after 8 August** are recovery layers. They are not a second migrate-window vendor.

10Web’s own documents and logs:

| Document | What it shows |
| --- | --- |
| Nazeli 27–28 Jul emails | Demand temporary WP admin `support@10web.io`; migrate **from our end** |
| Nazeli 30 Sep letter | Admits WP admin, Migration Assistant, Updraft use; admits migrate **not completed** |
| Site Health 10 Oct (`Systems copied with 10web found`) | **10WEB manager v1.20.21 still Active**, 11 weeks later |
| Error log 25 Jul 20:00 UTC | `10web-manager/includes/class-rest-api.php` executing on staging on migrate-start day |
| Error log 3 Aug 15:57 UTC | Same 10Web Manager REST class again |
| Error log 7 Aug 14:15 UTC | Kadence and Rank Math Pro files **missing** (critical fatals) while PHP `include_path` still lists **four 10web-manager vendor/pear paths** |

The logs do not contain the English sentence “10Web destroyed the website.” They do show 10Web Manager executing on staging during the migrate, and 10Web Manager still on the include path at the moment Kadence and Rank Math Pro failed to load, on the incident-letter day.

Daniel emailed daily, in his words begging, for weeks after 10Web went silent. BDM §6.2 item 7 and §7: non-response, then the 30 September closure letter.

---

## 4. Neutral summary of the five PDFs named in this message

| PDF | Neutral summary |
| --- | --- |
| Cursor summary of 10web destruction.pdf | BDM 7 Oct testimony. 65+ hub/child/sub-child URLs, custom `tc-*`, 10Web demanded admin, sitewide damages, support silence. |
| Systems copied with 10web found.pdf | WP Site Health 10 Oct 2026. 10WEB manager still Active on `tcstaging`. Continued plugin presence, not a CSS-theft log. |
| WP Error DEBUG log.pdf | `tcstaging` error_log. 10Web Manager REST on 25 Jul and 3 Aug; 7 Aug Kadence/Rank Math fatals with 10Web on include_path. |
| Hostinger Error Log 10-10-2026.pdf | Same log family as the WP debug export. |
| Hostinger Raw Backup History 10-10-2026.pdf | Updraft known-backups on 10 Oct: 16 timestamps, **oldest 15 Sep 2026**. Pre-25 Jul Drive databases are **not** in this server history. |

If “five separate documents found inside WordPress” means five **other** files besides these PDFs, send their exact names. This agent will ingest those next instead of guessing.

---

## 5. Specific documents still useful (ask, do not call the case unproven)

The case is not waiting on a confession line. These files would **pin numbers**, not establish that 10Web was in WordPress (that is already documented):

1. Print-to-PDF of **one** heavy pre-migration catalog URL (Computers) so letter-pages for that URL can be counted on paper.  
2. Pre-migration list of all **65-plus titles and parents** (Rank Math sitemap or Pages export), to mark each URL exists-intact / exists-gutted / missing.  
3. Remaining 10Web threads (the sample is 1 of 53).  
4. Drive file `backup_2026-07-23-1930_…-db.gz` for offline SQL read. **Do not restore it onto staging.**

---

## 6. Counsel sentences

Use:

> Destruction was sitewide: hub parents, sub-parents, children, and sub-children across Technology, Office, Smart Lighting, Productivity, Books, Self-Help, and editorial hubs including The Ones Who Gave Everything and The Truth Untold. Some child and sub-child pages are still missing from WordPress. REST rebuild cannot create those URLs from posts that are gone. Pages that still return 200 are often gutted shells. The printed size of the pre-migration site is about 3,575 to 6,500-plus US Letter pages.

> The only vendor inside WordPress during the migrate is 10Web. They demanded admin access, their Manager plugin ran on staging on 25 July and 3 August, Kadence and Rank Math failed on 7 August with 10Web still on the include path, Manager was still Active on 10 October, and they later denied destroying the site. No other AI or person is named as a WP admin in that window.

Do not use:

> 65 pages were damaged.  
> Only Technology Hub was destroyed.  
> There is no proof 10Web was in WordPress.  
> Post-crash REST word-count is the size of the original site.
