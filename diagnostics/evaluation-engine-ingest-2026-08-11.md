# Evaluation engine ingest (2026-08-11)

Daniel uploaded the summary pack Cursor / Copilot used for the weighted grading system. He cannot locate the Cursor code that was supposed to replace the manual spreadsheets.

## Files saved
| File | Repo path |
|------|-----------|
| TC Master Summary Document (Cursor Copy).xlsx | `docs/brand-references/selection-standards/TC-Master-Summary-Document-Cursor-Copy.xlsx` |
| Standards, Governance & Compliance Division.docx | `docs/brand-references/selection-standards/Standards-Governance-Compliance-Division.docx` |
| Multistage Engineering Evaluation Overview.docx | `docs/brand-references/selection-standards/Multistage-Engineering-Evaluation-Overview.docx` |
| Multistage PDF (earlier) | `docs/brand-references/selection-standards/multistage-engineering-overview-II.pdf` |
| **Governance Binder Part I (finished evaluations)** | `docs/brand-references/selection-standards/TC_Governance_Binder_PartI_edited.docx` — see `diagnostics/governance-binder-part-I-ingest-2026-08-11.md` |

## What the xlsx is
Manual Copilot workbook (9 sheets), not the automated engine:

1. Cover / version (v2.1ABB, 2026-08-01)  
2. **Engineering Scoring** — component rows + Weight 0–10 + Product Score + Weighted Score + Pass/Fail + Compliance body (UL/CE/ISO/…)  
3. **Editorial Scoring** — 21-ish qualitative metrics (author authority, accuracy, ethics, …)  
4. **Compliance Checklist** — UL, ETL, CSA, FCC, CE, RoHS, ISO, category-specific, editorial bodies  
5. **Cat. Benchmark Set** — desks/speakers/lighting/automation/computing thresholds  
6. **Page-Lvl Eval Sheet** — product / editorial / book page requirements  
7. **Weighted Scoring Model** — Engineering 0.6 / Editorial 0.4 (sheet formula broken: `#NAME?`)  
8. **Mission-Critical Component Mat.**  
9. **Standards & Compliance**

This is exactly the “too involved / type everything manually” path Daniel rejected.

## Intended Cursor automation (from Standing Brief §12 + Daniel)
**Input:** product/book **URL or ID** (Daniel also says UL # / ID #)  
**Output (public-facing only):**
- Short description / summary  
- TC grade / rank  
- SVG stars (or locked `tc-grade-block`)  
- Reasons to buy / avoid style brevity  

**Not shown to consumers:** internal weights, formulas, code (Overview §9).

**Tracks:**
- **Quantitative** → physical products (engineering sheets + compliance)  
- **Qualitative** → books, podcasts, editorial scripts (21-point editorial sheet)

## Code status in this repo
**Not found.** No UL/ID → grade Python/JS engine in `truth-collective` on this branch or obvious git history from recovery commits.  
Standing Brief **§12** marks the technical evaluation engine as **paused** after the site crash (“resume after staging is stable”).

Likely locations if it still exists elsewhere:
- An older Cursor chat / Cloud Agent run not committed  
- A different branch or local download on Daniel’s machine  
- Copilot Task artifact only (Master Binder share), not WP code  

## Governance hierarchy (from docs)
1. Master Governance (Compliance Division doc)  
2. Hub / category standards  
3. Page-level selection metrics  

Triple-stage: Standards bodies → Category scoring → Page-specific metrics.

## Full master document — paced chunks
Part I received 2026-08-11 (`TC_Governance_Binder_PartI_edited.docx`). Continue in chunks only (Part II+, hub docs). Do not request the entire unfinished binder at once.

## Next (when Daniel is ready)
1. Keep uploading if the Cursor code zip/file turns up.  
2. Until then: finish staging page/patterns (Selection Standards light pattern already started on 2847).  
3. Resume engine as a **separate workstream** after Tech Hub + key patterns are stable — rebuild from these sheets if the original code never resurfaces: URL/ID in → summary + `tc-grade-block` out.  
4. Accept the rewritten master later in chunks only.
