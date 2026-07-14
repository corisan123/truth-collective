# Playbook 01 — Fix AI Hub Canonical (Urgent)

This is the highest-priority site-wide fix. Do it first.

## Why

`/artificial-intelligence-books/` returns HTTP 200, but its canonical is set to
`/ai-mastery-collection-2026-editorial-series/`, which returns HTTP 404.
Because of that, the hub is missing from the RankMath sitemap. Fixing the
canonical puts the hub back into crawl and indexing readiness.

## Exact steps (WordPress admin)

1. Go to Pages.
2. Find and open **Artificial Intelligence Books** (or AI Mastery Book Collection).
3. Open the RankMath panel on the page.
4. Open the Advanced tab.
5. In Canonical URL, replace the current value with exactly:

```
https://tcstaging.truth-collective.com/artificial-intelligence-books/
```

Or clear the Canonical URL field so RankMath self-canonicals to the page URL.
6. Save / Update the page.
7. Open RankMath Schema on the same page. If a CollectionPage schema exists and
   its URL field points to the editorial-series URL, change that URL to:

```
https://tcstaging.truth-collective.com/artificial-intelligence-books/
```

8. Update again.
9. Hard refresh the live staging page and confirm View Source shows:

```
<link rel="canonical" href="https://tcstaging.truth-collective.com/artificial-intelligence-books/" />
```

10. Wait a few minutes, then open:

```
https://tcstaging.truth-collective.com/page-sitemap.xml
```

Confirm `/artificial-intelligence-books/` appears in the sitemap.

## Do not do

- Do not change the page slug.
- Do not point the canonical at `/ai-mastery-podcast-collection/`.
- Do not use SQL.
- Do not delete the editorial/podcast page.

## Done when

- Canonical equals the hub URL.
- Hub appears in `page-sitemap.xml`.
- Editorial/podcast page remains separate at `/ai-mastery-podcast-collection/`.
