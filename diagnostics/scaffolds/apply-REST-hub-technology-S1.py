#!/usr/bin/env python3
"""REST-hub-technology-S1: Technology Hub parent structure pass.

Assembly order (locked): hero, intro, stats, Who This Is For, Why This Matters,
Best Uses, listings, governance pattern, evaluation above Final Word, Final Word,
Explore Other Hubs, social last.

No Additional CSS write. No grayscale. Staging only.
"""
from __future__ import annotations

import base64
import json
import os
import re
import ssl
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

PAGE_ID = 111
BASE = os.environ.get("STAGING", "https://tcstaging.truth-collective.com").rstrip("/")
ROOT = Path(__file__).resolve().parents[2]
BACKUP_DIR = ROOT / "diagnostics" / "backups"
CSS_PATH = Path(__file__).with_name("REST-hub-technology-S1.css")
TICKET = "REST-hub-technology-S1"
TODAY = date.today().isoformat()
MARKER = "TC STAGING PATCH TECH-HUB-S1"

CHILD_URLS = [
    f"{BASE}/technology-hub/computers-digital-devices/",
    f"{BASE}/technology-hub/monitor-display/",
    f"{BASE}/technology-hub/audio-and-video/",
    f"{BASE}/technology-hub/headphones-for-work/",
    f"{BASE}/technology-hub/speakers-home-office-outdoors/",
    f"{BASE}/technology-hub/projectors-and-microphones/",
    f"{BASE}/technology-hub/best-digital-smart-tablets/",
    f"{BASE}/technology-hub/interactive-digital-displays-2/",
]


def die(msg: str, code: int = 1) -> None:
    raise SystemExit(f"ERROR: {msg}")


def client():
    user = os.environ.get("TC_WP_USER", "").strip()
    pw = os.environ.get("TC_WP_APP_PASSWORD", "").strip()
    if not user or not pw:
        die("Set TC_WP_USER and TC_WP_APP_PASSWORD.")
    ctx = ssl.create_default_context()
    auth = base64.b64encode(f"{user}:{pw}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "User-Agent": f"TC-{TICKET}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    return ctx, headers


def api(method: str, path: str, headers: dict, ctx, body: dict | None = None):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(BASE + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=120) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:800]
        die(f"HTTP {e.code} {method} {path}: {detail}")


def public_status(url: str) -> int:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": f"TC-{TICKET}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def one(pat: str, html: str, flags=0) -> str:
    m = re.search(pat, html, flags)
    if not m:
        die(f"Could not extract: {pat[:80]}")
    return m.group(1) if m.lastindex else m.group(0)


def build(live: str) -> str:
    css = CSS_PATH.read_text()
    hero = one(
        r'(<!-- wp:group \{"align":"full","className":"tc-tech-cover".*?<!-- /wp:group -->\s*<!-- /wp:group -->)',
        live,
        re.S,
    )
    hero = hero.replace('alt="" class="wp-image-8311"', 'alt="Technology Hub" class="wp-image-8311"')

    leads = re.findall(
        r'<p class="tc-hub-hero-lead">(.*?)</p>',
        live,
        re.S,
    )
    if len(leads) < 4:
        die(f"Expected 4 intro leads, found {len(leads)}")
    leads[0] = leads[0].replace(
        "the largest of the six product hubs at Truth Collective",
    )

    cat = one(
        r'(<!-- wp:group \{"className":"tc-tech-cat-section".*?<!-- /wp:columns -->\s*<!-- /wp:group -->)',
        live,
        re.S,
    )
    cat = cat.replace(
        "Eight paths. Each one reviewed against the Truth Collective Trusted Selection Standards before it earns a place here.",
        "Eight category pages, each reviewed against the Truth Collective Trusted Selection Standards. Emerging Technologies and AI Wearables remain on this grid until those child pages exist.",
    )
    cat = cat.replace('alt="" class="wp-image-8318"', 'alt="Monitors and Displays" class="wp-image-8318"')
    cat = cat.replace('alt="" class="wp-image-8316"', 'alt="Headphones and Headsets" class="wp-image-8316"')
    cat = cat.replace('alt="" class="wp-image-8319"', 'alt="Emerging Technologies" class="wp-image-8319"')
    cat = cat.replace('alt="" class="wp-image-8320"', 'alt="AI Wearables" class="wp-image-8320"')

    eval_ps = re.findall(
        r'(<p style="font-family:\'Inter\',sans-serif;font-size:15px;color:#374151;line-height:1\.8;margin-bottom:\d+px;">.*?</p>)',
        live,
        re.S,
    )
    if len(eval_ps) < 3:
        die(f"Expected 3 evaluation paragraphs, found {len(eval_ps)}")
    eval_body = []
    for p in eval_ps[:3]:
        inner = re.sub(r"^<p[^>]*>", "", p)
        inner = re.sub(r"</p>$", "", inner)
        eval_body.append(f"<p>{inner}</p>")

    final_p = one(
        r'<p class="has-ast-global-color-4-color has-text-color has-link-color">The Technology Hub holds eight trusted paths,.*?</p>',
        live,
        re.S,
    )
    final_inner = re.sub(r"^<p[^>]*>", "", final_p)
    final_inner = re.sub(r"</p>$", "", final_inner)

    def shell(eyebrow: str, heading: str, class_name: str) -> str:
        return f"""<!-- wp:group {{"className":"tc-hub-prose-section {class_name}","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group tc-hub-prose-section {class_name}"><!-- wp:paragraph {{"className":"tc-section-eyebrow"}} -->
<p class="tc-section-eyebrow">{eyebrow}</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">{heading}</h2>
<!-- /wp:heading --></div>
<!-- /wp:group -->"""

    intro = f"""<!-- wp:group {{"className":"tc-tech-intro-prose","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group tc-tech-intro-prose"><!-- wp:columns {{"className":"tc-tech-intro-split"}} -->
<div class="wp-block-columns tc-tech-intro-split"><!-- wp:column {{"width":"38%"}} -->
<div class="wp-block-column" style="flex-basis:38%"><!-- wp:paragraph {{"className":"tc-hub-eyebrow"}} -->
<p class="tc-hub-eyebrow">Welcome to the</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"className":"tc-hub-hero-title"}} -->
<h2 class="wp-block-heading tc-hub-hero-title">Technology <em>Hub</em></h2>
<!-- /wp:heading --></div>
<!-- /wp:column -->

<!-- wp:column {{"width":"62%"}} -->
<div class="wp-block-column" style="flex-basis:62%"><!-- wp:paragraph {{"className":"tc-hub-hero-lead"}} -->
<p class="tc-hub-hero-lead">{leads[0]}</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"className":"tc-hub-hero-lead"}} -->
<p class="tc-hub-hero-lead">{leads[1]}</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"className":"tc-hub-hero-lead"}} -->
<p class="tc-hub-hero-lead">{leads[2]}</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"className":"tc-hub-hero-lead"}} -->
<p class="tc-hub-hero-lead">{leads[3]}</p>
<!-- /wp:paragraph -->

<!-- wp:group {{"className":"tc-tech-meta-row","layout":{{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}}}} -->
<div class="wp-block-group tc-tech-meta-row"><!-- wp:paragraph -->
<p>By Truth Collective Editorial · Updated 2026</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="{BASE}/product-selection-standards/">Reviewed against our Trusted Selection Standards</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->"""

    stats = """<!-- wp:html -->
<div class="tc-tech-stats" aria-label="Technology Hub highlights">
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Reviewed and Graded</p>
    <p class="tc-tech-stats__value">Trusted Selection Standards</p>
  </div>
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Product Hubs</p>
    <p class="tc-tech-stats__value">Six in the collection</p>
  </div>
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Category Pages</p>
    <p class="tc-tech-stats__value">Eight published children</p>
  </div>
</div>
<!-- /wp:html -->"""

    eval_html = f"""<!-- wp:html -->
<!-- TC EVALUATION STANDARDS - TECHNOLOGY HUB -->
<section class="tc-eval-brief" id="tc-eval-brief">
  <div class="tc-eval-brief__inner">
    <p class="tc-section-eyebrow">How We Evaluate Technology</p>
    <h3>Nothing Here Got In Because It Was Popular.</h3>
    {eval_body[0]}
    {eval_body[1]}
    {eval_body[2]}
    <a class="tc-eval-brief__link" href="{BASE}/6751-2/" rel="noopener">View Full Evaluation Standards</a>
  </div>
</section>
<!-- /wp:html -->"""

    final = f"""<!-- wp:group {{"className":"tc-final-word","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group tc-final-word"><!-- wp:paragraph {{"className":"tc-section-eyebrow"}} -->
<p class="tc-section-eyebrow">Closing</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Final Word</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{final_inner}</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->"""

    parts = [
        "<!-- wp:html -->",
        f"<!-- {MARKER}: CSS only. Images remain native for Media Replace. {TODAY}. -->",
        f'<style id="tc-tech-hub-s1">\n{css.strip()}\n</style>',
        "<!-- /wp:html -->",
        "",
        hero,
        "",
        intro,
        "",
        stats,
        "",
        shell("Audience", "Who This Is For", "tc-who"),
        "",
        shell("Purpose", "Why This Matters", "tc-why"),
        "",
        shell("When to use this hub", "Best Uses", "tc-best-uses"),
        "",
        cat,
        "",
        '<!-- wp:block {"ref":2847} /-->',
        "",
        eval_html,
        "",
        final,
        "",
        '<!-- wp:block {"ref":2870} /-->',
        "",
        '<!-- wp:block {"ref":7532} /-->',
        "",
    ]
    return "\n".join(parts)


def main() -> None:
    ctx, headers = client()
    status, page = api(
        "GET",
        f"/wp-json/wp/v2/pages/{PAGE_ID}?context=edit",
        headers,
        ctx,
    )
    live = page["content"]["raw"]
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup = BACKUP_DIR / f"page-{PAGE_ID}-before-{TICKET}-{TODAY}.html"
    backup.write_text(live)
    print(f"backup {backup} chars={len(live)}")

    new = build(live)
    if MARKER not in new:
        die("Marker missing from built HTML.")
    if "tc-explore-hub" not in new or "tc-eval-brief" not in new:
        die("Required classes missing from built HTML.")
    if new.count("tc-explore-hub") < 10:
        die("Explore tiles missing.")

    _, updated = api(
        "POST",
        f"/wp-json/wp/v2/pages/{PAGE_ID}",
        headers,
        ctx,
        {"content": new},
    )
    raw = updated.get("content", {}).get("raw") or ""
    if MARKER not in raw:
        die("POST succeeded but marker not in saved content.")

    view = f"{BASE}/technology-hub/"
    print(f"public {view} HEAD {public_status(view)}")
    for url in CHILD_URLS:
        print(f"child HEAD {public_status(url)} {url}")
    print("S1 applied.")


if __name__ == "__main__":
    main()
