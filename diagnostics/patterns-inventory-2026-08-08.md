# WordPress Patterns inventory — 2026-08-08

**Source:** Staging REST `GET /wp-json/wp/v2/blocks` (Application Password)  
**Count:** **23** (matches Daniel)  
**Status:** Queued for later — **do not hand-edit now.** Cursor (+ Task/Claude under tickets) will repair/polish after Phase S priorities.

## Daniel notes (locked)
- Patterns hold documents / section systems he built; many URL links broke after the crash.
- He started editing Patterns, then correctly stopped — later AI pass will be faster and cleaner.
- Word/PDF source docs also exist on his computer (offline archive).
- **Homepage links:** Daniel confirms **all homepage links work now** (View). Optional leftover content cleanup (e.g. any stale `featured-productivity-tools` string in raw HTML) is not urgent if View is good.

## Pattern list (id · title · href count · modified)

| ID | Title | hrefs | Modified |
|----|-------|------:|----------|
| 2870 | Explore More Template | 0 | 2026-08-08 |
| 7837 | Final AI Mastery Collection Podcast Series Pattern | 1 | 2026-07-22 |
| 7688 | HTML Selection Evaluation Process | 0 | 2026-07-13 |
| 7532 | SOCIAL MEDIA | 0 | 2026-07-22 |
| 2859 | TC Grade 3.5 of 5 | 0 | 2026-04-25 |
| 2857 | TC Grade 4 of 5 | 0 | 2026-04-25 |
| 2855 | TC Grade 4.5 of 5 | 0 | 2026-04-25 |
| 2853 | TC Grade 5 of 5 | 0 | 2026-04-25 |
| 6918 | Technical Benchmark Whitepaper (Copy) | 0 | 2026-07-22 |
| 6747 | Technical Benchmarking Selection Process Overvfew | 0 | 2026-07-05 |
| 7836 | The Ones Who Gave Everything Tribute Series | 2 | 2026-07-22 |
| 5542 | Truth Box | 0 | 2026-06-28 |
| 2847 | Truth Collective's Trusted Selection Standards Governance and Official Documentation | 1 | 2026-07-23 |
| 8152 | … Trusted Selection Standards … (Copy) | 1 | 2026-07-23 |
| 8156 | … Trusted Selection Standards … (Copy) (Copy) | 1 | 2026-07-23 |
| 7827 | Truth Untold Series Block | 2 | 2026-07-22 |
| 7648 | Truth-Collective | 10 | 2026-08-08 |
| 4159 | Upper Body Group 2 | 0 | 2026-05-22 |
| 8057 | White Paper Benchmarking | 0 | 2026-07-23 |
| 8066 | White Paper Benchmarking (Copy) | 0 | 2026-07-22 |
| 5545 | revised Why Truth Collective | 2 | 2026-07-21 |
| 7672 | social media icons | 0 | 2026-07-14 |
| 5546 | tc overlay card | 0 | 2026-06-09 |

## Quick link scan (patterns only)
- Unique internal-ish `href`s across all 23: **13**
- Public HTTP check of those URLs on this pass: **0 hard 404s**
- That does **not** mean Patterns are polish-ready. Crash damage can still be: wrong-but-200 URLs, missing classes, stale copies on pages that are **unsynced**, duplicate “(Copy)” patterns, or content that needs voice/HTML rebuild.

## How we will do this later (not now)

**Phase:** after homepage/hub stabilize + flicker plan; fits **Phase R / polish**.

| Step | Who |
|------|-----|
| Export each pattern via REST; backup to `diagnostics/patterns/` | Cursor |
| Map every href → current published page (slug/id) | Cursor |
| Fix wrong URLs in **synced** patterns first (one pattern = many pages) | Cursor REST |
| Claude: voice pass on prose patterns only when ticketed | Claude |
| Task: HTML scaffold rebuilds only when Cursor tickets `HTML-pattern-*` | Copilot Task |
| Deduplicate obvious Copy/Copy patterns with Daniel Approve | Cursor + Daniel |
| Optional: Daniel drops Word/PDF into repo or chat when a pattern needs source truth | Daniel |

**Do not:** Daniel hand-edit all 23. Do not paste Word docs into Additional CSS. Do not let Task/Edge become pattern lead.

## Ticket stubs (future)
- `REST-patterns-link-audit` — full href map + 404/wrong-target report  
- `REST-pattern-{id}-links` — one pattern URL repair  
- `COPY-pattern-{id}` — Claude voice  
- `HTML-pattern-{id}` — Task scaffold if structure destroyed  

## Priority vs other work
1. Keep staging visual/CSS recovery moving (flicker, Computers, hubs)  
2. Patterns URL/polish pass as a **batch factory** once REST rhythm is proven  
3. Word/PDF = reference when a pattern’s intent is unclear — not required to start the audit  
