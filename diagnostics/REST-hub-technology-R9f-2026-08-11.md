# REST-hub-technology-R9f — APPLIED 2026-08-11

**Issue:** After R9e, hard refresh still no Replace on hero.

**Cause:** Frontend overlay CSS (`position:absolute` on the hero image + content stacked on top) also runs inside the block editor canvas. The image sits under the text layer, so Daniel cannot select it — toolbar/Replace never appears.

**Fix:** Editor-only CSS (`.editor-styles-wrapper …`) forces hero + category images back to normal static flow in the editor. Overlay layout remains on the public page only.

**Daniel steps**
1. Close Technology Hub editor fully
2. Reopen Edit
3. Click the large photo at the top (it should sit above the Truth Collective / title text in the editor now)
4. Toolbar → Replace
