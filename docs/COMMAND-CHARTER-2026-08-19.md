# COMMAND CHARTER — Daniel Reid Portfolio (Authority Sheet)

**Effective:** 2026-08-19  
**Authority:** Cursor (lead / quarterback) under Daniel Reid (owner / final taste)  
**Scope:** Truth Collective (staging → Semrush → launch) + ISI Consulting (finish → deploy) + growth content (followers / members)  
**Status:** This charter **supersedes stale parallel-AI instructions** in older docs where they conflict. Hard technical locks below still stand.  
**Daily board:** `docs/COMMAND-OS.md` (Current assignment). Cursor project rules: `.cursor/rules/*.mdc`.

---

## 0 — Leadership model (updated)

Daniel asked for an expert lead, not a timid rule-follower of every 6-month-old line.

| Role | Who | Power |
|------|-----|--------|
| Owner / taste / keys / money | **Daniel** | Approves launches, media, domain/email, spend |
| Quarterback / architecture / tickets / veto | **Cursor lead** (this command layer) | Assigns tickets, reviews drafts, unblocks auth/ops, does **not** steal Block A page families from the worker |
| Staging rebuild apply | **Cursor Cloud worker** (one agent) | Hub → children → sub-children REST apply on the assigned branch |
| Specialist draft factories | **Claude, social AI** | One ticket each; no site apply |

**Why a second Cursor agent exists:** so the lead can run platforms (Claude tickets, governance, growth, ISI prose) while the worker owns Block A page rebuilds. Lead may clear a hard blocker (auth, one stuck family) then returns the lane.

**Parallel is allowed only across different work blocks.**  
Never two AIs on the same page family, same CSS file, or same PR at once.

**Cursor does not remote-control other AIs through APIs.** Cursor writes tickets. Daniel pastes them. Specialists return drafts. Lead integrates. Worker applies staging pages.

---

## 1 — What stays (still correct)

Keep these even if other rules get trimmed:

1. **Staging only** for Truth Collective until Daniel says live.  
2. **No Hostinger Website backup restore** for staging recovery. No restore roulette.  
3. **Locked `tc-*` classes** — do not rename/merge/delete.  
4. **Vercel / 10Web PDF** = visual gold standard (reference), already in repo: `docs/brand-references/vercel-and-10web-comparison.pdf`. No re-download required unless Daniel wants fresher screenshots.  
5. **TC voice on TC pages:** no em dashes, no contractions, no bold body, no hype.  
6. **Affiliate-only product mentions** on TC (Amazon paused; links retained for relaunch).  
7. **Image sizes:** heroes/tiles **1600×1000**; product cards **1200×750**; placeholders must show dimensions.  
8. **Additional CSS:** Cursor + Daniel only. Never paste Claude/ChatGPT/Copilot CSS into the site.  
9. **10WEB manager:** leave alone until Daniel asks.  
10. **WP REST** via `TC_WP_USER` + `TC_WP_APP_PASSWORD` (Environment secrets).

---

## 2 — What to retire or rewrite (stale)

| Old rule / habit | Decision | Why |
|------------------|----------|-----|
| “Copilot Task blocked / Plan B forever” | **Retire as blocker narrative** | Cursor already owns scaffolds. Stop waiting on Tasks Pro. |
| “Copilot Edge / Premium HOLD as Task substitute” | **Keep HOLD for site HTML/CSS** | Still true for site damage risk. Edge may do **non-site** research later if Cursor assigns. |
| “One short step only / health-limited always” | **Soften** | Default to thorough batches; slow down only when Daniel says energy is limited. |
| “Never estimate / never parallel” | **Update** | Parallel **across blocks** is now encouraged. Same-block parallel still banned. |
| “Angie paused forever” | **Optional later** | Use only for Hostinger clicks Cursor cannot do; Cursor writes one-task prompts. |
| “Evaluation engine / binder urgency” | **Unpark as Claude DOC lane** | Worker keeps Block A pages. Lead assigns Claude: `diagnostics/CLAUDE-TICKET-governance-and-evaluations-2026-08-19.md`. Site UI later. |
| Overgrown STAGING PATCH archaeology as daily work | **Park** | Prefer page delete-first light rebuilds over endless CSS forensics. |
| ChatGPT / Operator on CSS/HTML | **Keep banned** | Historical damage. |

Standing Brief remains the brand/visual law for TC. This charter is the **operating command** for multi-AI execution. If they conflict on *process*, this charter wins until Daniel rejects it. If they conflict on *locked classes / staging / voice*, Standing Brief wins.

---

## 3 — Work blocks (the real board)

### Block A — Truth Collective (site finish → Semrush)
**Owner:** Cursor Cloud Agent (one active rebuild agent)  
**Quarterback:** Cursor (this command layer)  
**Goal:** Hub → children → sub-children light rebuilds; placeholders sized; H1 clean; 404s fixed; Semrush crawl-ready.

Order:
1. Hub homes (fix dual H1 / broken explore links)
2. Smart Lighting children
3. Office children
4. Books children
5. Self-Help + Productivity children
6. Home / About / Contact cleanup
7. Daniel image Replace pass
8. Semrush audit

### Block B — ISI Consulting (site finish → deploy)
**Owner:** Cursor (static site in `isi-consulting/`)  
**Claude:** whitepaper prose + polish of long About if needed  
**Daniel:** Formspree ID, `daniel@isiconsults.com` → Yahoo forward, DNS cutover from Squarespace  
**Goal:** Multi-page site live on isiconsults.com with signup + contact working.

### Block C — Growth content (followers + members)
**Owner:** Claude (primary copy) + optional social AI (format variants)  
**Cursor:** membership/signup UX on TC only when structure allows; no fake follower tactics  
**Daniel:** approve brand claims; post/schedule  
**Goal:** Authority content calendar + member invite path — not spam growth hacks.

### Block D — Ops / keys / hosting
**Owner:** Daniel  
Email forwards, App Passwords, Cursor secrets, media uploads, domain DNS.

---

## 4 — Platform lanes (command assignments)

| Platform | Status | Assigned blocks | Output format | Forbidden |
|----------|--------|-----------------|---------------|-----------|
| **Cursor (lead)** | ACTIVE COMMAND | Tickets, veto, auth/ops unblock, B architecture, C assign; Block A only if worker blocked | Tickets, reviews, rare blocker apply | Competing with worker on the same page family; CSS from other AIs |
| **Cursor Cloud Agent (worker)** | ACTIVE (one only on Block A) | A page families from `diagnostics/WORKER-HANDOFF-*.md` | Commits/PRs on staging branch | Governance binder; social calendar; starting Block C without ticket; restore roulette |
| **Claude** | ACTIVE SPECIALIST | B whitepaper; C social from built pages; G1 governance/evaluations; A long-form intros only when lead asks | Clean text only | HTML/CSS/WP paste; inventing product grades |
| **Social AI** (Buffer/ChatGPT social/etc.) | OPTIONAL | C only: thread variants, hashtag sets, short clips scripts from Claude masters | Captions / threads | TC or ISI site code; medical/financial hype |
| **Copilot Task** | IDLE | None unless Daniel buys Pro and Cursor issues a DOC ticket | Docs only | Site CSS/HTML lead |
| **Copilot Edge / Premium** | HOLD for site | None on A/B | — | Staging WP / Additional CSS |
| **ChatGPT Operator / “do the website” modes** | BANNED for site | None | — | Any TC/ISI markup |
| **Angie** | STANDBY | D clicks only via Cursor one-task prompt | Screenshots / confirm | Freestyle admin edits |
| **10Web** | OUT | Visual reference only | — | Manager edits on critical path |

---

## 5 — Parallel schedule (efficient, safe)

**Same week, different lanes:**

| Lane | Who | This week’s ticket |
|------|-----|-------------------|
| A1 | Cursor **worker** | Office children → Books → Self-Help/Productivity (`diagnostics/WORKER-HANDOFF-2026-08-19.md`). Lighting already applied. |
| A0 | Cursor **lead** | Write tickets; do not take next Office family unless worker is 401-blocked |
| B2 | Claude | ISI whitepaper (`diagnostics/CLAUDE-TICKET-isi-whitepaper-2026-08-19.md`) |
| C1 | Claude | Social from built pages (`diagnostics/CLAUDE-TICKET-tc-social-from-built-pages-2026-08-19.md`) |
| G1 | Claude | Governance + evaluation engine outline (`diagnostics/CLAUDE-TICKET-governance-and-evaluations-2026-08-19.md`) |
| D1 | Daniel | Paste Claude tickets; confirm worker REST 200; email forward `daniel@isiconsults.com` |

**Never parallel:** two agents editing the same hub family at once.

---

## 6 — Immediate command tickets (paste as written)

### Ticket W1 — Cursor worker agent (site)
Paste from: `diagnostics/WORKER-HANDOFF-2026-08-19.md` (bottom prompt).  
Next family: **Office children only**. Skip Smart Lighting.  
Parallel: Worker B may run ISI (`diagnostics/WORKER-B-ISI-HANDOFF-2026-08-19.md`) at the same time.  
Full swarm paste list: `docs/SWARM-LAUNCH-PACK.md`.

### Ticket C1 — Claude (ISI whitepaper)
`diagnostics/CLAUDE-TICKET-isi-whitepaper-2026-08-19.md`

### Ticket C2 — Claude (growth / social from built pages)
`diagnostics/CLAUDE-TICKET-tc-social-from-built-pages-2026-08-19.md`

### Ticket G1 — Claude (governance + engineering evaluations)
`diagnostics/CLAUDE-TICKET-governance-and-evaluations-2026-08-19.md`

---

## 7 — Success definition

**Done enough for Semrush submit (TC staging):**  
Clean H1s on hubs/children rebuilt; no known critical 404s on hub paths; placeholders labeled or real images in; voice rules held.

**Done enough for ISI public:**  
Multi-page site deployed; `daniel@isiconsults.com` forwards to Yahoo; contact/signup live; whitepaper filled by Claude then applied by Cursor.

**Growth:**  
Calendar approved by Daniel; first week of posts scheduled by Daniel (or tool of his choice).

---

## 8 — Daniel confirmation

Reply **Approve Command Charter** to lock this as operating authority.  
Reply **Amend: …** to change lanes.  
Until then, Cursor operates under this draft as the working command model.
