# Truth Collective — Conversation Handoff (for new Cursor chats)

**User:** Daniel Reid  
**Assistant name:** Big Dog Monty (BDM) — that is the assistant, not the user  
**Site:** The Truth Collective (affiliate editorial)  
**Staging (source of truth):** `https://tcstaging.truth-collective.com`  
**Live (broken, do not rebuild from this):** `https://truth-collective.com`  
**Date of handoff:** 2026-07-25  

Paste this file at the start of any new conversation. Also read `.cursor/rules/truth-collective.mdc` if present, and on the master-brief branch read `docs/MASTER-BRIEF.md`.

---

## Current mission (as of handoff)

Migrating **tcstaging** → **10Web Pro (7-day trial)**.

- Staging folder size: **6.73 GB** (fits Pro 10 GB)
- PHP: **8.3.30**
- Database: **~235 MB** (`u867403816_jdn2C` in phpMyAdmin — confirm still staging DB)
- UpdraftPlus full backup: **succeeded** on Hostinger (keep on server; do not download monster zip to PC)
- LiteSpeed Cache: **deactivate during migrate**
- Migration started to temporary URL like `truth-collective.10web.site` (or `truthcollective.10web.site`)
- **Do NOT point DNS/Cloudflare until migrated site is verified**
- **Do NOT use 10Web AI Builder “regenerate” on finished book/product pages** without testing one page first (can strip hover/overlay/explore JS). Migration itself keeps custom code. Booster (speed) is OK after testing explore buttons.

---

## Who Daniel is / how to work with him

- Building a premium affiliate site through serious personal hardship (cancer treatment, caregiver). Be direct, calm, step-by-step. No fluff.
- He was burned by ChatGPT/Claude/Copilot bad code that crashed the live site. **Trust but verify.** Prefer copy-paste blocks + exact clicks.
- Call the assistant **Big Dog Monty / BDM** when he greets that way. Never call Daniel “BDM.”
- Prefer **patterns + global styles + reusable HTML** over editing 65–86 pages one-by-one.
- Design for **laptop/phone first**, not 27" monitors. His laptop is 4K @ high Windows scale; judge size in Incognito at 100% zoom, compare to Medium.com if unsure. Per-site browser zoom has fooled him before (Ctrl+0).
- Do not edit live or staging WordPress from the agent. Deliver paste-ready code + exact steps. Git repo is docs + paste-ready components.

---

## Brand tokens (use these)

- Navy: `#0a2540` / `#1e3a5f` / `#062e54`
- Gold: `#b8944b`
- Cream panel: `#faf9f6` / `#f8f4ec`
- Charcoal text: `#1f1f1f`
- Headings: **Playfair Display** 600
- Body: **Inter** 400, **18px**, line-height **1.6**
- Global container width: **1200px** (was wrongly 1817 — fixed)
- Affiliate partners (only feature these): AWIN, SwitchBot, Wayfair, Birch Lane, ShareASale, PartnerStack; CJ Affiliate pending approval

---

# CODE WRITTEN — what it is and where it lives

## A) Membership / portal toggle pages (this branch)

**Folder:** `membership-toggle/`  
**Decision with Daniel:** no passwords. Email-only unlock + MailerLite list growth.

### Engine
| File | Role |
|------|------|
| `tc-membership-toggle.css` | Styles (prefixed `tc-`, safe next to Kadence / overlay cards) |
| `tc-membership-toggle.js` | Toggle, join/unlock, localStorage session, MailerLite fire-and-forget |
| `demo.html` | Browser preview of email-unlock flow |
| `MAILERLITE-SETUP.md` | Click-by-click MailerLite wiring |
| `README.md` | Install order for WordPress |

### Page templates (Custom HTML blocks)
| Template | Purpose | Use it? |
|----------|---------|---------|
| **`page-0-email-unlock.html`** | Preview ⇄ Full content; email join unlocks deeper editorial; browser remembers | **YES — recommended** |
| `page-1-landing-toggle.html` | Landing with New here / Members toggle (password-style sign-in) | Legacy / ignore unless real logins needed |
| `page-2-landing-compare.html` | Side-by-side Visitors vs Members + toggle for CTA | Optional marketing layout |
| `page-3-nonmember-example.html` | Teaser + gate on a linked article | Optional if building gated article UX |
| `page-4-member-example.html` | Unlocked member article view | Optional companion to page 3 |

### How page-0 works (vital)
1. Left toggle = **Preview** (teaser + email form).
2. Right toggle = **Full content** (locked until join; then auto-unlocks).
3. On submit: optional MailerLite POST via `data-mailerlite-action`, then `localStorage` marks joined, toggle flips to full content.
4. Return visits on same browser skip the gate.
5. Install once site-wide: CSS in Additional CSS, JS in WPCode footer; paste HTML into a Custom HTML block per portal page.
6. Align accent colors to navy/gold before publish (demo CSS still uses a teal accent in places).

**Not done:** templates not yet pasted onto live staging pages as published portals.

Related live work (not all in this folder): homepage **`tcj-signup`** Custom HTML block already posts to MailerLite  
`https://assets.mailerlite.com/jsonp/2310667/forms/190738396377777459/subscribe`  
(Editorial Subscribers group). Sender verify for `contact@truth-collective.com` was a blocker for confirm emails.

---

## B) Duotone / B&W editorial imagery (`tc-bw-reveal`)

**This is the “duotone editorial pages” code.** It lives on branch  
`cursor/lock-in-master-brief-and-components-b1dd` as `docs/components/bw-reveal.md`  
(also copied into this repo as `docs/components/bw-reveal.md` on this branch when present).

**What it does:** image stays black-and-white at rest, fades to full color on hover (optional subtle `scale(1.02)`). For editorial hubs (The Truth Untold, The Ones Who Gave Everything) and any editorial image.

**How to apply:**
1. Append the CSS once to Additional CSS (scoped to `.tc-bw-reveal` only — safe).
2. On the image (or its wrapper), Advanced → Additional CSS Class(es) → `tc-bw-reveal`.
3. Purge caches; check in private window.

**Behavior notes:** touch / small screens show full color (no hover). Reduced-motion drops the animation. Does **not** change overlay/explore/book cards. Optional later: caption fade, gradient, slower cinematic fade, image link.

Core CSS (append-only):

```css
.tc-bw-reveal img {
  filter: grayscale(100%) contrast(1.02) !important;
  transition: filter 600ms ease, transform 600ms ease !important;
  will-change: filter, transform !important;
}
@media (hover: hover) {
  .tc-bw-reveal:hover img {
    filter: grayscale(0%) contrast(1) !important;
    transform: scale(1.02) !important;
  }
}
@media (hover: none), (max-width: 767px) {
  .tc-bw-reveal img { filter: grayscale(0%) !important; transform: none !important; }
}
@media (prefers-reduced-motion: reduce) {
  .tc-bw-reveal img { transition: none !important; transform: none !important; }
  .tc-bw-reveal:hover img { transform: none !important; }
}
```

---

## C) Image / hover components (critical — do not mix up)

| Goal | Classes | Notes |
|------|---------|-------|
| Hover crop cards (hubs/products) — title on image, EXPLORE | Section: `tc-overlay-card` · Image/hub: `tc-explore-hub` | Gutenberg `figure` preferred; ~460px crop box |
| Book covers + description reveal | Column: `tc-book-card` · body: `tc-leadership-body` · button: `tc-book-button` | **Never** overlay/explore on books |
| Full-bleed animated hero | Section: `tc-explore-hero` | 16:9; staggered entrance |
| Wide banner, no crop, hover darken + EXPLORE | Section: `tc-explore-banner` only | Remove overlay/hub; do not stack |
| Editorial B&W → color | `tc-bw-reveal` on image/wrapper | Duotone effect above |
| Full image + text below (no card) | No overlay / explore-hub | Normal image |

**Never** put card classes on footers or full editorial banners.  
**Never** globally override `.tc-overlay-card` / `.tc-explore-hub` with `overflow:visible` / `object-fit:contain` — breaks all real cards.  
**Never stack** `tc-explore-banner` with overlay/hub (`!important` crop wins).

Other image fixes from this work:
- Kadence **Use fixed ratio** OFF for natural banners.
- Gutenberg Wide/Full → edge overflow; use Kadence Image Adv for contained banners.
- Missing EXPLORE pill: often `kb-section-link-overlay` covering `::after` — link the image instead.
- Repo `image-fix/tc-image-fix.css` — **do not paste globally**.

Also on other branches: `css/tc-hero-reveal.css`, `wordpress/additional-css/tc-overlay-card.css`, `docs/components/book-spotlight.md` (`tc-book-spotlight` v1).

---

## D) Other vital work done across these conversations

1. **Footer:** fancy 4-column navy footer was Home-only; smash caused by `tc-overlay-card` on columns — classes removed. Self-contained **`tc-ft`** HTML footer drafted (navy/gold, MailerLite, social SVGs) for footer widgets. Watch for typo line `background:linear-gradient(180deg,#c9a css,#b8944b);` — delete; keep solid `#b8944b`. Site-wide install not finished.
2. **Typography / container:** container ~1200; Inter 18 / 1.6; Playfair headings scale H1–H6; letter-spacing 0; pattern padding recipe 60/60/24/24 desktop, 40/40/20/20 mobile.
3. **MailerLite:** homepage signup verified capturing; double opt-in / welcome / sender verify still need confirmation.
4. **Structure / hubs (other agent branch):** Master Brief locked; hub placements; reparent playbooks; AI hub canonical fixed; book-card wrong-class playbook on `/ai-in-healthcare/`; money-page punch lists; Truth Untold prep.
5. **Computer side quest:** D: drive letter shift; Google Drive “Lost and Found” junk `.js` conflict files; safe folder `C:\Users\dreid\Documents\TC-BACKUP`; do not download multi-GB backups to laptop.
6. **10Web prep:** backup OK; Manager on tcstaging; migrate to `.10web.site` first; no DNS yet; no mass AI regenerate.

---

# OPERATING RULES (for every new conversation)

These were written and tightened across sessions so assistants and Daniel’s protocols both hold. Follow them.

## Identity
- Owner: **Daniel Reid**. Assistant: **Big Dog Monty (BDM)**.
- Never guess. Reach high certainty against live staging. If you cannot, say so and stop. Do not invent facts, URLs, or data.

## Hard working rules
1. One problem at a time; exact clicks; screenshots welcome.
2. Fix the real cause. No workarounds unless they are the only way. No restarting from scratch for a narrow fix.
3. Do not offer a menu of choices on routine builds — direct the next step; keep justifications short unless Daniel asks why.
4. Deliver paste-ready CSS/HTML/JS + steps. Check snippets against existing Additional CSS / `tc-` classes so nothing collides. Append scoped blocks; do not casually rewrite locked components.
5. Prefer patterns / global styles / reusable HTML over 65–86 page one-offs.
6. Never recommend replatforming to Tailwind or rebuilding the site from scratch.
7. Never paste global CSS that overrides `.tc-overlay-card` / `.tc-explore-hub` site-wide.
8. Prefer email-only membership UX over passwords unless Daniel asks for real accounts.
9. Protect energy: cosmetic bugs ≠ launch blockers.
10. Vet other AIs (including 10Web marketing claims) against custom-code risk.
11. When context is full: finish the in-flight task, then new chat with this HANDOFF pasted.

## Permanent content rules (site copy)
- No em dashes. No contractions. No bold in body text (labels/headings only). No exclamation points. No clickbait. No hype. No fabricated facts. No medical or financial claims.
- Affiliate-only: never feature a product/brand without an active partnership.
- Voice: premium, calm authority, truth-first. Specific beats vague.

## Locked components (do not rewrite)
`tc-book-card`, `tc-overlay-card`, `tc-explore-hub`, `tc-explore-hero` (+ newer additives: `tc-explore-banner`, `tc-bw-reveal`, membership toggle namespace).  
Never apply `object-fit: contain` to overlay cards. Book content must use book-card classes, not overlay/explore.

## SEO / launch gates (every page)
Focus keyword in SEO title (under 60, include 2026 where that standard applies), meta under 160, H1, H2, first paragraph, hero alt. Internal links parent/children/siblings. Never change an indexed slug. Schema parent/child/sub-child in RankMath. Before launch: robots OK, sitemap 200, no `__trashed` URLs, redirects mapped.

## 10Web rules
1. Migrate **tcstaging** only.  
2. Hosting + Booster; verify custom JS after Booster.  
3. AI regenerate = dangerous on custom card pages — test one first.  
4. Domain pointing only after verify on `.10web.site`.  
5. Plugin/core updates after migration, one at a time.

---

## Global typography targets (Kadence Customize)

| Element | Desktop | Mobile | Line-height |
|---------|---------|--------|-------------|
| Body | 18px Inter 400 | 17px | 1.6 (unitless) |
| Headings master | Playfair 600 | — | — |
| H1 | 48 | 32 | 1.2 |
| H2 | 38 | 28 | 1.2 |
| H3 | 30 | 24 | 1.25 |
| H4 | 24 | 20 | 1.3 |
| H5 | 20 | 18 | 1.3 |
| H6 | 16 | 15 | 1.4 |

Never use fixed rem/px widths/heights for layout; use max-width / container 1200 and height auto.

---

## Site structure notes

- ~65+ content-heavy pages; strategy is pattern/template level.
- Two Hostinger folders: `public_html/staging` (older) and `public_html/tcstaging` (**good site**).
- Hostinger disk ~10.71 GB / 50 GB; Updraft used ~2.7 GB (trim later).
- Deeper hub/editorial inventory and playbooks: branch `cursor/lock-in-master-brief-and-components-b1dd` under `docs/`.

---

## What was NOT completed

- Footer site-wide (`tc-ft` / synced pattern / widgets)
- Toggle portal pages published on staging
- MailerLite sender verify + welcome automation fully confirmed
- Full pattern congruence / edge padding audit
- DNS / go-live cutover
- 10Web migrate verify + Booster smoke-test

---

## Related Cursor agents / branches

| Agent / theme | Branch | What it holds |
|---------------|--------|----------------|
| Member email signup toggle (this thread) | `cursor/image-fix-and-membership-toggle-2672` | `membership-toggle/`, `image-fix/`, this HANDOFF |
| Page image cropping / Master Brief | `cursor/lock-in-master-brief-and-components-b1dd` | `docs/MASTER-BRIEF.md`, hubs, playbooks, `tc-bw-reveal`, `.cursor/rules` |
| Hero hover reveal | `cursor/tc-hero-reveal-42be` | `css/tc-hero-reveal.css` |
| Overlay card CSS | (earlier) | `wordpress/additional-css/tc-overlay-card.css` |
