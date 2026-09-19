# Component (NEW, proposed) — tc-book-spotlight

Purpose: give Daniel the smooth overlay feel he likes, but WITHOUT cropping the
book cover. The cover shows whole (natural shape, no `object-fit: cover` slice).
On hover, the description fades and slides up smoothly over the lower part of the
cover, like an overlay, instead of the jerky drop-down growth of `tc-book-card`.

Status: v1 for testing on ONE row (2 to 3 books) first. Tune from a screenshot
before rolling to all cards. Additive and fully scoped: a new class name, so it
cannot affect existing `tc-book-card`, `tc-overlay-card`, or `tc-explore-hub`
cards.

## How to apply (per book card, first row only for the test)

1. Column/section block Additional CSS Class(es): `tc-book-spotlight`
   (remove `tc-overlay-card` from these test cards).
2. Image block: remove `tc-explore-hub` (leave blank).
3. Description paragraph: keep `tc-leadership-body`.
4. Buy button block: `tc-book-button` (optional; reveals with the description).

## CSS to add (Appearance > Customize > Additional CSS, at the bottom)

Append-only. New class. Does not modify any existing rule.

```css
/* =============================================================================
   TC BOOK SPOTLIGHT  (append-only, scoped to .tc-book-spotlight)
   Full uncropped cover + smooth overlay description on hover.
============================================================================= */
.tc-book-spotlight,
.wp-block-kadence-column.tc-book-spotlight {
  position: relative !important;
  background: #ffffff !important;
  border-radius: 12px !important;
  overflow: hidden !important;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08) !important;
  transition: box-shadow 320ms ease, transform 320ms ease !important;
  height: 100% !important;
  box-sizing: border-box !important;
}
.tc-book-spotlight > .kt-inside-inner-col {
  position: relative !important;
  height: 100% !important;
  padding: 0 !important;
}

/* Cover: whole image, never cropped */
.tc-book-spotlight .wp-block-image,
.tc-book-spotlight figure {
  margin: 0 !important;
  overflow: hidden !important;
}
.tc-book-spotlight .wp-block-image img,
.tc-book-spotlight figure img {
  display: block !important;
  width: 100% !important;
  height: auto !important;      /* no object-fit cover, no slice */
}

/* Title + author sit normally under the cover at rest */
.tc-book-spotlight h3,
.tc-book-spotlight .wp-block-heading {
  font-family: "Playfair Display", Georgia, serif !important;
  color: #1f1f1f !important;
  font-size: 20px !important;
  line-height: 1.25 !important;
  text-align: center !important;
  margin: 12px 12px 4px !important;
}

/* Description: hidden at rest, fades/slides up as a smooth overlay on hover */
.tc-book-spotlight .tc-leadership-body {
  position: absolute !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  margin: 0 !important;
  padding: 22px 20px !important;
  background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.97) 26%) !important;
  color: #1f1f1f !important;
  font-family: "Inter", system-ui, sans-serif !important;
  font-size: 15px !important;
  line-height: 1.55 !important;
  text-align: left !important;
  opacity: 0 !important;
  transform: translateY(14px) !important;
  transition: opacity 320ms ease, transform 320ms ease !important;
  pointer-events: none !important;
}

@media (hover: hover) {
  .tc-book-spotlight:hover {
    box-shadow: 0 12px 30px rgba(0,0,0,0.15) !important;
    transform: translateY(-4px) !important;
  }
  .tc-book-spotlight:hover .tc-leadership-body {
    opacity: 1 !important;
    transform: translateY(0) !important;
  }
}

/* Touch and small screens: show description (no hover available) */
@media (max-width: 767px), (hover: none) {
  .tc-book-spotlight .tc-leadership-body {
    position: static !important;
    opacity: 1 !important;
    transform: none !important;
    background: transparent !important;
    padding: 12px 16px !important;
  }
}
```

## Tuning notes (after the screenshot)

- If the overlay covers too much of the cover, raise the gradient start (26% ->
  40%) or reduce padding.
- If the cover art has its title at the bottom and the overlay hides it, we can
  anchor the overlay to reveal from a smaller bottom band, or move title/author
  above the cover.
- If long descriptions overflow, cap with a max-height + subtle fade, or shorten
  copy per the brand voice.
- This is v1. Do not roll to all cards until Daniel confirms the feel from a real
  screenshot.
