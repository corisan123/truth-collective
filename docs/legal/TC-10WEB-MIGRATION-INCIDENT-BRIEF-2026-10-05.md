# Truth Collective — 10Web migration incident

## Draft factual brief for counsel (Daniel Reid)

**Prepared from:** Daniel Reid submissions to Cursor Cloud Agent, session **“10web migration,”** **October 5, 2026**.  
**Purpose:** Organize evidence and narrative while **Cursor Desktop transcripts** (relay prompts to 10Web; post-migration damage) are still being located.  
**Not legal advice.** Attorney should verify facts, authenticate exhibits, and assign Bates numbers.

**Claimant / operator:** Daniel Reid — **contact@truth-collective.com**  
**Primary vendor thread:** 10Web (AI chatbot “Charlie,” live chat **Marta**, support **Nazeli Sargsyan**, Zendesk)  
**Primary support ticket ( cited repeatedly):** **#375660** (user reports **25+** tickets merged/marked resolved without remedy)  
**Staging property:** **https://tcstaging.truth-collective.com** (WordPress on Hostinger)  
**Live property:** **https://truth-collective.com** (user: idle/broken; **~17 pages** indexed in Google Search Console from prior version; under-construction homepage; not reconciled with staging)

---

## I. Executive summary

1. Daniel spent months rebuilding a large WordPress affiliate property on **staging** after an **earlier, separate** live-site failure attributed to **non-Cursor AI** (Claude) converting overlay/Tailwind-style work into WordPress in a damaging way; that live harm is treated as **irreversible** on the live domain.

2. Near completion of staging rebuild, Daniel engaged **10Web** (~**July 24–25, 2026**) to **polish, optimize, and migrate** staging work toward launch—not to replace custom Cursor-built HTML/CSS/JS inside WordPress with an **AI Builder “fake” site**.

3. **10Web** (per Daniel’s preserved AI/support log and statements) provided **conflicting onboarding**, **failed automated migration** (including **6+ hour** run and **disconnect**), pushed **AI Website Builder** flows contrary to Daniel’s explicit **August 3, 2026** instruction to migrate **real WordPress** from **tcstaging**, and provided **“24/7”** support that was often **offline** or **merged tickets without resolution**.

4. Daniel asserts **destruction inside WordPress** after the migration attempt, **inability to roll back**, and damage extending to **backups predating 10Web** (**August 9, 2026** statement to Claude). Recovery is **forward repair** on Hostinger staging, documented in project handoff materials.

5. **Cursor** (Desktop) allegedly drafted **specific instructions** for Daniel to relay to 10Web before and during migration; those **Desktop transcripts are not yet recovered** but are critical to show **vendor disregard**. **This brief** consolidates what Daniel **has already submitted** on **October 5, 2026**.

---

## II. Site and technical environment (as stated)

| Item | Detail |
|------|--------|
| Hosting (staging) | Hostinger — path **`public_html/tcstaging`** |
| Staging DB name | **`u867403816_jdn2C`** (per repo handoff) |
| Live hosting | Separate **`public_html`** (no `tcstaging` in path) |
| Stack | WordPress, **Astra**, **Kadence Blocks**, **Rank Math**, **LiteSpeed Cache** |
| DNS | **Cloudflare** (user member); staging **not** on Cloudflare per user (**LiteSpeed** cache on staging) |
| Domain registrar | **GoDaddy** (user stated) |
| Custom code | Extensive **HTML/CSS/JS** hover/overlay/EXPLORE behavior; locked **`tc-*`** classes maintained with **Cursor** (project docs) |
| Scale (user narratives) | **~86 pages** in early 10Web chats; **~8,600 pages** in later user narrative; **750+ books**, **3500+ products**, **12 hubs**, deep child/sub-child structure, **21 affiliates** (mostly Amazon) |
| Post-crash projects (excluded from July 10Web workspace) | **ISI Consulting** (weeks later); **governance engine** for Truth Collective metrics (**after** crash); **9/10/2026 HTML folder** (post-crash export) |

---

## III. Chronology

### A. Pre-10Web (months before July 2026)

- **Live site** damaged; user attributes to **Claude** (and other AIs) **Tailwind/HTML → WordPress** conversion errors—not Cursor-led work.
- User rebuilds on **`tcstaging`**.

### B. 10Web sales & planning

| Date (2026) | Event |
|-------------|--------|
| **Jul 24 ~2:20 PM** | 10Web AI session opens; Daniel asks whether 10Web can **polish existing HTML animation pages** and migrate to live to **replace broken live site**. Bot describes **Builder conversion**, **Booster**, **Migration Assistant** (zip), limits on direct editing. |
| **Jul 24–25** | Extended AI sales dialog: **Pro/trial**, **preserve URLs/structure/code**, **affiliate links intact**, **migration copy does not affect live** until DNS, **backups**, **full control**, **90+ PageSpeed** claims. Daniel discloses **Cursor** as trusted guide; **tcstaging** vs idle **live**; prior AI failures; **LiteSpeed**; **Cloudflare**. |
| **Jul 25 ~10:37 AM** | Daniel (“Charlie”) **ready to migrate**; **Cursor checklist** complete; plan to disable **LiteSpeed** before migration. |
| **Jul 25** | **7-day trial / Pro plan** not found in UI; user charged **~$120** / **AI Starter ~$10/mo** instead. **Marta** (human): **“Websites”** not “My Sites”; must **delete** placeholder site (**1-site limit**) to obtain **10Web Manager** plugin. Plugin activated; **no dashboard redirect**; Marta chat closed. User reports **6+ hour** migration then **disconnect** and instruction to **start over**. |

### C. Failed migration & escalation

| Date (2026) | Event |
|-------------|--------|
| **Jul 24** (handoff doc) | **Uploads-oriented restore** activity (project diagnostics). |
| **Jul 28** (handoff doc) | **Database restore** noted. |
| **Aug 1** (handoff doc) | **Files restore** for `tcstaging` noted. |
| **Aug 3 ~10:35 AM** | Daniel to 10Web: **Not** AI Builder; need **human** migration of **`tcstaging.truth-collective.com`** to **`.10web.site` preview**; **do not publish** AI site. |
| **Aug 3–4** | User reports **8 days** of failed migration/reconnect; **“24/7”** vs **offline** support; escalation requests. |
| **Aug 4 ~9:34 AM** | **Nazeli Sargsyan** merges ticket into **#375660**. |

### D. Post-incident recovery (Cursor + Claude under project rules)

| Date (2026) | Event |
|-------------|--------|
| **Aug 9** | Daniel to **Claude**: migration **~two weeks** prior **destroyed site within WordPress**; goal was **polish**; **cannot roll back**; damage **tangled in WP**; **pre-10Web backups damaged**. Claude issues **SPEC for Cursor** (hover/archive/editorial patterns) but prioritizes **repair before polish**. |
| **Aug 13** | Claude-generated **recovery handoff** snapshot (Technology Hub R7, Ones Who Gave, binder, Explore More, etc.) — see repo `docs/TC-RECOVERY-LAUNCH-HANDOFF-PASTE.md`. |
| **Aug 19+** | Cursor Cloud agent **“Truth collective content rebuild”** on GitHub repo (not July Desktop relay logs). |

**Record date of this brief assembly:** **October 5, 2026.**

---

## IV. Alleged misrepresentations / conduct pattern (10Web channel)

Derived from **Daniel’s full 10Web AI/support export** submitted **October 5, 2026** (see repo index `docs/10WEB-SUPPORT-TRANSCRIPT-TIMELINE.md`). Counsel to compare verbatim log.

1. **Preserve custom code** vs push to **AI Builder** / “what website do you want to build?”  
2. **One-website plan** forcing **delete** of dashboard site to download migration plugin.  
3. **Trial/marketing** (**Pro / 7-day free**) vs checkout showing **pay now ($120)**.  
4. **Migration** promises vs **disconnect**, **reconnect failure**, **start over**.  
5. **Support availability** (“24/7 live”) vs **offline** Zendesk messages.  
6. **Ticket handling** — merge into **#375660**, user alleges **resolved** without fix (**25+** tickets).  
7. **Wrong plugins** in WordPress (**Photo Gallery / Form Maker by 10Web**) vs **10Web Manager** for migration.  
8. **Aug 3 explicit instruction** — real **WordPress staging URL** — vs continued bot loops/upsell.

---

## V. Cursor’s role (evidence theory)

| Role | Description |
|------|-------------|
| **Pre-migration** | Daniel states **Cursor** produced **checklists** and **messages to relay** to 10Web (LiteSpeed, preserve code, do not AI Builder, sizing, plugin caution). |
| **During failure** | Daniel states **Cursor** reacted to failures and drafted **escalation / corrective instructions** for 10Web. |
| **After migration appeared complete** | Daniel states **Cursor** documented **destruction** inside WordPress and directed **forward repair** when rollback impossible. |
| **Separation** | **Earlier live Claude crash** is a **separate** incident from **10Web migration** harm on staging. |
| **Pending exhibits** | **Desktop Cursor** `.md` exports + forensic copy of `%APPDATA%\Cursor\User` + **`J:\Laptop Backup`** search — see `docs/CURSOR-10WEB-RELAY-EVIDENCE-SEARCH.md`. |

**Cloud Agent October 2025 session** (`10web-migration-a537`, local path `C:\Users\dreid\.cursor\agents\cursor\10web-migration-a537`) documents **recovery runbooks**, **not** July relay transcripts.

---

## VI. Evidence inventory

### A. Submitted to Cursor / indexed in repo (October 5, 2026)

| ID | Description | Repo / location |
|----|-------------|-----------------|
| E-1 | Full **10Web AI chatbot + Marta + Nazeli** transcript (Jul 24 – Aug 4+) | User paste; index **`docs/10WEB-SUPPORT-TRANSCRIPT-TIMELINE.md`**; full text should remain on **`J:\Legal-Exhibits\…\10web-correspondence\`** |
| E-2 | **Grok** search result: July dates in **STAGING-RECOVERY-HANDOFF**; only July TC chat index **Jul 18 “Page image cropping”** | User report Oct 5 |
| E-3 | **Claude Aug 9, 2026** thread excerpt (destruction, no rollback, backup damage; SPEC for Cursor) | **`docs/exhibits/CLAUDE-2026-08-09-10WEB-DAMAGE-AND-SPECS.md`** |
| E-4 | **Claude Aug 13, 2026** recovery handoff summary | User paste; aligned in **`docs/TC-RECOVERY-LAUNCH-HANDOFF-PASTE.md`** |
| E-5 | Project **staging handoff** (restores, rules, 10WEB Manager pause, #375660) | **`STAGING-RECOVERY-HANDOFF.md`** |
| E-6 | **10Web read-only probe** (Oct 5) | **`diagnostics/10web-migration-readonly-2026-10-05.md`** |
| E-7 | **Preservation playbooks** (Desktop, Windows, ISI separation) | **`docs/CURSOR-CHAT-PRESERVATION-10WEB-CRASH.md`**, **`docs/CURSOR-10WEB-RELAY-EVIDENCE-SEARCH.md`** |

### B. Pending / in progress (Daniel local)

| ID | Description | Action |
|----|-------------|--------|
| P-1 | **Cursor Desktop** transcripts — relay prompts, damage discovery, “Cursor says…” aligned to 10Web dates | History search + **`J:\…FORENSIC_COPY`** string search; **Laptop Backup** |
| P-2 | Complete **`User`** folder copy to **`J:\DLegal_Exhibits2026_10_05_cursor_user_FORENSIC_COPY`** | User reported folder **created but empty** Oct 5 — **paste from `%APPDATA%\Cursor\User`** still needed |
| P-3 | **Zendesk / #375660** merged ticket PDFs | Export from 10Web support portal |
| P-4 | **Hostinger** backup logs, hPanel timestamps (**Jul 24, 28, Aug 1**) | Daniel / counsel subpoena or export |
| P-5 | **Google Search Console** indexed URL export (live) | For migration/redirect planning & harm |
| P-6 | **Payment** records (AI Starter **~$120** charge, plan UI screenshots) | Redact PAN; keep receipts |

### C. Workspace forensics (October 5, 2026 — user reported)

- **`workspaceStorage`:** **five** folders; **one empty**; others mostly **~9/19/2026** modified — **not** July Truth Collective repo path in Open Folder list (**ISI**, **governance engine**, **9/10 HTML** only).
- **`globalStorage`:** `anysphere.*` folders dated **10/5/2026** — recent Cloud tooling, not July chats.
- **Desktop:** bottom agent showed **CLOUD**; **Export Transcript** for Cloud runs limited; July expected **Desktop local** history.

---

## VII. Harm narrative (Daniel statements — verify independently)

### Claimant diligence and personal circumstances (Daniel — October 5, 2026)

Daniel states, for the record:

- Since **February 11, 2026**, he has worked on Truth Collective / related livelihood **7 days per week**, typically **12–15 hours per day**, with **only two days missed** in that period (hospitalized **two days** for a **lung infection after chemo**, ~two months before Oct 5, 2026).
- **Oncology (Daniel — Oct 5, 2026):** **Stage 3** since **November 2025**; disease **metastasized to blood**; newly diagnosed **lymphoma** (Oct 5, 2026); **next appointment November 16, 2026** for treatment options. Prior course includes **chemo/immunotherapy** (per earlier statements).
- He cares for a **special-needs child** and states he **will not give up** supporting his children.
- He states that **ISI Consulting** income and **10Web-related legal recovery** are both critical to household stability, and that without progress on those fronts the family faces **homelessness within approximately two months** (user estimate Oct 5, 2026 — counsel to treat as urgency/context, not a proven fact in this document).

This section is **declarative** for damages and credibility; it does not replace medical or financial records.

### Technical and business harm

- Months of rebuild labor (also described in 10Web chat Jul 25).
- **Launch delay:** podcast, editorial, Pinterest, social (**8 business accounts** idle), **~21 affiliates**.
- **Technical harm:** tangled WordPress state; **media/path 404s** on key pages (e.g. Computers — project diagnostics); **CSS/stacking** (`tc-explore*` patches); inability to **restore** to pre-10Web baseline (**Aug 9**).
- **Economic:** 10Web subscription charges; opportunity cost; potential **RCA/compensation** ticket **#375660**.

---

## VIII. Related but separate claims

| Incident | When | Attribution (user) |
|----------|------|---------------------|
| Live site CSS/HTML catastrophe | Months before Jul 2026 | **Claude** / other AIs — Tailwind conversion |
| 10Web migration catastrophe | **~Jul 25 – Aug 2026** | **10Web** product, support, migration process |

Counsel may choose to **plead separately** or as **continuing course of conduct**; this brief **does not merge** legal theories.

---

## IX. Recommended exhibit packaging (Daniel `J:` drive)

```
J:\DLegal_Exhibits2026_10_05_cursor_user_FORENSIC_COPY\
  LEGAL-BRIEF-2026-10-05.pdf          ← export this markdown for counsel
  10web-correspondence\               ← full 10Web chat + Zendesk PDFs
  cursor-exports\                     ← Desktop Export Transcript .md files
  cursor-user-FORENSIC.zip            ← full User folder + SHA256 hash file
  hostinger\                          ← backups, invoices, logs
  payments\                           ← 10Web receipts (redacted)
  EXHIBIT-INDEX.txt
```

---

## X. Recovery & launch (operational — not 10Web)

Staging repair remains on **Hostinger** under **Cursor lead** + **Claude voice-only**; **10Web not used** for repair. See **`docs/TC-RECOVERY-LAUNCH-HANDOFF-PASTE.md`**, **`docs/TC-LAUNCH-ROADMAP.md`**, **`docs/TC-STAGING-TO-LIVE-MIGRATION.md`**.

---

## XI. Next steps when Daniel has capacity

1. Paste **`%APPDATA%\Cursor\User`** → **`J:\…FORENSIC_COPY`**; zip + **SHA256**.  
2. Desktop **History** → search **`tell 10web`**, **`tcstaging`**, **`destroyed`**, **`Page image cropping`**.  
3. Export **#375660** full ticket thread.  
4. Deliver **`LEGAL-BRIEF-2026-10-05`** + exhibits to counsel.

---

## XII. Certification placeholder

I, **Daniel Reid**, declare that the facts stated herein are true to the best of my knowledge, except where identified as repo/third-party documents.

Signature: _________________________   Date: **October 5, 2026**

---

*Assembled by Cursor Cloud Agent from user submissions. Repository branch: `cursor/10web-migration-a537`.*
