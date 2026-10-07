# Owner testimony — kind-louse fake site, failed migrations, WP access

**Recorded:** 7 October 2026 in Cloud run `bc-3c3a1616-bd53-407e-8562-11da050498f8`.  
**Speaker:** Daniel Reid (owner).  
**Status:** owner testimony. Not a legal opinion. Dated engineering notes below are separate.

---

## What Daniel stated this date

- `kind-louse` / `kind-louse.10web.cloud` was **10Web’s fake website**, made **during** the migration. It was **not** a Truth Collective design mock Cursor chose to copy.
- 10Web ran **several migrations**. They kept coming back as **failed / disconnected**.
- 10Web **humans** then said they had to have **access inside WordPress** to pull the site through to their side.
- **That access step is when the damage occurred.**
- What was left: **fragments of what Daniel had provided them**, mashed together with **portions of the fake kind-louse website**.

---

## What kind of Cursor it was (engineering, not memory)

Daniel does not recall the product label. Git and GitHub do.

| Kind | Was it this? | How we know |
| --- | --- | --- |
| **Cloud Agent** (same *kind* as this chat; GitHub also calls it **Background Agent**) | **Yes, for the July Truth Collective git work** | Commits 14–26 Jul 2026 are authored `Cursor Agent <cursoragent@cursor.com>`. Branches use the Cloud pattern `cursor/<name>-<4hex>`. PRs carry `https://cursor.com/agents/bc-…` and `background-agent?bcId=` footers. |
| Desktop Chat / Composer / local Agent | **Not proven for late July TC git** | Oct 6 note on PR #5: no late-July Desktop/Task transcript found on the machine. Desktop may still have been used to *read* Cloud threads. |
| Cursor Task / Copilot Task | **No** | Different Microsoft product; later used as a drafter, not the July 10Web guide. |
| This Sep 19 Cloud run | **No** | This ID started 19 Sep 2026. Same *kind*, new *run*. |

**Runs (different IDs, same Cloud Agent kind):**

| Window | Branch / PR | Agent URL if known |
| --- | --- | --- |
| 14–18 Jul (prep; “Page image cropping”) | PR #2 `cursor/lock-in-master-brief-and-components-b1dd` | https://cursor.com/agents/bc-b360733d-fbaa-412a-bff6-bcacdceab1dd |
| **25–26 Jul (migration-start days)** | `cursor/image-fix-and-membership-toggle-2672` (Computers rebuild, drop-in HTML). **No GitHub PR**, so **no bcId in the repo** | Ask Cursor support for that **branch name** and dates 25–26 Jul 2026 |
| From 8 Aug (after damage) | recovery handoff onward | later Cloud IDs; not the damage-hour thread |

“Same Cursor all the way through” in the product sense = **Cloud Agent**. It is **not** proof one single `bcId` stayed open from 14 Jul through the WP-access damage hour.

---

## How this testimony fits notes already in the repo

| Claim | Already in repo? | File |
| --- | --- | --- |
| Fake Builder site | Yes, owner to 10Web **3 Aug 2026**: “AI Builder created fake site again”; asked human migration of `tcstaging`, no publish | PR #5 `docs/10WEB-SUPPORT-TRANSCRIPT-TIMELINE.md` (not on this branch except by pointer) |
| Failed / disconnected | Yes: 6+ hour run, disconnect, start over; 8 days reconnect fails | same timeline |
| kind-louse host exists; do not port | Yes, freeze 8–9 Aug. Then treated as a **mood board**. Owner 7 Oct **corrects** that: it was the **fake migration site** | `diagnostics/hub-technology-10web-freeze-2026-08-08.md` |
| Invented categories on kind-louse | Yes: Robotics mega-menu and other fake trees listed as **do not port** | freeze note |
| 10Web reaching WP | Plugin **10WEB manager Active v1.20.21** on 8 Aug | `STAGING-RECOVERY-HANDOFF.md` |
| Mash visible as 10Web HTML tags | **No.** 8 Aug public HTML had **no** `10web`/`tenweb`/`twbb` markers | `diagnostics/css-inventory-2026-08-08.md` |
| Mash visible as wrong IA | **Consistent, not proven:** 8 Aug Tech Hub inventory **16 tiles** vs **8** real published children | freeze note vs 8 Aug screenshot inventory |
| Exact clock of WP admin access | **Not in this VM** | 10Web ticket `#375660` thread (owner-held) |

---

## Counsel packaging (not legal advice)

Treat as **three exhibits**, not one:

1. **Cursor Cloud Agent** — checklist / relay *kind* (git 14–26 Jul; PR #2 URL). Cursor did not operate 10Web’s Builder.
2. **10Web failed/disconnected migrations + fake Builder (`kind-louse`)** — vendor chat 24 Jul–4 Aug + any remaining `kind-louse.10web.cloud` capture.
3. **Human WP access / Manager plugin** — ticket `#375660` and Hostinger/WP user logs if counsel can obtain them. That is the step Daniel names as the damage event.

Do not label kind-louse a “gold sample.” The Standing Brief PDF (`vercel-and-10web-comparison.pdf`) is a **separate** annotated comparison pack. kind-louse is **Tier 3 evidence of damage**, not a model to rebuild toward.
