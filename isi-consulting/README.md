# ISI Consulting site

Multi-page static site for [isiconsults.com](https://www.isiconsults.com).

## Pages
- `index.html` — Home
- `about.html` — About
- `services.html` — Services
- `process.html` — Process
- `contact.html` — Contact (`daniel@isiconsults.com`)
- `whitepaper.html` — Capabilities whitepaper scaffold (Claude fills prose)

## Live forms
Signup and comments/contact forms are wired to Formspree placeholders:
`action="https://formspree.io/f/REPLACE_WITH_FORM_ID"`

1. Create a free Formspree form (or MailerLite embed).
2. Replace `REPLACE_WITH_FORM_ID` on all forms (or set one ID for contact/signup/comments).
3. Until then, use `daniel@isiconsults.com`.

## Capabilities PDF
Drop the real PDF at `assets/ISI-Capabilities-Overview.pdf` and point the Home secondary CTA back to it.

## Deploy
Upload this folder to Hostinger/Vercel and point `isiconsults.com` DNS off Squarespace when ready.
