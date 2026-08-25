# Truth Collective — Master Execution Order (Staging Repair to Launch)

One ordered plan for repairing `tcstaging.truth-collective.com`, making it audit ready, migrating it to live, and running post launch steps in the correct sequence.

## Authority and ownership

- Cursor authored. Cursor leads sequencing and applies changes by REST, and owns Additional CSS with Daniel. Per `docs/AI-PLATFORM-RULES-AND-PROMPTS.md`, Claude drafts copy only and Copilot Task is blocked under Plan B.
- This plan implements, and does not replace, `docs/TC-STANDING-BRIEF.md` (priority order in section 13, phases in section 14, SEO in section 4), `STAGING-RECOVERY-HANDOFF.md`, and the Migration Brief summary (section 6). If anything conflicts, the Standing Brief wins until Daniel confirms an update.
- Living document. Update only with Daniel confirmation (Master Brief rule).

## Ground rules that carry through every phase

- Staging only: `https://tcstaging.truth-collective.com`, Hostinger `public_html/tcstaging`, DB `u867403816_jdn2C`. Live is separate under `public_html`. Never use Website backup restore for staging.
- No restore roulette. Fix the cause, not the symptom. No Jul 24 style full restores for the crop, link, or CSS symptom set.
- About 99 percent certainty or stop and ask.
- One page family at a time. Health limited pace, short steps.
- Never rename, merge, or delete locked classes: `tc-book-card`, `tc-product-card`, `tc-leadership-body`, `tc-book-button`, `tc-card-row`, `tc-overlay-card`, `tc-overlay-card-product`, `tc-explore-hub`, `tc-grade-block`, `tc-rating`, `tc-tech-intro`, `tc-explore-hero`.
- Content rules: no em dashes, no bold body, no contractions, no hype, affiliate only products, no fabricated facts.
- Additional CSS is Cursor plus Daniel only. Do not paste AI generated CSS into the site.
- Back up page content before any write. Save the prior raw to `diagnostics/backups/` with page id and date.
- Do not change published or indexed slugs.

## Verified current state (2026-08-25, read only REST)

- Access: REST authenticates as administrator. WordPress secrets are set as Environment scope, so future Truth Collective agents inherit them.
- Pages: 69 total, 59 published and 10 drafts. Content is intact, not deleted. The missing look comes from drafts, wrong tile links, and leftover or missing CSS.
- The 10 draft pages, hidden from the front end:
  - 8176 Toggle Page. Complete membership email unlock toggle. Needs publish plus a CSS check.
  - 92 High Performance and Execution. Recommended Books child.
  - 392 Entrepreneurship and Business Building. Recommended Books child.
  - 1394 Video Technology Devices and Interactive Visual Displays. Technology child.
  - 2962 Premium Interactive Digital Displays. Technology child.
  - 2553, 2554, 2555 The Truth Untold Series Parts 3, 4, 5.
  - 5938 Projectors, Screens, and Video Collaboration. No parent, no slug.
  - 6043 The Truth Collective Series Part 7, 8, 9, 10.
- Structure item: AI Mastery Book Collection (page 96) sits at top level, not nested under Recommended Books (page 38) where the brief places it. This is why it can look missing from the Books hub.
- Known display items to verify per page: wrong or old hub tile links that 404, leftover or missing `tc-` classes, and sitewide flicker from stacked overlay and explore CSS.

## Phase 0 — Access, safety, working method (in progress)

Goal: a safe, repeatable REST workflow with backups.

1. REST auth confirmed. Done.
2. Backup routine: every write first saves the prior page raw to `diagnostics/backups/` with page id and date. Cursor.
3. Additional CSS edited only by Cursor plus Daniel.

Gate: no content writes until the backup routine is in place.

## Phase A — Stabilize staging (make the real content visible)

Goal: remove the missing look without adding new content yet.

1. Decide the fate of each of the 10 drafts. Cursor shows each draft content first, Daniel decides publish, keep draft, or delete.
2. Hub tile links. For each hub, compare every tile URL to the real page permalink, list mismatches, correct them in `post_content`, one hub at a time. Start with the Office hub File Cabinets tile, which points at a wrong short URL.
3. AI Mastery. Nest page 96 under Recommended Books (38), or correct the Books hub tiles to point to it, per Daniel choice.
4. Sitewide flicker. Name one Additional CSS block to disable, test, and confirm. Cursor plus Daniel.

Gate: navigation works, no obvious 404 tiles, flicker addressed, before adding content.

## Phase B — Hub information content (inform viewers)

Goal: concise informative content on hub pages, lighter than before.

1. Cursor lists each hub and the content slot it needs, for example an intro and one or two informative paragraphs and category framing.
2. Claude drafts hub copy per ticket. Voice rules enforced. No HTML, no CSS.
3. Cursor wraps approved copy in safe Custom HTML using locked classes and applies by REST, one hub at a time.
4. Daniel views each hub and approves.

Gate: each hub reads as informative and on brand before polish.

## Phase C — Page family repair (cards, classes, toggle)

Goal: repair product, book, and overlay blocks that lost classes or styling.

1. Membership toggle (8176). Confirm the `body.page-id-8176` CSS is in Additional CSS, publish the page, verify the render.
2. Repair child pages where `tc-` classes were stripped. Per page check. Delete and rebuild ghost blocks rather than long repairs.
3. Verify product cards, grade blocks, and overlays render on a sample from each family: books, office, technology, lighting.

Gate: one healthy template per family confirmed.

## Phase D — Images (Daniel inserts, Cursor verifies)

Goal: replace placeholders with final images.

1. Cursor lists every placeholder with expected size. Hub tiles target 1600 by 1000 per the image guide. Category tiles per launch tips.
2. Daniel replaces images in the editor.
3. Cursor verifies sizes and that images do not spill outside their boxes.

Gate: no placeholder images remain on pages slated for launch.

## Phase E — Site wide polish

Goal: Vercel light, readable overlays, less bulk, no flicker.

1. Reduce and consolidate leftover overlay and explore CSS add ons, one named block at a time.
2. Apply the light hover language within locked classes.
3. Preserve the membership toggle pattern. Do not make it heavier.

Gate: pages feel light and readable, EXPLORE never splits, overlays legible.

## Phase F — SEO and pre audit readiness

Goal: meet the per page SEO standard in Standing Brief section 4.

1. Per page: focus keyword in title, meta under 160 characters, one H1, at least one H2, keyword in the first paragraph, hero alt text. Title under 60 characters and includes 2026.
2. Internal links: up to parent, down to children, three to four siblings. FTC pattern paragraph present.
3. Configure RankMath schema in the UI. Do not edit RankMath PHP.
4. Sitemap returns 200, robots not blocking, no `__trashed` URLs, no duplicate hub titles.

Gate: SEO checklist passes on launch pages.

## Phase G — SEMrush audit and fixes

Goal: run the audit only when navigation and templates are trustworthy.

1. Run the SEMrush site audit on staging.
2. Triage. Cursor fixes proven technical issues, Claude drafts copy fixes, Daniel handles media.
3. Re-run to confirm.

Gate: audit clean enough for launch per Daniel.

## Phase H — Pre migration freeze and backups

Goal: a safe, reversible migration starting point.

1. Freeze content changes on staging.
2. Back up staging files and DB. Back up live files and DB. Export the Additional CSS text.
3. Export the Google Search Console indexed URL inventory for the live site. Build the 301 map for any path changes.

Gate: all backups and the 301 map exist and are verified.

## Phase I — Migrate staging to live (preserve only)

Goal: an exact working copy of staging on live. Preserve, do not improve during migration.

1. Prefer Method A, a full clone package, after a confirmed live rollback backup.
2. Serialization safe replace of `tcstaging.truth-collective.com` to `truth-collective.com`.
3. Carry over all Additional CSS, locked classes, and rules exactly.
4. Post check: hover every card type, compare CSS line count, confirm schema, confirm no staging URLs remain, confirm the FTC footer.

Gate: live renders the same as approved staging, no staging URLs left.

## Phase J — Launch and Google Search Console

Goal: replace the old broken live site and get the new one indexed.

1. Confirm the new live site serves at the root domain.
2. Submit the sitemap in Search Console. Request indexing for key pages.
3. Apply 301 redirects from old paths to new per the map.
4. Verify coverage and fix crawl errors.

Gate: key pages indexed, redirects resolve, no coverage errors on the money pages.

## Phase K — Post launch monitoring and growth

Goal: stabilize, then grow.

1. Monitor Search Console coverage and Core Web Vitals.
2. Mobile polish pass, deferred until desktop is stable.
3. Resume social and Pinterest per Standing Brief section 13 step 5.

Gate: none. Ongoing.

## Immediate next actions (this session)

1. Toggle page 8176. Confirm the `body.page-id-8176` CSS is in Additional CSS, then publish. Reversible.
2. Draft decisions. Cursor prepares the 10 draft decision list with a short summary of each, for Daniel to mark publish, keep, or delete.
3. Link audit. Cursor produces the hub tile link audit, one hub at a time, starting with Office and Technology.

## Owners

- Cursor: leads, sequences, applies changes by REST, owns Additional CSS with Daniel, backs up before writes.
- Daniel: approves each step, inserts images and media, handles Hostinger and Search Console, revokes or rotates credentials.
- Claude: drafts copy only, under Cursor tickets. No HTML, no CSS.
