# Truth Collective — Verified Component Reference

Every rule below was captured directly from the staging Additional CSS
(`wp-custom-css`) and the live staging markup, not from memory. Before changing
any component, confirm the class names and structure against staging again.

All Truth Collective animation CSS lives in the theme Additional CSS and is
appended in dated, scoped blocks. Do not edit earlier blocks in place unless the
fix is in that block. Append fixes as new scoped blocks and never introduce
selectors that collide with the classes below.

Locked palette used by these components: navy `#1e3a5f`, charcoal `#1f1f1f`,
white `#ffffff`, gold `#b8944b`. Fonts: Playfair Display (headings), Inter (body).

---

## 1. `tc-book-card` — book hover reveal

Used on book category (child) pages.

Block structure (GTB = Gutenberg, KD = Kadence):

- Outer wrapper Group (GTB)
- Row Layout (KD)
- Section / Column (KD) receives class `tc-book-card`
- Inside: image (cover), heading (title), author paragraph, then description paragraphs
- Each description paragraph receives class `tc-leadership-body`
- The buttons block receives class `tc-book-button`

Behavior:

- At rest: cover, title, and author show. Description and button are collapsed (`max-height:0; opacity:0`).
- On hover: card lifts (`translateY(-2px)`), title turns navy, description rolls down, button fades in.
- Cards are locked to equal size (`min-height:360px; height:100%`).
- On touch and small screens (max-width 767px) description and button are always visible.

Key verified CSS:

```css
.tc-book-card,
.wp-block-kadence-column.tc-book-card {
  background: #ffffff !important;
  border-top: 4px solid #1e3a5f !important;
  padding: 24px !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
  transition: box-shadow 0.2s ease, transform 0.2s ease !important;
  height: 100% !important;
  min-height: 360px !important;
  box-sizing: border-box !important;
  min-width: 0 !important;
}
.tc-book-card p.tc-leadership-body { /* Inter 15px/1.6 #1f1f1f */ }
@media (hover: hover) {
  .tc-book-card p.tc-leadership-body { max-height:0; opacity:0; overflow:hidden; }
  .tc-book-card:hover p.tc-leadership-body { max-height:min(2200px,92vh); opacity:1; }
  .tc-book-card .tc-book-button { max-height:0; opacity:0; overflow:hidden; }
  .tc-book-card:hover .tc-book-button { max-height:220px; opacity:1; }
}
```

Note: book title heading is styled for h2/h3/h4 and h5 (`STAGING PATCH 01A`). Keep
titles in a heading block so the styling applies.

---

## 2. `tc-overlay-card` — overlay card (single item)

Block structure:

- Outer wrapper Group (GTB)
- Usually Row Layout (KD), sometimes just Section (KD)
- Header (GTB), Image (before or after header), Paragraph (GTB)
- Only the Section block receives class `tc-overlay-card`. No other block gets a class.

Behavior:

- Image fills the whole card (`position:absolute; inset:0; object-fit:cover`).
- At rest: title (h3) sits at the bottom of the image in white. Description paragraph is hidden (`opacity:0`).
- On hover: card lifts, image darkens, title moves to top, description appears.
- Whole card is linked.

Important constraint: this class absolutely positions the image and every `<p>`.
It is built for a single title plus a single description paragraph. Do not place
multiple paragraphs or long banner copy inside it. Card is `min-height:460px`.

Product variant `tc-overlay-card-product` (add both classes) changes the card to
a near-square `aspect-ratio:1/1` cover tile with the TC grade and buttons.

---

## 3. `tc-explore-hub` — hub and large-image overlay with EXPLORE control

Block structure:

- Group (GTB), Row Layout (KD), Section (KD), Image (GTB), then Header title (GTB)
- Only the Section receives class `tc-explore-hub`. No other classes.

Behavior:

- Image fills the card (`object-fit:cover`), `min-height:460px`.
- At rest: title (h2 or h3) in white at the bottom. Paragraphs are hidden (`display:none`).
- On hover: card lifts, image darkens to `brightness(60%)`, and a charcoal gradient EXPLORE control fades in at center. A gold `›` arrow (`#b8944b`) appears to its right.
- The EXPLORE control and arrow are built with `::after` and `::before`. There is no button block.
- Whole card is linked.

Verified: the EXPLORE label and the gold arrow are both defined in CSS. For hero
pages that should not show the gold arrow, use `tc-explore-hero` instead (below).

---

## 4. `tc-explore-hero` — full-bleed hero with staggered entrance animation

Block structure:

- Section (KD) receives class `tc-explore-hero`
- Inside: Image, then `h1`, then a single `p`. The EXPLORE pill is CSS `::after`.

Behavior (home hero):

- Sized to `aspect-ratio:16/9` so a 16:9 image shows fully with no crop. `min-height` is cleared by the later tuning block.
- Entrance animation on load, staggered: image reveal, then `h1` drops from top, then `p` slides in from the right, then EXPLORE pill slides in from the left.
- On this hero the EXPLORE control is the `::after` pill only. No gold arrow (arrow is the hub variant).
- Respects `prefers-reduced-motion`.

Constraint: like the other overlays, `.tc-explore-hero p` is absolutely
positioned. It expects one paragraph, not multiple.

---

## Cross-cutting rules

- Image uniformity: the image CSS in these components forces covers and hub or hero images to a locked box regardless of the source dimensions. Do not remove `object-fit:cover`, the width/height 100% rules, or the min-height without a verified reason.
- All four components link the whole card. Keep the block link or section link overlay intact.
- When a component looks correct in the WordPress editor but breaks on the front end, the cause is almost always one of these front-end-only rules (absolute positioning, object-fit, or min-height), not the block settings.
- Never apply a component class to content it was not built for. Example: applying `tc-overlay-card` to a banner with multiple paragraphs stacks every paragraph at one position and crops the image.
