# AUTONOMOUS FLEET — hands-off strategy (set this up first)

**Goal:** Daniel is **not** the paste portal for every paragraph.  
**Runtime that can actually run unattended:** Cursor Cloud Agents (repo + Environment secrets).  
**Not unattended without APIs/keys:** Claude chat, Canva UI, Pinterest UI, Buffer — those become **publish later**, after the fleet writes drafts into the repo.

---

## 1 — How this works

```
Lead (or you, once) seeds diagnostics/agent-queue/READY/
        │
        ├─ Cloud Agent A  (pages)     ──claims ticket──► staging REST + commit
        ├─ Cloud Agent B  (growth)    ──claims ticket──► drafts in diagnostics/outputs/
        ├─ Cloud Agent C  (ISI)       ──claims ticket──► isi-consulting/ + checklists
        └─ Cloud Agent D  (docs)      ──claims ticket──► governance / Semrush checklists
```

Each agent:
1. Reads `docs/AUTONOMOUS-FLEET.md` + its starter prompt
2. Claims **one** READY ticket (move to CLAIMED/)
3. Executes end-to-end
4. Writes outputs + moves ticket to DONE/
5. Commits and pushes
6. Claims the next READY ticket in its lane (or stops if none)

**You do not paste ticket bodies into Claude.** Agents read tickets from git.

---

## 2 — One-time Daniel setup (do this before more paste work)

1. In Cursor: open **Cloud Agents → Environment** named for this repo (e.g. `truth-collective`).
2. Confirm secrets exist: `TC_WP_USER` = `dreid1253@yahoo.com`, `TC_WP_APP_PASSWORD` = valid Application Password.
3. **Every new agent must select that Environment** when launched (this is why the 401 worker failed).
4. Launch **3 agents** using the fixed prompts in `diagnostics/fleet/STARTERS/` (copy prompt only — not six Claude chats):
   - `01-pages-block-a.md`
   - `02-growth-content.md`
   - `03-isi-block-b.md`
5. Optional 4th: `04-docs-governance-semrush.md`
6. Stop any old agent stuck in 401 loops.
7. Check back later on branch commits / PRs. Approve publishes (Pinterest/social) in a batch when drafts exist under `diagnostics/outputs/`.

That is the whole “portal” for Day 1. Not paragraph ferrying.

---

## 3 — What stays human (unavoidable for now)

| You still do | Why |
|--------------|-----|
| Launch agents with Environment selected | Cursor UI; lead cannot spawn your agents from here with your secrets |
| Media Replace in WP | Your files / taste |
| Post/schedule to Pinterest, LinkedIn, X | No TC API keys in repo for those platforms yet |
| Formspree ID, email forward, DNS | Hostinger / accounts |
| Final Approve on public claims | Brand owner |

| Fleet does without you mid-stream | Output |
|-----------------------------------|--------|
| Staging page light rebuilds | Live on tcstaging via REST |
| Social calendars, Pinterest board/pin briefs, membership emails | `diagnostics/outputs/growth/` |
| ISI checklists + static site fixes | `isi-consulting/` + diagnostics |
| Governance outlines, Semrush checklists | `diagnostics/outputs/docs/` |

---

## 4 — Queue rules (agents must obey)

- Path: `diagnostics/agent-queue/{READY,CLAIMED,DONE}/`
- Claim = `git mv READY/foo.md CLAIMED/foo.md`, add `claimed_by` + timestamp in the file, commit.
- One ticket at a time per agent. Same-family ban still applies (two agents never edit same page IDs).
- If REST `users/me` ≠ 200: stop that agent; write `diagnostics/outputs/BLOCKED-auth.md`; do not loop.
- Prefer claiming tickets whose `lane:` matches the starter prompt.

---

## 5 — Relationship to old paste pack

`docs/MARSHAL-STEP-1.md` (Claude paste) is **Plan B** if you want Claude’s voice specifically.  
**Plan A (default):** this fleet. Growth drafts are written by Cursor Agent `02-growth-content` into the repo.

---

## 6 — Success definition

Setup is done when:
- 3 agents are running (or have finished) on the Environment with secrets
- READY queue is draining into DONE without you pasting paragraphs
- You only review `diagnostics/outputs/` and staging URLs
