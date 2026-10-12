# CSS class binding versus Additional CSS text

**Prepared:** 12 October 2026  
**Why this file exists:** Daniel Reid rejected the sentence that Additional CSS / `tc-*` classes “survived intact.” That sentence is a half-truth. This file splits the layers so counsel does not hear “the CSS still worked.”

**Not a legal opinion.**

---

## 1. The discarded sentence

Do not write: “The CSS classes were intact.”  
Do not write: “Additional CSS survived, so 10Web did not touch CSS.”  
Do not write: “Damage is markup, not CSS,” as if those were separate worlds.

What was measured on 8 August and 19 September: the **Customizer stylesheet text** (`<style id="wp-custom-css">`, 57,615 characters, SHA `7e8c981…`) was byte-identical. That is the rule file in Appearance → Customize. It is not the live binding of those rules to Gutenberg or Kadence HTML.

---

## 2. Three layers (use all three)

| Layer | What it is | After 10Web |
| --- | --- | --- |
| A. Stylesheet text | Additional CSS in Customizer. Selectors for `tc-overlay-card`, `tc-explore-hub`, `tc-book-card`, and the rest | **Present.** Not truncated. This is the only layer the earlier memos proved. |
| B. Class names on blocks | The string `tc-overlay-card` / `tc-explore-hub` / `tc-book-card` still appearing somewhere in `post_content` | **Partial.** Many product/hub blocks had classes stripped (Computers: **0×** `tc-overlay-card-product` on 8 Aug). Some names remained. |
| C. Class-to-structure binding | Which WordPress block the class sits on, and whether that block is still Gutenberg or Kadence (section → column → image → description) so the Additional CSS selector matches | **Broken on most pages.** Remaining classes sit on the wrong node or on HTML that is no longer the tree the selector was written for. Hover/overlay/EXPLORE therefore does not fire, even when the class name is still in the page. |

Saying “classes remain” without layer C is the half-truth.

Additional CSS was written for **both** builders. Kadence selectors use `.kt-inside-inner-col >`. Gutenberg columns have no that wrapper. Locked placement:

- `tc-overlay-card` on the **Kadence Section / column**
- `tc-explore-hub` on the **image** (not on the column)
- Sibling `h3` then sibling `p`
- Books: `tc-book-card` on the section, `tc-leadership-body` on paragraphs, `tc-book-button` on the parent button

If 10Web left a class name on the wrong block, or replaced a Kadence section/column/image stack with a different Gutenberg or fake-Builder tree, layer A still exists and layer C is dead. That is why a page can show a `tc-*` class in the editor and still have no working animation.

---

## 3. What 10Web did inside WordPress (owner account, only named vendor)

Daniel’s account of the migrate window, which this packet now uses:

The only named entity inside WordPress during the failed migrations and the subsequent 10Web admin entrance is **10Web**. Internally they either:

1. **Wiped about 100% of many pages**, or  
2. Left CSS class names pointed at **misaligned HTML**, so the locked animations did not fire.

They also combined **fake images** and **fake website pages** (Builder sites `active-bluegill` / `kind-louse`) with fragments of the real site. That mash is the same event as the class-binding break: class names from the real build sitting on foreign or rebuilt Kadence/Gutenberg structure.

Cursor was not a WordPress admin in that window. This recovery run’s REST writes are after 8 August.

---

## 4. Builder eras (why Gutenberg books lasted more than Kadence catalogs)

| When | How pages were built |
| --- | --- |
| February–April 2026 | **Gutenberg only** (core blocks) |
| After Kadence was added | **Kadence + Gutenberg**: section, column, image, description, and the locked `tc-*` classes on those nodes |

Owner count for books:

- **20-plus book categories**
- About **1,000 books** on the pre-migration site
- About **200 books remaining** on the crashed site
- Most or all of those remaining books were **Gutenberg-only** pages, and **all of them have some level of damage**

Ironic result: Additional CSS was written to serve both builders, but the pages that still have a recognizable book grid are the older Gutenberg-only ones. Kadence section/column/image catalogs (Technology children, Office, products) took the wipe or the misaligned-class hit. This agent has not independently counted 1,000 SKUs. Those figures are Daniel’s census from the pre-migration site on his CPU. To pin them, send the 23 July `-db.gz` or a pre-migration book-hub Print-to-PDF.

---

## 5. Three pages with full working CSS classes

Daniel: **three pages** still have full working CSS class binding (animation fires because class sits on the correct Gutenberg or Kadence node).

This recovery chat previously treated “books work when `tc-explore-hub` is on the image” as the working pattern. It did not name three URLs.

**Ask:** send the three permalinks. They become the positive control: proof that Additional CSS still fires when markup matches, and therefore proof that failure on the other URLs is binding/markup, not a missing stylesheet.

Until those three URLs are listed, do not guess.

---

## 6. Error log: Kadence critical failure in the same brief as 10Web

7 August 2026 14:15 UTC, same `error_log` as the 10Web Manager lines:

- Kadence `Shutdown_Collection.php` **failed to open** (file not found)
- Kadence DI52 container **fatal** (cannot resolve `Shutdown_Collection`)
- PHP `include_path` still lists **four `10web-manager/vendor/pear/...` paths**
- Rank Math Pro `rank-math-pro.php` also missing
- Same day as the formal incident letter in ticket `#375660`

That is a **critical Kadence failure on staging while 10Web Manager is on the include path**. It is not a quote that says “10Web deleted Kadence.” It is contemporaneous: 10Web’s plugin is in the runtime path at the moment Kadence cannot load a class file. Pair it with the owner fact that Kadence-structured pages (section/column/image) are the ones whose class binding broke.

25 July and 3 August: `10web-manager/includes/class-rest-api.php` line 444 (`sftp_credentials`). 10Web Manager was executing on staging in the migrate window.

---

## 7. Counsel sentences to use

Use:

> The Customizer Additional CSS file is still there. That does not mean the CSS classes were intact. On most pages 10Web either wiped the content or left class names pointed at the wrong Gutenberg or Kadence structure (section, column, image, description), so the locked hover and overlay animations did not fire. About three pages still have working class binding. Of about 1,000 books across 20-plus categories, about 200 remain, all damaged, and those survivors were Gutenberg-only pages. Kadence failed hard on 7 August in the same error log that shows 10Web Manager on the include path.

Do not use:

> Additional CSS survived, so CSS was not damaged.  
> The `tc-*` classes are intact.  
> The problem is missing Additional CSS.
