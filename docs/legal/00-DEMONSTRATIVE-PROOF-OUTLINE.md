# Demonstrative proof outline — 10Web and `tcstaging`

**Prepared:** 7 October 2026  
**Compiler:** Cursor Cloud Agent `bc-3c3a1616-bd53-407e-8562-11da050498f8` (staging recovery run, not the July migration agent)  
**For:** Daniel Reid → counsel  
**Not a legal opinion, not an expert declaration, not a damages model.**  
This is the organized proof map. Files this agent has not seen (full 53 10Web threads, Hostinger restore-history export, recovered Cloud Agent Print-PDF) are marked **GAP**.

---

## 1. One-page case in sentences

Daniel rebuilt Truth Collective on Hostinger **staging** (`tcstaging`) after an **earlier, separate** live-site failure he attributes to **Claude**, not 10Web. By late July 2026 that staging site was a large custom WordPress property (Astra, Kadence, Rank Math, locked `tc-*` hover/overlay/book CSS). He hired 10Web to **polish and migrate a copy**, not to regenerate the site with AI Builder.

10Web’s **automated migrate failed repeatedly** (disconnect / failed UI; product told him to contact support). Their AI flow created **fake Builder sites** (Daniel 26 Jul: two fake pages deleted; Nazeli 27 Jul already saw `active-bluegill.10web.cloud`; later `kind-louse.10web.cloud`). He forbade AI Website Builder in writing. **Nazeli then required a temporary WordPress admin** (`support@10web.io`) so 10Web could migrate **from their end** (27–28 Jul emails, exhibits p17/p18). After that period, staging no longer matched the pre-migration build (8 Aug diagnosis: stripped overlay classes, mass stale 404s, July upload files 404, `10web_tmp`, Manager plugin still Active, flicker, EXPLORE split). Hostinger restores **did not return** the working site; a Jul 24 uploads restore **made Computers worse**. On 30 Sep 2026 Nazeli **denied** destroying the site or backups, recast the **access they had demanded** as Daniel’s authorization, admitted the migration **was not completed**, and refused the requested refund.

**That is the 10Web case this file can support.** It is documentary and technical. It is not a verdict.

---

## 2. 10Web conduct that **is** documented (use these; they are the proof)

Numbered findings. Each has a source. If a finding has no source in this repo, it is not listed here.

| # | Finding | Source class | Where |
| --- | --- | --- | --- |
| F1 | 10Web was engaged to migrate/polish **existing** `tcstaging` WordPress, not to invent a new AI site | Owner + 10Web AI log index | PR #5 `docs/10WEB-SUPPORT-TRANSCRIPT-TIMELINE.md` Phase A (24–25 Jul) |
| F2 | 10Web promised preserve structure / custom code / affiliates / copy does not affect live until DNS | 10Web AI statements in that log | same, Phase A “Key promises” |
| F3 | Automated migrate **failed / disconnected** (including 6+ hour run; UI: contact support) | Owner contemporaneous 26 Jul email on Nazeli thread | PR #6 `exhibit-10web-demands-admin-access-p18.png` |
| F4 | 10Web AI created **fake website pages**; Daniel deleted them | Same 26 Jul email | p18 |
| F5 | 10Web already had a hosted site `active-bluegill.10web.cloud` on his **one** slot | Nazeli 27 Jul | p18 |
| F6 | Nazeli **demanded** temporary WP admin for `support@10web.io` and dashboard access; they would **access the existing WP dashboard** and migrate **from our end** | Nazeli 27–28 Jul | p17, p18 |
| F7 | Owner forbade **AI Website Builder**; asked human migrate of `tcstaging`; do not publish AI site | 3 Aug in chat index; 4 Aug in BDM testimony | PR #5 timeline Phase C; PR #6 §3.4 |
| F8 | Ticket merged into **#375660** without a completed preserve-copy | Nazeli 4 Aug (index) | PR #5 timeline |
| F9 | 10WEB **Manager** still **Active v1.20.21** on staging 8 Aug | Recovery handoff | `STAGING-RECOVERY-HANDOFF.md` |
| F10 | Folder `uploads/10web_tmp` existed (HTTP 403 on `.htaccess`) then **gone** after Jul 24 uploads restore | 8 Aug diagnosis | handoff Q1 |
| F11 | `kind-louse.10web.cloud` existed; freeze 8–9 Aug: do not port fake trees / Tailwind / 10Web code | Recovery freeze | `diagnostics/hub-technology-10web-freeze-2026-08-08.md` |
| F12 | 8 Aug staging was **not** a healthy pre-migration site: overlay classes stripped on Computers, stale hub 404s, flicker, EXPLORE split, July media 404s | Cursor probes 8 Aug | handoff; `computers-page-2026-08-08.md`; `css-inventory-2026-08-08.md`; `media-library-broken-thumbs-2026-08-09.md` |
| F13 | 30 Sep letter: 10Web **admits** migrate **not successfully completed**; **denies** destroy/delete backups; **reframes** admin access as Daniel “provided” and “expressly authorized” Migration Assistant; **refuses** 3-month refund | Nazeli 30 Sep | PR #6 `exhibit-10web-sept30-denial.png` |
| F14 | F6 vs F13 is a **documentary contradiction** on who required WP access | Same two exhibit sets | `diagnostics/WHAT-SEPT30-VS-JULY-EMAILS-PROVE-2026-10-07.md` |

**F6 + F3 + F4 + F13 is the strongest 10Web-fault package this agent has actually seen.** It is not “no fault.” It is also not a signed confession that they restored over source or deleted Hostinger backups (they deny that; see §4).

---

## 3. Staging damage that **is** measured (8 Aug) — causation still mixed

These are **facts of condition**, not automatic 10Web-only causation:

- Additional CSS **survived** (~57,615 chars). 10Web did **not** wipe Customizer CSS. Locked 02A product overlay still described as working after the crash.
- Public HTML 8 Aug had **no** `10web`/`tenweb`/`twbb` **tags**. Damage showed as **WordPress blocks, classes, links, and media**, not leftover 10Web HTML comments.
- Computers: **0×** `tc-overlay-card-product` live; grade markup as literal text; sample July upload **404**. Revisions 28 Jul still held overlay classes and Amazon codes.
- Hub tiles: wrong short URLs → 404 while the **page still existed** at nested permalinks.
- Tech Hub 8 Aug inventory: **16 tiles** vs **8** real published children (consistent with foreign IA / fake-site mash; not a named staff login log).
- Production `/technology-hub/` still **404** on 7 Oct 2026; staging Tech Hub **200**.

Owner testimony (7 Oct): mash happened when **humans required inside-WP access** — real fragments + kind-louse. That **fits** F6 + F11 + 16-vs-8 tiles. This VM did not watch the admin session.

---

## 4. Call-outs: where 10Web is **not** proven, or **other people** wrote

Counsel will be hurt if these are billed as 10Web.

| Item | Who | Why it must be listed |
| --- | --- | --- |
| Earlier **live** site crash | Owner: **Claude** / other AIs, months before 10Web | Separate incident. Do not merge into the 10Web claim. |
| Hostinger **24 Jul uploads restore** | Hostinger + Daniel restore choice | 8 Aug notes: Computers **worse** than 28 Jul review. Product files under `uploads/2026/07/` 404. |
| Hostinger DB 28 Jul / files 1 Aug | Same | Logged “success”; site still broken. Safety net failed. Not the same as “10Web deleted the backup file,” unless Hostinger logs show 10Web as the actor. |
| Updraft Jul 28 `db.gz` **missing from disk** | Unknown actor | BDM testimony. Need Hostinger File Manager proof of who deleted it. |
| Cursor hub-parent **light rebuild** 12 Aug | This recovery project | Structure recovery; not a 10Web write. |
| Cursor Computers **light rebuild** 19 Aug | Same | Photos → SVG placeholders. Tagged in page. **Further catalog stripping.** |
| “4000+ products destroyed” | Owner testimony | This agent did not count 4000 unique SKUs. Revisions show large in-page catalogs in the **tens to low hundreds** of Amazon codes per page, plus 2324 media items. |
| 10Web **restored over source** or **deleted all backups** | 10Web **denies** (F13) | Not proven by the four screenshots. Need restore-history export. |
| Legal guilt / “culpability” | Fact-finder | This outline supports **failed service, required access, AI fake sites, unrepaired staging, and a denial that omits their demand.** It does not close damages or liability. |

If asked “is there no fault on 10Web?”: **No.** Findings F3–F8, F9–F11, and F13–F14 are 10Web-side. If asked “is destruction 100% 10Web with nothing else in the chain?”: **No.** See the table.

---

## 5. Demonstrative timeline (use on a board)

```
Pre-Jul 2026     Staging rebuild on Hostinger; locked tc-* CSS (git May–Jul)
24–25 Jul        10Web sales: preserve promises; Cursor checklist; LiteSpeed off
25–26 Jul        Automate migrate FAIL / disconnect; AI fake pages (p18)
27–28 Jul        Nazeli DEMANDS WP admin “from our end” (p17/p18)
28 Jul–3 Aug     More failed/disconnected; AI Builder ban restated 3 Aug
~3–8 Aug         Staging observed destroyed vs pre-migration (handoff 8 Aug)
7 Aug            Incident into #375660; Hostinger restores do not heal
10 Aug           10Web out of critical path (not responding)
12 / 19 Aug      Cursor light rebuilds (recovery; further loss — disclose)
30 Sep           Nazeli denial: you authorized access; we didn’t destroy; no refund
7 Oct            BDM testimony PR #6; this outline
```

---

## 6. What to hand counsel tomorrow (minimum packet)

From GitHub:

- PR #6 zip: testimony + four exhibits  
- This folder: `00-` and `01-`  
- `STAGING-RECOVERY-HANDOFF.md`  
- `diagnostics/10web-migration-damage-evidence-2026-10-07.md`  
- `diagnostics/computers-page-2026-08-08.md`  
- `diagnostics/css-inventory-2026-08-08.md`

From the PC (not in this git):

- All 53 10Web threads as PDF  
- Hostinger restore-history screenshots (Jul 24 / 28 / Aug 1)  
- Print-PDF of the recovered **Cloud Agent** 10Web thread  
- 10Web contract / invoices / 30 Sep letter as original PDF (not only the screenshot)  
- Pre-migration screenshots / Rank Math Computers ~90 if they exist  

Cover note, two sentences:

> 10Web’s migrator failed; they required WordPress admin to pull from their end; AI Builder sites already existed against written instructions; staging was not the pre-migration site by 8 August; on 30 September they denied fault and omitted their own access demand. Hostinger restores and later Cursor rebuilds caused additional change and must be listed separately.

---

## 7. Gaps (the “1000 more things” — fill the index, do not wait on a new theory)

Priority order:

1. Remaining **52** 10Web email/chat PDFs (especially any that show Manager writes, Migration Assistant, or WP-admin session).  
2. Hostinger **restore log** export for `tcstaging` and uploads Jul 24–Aug 1.  
3. Recovered Cursor **Cloud Agent** Print-PDF + `bc-` URL (Path B).  
4. Original **30 Sep PDF** (full header/footer, not only the highlighted screenshot).  
5. Pre-25 Jul backup artifact or screenshot of working Computers / Tech Hub.  
6. WP **Users** screenshot if `support@10web.io` admin still appears or appeared.  
7. Payment / plan records (AI Starter vs Pro trial mismatch).  
8. GSC / live 404 evidence (production Tech Hub 404 on 7 Oct).  

Each new file gets one row in `01-EVIDENCE-INDEX.md` (ID, date, source, 4-line summary). Do not rewrite this outline until those land; append.
