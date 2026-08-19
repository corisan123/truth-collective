# ISI email forwarding — daniel@isiconsults.com → Yahoo

**Brand address:** `daniel@isiconsults.com`  
**Deliver to:** `dreid1253@yahoo.com`  
**Pattern:** same as Truth Collective `contact@truth-collective.com` → Yahoo (public brand address; Yahoo stays private).

Public site now uses `daniel@isiconsults.com` everywhere (mailto + contact copy).

---

## Where to set this (pick where the domain’s email/DNS lives)

### A) Hostinger (most likely if domain email is on Hostinger like TC)

1. Hostinger **hPanel** → **Email** → **Email Accounts** (or **Forwarders**)
2. Domain: `isiconsults.com`
3. Create mailbox **or** forwarder:
   - **Preferred for “Yahoo only”:** **Email Forwarders**
     - Forward from: `daniel@isiconsults.com`
     - Forward to: `dreid1253@yahoo.com`
   - **Or** create mailbox `daniel@isiconsults.com` and add forwarding to Yahoo in that mailbox settings
4. Save. Send a test from a non-Yahoo address to `daniel@isiconsults.com` and confirm it lands in Yahoo.
5. Optional: set Yahoo filter/label “ISI” so it stays separate from TC mail.

### B) Squarespace (domain currently pointed at Squarespace site)

Squarespace site hosting ≠ automatic email. If MX still points elsewhere, use that host. If you buy Squarespace Email / Google Workspace through Squarespace:

1. Squarespace → **Domains** → `isiconsults.com` → **Email** / **Google Workspace**
2. Add user or alias `daniel@isiconsults.com`
3. Set forwarding to `dreid1253@yahoo.com` (Workspace: user settings → Forwarding; or Groups/routing)

### C) DNS check (if mail never arrives)

In Hostinger DNS / domain registrar, MX records must point at whoever hosts email (Hostinger mail, Google, Microsoft, etc.). Website on Squarespace can stay; email MX can stay on Hostinger. That split is normal.

---

## What Cursor cannot do

Cursor cannot log into Hostinger/Squarespace and create the forwarder. Daniel (or Angie with a one-task prompt) creates it in the panel. Cursor already updated the public site address to `daniel@isiconsults.com`.

## Formspree / signup later

When Formspree is connected, set notification email to `daniel@isiconsults.com` (which then forwards to Yahoo) so the brand address stays public.
