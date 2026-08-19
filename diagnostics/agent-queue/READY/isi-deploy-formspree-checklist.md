---
lane: isi
id: isi-deploy-formspree-checklist
priority: 1
---

# Ticket — ISI Block B

## Agent
Use starter `diagnostics/fleet/STARTERS/03-isi-block-b.md`.

## Do
1. Work only in `isi-consulting/` + diagnostics for ISI.
2. Map every `REPLACE_WITH_FORM_ID` / Formspree placeholder → `diagnostics/outputs/isi/formspree-map.md`.
3. Write `diagnostics/outputs/isi/deploy-checklist.md` (DNS from Squarespace, SSL, forms, email forward dependency).
4. Fix broken internal links in static pages if found.
5. Do **not** touch TC staging REST.
6. Commit, push, move ticket to DONE/.
