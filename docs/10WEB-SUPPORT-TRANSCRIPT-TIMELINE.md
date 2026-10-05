# 10Web support & AI chat — timeline for exhibits

**Source:** Daniel Reid export of 10Web AI Chatbot + live chat (Marta, Nazeli, Zendesk).  
**Primary ticket:** **#375660** (merged repeatedly; user reports “resolved” without fix).  
**Site in scope:** **`https://tcstaging.truth-collective.com`** (Hostinger staging); live **`truth-collective.com`** idle/broken in GSC.  
**Not ISI Consulting** (started weeks later).

**Context (separate from 10Web):** Earlier **live** site damage from non-Cursor AI (Claude) code conversion; user rebuilt at scale on **tcstaging** (~8,600 pages in user narrative; ~86 hubs/pages in early 10Web chats). **7/25/2026** user + Cursor checklist → begin 10Web migration for polish/launch.

This document is a **chronological index** for counsel. Full verbatim transcript is retained by Daniel (PDF/HTML/chat export); do not commit payment details or credentials to git.

---

## Phase A — Pre-migration sales & promises (7/24–7/25)

| Date (2026) | Actor | Summary |
|-------------|--------|---------|
| **Jul 24 ~2:20 PM** | 10Web AI | Session opens “You’re back online!” User asks: send **existing HTML/animation pages** for 10Web to **polish** and migrate to live to **replace broken site**. |
| Jul 24 | 10Web AI | States pages must be **converted to 10Web Builder / WP**; offers **Booster**, **Migration Assistant** (zip `wp-content` + SQL); **does not directly edit** sites for users. |
| Jul 24–25 | 10Web AI | **Pro Plan** / trial / pricing narrative; promises **90+ PageSpeed**, **preserve structure**, **migration copy does not affect live**, **domain/URLs preserved**, **backups**, **“full control”**, **AI does not change without approval**. |
| Jul 24–25 | User | Discloses **Cursor** as reliable guide; **Hostinger WP**, custom **HTML/JS** hover/EXPLORE, **750+ books / 3500+ products / 12 hubs**, **`tcstaging`**, live stalled; prior **Claude/ChatGPT/Copilot** failures; **LiteSpeed** on staging, **Cloudflare** on live DNS. |
| Jul 25 ~10:37 AM | User (“Charlie”) | **Ready to migrate**; Cursor completed checklist; will disable **LiteSpeed** before migration. |
| Jul 25 | 10Web AI | **10Web Manager Plugin** steps: download from dashboard → WP upload → subdomain + datacenter → **Migrate** (copy on 10Web, live unchanged until DNS). |

### Key promises to flag (Phase A)

- Custom **HTML/JS/CSS** “should remain intact” after migration; review if broken.  
- **Affiliate URLs/IDs** “remain intact.”  
- **Layered hub/child structure preserved.**  
- **Do not point DNS before** testing on temporary 10Web subdomain.  
- **Staging + live unaffected** during automated migration copy.

---

## Phase B — Payment, onboarding failure, first migration attempt (7/25)

| Date | Actor | Summary |
|------|--------|---------|
| Jul 25 | User / AI | **7-day trial / “Pro plan”** not visible; **$120 “pay now”**; no green diamond; user pays **AI Starter ~$10/mo**. |
| Jul 25 | 10Web AI | **No phone support**; live chat only for paid/trial; offers escalate. |
| Jul 25 | **Marta** (human) | **No “My Sites”** — corrects to **“Websites”**; user must **delete placeholder site** (1-site limit) to get **migration plugin** download. |
| Jul 25 | User / Marta | Plugin installed/activated; **no redirect** to 10Web dashboard; user stuck; Marta asks host type then **closes chat** for inactivity. |
| Jul 25+ | User | **Migration runs 6+ hours**; **disconnect**; message to **start over** (per user message to bot later). |

---

## Phase C — Disconnect, AI Builder confusion, escalation (late Jul–8/3)

| Date | Actor | Summary |
|------|--------|---------|
| (Jul 28–Aug 1) | Hostinger / user | Repo handoff records **DB restore Jul 28**, **files restore Aug 1** (parallel track — see `STAGING-RECOVERY-HANDOFF.md`). |
| **Aug 3 ~10:35 AM** | User | **Explicit:** “Not WordPress migration — **AI Builder created fake site again**.” Needs **human** migration of **`tcstaging.truth-collective.com`** to **`.10web.site` preview** — **no AI Builder**, **do not publish AI site**. |
| Aug 3 | 10Web AI | Repeats generic “Automatic Migration” + URL (bot loop); user charged for **another website** confusion. |
| Aug 3–4 | User | **8 days** migration attempts; **reconnect fails**; support contacts **no help**; **“24/7”** vs **offline** message. |
| **Aug 4 ~9:34 AM** | **Nazeli Sargsyan** | **Merges ticket into #375660**; “addressed in another ticket” — user reports **merged/closed unresolved** pattern (**25+ tickets** per user). |

---

## Phase D — Contradictions & issues for counsel (pattern list)

1. **Product vs migration:** Sold **Booster / polish** and **preserve custom code**, but flow pushes **AI Builder**, **new site**, **“what website do you want to build?”**  
2. **Plan limits:** **1 website** slot → user must **delete** site to download plugin; then **“edit website”** / limit messages block progress.  
3. **Trial/marketing:** Repeated **Pro / 7-day free** instructions UI **does not match** (AI Starter checkout **$120**).  
4. **Support:** **“24/7 live agents”** vs **offline** Zendesk; chats **closed** mid-issue (Marta); **ticket merge** (#375660) without resolution.  
5. **Technical:** **6+ hour** migration → **disconnected**; **REST API / disk quota / PHP** suggested by bot after failure.  
6. **Wrong plugins:** WP shows **Photo Gallery / Form Maker by 10Web**, not **10Web Manager** until dashboard path corrected.  
7. **User reliance on Cursor:** User states **Cursor** guided checklist and warned **LiteSpeed**; 10Web bot deflected **“why Cursor said no AI platforms.”**

---

## Cursor’s role (for separation of claims)

| Topic | Note |
|-------|------|
| **Earlier live crash** | User attributes to **Claude** (Tailwind→WP conversion), **months before** 10Web — separate from 10Web migration failure. |
| **Staging rebuild** | **Cursor + Daniel** on **tcstaging** (Handoff, REST era). |
| **10Web period** | User cites **“Cursor says…”** in 10Web chat; **Migration Brief** and rules require **preserve-only** staging→live. |
| **Evidence location** | This transcript = **10Web vendor channel**. **Desktop Cursor** July threads (e.g. **Jul 18 “Page image cropping”**) are **separate exhibits** — search Desktop history + forensic `User` copy. |

---

## Recommended exhibit packaging (Daniel local)

```
J:\DLegal_Exhibits2026_10_05_cursor_user_FORENSIC_COPY\
  10web-correspondence\
    10web-ai-chat_Jul24-Aug04_FULL.pdf          (or .html export from 10Web)
    zendesk-ticket-375660-all-merged.pdf
    EXHIBIT-INDEX.txt
  exports\                                       (Cursor Desktop .md exports)
  cursor-user-FORENSIC.zip                       (when copied)
```

**EXHIBIT-INDEX.txt** should list: date, source (AI/Marta/Nazeli), one-line description, Bates prefix if attorney assigns.

---

## Search Console / DNS facts (user stated in chat)

- Live **truth-collective.com**: broken/under construction; **~17 pages indexed**.  
- **tcstaging**: **LiteSpeed** cache, **not Cloudflare**; staging not indexed.  
- DNS: **Cloudflare** A records for main + subdomains; user asked whether **10Web primary** conflicts with stalled live WP — bot said configure A record, **not full DNS replace**.

---

## Repo cross-references

- `STAGING-RECOVERY-HANDOFF.md` — Jul 24 uploads restore, Jul 28 DB, Aug 1 files; 10WEB Manager active; ticket **#375660**.  
- `docs/10WEB-MIGRATION.md` — decommission / staging→live gates.  
- `docs/CURSOR-CHAT-PRESERVATION-10WEB-CRASH.md` — Desktop vs Cloud evidence.

---

*Generated from user-provided transcript paste, 2026-10-05. Not legal advice.*
