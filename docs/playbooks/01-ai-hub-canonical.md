# Playbook 01 — Fix AI Hub Canonical (Launch-Gate, Not an Emergency)

## Corrected urgency (per Daniel, 2026-07-15)

Staging is noindexed (`robots.txt: Disallow: /`), so nothing here is indexed by
Google today. This is NOT a live traffic emergency. It is a launch-gate item: it
must be correct before or at migration, because the bug travels to live.

## The problem

`/artificial-intelligence-books/` sets its canonical to
`/ai-mastery-collection-2026-editorial-series/`, which returns HTTP 404. The hub
is excluded from the RankMath sitemap as a result.

## Why it still must be fixed, even though staging is not indexed

Migration to live does a search-replace of `tcstaging.truth-collective.com` to
`truth-collective.com` across the database. The broken canonical does not fix
itself; it becomes `https://truth-collective.com/ai-mastery-collection-2026-editorial-series/`,
still a 404, now on the live site, and the sitemap exclusion carries over too. So
if left alone, the site launches with one of six hubs canonicalizing to a dead
URL and missing from the sitemap submitted to Google Search Console.

## The correct fix (do NOT hardcode any URL)

Do not type a `tcstaging` URL into the canonical field. That URL disappears at
migration. Instead, CLEAR the field so RankMath self-canonicals automatically.
This is correct on staging (self-references the staging URL) and automatically
correct after migration (self-references the live URL), with zero rework.

### Steps (requires WordPress login; BDM cannot do this, it is behind admin auth)

1. WordPress admin, open the Artificial Intelligence Books page.
2. Open the RankMath panel, Advanced tab.
3. Canonical URL field: delete its contents, leave it EMPTY. Do not paste a URL.
4. Update the page.
5. Open RankMath Schema on the page. If a CollectionPage schema URL points to the
   editorial-series 404 URL, clear or correct it the same way.
6. Update.
7. Tell BDM. BDM will re-check the live canonical and sitemap inclusion.

## Broader migration principle (applies site-wide)

Prefer empty/self-referencing canonicals over hardcoded URLs everywhere, so the
migration search-replace does not leave stale absolute URLs behind. Only hardcode
a canonical when intentionally pointing one page at a different page.

## Do not

- Do not hardcode a `tcstaging` canonical.
- Do not change the slug.
- Do not point the canonical at `/ai-mastery-podcast-collection/`.
- Do not use SQL.
- Do not delete the editorial/podcast page.

## Done when

- Canonical is empty (self-referencing) or points to the hub's own URL.
- Hub appears in `page-sitemap.xml`.
