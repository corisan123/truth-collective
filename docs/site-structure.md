# Truth Collective — Site Structure and Hierarchy

Captured from live staging on 2026-07-14. Reverify before relying on any URL.
Purpose: give every session the true page hierarchy so schema and internal links
use correct, canonical parents. Do not guess a parent. Use this file.

## Books hierarchy (schema intent)

Per the Master Brief, AI Mastery Collection is a category within Recommended
Books. The intended parent, child, sub-child chain is:

- Home
  - Recommended Books hub: https://tcstaging.truth-collective.com/recommended-books-2026/
    - Artificial Intelligence Books (AI Mastery Collection) hub: https://tcstaging.truth-collective.com/artificial-intelligence-books/
      - AI book category and topic pages (sub-children)

Rule: in schema `isPartOf` and in internal parent links, always use the parent's
own canonical URL. See the open canonical issue below before wiring these.

## Artificial Intelligence Books hub

- Parent of the AI child books: https://tcstaging.truth-collective.com/artificial-intelligence-books/
- This is the AI books landing page. It must be self-canonical.
- It also contains an intro section for the editorial and podcast series, but that
  series lives on its own separate page (see Editorial and podcast parent below).
- Will also host a new podcast and a new blog after launch.

## Editorial and podcast parent page

- Live URL, self-canonical, HTTP 200: https://tcstaging.truth-collective.com/ai-mastery-podcast-collection/
- Title: AI Mastery Collection | Podcast. Top level in WordPress (no parent).
- SEO title: "AI Mastery Podcast and Blog Series | Truth Collective 2026".
- Focus keyword: AI Mastery Podcast. Robots: Index.
- This is the parent for the editorial and podcast series and the future blog.
- Note: the old URL `/ai-mastery-collection-2026-editorial-series/` returns HTTP 404. It is not a live page. Do not link to it or canonicalize to it.
- Minor copy fix in the SEO description: "an editorial series covers AI" should read "an editorial series that covers AI".

Known children (menu, URL-nested under the hub):

- https://tcstaging.truth-collective.com/artificial-intelligence-books/ai-for-leaders-and-thinkers/
- https://tcstaging.truth-collective.com/artificial-intelligence-books/ai-workbooks-and-guided-learning/
- https://tcstaging.truth-collective.com/artificial-intelligence-books/foundational-ai-books/
- https://tcstaging.truth-collective.com/artificial-intelligence-books/future-proof-the-ai-books-that-redefine-work-skill/

AI book pages are now nested under the hub (verified 2026-07-14):

- https://tcstaging.truth-collective.com/artificial-intelligence-books/ai-books-for-business-leaders/ (page id 7739; old top-level URL 301-redirects here)
- https://tcstaging.truth-collective.com/artificial-intelligence-books/ai-books-for-beginners-2/

See `docs/page-inventory.md` for the full 66-URL inventory, the eight
`__trashed` office pages, and the safe menu rebuild target.

## Open issues on the AI hub (fix before publish)

1. Canonical bug: RESOLVED 2026-07-15. `/artificial-intelligence-books/` now
   self-canonicals and is back in the sitemap (verified live). The editorial and
   podcast page remains separate and self-canonical at
   `/ai-mastery-podcast-collection/`. Children `isPartOf` uses
   `https://tcstaging.truth-collective.com/artificial-intelligence-books/`.
   Still to do when schema is added: confirm the hub's RankMath CollectionPage
   schema `url` also references the hub itself, not the old editorial URL.
2. Multiple H1s. The hub page renders more than one H1 (theme entry title plus two
   content H1s). Reduce to a single H1. Keep one hub H1, demote the rest to H2.
3. Topic duplication. `/ai-books-for-business-leaders/` (7739) and
   `/artificial-intelligence-books/ai-for-leaders-and-thinkers/` (101) target
   nearly the same phrase. Differentiate or consolidate to avoid cannibalization.
