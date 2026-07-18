# Money Page Punch List — Executive Office Chairs and Seating

- URL: https://tcstaging.truth-collective.com/office-workspace-products-and-tools/executive-office-chairs-seating/
- Focus keyword (inferred): executive office chairs and seating
- Audited from live staging by BDM, 2026-07-15. Verify before applying.

## Already correct (leave alone)

- SEO title: "Top Ranked Executive Office Chairs And Seating For 2026" (has 2026). Good.
- Canonical self-references. Robots index,follow. Good.
- Trusted Selection + FTC pattern present with the real ftc.gov link. Good.
- TC grade blocks and product overlay cards in use. 39 affiliate links. Good.
- No em dashes in body copy (the 15 em dashes are all in CSS comments). Good.

## Fix, ranked

1. NO H1 on the page. This is the most important fix. The page has 19 H2s but
   zero H1 tags.
   - Add a single H1 using the focus keyword and the brand framework, for
     example: "Best Executive Office Chairs and Seating for 2026".
   - Make sure the top heading block is set to Heading 1, not Heading 2.

2. Meta description is too long (~210 characters, over the 160 limit). It will
   truncate in search.
   - Rewrite to under 160 characters, keeping the focus keyword near the front.
     Example: "Top ranked executive office chairs and seating for 2026,
     ergonomic task chairs, guest seating, and premium executive chairs chosen
     for comfort and daily use." (Trim to fit under 160.)

3. Severe duplicate image alt text. 45 content images, only 9 unique alts; the
   string "Top Ranked Executive Office Chairs and Seating" is reused on 35
   images.
   - Give every product image a unique, descriptive alt (brand + model). Some
     are already good ("Haworth Soji Black headrest Office Chair", "BDI Furniture
     Bolo executive office chairs"). Fix the 35 generic ones. This is the biggest
     accessibility and image-SEO gap of the three money pages.

4. Duplicated body sections. These three H2s each appear 3 times on the page:
   "Why These Chairs and Seating Products Made the List", "The Importance of
   Proper Seating and Performance of Chairs", "Best Chairs and Seating for Work
   and Home".
   - Confirm this is intentional sectioning per sub-group and not accidentally
     duplicated content blocks. If duplicated, remove the repeats. Repeated
     identical H2s and copy dilute SEO and read as a mistake.

5. Typo in an H2: "Premium Executive Chase and Lounging Sofas" should be
   "Premium Executive Chaise and Lounging Sofas".

6. No product ItemList schema. Same as the desk page: add a RankMath Custom
   Schema `ItemList` of the featured chairs (name + URL + brand). No fabricated
   ratings; use only real TC grades if expressing a Review.

7. Thin sideways internal linking. Add 3 to 4 sibling Office Workspace links
   (Executive Desk Setup, Office Desk Essential Products, Laptop Stands), keep
   the up-link to the Office Workspace hub.

## Publish gate reminders

- Confirm affiliate disclosure renders in footer.
- Mobile check on overlay grades and buttons.
