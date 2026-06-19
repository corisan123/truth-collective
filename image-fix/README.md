# Fix: image getting "cut in half" (Kadence overlay card)

## Why it happens
Your `<img>` is perfectly fine — it's a 1900×1080 file with a correct
`srcset`. Changing the upload size (1200×650 vs 1900×1080) won't help
because **the file isn't what's cropping**.

The crop comes from the **container** (`tc-overlay-card` / its column).
An "overlay card" usually has either:

1. a **fixed height** + `overflow:hidden`, while the image keeps
   `height:auto`. A tall 1900×1080 image at 100% width is taller than the
   card, so everything past the card's height is clipped → looks like the
   bottom half is gone; or
2. the image is **absolutely positioned** to fill the card and the card's
   height is set by the text, so the image overflows and gets clipped.

## The fix
`tc-image-fix.css` gives you two options. **Use exactly one.**

- **Option A (default, recommended):** the card grows to fit the image, so
  the whole image shows and the heading/paragraph sit below it. Nothing is
  cropped.
- **Option B (true banner):** keep a fixed-height banner with text on top,
  but crop the image **evenly from the center** (with `object-fit:cover`
  and `aspect-ratio`) so it's never lopsided. To use it, comment out
  Option A and uncomment the Option B block.

## How to install (Kadence / WordPress)
1. WordPress admin → **Appearance → Customize → Additional CSS**
   *(or Kadence → your global custom CSS / a code-snippets plugin)*.
2. Paste the contents of `tc-image-fix.css`.
3. **Publish**, then hard-refresh the page (Ctrl/Cmd+Shift+R).

If the image still clips, the fixed height is coming from the **Section**
or **Row** rather than the image block. In the Kadence editor select the
Section with class `tc-overlay-card` → **Style → Height/Min Height** and
set it to **auto / 0**, or confirm the class is actually on that Section.

> Tip: keep using the **1900×1080** file. With Option A it scales to any
> width cleanly; with Option B it center-crops to your banner ratio.
