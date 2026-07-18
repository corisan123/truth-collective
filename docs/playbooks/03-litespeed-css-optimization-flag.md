# Playbook 03 — LiteSpeed CSS Optimization Risk (Deferred, Not a Launch Blocker Yet)

Observed on LiteSpeed Cache → Page Optimization → CSS Settings, 2026-07-14.

## Current settings

- CSS Minify: OFF
- CSS Combine: ON
- Generate UCSS: OFF (this is the important one, see below)
- UCSS Inline: OFF
- Load CSS Asynchronously: ON
- CCSS Per URL: OFF
- Inline CSS Async Lib: ON
- Font Display Optimization: Default

## Why this matters

Generate UCSS (Unique CSS) removes CSS rules a page scanner considers unused per
page. The `tc-book-card`, `tc-overlay-card`, and `tc-explore-hub` hover rules
only apply on `:hover`, so an automated unused-CSS scan can misidentify them as
unused and strip them, silently breaking the hover reveal, lift, and EXPLORE
animations sitewide. Keep Generate UCSS OFF permanently on this site unless a
change here is tested on a single page first and verified against the exact
component list in `docs/components/README.md`.

CSS Combine and Load CSS Asynchronously are lower risk, mainly affecting load
order and a possible brief flash of unstyled content. Not addressed now.

## Action

None right now. This is a deferred item, revisit during the Phase 0 systemic
pass in `docs/roadmap.md`, after the menu is fixed. Do not enable Generate UCSS
before that review.
