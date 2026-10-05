# Truth Collective — Staging to Live Migration Brief

**Source:** `docs/brand-references/TC_Cursor_Migration_Brief.docx` (plain-text mirror for agents)  
**From:** `https://tcstaging.truth-collective.com` → **To:** `https://truth-collective.com`

## Purpose

Migrate the Truth Collective staging site to the live domain with zero loss of HTML, CSS, formatting, animation, schema, redirects, or locked rules. Read this entire document before taking any action. Do not improvise, rewrite working code, or substitute your own approach for the steps below. Where certainty is below 99 percent, stop and report back rather than guessing.

## Critical context

A previous AI crashed the original live site by converting HTML to CSS for overlays without understanding the existing code. Six weeks were lost. This migration must not repeat that failure. Every existing class, animation, and rule is intentional and must survive the move exactly as built. The single highest priority is **preservation**, not improvement.

**Do not run this migration while staging recovery is incomplete.** See `docs/TC-STANDING-BRIEF.md` §13 and `STAGING-RECOVERY-HANDOFF.md`.

---

## 1. Non-negotiable rules

These rules override any default behavior. They apply to every step.

- **Preserve everything.** Do not delete, rewrite, refactor, optimize, or reformat any HTML, CSS, or animation. Goal: an exact, working copy on the live domain.
- **Do not modify locked CSS classes:** `tc-book-card`, `tc-product-card`, `tc-leadership-body`, `tc-book-button`, `tc-card-row`, `tc-overlay-card`, `tc-overlay-card-product`, `tc-explore-hub`, `tc-grade-block`, `tc-rating`, `tc-tech-intro`, `tc-explore-hero`.
- **`tc-overlay-card-product`** always sits beside `tc-overlay-card`, never replaces it.
- **Do not edit RankMath plugin files.** Schema is configured in the RankMath interface, never in plugin PHP.
- **Do not change any published slug.** Slugs are permanent once live and indexed.
- **Content rules:** no em dashes, no bold body text, no contractions in any content Cursor touches. Match Master Brief 2.0.
- **Stop if uncertain.** No guessing. No workarounds unless a workaround is the only option and is approved first.

---

## 2. Pre-migration inventory and backup

Complete this entire section before changing anything on the live site.

### 2.1 Full staging backup

- Complete backup: all files and full database (hPanel backup tool plus a second export via All-in-One WP Migration or Duplicator).
- Store both backups in two locations (local working folder and Google Drive). Confirm both copies are complete and openable.
- Export **Additional CSS** separately as plain text and save with both backups.

### 2.2 Full live backup

- Complete backup of current live site (files and database) before any live change. This is the rollback point.
- Confirm the live backup is **restorable**, not just present.

### 2.3 Indexed URL inventory (Google Search Console)

- Export full list of indexed URLs from Pages and Performance reports for `truth-collective.com`.
- This list is the master reference for the redirect map (Section 5). Every indexed live URL must resolve after migration (same path or 301).

---

## 3. Asset and code preservation checklist

Confirm each item before migration and verify after migration.

| Asset to preserve | Verification after migration |
|-------------------|------------------------------|
| All Additional CSS (every line) | Compare line count and content; confirm identical |
| `tc-overlay-card` animations | Hover each card type; lift, darken, title slide, description reveal |
| `tc-explore-hub` / `tc-explore-hero` | EXPLORE label and gold arrow behavior on hubs/heroes |
| `tc-book-card` hover | Lift and three-paragraph description reveal |
| Image dimensions / uniform sizing | No images spill outside boxes |
| RankMath SEO fields per page | Focus keyword, SEO title, meta, slug |
| RankMath schema templates | TC Collection Page templates; `@type` intact |
| Internal links | Resolve to live URLs, not staging |
| FTC affiliate disclosure | Footer and per-page |
| Menus, navigation, header, footer | All nav points to live URLs |

---

## 4. Migration method

Confirm the single safest method with Daniel before executing. Do not mix methods.

### Method A — Full-site clone (recommended)

- Export entire staging site via All-in-One WP Migration or Duplicator.
- Import onto live domain, overwriting old live only after Section 2.2 backup is confirmed.
- Preserves database, theme settings, Additional CSS, RankMath, and block structure in one operation.

### Method B — Manual file and database transfer

- Only if Method A is not possible. Higher risk for serialized Customizer CSS and RankMath schema. Not preferred.

### Serialized URL replacement (critical)

After import, replace `tcstaging.truth-collective.com` → `truth-collective.com` using a **serialization-safe** tool (Better Search Replace or WP-CLI `search-replace`). Plain find/replace breaks serialized data. Dry run first, confirm counts, then run live.

---

## 5. Redirect map and 404 protection

Built from the Search Console inventory (Section 2.3).

- Same path on migrated site → no redirect needed.
- Path changed → 301 in RankMath Redirections from old path to new path.
- Preserve canonical direction (www/non-www, https). Staging paths were never indexed; redirect concern is **old live URLs only**.
- After migration, crawl live and confirm zero unexpected 404s against the indexed URL list.

---

## 6. Post-migration verification (in order)

1. Visual check every page (desktop and mobile).
2. Animation check on representative pages (all locked card types).
3. CSS integrity (Additional CSS line count vs pre-migration export).
4. Schema check (no undefined `@type` warnings; CollectionPage on hubs).
5. Link check (no `tcstaging` internal links; broken link scan).
6. RankMath per page (keyword, title, meta, scores).
7. Affiliate disclosure on every page.
8. SSL and canonical consistency.
9. Search Console: submit sitemap; request indexing on priority pages.

---

## 7. Sequence summary and stop points

Fixed order. Confirm at each **STOP** before continuing.

1. Back up staging (files, database, CSS). **STOP** — confirm restorable.
2. Back up live as rollback. **STOP** — confirm restorable.
3. Export Search Console indexed URL inventory. **STOP** — confirm saved.
4. Run SEMrush audit on staging. **STOP** — apply only proven fixes; re-back up after fixes.
5. Migrate staging → live via Method A. **STOP** if any preservation item is uncertain.
6. Serialization-safe URL replace (dry run, then live). **STOP** — confirm counts.
7. Build redirect map and apply 301s. **STOP**.
8. Full post-migration verification (Section 6). **STOP** — report failures before going public.
9. Submit sitemap and request indexing. Migration complete.

---

## Final instruction

Confirm the migration method with Daniel before executing. Preserve all code, CSS, animation, schema, and rules exactly. Stop at every stop point. The previous crash was caused by an AI acting without full understanding. Do not repeat it.
