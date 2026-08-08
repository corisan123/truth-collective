# Truth Collective — Staging Recovery Handoff

**Site:** https://tcstaging.truth-collective.com  
**Hostinger path:** `public_html/tcstaging`  
**Staging DB:** `u867403816_jdn2C`  
**Live:** separate under `public_html` (no `tcstaging` in path)

---

## Hard rules

1. **Never** use Website backup restore (that targets live).
2. **No restore roulette.** Diagnosis first. No new restores until Phase 1 answers are written down.
3. **Do not Continue** any unfinished Updraft restore (Jul 28 `db.gz` was missing from disk — dismiss it).
4. LiteSpeed: stay purged / off. Rename `object-cache.php` if present.
5. Do **not** wait on 10Web for recovery. Ticket **#375660** = RCA/compensation only.
6. Work in **short steps, one question at a time.**

---

## Already done (Hostinger success logged)

| Action | Date / note |
|--------|-------------|
| Files restore `tcstaging` | from **2026-08-01** |
| DB restore `u867403816_jdn2C` | from **2026-07-28** |
| Uploads-only restores | Jul 28 and Jul 24 — front end looked unchanged |
| Permalinks | Saved as **Post name** |

---

## Key findings (pre–Phase 1)

- Many “missing” pages still exist in **WP Pages**. Example: File Cabinets slug `office-file-cabinets-credenzas-essentials`, parent **Office Workspace Products and Tools**.
- Hub tiles often link to **wrong short/old URLs** → 404. Example: `/file-cabinets-credenza/` instead of the nested path.
- Working Office path example: `/office-workspace-products-and-tools/best-analog-writing-tools/`
- Visual issues (still after Jul 24 rollback): EXPLORE split as `EXPLOR` / `E`, overlay flicker, cropped/grey-bar images, white-on-white Smart Lighting descriptions, Computers page scrambled. User: child blocks were never built this way — full image + bottom title rising on hover was intended.
- **Sitewide flicker (Daniel; confirm locked 2026-08-08):** screen / pages **flicker really bad on every page**, not only hubs. Prior handoff only noted “overlay flicker” in passing — treat as a **global** symptom (likely competing hover/overlay CSS, absolute image layers, or stacked `tc-explore*` / STAGING PATCH rules). Do not chase with restores. Address after or with controlled Additional CSS layer disables; note separately from Computers class-stripping.
- Likely cause: leftover **Cursor/custom `tc-explore*` CSS** (and/or mismatched block classes), not missing media. `10web_tmp` is **gone** on live after Jul 24 restore.

---

## Phase 1 — diagnosis only (no restores)

Answer these three, then stop.

### Q1 — Is `10web_tmp` still under staging uploads?

**Where:** Hostinger → **File Manager** (live files, not Restore browser) →  
`public_html/tcstaging/wp-content/uploads/`  
**Look for:** folder named `10web_tmp`

| Result | Meaning |
|--------|---------|
| Folder **still there** | Jul 24 uploads restore likely **merged**, did not fully replace |
| Folder **gone** | That restore may have replaced uploads (or folder was removed another way) |

**Answer: NO — gone (live File Manager, 2026-08-08).**
- Jul 24 backup uploads was clean; live `…/uploads` also has no `10web_tmp` after last night’s restore.
- So uploads restore did remove 10Web residue (not left behind by a merge).
- Note: earlier public HTTP still returned 403 on `10web_tmp/.htaccess` — treat File Manager as source of truth; ignore stale web probes for this folder.

---

### Q2 — Does **View** work for File Cabinets + one Tech child?

**In WP Admin → Pages:**

1. Find **File Cabinets** (`office-file-cabinets-credenzas-essentials`) → click **View**.
2. Pick one Tech child under Technology Hub (e.g. Computers) → click **View**.

| Result | Meaning |
|--------|---------|
| View opens the real page | Page content exists; 404s are mostly **wrong links**, not missing pages |
| View 404s or blank | Deeper content/permalink problem — note exact URL |

**Public probe (2026-08-08):**

| URL | Status |
|-----|--------|
| `/file-cabinets-credenza/` (wrong short link on Office hub tile) | **404** |
| `/office-workspace-products-and-tools/office-file-cabinets-credenzas-essentials/` | **200** |
| WP REST: page `6482` published with correct link | yes |
| `/technology-hub/computers-digital-devices/` | **200** |

Office hub HTML still contains a tile linking to the **wrong** short URL. Menus use the correct nested URL.

---

### Q3 — Is EXPLORE / crop / white overlay a CSS issue (not media / not another restore)?

**Answer: YES — CSS (and CSS vs restored block markup). Not missing uploads.**

User screenshots after Jul 24-era rollback still show:
- Office / Analog Writing: `EXPLOR` / `E` split on hover pill
- Hub child tiles: cropped images, grey bar overlays, titles in wrong place
- Smart Lighting: some tiles full, some cropped; white-on-white description (unreadable)
- Expected design: full-bleed image, title at bottom, rise + lift/darken on hover

**Public probe (2026-08-08):** Additional CSS still injects Cursor-era rules:
- `.tc-explore-hub::after` / `.tc-explore-hero::after` → `content: "EXPLORE"` + `letter-spacing`
- Absolute image fill / overlay / hover darken rules on `.tc-explore-hub`

These patches can survive a “pre-10Web” content rollback if they live in **Customizer Additional CSS** (DB) or theme/file CSS. They are **not** fixed by another uploads restore.

→ **Next phase (after Phase 1):** CSS / block cleanup — disable or remove conflicting `tc-explore*` rules, then fix hub tile links. **No more restores for this symptom set.**

---

## Do not do yet

- No more Hostinger restores (files, DB, or uploads)
- No Updraft Continue
- No live-site changes
- No waiting on 10Web before diagnosis is written down

---

## After Phase 1 (answers clear enough to proceed)

**Do not restore again for crops / EXPLORE / black bars / uneven cards.** That symptom set is CSS + block markup.

User inventory (2026-08-08 screenshots): Smart Lighting children, Technology Hub (16 tiles, links dead, heavy crop), Tablets (uneven cards / unwanted buttons), Speakers (black bars), Audio & Video (mixed; some links work), Computers (**worst** — overlays collapsed, ratings raw, images gone). Feels worse after Jul 24-era restore because **old Cursor “STAGING PATCH / tc-explore” CSS** is still applied on top of rolled-back blocks.

Live HTML check: **no** `10web`/`tenweb` markers in page HTML. ~57KB of `tc-explore*` / STAGING PATCH CSS still present. See `diagnostics/css-inventory-2026-08-08.md`.

**Link pattern (confirmed, not “page deleted”):**
- File Cabinets **page exists** and loads:  
  `/office-workspace-products-and-tools/office-file-cabinets-credenzas-essentials/`
- Office hub **tile still points to old short URL** → 404: `/file-cabinets-credenza/`
- Other hub hrefs still use dead old parent `best-office-workspace-products-tools/...` (404), e.g. desk-accessories.
- Menus often have the correct nested URL; **image/block links inside page content are stale.** This is editable content, not unrecoverable corruption.

**CSS location / method (Daniel confirmed 2026-08-08):** Working method stays **Appearance → Customize → Additional CSS**. Code Snippets plugin has never been used (fact only — not a decision to switch). Additional CSS holds stylesheets, not page HTML.

**Next work order:**
1. Disable/remove conflicting Additional CSS (`tc-explore-hub`, product overlay patches) — crops/black bars.
2. On each hub page, update block link URLs to match **Pages → View** permalinks (start: Office hub File Cabinets tile).
3. **10WEB manager is still Active** (v1.20.21). **User pause (2026-08-08):** do **not** deactivate/delete 10Web yet — user too sick/exhausted; wants 10Web to own fix via ticket **#375660**. Helpers: do not push plugin changes or page-by-page edits until user asks.
4. Restores only if a later check proves missing media — not for this visual/link mess.

### Angie-assisted path (started 2026-08-08 ~09:13)
- User wants **Angie (Elementor)** to act inside WP, under **Cursor-written prompts only**.
- Protocol + task queue: `diagnostics/ANGIE-CONTROL.md`
- Still: no restore roulette; leave 10Web alone until user says otherwise.
- First Angie work: **one Office hub link** (prove control), not site-wide rebuild.

### Standing brief (source of truth)
- `docs/TC-STANDING-BRIEF.md` — §§1–8 from Vercel/10Web PDF + Master Brief 2.0 + Migration Brief + Launch tips 6.
- Cursor rule: `.cursor/rules/truth-collective.mdc`
- References: `docs/brand-references/`

---

## Quick reference — safe vs unsafe paths

| Safe (staging) | Unsafe (live) |
|----------------|---------------|
| `public_html/tcstaging` | `public_html` (no tcstaging) |
| DB `u867403816_jdn2C` | other Hostinger DBs |
| Staging-only backups of that path/DB | Website backup restore |

---

## Session note for helpers

User is recovering from chemo/immunotherapy. Prefer **one short step**, **one question**, wait for the answer, then continue. No long checklists dumped at once in chat.

**Business priority (standing brief §13):** Fix staging → polish → Semrush → launch → then social/Pinterest. Do not start binder integration, Semrush, or social work until staging recovery step 1 is done.

**Later action (not now):** Mobile / cell-phone view is **horrible** (Daniel checked a few days ago; may overlap 10Web migration start — unconfirmed). Fix only after desktop overlay/link recovery is stable. Do not start a mobile redesign mid-recovery.

### Computers page (2026-08-08) — markup, not CSS wipe
- Live + editor destroyed: raw `tc-grade-block` HTML as text, broken images, overlaps.
- Only classes left on page: intro `tc-book-card` + `tc-leadership-body`. **Product blocks lost overlay/explore/product classes.**
- Additional CSS still loads sitewide — classes missing on blocks so rules never attach.
- **Jul 24 restore crushed this page.** Jul 28 review yesterday was bad but not this bad. Do not re-run Jul 24.
- Product-row snippet (Jul 24-era): Kadence image still had `tc-explore-hub` + affiliate link; overlay belongs on Section, not the image — matches original split architecture.
- Detail: `diagnostics/computers-page-2026-08-08.md`
- **Next:** try **Page Revisions** (prefer ~Jul 28-era) before rebuilding; never another Jul 24 full restore.
