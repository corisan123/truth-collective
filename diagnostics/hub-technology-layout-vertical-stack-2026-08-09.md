# Technology Hub — vertical stack / old look (2026-08-09)

**Status:** Diagnosed. **R4 APPLIED** 2026-08-09 via REST (Cursor Staging Recovery II).

## What Daniel reported
- Cream / navy work is getting better
- Page still feels **all vertically stacked** and **old looking**
- 10Web did not keep layout vertically inline; things moved around in the mock (mood board only — we do not port 10Web HTML)

## Root cause on staging (page `111`)
1. **Hero (R3)** — cream split hero is the improved part (navy rail + cream copy). Horizontal.
2. **Below the hero** — the old **Technology Hub Categories** stack is still live: long heading list (Printers, Keyboards, Charging, Wearables, Holographic, Robots, Smart Home, Emerging…), mostly tall photo/text rows with `tc-explore-hub` **and** `tc-overlay-card` together.
3. That lower stack is why the page still reads as a tall 2019-era hub, not the airy 10Web cream grid.
4. Many of those old headings are **not** the eight real published children.

## Real children (R4 tiles — authoritative)
1. Computers → `/technology-hub/computers-digital-devices/`
2. Monitors → `/technology-hub/monitor-display/`
3. Audio & Video → `/technology-hub/audio-and-video/`
4. Headphones → `/technology-hub/headphones-for-work/`
5. Speakers → `/technology-hub/speakers-home-office-outdoors/`
6. Projectors & Mics → `/technology-hub/projectors-and-microphones/`
7. Tablets → `/technology-hub/best-digital-smart-tablets/`
8. Interactive Displays → `/technology-hub/interactive-digital-displays-2/`

## Image note (sitewide concern)
- On several hubs, **upload files return 200** — the “sizes no longer fit” look is often **CSS crop** from Explore + Overlay stacked (`min-height` + `object-fit: cover` + absolute fill), not a missing file.
- **Computers** child page is worse: most product `/uploads/` URLs **404**. That is a selective media/File Manager problem, separate from hub tile CSS. Do **not** Jul 24 full-site restore for this.

## Next ticket
`REST-hub-technology-R4` — replace old Categories→(before Final Thoughts) with cream **3-column** tile grid of the eight children; page-scoped `TECH-HUB-CREAM-R4`; no `tc-overlay-card` on these tiles (avoids combo crop).

**Blocked on:** staging Application Password (current credentials return **401** on `/users/me` and `context=edit`).
