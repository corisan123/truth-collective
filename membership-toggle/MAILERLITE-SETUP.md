# Connecting the toggle to MailerLite (plain-English guide)

You do **not** need passwords, a login server, or any coding skills for
this. The goal is simple:

> Someone types their **email** → MailerLite stores it (and starts sending
> your blogs/posts) → the **deeper content unlocks** for them.

There are two ways to do it. **Method B is the most reliable** and is what
I recommend. Method A looks the most seamless. Pick one.

---

## First: what "no password" means
Forget passwords entirely. A password would mean real user accounts —
that's a lot of work and it scares people off. For "join to see more,"
**email-only** is the standard and it converts far better. MailerLite is
the thing that "remembers" people (it stores every email and runs your
automations). The toggle just remembers *this browser* so the content
stays unlocked when they come back.

---

## Method A — Seamless (our form sends straight to MailerLite)

Use this if you want the join box to look exactly like the rest of the
page (our styled form), with the content unlocking instantly.

1. **Log in to MailerLite** → left menu **Forms** → **Embedded forms** →
   **Create embedded form**. Give it a name (e.g. "TC unlock"), pick the
   group/audience these subscribers should join, and save.
2. MailerLite shows you some HTML code. Find the part that says
   `action="https://assets.mailerlite.com/jsonp/..."` (or
   `action="https://app.mailerlite.com/webforms/submit/..."`).
   **Copy that whole URL inside the quotes.**
3. Open your page template (e.g. `page-templates/page-0-email-unlock.html`)
   and paste that URL between the quotes here:

   ```html
   <div class="tc-membership" data-tc-membership data-mode="email-unlock"
        data-mailerlite-action="PASTE-THE-URL-HERE">
   ```

4. Save the page. Done. When someone joins, their email goes to MailerLite
   and the full content opens.

> Note: browser security means our script sends the email "fire and
> forget" — it almost always works, but it can't show MailerLite's own
> error messages. If you want 100% guaranteed capture with MailerLite's
> own validation, use **Method B**.

---

## Method B — Most reliable (MailerLite's own form/pop-up + redirect)

Use this if you want MailerLite's guaranteed capture and (optionally) a
pop-up that appears on its own. This is the one I recommend.

### Step 1 — Make the form/pop-up in MailerLite
- **Forms → Pop-ups → Create** (or **Embedded form**, your choice).
- Add just an **Email** field (and Name if you like). Choose the group.
- For a pop-up, under **Display / Behavior** you can set it to appear
  automatically (on page load, after a few seconds, on scroll, or on exit).
  That's the "pop-up that opens by itself" you asked about — it's a toggle
  in MailerLite, no code.

### Step 2 — Tell MailerLite where to send people after they join
- In the form's **success / "after submit"** settings, choose
  **Redirect to a URL** and enter your full-content page, e.g.
  `https://tcstaging.truth-collective.com/full-editorial`.
- (If you prefer no redirect, you can instead show a "Thanks!" message and
  put the unlock script from Step 4 on the *same* page.)

### Step 3 — Put MailerLite's snippet on your site
- MailerLite gives you a small `<script>` snippet for the form/pop-up.
- Paste it once site-wide (same place you put the toggle's JS — e.g. a
  WPCode footer snippet), or on the specific page, per MailerLite's
  instructions.

### Step 4 — Remember the visitor so content stays unlocked
On the **full-content page** (the one MailerLite redirects to after they
join), add a **Custom HTML block** with this one line:

```html
<script>window.TCMembership && TCMembership.markJoined();</script>
```

That tells the toggle "this person joined," so the deeper content shows
unlocked now and on future visits from this browser.

That's it. Flow: visitor sees pop-up → enters email → MailerLite stores it
and starts your automation → MailerLite redirects to the full page →
content is unlocked.

---

## Which template goes where

| Your page | Use this template | Mode |
|-----------|-------------------|------|
| The hook page (teaser + join, recommended) | `page-templates/page-0-email-unlock.html` | email-only |
| Full-content page MailerLite redirects to | any page; add the Step-4 snippet | — |

You can ignore the older password-based templates
(`page-1`…`page-4`) — they're there only if you ever want real logins.
For your goal (grow followers/subscribers), use the **email-only**
`page-0-email-unlock.html`.

---

## Testing it
1. Open `demo.html` in a browser first — type any email, watch it unlock.
2. After wiring MailerLite, submit your own email on the live page and
   confirm it shows up in **MailerLite → Subscribers**.
3. Reload the page — you should land straight on the unlocked content
   (the browser remembered you). To test as a brand-new visitor, open a
   private/incognito window.

## Common questions
- **"Where are passwords stored?"** Nowhere — there are none. MailerLite
  stores the emails.
- **"Can someone skip the form and see the content?"** A tech-savvy person
  could, because it's browser-side. That's fine here — the content isn't
  secret, it's a hook to get the email. If you ever need truly locked
  content, that's when a membership plugin/login is worth it.
- **"Can the pop-up open by itself?"** Yes — set that in MailerLite's
  pop-up display settings (Method B, Step 1).
