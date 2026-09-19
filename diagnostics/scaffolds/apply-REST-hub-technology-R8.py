#!/usr/bin/env python3
"""Apply REST-hub-technology-R8: cover hero + tc-explore-hub grid on page 111."""
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
SCAFFOLD = Path(__file__).with_name("REST-hub-technology-R8-explore.html")
BACKUP_DIR = ROOT / "diagnostics" / "backups"
TICKET = "REST-hub-technology-R8"


def die(msg: str, code: int = 1) -> None:
    raise SystemExit(f"ERROR: {msg}")


def client():
    user = os.environ.get("TC_WP_USER", "").strip()
    pw = os.environ.get("TC_WP_APP_PASSWORD", "").strip()
    if not user or not pw:
        die("Set TC_WP_USER and TC_WP_APP_PASSWORD")
    ctx = ssl.create_default_context()
    auth = base64.b64encode(f"{user}:{pw}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "User-Agent": "TC-REST-hub-technology-R8",
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


def replace_top_custom_blocks(raw: str, scaffold: str) -> str:
    """Replace R2–R7 custom HTML stack (style/hero/stats/grid/script) with R8."""
    new_block = "<!-- wp:html -->\n" + scaffold.strip() + "\n<!-- /wp:html -->\n"

    # Cut from first TECH-HUB cream/r style marker through reveal script block,
    # or from first tc-tech-hero / tc-tech-cover through categories + script.
    patterns = [
        # Full R7 stack: style html + stats + cat + script (four consecutive wp:html)
        r"(?:<!-- wp:html -->\s*)?<!-- TC STAGING PATCH TECH-HUB[\s\S]*?<!-- /wp:html -->\s*"
        r"(?:<!-- wp:html -->[\s\S]*?<!-- /wp:html -->\s*){0,4}",
        # Fallback: from style id through reveal script
        r"<!-- wp:html -->\s*<style id=\"tc-tech-hub-cream-r[0-9]\"[\s\S]*?"
        r"<script id=\"tc-tech-hub-reveal-r[0-9]\"[\s\S]*?</script>\s*<!-- /wp:html -->\s*",
        # Fallback: cover/hero through explore grid script in one block already
        r"<!-- wp:html -->\s*<!-- TC STAGING PATCH TECH-HUB-R8:[\s\S]*?<!-- /wp:html -->\s*",
    ]

    # More reliable: find start of first tc-tech style/hero patch and end after reveal script
    start = None
    for marker in (
        "<!-- TC STAGING PATCH TECH-HUB",
        '<style id="tc-tech-hub-cream-',
        '<style id="tc-tech-hub-r8"',
        'class="tc-tech-hero-shell',
        'class="tc-tech-cover',
    ):
        i = raw.find(marker)
        if i != -1:
            # walk back to enclosing <!-- wp:html -->
            j = raw.rfind("<!-- wp:html -->", 0, i)
            start = j if j != -1 else i
            break
    if start is None:
        die("Could not find Tech Hub custom top stack to replace")

    end = None
    for marker in (
        '<script id="tc-tech-hub-reveal-r8">',
        '<script id="tc-tech-hub-reveal-r7">',
        '<script id="tc-tech-hub-reveal',
    ):
        k = raw.find(marker, start)
        if k != -1:
            close = raw.find("<!-- /wp:html -->", k)
            if close == -1:
                die("Reveal script found but no closing wp:html")
            end = close + len("<!-- /wp:html -->")
            break

    if end is None:
        # replace consecutive wp:html blocks from start until Final Thoughts
        ft = raw.find("Final Thoughts", start)
        if ft == -1:
            die("No Final Thoughts anchor")
        # end at last <!-- /wp:html --> before Final Thoughts
        segment = raw[start:ft]
        closes = [m.end() for m in re.finditer(r"<!-- /wp:html -->", segment)]
        if not closes:
            die("No wp:html closes before Final Thoughts")
        end = start + closes[-1]

    # Also eat whitespace after
    while end < len(raw) and raw[end] in "\n\r\t ":
        end += 1

    return raw[:start] + new_block + "\n" + raw[end:]


def lighten_final_thoughts(raw: str) -> str:
    """Keep Final Thoughts copy; strip heavy bordered Truth Collective group if present right after."""
    # Optional: leave patterns for now — only normalize Final Thoughts heading color if needed.
    return raw


def main() -> None:
    if not SCAFFOLD.exists():
        die(f"Missing scaffold {SCAFFOLD}")
    scaffold = SCAFFOLD.read_text(encoding="utf-8")
    ctx, headers = client()
    _, page = api(
        "GET",
        f"/wp-json/wp/v2/pages/{PAGE_ID}?context=edit&_fields=id,content,title,status",
        headers,
        ctx,
    )
    raw = page["content"]["raw"]
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = date.today().isoformat()
    backup = BACKUP_DIR / f"page-{PAGE_ID}-before-{TICKET}-{stamp}.html"
    backup.write_text(raw, encoding="utf-8")
    print(f"Backup: {backup}")

    new_raw = replace_top_custom_blocks(raw, scaffold)
    new_raw = lighten_final_thoughts(new_raw)

    if "tc-explore-hub" not in new_raw:
        die("R8 apply failed: no tc-explore-hub in result")
    if new_raw.count("tc-explore-hub") < 8:
        die(f"Expected ≥8 explore hubs, found {new_raw.count('tc-explore-hub')}")
    if "tc-tech-cover" not in new_raw:
        die("R8 apply failed: no cover hero")
    if "tc-tech-cat-tile" in new_raw:
        die("Old tc-tech-cat-tile still present")

    status, updated = api(
        "POST",
        f"/wp-json/wp/v2/pages/{PAGE_ID}",
        headers,
        ctx,
        {"content": new_raw},
    )
    print(f"POST status {status}; page {updated.get('id')} updated")
    print(f"View: {BASE}/technology-hub/")


if __name__ == "__main__":
    main()
