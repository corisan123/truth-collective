# Slot inbox

Daniel pastes one hub packet here (or into chat). Claude cannot write to the repo.

Cursor wraps these strings in locked `tc-*` HTML after that page’s skeleton is stable. Cursor does not rewrite voice. Claude’s standing prompt (when it arrives) governs the writing. This file does not.

## Slot names

```
===HUB===
[page title or slug]

===INTRO===
[welcome / hub prose]

===EVAL_BRIEF===
[How We Evaluate block]

===TILE_LABELS===
[one line per tile, in visual order]

===FINAL_THOUGHTS===
[closing prose]

===END===
```

Optional later, same packet, only if that page needs them:

```
===HERO_KICKER===
===STATS===
```

## Wrapping (Cursor)

| Slot | Lands in |
| --- | --- |
| INTRO | Constrained prose under the cover (`tc-tech-intro-prose` / `tc-leadership-body` as the skeleton already uses). Not a second hero. |
| EVAL_BRIEF | Existing evaluation brief region. Do not duplicate if the 19 Sep brief is already on that hub. |
| TILE_LABELS | Title **on** the tile image (bottom). One label per `tc-explore-hub` tile, same order as the grid. |
| FINAL_THOUGHTS | Closing region already on the skeleton. |

Do not wrap until the skeleton on that URL is stable. One paste per hub, not per section.
