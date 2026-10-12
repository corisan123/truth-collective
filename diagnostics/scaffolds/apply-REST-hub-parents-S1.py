#!/usr/bin/env python3
"""REST-hub-parents-S1: Books, Office, Lighting, Productivity, Self-Help.

Page chrome only. Restore native-tile fill so locked .tc-explore-hub animation
works without Kadence .kt-inside-inner-col. Additional CSS untouched.
No grayscale. Staging only. Slot copy stays empty.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import ssl
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

BASE = os.environ.get("STAGING", "https://tcstaging.truth-collective.com").rstrip("/")
ROOT = Path(__file__).resolve().parents[2]
BACKUP_DIR = ROOT / "diagnostics" / "backups"
CSS_PATH = Path(__file__).with_name("REST-hub-parents-S1.css")
TICKET = "REST-hub-parents-S1"
TODAY = date.today().isoformat()
MARKER = "TC STAGING PATCH HUB-PARENT-S1"

HUBS = [
    {
        "id": 38,
        "name": "Recommended Books",
        "eval_eyebrow": "How We Evaluate Books",
        "eval_p": "Every category on this page is reviewed against the Truth Collective Trusted Selection Standards. Titles earn a place by usefulness, clarity, and lasting value, not by marketing volume.",
        "tile_links": {
            "Leadership Books": f"{BASE}/recommended-books-2026/leadership-books/",
            "Communication and Persuasion": f"{BASE}/recommended-books-2026/communication-and-persuasion/",
        },
    },
    {
        "id": 5939,
        "name": "Office Workspace",
        "eval_eyebrow": "How We Evaluate Office Workspace",
        "eval_p": "Every path on this page is reviewed against the Truth Collective Trusted Selection Standards. Furniture and tools earn a place by supporting clearer work, not by trend.",
        "tile_links": {},
    },
    {
        "id": 115,
        "name": "Smart Lighting",
        "eval_eyebrow": "How We Evaluate Smart Lighting",
        "eval_p": "Every path on this page is reviewed against the Truth Collective Trusted Selection Standards. Lighting earns a place by supporting work, rest, and safety, not by novelty.",
        "tile_links": {},
    },
    {
        "id": 5680,
        "name": "Productivity Tools",
        "eval_eyebrow": "How We Evaluate Productivity Tools",
        "eval_p": "Every path on this page is reviewed against the Truth Collective Trusted Selection Standards. Tools earn a place by proving useful and reliable.",
        "tile_links": {},
    },
    {
        "id": 86,
        "name": "Self-Help and Mental Wellness",
        "eval_eyebrow": "How We Evaluate Self-Help and Mental Wellness",
        "eval_p": "Every path on this page is reviewed against the Truth Collective Trusted Selection Standards. These pages exist to reduce friction when someone is ready to begin, reset, or ask for help.",
        "tile_links": {},
    },
]


def die(msg: str) -> None:
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


def shell(eyebrow: str, heading: str, class_name: str) -> str:
    return f"""<!-- wp:group {{"className":"tc-hub-prose-section {class_name}","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group tc-hub-prose-section {class_name}"><!-- wp:paragraph {{"className":"tc-section-eyebrow"}} -->
<p class="tc-section-eyebrow">{eyebrow}</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">{heading}</h2>
<!-- /wp:heading --></div>
<!-- /wp:group -->"""


def css_for(pid: int) -> str:
    return CSS_PATH.read_text().replace("__PID__", str(pid))


def replace_style(html: str, pid: int) -> str:
    css = css_for(pid)
    block = (
        "<!-- wp:html -->\n"
        f"<!-- {MARKER}: CSS only. Native images for Media Replace. {TODAY}. -->\n"
        f'<style id="tc-hub-parent-s1">\n{css.strip()}\n</style>\n'
        "<!-- /wp:html -->\n\n"
    )
    html = re.sub(
        r"<!-- wp:html -->\s*<!-- TC STAGING:[\s\S]*?</style>\s*<!-- /wp:html -->\s*",
        block,
        html,
        count=1,
    )
    if MARKER not in html:
        start = html.find('<style id="tc-hub-parent-s1">')
        end = html.find("</style>", start) if start >= 0 else -1
        if start >= 0 and end >= 0:
            html = html[:start] + f'<style id="tc-hub-parent-s1">\n{css.strip()}\n</style>' + html[end + 8 :]
        else:
            html = block + html
    return html


def split_intro(html: str) -> str:
    if "tc-tech-intro-split" in html:
        return html
    m = re.search(
        r'(<!-- wp:group \{"className":"tc-tech-intro-prose"[\s\S]*?\} -->\s*<div[^>]*class="wp-block-group tc-tech-intro-prose"[^>]*>)([\s\S]*?)(</div>\s*<!-- /wp:group -->)',
        html,
    )
    if not m:
        die("Could not find intro group.")
    inner = m.group(2).strip()
    eyebrow = re.search(
        r'<!-- wp:paragraph \{"className":"tc-hub-eyebrow"\} -->\s*<p class="tc-hub-eyebrow">.*?</p>\s*<!-- /wp:paragraph -->',
        inner,
        re.S,
    )
    heading = re.search(
        r'<!-- wp:heading \{"className":"tc-hub-hero-title"\} -->\s*<h2 class="wp-block-heading tc-hub-hero-title">.*?</h2>\s*<!-- /wp:heading -->',
        inner,
        re.S,
    )
    leads = re.findall(
        r'<!-- wp:paragraph \{"className":"tc-hub-hero-lead"\} -->\s*<p class="tc-hub-hero-lead">.*?</p>\s*<!-- /wp:paragraph -->',
        inner,
        re.S,
    )
    meta = re.search(
        r'<!-- wp:group \{"className":"tc-tech-meta-row"[\s\S]*?<!-- /wp:group -->',
        inner,
    )
    if not (eyebrow and heading and leads):
        die("Intro pieces missing for split.")
    left = eyebrow.group(0) + "\n\n" + heading.group(0)
    right = "\n\n".join(leads)
    if meta:
        right += "\n\n" + meta.group(0)
    rebuilt = f"""{m.group(1)}<!-- wp:columns {{"className":"tc-tech-intro-split"}} -->
<div class="wp-block-columns tc-tech-intro-split"><!-- wp:column {{"width":"38%"}} -->
<div class="wp-block-column" style="flex-basis:38%">{left}</div>
<!-- /wp:column -->

<!-- wp:column {{"width":"62%"}} -->
<div class="wp-block-column" style="flex-basis:62%">{right}</div>
<!-- /wp:column --></div>
<!-- /wp:columns -->{m.group(3)}"""
    return html[: m.start()] + rebuilt + html[m.end() :]


def insert_shells(html: str) -> str:
    if "Who This Is For" in html:
        return html
    marker = '<!-- wp:group {"className":"tc-tech-cat-section"'
    i = html.find(marker)
    if i < 0:
        die("Could not find category section.")
    block = (
        shell("Audience", "Who This Is For", "tc-who")
        + "\n\n"
        + shell("Purpose", "Why This Matters", "tc-why")
        + "\n\n"
        + shell("When to use this hub", "Best Uses", "tc-best-uses")
        + "\n\n"
    )
    return html[:i] + block + html[i:]


def link_tiles(html: str, links: dict[str, str]) -> str:
    for title, url in links.items():
        pattern = (
            r'(<!-- wp:image \{[^}]*"linkDestination":")(?:none|custom)("[^}]*\} -->\s*'
            r'<figure class="wp-block-image[^"]*">)(?:<a href="[^"]*">)?'
            rf'(<img [^>]*class="wp-image-\d+"[^>]*>)(?:</a>)?'
            r'(</figure>\s*<!-- /wp:image -->\s*\n\n<!-- wp:heading[^>]*-->\s*'
            rf'<h3 class="wp-block-heading[^"]*">{re.escape(title)}</h3>)'
        )

        def sub(m: re.Match, href=url) -> str:
            img = m.group(3)
            if "loading=" not in img:
                img = img.replace("<img ", '<img loading="eager" ', 1)
            if f'alt=""' in img or "alt=''" in img:
                img = img.replace('alt=""', f'alt="{title}"').replace("alt=''", f'alt="{title}"')
            return f'{m.group(1)}custom{m.group(2)}<a href="{href}">{img}</a>{m.group(4)}'

        html, n = re.subn(pattern, sub, html, count=1, flags=re.S)
        if n != 1:
            # simpler: figure without anchor immediately before this h3
            loose = re.compile(
                rf'(<figure class="wp-block-image[^"]*">)(?!<a )(<img [^>]+>)(</figure>\s*<!-- /wp:image -->\s*\n\n<!-- wp:heading[^>]*-->\s*<h3 class="wp-block-heading[^"]*">{re.escape(title)}</h3>)',
                re.S,
            )

            def sub2(m: re.Match, href=url) -> str:
                img = m.group(2)
                if "loading=" not in img:
                    img = img.replace("<img ", '<img loading="eager" ', 1)
                return f'{m.group(1)}<a href="{href}">{img}</a>{m.group(3)}'

            html, n2 = loose.subn(sub2, html, count=1)
            if n2 != 1:
                die(f"Could not wrap tile link for {title!r}")
    return html


def eager_images(html: str) -> str:
    html = html.replace(' loading="lazy"', "")

    def eager(tag: str) -> str:
        if "loading=" in tag:
            return tag
        return tag.replace("<img ", '<img loading="eager" ', 1)

    return re.sub(r"<img[^>]*>", lambda m: eager(m.group(0)), html)


def extract_final_paragraph(html: str) -> str:
    m = re.search(
        r'<!-- wp:heading -->\s*<h2 class="wp-block-heading">Final Thoughts</h2>\s*<!-- /wp:heading -->\s*<!-- wp:paragraph -->\s*<p>(.*?)</p>\s*<!-- /wp:paragraph -->',
        html,
        re.S,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    leads = re.findall(r'<p class="tc-hub-hero-lead">(.*?)</p>', html, re.S)
    if leads:
        return re.sub(r"\s+", " ", leads[-1]).strip()
    return "This hub is reviewed against the Truth Collective Trusted Selection Standards."


def strip_tail_patterns(html: str) -> tuple[str, str]:
    """Remove 2847/2870/7532 refs, Final Thoughts, return leftover signup html if any."""
    signup = ""
    m = re.search(
        r'<!-- wp:html \{"metadata":\{[^}]*patternName":"core/block/6747"[\s\S]*?<!-- /wp:html -->',
        html,
    )
    if m:
        signup = m.group(0)
        html = html[: m.start()] + html[m.end() :]
    html = re.sub(r"<!-- wp:block \{\"ref\":2870\} /-->\s*", "", html)
    html = re.sub(r"<!-- wp:block \{\"ref\":2847\} /-->\s*", "", html)
    html = re.sub(r"<!-- wp:block \{\"ref\":7532\} /-->\s*", "", html)
    html = re.sub(
        r'<!-- wp:heading -->\s*<h2 class="wp-block-heading">Final Thoughts</h2>\s*<!-- /wp:heading -->\s*(?:<!-- wp:paragraph -->\s*<p>.*?</p>\s*<!-- /wp:paragraph -->\s*)?',
        "",
        html,
        flags=re.S,
    )
    return html.rstrip(), signup


def eval_html(hub: dict) -> str:
    return f"""<!-- wp:html -->
<section class="tc-eval-brief" id="tc-eval-brief">
  <div class="tc-eval-brief__inner">
    <p class="tc-section-eyebrow">{hub["eval_eyebrow"]}</p>
    <h3>Nothing Here Got In Because It Was Popular.</h3>
    <p>{hub["eval_p"]}</p>
    <a class="tc-eval-brief__link" href="{BASE}/6751-2/" rel="noopener">View Full Evaluation Standards</a>
  </div>
</section>
<!-- /wp:html -->"""


def final_html(text: str) -> str:
    return f"""<!-- wp:group {{"className":"tc-final-word","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group tc-final-word"><!-- wp:paragraph {{"className":"tc-section-eyebrow"}} -->
<p class="tc-section-eyebrow">Closing</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Final Word</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{text}</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->"""


def build(live: str, hub: dict) -> str:
    html = live
    final_text = extract_final_paragraph(html)
    html = replace_style(html, hub["id"])
    html = split_intro(html)
    html = insert_shells(html)
    html = link_tiles(html, hub["tile_links"])
    html = eager_images(html)
    html, signup = strip_tail_patterns(html)
    tail = ""
    if signup:
        tail += signup + "\n\n"
    tail += (
        '<!-- wp:block {"ref":2847} /-->\n\n'
        + eval_html(hub)
        + "\n\n"
        + final_html(final_text)
        + "\n\n"
        + '<!-- wp:block {"ref":2870} /-->\n\n'
        + '<!-- wp:block {"ref":7532} /-->\n'
    )
    html = html.rstrip() + "\n\n" + tail
    if "tc-explore-hub" not in html:
        die(f"Explore tiles missing on {hub['name']}.")
    if "tc-overlay-card" in html and "tc-explore-hub" in html:
        # product overlay must not share the explore class on this pass
        if re.search(r"tc-overlay-card[^\"']*tc-explore-hub|tc-explore-hub[^\"']*tc-overlay-card", html):
            die(f"Overlay+explore crop combo on {hub['name']}.")
    eval_at = html.find('id="tc-eval-brief"')
    final_at = html.find('<h2 class="wp-block-heading">Final Word</h2>')
    social_at = html.find('ref":7532')
    if eval_at < 0 or final_at < 0 or eval_at > final_at:
        die("Eval must sit above Final Word.")
    if social_at < final_at:
        die("Social pattern must be last.")
    if "figure a" not in css_for(hub["id"]):
        die("Tile-fill CSS missing figure a.")
    if "min-height: 460px" not in css_for(hub["id"]):
        die("Locked 460px tile height missing.")
    return html


def apply_one(hub: dict, ctx, headers, dry: bool) -> None:
    pid = hub["id"]
    _, page = api("GET", f"/wp-json/wp/v2/pages/{pid}?context=edit", headers, ctx)
    live = page["content"]["raw"]
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup = BACKUP_DIR / f"page-{pid}-before-{TICKET}-{TODAY}.html"
    if not backup.exists():
        backup.write_text(live)
        print(f"backup {backup} chars={len(live)}")
    else:
        print(f"backup exists {backup}")
    new = build(live, hub)
    built = BACKUP_DIR / f"page-{pid}-built-{TICKET}-{TODAY}.html"
    built.write_text(new)
    print(f"built {built} chars={len(new)} explore={new.count('tc-explore-hub')} who={'Who This Is For' in new}")
    if dry:
        print(f"dry-run skip POST {pid} {hub['name']}")
        return
    _, updated = api("POST", f"/wp-json/wp/v2/pages/{pid}", headers, ctx, {"content": new})
    raw = updated.get("content", {}).get("raw") or ""
    if MARKER not in raw:
        die("POST succeeded but marker missing.")
    if "min-height: 460px" not in raw or "figure a" not in raw:
        die("Tile-fill CSS not saved.")
    link = page.get("link") or f"{BASE}/?page_id={pid}"
    print(f"public {link} HEAD {public_status(link)}")
    print(f"S1 hub parent applied {pid} {hub['name']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int, default=0, help="Apply one hub id, or all.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    ctx, headers = client()
    chosen = [h for h in HUBS if not args.id or h["id"] == args.id]
    if not chosen:
        die(f"Unknown hub id {args.id}")
    for hub in chosen:
        apply_one(hub, ctx, headers, args.dry_run)


if __name__ == "__main__":
    main()
