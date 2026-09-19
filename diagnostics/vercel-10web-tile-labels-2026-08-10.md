# Salvage tile labels + page placement (Daniel 2026-08-10)

**Source:** Chat left→right from top-left; placement clarified same evening.  
**PDF:** Same file already at `docs/brand-references/vercel-and-10web-comparison.pdf` (md5 match). UI/hover gold — see `diagnostics/vercel-10web-sample-pdf-ingested-2026-08-09.md`.  
**Apply rule:** Use only tiles that fit the **page currently in progress**. These are salvage replacements for broken/wrong images — not a forced remake of every hub.

## Locked labels → intended page homes

| # | Label | Daniel placement | Staging match (when found) |
|---|--------|------------------|----------------------------|
| 1 | Robotics and AI Assistants | **Technology child** | No dedicated child under Tech Hub (id 111) yet — hold until page/URL confirmed |
| 2 | Smart Home Automation | **Technology child** | No dedicated Tech Hub child yet — hold |
| 3 | Smart Lighting Hero image | **Smart Lighting Hub** | `/smart-lighting/` (id 115) |
| 4 | AI Wearables | **Technology child** | No dedicated Tech Hub child yet — hold |
| 5 | Audio Video Hero Image | **Technology → Audio/Video** (hero) | `/technology-hub/audio-and-video/` (id 117) |
| 6 | Audio/Video | **Technology → Audio/Video** | same as #5 (tile vs hero) |
| 7 | Office Speakers | Technology Speakers (implied) | `/technology-hub/speakers-home-office-outdoors/` (id 1449) |
| 8 | Digital Tablets | **Technology → Tablets** (one of several) | `/technology-hub/best-digital-smart-tablets/` (id 1098) |
| 9 | Technologies and rapid changes (AR, VR, Holographics) | Technology-related (placement TBD) | No dedicated child found yet — hold |
| 10 | Filing Cabinets and Credenzas | Daniel said “Technology child A/V” — **conflicts** with label + live page | Live: Office Workspace child `/office-workspace-products-and-tools/office-file-cabinets-credenzas-essentials/` (id 6482). Treat as **Office Workspace** unless Daniel corrects. |
| 11 | Self-Care Meditation Essentials | **Self-Help & Mental Wellness** child — Rest / Rest–Meditation | `/meditation-essentials-calm-rest-reset/` (id 2005; titled Rest, Reset, & Meditation Essentials). WP parent currently `0` — intended under Self-Help hub (id 86). |
| 12 | Tablets | **Technology → Tablets** (another of several) | same tablets family as #8 |
| 13 | TC Video Cameras | **Sub-child of Audio/Video** | No child under A/V (117) in REST yet — hold URL; use when that page is the active job |
| 14 | Digital Interactive Displays — Office and Commercial | **Technology child** | `/technology-hub/interactive-digital-displays-2/` (id 5784) |
| 15 | Productivity Hub | **Productivity Hub** | `/productivity-tools/` (id 5680) |
| 16 | TC Books | Hero for one of ~20 book categories → Daniel: **Self-Help → Mental Wellness Books** | `/self-help-and-mental-wellness/mental-wellness-books/` (id 1931, parent 86) |

## Tech Hub note
Live Technology Hub children (parent 111) remain the locked eight: Computers, Monitors, Audio & Video, Headphones, Speakers, Projectors & Mics, Tablets, Interactive Displays.  
**#1 / #2 / #4 / #9 / #13** are Daniel’s intended homes — do not invent new hub grid tiles until those child pages exist and he asks to surface them on the hub.

## Keep packs separate

| Pack | File | Use |
|------|------|-----|
| Canva remade sitewide #1–#27 | `diagnostics/canva-remade-image-inventory-2026-08-10.md` | Product/workspace salvage tiles |
| This set #1–#16 | this file | Future-tech / hubs / branded heroes + placement map |
| AI Mastery (+ Part 6) | `diagnostics/AI-mastery-tile-order-2026-08-10.md` | Editorial section; Book Collections under Recommended Books |
| Vercel/10Web PDF | brand-reference | Motion/hover/layout gold — **not** WP HTML to port |

## Next
1. Confirm **#10**: Office Filing Cabinets (live) vs Technology A/V (said).  
2. Extract reachable PNG/JPG for the page in progress, then REST-swap matching tiles only.  
3. Current page in progress remains **Technology Hub** eight unless Daniel switches.
