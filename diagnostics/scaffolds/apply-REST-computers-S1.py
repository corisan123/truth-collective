#!/usr/bin/env python3
"""REST-computers-S1: restore photos from rev 8273, keep overlay (not explore-hub).

Staging only. Additional CSS untouched. No grayscale.
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

PAGE_ID = 359
BASE = os.environ.get("STAGING", "https://tcstaging.truth-collective.com").rstrip("/")
ROOT = Path(__file__).resolve().parents[2]
BACKUP_DIR = ROOT / "diagnostics" / "backups"
REV_PATH = BACKUP_DIR / "page-359-rev8273-2026-08-08-raw.html"
TICKET = "REST-computers-S1"
TODAY = date.today().isoformat()
MARKER = "TC STAGING PATCH COMPUTERS-S1"

MISSING = [
    {
        "title": "GMKtec AI Mini PC Ultra 9 285H",
        "href": "https://amzn.to/4baDejA",
        "id": 8219,
        "src": "https://tcstaging.truth-collective.com/wp-content/uploads/2026/07/51yoW2Hbg8L._AC_SL1184_-1-1024x898.jpg",
        "sub": "Ultra 9 285H · 32GB DDR5 · 1TB SSD",
        "why": "The 8 August catalog included this Mini PC. Restored from WordPress revision 8273.",
        "grade": "4.5",
    },
    {
        "title": "Yegolito 72GB Voice Recorder",
        "href": "https://amzn.to/4vPnXw1",
        "id": 8255,
        "src": "https://tcstaging.truth-collective.com/wp-content/uploads/2026/07/Facebook-Cover-AI-Agentic-Advances-1200-x-900-px-2.png",
        "sub": "72GB · USB-C · voice-activated",
        "why": "The 8 August catalog included this recorder. Restored from WordPress revision 8273.",
        "grade": "4.0",
    },
    {
        "title": "4-in-1 Digital Voice Recorder",
        "href": "https://amzn.to/4bBkHgz",
        "id": 8254,
        "src": "https://tcstaging.truth-collective.com/wp-content/uploads/2026/07/Facebook-Cover-AI-Agentic-Advances-1200-x-900-px-1.png",
        "sub": "32GB · noise reduction · wearable clip",
        "why": "The 8 August catalog included this recorder. Restored from WordPress revision 8273.",
        "grade": "4.5",
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


def amzn_map(rev: str) -> dict[str, tuple[int, str]]:
    out: dict[str, tuple[int, str]] = {}
    for m in re.finditer(
        r'wp-image-(\d+)[^>]*src="(https://tcstaging\.truth-collective\.com/wp-content/uploads/[^"]+)"[^>]*>\s*</a>|'
        r'src="(https://tcstaging\.truth-collective\.com/wp-content/uploads/[^"]+)"[^>]*class="[^"]*wp-image-(\d+)',
        rev,
    ):
        pass
    for m in re.finditer(
        r'href="(https://amzn\.to/[^"]+)"[\s\S]{0,900}?wp-image-(\d+)[\s\S]{0,400}?src="(https://tcstaging\.truth-collective\.com/wp-content/uploads/[^"]+)"|'
        r'wp-image-(\d+)[\s\S]{0,400}?src="(https://tcstaging\.truth-collective\.com/wp-content/uploads/[^"]+)"[\s\S]{0,400}?href="(https://amzn\.to/[^"]+)"|'
        r'link":"(https://amzn\.to/[^"]+)"[\s\S]{0,500}?wp-image-(\d+)[^"]*"[^>]*src="(https://tcstaging\.truth-collective\.com/wp-content/uploads/[^"]+)"',
        rev,
    ):
        g = m.groups()
        href = next((x for x in g if x and x.startswith("https://amzn.to/")), None)
        img_id = next((x for x in g if x and x.isdigit()), None)
        src = next((x for x in g if x and "/uploads/" in x), None)
        if href and img_id and src:
            code = href.rsplit("/", 1)[-1]
            out.setdefault(code, (int(img_id), src))
    # kadence image: link in comment then img
    for m in re.finditer(
        r'"link":"(https://amzn\.to/[^"]+)"[\s\S]{0,800}?wp-image-(\d+)"[^>]*/>|'
        r'"link":"(https://amzn\.to/[^"]+)"[\s\S]{0,800}?src="(https://tcstaging\.truth-collective\.com/wp-content/uploads/[^"]+)"[^>]*wp-image-(\d+)',
        rev,
    ):
        gs = [x for x in m.groups() if x]
        href = next((x for x in gs if x.startswith("https://amzn.to/")), None)
        src = next((x for x in gs if "/uploads/" in x), None)
        img_id = next((x for x in gs if x.isdigit()), None)
        if href and img_id:
            if not src:
                sm = re.search(
                    rf'wp-image-{img_id}[^>]*>|wp-image-{img_id}"',
                    rev,
                )
            code = href.rsplit("/", 1)[-1]
            if src:
                out.setdefault(code, (int(img_id), src))
    for m in re.finditer(
        r'<!-- wp:kadence/image \{[^}]*"id":(\d+),[^}]*"link":"(https://amzn\.to/[^"]+)"[\s\S]*?<img src="(https://tcstaging\.truth-collective\.com/wp-content/uploads/[^"]+)"',
        rev,
    ):
        img_id, href, src = m.group(1), m.group(2), m.group(3)
        out.setdefault(href.rsplit("/", 1)[-1], (int(img_id), src))
    for m in re.finditer(
        r'<a href="(https://amzn\.to/[^"]+)"[^>]*>\s*<img src="(https://tcstaging\.truth-collective\.com/wp-content/uploads/[^"]+)" alt="[^"]*" class="wp-image-(\d+)"',
        rev,
    ):
        href, src, img_id = m.group(1), m.group(2), m.group(3)
        out.setdefault(href.rsplit("/", 1)[-1], (int(img_id), src))
    # Live 19 Aug remapped three affiliate codes. Photos follow the 8273 card, not the remapped URL.
    out.update({
        "3TrPBl5": (
            8269,
            "https://tcstaging.truth-collective.com/wp-content/uploads/2026/07/Facebook-Cover-AI-Agentic-Advances-and-Emerging-Technologies-1000-x-1000-px-8.png",
        ),
        "4yGM8PT": (
            8270,
            "https://tcstaging.truth-collective.com/wp-content/uploads/2026/07/Facebook-Cover-AI-Agentic-Advances-and-Emerging-Technologies-1000-x-1000-px-9.png",
        ),
        "4x9Evjp": (
            8213,
            "https://tcstaging.truth-collective.com/wp-content/uploads/2026/07/Untitled-600-x-900-px-1000-x-1100-px-1200-x-900-px-2-1024x768.png",
        ),
        "44Pdk1e": (
            8238,
            "https://tcstaging.truth-collective.com/wp-content/uploads/2026/07/512mnLKArL._AC_SL1000_.jpg",
        ),
    })
    return out


NATIVE_IMG = """<!-- wp:image {{"lightbox":{{"enabled":false}},"id":{id},"sizeSlug":"large","linkDestination":"custom"}} -->
<figure class="wp-block-image size-large"><a href="{href}" rel="nofollow sponsored noopener" target="_blank"><img src="{src}" alt="{alt}" class="wp-image-{id}" loading="eager"/></a></figure>
<!-- /wp:image -->"""


def product_card(item: dict) -> str:
    return f"""<!-- wp:column {{"width":"50%","className":"tc-overlay-card tc-overlay-card-product"}} -->
<div class="wp-block-column tc-overlay-card tc-overlay-card-product" style="flex-basis:50%">{NATIVE_IMG.format(id=item['id'], href=item['href'], src=item['src'], alt=item['title'])}

<!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading"><a href="{item['href']}" rel="nofollow sponsored noopener" target="_blank">{item['title']}</a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {{"className":"tc-product-subtitle"}} -->
<p class="tc-product-subtitle">{item['sub']}</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"className":"tc-product-why"}} -->
<p class="tc-product-why">{item['why']}</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="tc-overlay-buttons">
  <a class="tc-affiliate-btn" href="{item['href']}" rel="nofollow sponsored noopener" target="_blank">View</a>
  <div class="tc-grade-btn" aria-label="Truth Collective Grade {item['grade']} out of 5">
    <span>TC Grade</span>
    <div class="tc-grade-block" style="--tc-grade:{item['grade']};" data-grade="{item['grade']}"></div>
  </div>
</div>
<!-- /wp:html --></div>
<!-- /wp:column -->"""


CSS = r"""@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600&family=Inter:wght@400;500;600&display=swap");
/* REST-computers-S1. Page chrome only. Additional CSS untouched. Overlay on products, never explore-hub. */

body.page-id-359 { background: #f8f4ec; }
body.page-id-359 .entry-content > .alignfull {
  margin-left: 0 !important; margin-right: 0 !important; max-width: none !important; width: 100% !important;
}
body.page-id-359 .tc-tech-cover.wp-block-group {
  position: relative !important; min-height: min(72vh, 640px) !important;
  margin: 0 !important; padding: 0 !important; overflow: hidden !important; background: #1e3a5f;
}
body.page-id-359 .tc-tech-cover > .tc-tech-cover__media,
body.page-id-359 .tc-tech-cover > figure.tc-tech-cover__media {
  position: absolute !important; inset: 0 !important; margin: 0 !important; width: 100% !important; height: 100% !important; z-index: 1 !important;
}
body.page-id-359 .tc-tech-cover > .tc-tech-cover__media img,
body.page-id-359 .tc-tech-cover > figure.tc-tech-cover__media img {
  display: block !important; width: 100% !important; height: 100% !important; object-fit: cover !important; filter: brightness(0.62);
}
body.page-id-359 .tc-tech-cover::after {
  content: ""; position: absolute; inset: 0; z-index: 2; pointer-events: none;
  background: linear-gradient(120deg, rgba(30,58,95,0.55) 0%, rgba(30,58,95,0.22) 60%, rgba(30,58,95,0.08) 100%);
}
body.page-id-359 .tc-tech-cover > .tc-tech-cover__content {
  position: relative !important; z-index: 3 !important; max-width: 720px !important; margin: 0 !important;
  padding: clamp(3.5rem, 8vw, 6.5rem) clamp(1.5rem, 5vw, 4rem) !important;
  min-height: min(72vh, 640px) !important; display: flex !important; flex-direction: column !important; justify-content: flex-end !important;
}
body.page-id-359 .tc-tech-cover__brand {
  margin: 0 0 1rem !important; font-family: Inter, sans-serif !important; font-size: 0.78rem !important;
  font-weight: 500 !important; letter-spacing: 0.22em !important; text-transform: uppercase !important; color: #b8944b !important;
}
body.page-id-359 .tc-tech-cover h1 {
  margin: 0 0 1.25rem !important; font-family: "Playfair Display", serif !important;
  font-size: clamp(2.4rem, 5vw, 3.6rem) !important; font-weight: 600 !important; line-height: 1.1 !important; color: #fff !important;
}
body.page-id-359 .tc-tech-cover__cta {
  display: inline-flex !important; align-items: center; gap: 0.45rem; width: fit-content;
  padding: 0.85rem 1.35rem !important; border: 1px solid rgba(255,255,255,0.55) !important;
  color: #fff !important; text-decoration: none !important; font-family: Inter, sans-serif !important;
  font-size: 0.78rem !important; letter-spacing: 0.16em !important; text-transform: uppercase !important; background: transparent !important;
}
body.page-id-359 .tc-section-eyebrow, body.page-id-359 .tc-hub-eyebrow {
  margin: 0 0 0.65rem !important; font-family: Inter, sans-serif !important; font-size: 0.75rem !important;
  font-weight: 500 !important; letter-spacing: 0.18em !important; text-transform: uppercase !important; color: #b8944b !important;
}
body.page-id-359 .tc-tech-intro-prose { background: #f8f4ec; padding: clamp(2.75rem, 5vw, 4.25rem) clamp(1.25rem, 4vw, 3rem) 1.5rem; max-width: 1180px; margin: 0 auto; }
body.page-id-359 .tc-tech-intro-split { display: flex !important; gap: clamp(2rem, 5vw, 4.5rem) !important; align-items: flex-start !important; }
body.page-id-359 .tc-tech-intro-split > .wp-block-column:first-child { flex-basis: 38% !important; }
body.page-id-359 .tc-tech-intro-split > .wp-block-column:last-child { flex-basis: 62% !important; }
body.page-id-359 .tc-hub-hero-title {
  margin: 0 !important; font-family: "Playfair Display", serif !important;
  font-size: clamp(2.2rem, 4vw, 3.1rem) !important; font-weight: 600 !important; line-height: 1.08 !important; color: #1e3a5f !important;
}
body.page-id-359 .tc-hub-hero-title em { color: #b8944b !important; font-style: italic !important; }
body.page-id-359 .tc-hub-hero-lead {
  margin: 0 0 1.15rem !important; max-width: 38rem; font-family: Inter, sans-serif !important;
  font-size: 1.05rem !important; line-height: 1.7 !important; color: #1f1f1f !important;
}
body.page-id-359 .tc-tech-stats {
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.25rem;
  max-width: 1180px; margin: 0 auto; padding: 1.5rem clamp(1.25rem, 4vw, 3rem) 2rem; background: #f8f4ec;
}
body.page-id-359 .tc-tech-stats__item { background: #fff; border: 1px solid rgba(30,58,95,0.12); padding: 1.15rem 1.2rem; }
body.page-id-359 .tc-tech-stats__item::before { content: ""; display: block; width: 1.5rem; height: 2px; background: #b8944b; margin-bottom: 0.65rem; }
body.page-id-359 .tc-tech-stats__label { margin: 0; font-family: Inter, sans-serif; font-size: 0.72rem; letter-spacing: 0.14em; text-transform: uppercase; color: #b8944b; }
body.page-id-359 .tc-tech-stats__value { margin: 0.35rem 0 0; font-family: "Playfair Display", serif; font-size: 1.15rem; color: #1e3a5f; }
body.page-id-359 .tc-hub-prose-section { background: #f8f4ec; max-width: 1180px; margin: 0 auto; padding: 0 clamp(1.25rem, 4vw, 3rem) 2.25rem; }
body.page-id-359 .tc-hub-prose-section .wp-block-heading {
  margin: 0 0 0.35rem !important; font-family: "Playfair Display", serif !important;
  font-size: clamp(1.7rem, 2.6vw, 2.15rem) !important; font-weight: 600 !important; color: #1e3a5f !important;
}
body.page-id-359 .tc-product-section { background: #f8f4ec; max-width: 1180px; margin: 0 auto; padding: 0 clamp(1.25rem, 4vw, 3rem) 2rem; }
/* Native overlay fill. Additional CSS still keys off .kt-inside-inner-col (Kadence). */
body.page-id-359 .tc-overlay-card {
  position: relative !important; overflow: hidden !important; min-height: 460px !important;
  background: #1f1f1f !important; margin: 0 !important;
}
body.page-id-359 .tc-overlay-card-product {
  min-height: 0 !important; height: auto !important; aspect-ratio: 1 / 1 !important;
  min-width: 0 !important; width: 100% !important; max-width: 100% !important;
}
body.page-id-359 .tc-overlay-card > .wp-block-image,
body.page-id-359 .tc-overlay-card > figure {
  position: absolute !important; inset: 0 !important; margin: 0 !important;
  width: 100% !important; height: 100% !important; z-index: 1 !important; overflow: hidden !important;
}
body.page-id-359 .tc-overlay-card > .wp-block-image a,
body.page-id-359 .tc-overlay-card > figure a {
  display: block !important; position: absolute !important; inset: 0 !important;
  width: 100% !important; height: 100% !important;
}
body.page-id-359 .tc-overlay-card img {
  display: block !important; width: 100% !important; height: 100% !important;
  object-fit: cover !important; object-position: center !important;
}
body.page-id-359 .entry-content .tc-overlay-card > h3,
body.page-id-359 .entry-content .tc-overlay-card > .wp-block-heading {
  position: absolute !important; left: 24px !important; right: 24px !important; bottom: 24px !important;
  z-index: 3 !important; margin: 0 !important; color: #fff !important;
  font-family: "Playfair Display", serif !important; font-size: 18px !important; font-weight: 700 !important;
  text-align: center !important; text-shadow: 0 1px 4px rgba(0,0,0,0.80) !important;
}
body.page-id-359 .entry-content .tc-overlay-card > h3 a,
body.page-id-359 .entry-content .tc-overlay-card > .wp-block-heading a {
  color: #fff !important; text-decoration: none !important;
}
body.page-id-359 .entry-content .tc-overlay-card > p {
  position: absolute !important; left: 28px !important; right: 28px !important; top: 50% !important;
  transform: translateY(-50%) !important; z-index: 3 !important; margin: 0 !important;
  color: #fff !important; font-family: Inter, sans-serif !important; font-size: 15px !important;
  line-height: 1.6 !important; text-align: center !important; opacity: 0 !important; pointer-events: none !important;
}
@media (hover: hover) and (pointer: fine) {
  body.page-id-359 .tc-overlay-card:hover { transform: translateY(-4px); }
  body.page-id-359 .tc-overlay-card:hover img { filter: brightness(0.7) !important; }
  body.page-id-359 .entry-content .tc-overlay-card:hover > h3,
  body.page-id-359 .entry-content .tc-overlay-card:hover > .wp-block-heading {
    bottom: auto !important; top: 28px !important;
  }
  body.page-id-359 .entry-content .tc-overlay-card:hover > p { opacity: 1 !important; }
}
body.page-id-359 .tc-dim-note { display: none !important; }
body.page-id-359 .tc-eval-brief {
  max-width: 1180px; margin: 0 auto 0.5rem; padding: 2.25rem clamp(1.25rem, 4vw, 3rem);
  background: #fff; border: 1px solid rgba(30,58,95,0.12); border-top: 3px solid #b8944b;
}
body.page-id-359 .tc-eval-brief h3 {
  font-family: "Playfair Display", serif !important; font-size: 1.7rem !important; color: #1e3a5f !important; margin: 0 0 1rem !important;
}
body.page-id-359 .tc-eval-brief p { font-family: Inter, sans-serif; font-size: 15px; line-height: 1.8; color: #1f1f1f; }
body.page-id-359 .tc-final-word { background: #f8f4ec; max-width: 1180px; margin: 0 auto; padding: 2.5rem clamp(1.25rem, 4vw, 3rem) 3rem; }
body.page-id-359 .tc-final-word .wp-block-heading {
  font-family: "Playfair Display", serif !important; font-size: clamp(1.8rem, 3vw, 2.35rem) !important; color: #1e3a5f !important;
}
@media (max-width: 780px) {
  body.page-id-359 .tc-tech-intro-split { flex-direction: column !important; }
  body.page-id-359 .tc-tech-stats { grid-template-columns: 1fr; }
}
"""


def shell(eyebrow: str, heading: str, class_name: str) -> str:
    return f"""<!-- wp:group {{"className":"tc-hub-prose-section {class_name}","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group tc-hub-prose-section {class_name}"><!-- wp:paragraph {{"className":"tc-section-eyebrow"}} -->
<p class="tc-section-eyebrow">{eyebrow}</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">{heading}</h2>
<!-- /wp:heading --></div>
<!-- /wp:group -->"""


def native_image_block(img_id: int, src: str, href: str, alt: str) -> str:
    return NATIVE_IMG.format(id=img_id, href=href, src=src, alt=alt)


def split_intro(html: str) -> str:
    if "tc-tech-intro-split" in html:
        return html
    m = re.search(
        r'(<!-- wp:group \{"className":"tc-tech-intro-prose"[\s\S]*?\} -->\s*<div[^>]*class="wp-block-group tc-tech-intro-prose"[^>]*>)([\s\S]*?)(</div>\s*<!-- /wp:group -->)',
        html,
    )
    if not m:
        return html
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
        return html
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


def replace_svg_cards(html: str, mapping: dict[str, tuple[int, str]]) -> tuple[str, int]:
    replaced = 0

    def sub_card(m: re.Match) -> str:
        nonlocal replaced
        block = m.group(0)
        hm = re.search(r'href="(https://amzn\.to/[^"]+)"', block)
        if not hm:
            return block
        href = hm.group(1)
        code = href.rsplit("/", 1)[-1]
        if code not in mapping:
            return block
        img_id, src = mapping[code]
        alt_m = re.search(r">([^<]+)</a></h3>", block)
        alt = alt_m.group(1).strip() if alt_m else "Product"
        native = native_image_block(img_id, src, href, alt)
        block = re.sub(
            r"<!-- wp:html -->\s*<figure class=\"tc-product-card\">.*?</figure>\s*<!-- /wp:html -->",
            native,
            block,
            count=1,
            flags=re.S,
        )
        block = re.sub(
            r"<!-- wp:paragraph \{\"className\":\"tc-dim-note\"\} -->\s*<p class=\"tc-dim-note\">.*?</p>\s*<!-- /wp:paragraph -->\s*",
            "",
            block,
            flags=re.S,
        )
        replaced += 1
        return block

    html = re.sub(
        r"<!-- wp:column \{[^}]*tc-overlay-card-product[\s\S]*?<!-- /wp:column -->",
        sub_card,
        html,
    )
    return html, replaced


def build(live: str, mapping: dict[str, tuple[int, str]]) -> str:
    html = live
    html, n = replace_svg_cards(html, mapping)
    print(f"replaced_cards {n}")
    html = split_intro(html)

    hero_src = "https://tcstaging.truth-collective.com/wp-content/uploads/2026/07/Facebook-Cover-AI-Agentic-Advances-and-Emerging-Technologies-1000-x-1000-px-1.png"
    hero = f"""<!-- wp:image {{"id":8233,"sizeSlug":"full","linkDestination":"none","align":"full","className":"tc-tech-cover__media"}} -->
<figure class="wp-block-image alignfull size-full tc-tech-cover__media"><img src="{hero_src}" alt="Computers and Digital Devices" class="wp-image-8233"/></figure>
<!-- /wp:image -->"""
    html = re.sub(
        r"<!-- wp:html -->\s*<figure class=\"tc-tech-cover__media\">.*?</figure>\s*<!-- /wp:html -->\s*\n\n<!-- wp:paragraph \{\"className\":\"tc-dim-note\"\} -->\s*<p class=\"tc-dim-note\">.*?</p>\s*<!-- /wp:paragraph -->",
        hero,
        html,
        count=1,
        flags=re.S,
    )

    html = html.replace(
        """  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Nine Categories</p>
    <p class="tc-tech-stats__value">Desktops through accessories</p>
  </div>
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Image Spec</p>
    <p class="tc-tech-stats__value">Hero 1600×1000 · Cards 1200×750</p>
  </div>""",
        """  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Parent Hub</p>
    <p class="tc-tech-stats__value">Technology Hub</p>
  </div>
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Catalog</p>
    <p class="tc-tech-stats__value">In-page product blocks</p>
  </div>""",
    )

    intro = html.find('<!-- wp:group {"className":"tc-tech-intro-prose"')
    stats_end = html.find("<!-- wp:group {\"className\":\"tc-product-section\"")
    if intro < 0 or stats_end < 0:
        die("Could not find intro/product section markers.")
    if "Who This Is For" not in html:
        html = (
            html[:stats_end]
            + shell("Audience", "Who This Is For", "tc-who")
            + "\n\n"
            + shell("Purpose", "Why This Matters", "tc-why")
            + "\n\n"
            + shell("When to use this page", "Best Uses", "tc-best-uses")
            + "\n\n"
            + html[stats_end:]
        )

    extra = """<!-- wp:group {"className":"tc-product-section","layout":{"type":"constrained"}} -->
<div class="wp-block-group tc-product-section"><!-- wp:paragraph {"className":"tc-tech-cat-kicker"} -->
<p class="tc-tech-cat-kicker">Restored from 8 August</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"className":"tc-tech-cat-heading"} -->
<h2 class="wp-block-heading tc-tech-cat-heading">Returned to the catalog</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"className":"tc-tech-cat-lead"} -->
<p class="tc-tech-cat-lead">These three listings were on the 8 August Computers page and were dropped in the 19 August placeholder rebuild. Photos and affiliate URLs come from WordPress revision 8273.</p>
<!-- /wp:paragraph -->

<!-- wp:columns {"className":"tc-product-row is-layout-flex wp-block-columns-is-layout-flex"} -->
<div class="wp-block-columns tc-product-row is-layout-flex wp-block-columns-is-layout-flex">"""
    extra += product_card(MISSING[0]) + "\n\n" + product_card(MISSING[1])
    extra += """</div>
<!-- /wp:columns -->

<!-- wp:columns {"className":"tc-product-row is-layout-flex wp-block-columns-is-layout-flex"} -->
<div class="wp-block-columns tc-product-row is-layout-flex wp-block-columns-is-layout-flex">"""
    extra += product_card(MISSING[2])
    extra += """</div>
<!-- /wp:columns --></div>
<!-- /wp:group -->

"""
    if "4baDejA" not in html:
        html = html.replace(
            "</div>\n<!-- /wp:group -->\n\n<!-- wp:html -->\n<p class=\"tc-computers-note\">",
            "</div>\n<!-- /wp:group -->\n\n" + extra + "<!-- wp:html -->\n<p class=\"tc-computers-note\">",
            1,
        )

    eval_html = f"""<!-- wp:html -->
<section class="tc-eval-brief" id="tc-eval-brief">
  <div class="tc-eval-brief__inner">
    <p class="tc-section-eyebrow">How We Evaluate Computers</p>
    <h3>Nothing Here Got In Because It Was Popular.</h3>
    <p>Every computer and digital device on this page is reviewed against the Truth Collective Trusted Selection Standards. Grades come from those reviews, not from marketplace star counts.</p>
    <a class="tc-eval-brief__link" href="{BASE}/6751-2/" rel="noopener">View Full Evaluation Standards</a>
  </div>
</section>
<!-- /wp:html -->"""
    final = """<!-- wp:group {"className":"tc-final-word","layout":{"type":"constrained"}} -->
<div class="wp-block-group tc-final-word"><!-- wp:paragraph {"className":"tc-section-eyebrow"} -->
<p class="tc-section-eyebrow">Closing</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Final Word</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Buy for the work you do, not for the loudest launch video. This page holds graded computers and digital devices reviewed against the same Trusted Selection Standards as the rest of the Technology Hub.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->"""

    html = re.sub(r"<!-- wp:block \{\"ref\":2870\} /-->\s*", "", html)
    html = re.sub(r"<!-- wp:block \{\"ref\":2847\} /-->\s*", "", html)
    html = re.sub(
        r"<!-- wp:heading -->\s*<h2 class=\"wp-block-heading\">Final Thoughts</h2>\s*<!-- /wp:heading -->\s*<!-- wp:paragraph -->\s*<p>Buy for the work you do[\s\S]*?</p>\s*<!-- /wp:paragraph -->",
        "",
        html,
    )

    tail = (
        '<!-- wp:block {"ref":2847} /-->\n\n'
        + eval_html
        + "\n\n"
        + final
        + "\n\n"
        + '<!-- wp:block {"ref":2870} /-->\n\n'
        + '<!-- wp:block {"ref":7532} /-->\n'
    )
    html = html.rstrip() + "\n\n" + tail

    style = f"<!-- wp:html -->\n<!-- {MARKER}: CSS only. Native images for Media Replace. {TODAY}. -->\n<style id=\"tc-computers-s1\">\n{CSS.strip()}\n</style>\n<!-- /wp:html -->\n\n"
    html = re.sub(
        r"<!-- wp:html -->\s*<!-- TC STAGING: Computers page light rebuild[\s\S]*?</style>\s*<!-- /wp:html -->\s*",
        style,
        html,
        count=1,
    )
    if MARKER not in html:
        html = style + html
    html = html.replace("tc-explore-hub", "tc-overlay-card-product")
    return html


def main() -> None:
    ctx, headers = client()
    if not REV_PATH.exists():
        die(f"Missing {REV_PATH}")
    rev = REV_PATH.read_text()
    mapping = amzn_map(rev)
    print("mapped_amzn", len(mapping), sorted(mapping)[:8])

    _, page = api("GET", f"/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", headers, ctx)
    live = page["content"]["raw"]
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup = BACKUP_DIR / f"page-{PAGE_ID}-before-{TICKET}-{TODAY}.html"
    if not backup.exists():
        backup.write_text(live)
        print(f"backup {backup} chars={len(live)}")

    new = build(live, mapping)
    if MARKER not in new:
        die("Marker missing.")
    if "tc-explore-hub" in new:
        die("explore-hub leaked onto Computers products.")
    if new.count("tc-overlay-card-product") < 20:
        die("Product overlay classes missing.")
    if "wp-image-8233" not in new:
        die("Hero photo missing.")
    if 'ref":7532' not in new:
        die("Social pattern missing.")
    eval_at = new.find('id="tc-eval-brief"')
    final_at = new.find('<h2 class="wp-block-heading">Final Word</h2>')
    if eval_at < 0 or final_at < 0 or eval_at > final_at:
        die("Eval must sit above Final Word.")
    live_codes = sorted(set(m.rsplit("/", 1)[-1] for m in re.findall(r"https://amzn\.to/[A-Za-z0-9]+", live)))
    unmapped = [c for c in live_codes if c not in mapping]
    if unmapped:
        die(f"Unmapped live affiliate codes: {unmapped}")

    _, updated = api("POST", f"/wp-json/wp/v2/pages/{PAGE_ID}", headers, ctx, {"content": new})
    raw = updated.get("content", {}).get("raw") or ""
    if MARKER not in raw:
        die("POST succeeded but marker missing.")
    view = f"{BASE}/technology-hub/computers-digital-devices/"
    print(f"public {view} HEAD {public_status(view)}")
    print("S1 computers applied.")


if __name__ == "__main__":
    main()
