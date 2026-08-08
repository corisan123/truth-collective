# Plan B — Tasks Pro unavailable (structured workflows)

**Status:** ACTIVE as of 2026-08-08  
**Trigger:** Microsoft **Tasks Pro is not available for purchase** — Task limits cannot be increased yet.  
**Goal:** Keep recovery moving at top quality **without waiting** on Task billing, and **without** switching to Copilot Premium / Edge as a fake substitute.

**Authority:** Implements Standing Brief §10 / §13 / §14. Cursor remains lead.

---

## What we refuse

| Temptation | Why no |
|------------|--------|
| Wait idle until Tasks Pro returns | Staging stays broken; live stays idle |
| Buy **Copilot Premium** to “replace Task” | Wrong engine; pulls toward Edge-style damage path |
| Make Claude or Edge the lead / applicator | Violates locked roles; CSS risk |
| Have Claude invent full HTML/CSS systems | Cursor owns structure + Additional CSS |
| Burn free Task quota on full-site reviews | Low value; Task does not know the site |

---

## Plan B role map (until Tasks Pro is buyable)

| Work | Plan A (Tasks Pro) | **Plan B (now)** |
|------|--------------------|------------------|
| Lead + REST + CSS + veto | Cursor | **Cursor** (unchanged) |
| Voice / long copy / critique | Claude | **Claude** (unchanged; use now) |
| HTML scaffolds / card grids | Copilot Task | **Cursor** (primary) — extract gold from staging, clone/harden |
| Structured section outlines (not CSS) | Task optional | **Claude** — labeled plain-text blocks / wireframe notes only |
| Engineering / binder long docs | Task | **Defer**, or **one scarce free-Task DOC** only if Daniel still has Task runs; else Cursor outlines + Claude prose |
| Patterns (23) link repair | Task assist | **Cursor REST batch** later |
| Edge | Hold | **Hold** |

**Hard truth:** You wanted the **Task engine**, not Premium. Plan B is **Cursor + Claude (+ REST)**. Free Task is optional garnish only when a run remains.

---

## Structured workflow (hub factory)

Do **not** perfect-polish one page to the end of the site before touching others.  
Do **layers per hub**, then next hub.

### Workflow W1 — Hub Stabilize (Cursor + Daniel)

**Ticket prefix:** `REST-hub-{slug}-S`  
**One hub at a time.**

1. Cursor inventories via REST: links, `tc-*` classes, image 404s, ghost blocks.  
2. Cursor proposes a short fix list (Approve per write or small batch).  
3. Apply: links → classes → delete/replace ghosts → note media for Daniel.  
4. Daniel View-checks the hub URL.  
5. Mark hub **S-DONE**. No Claude/Task required.

**Exit:** Hub navigates; cards not visually destroyed beyond known CSS issues.

### Workflow W2 — Gold Template (Cursor)

**Ticket prefix:** `TMPL-hub-{slug}`  

1. Cursor picks the healthiest card/section in that hub.  
2. Saves gold HTML fragment under `diagnostics/templates/`.  
3. Lists locked classes used + href rules.  
4. This is what Task *would* have copied — Cursor uses it to clone.

**Exit:** One approved template file for the hub family.

### Workflow W3 — Voice + lighten (Claude)

**Ticket prefix:** `COPY-hub-{slug}` or `CRITIQUE-hub-{slug}`  
Claude is standing by — **use under Plan B.**

1. Cursor sends Claude: current prose + hub URL notes + length limits.  
2. Claude returns voice-clean copy **or** aesthetic notes (Vercel-light, less bulky).  
3. **No CSS. No full-page HTML for paste.**  
4. Optional: Claude may return a **plain-text section outline** (headings + bullet structure) labeled for Cursor to wrap — not markup systems.

**Exit:** Copy/notes marked APPROVED by Cursor/Daniel.

### Workflow W4 — Apply polish HTML (Cursor)

**Ticket prefix:** `REST-hub-{slug}-R`  

1. Cursor wraps approved Claude copy in gold-template HTML.  
2. Conflict check against STAGING PATCH 02A / Explore+Overlay rules.  
3. REST apply one section or small set.  
4. Daniel View.

**Exit:** Hub family matches template language.

### Workflow W5 — Next hub

Repeat W1→W4. After 2–3 hubs share the same language, schedule named CSS flicker work (`CSS-flicker-01`) — still Cursor + Daniel only.

### Workflow W6 — Patterns batch (later)

**Ticket prefix:** `REST-patterns-*`  
See `diagnostics/patterns-inventory-2026-08-08.md`. Cursor REST; Claude only for prose patterns; no Task required.

### Workflow W7 — Binder / eng docs (paused or scarce)

If free Task has a run left: **one** `DOC-*` ticket only (Cursor-scoped).  
If not: leave binder on Option 1 pause; Claude can draft CTA copy later; Cursor ports.

---

## If a free Task run still exists (scarce)

Spend it on **high-leverage DOC**, not sitewide HTML:
1. Prefer: one engineering/governance doc Daniel already needs.  
2. Or: one HTML scaffold **only after** Cursor attaches gold template + class list.  
3. Never: “review the whole site,” orchestrator mode, Additional CSS, Premium upsell path.

Paste the Task standing brief from the prior Cursor message (A + limited B, Cursor lead). Then one ticket only.

---

## Parallel day rhythm (Plan B)

| Block | Claude | Cursor | Daniel |
|-------|--------|--------|--------|
| 1 | `COPY` or `CRITIQUE` for hub A | `REST` stabilize hub A or apply hub B | View / Approve |
| 2 | Outline notes for next section (text only) | Build/clone from gold template | Media 404s if any |
| 3 | Idle | Diagnostics + next ticket | Rest |

Task column = empty unless a scarce free run is intentionally burned on one DOC/HTML ticket.

---

## When Tasks Pro becomes buyable (Plan A resume)

Do **not** restructure again. Swap Task back in:

| Lane | Returns to |
|------|------------|
| HTML scaffolds | Task (under Cursor tickets + gold template) |
| Eng/binder docs | Task |
| Voice/critique | Claude |
| Apply/CSS | Cursor |

Update status in this file from ACTIVE → STANDBY and say so in Standing Brief.

---

## Immediate next step (recommended)

1. **Do not wait** on Tasks Pro.  
2. Keep Edge / Premium off the path.  
3. Start **W1 on the first hub** Daniel picks (homepage already link-good — pick the next most important damaged hub, e.g. Technology or Office — not Computers first unless he wants the hard one).  
4. Claude: keep standing by for W3 tickets only.  
5. Task: align with standing brief if useful, then **idle** until either a scarce free run has a single ticket or Tasks Pro returns.

---

## One-line summary

**Plan B = Cursor REST factory + Claude voice, hub layers, gold templates. Task optional when Pro exists again. Never Premium/Edge as Task substitute.**
