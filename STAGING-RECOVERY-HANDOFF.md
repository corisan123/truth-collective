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
- Visual issues seen: EXPLORE split as `EXPLOR` / `E`, overlay flicker, cropped/grey-bar images, Computers page scrambled.
- Uploads previously had `10web_tmp` (10Web evidence). Need to know if it survived the Jul 24 uploads restore (merge vs real replace).

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

**Status (2026-08-08):**
- Jul 24 **backup** browser at `…/uploads` shows: `2026`, `backup`, `rank-math`, `wpforms` — **no** `10web_tmp`. That backup is clean. Good.
- User reports after last night’s restore, 10Web is gone from their view.
- Public probe still gets **403** on `/wp-content/uploads/10web_tmp/.htaccess` (and on `plugins/10web-manager/`). Needs a quick **live File Manager** confirm (not the Restore/backup file list) before closing Q1.

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

### Q3 — Is EXPLORE a CSS issue (not a broken image)?

**Check:** Appearance → Customize → Additional CSS (or page source).  
Look for rules like `.tc-explore-hub::after` / `.tc-explore-hero::after` with `content: "EXPLORE"`.

**Public probe (2026-08-08):** Confirmed CSS, not media.

- Text comes from CSS `content: "EXPLORE"` on `::after`
- `letter-spacing: 0.22em` (hub) / `0.2em` (hero)
- Padding/`overflow` on the pill can make it look like `EXPLOR` + stray `E`
- Overlay flicker is also CSS/animation related (`.tc-explore-hub` hover / `::before` / `::after`)

→ Fix later with CSS edits. **Not** an uploads restore problem.

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
