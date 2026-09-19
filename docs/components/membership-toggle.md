# Component — Membership and Email Unlock Toggle

A self-contained Preview vs Full content toggle with an email gate and optional
MailerLite capture. Built for editorial and blog pages. Preserved here because
the original chat was lost.

## Safety

- Namespace is `tc-membership`, `tc-toggle`, `tc-panel`, `tc-card`, `tc-title`,
  `tc-lead`, `tc-btn`, `tc-list`, `tc-form`, `tc-field`, `tc-msg`. None of these
  collide with the site classes `tc-book-card`, `tc-leadership-body`,
  `tc-book-button`, `tc-overlay-card`, `tc-explore-hub`, or the product grade
  classes. Safe to add as-is.

## DO NOT USE the old image fix

An earlier version of this doc included an image fix that set
`object-fit: contain !important` and `aspect-ratio: auto !important` on
`.tc-overlay-card` and `.tc-explore-hub`. Do not paste it. It breaks the
hover-reveal overlay and the EXPLORE pill behavior. The overlay components are
already correct in `docs/components/README.md`.

## Install order

1. CSS into Additional CSS.
2. JavaScript via the WPCode plugin, Auto Insert, Site Wide Footer, set Active.
3. HTML into a Custom HTML block on the page.

## Piece 1 — CSS (toggle only)

```css
.tc-membership {
  --tc-accent: #0f7b6c; --tc-accent-2: #14b8a6; --tc-ink: #1f2933;
  --tc-muted: #6b7280; --tc-bg: #ffffff; --tc-bg-soft: #f3f6f8;
  --tc-border: #e2e8f0; --tc-radius: 16px;
  --tc-shadow: 0 18px 40px -18px rgba(15,23,42,.35); --tc-maxw: 1100px;
  box-sizing: border-box; width: 100%; max-width: var(--tc-maxw);
  margin-inline: auto; color: var(--tc-ink); font-family: inherit;
}
.tc-membership *, .tc-membership *::before, .tc-membership *::after { box-sizing: border-box; }
.tc-toggle { position: relative; display: grid; grid-template-columns: 1fr 1fr; align-items: center; width: min(420px,92%); margin: 0 auto 2rem; padding: 6px; background: var(--tc-bg-soft); border: 1px solid var(--tc-border); border-radius: 999px; isolation: isolate; }
.tc-toggle__btn { position: relative; z-index: 2; appearance: none; border: 0; background: transparent; cursor: pointer; padding: .7rem 1rem; font: inherit; font-weight: 600; color: var(--tc-muted); border-radius: 999px; transition: color .25s ease; white-space: nowrap; }
.tc-toggle__btn.is-active { color: #fff; }
.tc-toggle__thumb { position: absolute; z-index: 1; top: 6px; bottom: 6px; left: 6px; width: calc(50% - 6px); border-radius: 999px; background: linear-gradient(135deg, var(--tc-accent), var(--tc-accent-2)); box-shadow: 0 6px 14px -6px var(--tc-accent); transition: transform .28s cubic-bezier(.4,0,.2,1); }
.tc-membership[data-view="member"] .tc-toggle__thumb { transform: translateX(100%); }
.tc-panel { display: none; animation: tc-fade .35s ease both; }
.tc-membership[data-view="visitor"] .tc-panel--visitor { display: block; }
.tc-membership[data-view="member"]  .tc-panel--member  { display: block; }
@keyframes tc-fade { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
.tc-card { background: var(--tc-bg); border: 1px solid var(--tc-border); border-radius: var(--tc-radius); box-shadow: var(--tc-shadow); padding: clamp(1.5rem,4vw,2.75rem); }
.tc-eyebrow { display: inline-block; font-size: .8rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; color: var(--tc-accent); margin: 0 0 .5rem; }
.tc-title { font-size: clamp(1.5rem,3.5vw,2.25rem); line-height: 1.15; margin: 0 0 .6rem; }
.tc-lead { color: var(--tc-muted); font-size: 1.05rem; line-height: 1.6; margin: 0 0 1.5rem; }
.tc-form { display: grid; gap: .9rem; max-width: 460px; }
.tc-field { display: grid; gap: .35rem; }
.tc-field label { font-weight: 600; font-size: .9rem; }
.tc-field input { width: 100%; padding: .85rem 1rem; font: inherit; color: var(--tc-ink); background: var(--tc-bg); border: 1px solid var(--tc-border); border-radius: 10px; transition: border-color .2s, box-shadow .2s; }
.tc-field input:focus { outline: 0; border-color: var(--tc-accent); box-shadow: 0 0 0 3px color-mix(in srgb, var(--tc-accent) 22%, transparent); }
.tc-btn { appearance: none; cursor: pointer; border: 0; border-radius: 10px; padding: .9rem 1.4rem; font: inherit; font-weight: 700; color: #fff; background: linear-gradient(135deg, var(--tc-accent), var(--tc-accent-2)); transition: transform .15s ease, box-shadow .15s ease, opacity .2s; box-shadow: 0 10px 24px -12px var(--tc-accent); }
.tc-btn:hover { transform: translateY(-1px); }
.tc-btn:active { transform: translateY(0); }
.tc-btn[disabled] { opacity: .6; cursor: progress; transform: none; }
.tc-btn--ghost { background: transparent; color: var(--tc-accent); border: 1px solid var(--tc-border); box-shadow: none; }
.tc-fineprint { font-size: .82rem; color: var(--tc-muted); margin: .25rem 0 0; }
.tc-msg { font-size: .92rem; margin: .25rem 0 0; min-height: 1.2em; }
.tc-msg--error { color: #b42318; }
.tc-msg--success { color: var(--tc-accent); }
.tc-locked { display: block; }
.tc-unlocked { display: none; }
.tc-membership[data-member="in"] .tc-locked { display: none; }
.tc-membership[data-member="in"] .tc-unlocked { display: block; animation: tc-fade .35s ease both; }
.tc-member-bar { display: flex; flex-wrap: wrap; gap: .75rem; align-items: center; justify-content: space-between; padding: .85rem 1.1rem; margin-bottom: 1.25rem; background: color-mix(in srgb, var(--tc-accent) 8%, white); border: 1px solid color-mix(in srgb, var(--tc-accent) 25%, white); border-radius: 12px; font-size: .95rem; }
.tc-member-bar strong { color: var(--tc-accent); }
.tc-list { list-style: none; margin: 0 0 1.25rem; padding: 0; display: grid; gap: .6rem; }
.tc-list li { position: relative; padding-left: 1.75rem; line-height: 1.5; }
.tc-list li::before { content: "\2713"; position: absolute; left: 0; top: 0; font-weight: 800; color: var(--tc-accent); }
@media (prefers-reduced-motion: reduce) { .tc-panel, .tc-unlocked { animation: none; } .tc-toggle__thumb, .tc-btn { transition: none; } }
```

Note: the brand palette for this component still uses a teal accent. If this is
used on a Truth Collective page, align the accent to the locked palette (navy
`#1e3a5f`, gold `#b8944b`) before publish.

## Piece 2 and Piece 3

The JavaScript (WPCode footer snippet) and the Custom HTML block are preserved in
the source file at `uploads/toggle_page_html_from_cursor_ce29.txt` lines 131 to
279. Copy them from there when building the page. The JS is namespaced under
`TCMembership` and only activates on elements marked `data-tc-membership`.
