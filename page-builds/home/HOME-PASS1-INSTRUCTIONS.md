# Home Pass 1 — paste instructions

Claude = aesthetics. Cursor = this code. You = paste once.

## A) Additional CSS (do this first)

1. WP Admin → **Appearance → Customize → Additional CSS**
2. Scroll to the **bottom**
3. Paste the full contents of `HOME-PASS1-additional-css.css`
4. **Publish**
5. Open `https://tcstaging.truth-collective.com/` in **Incognito**
6. Hover the hub / explore tiles — titles must stay readable; EXPLORE pill navy

If anything looks wrong site-wide (it should not — this is `page-id-5` only), delete only the block between  
`TC HOME PASS 1` and `End TC HOME PASS 1`.

## B) Copy edits in the editor (no code)

Edit the **Home** page blocks. Do not add a Code block.

### Hero paragraph
Replace the long intro with **one sentence**:

> Everything here is chosen with intention, tested against real standards, and stripped of anything that does not earn its place.

### Hero / first-viewport trust list
If a four-item list sits under the hero (books reviewed / baseline / no paid placements / curated by experience): **delete it** or move that whole block below “Start With a Guide…”.

### Mission block
Keep **one** mission section. Shorten the long “affiliate internet is accelerating…” block to **2–3 sentences**, or hide duplicate mission rows for now by moving them to draft later.

### Guide tiles
- Replace or crop the noisy book-spine image (Media Library).
- Keep descriptions out of the permanent image text if they are burned into the JPG — use a clean photo.

### Duplicate heading text
Anywhere an H2 still says only `Home | Truth Collective in 2026`, change it to the real section name (or delete the duplicate heading). Examples of better H2s:
- `What You Can Expect`
- `Our Mission`
- `Six Trusted Hubs`

### About paragraph
Cut to **2–3 sentences**.

## C) What we are NOT doing in Pass 1
- Nav dropdown rebuild (Header builder — separate pass)
- Full footer rebuild
- Replacing the whole homepage with one giant Custom HTML dump
- Touching global locked explore CSS outside Home overrides

## D) Done check
- [ ] Incognito home loads
- [ ] Hub tile hover: title readable + EXPLORE visible
- [ ] Hero EXPLORE looks solid navy (not weak outline)
- [ ] No WordPress “Home | …” page title above the hero
- [ ] Hero copy is one sentence

Then tell Cursor: **Home Pass 1 done** → next Hub.
