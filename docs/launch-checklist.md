# Launch Checklist and Top-Tier Gap List

Synthesized from the 2026-06-29 Cursor launch tips and the Master Brief. Use this
alongside the Publish Gate in `MASTER-BRIEF.md`.

## Status snapshot (keep updated)

- Roughly 65 pages optimized on staging, about 25 remaining at the time of the tips.
- Protect the finished pages. Do not reparent or change slugs without a URL map.

## Migration mechanics (staging to live)

- Live truth-collective.com is being replaced by the staging build. Migration
  does a database search-replace of `tcstaging.truth-collective.com` to
  `truth-collective.com`.
- Bugs travel with migration. A broken canonical, a hardcoded staging URL, or a
  sitemap exclusion on staging becomes the same bug on live. Fix structural
  issues before or at migration, not after.
- Prefer empty/self-referencing canonicals over hardcoded URLs site-wide, so the
  search-replace never leaves stale absolute URLs behind.
- After migration: flip robots to allow crawling, uncheck Discourage search
  engines, purge all caches, submit the sitemap in Google Search Console.

## Launch blockers (must be true before migrating to live)

- robots is not blocking the site.
- Sitemap loads with HTTP 200, not 500.
- No `__trashed` URLs in the tree.
- No duplicate hub titles (the old Communication and Persuasion type issue).
- Hub and child URL map exists, even if some children are thin.
- Redirect plan is ready for old live URLs at cutover.
- Broken parent IDs and orphan pages are resolved.

## High-impact polish before launch

1. Breadcrumbs via RankMath or the theme, hub to category to page.
2. One hub tile template everywhere: three columns, `tc-overlay-card` plus
   `tc-explore-hub`, image then H3 then one-line blurb, whole tile linked.
3. A How We Grade micro-block on child pages, linking to the Selection Standards.
4. FAQ block plus FAQ schema on large category pages, two to four real questions.
5. Related categories footer on each child, at least three internal links.
6. Mobile check on overlay cards. Hover is not tap. Titles must be readable
   without hover, and EXPLORE and grades must be reachable on touch.
7. LiteSpeed purge after CSS or block changes so staging matches what is served.

## Top 1% gap list (where the site is strong and where to close gaps)

- Trust and E-E-A-T: strong. Selection Standards, grades, disclosure in place.
- Hub to child architecture: improving. Finish orphan and reparent work.
- Search-intent titles and slugs: good on many pages. Keyword first, include the year and type.
- Internal linking: weak on some pages. Every page links up and sideways.
- Schema: needs a consistent pass on all pages, parent, child, sub-child.
- Crawlability: fix robots and sitemap before any SEMrush run and before cutover.
- Consistency: lock one card system and one hub template site-wide.
- Content depth: the card and grade system is above average when complete.

## Speakers hub (planned, decisions still open)

The office and desk speakers page is being broadened into a speakers-by-type hub
with about 20 child categories. Before building 20 tiles, three decisions are
needed from Daniel: the hub working title, the slug (do not lock to
office-desk-speakers if scope is all speaker types), and the parent (Technology
Hub or Office Workspace). Then clone one master tile across all children, create
child stubs so no EXPLORE link 404s, and run RankMath on the hub and each child.

## Model choice

Use the highest reasoning model for architecture, SEO, migration, and audits.
Use a fast model for repetitive paste, CSS snippets, and single-page fixes once
the plan is locked.
