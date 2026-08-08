# Homepage audit (staging, read-only) — 2026-08-08

**URL:** https://tcstaging.truth-collective.com/  
**Mode:** Public HTML only. No wp-admin. No Application Password.

## What is on the home page

- Same **~57KB+** Additional CSS payload as other pages: `tc-explore-hub`, `tc-explore-hero`, multiple `STAGING PATCH` blocks.
- Home uses hub/hero explore classes heavily (`tc-explore-hub` / `tc-explore-hero` present dozens of times in CSS + markup).
- Copy/content is present (mission, six hubs, guides). This is **not** an empty page.
- Visual risk matches siteswide: leftover Cursor `tc-explore*` / STAGING PATCH CSS can crop tiles, split EXPLORE, break overlays — same root cause as Technology Hub / Computers, not missing media.

## WordPress “faster access” option (answered for Daniel)

Likely means **Application Passwords** (Users → Profile → Application Passwords), which lets Cursor call the **WordPress REST API** authenticated (read/edit pages, sometimes Customizer CSS).

**Why not enable it for recovery step 1:**
- Write access can change many pages at once if misused — higher risk while we are undoing AI damage.
- Additional CSS edits: Cursor names the comment block; Daniel comments out or removes **one** block; Publish; check one URL.
- Public HTML + Angie one-task prompts are enough for diagnosis and the first fixes.
- Revisit Application Passwords later for the **86-page polish pipeline** (after staging CSS/links are stable), with a staging-only password and read/write limited to pages Cursor lists.

Also not needed now: enabling XML-RPC (security risk). SFTP/SSH helps file themes but Additional CSS lives in the DB/Customizer.

**Method lock:** Working CSS home remains **Appearance → Customize → Additional CSS**. Daniel has never used Code Snippets; that was a capability question only — not a favored-method change.

## Next homepage action (after CSS locate)

Do **not** rewrite the homepage yet. Find STAGING PATCH / `tc-explore` comment titles in Additional CSS, then disable one named conflicting block sitewide — that improves home + hubs together.
