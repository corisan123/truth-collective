#!/usr/bin/env python3
"""R9: Convert Tech Hub top from Custom HTML images to native WP/Kadence blocks.

Daniel can click each image → Replace in the editor.
Only CSS + small reveal script remain in Custom HTML.
"""
from __future__ import annotations

import base64
import json
import os
import re
import ssl
import urllib.request
from datetime import date
from pathlib import Path

PAGE_ID = 111
BASE = os.environ.get("STAGING", "https://tcstaging.truth-collective.com").rstrip("/")
ROOT = Path(__file__).resolve().parents[2]
BACKUP_DIR = ROOT / "diagnostics" / "backups"

# placeholder media (Daniel replaces in editor). Audio uses nearest library match.
TILES = [
    {
        "title": "Computers and Digital Devices",
        "href": f"{BASE}/technology-hub/computers-digital-devices/",
        "id": 5856,
        "src": f"{BASE}/wp-content/uploads/2026/06/Untitled-1000-x-1188-px-1000-x-1188-px-1900-x-1080-px-1000-x-800-px-400-x-400-px-270-x-270-px-1000-x-1188-px-1.png",
    },
    {
        "title": "Monitors and Displays",
        "href": f"{BASE}/technology-hub/monitor-display/",
        "id": 5633,
        "src": f"{BASE}/wp-content/uploads/2026/06/Untitled-1200-x-628-px-1200-x-628-px-1200-x-628-px-1200-x-628-px-1000-x-628-px-1000-x-628-px-1900-x-1080-px-1920-x-1350-px-1200-x-900-px-1200-x-900-px-600-x-600-px-1080-x-13-41.png",
    },
    {
        "title": "Audio and Video",
        "href": f"{BASE}/technology-hub/audio-and-video/",
        "id": 1370,
        "src": f"{BASE}/wp-content/uploads/2026/04/Untitled-2552-x-1280-px.png",
    },
    {
        "title": "Headphones and Headsets",
        "href": f"{BASE}/technology-hub/headphones-for-work/",
        "id": 1421,
        "src": f"{BASE}/wp-content/uploads/2026/04/Untitled-2552-x-1280-px-2552-x-1080-px.png",
    },
    {
        "title": "Desk Speakers",
        "href": f"{BASE}/technology-hub/speakers-home-office-outdoors/",
        "id": 1450,
        "src": f"{BASE}/wp-content/uploads/2026/04/Untitled-800-x-2000-px-1200-x-1800-px-1400-x-600-px-1400-x-600-px-1800-x-800-px-1400-x-800-px-1200-x-1000-px-1.png",
    },
    {
        "title": "Projectors and Microphones",
        "href": f"{BASE}/technology-hub/projectors-and-microphones/",
        "id": 5944,
        "src": f"{BASE}/wp-content/uploads/2026/06/Untitled-1000-x-800-px-1000-x-650-px-1900-x-1080-px-2.png",
    },
    {
        "title": "Digital Smart Tablets",
        "href": f"{BASE}/technology-hub/best-digital-smart-tablets/",
        "id": 1081,
        "src": f"{BASE}/wp-content/uploads/2026/03/Untitled-design-85.png",
    },
    {
        "title": "Interactive Digital Displays",
        "href": f"{BASE}/technology-hub/interactive-digital-displays-2/",
        "id": 5785,
        "src": f"{BASE}/wp-content/uploads/2026/06/Untitled-1000-x-1188-px-1000-x-1188-px-1900-x-1080-px.png",
    },
]

COVER_ID = 5856
COVER_SRC = TILES[0]["src"]

CSS = r'''
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600&family=Inter:wght@400;500;600&display=swap");
/* R9 — native blocks; only layout chrome in Custom HTML */
body.page-id-111 .entry-content > .alignfull {
  margin-left: 0 !important;
  margin-right: 0 !important;
  max-width: none !important;
  width: 100% !important;
}
body.page-id-111 .tc-tech-cover.wp-block-cover {
  min-height: min(72vh, 640px) !important;
  margin: 0 !important;
  padding: 0 !important;
}
body.page-id-111 .tc-tech-cover .wp-block-cover__inner-container {
  max-width: 720px;
  margin-left: clamp(1.25rem, 5vw, 4rem) !important;
  margin-right: auto !important;
  padding: clamp(3rem, 7vw, 5.5rem) 0 !important;
}
body.page-id-111 .tc-tech-cover__brand {
  margin: 0 0 1rem !important;
  font-family: Inter, sans-serif !important;
  font-size: 0.8rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.22em !important;
  text-transform: uppercase !important;
  color: #b8944b !important;
}
body.page-id-111 .tc-tech-cover .wp-block-heading {
  font-family: "Playfair Display", serif !important;
  font-size: clamp(2.4rem, 5vw, 3.6rem) !important;
  font-weight: 600 !important;
  line-height: 1.1 !important;
  color: #fff !important;
  margin: 0 0 1rem !important;
}
body.page-id-111 .tc-tech-cover p.tc-tech-cover__lead {
  max-width: 34rem;
  font-family: Inter, sans-serif !important;
  font-size: 1.05rem !important;
  line-height: 1.6 !important;
  color: rgba(255,255,255,0.92) !important;
  margin: 0 0 1.5rem !important;
}
body.page-id-111 .tc-tech-cover__cta {
  display: inline-flex !important;
  align-items: center;
  gap: 0.45rem;
  padding: 0.85rem 1.35rem !important;
  border: 1px solid rgba(255,255,255,0.55) !important;
  color: #fff !important;
  text-decoration: none !important;
  font-family: Inter, sans-serif !important;
  font-size: 0.78rem !important;
  letter-spacing: 0.16em !important;
  text-transform: uppercase !important;
  background: transparent !important;
}
body.page-id-111 .tc-tech-cover__cta:hover {
  border-color: #b8944b !important;
  background: rgba(184,148,75,0.22) !important;
}

body.page-id-111 .tc-tech-intro-prose {
  background: #f8f4ec;
  padding: clamp(2rem, 4vw, 3rem) clamp(1.25rem, 4vw, 3rem) 0.25rem;
  max-width: 1180px;
  margin: 0 auto;
}
body.page-id-111 .tc-tech-intro-prose .tc-hub-eyebrow {
  margin: 0 0 0.5rem !important;
  font-family: Inter, sans-serif !important;
  font-size: 0.78rem !important;
  letter-spacing: 0.16em !important;
  text-transform: uppercase !important;
  color: #b8944b !important;
}
body.page-id-111 .tc-tech-intro-prose .tc-hub-hero-title {
  margin: 0 0 1rem !important;
  font-family: "Playfair Display", serif !important;
  font-size: clamp(1.9rem, 3vw, 2.6rem) !important;
  font-weight: 600 !important;
  color: #1e3a5f !important;
}
body.page-id-111 .tc-tech-intro-prose .tc-hub-hero-title em {
  color: #b8944b !important;
  font-style: italic !important;
}
body.page-id-111 .tc-tech-intro-prose .tc-hub-hero-lead {
  margin: 0 0 1rem !important;
  max-width: 42rem;
  font-family: Inter, sans-serif !important;
  font-size: 1.05rem !important;
  line-height: 1.65 !important;
  color: #334155 !important;
}
body.page-id-111 .tc-tech-meta-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 0.75rem;
  margin-top: 1.25rem;
  padding: 0.85rem 0 1.25rem;
  border-top: 1px solid rgba(30,58,95,0.12);
}
body.page-id-111 .tc-tech-meta-row p {
  margin: 0 !important;
  font-family: Inter, sans-serif !important;
  font-size: 0.8rem !important;
  color: #64748b !important;
}
body.page-id-111 .tc-tech-meta-row a { color: #1e3a5f !important; }

body.page-id-111 .tc-tech-stats {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.25rem;
  padding: 1.35rem clamp(1.25rem, 4vw, 3rem);
  background: #f8f4ec;
  border-bottom: 1px solid rgba(30,58,95,0.08);
}
body.page-id-111 .tc-tech-stats__item::before {
  content: "";
  display: block;
  width: 1.5rem;
  height: 2px;
  background: #b8944b;
  margin-bottom: 0.65rem;
}
body.page-id-111 .tc-tech-stats__label {
  margin: 0;
  font-family: Inter, sans-serif;
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #b8944b;
}
body.page-id-111 .tc-tech-stats__value {
  margin: 0.35rem 0 0;
  font-family: "Playfair Display", serif;
  font-size: 1.15rem;
  color: #1e3a5f;
}
@media (max-width: 700px) {
  body.page-id-111 .tc-tech-stats { grid-template-columns: 1fr; }
}

body.page-id-111 .tc-tech-cat-section {
  background: #f8f4ec;
  padding: clamp(2.25rem, 4vw, 3.5rem) clamp(1.25rem, 4vw, 3rem) clamp(2.5rem, 5vw, 4rem);
  max-width: 1180px;
  margin: 0 auto;
}
body.page-id-111 .tc-tech-cat-section .tc-tech-cat-kicker {
  margin: 0 0 0.65rem !important;
  font-family: Inter, sans-serif !important;
  font-size: 0.75rem !important;
  letter-spacing: 0.16em !important;
  text-transform: uppercase !important;
  color: #b8944b !important;
}
body.page-id-111 .tc-tech-cat-section .tc-tech-cat-heading {
  margin: 0 0 0.75rem !important;
  font-family: "Playfair Display", serif !important;
  font-size: clamp(1.8rem, 3vw, 2.35rem) !important;
  color: #1e3a5f !important;
}
body.page-id-111 .tc-tech-cat-section .tc-tech-cat-lead {
  margin: 0 0 1.75rem !important;
  max-width: 40rem;
  font-family: Inter, sans-serif !important;
  color: #475569 !important;
  line-height: 1.6 !important;
}

/* Explore tiles: Kadence column + real wp:image (Replace works) */
body.page-id-111 .tc-tech-explore-row {
  margin: 0 0 1.35rem !important;
  max-width: none !important;
}
body.page-id-111 .tc-tech-explore-row .kt-row-column-wrap {
  gap: 1.35rem !important;
}
body.page-id-111 .tc-explore-hub {
  display: block !important;
  min-height: 300px !important;
  box-shadow: 0 8px 22px rgba(30, 58, 95, 0.10);
}
body.page-id-111 .tc-explore-hub .kt-inside-inner-col {
  min-height: 300px !important;
  position: relative !important;
  overflow: hidden !important;
}
@media (max-width: 780px) {
  body.page-id-111 .tc-explore-hub,
  body.page-id-111 .tc-explore-hub .kt-inside-inner-col { min-height: 260px !important; }
}
'''


def tile_column(uid: str, tile: dict) -> str:
    mid = tile["id"]
    return f'''<!-- wp:kadence/column {{"borderWidth":["","","",""],"uniqueID":"{uid}","kbVersion":2,"className":"tc-explore-hub"}} -->
<div class="wp-block-kadence-column kadence-column{uid} tc-explore-hub"><div class="kt-inside-inner-col"><!-- wp:image {{"lightbox":{{"enabled":false}},"id":{mid},"sizeSlug":"full","linkDestination":"custom"}} -->
<figure class="wp-block-image size-full"><a href="{tile["href"]}"><img src="{tile["src"]}" alt="{tile["title"]}" class="wp-image-{mid}"/></a></figure>
<!-- /wp:image -->

<!-- wp:heading {{"textAlign":"center","level":3}} -->
<h3 class="wp-block-heading has-text-align-center">{tile["title"]}</h3>
<!-- /wp:heading --></div></div>
<!-- /wp:kadence/column -->'''


def explore_rows() -> str:
    rows = []
    for i in range(0, 8, 2):
        left = TILES[i]
        right = TILES[i + 1]
        uid = f"111_r9row{i//2}"
        rows.append(
            f'''<!-- wp:kadence/rowlayout {{"uniqueID":"{uid}","colLayout":"equal","kbVersion":2,"className":"tc-tech-explore-row"}} -->
<div class="wp-block-kadence-rowlayout alignnone kt-row-layout-{uid} tc-tech-explore-row"><div class="kt-row-layout-inner kt-layout-inner-wrap kt-row-has-bg"><div class="kt-row-column-wrap kt-has-2-columns kt-row-layout-equal kt-tab-layout-inherit kt-mobile-layout-row kt-column-gap-default">
{tile_column(uid + "a", left)}

{tile_column(uid + "b", right)}
</div></div></div>
<!-- /wp:kadence/rowlayout -->'''
        )
    return "\n\n".join(rows)


def build_native_top() -> str:
    style = (
        "<!-- wp:html -->\n"
        "<!-- TC STAGING PATCH TECH-HUB-R9: CSS only. Images are native blocks for Media Replace. -->\n"
        f'<style id="tc-tech-hub-r9">\n{CSS.strip()}\n</style>\n'
        "<!-- /wp:html -->\n"
    )

    cover = f'''<!-- wp:cover {{"url":"{COVER_SRC}","id":{COVER_ID},"dimRatio":55,"overlayColor":"ast-global-color-4","isUserOverlayColor":true,"minHeight":640,"minHeightUnit":"px","align":"full","className":"tc-tech-cover","layout":{{"type":"constrained"}}}} -->
<div class="wp-block-cover alignfull tc-tech-cover" style="min-height:640px"><img class="wp-block-cover__image-background wp-image-{COVER_ID}" alt="Technology Hub" src="{COVER_SRC}" data-object-fit="cover"/><span aria-hidden="true" class="wp-block-cover__background has-ast-global-color-4-background-color has-background-dim-50 has-background-dim"></span><div class="wp-block-cover__inner-container"><!-- wp:paragraph {{"className":"tc-tech-cover__brand"}} -->
<p class="tc-tech-cover__brand">Truth Collective</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":1}} -->
<h1 class="wp-block-heading">Technology Hub</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"className":"tc-tech-cover__lead"}} -->
<p class="tc-tech-cover__lead">The largest of Truth Collective's six hubs. Digital products that shape how people work, create, and live, reviewed before they earn a place here.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a class="tc-tech-cover__cta" href="#tc-tech-categories">Explore the categories ›</a></p>
<!-- /wp:paragraph --></div></div>
<!-- /wp:cover -->
'''

    intro = '''<!-- wp:group {"className":"tc-tech-intro-prose","layout":{"type":"constrained"}} -->
<div class="wp-block-group tc-tech-intro-prose"><!-- wp:paragraph {"className":"tc-hub-eyebrow"} -->
<p class="tc-hub-eyebrow">Welcome to the</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"className":"tc-hub-hero-title"} -->
<h2 class="wp-block-heading tc-hub-hero-title">Technology <em>Hub</em></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"className":"tc-hub-hero-lead"} -->
<p class="tc-hub-hero-lead">The Technology Hub is the largest of Truth Collective's six hubs. It brings together the digital products that shape how people work, create, and live, from computers and displays to the tools just now reaching everyday use. Every category below has been reviewed and graded against the Truth Collective Trusted Selection Standards before it earns a place here.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"className":"tc-hub-hero-lead"} -->
<p class="tc-hub-hero-lead">Each category leads to a dedicated page where the top products are ranked, graded, and explained in full. A closing section looks at the technologies still ahead, framed as what is worth watching, not as speculation.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"className":"tc-tech-meta-row","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group tc-tech-meta-row"><!-- wp:paragraph -->
<p>By Truth Collective Editorial · Updated 2026</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://tcstaging.truth-collective.com/product-selection-standards/">Reviewed against our Trusted Selection Standards →</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
'''

    stats = '''<!-- wp:html -->
<div class="tc-tech-stats" aria-label="Technology Hub highlights">
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Reviewed and Graded</p>
    <p class="tc-tech-stats__value">Trusted Selection Standards</p>
  </div>
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Six Total Hubs</p>
    <p class="tc-tech-stats__value">Largest of the collection</p>
  </div>
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Always Current</p>
    <p class="tc-tech-stats__value">Continuously updated</p>
  </div>
</div>
<!-- /wp:html -->
'''

    cat_head = '''<!-- wp:group {"className":"tc-tech-cat-section","layout":{"type":"constrained"}} -->
<div id="tc-tech-categories" class="wp-block-group tc-tech-cat-section"><!-- wp:paragraph {"className":"tc-tech-cat-kicker"} -->
<p class="tc-tech-cat-kicker">Browse by category</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"className":"tc-tech-cat-heading"} -->
<h2 class="wp-block-heading tc-tech-cat-heading">Technology Hub Categories</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"className":"tc-tech-cat-lead"} -->
<p class="tc-tech-cat-lead">Eight paths. Each one reviewed against the Truth Collective Trusted Selection Standards before it earns a place here.</p>
<!-- /wp:paragraph -->
'''

    cat_close = "</div>\n<!-- /wp:group -->\n"

    return "\n".join([style, cover, intro, stats, cat_head, explore_rows(), cat_close])


def replace_top(raw: str, native: str) -> str:
    # From first TECH-HUB patch / cover / r8 style through end of category section, before Final Thoughts
    start = None
    for marker in (
        "<!-- TC STAGING PATCH TECH-HUB",
        '<style id="tc-tech-hub-',
        "tc-tech-cover",
        "tc-tech-intro-prose",
    ):
        i = raw.find(marker)
        if i == -1:
            continue
        # Prefer enclosing wp:html for style patches; otherwise nearest block comment.
        j = raw.rfind("<!-- wp:html -->", 0, i)
        k = raw.rfind("<!-- wp:", 0, i)
        if marker.startswith("<!-- TC") or marker.startswith("<style"):
            start = j if j != -1 else (k if k != -1 else i)
        else:
            start = k if k != -1 else i
        break
    if start is None:
        raise SystemExit("could not find top stack start")

    ft = raw.find(">Final Thoughts<")
    if ft == -1:
        ft = raw.find("Final Thoughts")
    if ft == -1:
        raise SystemExit("Final Thoughts missing")
    # walk back to block comment before Final Thoughts heading
    heading = raw.rfind("<!-- wp:heading", 0, ft)
    if heading == -1:
        raise SystemExit("heading before Final Thoughts missing")
    end = heading
    while end > 0 and raw[end - 1] in "\n\r\t ":
        end -= 1

    return raw[:start] + native + "\n\n" + raw[end:]


def main() -> None:
    user = os.environ["TC_WP_USER"].strip()
    pw = os.environ["TC_WP_APP_PASSWORD"].strip()
    auth = base64.b64encode(f"{user}:{pw}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "User-Agent": "TC-REST-R9",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    ctx = ssl.create_default_context()

    def api(method: str, path: str, body: dict | None = None):
        data = None if body is None else json.dumps(body).encode()
        req = urllib.request.Request(BASE + path, data=data, headers=headers, method=method)
        with urllib.request.urlopen(req, context=ctx, timeout=120) as r:
            return json.load(r)

    page = api("GET", f"/wp-json/wp/v2/pages/{PAGE_ID}?context=edit&_fields=id,content")
    raw = page["content"]["raw"]
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup = BACKUP_DIR / f"page-{PAGE_ID}-before-REST-hub-technology-R9-{date.today().isoformat()}.html"
    backup.write_text(raw, encoding="utf-8")
    print("backup", backup)

    native = build_native_top()
    Path(ROOT / "diagnostics/scaffolds/REST-hub-technology-R9-native-top.html").write_text(
        native, encoding="utf-8"
    )
    new_raw = replace_top(raw, native)

    for must in ("wp:cover", "wp-image-", "tc-explore-hub", "Welcome to the", "Final Thoughts"):
        if must not in new_raw:
            raise SystemExit(f"missing {must}")
    if new_raw.count("wp-image-") < 9:
        raise SystemExit(f"expected >=9 wp-image classes, got {new_raw.count('wp-image-')}")
    # ensure not stuck with only html img grid
    if 'class="tc-tech-explore-grid"' in new_raw:
        raise SystemExit("old html explore grid still present")

    updated = api("POST", f"/wp-json/wp/v2/pages/{PAGE_ID}", {"content": new_raw})
    print("updated", updated["id"])
    print("view", f"{BASE}/technology-hub/")
    print("Editor: click each tile/cover image → Replace. Upload 1600x1000.")


if __name__ == "__main__":
    main()
