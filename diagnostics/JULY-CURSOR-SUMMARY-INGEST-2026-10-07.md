# July Cursor summary — capture now, then ingest here

**Owner 7 Oct 2026:** After finding the July–August 10Web Cursor thread, Daniel asked **that** conversation to summarize:

1. State of the website **prior** to migration start  
2. Issues **during** migration  
3. **Directives given to 10Web** that they ignored  
4. Level of **destruction after** migration  

That summary is high-value **prior-agent testimony**. It is not the same as this Sep 19 Cloud Agent’s later engineering memos.

---

## Do this immediately (then stop)

A summary **request** is not the same as Continue / Apply / edit WordPress. Still: **do not ask that old thread anything else.**

1. **Export Transcript** (Desktop) or **Print → PDF** (Cloud) **now**, so the new summary turn is included.  
2. If you have not already made the forensic `Cursor\User` zip, do Path A1 in `diagnostics/HOW-TO-SAVE-FOUND-CURSOR-CHAT-2026-10-07.md` after a full Cursor Exit.  
3. Save as:

   `2026-10-07__JULY-CURSOR__SELF-SUMMARY__pre-during-directives-post.md`

   plus a PDF if you printed. Two copies (external drive + Google Drive).  
4. **Do not** paste the full raw chat (secrets) into GitHub.  
5. Paste **the summary only** into **this** Cloud Agent (`bc-3c3a1616…`). This agent will file it as **Exhibit C — July Cursor self-summary (7 Oct 2026 recap)** next to the 10Web vendor timeline, labeled testimony not independent lab proof.

If the old agent started **editing files or giving WP steps**, stop it. Export anyway. New site work stays in this staging Cloud run.

---

## Four headings — what THIS recovery record already holds

Use this to **compare** with the July conversation’s own summary. Sources are git/handoff/10Web chat index from **8 Aug 2026 onward**, plus owner statements this week. This is **not** a substitute for that thread’s recap.

### 1. Website state prior to migration (~before 25 Jul 2026)

**Owner / contemporaneous notes**

- Migration purpose (24–25 Jul 10Web chat): polish existing HTML/animation pages and migrate; replace the stalled **live** site. Work site was **`tcstaging.truth-collective.com`** (Hostinger WP).  
- Custom **HTML/JS** hover / EXPLORE; Additional CSS in Customizer (not Code Snippets).  
- Owner scale in 10Web chat: hundreds of books, thousands of products, ~12 hubs (narrative).  
- Computers child: owner said it reached ~**90/100 Rank Math**, animated, photos, overlays, **finished just before the crash**.  
- Git 14–18 Jul: Master Brief, hub structure, LiteSpeed/cache diagnosis, overlay/explore class discipline (`tc-overlay-card` on column, `tc-explore-hub` on image, `tc-book-card` for books).  
- Locked animation **02A** (product View + TC Grade) later described as still working on a product page after the crash.

**This agent has not seen a pre-25-Jul full-site backup.** Pre-state is owner + git + later WP revisions, not a frozen disk image.

### 2. Issues during migration (25 Jul – ~4 Aug)

From the owner-supplied 10Web chat index (`docs/10WEB-SUPPORT-TRANSCRIPT-TIMELINE.md` on PR #5) and this week’s testimony:

- Plan/UI mismatch (Pro trial vs AI Starter checkout).  
- 1-site limit; placeholder delete to get **Manager** plugin.  
- Plugin install without dashboard redirect; Marta chat closed.  
- Migration **6+ hours** then **disconnect** / start over; **several** failed/disconnected runs.  
- 10Web path pushed **AI Builder** / new site (`kind-louse.10web.cloud`) instead of copying `tcstaging` WordPress.  
- **3 Aug:** owner: “AI Builder created fake site again”; asked **human** migration of `tcstaging` to a `.10web.site` preview; **no AI Builder; do not publish**.  
- **4 Aug:** ticket merge into **#375660**.  
- Parallel Hostinger track (handoff): DB restore **28 Jul**, files **1 Aug**, uploads **28 Jul and 24 Jul**.  
- Owner 7 Oct: after failed runs, **humans required access inside WordPress**; that is the named damage step (mash of real fragments + kind-louse).

### 3. Directives to 10Web (Cursor-guided / owner-relayed) vs what the log shows

These are the **do / do-not** items already indexed. The July Cursor thread is the place that likely **drafted** the paste-to-10Web wording. Pair each with the 10Web reply (Exhibit C vs Exhibit T).

| Directive (as recorded) | What the 10Web log shows |
| --- | --- |
| Disable **LiteSpeed** before migrate | Owner told 10Web Cursor completed a checklist and would disable LiteSpeed |
| Migrate **existing** `tcstaging` WP (custom HTML/JS/CSS), **preserve** structure, affiliates, hub/child tree | Bot promised preserve; flow still pushed **Builder / convert / new site** |
| **Do not** use **AI Builder**; **do not publish** a fake AI site | Owner had to say this **explicitly 3 Aug** after “fake site again” |
| Preview on 10Web subdomain; **do not point DNS** until tested | Bot also said don’t point DNS before test; later DNS/A-record talk mixed with live Cloudflare |
| 10Web **Manager** plugin (not Photo Gallery / Form Maker) | Wrong 10Web plugins appeared in WP until path corrected |
| Human migration after automations failed | Ticket merge / “addressed in another ticket” without a completed preserve-copy |

“Ignored” is a **counsel** word. This file only lists **instruction vs observed path**. The July self-summary should quote the actual paste blocks if they are in that chat.

### 4. Destruction after migration (as measured from 8 Aug, not 25 Jul)

**Must split three layers** or the claim fights itself.

**A. 10Web-period / WP-access mash (owner: this is the damage event)**  
- kind-louse fake Builder site mixed with fragments of the real pages.  
- 8 Aug Tech Hub inventory: **16 tiles** vs **8** real children (foreign IA consistent with mash).  
- 10WEB Manager still **Active v1.20.21**.  
- `10web_tmp` later **gone** after Jul 24 uploads restore.  
- Public HTML 8 Aug: **no** `10web`/`tenweb`/`twbb` **tags**; damage showed as **wrong blocks, missing classes, dead hrefs, missing July upload files**.

**B. Hostinger restores (not 10Web writes)**  
- Jul 24 uploads restore **crushed Computers worse** than the 28 Jul review.  
- July `uploads/2026/07/` files often **404**.  
- DB 28 Jul / files 1 Aug did not return a healthy site.

**C. Later Cursor recovery (also not 10Web)**  
- 12 Aug hub-parent light rebuilds.  
- 19 Aug Computers light rebuild: photos → SVG placeholders (further catalog stripping).

**What survived (cuts against “everything wiped”)**  
- Additional CSS **57,615** chars, SHA unchanged 8 Aug–23 Sep.  
- Pages often still existed; 404s were often **stale in-content hrefs**.  
- Computers revisions still held Amazon codes and many photo references (e.g. rev 8273).  
- Production Technology Hub **404** as of 7 Oct; staging Tech Hub **200**.

Full counts: `diagnostics/10web-migration-damage-evidence-2026-10-07.md`.

---

## When the July summary is pasted into this chat

This agent will:

- Save it as a dated diagnostics file  
- Label it **July Cursor self-summary (generated 7 Oct 2026 inside the recovered thread)**  
- Not merge it silently into engineering counts  
- Flag contradictions with 8 Aug probes, Hostinger restore dates, and 19 Aug Cursor rebuilds so counsel can keep layers separate
