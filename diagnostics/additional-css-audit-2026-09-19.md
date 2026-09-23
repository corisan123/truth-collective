# Additional CSS audit — staging 2026-09-19

**Source of truth:** Appearance → Customize → Additional CSS, read live from homepage `<style id="wp-custom-css">`.  
**REST `custom_css` type is not exposed** (404). That is why later hub chrome lives in page HTML `<style>` blocks.

**Crash check:** Additional CSS was **not damaged, truncated, or rewritten** by the crash. Live file is byte-identical to the 8 August homepage extract.

| | Live 19 Sep 2026 | Snapshot 8 Aug 2026 |
| --- | --- | --- |
| Characters | 57,615 | 57,615 |
| Lines | 1,682 | 1,682 |
| SHA-256 | `7e8c981ed33f52075707d54039c20817b9f6743623f27a30a3558ee1e966d6bb` | same |
| Braces / comments | balanced, no unclosed comment | same |
| `@keyframes` with no caller | none | same |

Repo copy: `diagnostics/css-chunks/additional-css-from-homepage-2026-08-08.css` (keep; it is still current).

**Nothing in Additional CSS was deleted after 02-GRADE.** Membership toggle remains the footer, as expected.

---

## What this file is

One append-only stack. Later patches override earlier ones with `!important` (485 uses). That is the historical method. Do not reorder. Do not wipe. Disable **one named block** only when that named animation is proven dead.

---

## Named blocks (file order)

| Block | Status | Notes |
| --- | --- | --- |
| STAGING TEST 01 — Book card hover reveal | Keep | `tc-book-card` + `tc-leadership-body` + `tc-book-button` |
| STAGING PATCH 01A — Book H5 title | Keep | Book cards only |
| STAGING TEST 02 — Overlay card Option A | Keep | `tc-overlay-card` on Kadence **column**. Image `position:absolute; inset:0; object-fit:cover`. `min-height:460px`. Title on image bottom. Hover lift + darken. |
| TC Row-Stretch Override | Keep | Fights book-card `height:100%` |
| TC Gold Star Rating Base64 | Keep | `tc-grade-block` / `tc-rating-*` |
| Tech Hub EXPLORE button wrapper | Keep, mostly idle | Styles `.tc-book-card .wp-block-html .tc-explore-link` (real HTML anchor). **0 live uses** of that class on 59 published pages. |
| Tech Hub editorial intro (`tc-tech-intro`) | Keep | Light hubs now use page-scoped intro CSS too |
| STAGING PATCH 01B — sibling stretch | Keep | Books |
| STAGING PATCH 01D — “center EXPLORE” | Keep | Name is stale. It centers `.tc-book-button`, not EXPLORE. |
| STAGING PATCH 01C-PRODUCT — lock image height | Keep, watch | `tc-product-card` only. `aspect-ratio:1/1` + `object-fit:contain`. Duplicate `object-position`. Books never crop. |
| STAGING PATCH 01E / 01G | Keep | Book padding / label line |
| **TC Explore Hub Overlay Animation, 2026-05-26** | Keep | **CSS look-alike.** `.tc-explore-hub::after { content:"EXPLORE" }`. Hover fade. Gold `::before` `›`. Assumes class on Kadence **column**, image as inner `figure`, `min-height:460px`, absolute cover fill. |
| **TC Explore Hero Animation + render fix + tuning** | Keep | **Homepage entrance.** Not JS. See button taxonomy. Duplicate `@keyframes` (original, then 1024px, then 767px, then tuning). Last writer wins. |
| **STAGING PATCH 02A** | **SKIP / known good** | Real HTML two-button overlay: View + TC Grade. Do not edit. |
| 02-PRODUCT CONSOLIDATED | Keep | Product modifier square cover |
| Duplicate “card shape” snippet after CONSOLIDATED | Keep for now | Same `aspect-ratio:1/1` restated before overflow fix |
| 02-PRODUCT OVERFLOW FIX | Keep, still the intended grid fix | `min-width:0` so 1/1 cards do not shove neighbors. Daniel 8 Aug: not working properly on some pages. Cause is often **missing class on markup**, not a crash hole in this CSS. |
| 02-PRODUCT POLISH | Keep | White title + scrim on product |
| TC PRODUCT OVERLAY BUTTONS SSoT | Keep | Authoritative product button grid |
| TC PRODUCT GRADE STARS real bug fix | Keep | Flex-axis star height |
| **OVERLAY + EXPLORE-HUB COMBINED FIX** | Keep, incomplete | Only moves a following `p` so it clears the EXPLORE pill. **Does not undo image crop** when both classes share one card. |
| STAGING PATCH 02-GRADE | Keep | Hub grade hidden on hover |
| Unnamed mobile row padding | Later | Sitewide `.kt-row-column-wrap` at `max-width:767px`. Not overlay-scoped. |
| TC Membership Toggle | Keep | `body.page-id-8176` only |

**Grayscale:** **zero** rules in Additional CSS. Correct. Editorial B/W → color is a later Additional CSS pass, **the three editorial hubs only**.

---

## Overlay + Explore on the same card (the crop)

Two separate systems were written to own the image plane:

1. **`tc-overlay-card` on the Section/column** — absolute image fill, 460px min-height, title on image, description on hover.
2. **`tc-explore-hub` on the image (or later on the column)** — another absolute fill, another 460px min-height, CSS EXPLORE `::after`.

Together: two `position:absolute; inset:0; object-fit:cover` layers plus two min-heights. That is the distortion you remember. Combined Fix only moved copy, so the crop can still happen wherever markup still stacks both classes.

**Still stacked today**

| Page | Pattern |
| --- | --- |
| Homepage `5` | `tc-overlay-card` on column + `tc-explore-hub` **on the inner image** (core `wp:image` and Kadence image). 10 overlay columns, 13 explore-hub images. This is the live crop combo. |
| AI Mastery Book Collection `96` | Same family: 10 overlay + 20 explore-hub. Last edited **19 Jul 2026**. Not in the Aug 12 light rebuild. Highest leftover dual-class risk among hubs. |

**Combo removed by later light rebuilds** (explore-hub on core/Kadence **column**, no overlay-card on that tile): Technology Hub `111`, Office `5939`, Smart Lighting `115`, Productivity `5680`, Self-Help `86`, Books hub `38`, Truth Untold `2516`, and the Aug 19 Tech children (speakers, tablets, monitors, …).

**Products / Computers `359`:** overlay-card + overlay-card-product + product-card. **`tc-explore-hub` count = 0.** That is the correct split. Do not put explore-hub on product or book covers.

---

## Image sizing rules still in Additional CSS

These all remain. They fight when the wrong class is on the card:

- Overlay / explore-hub: `object-fit: cover` + absolute fill + `min-height: 460px`
- Product 01C: `object-fit: contain` + `aspect-ratio: 1/1` on `tc-product-card` images
- Product 02 family: `object-fit: cover` + `aspect-ratio: 1/1` on `tc-overlay-card-product`
- Hero: `object-fit: cover` + later **16:9** `aspect-ratio` on `.tc-explore-hero`

Wrong pixel dimensions still make cover-fill look cropped. That is why 1600×1000 (hub tiles) and ~600×600 (product squares) were locked. The CSS is not missing those rules.

---

## Second CSS layer (not Additional CSS)

Light rebuilds could not write Customizer CSS via REST, so they injected **page-scoped `<style>`** (about 9–16 KB per hub). Example on Technology Hub `111`: R9 comments, `.tc-tech-cover`, explore-tile min-heights **300px / 260px** (overrides the global 460px), “ensure EXPLORE pseudo still paints.” Computers `359` and other Aug 19 children carry a similar block that also styles `.tc-overlay-card` / aspect-ratio locally.

So the site is **two sheets**:

1. Global Additional CSS (intact, 8 Aug = 19 Sep).
2. Per-page HTML CSS (Aug 9–19). This is why some hubs look lighter than homepage even though Additional CSS never changed.

Do not migrate page CSS into Additional CSS in this pass.

---

## Button / EXPLORE taxonomy (locked after Daniel 19 Sep)

Three different things have been called “the EXPLORE button.” They are not the same.

### A — CSS look-alike (most hub tiles)

Class `tc-explore-hub`. No `<button>`. No `<script>`. Additional CSS `::after { content: "EXPLORE" }`. Whole image is the link. Hover fades the label in. This is what the Vercel/10Web PDF describes for tiles.

### B — Coded entrance look-alike (homepage, rare)

Class `tc-explore-hero` on the homepage Kadence hero column only (published pages: **homepage `5` only**). Additional CSS, 1 June 2026:

- Image darkens (`tc-hero-image-reveal`)
- Heading drops in
- Paragraph slides from the **right** (`tc-hero-paragraph-slide-right`)
- Then a transparent/dark **EXPLORE** pill slides from the **left** and lands center (`tc-hero-pill-slide-left`, delay ~1s after tuning)

There is **no homepage `<script>` that draws EXPLORE**. There is **no EXPLORE HTML** in page 5 content. It is `@keyframes` on `::after`. `pointer-events: none` on that pill — it is visual. The intended click is a Kadence section link overlay, which **this hero currently does not have**, so the pill does not navigate by itself.

This is the “coded, not a CSS class button” behavior you remember. It is CSS animation code, not JavaScript. Keep it **seldom**. Do not spray `tc-explore-hero` onto hub tiles or product cards.

Light hub heroes use a **different** coded control: real HTML `.tc-tech-cover__cta` in page CSS (transparent border, gold on hover). That is a real `<a>`, page-scoped, not Additional CSS hero, not JS.

### C — Real HTML buttons that fire from CSS classes

| Control | Class | Where |
| --- | --- | --- |
| View + TC Grade | `tc-overlay-buttons` / `tc-affiliate-btn` / `tc-grade-btn` | Computers (21 cards) and leftover product chrome on other Tech children. **02A = skip.** |
| Book CTA | `tc-book-button` | Mental Wellness Books `1931` (32). CSS 01 / 01D. |
| HTML EXPLORE anchor | `tc-explore-link` | CSS still present. **0 live published uses.** |
| Cover CTA | `tc-tech-cover__cta` | Light hub heroes (page CSS) |

### D — Actual JavaScript (not EXPLORE)

Published page scripts are almost all MailerLite `.tcj-signup`. Membership toggle JS lives on draft `8176`. Old Tech Hub IntersectionObserver reveal (`tc-tech-hub-reveal-r8`) is **not** on live page 111 anymore.

---

## Broken vs intact (plain)

| Question | Answer |
| --- | --- |
| Did the crash eat Additional CSS? | **No.** Identical to 8 Aug. Syntax valid. |
| Is the overlay+explore crop “fixed in CSS”? | **Partially.** Combined Fix does not restore image geometry. Crop is gone where markup stopped stacking both classes. Crop risk **remains on homepage and AI Mastery `96`.** |
| Are image-sizing rules missing? | **No.** Cover, contain, 1:1, 16:9, 460px min-height are all still there and still conflict if classes are mixed. |
| Is grayscale damaged? | **It was never in this file.** Later pass only. |
| Are hero keyframes dead? | **No.** All five names are used. Duplicates are overrides, not orphans. |
| Should Additional CSS be edited now? | **No.** Structure pass still has not started. No named animation is dead. |

---

## Do not do from this audit

- Do not comment out Explore Hub or 02A.
- Do not Hostinger-restore CSS.
- Do not put `tc-explore-hub` on book covers or product cards.
- Do not start grayscale.
- Do not start the Technology Hub structure pass until Daniel has the Computers product report and says go.
