# Exhibit note — Claude conversation, 2026-08-09 (Daniel export)

**Source:** Daniel Reid paste into Claude, **2026-08-09**.  
**Use:** Legal bundle (10Web damage narrative) + **design SPEC** for Cursor after repair (not mid-repair).  
**Pair with:** `docs/10WEB-SUPPORT-TRANSCRIPT-TIMELINE.md`, Cursor Desktop relay exports (`docs/CURSOR-10WEB-RELAY-EVIDENCE-SEARCH.md`).

---

## Daniel statements (evidence — user's words)

| Date | Statement |
|------|-----------|
| **2026-08-09** | Migration to **10Web ~two weeks prior** (~late July 2026) **destroyed the site within WordPress**. |
| **2026-08-09** | Goal of 10Web was **improve and polish**, not rebuild from scratch. |
| **2026-08-09** | **Cannot roll damage back** — damage **tangled in WordPress**. |
| **2026-08-09** | Damage affected **backups saved from before 10Web started** (user assertion — counsel may compare to Hostinger/Updraft logs). |

Repo handoff (`STAGING-RECOVERY-HANDOFF.md`) documents **Jul 24 / Jul 28 / Aug 1** restores and cautions **restore roulette**; it does **not** replace Daniel’s **8/9** statement about **pre-10Web backup corruption**. Treat both as exhibits.

---

## Claude → Cursor SPEC (8/9 — polish lane, post-repair)

**Context:** 10Web samples showed patterns **already partially on site** (copy exists); missing layer = **presentation/hover**, **Cursor lane**.

### New vs already captured (Claude analysis)

| Pattern | Status |
|---------|--------|
| Two-button **Details/Reviews** on small product images; 10Web **cover** landing animation | Already in Standing Brief / prior notes — **consistent** |
| **Richer hover** on large category tiles (heading + line + 3 bullets + navy **View Collection**) | **New SPEC** vs plainer EXPLORE-only hub tiles |
| **Shop archive** page (“Curated Collection”: sidebar filters, sort, grid, strike price, Buy on Amazon) | **New page type** — do not merge with hub |
| **Editorial grid** on navy: desaturated thumb → color on hover + date + **Read Feature** | **Distinct** from product cards |
| **Product detail** (e.g. lamp): white frame, pill category, price, one line, qty/cart | **Locked** direction (matches prior flags) |

### Claude priority order (8/9 — aligns with Standing Brief §13)

1. **Repair / stabilize** first (10Web damage, hub **stacking/duplicate blocks** — Technology Hub lesson).  
2. **Then** richer hover on tiles that **already have** bullet copy (Ergonomic Design, Premium Materials, etc.) — **no content rewrite**.  
3. **Defer** shop-archive page type until hubs stable.  
4. **Do not** apply new hover systems **mid-repair** (repeat of stacking/rework risk).

Daniel correction to Claude: **no rollback** — repair is **forward fix**, not restore-to-pre-10Web.

---

## SPEC for Cursor (locked from 8/9 Claude ticket — implement only when Daniel marks hub stable)

1. **Large category tiles (optional richer hover):** On hover: heading, one description line, 2–3 bullet feature points, solid button — **only where copy already exists**; separate from simpler **EXPLORE** hub treatment.  
2. **Shop-style archive:** Own template — sidebar filters (price, availability, tags), sort, product grid with affiliate CTA — **not** merged into category hubs.  
3. **Editorial/blog grid:** Navy full-bleed; thumbnails **desaturated at rest → full color on hover**; date + **Read Feature** button — separate from product cards.  
4. **Product detail:** Keep locked pattern — whitespace, white-on-white frame, category pill, price, **one** short description line, qty/CTA row — no long copy block.

Visual gold reference remains `docs/brand-references/vercel-and-10web-comparison.pdf` — **reference only**, implement via locked `tc-*` classes + Cursor/Daniel Additional CSS.

---

## For lawsuit pairing (Cursor relay + 10Web disregard)

Search Desktop Cursor history (Aug 2026) for threads where Cursor:

- Drafted **do not AI Builder / preserve tcstaging / preserve HTML** relays to 10Web.  
- Documented **damage inside WordPress** after migration “completed.”  
- Advised **repair forward** when backups unusable.

Search terms: `destroyed`, `tangled`, `backup`, `roll back`, `10web`, `two weeks`, `August 9`.

Claude 8/9 thread proves **Daniel reported destruction to another AI** contemporaneously; **Cursor exports** prove **directives** 10Web allegedly ignored.

---

## Session rule (2026-10-05)

Do **not** start richer hover or shop-archive work until Daniel confirms hub passes **structural** repair gate in `docs/TC-LAUNCH-ROADMAP.md` Phase A–C.
