# Truth Collective — Authoritative Hub Structure

## Hub placement rule (confirmed by Daniel, 2026-07-14)

Anything plugged in or digital goes to Smart Lighting or Technology Hub.
Anything office-related furniture, analog devices, and similar physical, non
digital items goes to Office Workspace Products and Tools. Check every future
placement decision against this rule before asking or guessing.

This supersedes any inference drawn from the sitemap alone. Confirmed directly by
Daniel on 2026-07-14, including the full child list for all 6 major hubs.

## 6 major hubs with confirmed children

### 1. Recommended Books (`/recommended-books-2026/`)

- Communication and Persuasion
- 100+ Leadership Books for Growth, Discipline, and Performance
- Decision Making and Strategy
- Entrepreneurship and Business Building
- High Performance and Execution
- Powerful Voices of Influence 2026
- Project Management Books
- Wealth, Money, and Investing Books

Confirmed deviation from the original Master Brief text: the Master Brief lists
AI Mastery Collection as one of the 9 book categories under this hub. Daniel's
current, confirmed direction is that AI Mastery Book Collection is its own
standalone parent hub (see editorial hubs below), not nested under Recommended
Books. This entry records that as the live, intended structure.

### 2. Smart Lighting for Home, Office and Wellness (`/smart-lighting/`)

- Smart Bulbs — per the hub placement rule, digital, belongs here. Needs
  reparenting: current URL is top-level (`smart-bulbs-light-strips`).
- Advanced Lighting for Indoors and Outdoors
- Smart AI Lighting and Rechargeable Devices
- Smart Lighting Controls
- Smart Security Lighting and Cameras

### 3. Technology Hub (`/technology-hub/`)

- Best Digital Smart Tablets 2026 — per the hub placement rule, digital, belongs
  here. Needs reparenting: current URL is nested under Office Workspace
  (`office-workspace-products-and-tools/best-digital-smart-tablets`). Action
  needed, not just confirmation.
- Professional Desk Speakers and Desk Audio — per the rule, digital, belongs
  here. No confirmed URL found yet. May correspond to
  `speakers-home-office-outdoors` or may be a separate, not-yet-verified page.
  Verify the live URL before wiring links or schema.
- Best Headphones, Headsets, and Hearing Protection for Work (`technology-hub/headphones-for-work`)
- Computers and Digital Devices (`technology-hub/computers-digital-devices`)
- Video Technology Devices and Interactive Visual Displays (`technology-hub/video-technology-and-interactive-displays`).
  Flag: the live page title still carries a leftover draft prefix, "DRAFT 6 15
  2026," in front of the real title. Remove before launch.
- Superior Interactive Digital Displays — per the rule, digital, belongs here.
  Needs reparenting: current URL is top-level (`interactive-digital-displays-2`).
- Best Monitor Setup for 2026, Premium Displays and Gear (`technology-hub/monitor-display`).
  Confirmed by Daniel, 2026-07-14, matches the placement rule. Master Brief updated.
- Premium Quality Projectors and Microphones for 2026 (`technology-hub/projectors-and-microphones`).
  Confirmed by Daniel, 2026-07-14, matches the placement rule. Master Brief updated.
- Premier Audio and Video Workspace 2026 (`technology-hub/audio-and-video`).
  Settled by the placement rule, digital, correctly placed here. No action needed.

### 4. Productivity Tools for 2026, Software and Systems

Single hub page, no children listed. Canonical is
`productivity-tools-software-and-systems`. Confirmed resolved: the homepage hub
tile row for this hub was corrupted. Daniel deleted the entire row and rebuilt
it. It now works. Same technique, delete and rebuild rather than repair, used
successfully here as it was for the menu.

### 5. Powerful Self-Help and Mental Wellness Resources (`/self-help-and-mental-wellness/`)

- Mental Wellness Books for Self-Help, Focus, Clarity and Calm (`self-help-and-mental-wellness/mental-wellness-books`)
- Mental Wellness Support, Recovery, and Resources 2026 (non-monetized) — flag:
  two similarly named URLs exist in the sitemap, `mental-health-support-services-and-helplines`
  and `mental-wellness-support-resources`. Confirm with Daniel which one is this
  live page before wiring links, rather than guessing.
- Rest, Reset and Meditation Essentials (`meditation-essentials-calm-rest-reset`)
- Self-Help, Self-Awareness, Self-Actualized (`self-help-books`)
- Podcasts, Conversations, Community for Mental Wellness (non-monetized) (`mental-wellness-resources`)

This reconciles with the Master Brief's "3 non-monetized resource pages": the
parent landing page itself, Support Recovery and Resources, and Podcasts
Conversations Community. Confirmed as 3 total, matching exactly.

### 6. Office Workspace Products and Tools (`/office-workspace-products-and-tools/`)

- Laptop Stands and Accessories (`office-workspace-products-and-tools/laptop-stands-for-work`)
- Smart Writing Products, Tools and Essentials — flag: current URL is top-level
  (`smart-writing-products-tools-essentials`), not nested under this hub. Named
  exception to the hub placement rule: Daniel explicitly placed this under
  Office Workspace, not Technology Hub, despite the "smart" name. Confirmed
  intentional, do not move to Technology Hub.
- Office Desk Essential Products in 2026 (`office-workspace-products-and-tools/office-desk-essential-products`)
- Cable Management, Executive Enterprise Setups 2026 — per the hub placement
  rule, a physical organizer, not itself digital, belongs here. Needs
  reparenting: currently sits under Productivity Tools
  (`productivity-tools/cable-management`), which does not fit either, since
  Productivity Tools is for software and systems, not physical accessories.

The 8 pages being reparented from `__trashed` URLs (see
`docs/playbooks/04-reparent-trashed-office-pages.md`) belong here too, once
fixed.

Confirmed resolved: the homepage hub tile row for this hub was also corrupted,
listed like the other hub tiles on the home page. Daniel deleted the entire row
and rebuilt it. It now works.

## Open items from this hub map

Resolved by the hub placement rule and Daniel's direct confirmation, action
now known, needs execution (reparent via Quick Edit, no SQL):

1. Best Digital Smart Tablets: move to Technology Hub.
2. Superior Interactive Digital Displays: move to Technology Hub.
3. Smart Bulbs: move to Smart Lighting.
4. Cable Management: move to Office Workspace (out of Productivity Tools).

Settled, no action needed:

5. Smart Writing Products: confirmed exception, stays under Office Workspace.
6. Audio and Video: confirmed correct under Technology Hub.
7. Monitor Setup and Projectors/Microphones: confirmed correct under Technology Hub.

Still genuinely open, cannot resolve without more information, do not guess:

8. Professional Desk Speakers and Desk Audio: confirm the live URL, not yet found.
9. Video Technology page title: remove the leftover "DRAFT 6 15 2026" prefix.
10. Mental Wellness Support/Recovery page: confirm which of the two similarly named URLs is correct.

## 3 editorial hubs (non-monetized or mixed, standalone from the 6)

### The Truth Untold

Editorial series. Standalone. Theme: leadership done well versus poorly, AI
exposing weak management. Primary LinkedIn content, secondary Pinterest.

### The Ones Who Gave Everything

Non-monetized tribute editorial hub honoring men and women who helped make the
world a better place. Parent page: The Ones Who Gave Everything. Child page
pattern: one honoree per page. First child, live this month if launched:
Reverend Billy Graham.

### AI Mastery Book Collection

Parent page: AI Mastery Book Collection (the Artificial Intelligence Books hub,
`/artificial-intelligence-books/`). Contains 8 book categories as children. The
parent page also carries an intro section for a separate editorial and podcast
series: 10 parts, sourced from the book pages, turned into podcasts and social
media posts. That series lives on its own page,
`/ai-mastery-podcast-collection/`, and is a distinct page from the hub.

## Self-Help and Mental Wellness hub detail

Per the Master Brief: 3 monetized book pages, plus non-monetized resource pages.
Daniel confirmed 2 non-monetized community-giving pages specifically for
substance abuse: hotlines, verified websites, and podcasts, every entry
triple-checked accurate. These sit alongside the parent landing page and the
mental wellness podcast/community page already in the sitemap:

- mental-health-support-services-and-helplines
- mental-wellness-support-resources

Both are non-monetized and must never receive Pinterest pins per the Master
Brief Pinterest standards (pins never link to non-monetized resource pages).

## Open item

Confirm whether the AI Mastery hub's 8 confirmed categories match the "Eight
Most Requested Categories" heading and the "Eight Book Categories" section
already on the live page, or whether some listed categories there do not yet
have child pages. Cross-reference against `docs/page-inventory.md` before
wiring the hub's ItemList schema.
