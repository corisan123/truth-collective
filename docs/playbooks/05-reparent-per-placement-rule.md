# Playbook 05 — Reparent Per the Hub Placement Rule (No SQL)

## The rule (confirmed by Daniel, 2026-07-14)

Anything plugged in or digital goes to Smart Lighting or Technology Hub.
Anything office-related furniture, analog devices, and similar physical, non
digital items goes to Office Workspace Products and Tools.

## Pages that need to move, per this rule

| Page | Current parent | Move to | Method |
| --- | --- | --- | --- |
| Best Digital Smart Tablets 2026 | Office Workspace Products and Tools | Technology Hub | Quick Edit, Parent dropdown |
| Superior Interactive Digital Displays | none (top-level) | Technology Hub | Quick Edit, Parent dropdown |
| Smart Bulbs | none (top-level) | Smart Lighting | Quick Edit, Parent dropdown |
| Cable Management, Executive Enterprise Setups 2026 (scope includes racks, IT gear, trays, stands) | Productivity Tools | Office Workspace Products and Tools | Quick Edit, Parent dropdown |

## Exact steps, repeat for each page

1. Pages, find the page by title.
2. Hover, click Quick Edit.
3. Parent dropdown, select the new parent from the table above.
4. Click Update.
5. Watch for the RankMath auto-redirect notice, confirm it fired.
6. Check the Canonical URL field per the same rule used in Playbook 04: if
   empty, nothing to do. If it hardcodes the old URL, clear it back to empty.

## After all 4 are moved

1. RankMath, Redirections, confirm 4 new entries exist, old URL to new URL, 301.
2. Purge both caches: LiteSpeed Cache plugin, Toolbox, Purge All, and hPanel,
   WordPress, Overview, Flush Cache.
3. Check each new URL and each old URL in a private window.
4. Add all 4 into the menu under their new parent, matching the nesting style
   already used elsewhere.

## Settled, no action needed

Audio and Video, Monitor Setup, and Projectors and Microphones are confirmed
correctly placed under Technology Hub. Smart Writing Products is confirmed as
an intentional exception, staying under Office Workspace despite its digital
sounding name. Do not move any of these four.

## Still open, do not guess

Professional Desk Speakers and Desk Audio has no confirmed live URL yet. Verify
before wiring any link or schema.
