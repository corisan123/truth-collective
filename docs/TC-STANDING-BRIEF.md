# Truth Collective — Standing Brief

Living brief for Cursor/Angie. Add **one section at a time**.  
Source of truth for look/feel until WordPress staging matches.

---

## §1 — Visual / motion gold standard (Vercel + 10Web samples)

**Context:** After a live-site crash and failed recovery, Daniel explored AI builders **Vercel** and **10Web**. Both built short sample pages that taught the hover / lift / overlay language later named `tc-explore-hub`, `tc-explore-hero`, etc. At the time those samples used **Tailwind** (not WordPress-native). Cursor has already rebuilt the **membership/toggle page** to match the **Vercel** look.

**Reference file:** `docs/brand-references/vercel-and-10web-comparison.pdf` (28 pages of annotated screenshots).

### Preference ranking (overlays)

1. **Vercel overlays** — preferred for polish (legible hover, not too dark).  
2. **10Web overlays** — strong, sometimes preferred for toggle UI.  
3. **Current WordPress staging** — not the target (crops, black/white bars, broken EXPLORE, stale links).

### Hub tiles (6 hubs) — intended behavior

- Large, high-resolution images; full tile is the visual plane (not a tiny cropped patch).  
- **At rest:** title sits at the **bottom** of the image.  
- **On hover:** image lifts / responds; title **rises toward middle**; a clean transparent **EXPLORE** control appears underneath.  
- **Entire image is linked** to the hub landing page (click works even if EXPLORE is missed).  
- EXPLORE must read as one word — never split (`EXPLOR` / `E`).

### Guide / collection cards (Vercel “Start With a Guide…”)

- At rest: strong photo, title over image (usually bottom).  
- On hover: soft dark translucent overlay (readable, **not** crushed black); title can move up; short description + “View Collection →” appear; subtle lift/shadow.

### Membership / toggle (10Web vs Vercel)

- Toggle changes the look and destination of the panels.  
- **Four different looks** depending on toggle state.  
- Cursor already aligned the WP toggle page toward **Vercel**. Prefer that direction unless Daniel says otherwise.

### Smaller product tiles (sub-child grids)

- Too small for long descriptions on the image.  
- On hover: two transparent bottom controls — **Details** | **Reviews** (star grade for products/items; not the same pattern for books).  
- Equal card sizes; no random black bars or white-out strips.

### Hero / cover

- **10Web “cover”:** image present on load; words + button animate into the center.  
- **Vercel:** top placeholder for video called out as high value.  
- Classes historically used on WP: `tc-explore-hero` (hero) and `tc-explore-hub` (hub/product tiles).

### Explicit non-goals for §1

- Do not treat Tailwind sample code as drop-in WP CSS.  
- Do not use another Hostinger restore to “get the Vercel look.”  
- Do not leave 10Web plugin changes to Angie unless Daniel asks.

---

## §2 — (next)
*(Waiting for next section from Daniel.)*
