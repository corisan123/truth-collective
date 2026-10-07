# Additional CSS review — website settings, 23 September 2026

Daniel asked that edits not proceed blind of Appearance → Customize → Additional CSS. That file is the pre-10Web working rule set.

**Live source:** homepage `<style id="wp-custom-css">` at `https://tcstaging.truth-collective.com/`. REST `custom_css` is still 404, so this is the only read path.

| Check | Result |
| --- | --- |
| Characters | 57,615 |
| SHA-256 | `7e8c981ed33f52075707d54039c20817b9f6743623f27a30a3558ee1e966d6bb` |
| vs 8 Aug dump | **byte-identical** |
| vs 19 Sep audit | same file, not crash-damaged |

Repo copies:

- `diagnostics/css-chunks/additional-css-from-homepage-2026-08-08.css`
- `diagnostics/css-chunks/additional-css-live-from-settings-2026-09-23.css` (same bytes)

Do **not** rewrite Additional CSS. Page 111 chrome stays in the page `<style id="tc-tech-hub-s1">` adapter.

---

## How the locked classes fire (HTML the CSS was written against)

### 1. Overlay card — title rises

Block: `STAGING TEST 02 — OVERLAY CARD (Option A)`.

HTML:

- Class `tc-overlay-card` on the **column**
- Inside: image, `h3.wp-block-heading`, then `p`

Rules that matter:

- Rest: title `bottom: 24px; top: auto` on the photo
- Hover: `bottom: auto; top: 28px` — title moves to the **top** of the image
- Hover: image darkens (`brightness(0.7)`), card lifts
- Description `p` sits at 50% and fades in

Kadence selector uses `.kt-inside-inner-col >`. Gutenberg columns have no that wrapper, so page-scoped CSS must mirror the same numbers on `> h3` / `> p`.

### 2. Explore hub — EXPLORE pill, title does not move

Block: `TC Explore Hub Overlay Animation, 2026-05-26`.

- Class `tc-explore-hub` on the **image** (pre-10Web Tech Hub) or later, wrongly, on the column
- `::after { content: "EXPLORE"; top: 50%; left: 50% }` — charcoal pill, hidden until hover
- Hover: title `opacity: 0.7` only. **No `top` / `bottom` change.**
- Inner `p { display: none }` — only if the paragraph is *inside* the explore-hub node

If `tc-explore-hub` is on the column, Additional CSS never lifts the title. Page CSS `bottom: 46%` was an invented substitute and lands the title **on** the centered pill. That is the hover bug on Technology Hub.

### 3. Combined overlay + explore (Keep)

Block: `TC OVERLAY-CARD (column) + EXPLORE-HUB (image) COMBINED FIX`.

Working books / pre-10Web Tech Hub markup:

- Column: `tc-overlay-card`
- Image / figure: `tc-explore-hub`
- Sibling `h3` then sibling `p`

Hover stack:

1. Overlay moves the title to `top: 28px` (above the pill)
2. Explore paints EXPLORE in the **middle** of the image
3. Combined fix moves the following `p` to `bottom: 26px` so copy does not sit on the pill

Additional CSS combined selector still requires `.kt-inside-inner-col > .tc-explore-hub ~ p`. Gutenberg needs the same `~ p` rule without that wrapper.

Dual-class **crop** on homepage `5` and AI Mastery `96` is a separate geometry fight (two absolute fills). Combined Fix does not undo crop. Neutralize inner `.tc-explore-hub { transform; min-height }` when the class is on the image inside an overlay column.

### 4. What was wrong on Technology Hub 111

| Live before this pass | Website-settings rule |
| --- | --- |
| `tc-explore-hub` on the **column** | Explore belongs on the **image** |
| `tc-overlay-card` count **0** | Overlay belongs on the **column** |
| Page CSS `bottom: 46%` on hover | Overlay hover is `top: 28px; bottom: auto` |
| Who / Why / Best heading-only | Named regions need existing page copy |

Emerging Technologies and AI Wearables still have **no dedicated WP page** (publish/draft/trash search empty). Product copy for both already lives on Computers `359`. Tiles link there until dedicated children exist. That is not a new page.

---

## Do not do from this review

- Do not paste a rewrite into Additional CSS
- Do not hop to Computers or other hubs until this parent hover + Who/Why/Best pass is correct
- Do not invent Emerging / AI Wearables child pages
