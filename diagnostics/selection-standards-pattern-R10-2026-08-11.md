# Selection Standards pattern R10 (Claude SPEC) — 2026-08-11

**Applied to:** `2847`, `8152`, `8156`  
**Scaffold:** `diagnostics/scaffolds/pattern-2847-selection-standards-R10.html`  
**Apply script:** `diagnostics/scaffolds/apply-pattern-2847-R10.py`  
**Backups:** `diagnostics/backups/pattern-{2847,8152,8156}-before-R10-2026-08-11.html`

## Claude SPEC addressed
1. Removed redundant navy title restatement banner (kept one kicker + one Playfair title).
2. Broke body into shorter sections with pull quote, 2-track stat, and divider.
3. Restyled Stage I/II/III as sequential steps (`01`/`02`/`03` + gold connecting thread), not three identical navy CTAs.
4. No raw `style="display:flex..."` markup. Layout uses `tc-standards-pattern*` classes only. Synced old copies 8152/8156 that still had inline grade flex HTML.

## Stage targets (unchanged)
| Stage | Target |
|-------|--------|
| I | Technical Benchmarking PDF |
| II | `/6751-2/` |
| III | Interim `/product-selection-standards/` |

## Claude follow-up (yes)
Public pattern copy should be checked against the internal governance binder so the public summary and internal docs do not drift. Cursor handles structure/CSS; Claude owns that voice/governance alignment pass.
