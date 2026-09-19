# Money Pages — Shared Findings and Batch Plan

Audited from live staging by BDM, 2026-07-15. The three launch money pages:

- Executive Desk Setup (`docs/pages/money-01-executive-desk-setup.md`)
- Executive Office Chairs and Seating (`docs/pages/money-02-executive-office-chairs.md`)
- Monitors and Premium Displays (`docs/pages/money-03-monitors-and-displays.md`)

## Overall verdict

These pages are in good shape structurally. They already have the hard parts
right: self-canonicals, indexable robots, 2026 titles, the Trusted Selection and
FTC pattern, real TC grade blocks, product overlay cards, and affiliate links.
No em dashes in body copy (only in CSS comments). This is strong work.

## The shared fixes (do these as a batch across all three)

1. Image alt text is the biggest common gap. All three reuse one generic alt
   across most product images:
   - Desk: 7 of 24 images share one alt.
   - Chairs: 35 of 45 images share one alt (worst case).
   - Monitors: 20 of 27 images share one alt.
   Fix: unique, descriptive alt per product image (brand + model + type). Focus
   keyword stays on the hero image alt only. This is accessibility + image SEO,
   and for a product site it also helps Google Images traffic.

2. Product ItemList schema is missing on all three. Each has real TC grades but
   no structured data listing the products. Add a RankMath Custom Schema
   `ItemList` per page (product name + URL + brand). Use only real TC grades if
   expressing a Review; never fabricate ratings. Per-product star rich results
   need dedicated product pages; ItemList is correct for these listing pages.

3. Sideways internal linking is thin. All three have an "Explore More" row that
   points to other hubs but few or no same-hub siblings. Add 3 to 4 sibling
   links within the same hub on each page.

## Page-specific must-fixes

- Chairs: NO H1 on the page (add one with the focus keyword). Meta description
  over 160 chars (trim). Possible duplicated body sections (3x repeated H2s),
  confirm intentional. Typo "Chase" should be "Chaise".
- Desk: H1 is off-framework and missing the focus keyword (rewrite to include
  "executive desk setup").
- Monitors: cleanest of the three; only the alt text and ItemList items apply.

## Suggested batch order

1. Chairs first (it has the H1 gap, the meta length issue, and the worst alt
   problem, so highest impact).
2. Desk second (H1 rewrite + alts).
3. Monitors third (alts + ItemList only).

Then apply the shared ItemList schema and sibling-link additions across all three
in one pass. This is the "fix the template once" approach from the launch plan.
