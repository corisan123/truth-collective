# Playbook 06 — Book Covers Cropping: Wrong Card Class

## Root cause (verified live 2026-07-18 on /ai-in-healthcare/)

Book cards on the AI in Healthcare page use the WRONG component classes:
- Column has `tc-overlay-card`
- Image figure has `tc-explore-hub`

Those are the full-bleed background-image components. They force the image to
fill a fixed ~460px-tall box with `object-fit: cover`, which slices the cover.
No Canva export size can fix this, because `object-fit: cover` fills by the box
shape and discards the rest of the image regardless of its dimensions. The same
classes also try to position the title and description as overlay text.

The content is actually book-card content: cover + H3 title + author + a
`tc-leadership-body` description + an Amazon buy button. The correct component is
`tc-book-card`, which shows the full cover (`height: auto`, no crop), title and
author below, and the description revealing on hover. This matches the working
AI Books for Business Leaders page.

## Scope

All 10 book cards on `/ai-in-healthcare/` use the wrong classes (10 columns with
`tc-overlay-card`, 10 figures with `tc-explore-hub`, 0 correct `tc-book-card`).
Fix all 10.

Likely repeated on other AI child pages built the same period. After fixing this
page, check the other AI child pages (foundational-ai-books, ai-workbooks-and-
guided-learning, future-proof, ai-books-for-beginners-2) for the same wrong
classes. The correct reference is ai-books-for-business-leaders, which uses
tc-book-card correctly.

## The fix, per card (no new CSS, no image re-export)

In the WordPress editor, for each of the 10 cards:

1. Select the column/section block. In its Additional CSS Class(es) field,
   change `tc-overlay-card` to `tc-book-card`.
2. Select the image block. Remove `tc-explore-hub` from its Additional CSS
   Class(es) field (leave it empty).
3. Leave the description paragraph's `tc-leadership-body` class as is.
4. Select the buy button block. Add `tc-book-button` to its Additional CSS
   Class(es) field.
5. Update the page.
6. Purge both caches (LiteSpeed plugin Purge All + hPanel Flush Cache).
7. View in a private window: covers should show fully, no cropping, description
   and button revealing on hover.

## Why this is the right fix, not object-fit: contain

Switching the overlay card to `object-fit: contain` would stop the slice but keep
the wrong component (fixed 460px box, overlay title behavior, letterbox gaps).
Using `tc-book-card` is the correct, intended component for book content and
matches the rest of the site. Fix the cause, not a workaround.

## Separate note (not the crop issue)

`/ai-in-healthcare/` is a top-level URL. If it is meant to sit under the AI
Mastery Book Collection hub, confirm intended nesting. Do not change the slug
after it is indexed on live. Handle as part of the pre-launch structure pass.
