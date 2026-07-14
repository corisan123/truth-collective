# Staging Page Inventory

Source of truth: RankMath `page-sitemap.xml` captured 2026-07-14.
Total URLs in sitemap: 66. Staging: https://tcstaging.truth-collective.com

Do not edit the WordPress database in SQL. Menus are rebuilt only through
Appearance > Menus. SQL edits are what crushed the menus before.

## Critical launch blockers found in this inventory

1. Eight pages still live under a `__trashed` parent slug.
   Parent path: `/best-office-workspace-products-tools__trashed/`
   These must be reparented under `/office-workspace-products-and-tools/` and the
   old `__trashed` URLs redirected. Do this in the WordPress Pages UI, not SQL.
2. The AI books hub (`/artificial-intelligence-books/`) returns HTTP 200 but is
   missing from the sitemap. Cause: its canonical points to a 404 URL. Fix the
   canonical to itself first. The hub will then reappear in the sitemap.
3. Duplicate Communication and Persuasion pages both return 200:
   - `/recommended-books-2026/communication-and-persuasion/`
   - `/recommended-books-2026/communication-and-persuasion-books/`
4. Orphan numeric page: `/6751-2/`
5. Broken or messy editorial URLs:
   - `/the-truth-untold-seriespart-2/` (missing hyphen)
   - `/the-truth-collective-series-part-78910/`
6. Never use SQL to fix menus or parents. Use Appearance > Menus and the Page
   Parent dropdown in Quick Edit.

## Hard rule: no SQL

Copilot previously directed SQL edits inside the site database. That crushed the
menus. From this point forward:

- Menus: Appearance > Menus only. Rebuild from the target structure below.
- Parents: Pages > Quick Edit > Parent dropdown only.
- Redirects: RankMath Redirections only.
- Never open phpMyAdmin or run SQL against `wp_posts`, `wp_terms`, or
  `wp_term_relationships`.

See `docs/hub-structure.md` for the authoritative 6 hub + 3 editorial hub
breakdown confirmed directly by Daniel, and `docs/playbooks/02-menu-diagnosis-and-safe-rebuild.md`
for why the menu keeps disappearing (caching, most likely) and how to rebuild it
without SQL.

## Target menu structure (rebuild to this)

Use this as the Appearance > Menus target. Create a new menu named
`Primary Navigation`, assign it to the theme header location, then add items
from Pages. Do not try to salvage the broken menu. Build a fresh one.

### Primary

- Home `/`
- About `/about-the-truth-collective/`
- Getting Started `/getting-started/`
- Recommended Books `/recommended-books-2026/`
  - Leadership Books
  - Communication and Persuasion (pick ONE of the two duplicates)
  - Decision Making and Strategy
  - Wealth Money and Investing
  - Entrepreneurship and Business Building
  - High Performance and Execution
  - Project Management Books
  - Voices of Influence
  - Artificial Intelligence Books `/artificial-intelligence-books/` (must be self-canonical first)
    - AI Books for Beginners
    - AI Books for Business Leaders
    - Foundational AI Books
    - AI Workbooks and Guided Learning
    - Future-Proof AI Books
- Office Workspace `/office-workspace-products-and-tools/`
  - Office Desk Essential Products
  - Laptop Stands
  - Best Digital Smart Tablets
  - plus the eight pages currently trapped under `__trashed` after reparent
- Technology Hub `/technology-hub/`
  - Headphones for Work
  - Computers and Digital Devices
  - Video Technology and Interactive Displays
  - Speakers Home Office Outdoors `/speakers-home-office-outdoors/`
  - Smart Writing Products `/smart-writing-products-tools-essentials/`
- Smart Lighting `/smart-lighting/`
  - Advanced Lighting
  - Smart AI Lighting Devices
  - Smart Lighting Controls
  - Smart Security Lighting and Cameras
  - Smart Bulbs Light Strips `/smart-bulbs-light-strips/`
- Self-Help and Mental Wellness `/self-help-and-mental-wellness/`
  - Mental Wellness Books
  - Self-Help Books `/self-help-books/`
  - Meditation Essentials `/meditation-essentials-calm-rest-reset/`
  - Mental Health Support Services (non-monetized)
  - Mental Wellness Support Resources (non-monetized)
  - Mental Wellness Resources / Podcasts (non-monetized)
- The Truth Untold `/the-truth-untold/`
  - Parts 1 through 5 (fix the broken part-2 slug separately)
- AI Mastery Podcast Collection `/ai-mastery-podcast-collection/`
- Ones Who Gave Everything `/ones-who-gave-everything/`
- Product Selection Standards `/product-selection-standards/`
- Affiliate Disclosure `/affiliate-disclosure/`
- Contact `/contact/`
- Privacy Policy `/privacy-policy-2/`

## Full sitemap list by group

### Recommended Books (10)

- recommended-books-2026
- recommended-books-2026/leadership-books
- recommended-books-2026/communication-and-persuasion
- recommended-books-2026/communication-and-persuasion-books
- recommended-books-2026/decision-making-strategy
- recommended-books-2026/wealth-money-and-investing
- recommended-books-2026/entrepreneurship-and-business-building
- recommended-books-2026/high-performance-execution
- recommended-books-2026/project-management-books
- recommended-books-2026/voices-of-influence-2

### Artificial Intelligence Books children (5 in sitemap; hub missing)

- artificial-intelligence-books/ai-books-for-beginners-2
- artificial-intelligence-books/ai-books-for-business-leaders
- artificial-intelligence-books/foundational-ai-books
- artificial-intelligence-books/ai-workbooks-and-guided-learning
- artificial-intelligence-books/future-proof-the-ai-books-that-redefine-work-skill

Note: the old top-level `/ai-books-for-business-leaders/` now 301-redirects to
the nested URL. Hierarchy is corrected. Update playbooks to the nested URL.

### Office Workspace (4 clean + 8 trashed)

Clean:

- office-workspace-products-and-tools
- office-workspace-products-and-tools/office-desk-essential-products
- office-workspace-products-and-tools/laptop-stands-for-work
- office-workspace-products-and-tools/best-digital-smart-tablets

Trapped under `__trashed` parent (all still HTTP 200):

- .../executive-office-chairs-seating
- .../office-file-cabinets-credenzas-essentials
- .../best-analog-writing-tools
- .../monitor-display
- .../cable-management
- .../executive-desk-setup
- .../audio-and-video
- .../projectors-and-microphones

### Technology Hub (4)

- technology-hub
- technology-hub/headphones-for-work
- technology-hub/computers-digital-devices
- technology-hub/video-technology-and-interactive-displays

### Smart Lighting (5 + 1 related orphan)

- smart-lighting and four children
- smart-bulbs-light-strips (top-level, should hang under Smart Lighting)

### Self-Help and Mental Wellness

- self-help-and-mental-wellness
- self-help-and-mental-wellness/mental-wellness-books
- self-help-books
- meditation-essentials-calm-rest-reset
- mental-health-support-services-and-helplines
- mental-wellness-support-resources
- mental-wellness-resources

### Editorial

- the-truth-untold and parts 1, 3, 4, 5
- the-truth-untold/the-truth-about-corporate-america-part-2
- the-truth-untold-seriespart-2 (broken slug)
- the-truth-collective-series-part-78910
- ai-mastery-podcast-collection
- ones-who-gave-everything and reverend-billy-graham

### Other top-level

- speakers-home-office-outdoors
- smart-writing-products-tools-essentials
- interactive-digital-displays-2
- product-selection-standards
- affiliate-disclosure
- about-the-truth-collective
- getting-started
- contact
- privacy-policy-2
- 6751-2 (orphan)

### Live but missing from sitemap (verify after canonical fixes)

- artificial-intelligence-books (200, wrong canonical)
- productivity-tools (200)

## Ranked next actions from this inventory

1. Fix AI hub canonical to itself so it returns to the sitemap.
2. Rebuild the Primary menu from the target structure above. Fresh menu, not a repair of the crushed one.
3. Reparent the eight `__trashed` office pages under Office Workspace using Quick Edit. Then add RankMath redirects from the old `__trashed` URLs.
4. Resolve the Communication and Persuasion duplicate. Keep one, redirect the other.
5. Decide the fate of `/6751-2/` (noindex and hide, or identify and rename).
