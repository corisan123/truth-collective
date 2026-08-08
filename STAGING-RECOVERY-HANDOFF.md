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

## After Phase 1 (only when all three answers are clear)

Likely next focus (not today): fix **wrong hub tile URLs** in block content so they match real page permalinks — starting with File Cabinets on the Office hub. CSS cleanup for EXPLORE/overlays after that. Restores only if Phase 1 proves media was never actually replaced.

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
