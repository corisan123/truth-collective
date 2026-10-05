# 10Web migration and decommission

Living runbook for moving **off** 10Web hosting/tooling and, when staging is ready, **staging → live** on Hostinger. This is separate from the visual gold standard in `docs/brand-references/vercel-and-10web-comparison.pdf` (Vercel/10Web **samples** that informed `tc-explore-*` CSS).

**Authority:** `docs/TC-STANDING-BRIEF.md` §13 (fix staging before launch). **10WEB Manager:** do not deactivate or delete until Daniel explicitly asks (historical pause: ticket **#375660** for RCA/compensation only; 10Web is not on the critical path for recovery).

---

## Two tracks

| Track | Goal | When |
|-------|------|------|
| **A — Exit 10Web** | Hostinger is source of truth; remove 10Web Manager and residue | After Daniel approves plugin removal |
| **B — Staging → live** | Exact copy of approved staging on `truth-collective.com` | After §13 steps 1–3 (fix, polish, SEMrush) |

Track B is documented in **`docs/TC-STAGING-TO-LIVE-MIGRATION.md`** (mirror of Migration Brief). Phases H–J in **`docs/TC-LAUNCH-ROADMAP.md`**.

---

## Current state (read-only checks — 2026-10-05)

| Check | Staging (`tcstaging`) | Live (`truth-collective.com`) |
|-------|------------------------|-------------------------------|
| Homepage HTTP | 200 | (not re-checked this session) |
| `10web` / `tenweb` in public homepage HTML | None found | None found (2026-08-08 handoff) |
| `wp-content/plugins/10web-manager/` probe | **403** (directory likely present) | **404** (folder not exposed or absent) |
| `uploads/10web_tmp` | **Gone** (File Manager, 2026-08-08) | **Gone** after Jul 24 restore |
| 10WEB Manager plugin (admin) | **Active v1.20.21** (handoff 2026-08-08) | Confirm in wp-admin before removal |
| Cursor REST Application Password | **Not working** in cloud agent env (`TC_WP_USER` + injected secret: public reads OK; `users/me`, `plugins`, `context=edit` → 401) | Do not use on live until launch playbook |

**Action for Daniel:** Rotate staging Application Password (Standing Brief §14: email as username; name e.g. **Cursor Staging Recovery III**). Add to Cloud Agent environment secrets, then revoke old keys.

---

## Track A — 10Web decommission (preserve-only)

**Gate:** Daniel says in writing to proceed (including resolving or accepting ticket #375660). Staging is stable enough that plugin removal will not block recovery work.

### A1 — Pre-flight (Daniel + Hostinger)

1. hPanel full backup of **staging** (files + DB).
2. Export Additional CSS to plain text (Customizer → Additional CSS → copy to file in repo or Drive).
3. Note active 10Web-related plugins (minimum: **10WEB Manager**; check for speed/optimizer plugins).

### A2 — Deactivate and remove (Daniel in wp-admin)

1. **Plugins → 10WEB Manager → Deactivate.** Wait 24–48 hours; spot-check key URLs (one hub, one product page, membership toggle page 8176 if published).
2. **Delete** the plugin if no regressions.
3. **File Manager:** confirm no `wp-content/uploads/10web_tmp` and no orphaned `tenweb*` / `10web*` folders under `wp-content`.
4. Optional: WP-CLI or Better Search Replace **dry run** for options containing `tenweb` / `10web` (do not run live replace without Cursor/Daniel review).

### A3 — Post-removal verification

- No new console errors; no broken admin menus.
- Hover checks: `tc-explore-hub`, `tc-overlay-card`, `tc-book-card` on sample pages (10Web did not own this CSS; confirm no accidental dependency).
- LiteSpeed/cache: purge once after plugin removal.

### A4 — Live site

Repeat A1–A3 on **live** only if 10WEB Manager is still installed there. Read-only probe suggests live may already lack `10web-manager` directory; confirm in admin before changes.

---

## Track B — Staging → live (after recovery)

**Hard gate:** Standing Brief §13 — do **not** launch until staging fix, polish, and SEMrush gates in `docs/TC-LAUNCH-ROADMAP.md` are met.

Execution:

1. Phase **H** — freeze, backups, GSC URL export, 301 map draft.
2. Phase **I** — Method A clone, serialization-safe URL replace, preserve-only post-checks.
3. Phase **J** — sitemap, indexing, redirects.

Full step list: **`docs/TC-STAGING-TO-LIVE-MIGRATION.md`**.

---

## What helpers must not do

- Deactivate/delete **10WEB Manager** without Daniel’s explicit request.
- Use Website backup restore on staging for CSS/link symptoms (see handoff).
- “Improve” or refactor Additional CSS during Track B.
- Run Track B while hub links, flicker, or draft visibility issues from Phase A–G are still open.

---

## Related files

- **`docs/CURSOR-CHAT-PRESERVATION-10WEB-CRASH.md`** — how to find/save Before/During/After Cursor chats (July crash + ticket #375660)
- `diagnostics/cursor-chat-archive/` — redacted Cloud Agent transcripts; Desktop exports go under `desktop/`
- `STAGING-RECOVERY-HANDOFF.md` — crash recovery, `10web_tmp`, CSS layer history
- `docs/TC-LAUNCH-ROADMAP.md` — master phase order
- `docs/TC-STANDING-BRIEF.md` — §1 (10Web/Vercel visual reference), §6 (migration summary), §13–14
- `diagnostics/10web-migration-readonly-2026-10-05.md` — this session’s probe log
