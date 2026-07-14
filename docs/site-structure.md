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

- URL given by Daniel as the parent of the AI child books: https://tcstaging.truth-collective.com/artificial-intelligence-books/
- Will also host a new podcast and a new blog after launch.

Known children (menu, URL-nested under the hub):

- https://tcstaging.truth-collective.com/artificial-intelligence-books/ai-for-leaders-and-thinkers/
- https://tcstaging.truth-collective.com/artificial-intelligence-books/ai-workbooks-and-guided-learning/
- https://tcstaging.truth-collective.com/artificial-intelligence-books/foundational-ai-books/
- https://tcstaging.truth-collective.com/artificial-intelligence-books/future-proof-the-ai-books-that-redefine-work-skill/

Related AI pages that are top level in WordPress (URL not nested under the hub):

- https://tcstaging.truth-collective.com/ai-books-for-business-leaders/ (page id 7739)
- https://tcstaging.truth-collective.com/ai-books-for-beginners-2/ (page id 7721)

## Open issues on the AI hub (need resolution before it is the indexed parent)

1. Canonical conflict (high priority). `/artificial-intelligence-books/` sets its
   canonical to `https://tcstaging.truth-collective.com/ai-mastery-collection-2026-editorial-series/`.
   Effect: Google is told the canonical hub is the editorial-series URL, not
   `/artificial-intelligence-books/`. Decision required: which URL is the real,
   indexed AI hub. Then make that page self-canonical and point children's
   `isPartOf` at that same canonical URL.
2. Multiple H1s. The hub page renders more than one H1 (theme entry title plus two
   content H1s). Reduce to a single H1.
3. Topic duplication. `/ai-books-for-business-leaders/` (7739) and
   `/artificial-intelligence-books/ai-for-leaders-and-thinkers/` (101) target
   nearly the same phrase. Differentiate or consolidate to avoid cannibalization.

Until issue 1 is decided, `isPartOf` for AI book pages is provisional.
