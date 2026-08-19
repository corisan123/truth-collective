# Semrush readiness — Truth Collective staging (2026-08-19)

**Site:** https://tcstaging.truth-collective.com  
**Published pages crawled:** 59  
**Data:** `diagnostics/semrush-readiness-2026-08-19.json`

## Do this before submitting to Semrush

1. **Restore Cursor secrets** `TC_WP_USER` + `TC_WP_APP_PASSWORD` and run:
   `python3 diagnostics/scaffolds/apply-tech-children-light-batch.py`
   That applies Computers + all Technology Hub children with dimension placeholders and single-H1 shells.
2. **Replace placeholders** with final images at the sizes printed on each slot (1600×1000 heroes/tiles, 1200×750 product cards). Prefer Media Library JPG/WebP over SVG data URIs for the audit.
3. **Fix known 404:** `/featured-productivity-tools/` (linked from at least one hub path). Point to `/productivity-tools/` or remove.
4. **Amazon Associates:** links retained for reapply at launch; Semrush may note affiliate patterns. Disclosure copy is on rebuilt product pages.

## Light-rebuilt hubs (already live)

Technology Hub, Smart Lighting, Office, Books, Self-Help, Productivity, Ones Who Gave, Truth Untold, AI Podcast, Billy Graham tribute.

## Ready to apply (scaffolds in repo, not live until REST)

| Page ID | Page |
|---------|------|
| 359 | Computers and Digital Devices |
| 121 | Monitors and Displays |
| 117 | Audio and Video |
| 1420 | Headphones and Headsets |
| 1449 | Desk Speakers |
| 5940 | Projectors and Microphones |
| 1098 | Digital Smart Tablets |
| 5784 | Interactive Digital Displays |

## SEO flags from public crawl (fix after apply)

- Multiple or zero H1 on many child pages (listed in JSON)
- Home has 2× H1
- Several book/office children missing H1
- Meta descriptions: present on crawled pages (Rank Math)

## Suggested Semrush project settings

- Property: `https://tcstaging.truth-collective.com` (staging) **or** wait until live domain if you want production scores only
- Crawl: all subfolders; include `/technology-hub/`, `/recommended-books-2026/`, `/office-workspace-products-and-tools/`
- After apply + image replace, re-crawl before treating scores as launch-ready

## Applied 2026-08-19 (staging REST)

- Technology children (Computers + monitors / AV / headphones / speakers / projectors / tablets / interactive displays)
- Smart Lighting children (4863, 4877, 4896, 5099, 4886) — see `REST-smart-lighting-children-apply-2026-08-19.md`
- Dual H1 cleared on Productivity, Ones Who Gave, AI Podcast via Astra `site-post-title=disabled`

## Next page batches

1. Office children (chairs, desks, analog writing, essentials, laptop stands, filing)
2. Book category children
3. Self-Help / Productivity children
4. Home + About + Contact cleanup
