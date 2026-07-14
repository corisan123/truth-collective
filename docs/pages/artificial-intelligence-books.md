# Page Improvement Playbook — Artificial Intelligence Books (AI hub)

- URL: https://tcstaging.truth-collective.com/artificial-intelligence-books/
- Role: parent hub for the AI book pages. Also carries an intro for the separate editorial and podcast page.
- Focus keyword: artificial intelligence books
- Status captured from staging on 2026-07-14. Reverify before applying.

## 1. SEO status

- SEO title: "Artificial Intelligence Books | Best AI Mastery Picks 2026" (includes 2026, follows the framework spirit). Keep.
- Meta description present and includes the focus phrase. Keep.

## 2. Canonical (high priority fix)

The page sets its canonical to the editorial-series URL. That is wrong. The hub
is a separate page from the editorial series.

- Set the Canonical URL to itself: https://tcstaging.truth-collective.com/artificial-intelligence-books/
- Set the RankMath CollectionPage schema `url` to itself as well.
- The editorial and podcast page keeps its own canonical: https://tcstaging.truth-collective.com/ai-mastery-collection-2026-editorial-series/

## 3. Single H1 (fix)

The page renders more than one H1. Keep one H1 for the hub, demote the rest to H2.

- Keep as H1: "Artificial Intelligence Mastery Collection Series".
- Demote to H2: "Truth Collective Technical Quality Statement" and any other H1 block.

## 4. Content-rule violations (fix). No em dashes ever, no contractions.

| Location | Problem | Compliant replacement |
| --- | --- | --- |
| Quote heading | em dash and contractions "isn't", "it's", plus hyphenated brand | Artificial Intelligence is not just another technology. It is the new literacy of the modern world. (Truth Collective, FY 2025) |
| Intro paragraph ("The books featured...") | contraction "isn't" | reading it alone is not the only path forward |
| Business leaders category paragraph ("AI is exposing weak leadership...") | em dash before "the ability to reason" | the human quantifier, the ability to reason beyond statistics |
| Newsletter subhead ("Four times a year ...") | em dash | Four times a year. The best new additions, updated guides, and honest reassessments. No spam. No filler. No noise. |

The newsletter subhead is a reusable block. Fixing it corrects the em dash
everywhere that block appears.

## 5. Link hygiene

- The intro paragraph links "Standard Evaluation Process" to a raw .docx download
  (`/wp-content/uploads/2026/07/Master-Engineering-Driven-Evaluation-System.docx`).
  Point this to the on-site standards page instead of a Word file:
  https://tcstaging.truth-collective.com/master-engineering-driven-evaluation-system-7/

## 6. Internal linking

- Up to parent: Recommended Books, https://tcstaging.truth-collective.com/recommended-books-2026/
- Down to children: confirm every one of the eight on-page categories links to its page. The following child pages are confirmed in the site menu. Wire each category card to its page, and mark any category without a page as coming soon rather than a dead card.

## 7. Schema (RankMath Custom Schema)

Add the hub as a self-canonical CollectionPage that is part of Recommended Books,
with an ItemList of its confirmed child pages. Do not invent URLs for categories
that do not yet have pages.

```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Artificial Intelligence Books | Best AI Mastery Picks 2026",
  "url": "https://tcstaging.truth-collective.com/artificial-intelligence-books/",
  "description": "Artificial intelligence books curated and evaluated for professionals who want to apply what they learn.",
  "isPartOf": {
    "@type": "CollectionPage",
    "name": "Recommended Books",
    "url": "https://tcstaging.truth-collective.com/recommended-books-2026/"
  },
  "mainEntity": {
    "@type": "ItemList",
    "name": "Artificial Intelligence book categories",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "AI For Beginners", "url": "https://tcstaging.truth-collective.com/ai-books-for-beginners-2/" },
      { "@type": "ListItem", "position": 2, "name": "AI Books for Leaders and Critical Thinkers", "url": "https://tcstaging.truth-collective.com/ai-books-for-business-leaders/" },
      { "@type": "ListItem", "position": 3, "name": "AI Workbooks and Guided Learning", "url": "https://tcstaging.truth-collective.com/artificial-intelligence-books/ai-workbooks-and-guided-learning/" },
      { "@type": "ListItem", "position": 4, "name": "Foundational AI Books", "url": "https://tcstaging.truth-collective.com/artificial-intelligence-books/foundational-ai-books/" },
      { "@type": "ListItem", "position": 5, "name": "Future-Proof: The AI Books That Redefine Work and Skills", "url": "https://tcstaging.truth-collective.com/artificial-intelligence-books/future-proof-the-ai-books-that-redefine-work-skill/" }
    ]
  }
}
```

## 8. Duplication to resolve

`/artificial-intelligence-books/ai-for-leaders-and-thinkers/` (page 101) and the
top-level `/ai-books-for-business-leaders/` (page 7739) target nearly the same
phrase. Pick one as the canonical leaders page and differentiate or redirect the
other. Until then, do not list both as separate categories.

## 9. Apply order

1. Fix the canonical to self, and the schema `url` to self.
2. Reduce to a single H1.
3. Apply the four content-rule fixes.
4. Repoint the .docx link to the standards page.
5. Wire the category cards down to their pages, mark coming-soon where no page exists.
6. Add the Custom Schema.
7. Run the Publish Gate checklist.
