#!/usr/bin/env python3
"""REST-hub-technology-S1c: Technology Hub parent until this page is correct.

Follows website-settings Additional CSS: overlay-card on the column,
explore-hub on the image, title rises to top 28px above centered EXPLORE.
Fills Who / Why / Best from existing hub copy. Staging only. No Additional CSS write.
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
TICKET = "REST-hub-technology-S1c"
TODAY = date.today().isoformat()
MARKER = "TC STAGING PATCH TECH-HUB-S1"
COMPUTERS_URL = f"{BASE}/technology-hub/computers-digital-devices/"

# Pre-10Web / existing hub copy. No invented stats.
TILE_BLURBS = {
    "Computers and Digital Devices": "Laptops, desktops, and the devices that carry the day.",
    "Monitors and Displays": "Displays graded for clarity, comfort, and long work sessions.",
    "Audio and Video": "Workspace audio and video selected for clear signal, not clutter.",
    "Headphones and Headsets": "From deep work focus to clear communication to hearing safety, the right audio gear matters. Reviewed and ranked across studio, office, and active environments.",
    "Desk Speakers": "Desk and office speakers chosen for clean, controlled sound.",
    "Projectors and Microphones": "Projection and microphone tools for rooms that need to be heard.",
    "Digital Smart Tablets": "For thinkers, artists, planners, and professionals. Tablets, digital writing devices, and creative tools that capture ideas the moment they arrive.",
    "Interactive Digital Displays": "Beyond standard monitors, digital displays for presentations, conference rooms, video walls, and creative installations. Built for scale and visual impact.",
    "Emerging Technologies": "Tools still in their early days. A curated look at the real technologies entering the market and reshaping how work, learning, and creativity will happen next.",
    "AI Wearables": "The wearable layer of artificial intelligence. AR glasses, smart rings, AI pins, biometric sensors, and the devices quietly changing how we work and live.",
}
HOLD_TITLES = {
    "Emerging Technologies": COMPUTERS_URL,
    "AI Wearables": COMPUTERS_URL,
}

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


def slice_from_to(html: str, start: str, end: str) -> str:
    i = html.find(start)
    j = html.find(end, i + 1 if i >= 0 else 0)
    if i < 0 or j < 0:
        die(f"Could not slice from {start[:60]!r} to {end[:60]!r}")
    return html[i:j].rstrip()


def build(live: str) -> str:
    css = CSS_PATH.read_text()
    hero = slice_from_to(
        live,
        '<!-- wp:group {"align":"full","className":"tc-tech-cover"',
        '<!-- wp:group {"className":"tc-tech-intro-prose"',
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
        "the largest of Truth Collective's nine hubs",
        "the largest of the six product hubs at Truth Collective",
    )

    cat = slice_from_to(
        live,
        '<!-- wp:group {"className":"tc-tech-cat-section"',
        '<!-- wp:heading {"style":{"elements":{"link":{"color":{"text":"var:preset|color|ast-global-color-4"}}}}',
    )
    cat = cat.replace(
        "Eight paths. Each one reviewed against the Truth Collective Trusted Selection Standards before it earns a place here.",
        "Eight category pages, each reviewed against the Truth Collective Trusted Selection Standards. Emerging Technologies and AI Wearables remain on this grid until those child pages exist.",
    )
    cat = cat.replace('alt="" class="wp-image-8318"', 'alt="Monitors and Displays" class="wp-image-8318"')
    cat = cat.replace('alt="" class="wp-image-8316"', 'alt="Headphones and Headsets" class="wp-image-8316"')
    cat = cat.replace('alt="" class="wp-image-8319"', 'alt="Emerging Technologies" class="wp-image-8319"')
    cat = cat.replace('alt="" class="wp-image-8320"', 'alt="AI Wearables" class="wp-image-8320"')
    cat = cat.replace(' loading="lazy"', "")
    cat = re.sub(r"<img(?![^>]*loading=)", '<img loading="eager"', cat)
    cat = rewrite_tiles(cat)

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

    final_p = re.search(
        r'<p class="has-ast-global-color-4-color has-text-color has-link-color">The Technology Hub holds eight trusted paths,.*?</p>',
        live,
        re.S,
    )
    if not final_p:
        die("Could not extract Final Thoughts paragraph.")
    final_inner = re.sub(r"^<p[^>]*>", "", final_p.group(0))
    final_inner = re.sub(r"</p>$", "", final_inner)

    def shell(eyebrow: str, heading: str, class_name: str, body: str) -> str:
        paras = "\n\n".join(
            f"""<!-- wp:paragraph -->
<p>{p}</p>
<!-- /wp:paragraph -->"""
            for p in body
        )
        return f"""<!-- wp:group {{"className":"tc-hub-prose-section {class_name}","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group tc-hub-prose-section {class_name}"><!-- wp:paragraph {{"className":"tc-section-eyebrow"}} -->
<p class="tc-section-eyebrow">{eyebrow}</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">{heading}</h2>
<!-- /wp:heading -->

{paras}</div>
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
        shell(
            "Audience",
            "Who This Is For",
            "tc-who",
            [
                "This hub is for people choosing computers, displays, audio, and the supporting tools that shape daily work and creative life.",
                "Start with the category that matches what you need most, then move outward to the tools that complete the setup.",
            ],
        ),
        "",
        shell(
            "Purpose",
            "Why This Matters",
            "tc-why",
            [
                "Every category on this page has been reviewed and graded against the Truth Collective Trusted Selection Standards before it earns a place here.",
                "We do not list everything available. We list what we trust, selected for build quality, daily usefulness, and long term value.",
            ],
        ),
        "",
        shell(
            "When to use this hub",
            "Best Uses",
            "tc-best-uses",
            [
                "Use this hub by need, not by brand. Daily essentials that hold work together sit beside tools that lift performance or open a new way of working.",
                "Each published category leads to a dedicated page where products are ranked, graded, and explained. Emerging Technologies and AI Wearables stay on this grid and currently open the Computers page, where those listings already live, until dedicated child pages exist.",
            ],
        ),
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


def filled_shell(eyebrow: str, heading: str, class_name: str, body: list[str]) -> str:
    paras = "\n\n".join(
        f"""<!-- wp:paragraph -->
<p>{p}</p>
<!-- /wp:paragraph -->"""
        for p in body
    )
    return f"""<!-- wp:group {{"className":"tc-hub-prose-section {class_name}","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group tc-hub-prose-section {class_name}"><!-- wp:paragraph {{"className":"tc-section-eyebrow"}} -->
<p class="tc-section-eyebrow">{eyebrow}</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">{heading}</h2>
<!-- /wp:heading -->

{paras}</div>
<!-- /wp:group -->"""


def rewrite_tiles(html: str) -> str:
    """Move explore-hub onto the image, overlay-card onto the column, restore blurbs."""

    def add_explore_on_image(block: str) -> str:
        if '"className":"tc-explore-hub"' not in block:
            block = block.replace(
                '"linkDestination":"custom"} -->',
                '"linkDestination":"custom","className":"tc-explore-hub"} -->',
                1,
            )
            block = block.replace(
                '"linkDestination":"none"} -->',
                '"linkDestination":"custom","className":"tc-explore-hub"} -->',
                1,
            )
        if "tc-explore-hub" not in block.split("<!-- /wp:image -->")[0]:
            die("Could not put tc-explore-hub on the image comment")
        block = block.replace(
            '<figure class="wp-block-image size-full">',
            '<figure class="wp-block-image size-full tc-explore-hub">',
            1,
        )
        block = block.replace(
            '<figure class="wp-block-image size-full tc-explore-hub tc-explore-hub">',
            '<figure class="wp-block-image size-full tc-explore-hub">',
        )
        return block

    def add_blurb(block: str, title: str) -> str:
        blurb = TILE_BLURBS.get(title)
        if not blurb:
            die(f"No existing blurb mapped for tile {title!r}")
        if blurb in block:
            return block
        heading_end = block.find("<!-- /wp:heading -->")
        if heading_end < 0:
            die(f"Tile heading close missing for {title!r}")
        insert_at = heading_end + len("<!-- /wp:heading -->")
        para = f"""

<!-- wp:paragraph -->
<p>{blurb}</p>
<!-- /wp:paragraph -->"""
        return block[:insert_at] + para + block[insert_at:]

    def link_hold(block: str, title: str) -> str:
        url = HOLD_TITLES.get(title)
        if not url:
            return block
        if f'href="{url}"' in block:
            return block
        img = re.search(r"<img\b[^>]*>", block)
        if not img:
            die(f"Hold tile {title!r} has no img")
        if "<a " in block[img.start() - 80 : img.end() + 20]:
            return block
        wrapped = f'<a href="{url}">{img.group(0)}</a>'
        return block[: img.start()] + wrapped + block[img.end() :]

    pattern = re.compile(
        r'<!-- wp:column \{"width":"50%","className":"tc-(?:explore-hub|overlay-card)"\} -->'
        r".*?"
        r"<!-- /wp:column -->",
        re.S,
    )

    def one(m: re.Match) -> str:
        block = m.group(0)
        title_m = re.search(
            r'<h3 class="wp-block-heading has-text-align-center">(.*?)</h3>',
            block,
        )
        if not title_m:
            die("Explore tile missing h3 title")
        title = title_m.group(1)
        block = block.replace(
            '{"width":"50%","className":"tc-explore-hub"}',
            '{"width":"50%","className":"tc-overlay-card"}',
        )
        block = block.replace(
            '<div class="wp-block-column tc-explore-hub"',
            '<div class="wp-block-column tc-overlay-card"',
        )
        block = add_explore_on_image(block)
        block = link_hold(block, title)
        block = add_blurb(block, title)
        if "tc-overlay-card" not in block or "tc-explore-hub" not in block:
            die(f"Class split failed for {title!r}")
        return block

    new, n = pattern.subn(one, html)
    if n != 10:
        die(f"Expected 10 hub tiles, rewrote {n}")
    return new


def replace_shells(html: str) -> str:
    shells = [
        (
            "tc-who",
            filled_shell(
                "Audience",
                "Who This Is For",
                "tc-who",
                [
                    "This hub is for people choosing computers, displays, audio, and the supporting tools that shape daily work and creative life.",
                    "Start with the category that matches what you need most, then move outward to the tools that complete the setup.",
                ],
            ),
        ),
        (
            "tc-why",
            filled_shell(
                "Purpose",
                "Why This Matters",
                "tc-why",
                [
                    "Every category on this page has been reviewed and graded against the Truth Collective Trusted Selection Standards before it earns a place here.",
                    "We do not list everything available. We list what we trust, selected for build quality, daily usefulness, and long term value.",
                ],
            ),
        ),
        (
            "tc-best-uses",
            filled_shell(
                "When to use this hub",
                "Best Uses",
                "tc-best-uses",
                [
                    "Use this hub by need, not by brand. Daily essentials that hold work together sit beside tools that lift performance or open a new way of working.",
                    "Each published category leads to a dedicated page where products are ranked, graded, and explained. Emerging Technologies and AI Wearables stay on this grid and currently open the Computers page, where those listings already live, until dedicated child pages exist.",
                ],
            ),
        ),
    ]
    new = html
    for class_name, replacement in shells:
        pat = re.compile(
            rf'<!-- wp:group \{{"className":"tc-hub-prose-section {class_name}".*?'
            rf"<!-- /wp:group -->",
            re.S,
        )
        new, n = pat.subn(replacement, new, count=1)
        if n != 1:
            die(f"Could not replace {class_name} shell ({n})")
    return new


def patch_existing(live: str, css: str) -> str:
    start = live.find('<style id="tc-tech-hub-s1">')
    end = live.find("</style>", start)
    if start < 0 or end < 0:
        die("S1 style block missing on an already-patched page.")
    new = live[:start] + f'<style id="tc-tech-hub-s1">\n{css.strip()}\n</style>' + live[end + 8 :]
    new = replace_shells(new)
    new = rewrite_tiles(new)

    def eager(tag: str) -> str:
        if "loading=" in tag:
            return tag
        return tag.replace("<img ", '<img loading="eager" ', 1)

    new = new.replace(' loading="lazy"', "")
    new = re.sub(r"<img[^>]*>", lambda m: eager(m.group(0)), new)
    return new


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
    suffix = "S1b" if MARKER in live else TICKET
    backup = BACKUP_DIR / f"page-{PAGE_ID}-before-REST-hub-technology-{suffix}-{TODAY}.html"
    if not backup.exists():
        backup.write_text(live)
        print(f"backup {backup} chars={len(live)}")
    else:
        print(f"backup exists {backup} (left in place)")

    css = CSS_PATH.read_text()
    if MARKER in live:
        new = patch_existing(live, css)
        print("mode patch-existing")
    else:
        new = build(live)
        print("mode full-rebuild")
    if MARKER not in new:
        die("Marker missing from built HTML.")
    if "tc-explore-hub" not in new or "tc-eval-brief" not in new:
        die("Required classes missing from built HTML.")
    if new.count("className\":\"tc-overlay-card\"") != 10:
        die(f"Expected 10 overlay columns, got {new.count('className\":\"tc-overlay-card\"')}")
    if new.count("tc-explore-hub") < 10:
        die("Explore tiles missing.")
    if "bottom: 46% !important" in new or "bottom:46% !important" in new:
        die("Invented 46 percent hover still present.")
    if "top: 28px" not in new:
        die("Overlay hover top:28px missing from page CSS.")
    if "We do not list everything available" not in new:
        die("Who/Why/Best still empty.")
    if 'href="' + COMPUTERS_URL + '"' not in new:
        die("Emerging/AI Wearables hold link to Computers missing.")
    if "figure a" not in css or "loading=\"eager\"" not in new:
        die("S1b tile-fill markers missing.")

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
    if "inset: 0" not in raw or "figure a" not in raw:
        die("Tile-fill CSS not in saved content.")

    view = f"{BASE}/technology-hub/"
    print(f"public {view} HEAD {public_status(view)}")
    for url in CHILD_URLS:
        print(f"child HEAD {public_status(url)} {url}")
    print("S1 applied.")


if __name__ == "__main__":
    main()
