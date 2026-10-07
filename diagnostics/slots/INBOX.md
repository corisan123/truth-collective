# Slot inbox

Daniel pastes one hub packet here (or into chat). Claude cannot write to the repo.

Cursor wraps these strings in locked `tc-*` HTML after that page’s skeleton is stable. Cursor does not rewrite voice. Claude’s standing prompt (when it arrives) governs the writing. This file does not.

## Slot names

```
===HUB===
[page title or slug]

===INTRO===
[welcome / hub prose for the intro column]

===STATS===
[three short stat labels/values, facts only]

===WHO_THIS_IS_FOR===
===WHY_THIS_MATTERS===
===BEST_USES===

===TILE_LABELS===
[one line per tile, in visual order]

===EVAL_BRIEF===
[How We Evaluate block]

===FINAL_THOUGHTS===
[Final Word prose]

===END===
```

## Wrapping (Cursor)

| Slot | Lands in |
| --- | --- |
| INTRO | Right column of the asymmetric intro (heading stays in the left column). |
| STATS | Stat strip under intro. Boxed, permitted. |
| WHO_THIS_IS_FOR / WHY_THIS_MATTERS / BEST_USES | Named regions under the stat strip, before listings. |
| TILE_LABELS | Title **on** the tile image (bottom). One label per `tc-explore-hub` tile, same order as the grid. |
| EVAL_BRIEF | Evaluation region **directly above Final Word**. Boxed, permitted. Do not duplicate. |
| FINAL_THOUGHTS | Final Word region. |

Do not wrap until the skeleton on that URL is stable. One paste per hub, not per section.

Page order is locked in `docs/TC-LOCK-2026-09-19.md`.
