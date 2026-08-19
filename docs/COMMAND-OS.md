# COMMAND OS — Living board (Truth Collective + ISI)

**Authority:** Daniel Reid (owner) · Cursor lead (quarterback) · Cursor worker (Block A apply)  
**Parent law:** `docs/COMMAND-CHARTER-2026-08-19.md` + `docs/TC-STANDING-BRIEF.md`  
**Cursor enforcement:** `.cursor/rules/*.mdc` (alwaysApply) — these are the written “page rules.”

This file is the **big-picture board**. Agents must update the **Current assignment** section when a family ships or a ticket moves. Do not invent parallel plans in chat.

---

## 1 — Why this exists (anti-drift)

Daniel spent real time on Environment secrets, App Passwords, and a **dedicated worker agent**. That investment is wasted if:

- Lead does the worker’s page family
- Worker idles on auth while lead freelances
- Rules live only in chat memory
- Tickets are ad-hoc one-liners with no board

**Rule:** Process is product. Prefer written OS + rules over clever improvisation.

---

## 2 — Roles (locked)

| Role | Agent | Does | Does not |
|------|-------|------|----------|
| Owner | Daniel | Approve, keys, media, paste tickets to Claude, post social | Expect lead to “just do everything” without board updates |
| Lead | Cursor command chat / lead agent | Tickets, veto, unblock auth/ops, architecture, Claude/governance/growth lanes | Steal Block A page families when a worker is assigned |
| Worker | One Cursor Cloud agent on Block A branch | Hub → children REST apply per handoff | Governance binder, social calendar, ISI prose, inventing new lanes |
| Specialist | Claude | Copy, calendars, evaluation/governance docs | HTML, CSS, WP, secrets |

**Secrets / new-agent rule:** If Daniel creates or refreshes `TC_WP_*` secrets for a worker, the **next Block A family belongs to that worker**. Lead may diagnose auth once, then returns the lane.

---

## 3 — Current assignment (UPDATE EVERY SHIP)

**Date:** 2026-08-19

| Lane | Owner | Status | Ticket / handoff |
|------|-------|--------|------------------|
| A — Staging pages | **Worker** | NEXT: Office children | `diagnostics/WORKER-HANDOFF-2026-08-19.md` |
| A — Lighting children | Done (staging) | Do not redo | `diagnostics/REST-smart-lighting-children-apply-2026-08-19.md` |
| A — Tech children | Done (staging) | Do not redo | prior REST ticket |
| Auth | Shared | Working when USER = email | `diagnostics/REST-AUTH-GATE-2026-08-19.md` |
| B — ISI whitepaper | Claude | Paste ready | `diagnostics/CLAUDE-TICKET-isi-whitepaper-2026-08-19.md` |
| C — Social from built pages | Claude | Paste ready | `diagnostics/CLAUDE-TICKET-tc-social-from-built-pages-2026-08-19.md` |
| G — Governance / evaluations | Claude | Paste ready | `diagnostics/CLAUDE-TICKET-governance-and-evaluations-2026-08-19.md` |
| D — Email forward / Formspree | Daniel | Pending | ISI docs |

**Block A order (do not reorder without board edit):**  
Office children → Books children → Self-Help / Productivity children → Home / About / Contact → Daniel image Replace → Semrush.

---

## 4 — Session open checklist (every Cursor agent)

1. Read Standing Brief + Staging Handoff + this COMMAND OS + Command Charter.  
2. Identify role: **lead** or **worker** (from prompt / branch / handoff).  
3. Read **Current assignment** above. Do that, not a new idea.  
4. REST: prove `users/me` 200 with `TC_WP_USER` email before any page write.  
5. If blocked: write a short diagnostics note + stop. Do not invent a second plan.  
6. After ship: update section 3, commit, push.

---

## 5 — Written rule files (the “page rules”)

| File | Purpose |
|------|---------|
| `.cursor/rules/truth-collective.mdc` | Hard site locks (staging, classes, voice, CSS) |
| `.cursor/rules/lead-worker-no-drift.mdc` | Lead vs worker; secrets investment; no lane theft |
| `.cursor/rules/command-os.mdc` | Must follow living board; update Current assignment |
| `.cursor/rules/rest-and-secrets.mdc` | Auth probe, backup-before-write, no secrets in git |
| `docs/COMMAND-CHARTER-2026-08-19.md` | Full multi-AI authority sheet |
| `docs/COMMAND-OS.md` | This board |
| `docs/AI-PLATFORM-RULES-AND-PROMPTS.md` | Paste prompts; defer role split to Charter + OS |

If chat contradicts a rule file or this board, **rule file / board wins**.

---

## 6 — Definition of locked-in (quality bar)

Lead is “best” when:

- Worker has a clear next family and does it
- Claude has paste-ready tickets for parallel non-site work
- Board section 3 matches reality after every ship
- No two agents on the same page family
- No ad-hoc “while I’m here” redesigns outside the order

Lead is failing when:

- Doing Office/Books while a worker was spun up for that
- Writing more chat than rules
- Parking governance forever while claiming to lead platforms
