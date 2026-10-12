# Scale, labor, editorial hubs, and the evaluation engine

**Prepared:** 12 October 2026  
**Why this file exists:** Prior memos treated live `amzn.to` counts and “4000 SKUs” as if they were the size of the site. Daniel Reid rejected that. Catalog size is not affiliate-link count. Unfinished cards, research funnel, non-monetized editorial, The Ones Who Gave Everything, company-character rules, and the multi-stage evaluation engine were not accounted for. This file corrects that.

**Not a legal opinion.** Owner census figures are labeled as such. The six documents ingested this turn are the public governance snapshot. They are not the full JavaScript runtime.

---

## 1. What “about 4,000 at 7/24/26” means (and what it does not)

Daniel: on **24 July 2026** the website held about **4,000 plus or minus books, products, and items**. That is a **presence on pages** census (cards, images, descriptions, editorial items), not a count of live Amazon links.

He did **not** claim every image already had an affiliate URL. Building was still in process, aimed at launch:

- Many pages were **structure-complete, not link-complete**.
- Complex `tc-*` HTML often required **remaking and resizing** an image after it was placed. Remake **stripped** the attached link. Re-attach had not happened yet.
- Some links were added and **did not stick**.
- Plan after migrate, before public launch: one sweep of animation, formatting, and every affiliate URL (present, active, correct destination). Missing links were a **small pre-launch tweak**, not the catalog.
- Days of labor were **structure, research, and review**. Link polish was not mission-critical for the 25 July migrate.

**Research funnel (owner):** depending on the page, as many as **10 or more** candidates were reviewed for each item that passed the 21-point qualitative metric (literature) or the engineering track (products) and earned a place on the site. A 4,000 on-page count therefore sits on top of a much larger rejected-research pile. The 4,000 figure is already the **survivors of that funnel**, not the hours of review.

REST `amzn.to` counts on this branch (tens to low hundreds per page; 21 live affiliate cards on Computers after the 19 August light rebuild; 2324 media items in September) measure **links and files that still exist after the crash and later recovery**. They are **not** a census of 24 July on-page items. Using them to contradict 4,000 was wrong.

Do not write: “Cursor counted 4,000 unique SKUs.”  
Do not write: “Only X Amazon links, so the catalog was small.”  
Do write: about 4,000 on-page books/products/items at 24 July, many still awaiting link re-attach after image remakes, sitting on a 10-plus-to-one research funnel, plus non-monetized editorial that is not an SKU at all.

---

## 2. Non-monetized and editorial work (missed in earlier commentary)

The site is not only affiliate catalogs. Stage III (document ingested today) governs **literature, editorial, non-monetized pages**, and narrative materials with the **same** qualitative bar as books. Monetization does not relax the standard.

Named in Stage III and in Daniel’s 12 October statement:

- Self-Help and Mental Wellness (healing, suicide-prevention articles, helplines)
- Podcast listings and scripts (AI Mastery Podcast)
- Truth Untold
- **The Ones Who Gave Everything** (editorial hub)
- Other non-monetized pages and long-form articles

**The Ones Who Gave Everything (owner census):**

- More than **278 images**
- One featured person **per week**
- Summarized life’s work of men and women who gave their lives to help others
- About **300-plus people** approved to be featured
- Each person lived in **one file** that itself contained **hundreds of letter-pages**

That hub is labor and media. It does not show up in an `amzn.to` grep. Page id on this branch: `5897`. REST after the crash is not a substitute for those 300 files.

Daniel: he does not have resources to recreate every difference this agent cannot see from live REST. Absence from a post-crash probe is not absence from the 24 July site.

---

## 3. Company-character rules (also not an Amazon count)

Hub-level governance (document ingested today) plus Daniel’s statement: products are banned not only for failing engineering tests. If a company is known for child labor, abuse of women or children, pornography, illegal drugs, or promotion of immorality, **the product, the parent company, and child companies** are banned. Branding included a **full website (several pages)** of rules for companies and consequence levels.

That is part of launch-ready work. It is not captured by overlay-class counts.

---

## 4. The evaluation engine (the work this chat had not accounted for)

Daniel: a one-of-a-kind **unified governance evaluation system**, about **110 days** to build, thousands of lines of HTML and JavaScript, category-specific scoring so a book is not graded like an AI computer or a tablet.

**Authorship (owner, 12 Oct 2026):** Copilot and Copilot Task wrote the **governance content** first. **Cursor Desktop** afterwards wrote the **complex JS and HTML engine**. That is the Standing Brief §12 split. The 4 September Copilot.fun save is the Task-era interactive binder; it is not the Desktop engine. Scan: `08-EVALUATION-ENGINE-REPO-SCAN-2026-10-12.md` §0. Public face of the site: compassionate, evidence-based, not copied star ratings or paid guesswork. Internal 21-point metric is **Stage III literature only**, not the whole professed system.

**What this turn ingested (snapshots, not the full JS runtime):**

| File | What it is |
| --- | --- |
| `II-Master-Engineering-Driven-Evaluation-System-update-2026-08-02.pdf` | Master engineering whitepaper, Draft 2.1.1, dated July 2026 / updated 2 Aug 2026. Dual-stage methodology. ISO, UL, ETL, CSA, FCC, CPSC, DOE, EPA, AES, IEEE, JEDEC, PCI-SIG, AWI, NHLA. Tiers 1–4. Category addenda (woodworking, audio, computing, smart home, lighting). FTC / no paid endorsements. Author D. Reid, ISI Consulting. |
| `Stage-I-Evaluation-Benchmarking-and-Governing-Bodies.docx` | Stage I: map every product category to governing bodies before Stage II scoring. |
| `Stage-III-Qualitative-Eval-Process.pdf` | Stage III v2.1: literature and **non-monetized** editorial. Research typically **five to six candidates per one selected** (Daniel’s later oral figure for products is 10-plus). **21-point** qualitative metric. Direct full read required. Governs books, mental wellness, Ones Who, podcasts, Truth Untold. |
| `Stage-V-Technology-Hub-Evaluation-System.pdf` | Stage V: Technology Hub only (computers, tablets, networking, A/V, storage). Mission-critical components weighted 50–60%. IEEE, JEDEC, UL, FCC, RoHS. |
| `Stage-VI-Workspace-Evaluation-Standards.docx` | Stage VI: desks, chairs, monitor arms, storage, ergonomics. BIFMA, ANSI, AWI, NHLA, ASTM. |
| `Standards-Governance-Compliance-Division-2026-10-12.docx` | Top-level hub governance: three layers (master / hub / page-level). Universal principles: evidence over opinion, standards over marketing. Company-wide scoring model. |

Copies: `docs/legal/source-pdfs/` and `docs/brand-references/selection-standards/ingest-2026-10-12/`.

**Architecture in those docs (three layers, three stages):**

- Layer 1 master governance  
- Layer 2 hub documents (Technology, Workspace, Lighting, Productivity, Self-Help, and the rest)  
- Layer 3 page-level metrics for the individual item  

- Stage I standards mapping (products)  
- Stage II category scoring (engineering **or** qualitative)  
- Stage III page-specific selection  

Literature uses the 21-point qualitative track. Engineered products use ISO/UL/BIFMA-style tracks with **different metrics per industry**. The master PDF states that explicitly (section 10, updated 2 Aug 2026 8:44am): each mechanical category grouping has **separate** engineering criteria.

**What is still not in this snapshot:** the executable JavaScript/HTML engine Daniel describes (thousands of lines, ~110 days). An 11 August ingest on this repo already recorded that the automated UL/ID → grade engine was **not found** in git and was **paused** after the crash (`diagnostics/evaluation-engine-ingest-2026-08-11.md`). These six files are the **specification and public standards**. They prove the system was written as category-specific governance, not a guess-and-copy affiliate script. They do not let this agent compile the JS.

**12 Oct repo scan (see `08-EVALUATION-ENGINE-REPO-SCAN-2026-10-12.md`):** the six Stage files Daniel pointed at as `unified-governance-system_files` are already in `source-pdfs/` (byte-identical). Git **does** hold Evaluation Engine v1 as an **Excel** workbook (`evaluation-engine/TC_Evaluation_Engine_v1.xlsx`, ~180 formulas, copied from the 3 Aug Cloud branch). Git does **not** hold thousands of JS lines. The word “quantum” is not in the CURRENT binder text. If the runtime is a browser save named `unified-governance-system_files`, send the `.html` plus that folder as one zip.

If the site cannot be rebuilt, or is rebuilt without that engine, Daniel’s statement: those **110 days are worthless**. That is a damages category: lost evaluation engine, not only lost product cards.

---

## 5. Launch readiness language

Daniel: the site was about **90% launch-ready** prior to the 25 July migration. Remaining work was confirmation sweeps (animation, formatting, affiliate URLs), not rebuilding hubs, editorial series, or the evaluation engine from zero.

90% is **owner assessment**. This agent did not audit 90%. Do not contradict it with post-crash REST. Do not upgrade it to a measured 90% either. Pair it with: 65-plus WordPress URLs, 3,575 to 6,500-plus letter pages, ~4,000 on-page items, Ones Who 300-plus people / 278-plus images, evaluation Stages I–VI on disk, Customizer CSS bound to Gutenberg and Kadence trees that 10Web then misaligned or wiped.

---

## 6. Counsel sentences

Use:

> About 4,000 books, products, and items sat on the pages as of 24 July 2026. That is not a count of live affiliate links. Many cards were still awaiting link re-attach after required image remakes. Each published item sat on a research funnel of as many as ten-plus candidates that failed the 21-point or engineering bar. Non-monetized editorial (mental wellness, helplines, podcasts, The Ones Who Gave Everything with 300-plus featured lives and 278-plus images) is part of the same site. A multi-stage evaluation engine, documented in Stage I through VI and master governance papers dated July–August 2026, scored products and literature by category against named governing bodies. The 21-point metric is the literature track only. About 110 days of engine work is a separate damages item from lost cards. Live `amzn.to` greps after the crash do not measure that site.

Do not use:

> Only X Amazon links existed, so 4,000 is inflated.  
> The 21-point sheet was the whole engine.  
> Editorial hubs do not count because they are not products.
