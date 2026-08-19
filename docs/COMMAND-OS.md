# COMMAND OS — Living board (Truth Collective + ISI)

**Authority:** Daniel Reid (owner) · Cursor lead (quarterback) · specialized workers/helpers  
**Parent law:** `docs/COMMAND-CHARTER-2026-08-19.md` + `docs/TC-STANDING-BRIEF.md`  
**Paste dashboard:** `docs/MARSHAL-STEP-1.md` then `docs/SWARM-LAUNCH-PACK.md`  
**Lead primary job:** marshall specialists (growth, Pinterest, social, governance, ISI). Page apply only in the env with REST 200 — never the stuck 401 loop.

**Staging reality (locked):** Work is on `tcstaging` only. Staging is **not** the live site. Do **not** treat views as LiteSpeed-cached or Cloudflare-cached. No purge-CDN steps unless Daniel opens a live-launch ticket. See `.cursor/rules/staging-not-live-not-cdn.mdc`.


---

## 1 — Anti-drift

Secrets + new agents are investments. Lead does not steal Block A. Rules live in `.cursor/rules/`, not chat memory. Board section 3 is truth.

---

## 2 — Roles (locked)

| Role | Who | Does | Does not |
|------|-----|------|----------|
| Owner | Daniel | Approves, keys, media, pastes many tickets at once | Wait for one AI to finish all work |
| Lead | Cursor command (fresh OK) | Tee swarm, update board, veto, unblock | Steal Worker A page families |
| Worker A | One Cloud agent | TC Block A pages | ISI, Claude, social, governance |
| Worker B | Second Cloud agent (optional) | ISI Block B only | TC REST pages |
| Claude | Multiple chats OK | One topic per chat | HTML/CSS/WP |
| Social AI | After Claude masters | Captions/threads | Site code |
| Edge/research | Docs only | Semrush/research checklists | Theme/CSS |
| Angie | One-task prompts | Hostinger clicks | Freestyle site edits |
| Copilot Task | IDLE until Pro | DOC skeletons later | Site HTML lead |

---

## 3 — Current assignment — SWARM (2026-08-19)

### Running / READY (start in parallel)

| ID | Lane | Owner | Status | Ticket |
|----|------|-------|--------|--------|
| M0 | **Marshall Step 1** (Daniel pastes) | Daniel + Lead | **DO THIS** | `docs/MARSHAL-STEP-1.md` |
| C1 | TC social calendar | Claude | READY | `diagnostics/CLAUDE-TICKET-tc-social-from-built-pages-2026-08-19.md` |
| C5 | Pinterest boards + pins | Claude | READY | `diagnostics/CLAUDE-TICKET-pinterest-boards-pins-2026-08-19.md` |
| C6 | 8 accounts resume plan | Claude | READY | `diagnostics/CLAUDE-TICKET-eight-accounts-resume-plan-2026-08-19.md` |
| C2 | Membership email sequence | Claude | READY | `diagnostics/CLAUDE-TICKET-membership-email-sequence-2026-08-19.md` |
| C4 | Social platform variants | Social AI | Wait C1 | `diagnostics/SOCIAL-AI-TICKET-format-variants-2026-08-19.md` |
| C7 | Canva pin/social templates | Canva | Wait C5 | `diagnostics/CANVA-TICKET-pin-social-templates-2026-08-19.md` |
| G1 | Governance + evaluations | Claude | READY | `diagnostics/CLAUDE-TICKET-governance-and-evaluations-2026-08-19.md` |
| G2 | Public Selection Standards | Claude | READY | `diagnostics/CLAUDE-TICKET-selection-standards-public-summary-2026-08-19.md` |
| B2 | ISI whitepaper | Claude | READY | `diagnostics/CLAUDE-TICKET-isi-whitepaper-2026-08-19.md` |
| B1 | ISI deploy / Formspree map | Worker B | READY | `diagnostics/WORKER-B-ISI-HANDOFF-2026-08-19.md` |
| R1 | Semrush staging checklist | Edge | READY | `diagnostics/EDGE-TICKET-semrush-staging-setup-2026-08-19.md` |
| D1 | ISI email forward | Angie | READY | `diagnostics/angie-prompts/ANGIE-ISI-EMAIL-FORWARD-2026-08-19.md` |
| D2 | Ops / media / Approves | Daniel | READY | `diagnostics/DANIEL-OPS-CHECKLIST-2026-08-19.md` |
| A1 | Self-Help / Productivity → Home cleanup | Lead (REST 200 env) | Background | COMMAND OS Block A order |

### After dependency

| ID | Lane | Owner | Wait for | Ticket |
|----|------|-------|----------|--------|
| C4 | Social platform variants | Social AI | C1 Claude return | `diagnostics/SOCIAL-AI-TICKET-format-variants-2026-08-19.md` |
| T1 | Operator binder skeleton | Copilot Task | Tasks Pro + G1 | `diagnostics/TASK-TICKET-operator-binder-skeleton-WHEN-PRO.md` |

### Done (do not redo)

| Lane | Note |
|------|------|
| Tech children | Staging applied |
| Smart Lighting children | Staging applied |
| Office children (6) | Staging applied 2026-08-19 — `REST-office-children-apply-2026-08-19.md` |
| Books children under hub 38 (7) | Staging applied 2026-08-19 — `REST-books-children-apply-2026-08-19.md` |
| Dual H1 on Prod / Ones / AI Podcast | `site-post-title=disabled` |

### Stuck agent

GPT worker reporting endless 401: **stop it**. Secrets work in this lead env. See `diagnostics/BREAK-AUTH-LOOP-2026-08-19.md`.

### Block A order

~~Office~~ → ~~Books (hub 38)~~ → Self-Help / Productivity children → Home / About / Contact → Daniel image Replace → Semrush crawl.


---

## 4 — Session open (every agent)

1. Role? Lead / Worker A / Worker B / other.  
2. Read this board §3 + matching handoff/ticket.  
3. REST only if Worker A (email user).  
4. Ship → update §3 → commit.  
5. If blocked, short diagnostics note; do not invent a new lane.

---

## 5 — Rule + skill index

| Path | Purpose |
|------|---------|
| `.cursor/rules/truth-collective.mdc` | Site locks |
| `.cursor/rules/lead-worker-no-drift.mdc` | No lane theft |
| `.cursor/rules/command-os.mdc` | Obey board |
| `.cursor/rules/rest-and-secrets.mdc` | Auth hygiene |
| `.cursor/rules/parallel-by-default.mdc` | Many hands |
| `.cursor/skills/cursor-lead/` | Lead skill |
| `.cursor/skills/cursor-block-a-worker/` | Worker A skill |
| `.cursor/skills/claude-specialist/` | Claude lane skill |
| `docs/CURSOR-RULES-INDEX.md` | Human index |
| `docs/SWARM-LAUNCH-PACK.md` | Paste dashboard |

---

## 6 — Quality bar (boss standard)

**Winning:** many READY tickets; Worker A and B both busy; Claude chats A–F pasteable; Daniel checklist in motion; board matches reality.  
**Failing:** one-at-a-time; lead doing Office; empty specialist lanes; rules only in chat.
