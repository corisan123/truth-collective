# truth-collective

Website files and operating documentation for The Truth Collective (truth-collective.com).

Owner: Daniel Reid. Daniel calls the assistant Big Dog Monty, or BDM. Greet him as BDM.

## READ FIRST. DO NOT GUESS.

Any agent or contributor working on this site must read the documents in `docs/`
before making any change or giving any recommendation. These documents are the
locked source of truth. If a request conflicts with them, the documents win. If
you cannot reach certainty, say so. Do not guess, and do not build a workaround
in place of fixing the real cause.

- `docs/MASTER-BRIEF.md` — the governing rules, voice, SEO, compliance, and operating mode. Read every session.
- `docs/brand-overview.md` — brand positioning, audience, and content focus.
- `docs/engineering-evaluation-standards.md` — the product grading and tiering methodology.
- `docs/components/README.md` — verified `tc-` component structures and the CSS that fires them (captured from staging).
- `docs/launch-plan.md` — the working method and priority order to launch.
- `docs/launch-checklist.md` — launch blockers and the top-tier gap list.
- `docs/site-structure.md` — the real page hierarchy and canonical URLs.
- `docs/patterns/ftc-trusted-selection.md` — the locked trust and FTC pattern.
- `docs/pages/` — per-page improvement playbooks.

A Cursor project rule at `.cursor/rules/truth-collective.mdc` makes every session
read the above and follow the locked rules automatically.

## Environments

- Live: https://truth-collective.com
- Staging: https://tcstaging.truth-collective.com (all edits and fixes happen here first)

## Working rules for code

- Every CSS or HTML snippet must be checked against the CSS already present in
  staging Additional CSS. Never introduce rules that conflict with existing
  `tc-` classes.
- Verify class names, block structure, and selectors against the live staging
  markup before proposing changes.
