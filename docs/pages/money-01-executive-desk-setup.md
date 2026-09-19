# Money Page Punch List — Executive Desk Setup

- URL: https://tcstaging.truth-collective.com/office-workspace-products-and-tools/executive-desk-setup/
- Focus keyword (inferred): executive desk setup
- Audited from live staging by BDM, 2026-07-15. Verify before applying.

## Already correct (leave alone)

- SEO title: "Best Executive Desk Setup For 2026 Standing And Traditional" (has 2026, ~58 chars). Good.
- Meta description present, includes the focus phrase, within length. Good.
- Canonical self-references. Robots index,follow. Good.
- Trusted Selection + FTC pattern present, with the real ftc.gov link. Good.
- TC grade blocks (`tc-grade-block`) and product overlay cards in use. Grades display. Good.
- 20 affiliate links present. Content rules: no em dashes in body (the 15 em dashes are all in CSS comments, not copy). Good.
- One H1 only. Good count.

## Fix, ranked

1. H1 does not match the focus keyword or the brand H1 framework.
   - Current H1: "Premium Ranked Desks for Executives".
   - Brand framework: "Best [category] for [audience]".
   - Change to something like: "Best Executive Desk Setup for Standing and Traditional Workspaces".
     Keep the phrase "executive desk setup" in the H1. This is the single most
     important on-page SEO fix here.

2. Duplicate/generic image alt text. 24 content images, only 17 unique alts; the
   string "Executive Style Desks and Setup" is reused on 7 images.
   - Give every product image a unique, descriptive alt (brand + model + type).
     Several are already good (for example "FlexiSpot E6 Pro Standing Desk 60x27",
     "Vari Classic Electric Standing Desk 60x30"). Fix the 7 generic ones.
   - Keep the focus keyword on the primary/hero image alt only.

3. No product ItemList schema. The page has real TC grades but no structured data
   listing the products.
   - Add a RankMath Custom Schema `ItemList` of the featured desks (name + URL,
     and `brand` where known). Do not add fabricated ratings. If a TC grade is a
     real numeric rating, it may be expressed as a `Review`/`reviewRating` per
     product, authored by Truth Collective, but only using the real grade.
   - Per-product star rich results require dedicated product pages; on this
     listing page ItemList is the correct structured-data type.

4. Internal linking is thin sideways. The "Explore More" row links only to
   Technology Hub and Smart Lighting (2 links, and both are other hubs).
   - Add 3 to 4 sideways links to sibling Office Workspace pages (for example
     Executive Office Chairs and Seating, Office Desk Essential Products, Laptop
     Stands and Accessories). Keep the up-link to the Office Workspace hub.

## Publish gate reminders

- Confirm affiliate disclosure renders in footer.
- Update "Updated June 2026" byline to the current month at publish.
- Mobile check: overlay grades and buttons reachable on touch, not hover-only.
