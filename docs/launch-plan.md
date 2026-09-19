# Launch Plan and Working Method

The goal is to polish every page to the locked standard and launch. This file
defines how BDM and Daniel work together to get there efficiently.

## The core decision: do not hand-clean pages before handoff

Daniel should not spend his limited energy manually polishing old pages before
sending them over. That makes Daniel the bottleneck and forces guesswork about
what to change. The faster method is the reverse:

1. Daniel makes sure a page is published on staging. It does not need to look good.
2. BDM reads the live page and audits it against the Master Brief, the component
   reference, and the site structure.
3. BDM produces a per-page playbook in `docs/pages/` with an exact, ranked punch
   list, including the correct parent and sibling chain, so nothing is guessed.
4. Daniel applies the list, or the code executor applies it, then BDM verifies
   against staging.

The housekeeping Daniel noticed, such as aligning children to parents, canonical
errors, image sizing, and cheap layouts, is exactly what the audit detects and
specifies. He does not need to fix it first. He hands over a URL, not a clean page.

## Do the systemic work once, then pages

Fix shared things a single time so every page benefits:

- The `tc-` component library and image-uniformity rules (documented).
- The reusable newsletter block that carries an em dash (fix once, fixes all).
- Canonical hygiene and the schema templates (parent, child, sub-child).
- The Trusted Selection and FTC pattern (locked).

## Priority order (ranked by ROI and speed to monetization)

1. Systemic fixes above.
2. The three launch money pages from the Master Brief: Best Standing Desks,
   Best Office Chairs Under 500, Best Monitors for Productivity.
3. Hubs, then their children, one category at a time. Books first, since they are
   the most templated.
4. Non-monetized help pages, held to the same trust and technical standard.
5. SEMrush or equivalent audit. Fix only proven issues. Final sweep. Launch.

## Making cheap old pages look current (objective checklist)

"Polish" is a checklist, not a feeling. An old page is brought to standard when:

- Palette matches the locked hex values. Navy `#1e3a5f`, charcoal `#1f1f1f`,
  cream `#f8f4ec`, white `#ffffff`, gold `#b8944b` for signatures only.
- Fonts are Playfair Display for headings and Inter for body.
- Cards use the approved components (`tc-book-card`, `tc-overlay-card`,
  `tc-explore-hub`) rather than ad hoc layouts.
- One H1. Logical H2 and H3 order.
- Images render in locked boxes, no cut-off, unique alt text.
- Content rules pass. No em dashes, no contractions, no bold body text, no hype.
- Internal links up, down, and sideways. FTC pattern present. Schema set.

## Division of labor

BDM directs and produces exact code and instructions. Daniel or the code executor
applies them. BDM reviews every change against staging so nothing conflicts with
existing CSS. Any CSS destined for Additional CSS is checked against what is
already there before it is handed over.

## Continuity

The old problem of losing rules between sessions is solved by this repo. Every
session reads `docs/` first. Daniel does not need to find old chats. If context
is missing, BDM rebuilds it from staging plus these docs.
