# Unified governance / evaluation engine — what is in the repo

**Prepared:** 12 October 2026  
**Question:** Has this packet accounted for the unified evaluation governance engine? If the site cannot be completed, is that engine wasted?  
**Owner pointer this turn:** `unified-governance-system_files`

**Not a legal opinion.**

---

## Direct answers

**Accounted as a damages category: yes.** `06-SCALE-LABOR-ENGINE-AND-EDITORIAL-2026-10-12.md` already treats ~110 days of engine labor as a separate loss from lost product cards. If the site cannot be finished, or is rebuilt without this system, that work has no public place to run. That is Daniel’s statement. This scan does not shrink it.

**Accounted as executable JavaScript in this git checkout: no.** This branch does not contain thousands of lines of JS/HTML that compute TC Grades from a URL or ID. Standing Brief §12 paused that implementation after the crash. Daniel told recovery on 11 August he could not locate the Cursor code that was supposed to replace the manual spreadsheets.

**The six files in the 12 October 17:14 upload are already in this repo, byte-identical.** SHA256 prefixes match `docs/legal/source-pdfs/`. They are the **specification** set (Stages I, III, V, VI, master engineering PDF, Compliance Division). They are not a coding engine.

**The GitHub folder in the screenshot is now scanned.** Public repo `https://github.com/corisan123/unified-governance-system.html` (created 4 September 2026, description “Evaluation Machine”, commit `49d9cd3` “Add files via upload”). It is a browser “Webpage, Complete” save of a **Copilot.fun** artifact (`blob:https://copilot.fun/6296750c-3c77-4dad-aea5-ede042d770fa`), title **TC Unified Governance Binder | Truth Collective**. Most of the large `.js.download` files are Copilot’s host (Vite/React, Microsoft Clarity, Bing UET), not TC scoring math. The TC piece is the 216 KB HTML: binder TOC plus an evaluation form that builds a prompt and calls `AppSDK.ai.chat` (Microsoft Copilot). There is **no** local quantum-mathematics library in that folder. See §1b.

**The word `quantum` does not appear** in the Governance Binder CURRENT text (~142,703 characters) or in extractable text of the Stage I/III/V master PDFs opened this turn. Weighted scoring, mission-critical 50–60% bands, IEEE/UL/JEDEC/BIFMA mapping, and per-category addenda **do** appear. If the quantum/advanced-mathematics layer lives in unpublished JS or another file, send that file by name.

---

## 0. Authorship (owner correction 12 October 2026)

Daniel: **Copilot and Copilot Task wrote the governance content first. Cursor Desktop afterwards wrote the complex JS and HTML engine.**

That matches Standing Brief §12, written 8 August 2026, before this Cloud run:

| Lane | Assigned work |
| --- | --- |
| Copilot Edge | Quantitative / qualitative engineering evaluation **documents** and SME spec sheets |
| Copilot Task | Interactive Master Binder **UI** (example: Premium Display Intelligence) |
| **Cursor** | Complex **HTML/JS** so Daniel enters product URL or ID → summary + technical TC Grade (not vibe scoring) |

Do not treat the 4 September Copilot.fun save as the whole engine, and do not treat Copilot as the author of the later Desktop coding.

| Layer | Who | Where it is |
| --- | --- | --- |
| Governance binder, Stage I–VI PDFs/docx, Compliance Division | Copilot / Task, then filed in git | `docs/brand-references/selection-standards/`, `docs/legal/source-pdfs/` |
| Copilot.fun “TC Unified Governance Binder” page (form + `AppSDK.ai.chat`) | Task-era interactive face, browser-saved 4 Sep 2026 | `corisan123/unified-governance-system.html` |
| Excel Evaluation Engine v1 | Cursor **Cloud** Agent 3 Aug 2026 (`cursoragent@cursor.com`) | `evaluation-engine/TC_Evaluation_Engine_v1.xlsx` |
| Complex JS/HTML URL-or-ID engine | **Cursor Desktop** (owner). Standing Brief paused it after the crash | **Not** in `truth-collective` as thousands of lines. **Not** the 1.5 MB Copilot Vite file. 11 Aug recovery already recorded Daniel could not locate that Cursor code in this repo |
| ISI Consulting diagnostic engines (Monte Carlo, `math.js`, engine-bus, 91 JS files, ~579 KB) | Cursor Desktop, **different company** | `corisan123/ISI-CONSULTING-FULL`. ISI `HANDOFF.md` (23 Sep 2026) forbids mixing that window with Truth Collective and names a separate canvas “TC evaluation layer map” |

Counsel sentence:

> Copilot and Task wrote the governance standards. Cursor Desktop was then assigned the complex JS/HTML evaluation engine. A Copilot.fun save from 4 September still scores by calling Microsoft Copilot. That save is not proof Desktop never wrote a local engine. The Desktop TC engine files are not in the Truth Collective git checkout this agent has. A large Cursor Desktop quantitative JS tree exists for ISI Consulting and is a separate product.

---

## 1. What `unified-governance-system_files` mapped to in this chat

Six documents uploaded 12 October 2026 17:14. Same bytes as files already ingested:

| Upload name | Repo copy | Size |
| --- | --- | --- |
| `Truth_Collective___Standards__Governance___Compliance_Division` | `source-pdfs/Standards-Governance-Compliance-Division-2026-10-12.docx` | 27,155 |
| `II_Master_Engineering_Driven_Evaluation_System_update_8_2_2026` | `source-pdfs/II-Master-Engineering-Driven-Evaluation-System-update-2026-08-02.pdf` | 239,518 (7 pages) |
| `Stage_I_Evaluation_Benchmarking_and_Governing_Bodies` | `source-pdfs/Stage-I-Evaluation-Benchmarking-and-Governing-Bodies.docx` | 29,684 |
| `Stage_III_Qualititative_Eval_Process_-_Copy` | `source-pdfs/Stage-III-Qualitative-Eval-Process.pdf` | 407,992 (5 pages) |
| `TC_STage_V_Evaluations_Standards_Processes` | `source-pdfs/Stage-V-Technology-Hub-Evaluation-System.pdf` | 393,977 (6 pages) |
| `TC_Stage_VI_Workspace_Products_and_Tools__Evaluation_Engieering_Selection__Standards` | `source-pdfs/Stage-VI-Workspace-Evaluation-Standards.docx` | 28,997 |

These six are **public/internal governance specs**. They define how a book is not graded like a computer or a desk. They do not execute.

### 1b. The GitHub `unified-governance-system_files` folder (screenshot, commit 49d9cd3)

Opened from `corisan123/unified-governance-system.html` on 12 October 2026. Saved from `blob:https://copilot.fun/6296750c-…`. HTML title: **TC Unified Governance Binder | Truth Collective**.

| File | Size | What it actually is |
| --- | --- | --- |
| `6296750c-3c77-4dad-aea5-ede042d770fa.html` | 216,792 | The TC artifact: binder navigation (Parts I–V, 12 hubs, appendices) **plus** “TC Evaluation Engine” form (item name, hub, UL, ASIN, Generate Report). Visible text ~2,654 words. Inline TC UI JS ~22,573 characters / 449 lines. |
| `saved_resource.html` | 3,953 | Copilot “Executable Web Artifact” iframe shell. |
| `index-BmkOI90j.js.download` | 1,561,378 | Copilot Vite/React host. 464 hits for `copilot`. Not TC grade formulas. |
| `index.zDO0dYVx.js.download` | 114,350 | Copilot sandbox JS. |
| `index-KGdgaBzR.css` | 614,192 | Copilot/Tailwind host CSS. |
| `clarity.js.download`, `n59ae4ieqq`, `0.8.69` | 73 KB + | Microsoft Clarity analytics. |
| `bat.js.download`, `355045625.js.download` | 55 KB + | Bing UET conversion pixel. |
| `message-reactions-*.css`, `use-initial-contacts-*.css` | small | Copilot chat UI chrome. |

How the on-page “engine” scores: the Generate button builds a text prompt (“Evaluate the following item using the TC framework”) and calls `AppSDK.ai.chat` with a 2,530-character `TC_SYSTEM_PROMPT` (product weights 30/25/20/15/10, 21-point books, 5.0–below-3.0 bands). The model returns JSON. **That is an LLM call to Microsoft Copilot, not thousands of lines of local advanced mathematics.** The word `quantum` does not appear in the HTML or the prompt.

This does **not** replace the 142k-character Governance Binder docx or the Excel Engine v1. It is the Copilot-hosted interactive face of the binder plus an AI-backed grade form. It cannot run without Copilot AppSDK. If staging never launches, this artifact also has no Truth Collective page to live on.

---

## 2. Governance documents already in git (the binder)

| File | What a scan shows |
| --- | --- |
| `docs/brand-references/selection-standards/TC_Governance_Binder_CURRENT.docx` | Version 2.1, August 2026. ~4,450 text nodes, ~142,703 characters. Cover: “Unified Governance System — Engineering, Editorial, Literature & Hub Level Standards.” TOC claims **all 17 governance documents**. Parts I–V (Master, Engineering, Editorial/21-point, Hub evaluation systems, Editorial series: Ones Who, AI Mastery Podcast, Truth Untold). Weighted scoring mentioned 41 times. Stage I/II/III named. IEEE 16, UL 49. No “quantum”, no “JavaScript”. |
| Split Part I / Part III docx | Older splits; CURRENT is the authority (ingest 11 Aug). |
| `Multistage-Engineering-Evaluation-Overview.docx` + `multistage-engineering-overview-II.pdf` (1.9 MB, 8 pages; PDF extract is nearly empty — likely image-heavy) | Overview of the triple-stage engineering track. |
| `Standards-Governance-Compliance-Division.docx` | Layer 1 master (same family as the 17:14 upload). |
| `docs/engineering-evaluation-standards.md` on branch `cursor/lock-in-master-brief-and-components-b1dd` | July prep copy of engineering standards. |

Binder ingest notes: `diagnostics/governance-binder-CURRENT-ingest-2026-08-11.md` (and Part I / Part III ingests).

Canonical public Stage map in the binder:

- Stage I — standards bodies before scoring  
- Stage II — quantitative engineering (products)  
- Stage III — qualitative literature/editorial (21-point)

The 12 October Stage V / Stage VI files are **hub-level** documents (Technology; Workspace). They sit in binder Part IV. They do not replace Stage I–III numbering. Do not collapse “Stage V PDF” into “the whole engine.”

---

## 3. Coding engines found in git

### A. Manual Copilot workbook (this branch)

`docs/brand-references/selection-standards/TC-Master-Summary-Document-Cursor-Copy.xlsx` (54,791 bytes). Nine sheets: Engineering Scoring, Editorial Scoring, Compliance, Cat. Benchmark, Page-Lvl Eval, Weighted Scoring Model, Mission-Critical, Standards & Compliance. **One formula tag.** 11 August ingest: this is the “type everything manually” path Daniel rejected. Weighted Scoring Model had `#NAME?` in that ingest.

### B. Evaluation Engine v1 workbook (now copied onto this branch)

Path: `evaluation-engine/TC_Evaluation_Engine_v1.xlsx` (21,371 bytes).  
Source branch: `cursor/image-fix-and-membership-toggle-2672` and `cursor/10web-lawsuit-testimony-2672` (commit 3 August 2026: “Add TC Evaluation Engine v1 workbook from master metrics”).  
README: `evaluation-engine/README.md`.

Eight tabs: Instructions, Master_Config, Intake, Engineering_Score, Editorial_Score, Compliance, Category_Benchmarks, Results.

What it **does**:

- One product or book on Intake  
- Score only Applicable rows (Weight × Score)  
- Products use engineering path (not a forced 60/40 mix)  
- Books use 21-point-style editorial path  
- Results sheet auto-calculates TC Grade, quality band, publish recommendation  
- About **180 spreadsheet formulas** (117 engineering, 46 editorial, 16 results, 1 compliance)

What it **does not** do:

- JavaScript runtime  
- URL/UL-number in → public HTML tile out (README lists that as “still missing”)  
- Category presets that auto-flip Applicable rows  
- Quantum mathematics library  

This is a **working Excel scoring engine** built from the master sheet + governance PDF. It is not thousands of JS lines.

### C. Intended Cursor HTML/JS engine (not in this checkout)

Standing Brief §12 and the 11 August ingest:

- Input: product/book URL or ID (Daniel also said UL #)  
- Output: short description, TC Grade, stars/`tc-grade-block`, reasons to buy/avoid  
- Internal weights hidden from consumers  
- **Paused** after the crash. “Do not discard. Resume after staging is stable.”  
- **Not found** as Python/JS in this recovery branch or in obvious recovery history  

The only `.js` pulled from the July/August Cloud branches in this scan is `membership-toggle/tc-membership-toggle.js` (**353 lines**). That is the visitor/member toggle, not the grade engine.

### D. What *is* on staging related to grades

- Additional CSS for `.tc-grade-block` and product overlay “TC Grade” buttons  
- WordPress patterns 2853–2859 (TC Grade 3.5 / 4 / 4.5 / 5 display blocks)  
- Hub “How We Evaluate …” briefs injected 19 September (short HTML copy, not the scorer)  
- Page 6751: Technical Selection Benchmarking Overview (public stub / binder link target)

Those are **display**. They are not the scoring engine.

---

## 4. If the site cannot be completed

Use this, not a shrug:

> The unified governance system is a written 17-document binder (August 2026 v2.1), hub Stage documents, a manual master workbook, and an Excel Evaluation Engine v1 that emits TC Grades from weighted engineering or 21-point editorial scores. The live-site HTML/JS engine that was supposed to take a URL or ID and write a public grade tile was paused after the 10Web crash and is not in this git checkout. Product pages, catalogs, and overlay/grade markup were destroyed or gutted sitewide. Without those pages, and without the runtime on the site, the evaluation system has nowhere to attach. That labor (owner: about 110 days, plus the binder and workbooks) is wasted if the site cannot be finished.

Do not write: “There was no evaluation engine.”  
Do not write: “Copilot wrote the JS engine.” Copilot/Task wrote the **content**; Cursor Desktop was assigned the **coding**.  
Do not write: “The 1.5 MB `.js.download` file is Cursor Desktop’s TC engine.” That file is Copilot’s host.  
Do not write: “ISI’s Monte Carlo kernel is the Truth Collective engine” unless Daniel says those files were also for TC. ISI’s own handoff says they are not.  
Do not write: “quantum mathematics” as a string found in the TC binder; it is not in the binder text scanned today.

---

## 5. What to send next (specific)

1. The **Cursor Desktop** Truth Collective engine folder (JS/HTML that takes URL or ID / UL number and emits a TC Grade **without** `AppSDK.ai.chat`). Path on the PC, a zip, or the Desktop chat that built it.  
2. Confirm whether ISI-CONSULTING-FULL (`internal/js/math.js`, engine-bus) is **only** ISI, or was also meant as the TC quantitative kernel.  
3. If “quantum advanced mathematics” is a named file from the Desktop TC engine, send that filename.

Do not restore Updraft archives onto staging while hunting this.
