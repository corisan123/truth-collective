# Quarterly Review signup pattern (2026-08-11)

**Pattern ID:** `6747`  
**Correct title:** Quarterly Review Signup (Join the Quarterly Review)  
**Was misnamed:** Technical Benchmarking Selection Process Overvfew  
**Scaffold:** `diagnostics/scaffolds/pattern-6747-quarterly-review-signup.html`

## Status
This is the **locked gold** subscribe block Cursor built from the Vercel / 10Web sample direction. Keep the look. Do not replace with a generic MailerLite embed or Kadence form.

## Live inserts
Home, Recommended Books, AI Mastery Books, Ones Who Gave Everything (`ref:6747`).

## Behavior
- MailerLite JSONP action: `https://assets.mailerlite.com/jsonp/2310667/forms/190738396377777459/subscribe`
- Client-side email validate → POST FormData → success state
- Classes: `tcj-signup` / `tcj-*` (dedicated signup system; leave intact)

## Voice nits applied on re-save
- Removed em dashes in subcopy / error strings
- Success title: "You are on the list." (no contraction)
