# Truth Collective — Standing Brief

Living brief for Cursor and Angie. Full source docs live in `docs/brand-references/`.  
Update only with Daniel’s confirmation (Master Brief rule).

**Sources ingested 2026-08-08:**
- `vercel-and-10web-comparison.pdf` (§1)
- `TC_Master_Brief_update_2.0_5_26_2026.docx` (§2–§5)
- `TC_Cursor_Migration_Brief.docx` (§6)
- `Cursor_tips_for_launch_6.docx` (§7)
- `HEARING_TRACKER_WEBSITE_TO_COMPARE_TC_WEBSITE.docx` + TechRadar screenshots (§9)
- Membership toggle CSS (§11) + Copilot Task Master Binder archive (§12)

**Session open line:** Read `docs/TC-STANDING-BRIEF.md` and `STAGING-RECOVERY-HANDOFF.md`, then continue.

---

## §1 — Visual / motion gold standard (Vercel + 10Web samples)

**Context:** After a live-site crash and failed recovery, Daniel explored **Vercel** and **10Web**. Their sample pages defined hover / lift / overlay language later named `tc-explore-hub`, `tc-explore-hero`, etc. Samples used Tailwind (reference only, not WP drop-in). Cursor already rebuilt the **membership/toggle page** toward **Vercel**.

**Reference:** `docs/brand-references/vercel-and-10web-comparison.pdf`

### Preference ranking (overlays)
1. **Vercel overlays** — preferred polish (legible hover, not crushed dark)
2. **10Web overlays** — strong (toggle UI sometimes preferred)
3. **Broken WP staging** — not the target

### Hub tiles (`tc-explore-hub`)
- Large high-res images; full tile is the visual plane
- **At rest:** title at **bottom** of image
- **On hover:** image lifts and slightly darkens; title rises; transparent **EXPLORE** (hubs may use gold `>`). Entire image is linked
- EXPLORE is **not a button** — look-alike label driven with JS/CSS; **the entire image is the link**
- EXPLORE must never split (`EXPLOR` / `E`)
- Target placement: class on the intentional block (historically image and/or Section — see layer history below). Do not invent a third class system.

### Overlay cards (`tc-overlay-card`)
- Structure: Group (GTB) → often Row (KD) → Section (KD) → header + image + paragraph
- Class **only on Section:** `tc-overlay-card` (product modifier `tc-overlay-card-product` sits **beside**, never replaces)
- Hover: lift, slight darken, title moves up, description reveals in bright white; whole card linked

### Overlay + Explore layer history (Daniel 2026-08-08 — recovery critical)

1. **First:** `tc-overlay-card` on **Section** (Kadence) only.
2. **Separately:** `tc-explore-hub` on **images** — EXPLORE look-alike + whole-image link (not a real button).
3. **Later:** both used **together** on some pages → **CSS conflict → image crop** (one layer overriding another).
4. Cursor then appended **many add-on patches** for each circumstance, each claiming no collision with locked classes — still stacked in Additional CSS.
5. Images also had to be **specific sizes**; wrong dimensions made the CSS behave oddly.

**Recovery rule:** Expect many Explore/Overlay add-ons. Do **not** delete the whole Explore system in one pass. Identify which **later add-on** fights the combo (both classes present) vs the original single-class behavior. Disable one named add-on block at a time and re-check the page that crops.

### Book cards (`tc-book-card`)
- Section: `tc-book-card`; paragraphs: `tc-leadership-body`; parent button: `tc-book-button`
- At rest: cover + title + author only; hover: lift + descriptions roll down; leave hover: roll up

### Smaller product tiles
- Hover: **Details | Reviews** (grades via `tc-grade-block`); equal sizes; no black/white bars

### Hero (`tc-explore-hero`)
- Cover-style entrance; EXPLORE without gold arrow on pure heroes (arrow OK on hub tiles)

---

## §2 — Brand, voice, and permanent content rules

**Who:** Premium affiliate site by Daniel Reid (Duke BS; Executive MBA Queens University of Charlotte; 30+ years national BD / construction; works through cancer treatment). Sells **decision certainty**, not products. Trust flywheel, not conversion funnel. Goal: top 1% affiliate authority.

**Voice:** Premium, calm authority, truth-first. Confident, never loud. Direct, never abrasive. Specific beats vague.  
On-brand: "Books that compound over years. Skip the noise."  
Off-brand: "You won't believe what this book did for me!"

**Permanent content rules (never violate):**
- No em dashes (use periods, commas, or restructure)
- No bold in body (headlines/labels only)
- No contractions sitewide
- No clickbait, no exclamation points, no hype
- No fabricated facts/contacts
- No medical/financial/clinical claims language
- No guessing; no workarounds unless only option and approved
- No rewriting approved structures without strong reason
- **Affiliate-Only Rule:** never feature a product/brand without an active affiliate partnership
- Current partners noted in Master Brief: AWIN, SwitchBot, Wayfair, Birch Lane, ShareASale, PartnerStack; CJ applied pending

**Colors (locked):** navy `#1e3a5f` · charcoal `#1f1f1f` / `#1a1a1a` · cream `#f8f4ec` / `#faf9f6` · white `#ffffff` · gold `#b8944b`  
**Type:** Playfair Display (headlines) · Inter (body)

**Mission note:** Some Self-Help / Mental Wellness pages are non-monetized people-help resources (crisis lines, verified directories). Open door after launch for contact/help. If a product is not listed, it did not meet selection standards.

---

## §3 — Locked CSS classes (never rename, merge, or “improve”)

`tc-book-card` · `tc-product-card` · `tc-leadership-body` · `tc-book-button` · `tc-card-row` · `tc-overlay-card` · `tc-overlay-card-product` · `tc-explore-hub` · `tc-grade-block` · `tc-rating` · `tc-tech-intro` · `tc-explore-hero`

Uniform image sizing rules are intentional. Images must not spill outside their boxes.

---

## §4 — Site structure, SEO, product grade, launch intent

**Hubs:** Recommended Books · Office Workspace · Technology · Smart (AI) Lighting · Featured Productivity Tools · Self-Help and Mental Wellness · plus editorial **The Truth Untold Series**

**SEO (every page):** focus keyword in title, meta (&lt;160), H1, ≥1 H2, first paragraph, hero alt; density 0.5–1.5%; title &lt;60 chars and includes **2026**; RankMath Content AI during writing.  
Title framework: `Best [category] for [audience] in 2026 | Truth Collective`  
**Slug lock:** never change a published/indexed slug.  
Internal links: up to parent, down to children, sideways 3–4 siblings. External FTC pattern paragraph locked.

**Product standards:** ≥3.5/5 long-term reviews; pro daily-use quality; sensible returns; trusted retailer. Grade via `tc-grade-block` (may differ from retailer).

**Launch money pages (historical target):** Best Standing Desks · Best Office Chairs Under 500 · Best Monitors for Productivity. Then SEMrush, fix proven issues, go live.

**Publish gate:** technical render · trust · FTC disclosure · internal links · index-worthy · clear next step.

---

## §5 — Operating mode (how Cursor must work)

- **99% certainty or stop.** Never guess. Look at uploads before commenting.
- Prefer ranked expert next step over menus of choices (Master Brief). During **staging recovery / health-limited sessions**, still use **one short step** so Daniel is not overloaded.
- Fix the issue and cause; do not invent parallel CSS systems per page.
- Do not edit RankMath plugin PHP; configure schema in RankMath UI.
- Staging work stays on staging until hierarchy, URLs, and hub tiles are locked.
- Angie executes only Cursor-written one-task prompts (`diagnostics/ANGIE-CONTROL.md`).
- Leave **10WEB manager** alone until Daniel asks.
- No Hostinger restore roulette; never Website backup restore onto live by mistake.

**AI stack roles:** See **§10**. Cursor + Daniel own all Additional CSS. Claude = aesthetics/formatting only (no paste-in CSS). Angie = Cursor-directed WP actions. V0/Vercel/10Web = visual reference. ChatGPT/Copilot out of CSS path.

---

## §6 — Staging → live migration (summary)

Full plan: `docs/brand-references/TC_Cursor_Migration_Brief.docx`

- Goal: exact working copy; **preserve**, do not improve/refactor animations or Additional CSS
- Back up staging + live + export Additional CSS text before any live touch
- Export GSC indexed URL inventory; build 301 map for path changes
- Prefer Method A: full clone plugin package after live rollback backup confirmed
- Serialization-safe replace `tcstaging.truth-collective.com` → `truth-collective.com`
- Post-check: hover all card types, CSS line count, schema, no staging URLs left, FTC footer, sitemap submit
- Stop at every stop point if certainty &lt; 99%

**Do not run migration while staging recovery is incomplete.**

---

## §7 — Launch tips still in force (Jun 2026)

Full note: `docs/brand-references/Cursor_tips_for_launch_6.docx`

- Hubs need image + title + one line + EXPLORE; depth lives on children
- Hub tiles: **3 columns**, not 4; block order image → title → brief
- Before migrate: hub/child URL map, robots not blocking, sitemap 200, no `__trashed` URLs, no duplicate hub titles
- Image export target often **1000×800** for category tiles (keeps rows even)
- LiteSpeed purge after CSS/block changes
- Speakers scope may broaden from office-desk to speakers-by-type — decide slug/parent before cloning many tiles

---

## §8 — Current recovery override (Aug 2026)

See `STAGING-RECOVERY-HANDOFF.md`. Short version:
- Crops / EXPLORE damage / uneven cards = leftover conflicting CSS + stale hub block URLs, not “delete all pages”
- Fix with controlled Angie/Cursor edits; not more restores
- File Cabinets page exists; Office hub tile still points at `/file-cabinets-credenza/` (wrong)

---

## §9 — Competitor polish references (feel, not clone)

**Sources:** Hearing Tracker note + TechRadar screenshots (2026-08-08).  
**File:** `docs/brand-references/HEARING_TRACKER_WEBSITE_TO_COMPARE_TC_WEBSITE.docx`  
**Sites:** https://www.hearingtracker.com · https://www.techradar.com

These are **polish / UX references**. Keep Truth Collective locked palette and type (§2). Do not import TechRadar magenta/dark-news skin as the TC brand system.

### Shared feel targets
- Polished, professional, **not heavy or blocky** / not big bulky blocks
- Generous spacing; clear hierarchy; high-quality imagery
- Motion that invites exploration (hover, light lift) without crushing readability
- Homepage can lead with **video or premium hero** (Hearing Tracker plays video on entry; Vercel samples also valued a video placeholder)

### 10Web / Vercel sample patterns to reach (screenshots 2026-08-08)
Confirmed from Daniel’s attachments (sample UI, not current WP staging):
1. **Air and lightness** — soft backgrounds, rounded light product cards, navy/gold CTAs, no stacked gray slabs
2. **Category tiles: grayscale at rest → full color on hover** — non-hovered neighbors stay B/W; hovered tile gains color, short blurb, bullets, “View Collection →”
3. **Editorial cards** — outlined titles, greyscale imagery at rest, color on hover; “Read Feature”
4. **About / newsletter** — clean two-column light or dark navy footers; Playfair + Inter; gold accents; not bulky form blocks
5. **Hero** — bright workspace photo, simple “Explore the Hubs” CTA, light motion on load (Vercel/10Web samples)

**Gap:** Current WP staging is heavier/bulkier than these samples. Direction is toward this lightness while keeping locked TC tokens and classes. Cursor CSS for the B/W→color effect was written for the 10Web sample; paste that CSS into the repo when available (`docs/brand-references/`).

### Hearing Tracker — match these three homepage jobs
1. **Premium visual hero** — immediate premium signal (TC: curated workspace, book stack, or Truth Untold cover / video)
2. **Clear intent routing** — “How can we help?” style paths (TC target: four paths such as Leadership, Workspace, Self-Development, Technology)
3. **Authority signals** — lab-tested / counted proof badges (TC: 30+ years executive experience, research hours with leaders, named hubs and featured series)

### TechRadar — lighter commercial layout, not TC identity
- TechRadar is **very commercial** — that is **not** Truth Collective.
- Useful only as proof a pro site can feel **lighter and less bulky** than current TC staging.
- Current TC heaviness came largely from earlier direction by ChatGPT, Copilot, and Claude (layout advice), not from Daniel’s brand intent.
- Borrow: air, hierarchy, modular clarity. Do **not** borrow: news-portal commerce tone, dark magenta skin, or dense promo chrome.

### Explicit non-goals
- Do not rebuild TC as a dark news portal or TechRadar clone
- Do not replace TC navy/cream/gold with TechRadar accents
- Do not start a homepage redesign mid-recovery until staging links/CSS are stable enough to trust what you see

---

## §10 — AI role split (mandatory)

| Who | Role |
|-----|------|
| **Cursor + Daniel** | **Only** parties who write/edit/paste **Additional CSS**, and who **authorize** staging changes (hand edit, Application Password/REST, browser-in-admin, or Angie prompts). Cursor owns complex HTML using locked `tc-*` classes. Claude’s “don’t give Cursor the keys” advice is **overridden** for staging — Daniel trusts Cursor more; staging-only credentials OK under one-task Approve rules. |
| **Claude** | Aesthetics judgment, long-paragraph rewrite, formatting. **No** production CSS and no unreviewed full-page HTML for Daniel to paste. Specs → Cursor. |
| **Copilot Task** | Strong **drafter** of Custom HTML / copy / page sections (matches DOM class names if told). **Cannot** log into wp-admin, FTP, or edit Additional CSS. Everything it writes is a **draft for Cursor review** before paste. Not a replacement for Angie. Tailwind/full-app HTML (e.g. Master Binder) is **not** drop-in WP. |
| **Angie** | In-WP agent (beta). **Paused** on critical path — spins/fails edits. Optional later if stable. |
| **ChatGPT / Copilot Edge** | Out of production CSS/HTML path (historical damage). |
| **Vercel / v0 / 10Web samples** | Visual reference only — not WP repair agents. |

**Must:** No other generative AI puts code into Additional CSS. If Claude proposes CSS, Cursor reviews and implements or rejects. Daniel does not paste Claude, ChatGPT, or Copilot CSS into the site.

### 86-page polish pipeline (after staging is stable — Phase R)

Goal: Daniel does **not** manually rebuild ~86 pages by hand forever. Pipeline:

1. **Claude and/or Copilot Task** draft long copy + optional HTML **using only locked `tc-*` classes** (Cursor supplies the class list). No Tailwind CDN apps. No Additional CSS.
2. **Cursor** reviews/rewrites that draft into safe Custom HTML (genius at structure/conflict checks; weaker at pure aesthetics — so Claude/Task feed taste, Cursor ships code).
3. **Applicator:** Daniel hand-paste, **or** Cursor via staging Application Password / browser-in-admin, **or** Angie if beta works — **one block/page family at a time**.
4. Repeat by page family. Corrupted ghost blocks → delete + replace, not four-day repair.

**Honesty check — Copilot Task’s own limits:** It can write paste-ready blocks and match classes; it **cannot** push to the server or open wp-admin. So it is **not** “anything and everything” alone. With Cursor in charge as reviewer + applicator, Task is a strong **content/HTML factory**. It is not Angie and not Additional CSS owner.

**Division of taste vs code:** Cursor = problem-solving, complex HTML/CSS, WP auth changes. Claude/Copilot Task = aesthetics and content drafts under Cursor veto.

---

## §11 — Membership toggle (known-good Cursor CSS)

- Vercel-aligned light toggle using TC navy/gold/cream tokens
- Reference file: `docs/brand-references/tc-membership-toggle.css`
- Scoped page id in CSS: `body.page-id-8176`
- Preserve this pattern; do not “improve” into a heavier card system

---

## §12 — Technical evaluation engine (paused; resume later)

**Intent (Cursor + Copilot Edge + Copilot Task):**
- Copilot Edge: quantitative/qualitative engineering evaluation docs and SME governance spec sheets
- Copilot Task: interactive **Master Binder** UI (example: Premium Display Intelligence)
- Cursor: complex HTML so Daniel enters product URL or ID → descriptive summary + expert grade/rank that is **technical, not subjective**
- Two tracks:
  - **Quantitative** — physical products (Master Binder pattern)
  - **Qualitative** — books, editorials, scripts, etc.
- Paused when the site crash hit. Do not discard. Resume after staging is stable.

**Captured artifact (2026-08-08):**
- Docs: `docs/brand-references/master-binder-premium-display-intelligence.md`
- Tokens: `docs/brand-references/master-binder-tc-tokens.css`
- Share: https://copilot.microsoft.com/shares/artifacts/Z6LhgwiDPF9L2D8JPqHTd
- Structure: Governance → Scoring (expectation gap, 80/10) → Technical Ref → Editorial FAQ → Ranked Top 20 → filterable Master Grid → Glossary
- Tailwind sample only — **Cursor + Daniel** port to WP; never paste Copilot HTML into Additional CSS as-is

**Copilot Task site audit (2026-08-08) — conflict framing (locked):**
- Binder was built from four prior docs only — **not** from live/staging inventory.
- Site = full curated TC-graded catalog. Binder = executive/premium editorial intelligence. Different jobs.
- High conflicts if treated as one catalog: Amazon ★ vs TC Grade; many Top 20 SKUs not on site; some models differ (e.g. ASUS PA32UCXR vs site PA32UCDM; Samsung G9 variants).
- That mismatch is OK if framed as companion editorial, not product inventory.

**Launch decision (Daniel + Cursor — do not reopen during recovery):**
- **Option 1 only for launch:** keep product pages; add a short CTA to a separate Master Binder child page after staging overlays/links are stable.
- **Do not** Option 2/3 before launch (no SKU rewrite, no product-page redo, no full binder reconciliation).
- **Do not** let Copilot Task paste its full Tailwind HTML into Gutenberg / Additional CSS / theme files.
- Copilot may draft CTA copy only. **Cursor + Daniel** own any WP HTML/CSS and locked `tc-*` classes.
- Animations stay safe by reusing locked classes or adding new unique classes — never editing the animation stylesheet during binder work.

**Rules when resumed:**
- Cursor owns implementation code (Additional CSS / custom HTML)
- Claude may critique aesthetics only
- Grades stay standards-driven (Selection Standards / SME governance), never vibe scoring
- Site TC Grades are authoritative on product pages; binder star decoder is consumer-sentiment education unless later rewritten in TC Grade language (post-launch Option 3)

---

## §13 — Priority order (locked; Daniel 2026-08-08)

Top-1% quality is the destination. Order of work is non-negotiable:

1. **Fix staging** — overlays, wrong hub links, leftover AI CSS damage. No new feature work that risks another break.
2. **Improve / polish** — Vercel-level hover language, light commercial feel, locked `tc-*` classes only.
3. **Semrush audit** — after staging looks launch-ready, not before.
4. **Launch** — staging → live per Migration Brief preserve-only rules (§6).
5. **Post-launch growth** — Pinterest boards/pins, resume posting on **8 Truth Collective business social accounts** (currently zero followers / idle because live has sat broken ~60+ days).

**Context:** ~5 weeks already spent repairing Claude / ChatGPT / Copilot Edge mistakes. Live site idle and broken. Daniel will not redo product catalogs for binder polish. Helpers must not invent parallel workstreams (binder SKUs, social strategy, Semrush) until step 1 is done.

**Default next action (Daniel 2026-08-08):** **Angie Phase S (stable)** then **Phase R (rebuild page-by-page)**. See `diagnostics/ANGIE-CONTROL.md`. No more multi-day ghost-block repair; corrupted blocks are deleted and rebuilt. No Hostinger restore roulette. Computers revision hunt closed.

**Ghost / wrong-link rule:** Slug and URL can look correct and still fail. Do not spend days hunting invisible corruption. Delete the bad block; rebuild with Cursor + Angie.

**Global symptom:** staging **flickers badly on every page** (Daniel). Not limited to one hub. Likely stacked explore/overlay CSS — not a Hostinger restore issue.

**Queued after desktop recovery (not now):** Mobile / phone layout is badly broken (Daniel spot-check; possible 10Web-migration overlap, unconfirmed). Address in polish phase — do not open a mobile workstream during CSS/link recovery.
