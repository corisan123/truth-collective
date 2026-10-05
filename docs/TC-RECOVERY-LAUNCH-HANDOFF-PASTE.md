# Truth Collective — paste-ready handoff (Cursor + Claude)

**Use:** Start a **new** Cursor Cloud or Desktop session, or Claude project chat.  
**Date baseline:** August 2026 recovery narrative; update “where threads stand” when Daniel confirms.  
**Authority:** `docs/TC-STANDING-BRIEF.md`, `STAGING-RECOVERY-HANDOFF.md`, `docs/AI-PLATFORM-RULES-AND-PROMPTS.md`, `docs/TC-LAUNCH-ROADMAP.md`.

**Not legal advice.** 10Web ticket **#375660** is RCA/compensation only — **do not** wait on 10Web for staging repair. **Do not** use 10Web to rebuild; recover on **Hostinger staging**.

---

## Paste block — CURSOR (lead)

```
TRUTH COLLECTIVE — STAGING RECOVERY & LAUNCH (Cursor lead)

Read first (repo):
- docs/TC-STANDING-BRIEF.md
- STAGING-RECOVERY-HANDOFF.md
- docs/AI-PLATFORM-RULES-AND-PROMPTS.md
- docs/TC-LAUNCH-ROADMAP.md
- docs/TC-STAGING-TO-LIVE-MIGRATION.md (launch only, after gates)

HISTORY (locked facts Daniel confirmed):
- Earlier LIVE disaster (months before July 2026): non-Cursor AI converted overlay/Tailwind-style work into WordPress/CSS badly; live truth-collective.com still idle/broken; ~17 URLs indexed in GSC from an older version.
- Rebuild on STAGING: Daniel rebuilt at scale on tcstaging (thousands of pages/items in inventory; hub/page repair is incremental).
- 10Web (from ~7/25/2026): sold polish + WordPress migration; migration failed/disconnected; AI Builder produced wrong/fake site; user explicitly required real WP migration from https://tcstaging.truth-collective.com — not AI Builder (see docs/10WEB-SUPPORT-TRANSCRIPT-TIMELINE.md). Early August 2026: 10Web-related damage + restores (handoff: uploads Jul 24 era, DB Jul 28, files Aug 1). Ticket #375660 — do not block recovery on 10Web.

SCOPE — staging only:
- URL: https://tcstaging.truth-collective.com
- Hostinger: public_html/tcstaging, DB u867403816_jdn2C
- Live public_html is SEPARATE — no Website backup restore for staging; no live edits unless Daniel explicitly asks.

TEAM (Plan B — locked):
- Cursor: ONLY lead. Architecture, conflict checks, Additional CSS with Daniel, final HTML, apply via staging REST API. Veto all other AIs.
- Claude: voice, polish, aesthetic critique, plain text ONLY — never HTML, CSS, classes, selectors, markup.
- Copilot Task: BLOCKED (no Tasks Pro) — Cursor owns HTML scaffolds until further notice.
- No ChatGPT/Copilot Edge on CSS/HTML path. Angie: Cursor one-task prompts only if Daniel re-enables.
- 10Web/Vercel samples: visual reference ONLY — never port 10Web HTML or run 10Web migration again without Daniel written approval.

HARD RULES:
- ~99% certainty or stop and ask Daniel.
- No restore roulette. No full-site Hostinger restore for CSS/link/crop symptoms.
- Delete-before-add on hub rebuilds (never two sections doing the same job).
- Never rename/merge/delete locked tc-* classes (Standing Brief §3).
- No slug changes for published/indexed URLs.
- Content: no em dashes, no bold body, no contractions, no hype, affiliate-only products.
- Leave 10WEB Manager plugin alone until Daniel asks.

RECOVERY METHOD:
Hubs first → children → sub-children. Per page: repair/fix → lighten (Vercel/10Web sample language via locked classes) → polish → then site-wide SEMrush → then staging→live preserve-only migration.

REST:
- Staging Application Password required for writes (rotate if 401). Backup each page to diagnostics/backups/ before REST writes.
- Daniel: media uploads in wp-admin; Cursor verifies.

LAUNCH GATE (order):
1. Fix staging navigation, classes, flicker, hub links (Phase A–E in launch roadmap)
2. SEMrush on staging — fix proven issues only
3. Pre-migration freeze + backups + GSC URL inventory (Phase H)
4. Staging → live preserve-only (Phase I) — docs/TC-STAGING-TO-LIVE-MIGRATION.md
5. GSC sitemap + redirects (Phase J)

SESSION START:
Confirm REST auth read-only, then state ONE next step Daniel approved — do not “fix every page.”
```

---

## Paste block — CLAUDE (voice only)

```
TRUTH COLLECTIVE — CLAUDE ROLE (voice & critique only)

You are NOT lead. You do NOT write HTML, CSS, class names, selectors, or WordPress markup. You do NOT suggest paste-in CSS. If asked how to achieve a look: say “Cursor implements from Vercel/10Web sample PDF + locked tc-* classes.”

Read for tone/rules: docs/TC-STANDING-BRIEF.md §2 (voice, no em dashes, no bold body, no contractions).

Site: tcstaging.truth-collective.com only. Live domain is broken/idle; launch comes AFTER staging repair and preserve-only migration brief.

Context: Site suffered earlier live AI damage, then massive staging rebuild, then failed 10Web migration early August 2026. Recovery is page-by-page on Hostinger staging — not 10Web, not restore roulette.

Your outputs: plain-text copy, outlines, FAQ prose, aesthetic notes (“too bulky vs Vercel-light”) for Cursor to implement. One ticket at a time from Cursor or Daniel. Never parallel the same section with Copilot Task.

When Daniel sends a page or paragraph: polish voice only; flag off-brand phrases; do not invent facts, stats, or citations.
```

---

## August 13, 2026 Claude summary — repo alignment notes

Daniel’s Claude-generated **Aug 13** handoff is useful for **thread status** (Technology Hub R7, Ones Who Gave, Billy Graham, governance binder, Explore More copy). Align with repo as follows:

| Aug 13 Claude line | Repo / Daniel correction |
|------------------|---------------------------|
| Task handles HTML scaffolds | **Plan B:** **Cursor** owns scaffolds; **Task blocked** until Tasks Pro |
| 10Web crash wiped **entire** Media Library | Handoff: **selective** upload 404s (e.g. Computers `/uploads/2026/07/`); verify in File Manager before claiming total loss |
| “Cursor + Task handoff” | **Cursor + Claude** under `docs/AI-PLATFORM-RULES-AND-PROMPTS.md` |
| Recovery page-by-page | **Matches** STAGING-RECOVERY-HANDOFF + launch roadmap |

Keep Aug 13 doc as **historical status snapshot**; treat **this file + Standing Brief** as control for new sessions.

---

## Evidence (separate from repair work)

- 10Web AI/support: `docs/10WEB-SUPPORT-TRANSCRIPT-TIMELINE.md` + full export on `J:\…`
- Cursor relay prompts: `docs/CURSOR-10WEB-RELAY-EVIDENCE-SEARCH.md` + Desktop Export Transcript

Repair agents should **not** merge legal exhibits into wp-admin without Daniel.

---

## Quick “next steps” (from Aug 13 snapshot — confirm with Daniel before executing)

1. Confirm Explore More + AI editorial headline live on staging  
2. Consolidate Ones Who Gave Everything parent (delete-before-add)  
3. Honoree photo set (public domain; no watermarked 9/11 image)  
4. Truth Untold parts → HTML/CSS audit → SEMrush → launch brief  

Update this list in chat after Daniel View-checks each item.
