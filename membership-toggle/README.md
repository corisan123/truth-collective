# Membership Toggle (Visitors ⇄ Members)

A lightweight, dependency-free component for The Truth Collective.

## ⭐ Recommended setup: email-only "join to unlock" (no passwords)
For growing followers/subscribers, **don't use passwords.** Use the
email-only flow: a visitor types their email → it's stored in MailerLite →
the deeper content unlocks instantly and their browser remembers them.

- Template: **`page-templates/page-0-email-unlock.html`**
- Setup guide (plain English, click-by-click): **`MAILERLITE-SETUP.md`**
- Preview now: open **`demo.html`** in a browser.

The password-based pieces below still exist if you ever need real logins,
but you can ignore them for the email hook.

---

A center **toggle switch** drives everything:

- left = new visitors, right = members/full content.
- **Visitors** see an **email** form (feeds MailerLite / your automation).
- **Members/Full content** unlocks after they join (email) or sign in.
- The chosen view and the joined/signed-in state are remembered in the
  browser.

## Files
| File | What it is |
|------|------------|
| `tc-membership-toggle.css` | All styles (prefixed `tc-`, won't clash with Kadence) |
| `tc-membership-toggle.js`  | The engine (vanilla JS) |
| `demo.html`                | Open in a browser to preview the whole flow |
| `MAILERLITE-SETUP.md`      | ⭐ Plain-English guide to wire up MailerLite (no passwords) |
| `page-templates/page-0-email-unlock.html` | ⭐ Recommended: email-only join-to-unlock |
| `page-templates/page-1-landing-toggle.html` | Landing page with the toggle (password style) |
| `page-templates/page-2-landing-compare.html` | Visitors vs Members side-by-side + toggle |
| `page-templates/page-3-nonmember-example.html` | What a **non-member** sees on a linked article (teaser + gate) |
| `page-templates/page-4-member-example.html` | What a **member** sees after validating (full gated article) |

## Quick preview
Open `demo.html` in any browser. It runs in **DEMO MODE**: sign-up just
confirms, and sign-in accepts any email + password so you can see the
unlocked member view. Nothing leaves your machine.

---

## Install on WordPress (Kadence)

### 1) Load the CSS + JS once, site-wide
Easiest: a free **code snippets** plugin (e.g. "WPCode") or your child
theme. Upload the two files (e.g. to your child theme `/assets/`) and
enqueue them, **or** paste them inline:

- Paste `tc-membership-toggle.css` into **Appearance → Customize →
  Additional CSS**.
- Add `tc-membership-toggle.js` via WPCode as a **JS snippet** set to load
  in the **site footer** (so it runs after the page HTML).

> You only need to load these **once** for the whole site, not per page.

### 2) Add a page
1. Create a new WordPress page.
2. Add a **Custom HTML** block (Kadence supports this).
3. Paste the contents of one of the `page-templates/*.html` files.
4. Publish.

Build your 4 pages by using:
- Page 1 → `page-1-landing-toggle.html`
- Page 2 → `page-2-landing-compare.html`
- Page 3 → `page-3-nonmember-example.html`
- Page 4 → `page-4-member-example.html`

---

## Connecting it to real services (so it actually works)

Each component reads optional settings from data-attributes on the
`.tc-membership` element (or from a global `window.TC_MEMBERSHIP_CONFIG`).
Leave them blank to stay in demo mode.

```html
<div class="tc-membership" data-tc-membership
     data-default-view="visitor"
     data-signup-endpoint="https://your-site/wp-json/tc/v1/signup"
     data-signin-endpoint="https://your-site/wp-json/tc/v1/login"
     data-member-redirect="/members/dashboard">
```

### Sign-up (email automation)
Set `data-signup-endpoint` to a URL that accepts a JSON `POST`:

```json
{ "email": "you@example.com", "name": "Jane", "source": "tc-membership-toggle" }
```

It should reply with JSON like `{ "success": true, "message": "..." }`.
You can point this at:
- A WordPress REST route that forwards to Mailchimp/MailerLite/etc., or
- Your email platform's hosted form endpoint, or
- `admin-ajax.php?action=tc_signup` with a small PHP handler.

### Sign-in (members)
Set `data-signin-endpoint` to a URL that accepts:

```json
{ "email": "you@example.com", "password": "••••••" }
```

and replies `{ "success": true, "token": "optional" }` on success or
`{ "success": false, "message": "Invalid login" }` on failure.

On success the component unlocks `.tc-unlocked` content and, if
`data-member-redirect` is set, sends the member to that page.

> ⚠️ **Security:** JavaScript can hide content, but it cannot truly protect
> it — the HTML is downloadable. For genuinely private articles, gate the
> **content on the server**. The clean way on WordPress is a membership
> plugin (MemberPress, Paid Memberships Pro, Restrict Content Pro). Use
> this component for the polished UX and point its endpoints at that
> plugin / the WP REST API. In demo mode (no endpoints) the member content
> is **not** protected — it's only for previewing the experience.

## Customizing
- **Colors:** edit the CSS variables at the top of
  `tc-membership-toggle.css` (`--tc-accent`, etc.).
- **Labels & copy:** edit the text inside each `page-templates` file.
- **Member content:** put whatever you want inside the `.tc-unlocked`
  block — it only appears after a successful sign-in.
