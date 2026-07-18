# Prep — The Truth Untold Series (content paste + slug fix)

Audited from live staging by BDM, 2026-07-15, to make Daniel's content paste
smooth. Daniel has 6 series posts to paste into already-built pages.

## Current state of the 6 parts

| Part | URL | Body words | State |
| --- | --- | --- | --- |
| Hub | `/the-truth-untold/` | ~2156 | Built out. |
| Part 1 | `/the-truth-untold/the-truth-untold-series-part-1/` | ~77 | Empty stub, ready for paste. |
| Part 2 | `/the-truth-untold/the-truth-about-corporate-america-part-2/` | ~534 | Has content already. Confirm final. |
| Part 3 | `/the-truth-untold/the-truth-untold-series-part-3/` | ~89 | Empty stub, ready for paste. |
| Part 4 | `/the-truth-untold/the-truth-untold-series-part-4/` | ~89 | Empty stub, ready for paste. |
| Part 5 | `/the-truth-untold/the-truth-untold-series-part-5/` | ~86 | Empty stub, ready for paste. |
| Part 6 | `/the-truth-untold-seriespart-2/` | ~216 | Broken slug, not nested under the hub. See below. |

## Fix BEFORE pasting: the Part 6 slug and nesting

The page titled "Part 6" has slug `the-truth-untold-seriespart-2`:
- The slug is malformed (missing hyphen, and says "part-2" though the title is Part 6).
- It is top-level, not nested under `/the-truth-untold/` like the others.

Because staging is not indexed yet, the slug can still be corrected cleanly now
with no SEO cost. Do this before launch:

1. Open the Part 6 page in WordPress.
2. Set Parent to The Truth Untold (so it nests under `/the-truth-untold/`).
3. Change the slug to `the-truth-untold-series-part-6`.
4. Update. RankMath will create a redirect from the old URL automatically.
5. Result URL: `/the-truth-untold/the-truth-untold-series-part-6/`.

## Paste checklist for each part (keeps content on-brand)

When pasting each post, confirm against the Master Brief:
- No em dashes. No contractions. No bold in body. No exclamation points. No hype.
- One H1 per page, ideally the part title with the series name.
- Focus keyword in SEO title (include 2026 where natural), meta under 160, H1,
  first paragraph, and one H2.
- Internal links: up to `/the-truth-untold/` hub, and sideways to 2 to 3 other
  parts.
- These are editorial pages. They are primary LinkedIn content and secondary
  Pinterest. They can carry pins (they are not the non-monetized help pages).
- After pasting, purge both caches and verify in a private window.

## Note

Part 2's slug (`the-truth-about-corporate-america-part-2`) is descriptive and
fine. No change needed there. Only Part 6 needs the slug and nesting fix.
