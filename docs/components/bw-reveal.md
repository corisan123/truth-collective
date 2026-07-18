# Component (NEW) — tc-bw-reveal (black & white to color on hover)

Purpose: editorial images sit in black and white at rest, then smoothly turn to
full color on hover. For the editorial hubs (The Truth Untold, The Ones Who Gave
Everything) and any image where this effect is wanted.

Additive and fully scoped: a new class name, so it cannot affect any existing
`tc-` component. Nothing else changes.

## How to apply

1. Add the CSS once (Appearance > Customize > Additional CSS, at the bottom).
2. On any image block you want the effect on: open the block, Advanced,
   Additional CSS Class(es), and add `tc-bw-reveal`.
3. Update the page, purge both caches, check in a private window.

Touch devices (no hover) show full color automatically, so nothing looks broken
on phones. Reduced-motion users get the color instantly with no fade.

## CSS to add (append-only, scoped)

```css
/* =============================================================================
   TC BW REVEAL  (append-only, scoped to .tc-bw-reveal)
   Black and white at rest, full color on hover. Editorial imagery.
============================================================================= */
.tc-bw-reveal img {
  filter: grayscale(100%) contrast(1.02) !important;
  transition: filter 600ms ease, transform 600ms ease !important;
  will-change: filter, transform !important;
}

@media (hover: hover) {
  .tc-bw-reveal:hover img {
    filter: grayscale(0%) contrast(1) !important;
    transform: scale(1.02) !important;   /* subtle editorial lift; remove if not wanted */
  }
}

/* Touch and small screens: show full color (no hover available) */
@media (hover: none), (max-width: 767px) {
  .tc-bw-reveal img {
    filter: grayscale(0%) !important;
    transform: none !important;
  }
}

/* Respect reduced motion: keep the effect, drop the animation */
@media (prefers-reduced-motion: reduce) {
  .tc-bw-reveal img {
    transition: none !important;
    transform: none !important;
  }
  .tc-bw-reveal:hover img {
    transform: none !important;
  }
}
```

## Optional add-ons (say the word and I will add)

- Caption or title that fades in on hover over the image.
- A soft dark gradient at the bottom so white caption text stays readable.
- A slower, more cinematic fade (900ms) for hero-size editorial images.
- Whole-image link support (if the editorial image should click through to the
  article), which works the same way as the book covers: the link is the image's
  own link setting, independent of this class.

## Notes

- The subtle `scale(1.02)` zoom on hover gives an editorial feel. If Daniel wants
  pure color change with no movement, delete the two `transform: scale(1.02)`
  and related transform lines.
- This is v1. Tune timing and zoom from a real screenshot before rolling out.
