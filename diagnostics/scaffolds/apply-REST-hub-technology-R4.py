#!/usr/bin/env python3
"""Apply REST-hub-technology-R4 to staging Technology Hub (page 111).

Requires env:
  TC_WP_USER  — usually dreid1253@yahoo.com
  TC_WP_APP_PASSWORD — WordPress Application Password (spaces OK)

Safe order: backup raw → upgrade page-scoped CSS R3→R4 → replace Categories
section through the block before Final Thoughts → POST.
"""
from __future__ import annotations

import base64
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

PAGE_ID = 111
BASE = os.environ.get("STAGING", "https://tcstaging.truth-collective.com").rstrip("/")
ROOT = Path(__file__).resolve().parents[2]
SCAFFOLD = Path(__file__).with_name("REST-hub-technology-R4-category-grid.html")
CSS_FILE = Path(__file__).with_name("REST-hub-technology-R4.css")
BACKUP_DIR = ROOT / "diagnostics" / "backups"
TICKET = "REST-hub-technology-R4"


def die(msg: str, code: int = 1) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)


def client():
    user = os.environ.get("TC_WP_USER", "").strip()
    pw = os.environ.get("TC_WP_APP_PASSWORD", "").strip()
    if not user or not pw:
        die("Set TC_WP_USER and TC_WP_APP_PASSWORD in the environment.")
    ctx = ssl.create_default_context()
    auth = base64.b64encode(f"{user}:{pw}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "User-Agent": "TC-REST-hub-technology-R4",
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
        detail = e.read().decode("utf-8", "replace")[:500]
        die(f"HTTP {e.code} {method} {path}: {detail}")


def upgrade_css_block(raw: str, css: str) -> str:
    """Replace R2/R3 page-scoped style with R4, or insert after first html block."""
    style = (
        "<!-- wp:html -->\n"
        "<!-- TC STAGING PATCH TECH-HUB-CREAM-R4: cream hero + 3-col category grid; "
        "migrate style to Additional CSS later -->\n"
        f'<style id="tc-tech-hub-cream-r4">\n{css.rstrip()}\n</style>\n'
        "<!-- /wp:html -->\n"
    )
    patterns = [
        r"<!-- wp:html -->\s*<!-- TC STAGING PATCH TECH-HUB-CREAM-R[23]:.*?<!-- /wp:html -->\s*",
        r"<!-- wp:html -->\s*<style id=\"tc-tech-hub-cream-r[23]\"[^>]*>.*?</style>\s*<!-- /wp:html -->\s*",
    ]
    for pat in patterns:
        new_raw, n = re.subn(pat, style + "\n", raw, count=1, flags=re.S)
        if n:
            return new_raw
    # Fallback: prepend after any leading image block
    return style + "\n" + raw


def replace_categories(raw: str, section_html: str) -> str:
    """
    Replace from Technology Hub Categories heading through just before Final Thoughts.
    Prefer block comments / headings present in staging raw.
    """
    # Strip CSS from scaffold if present — CSS is applied via upgrade_css_block
    section_only = re.sub(
        r"<!-- wp:html -->\s*<!-- TC STAGING PATCH TECH-HUB-CREAM-R4:.*?<!-- /wp:html -->\s*",
        "",
        section_html,
        count=1,
        flags=re.S,
    ).strip()
    if "tc-tech-cat-section" not in section_only:
        # scaffold is a single html block including style — rebuild section-only
        m = re.search(
            r"(<section class=\"tc-tech-cat-section\".*?</section>)",
            section_html,
            flags=re.S,
        )
        if not m:
            die("Scaffold missing tc-tech-cat-section")
        section_only = (
            "<!-- wp:html -->\n" + m.group(1) + "\n<!-- /wp:html -->"
        )
    else:
        if not section_only.startswith("<!-- wp:html"):
            section_only = "<!-- wp:html -->\n" + section_only + "\n<!-- /wp:html -->"

    start_pat = re.compile(
        r"(?:<!-- wp:heading[^>]*-->\s*)?<h2[^>]*>\s*Technology Hub Categories\s*</h2>",
        re.I,
    )
    end_pat = re.compile(
        r"(?:<!-- wp:heading[^>]*-->\s*)?<h2[^>]*>\s*Final Thoughts\s*</h2>",
        re.I,
    )
    sm = start_pat.search(raw)
    em = end_pat.search(raw)
    if not sm or not em or em.start() <= sm.start():
        die(
            "Could not find Categories→Final Thoughts markers in raw content. "
            "Aborting (no guess edits)."
        )

    # Extend start backward to include the heading's opening block comment if present
    start = sm.start()
    back = raw.rfind("<!-- wp:", 0, start)
    if back != -1 and start - back < 200:
        start = back

    # Keep Final Thoughts heading; insert section before it
    end = em.start()
    back = raw.rfind("<!-- wp:", 0, end)
    if back != -1 and end - back < 200 and back > start:
        end = back

    return raw[:start] + section_only + "\n\n" + raw[end:]


def main() -> None:
    ctx, headers = client()
    status, me = api("GET", "/wp-json/wp/v2/users/me", headers, ctx)
    print(f"Auth OK as {me.get('name')} ({me.get('slug')})")

    status, page = api(
        "GET", f"/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", headers, ctx
    )
    raw = page["content"]["raw"]
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = date.today().isoformat()
    backup = BACKUP_DIR / f"page-111-before-{TICKET}-{stamp}.html"
    backup.write_text(raw)
    print(f"Backup: {backup} ({len(raw)} chars)")

    css = CSS_FILE.read_text()
    section = SCAFFOLD.read_text()
    new_raw = upgrade_css_block(raw, css)
    # Remove duplicate R4 style if scaffold insert path also left an old R3
    new_raw = re.sub(
        r"<!-- wp:html -->\s*<!-- TC STAGING PATCH TECH-HUB-CREAM-R[23]:.*?<!-- /wp:html -->\s*",
        "",
        new_raw,
        flags=re.S,
    )
    # Ensure one R4 style exists
    if 'id="tc-tech-hub-cream-r4"' not in new_raw:
        new_raw = upgrade_css_block(new_raw, css)
    new_raw = replace_categories(new_raw, section)

    if new_raw == raw:
        die("No changes produced.")

    status, updated = api(
        "POST",
        f"/wp-json/wp/v2/pages/{PAGE_ID}",
        headers,
        ctx,
        {"content": new_raw},
    )
    print(f"Applied {TICKET}. HTTP {status}. View: {BASE}/technology-hub/")
    print("Hard-refresh and confirm: 3-col cream grid of 8 real children under the hero.")


if __name__ == "__main__":
    main()
