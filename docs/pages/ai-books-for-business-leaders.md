# Page Improvement Playbook — AI Books for Leaders and Critical Thinkers

- URL (canonical, nested under AI hub): https://tcstaging.truth-collective.com/artificial-intelligence-books/ai-books-for-business-leaders/
- Old top-level URL 301-redirects to the nested URL. Hierarchy is corrected.
- WordPress page id: 7739
- Focus keyword: AI books for leaders and critical thinkers
- Status captured from staging on 2026-07-14. Reverify before applying.

This file is the drop-in package to bring this page to the Publish Gate standard.
Nothing here changes the locked, indexed slug. All facts were read from the live
staging page, not assumed.

## 1. SEO status (already compliant, no change needed)

- SEO title: "AI Books For Business Leaders And Critical Thinkers In 2026" (57 chars, includes 2026). Keep.
- Meta description: 153 chars, includes the focus phrase. Keep.
- H1: "AI Books for Leaders and Critical Thinkers | 2026" includes the keyword. Keep.
- Keyword present in first paragraph and multiple H2s.

Note: the title does not follow the "Best [category] for [audience] in 2026 | Truth Collective"
framework, but it is indexed and compliant on length and year. Do not change it to chase the framework.

## 2. Image alt text (fix: make all nine unique)

All nine covers currently share one alt string. Replace per cover. Keep the focus
keyword on the first (primary) image only. Set each in the Image block alt field.

| wp-image id | Alt text |
| --- | --- |
| 7740 | The AI-Driven Leader by Geoff Woods, AI books for leaders and critical thinkers |
| 7741 | All-in On AI by Thomas H. Davenport and Nitin Mittal, book cover |
| 7742 | Human + Machine by Paul R. Daugherty and H. James Wilson, book cover |
| 7743 | Competing in the Age of AI by Marco Iansiti and Karim Lakhani, book cover |
| 7744 | Power and Prediction by Ajay Agrawal, Joshua Gans, and Avi Goldfarb, book cover |
| 7745 | AI Snake Oil by Arvind Narayanan and Sayash Kapoor, book cover |
| 7746 | The Coming Wave by Mustafa Suleyman, book cover |
| 7747 | AI Superpowers by Kai-Fu Lee, book cover |
| 7748 | The Agentic AI Bible by Thomas R. Caldwell, book cover |

## 3. Internal linking (fix: add a sibling row)

Verified live URLs. Keep the existing prose link up to the hub, and add a sideways
row of siblings near the foot of the page.

- Up to parent hub: Artificial Intelligence Books, https://tcstaging.truth-collective.com/artificial-intelligence-books/ (the AI Mastery Collection, parent of the AI book pages). See the canonical issue in `docs/site-structure.md` before finalizing.
- Sideways siblings (use three to four):
  - AI For Beginners, https://tcstaging.truth-collective.com/ai-books-for-beginners-2/
  - Foundational AI Books, https://tcstaging.truth-collective.com/artificial-intelligence-books/foundational-ai-books/
  - AI Workbooks and Guided Learning, https://tcstaging.truth-collective.com/artificial-intelligence-books/ai-workbooks-and-guided-learning/
  - Future-Proof: The AI Books That Redefine Work and Skills, https://tcstaging.truth-collective.com/artificial-intelligence-books/future-proof-the-ai-books-that-redefine-work-skill/

Do not link to /artificial-intelligence-books/ai-for-leaders-and-thinkers/ from
here yet. It targets nearly the same phrase as this page and should be
deduplicated or differentiated first.

## 4. Schema (fix: add CollectionPage + ItemList via RankMath Custom Schema)

RankMath already outputs the BreadcrumbList. Leave it. Add the following as a
Custom Schema on this page (RankMath > Schema > Custom Schema, JSON import). It
adds the page as a CollectionPage that is part of the Artificial Intelligence
Books hub, with the nine books as an ItemList. The parent hub must be made
self-canonical first, see `docs/site-structure.md`. Book grades will be added as
editorial reviews once the books rubric is set.

```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "AI Books for Leaders and Critical Thinkers | 2026",
  "url": "https://tcstaging.truth-collective.com/artificial-intelligence-books/ai-books-for-business-leaders/",
  "about": "Curated AI books for business leaders and critical thinkers",
  "isPartOf": {
    "@type": "CollectionPage",
    "name": "Artificial Intelligence Books",
    "url": "https://tcstaging.truth-collective.com/artificial-intelligence-books/"
  },
  "mainEntity": {
    "@type": "ItemList",
    "numberOfItems": 9,
    "itemListOrder": "https://schema.org/ItemListOrderAscending",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "item": { "@type": "Book", "name": "The AI-Driven Leader: Harnessing AI to Make Faster, Smarter Decisions", "author": { "@type": "Person", "name": "Geoff Woods" }, "url": "https://amzn.to/4flb7iV" } },
      { "@type": "ListItem", "position": 2, "item": { "@type": "Book", "name": "All-in On AI: How Smart Companies Win Big with Artificial Intelligence", "author": [ { "@type": "Person", "name": "Thomas H. Davenport" }, { "@type": "Person", "name": "Nitin Mittal" } ], "url": "https://amzn.to/4w8m4ve" } },
      { "@type": "ListItem", "position": 3, "item": { "@type": "Book", "name": "Human + Machine, Updated and Expanded: Reimagining Work in the Age of AI", "author": [ { "@type": "Person", "name": "Paul R. Daugherty" }, { "@type": "Person", "name": "H. James Wilson" } ], "url": "https://amzn.to/4wJiGXC" } },
      { "@type": "ListItem", "position": 4, "item": { "@type": "Book", "name": "Competing in the Age of AI: Strategy and Leadership When Algorithms and Networks Run the World", "author": [ { "@type": "Person", "name": "Marco Iansiti" }, { "@type": "Person", "name": "Karim Lakhani" } ], "url": "https://amzn.to/4w5j7f5" } },
      { "@type": "ListItem", "position": 5, "item": { "@type": "Book", "name": "Power and Prediction: The Disruptive Economics of Artificial Intelligence", "author": [ { "@type": "Person", "name": "Ajay Agrawal" }, { "@type": "Person", "name": "Joshua Gans" }, { "@type": "Person", "name": "Avi Goldfarb" } ], "url": "https://amzn.to/3QXeSmu" } },
      { "@type": "ListItem", "position": 6, "item": { "@type": "Book", "name": "AI Snake Oil: What Artificial Intelligence Can Do, What It Can't, and How to Tell the Difference", "author": [ { "@type": "Person", "name": "Arvind Narayanan" }, { "@type": "Person", "name": "Sayash Kapoor" } ], "url": "https://amzn.to/4aTvylD" } },
      { "@type": "ListItem", "position": 7, "item": { "@type": "Book", "name": "The Coming Wave", "author": { "@type": "Person", "name": "Mustafa Suleyman" }, "url": "https://amzn.to/4plF1rB" } },
      { "@type": "ListItem", "position": 8, "item": { "@type": "Book", "name": "AI Superpowers: China, Silicon Valley, and the New World Order", "author": { "@type": "Person", "name": "Kai-Fu Lee" }, "url": "https://amzn.to/4gzi1Dn" } },
      { "@type": "ListItem", "position": 9, "item": { "@type": "Book", "name": "The Agentic AI Bible: The Complete and Up-to-Date Guide to Design, Develop, and Scale Goal-Driven, LLM-Powered Agents", "author": { "@type": "Person", "name": "Thomas R. Caldwell" }, "url": "https://amzn.to/4pjLDqH" } }
    ]
  }
}
```

## 5. Compliance and trust (verified present)

- Affiliate disclosure auto-renders in the footer (Master Brief section 8). Confirm it shows on this page.
- The nine covers link to Amazon affiliate URLs (`amzn.to`).
- The Trusted Selection Standards and FTC block is present on this page and points directly to the FTC website. This satisfies the Master Brief section 7 external-link requirement. See `docs/patterns/ftc-trusted-selection.md`.

## 6. Apply order

1. Set the nine unique alt strings.
2. Add the sibling internal-link row.
3. Add the Custom Schema JSON in RankMath.
4. Run the Publish Gate checklist in the Master Brief before pushing to live.
