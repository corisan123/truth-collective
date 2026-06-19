/* =====================================================================
   The Truth Collective — Membership Toggle Engine (vanilla JS, no deps)

   What it does
   ------------
   1. Powers the center toggle that switches between the Visitor view
      and the Member view. The chosen view is remembered per browser.
   2. Handles the Visitor email sign-up form (for your automation /
      newsletter). Posts to an endpoint if you give it one, otherwise
      runs in a safe demo mode.
   3. Handles the Member sign-in form. On success it unlocks the gated
      member content on the page, or redirects to a members-only page.
   4. Remembers a signed-in member so gated pages open without asking
      again, and provides a Sign-out button.

   IMPORTANT SECURITY NOTE
   -----------------------
   Real "members only" content must be protected on the SERVER. JavaScript
   alone cannot keep content private — anyone can read page source. Use
   this component for the UX (the toggle, the forms, the smooth unlock),
   and wire the endpoints below to a real backend (WordPress REST API, a
   membership plugin like MemberPress/Paid Memberships Pro, or your email
   platform). Without an endpoint the component runs in DEMO mode so you
   can preview the flow. Demo mode is clearly labeled and not secure.

   Configuration (two ways, data-attributes win over the global)
   -------------------------------------------------------------
   Global default (optional), put before this script:
     <script>
       window.TC_MEMBERSHIP_CONFIG = {
         signupEndpoint: "/wp-admin/admin-ajax.php?action=tc_signup",
         signinEndpoint: "/wp-json/tc/v1/login",
         memberRedirect: "",          // e.g. "/members/dashboard"
         sessionKey:     "tc_member_session"
       };
     </script>

   Per-component override via data-attributes on .tc-membership:
     data-default-view="visitor|member"
     data-signup-endpoint="..."
     data-signin-endpoint="..."
     data-member-redirect="..."
   ===================================================================== */
(function () {
  "use strict";

  var GLOBAL = window.TC_MEMBERSHIP_CONFIG || {};
  var SESSION_KEY = GLOBAL.sessionKey || "tc_member_session";
  var VIEW_KEY = "tc_membership_view";

  /* ---- tiny helpers ------------------------------------------------ */
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $all(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  function store(key, val) {
    try { window.localStorage.setItem(key, val); } catch (e) {}
  }
  function read(key) {
    try { return window.localStorage.getItem(key); } catch (e) { return null; }
  }
  function remove(key) {
    try { window.localStorage.removeItem(key); } catch (e) {}
  }
  function validEmail(v) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(v || "").trim());
  }
  function setMsg(el, text, type) {
    if (!el) return;
    el.textContent = text || "";
    el.className = "tc-msg" + (type ? " tc-msg--" + type : "");
  }

  /* ---- per-component config --------------------------------------- */
  function cfg(root) {
    return {
      defaultView: root.getAttribute("data-default-view") || "visitor",
      signupEndpoint: root.getAttribute("data-signup-endpoint") || GLOBAL.signupEndpoint || "",
      signinEndpoint: root.getAttribute("data-signin-endpoint") || GLOBAL.signinEndpoint || "",
      memberRedirect: root.getAttribute("data-member-redirect") || GLOBAL.memberRedirect || ""
    };
  }

  /* ---- view switching --------------------------------------------- */
  function setView(root, view) {
    view = view === "member" ? "member" : "visitor";
    root.setAttribute("data-view", view);
    store(VIEW_KEY, view);
    $all(".tc-toggle__btn", root).forEach(function (btn) {
      var on = btn.getAttribute("data-view") === view;
      btn.classList.toggle("is-active", on);
      btn.setAttribute("aria-selected", on ? "true" : "false");
    });
  }

  /* ---- member session --------------------------------------------- */
  function getSession() {
    var raw = read(SESSION_KEY);
    if (!raw) return null;
    try { return JSON.parse(raw); } catch (e) { return null; }
  }
  function setSession(data) { store(SESSION_KEY, JSON.stringify(data || {})); }
  function clearSession() { remove(SESSION_KEY); }

  function reflectSession(root) {
    var session = getSession();
    root.setAttribute("data-member", session ? "in" : "out");
    var who = $("[data-tc-member-email]", root);
    if (who && session && session.email) who.textContent = session.email;
  }

  /* ---- network ----------------------------------------------------- */
  function postJSON(url, payload) {
    return fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      credentials: "same-origin",
      body: JSON.stringify(payload)
    }).then(function (res) {
      return res.json().catch(function () { return {}; }).then(function (json) {
        return { ok: res.ok, status: res.status, data: json };
      });
    });
  }

  /* ---- sign-up (visitor) ------------------------------------------ */
  function wireSignup(root, conf) {
    var form = $("[data-tc-signup]", root);
    if (!form) return;
    var msg = $("[data-tc-signup-msg]", root) || $(".tc-msg", form);

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var emailInput = form.querySelector('input[type="email"], input[name="email"]');
      var email = emailInput ? emailInput.value.trim() : "";
      var name = (form.querySelector('input[name="name"]') || {}).value || "";

      if (!validEmail(email)) {
        setMsg(msg, "Please enter a valid email address.", "error");
        if (emailInput) emailInput.focus();
        return;
      }

      var btn = form.querySelector('button[type="submit"], .tc-btn');
      if (btn) btn.disabled = true;
      setMsg(msg, "Submitting…");

      var done = function (text) {
        setMsg(msg, text, "success");
        form.reset();
        if (btn) btn.disabled = false;
      };
      var fail = function (text) {
        setMsg(msg, text || "Something went wrong. Please try again.", "error");
        if (btn) btn.disabled = false;
      };

      if (!conf.signupEndpoint) {
        // DEMO MODE — no backend wired yet.
        store("tc_demo_signup", email);
        setTimeout(function () {
          done("Thanks! You're on the list. (Demo mode — connect signupEndpoint to send this to your automation.)");
        }, 500);
        return;
      }

      postJSON(conf.signupEndpoint, { email: email, name: name, source: "tc-membership-toggle" })
        .then(function (r) {
          if (r.ok && (r.data.success === undefined || r.data.success)) {
            done(r.data.message || "Thanks! Check your inbox to confirm your subscription.");
          } else {
            fail(r.data.message);
          }
        })
        .catch(function () { fail(); });
    });
  }

  /* ---- sign-in (member) ------------------------------------------- */
  function wireSignin(root, conf) {
    var form = $("[data-tc-signin]", root);
    if (form) {
      var msg = $("[data-tc-signin-msg]", root) || $(".tc-msg", form);

      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var email = (form.querySelector('input[type="email"], input[name="email"]') || {}).value || "";
        var pass = (form.querySelector('input[type="password"], input[name="password"]') || {}).value || "";
        email = email.trim();

        if (!validEmail(email)) { setMsg(msg, "Enter the email you signed up with.", "error"); return; }
        if (!pass) { setMsg(msg, "Enter your password.", "error"); return; }

        var btn = form.querySelector('button[type="submit"], .tc-btn');
        if (btn) btn.disabled = true;
        setMsg(msg, "Signing in…");

        var succeed = function (session) {
          setSession(session);
          reflectSession(root);
          setMsg(msg, "Welcome back!", "success");
          if (btn) btn.disabled = false;
          if (conf.memberRedirect) {
            window.location.href = conf.memberRedirect;
          }
        };
        var deny = function (text) {
          setMsg(msg, text || "We couldn't verify those details.", "error");
          if (btn) btn.disabled = false;
        };

        if (!conf.signinEndpoint) {
          // DEMO MODE — accepts any email + password so you can preview
          // the unlocked member experience. NOT secure. Wire signinEndpoint.
          setTimeout(function () {
            succeed({ email: email, demo: true, at: Date.now() });
            setMsg(msg, "Signed in (Demo mode — content is not actually protected).", "success");
          }, 500);
          return;
        }

        postJSON(conf.signinEndpoint, { email: email, password: pass })
          .then(function (r) {
            if (r.ok && r.data && r.data.success) {
              succeed({ email: email, token: r.data.token || null, at: Date.now() });
            } else {
              deny(r.data && r.data.message);
            }
          })
          .catch(function () { deny("Network error. Please try again."); });
      });
    }

    // Sign-out
    $all("[data-tc-signout]", root).forEach(function (b) {
      b.addEventListener("click", function (e) {
        e.preventDefault();
        clearSession();
        reflectSession(root);
        setView(root, "visitor");
      });
    });
  }

  /* ---- init one component ----------------------------------------- */
  function init(root) {
    if (root.__tcReady) return;
    root.__tcReady = true;
    var conf = cfg(root);

    // toggle buttons
    $all(".tc-toggle__btn", root).forEach(function (btn) {
      btn.addEventListener("click", function () {
        setView(root, btn.getAttribute("data-view"));
      });
    });

    // restore last view (or use default); if already a member, prefer member view
    var saved = read(VIEW_KEY);
    var startView = saved || conf.defaultView;
    if (getSession() && !saved) startView = "member";
    setView(root, startView);

    reflectSession(root);
    wireSignup(root, conf);
    wireSignin(root, conf);
  }

  function boot() { $all("[data-tc-membership]").forEach(init); }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  // Expose a tiny API for advanced use / re-init after AJAX page loads.
  window.TCMembership = { init: init, boot: boot, signOut: function () { clearSession(); boot(); } };
})();
