#!/usr/bin/env python3
"""Inject approved hub evaluation briefs via WP REST on staging.

Ticket: REST-hub-eval-briefs-v1
Auth: TC_WP_USER + TC_WP_APP_PASSWORD
Site: https://tcstaging.truth-collective.com

Safe order per page: GET → backup raw → splice Custom HTML below intro /
above category grid → POST → confirm marker present.
Also wraps unlinked Technology Hub tiles for Audio and Video (117) and
Desk Speakers (1449).
"""
from __future__ import annotations

import base64
import json
import os
import ssl
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

BASE = os.environ.get("STAGING", "https://tcstaging.truth-collective.com").rstrip("/")
ROOT = Path(__file__).resolve().parents[3]
BACKUP_DIR = ROOT / "diagnostics" / "backups"
BRIEF_DIR = Path(__file__).resolve().parent
TICKET = "REST-hub-eval-briefs-v1"
BINDER = f"{BASE}/6751-2/"
MARKER = "TC EVALUATION STANDARDS"
INSERT_BEFORE = '<!-- wp:group {"className":"tc-tech-cat-section"'
TODAY = date.today().isoformat()

HUBS = [
    (111, "technology-hub.html", "Technology Hub"),
    (115, "smart-lighting.html", "Smart Lighting"),
    (5680, "productivity-tools.html", "Productivity Tools"),
    (5939, "office-workspace.html", "Office Workspace"),
    (86, "self-help.html", "Self-Help and Mental Wellness"),
    (38, "recommended-books.html", "Recommended Books"),
]


def die(msg: str, code: int = 1) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)


def client():
    user = os.environ.get("TC_WP_USER", "").strip()
    pw = os.environ.get("TC_WP_APP_PASSWORD", "").strip()
    if not user or not pw:
        die("Set TC_WP_USER and TC_WP_APP_PASSWORD.")
    ctx = ssl.create_default_context()
    auth = base64.b64encode(f"{user}:{pw}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "User-Agent": "TC-REST-hub-eval-briefs-v1",
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


def wrap_block(html: str) -> str:
    return (
        "<!-- wp:html -->\n"
        f"{html.rstrip()}\n"
        "<!-- /wp:html -->\n\n"
    )


def fix_tech_tile_links(raw: str) -> str:
    """Add missing hrefs on Audio and Video + Desk Speakers tiles."""
    replacements = [
        (
            '<figure class="wp-block-image size-full"><img src="https://tcstaging.truth-collective.com/wp-content/uploads/2026/08/Untitled-1600-x-1000-px-1.png" alt="" class="wp-image-8315"/></figure>',
            '<figure class="wp-block-image size-full"><a href="https://tcstaging.truth-collective.com/technology-hub/audio-and-video/"><img src="https://tcstaging.truth-collective.com/wp-content/uploads/2026/08/Untitled-1600-x-1000-px-1.png" alt="Audio and Video" class="wp-image-8315"/></a></figure>',
        ),
        (
            '<figure class="wp-block-image size-full"><img src="https://tcstaging.truth-collective.com/wp-content/uploads/2026/08/Desk-Speakers.png" alt="" class="wp-image-8317"/></figure>',
            '<figure class="wp-block-image size-full"><a href="https://tcstaging.truth-collective.com/technology-hub/speakers-home-office-outdoors/"><img src="https://tcstaging.truth-collective.com/wp-content/uploads/2026/08/Desk-Speakers.png" alt="Desk Speakers" class="wp-image-8317"/></a></figure>',
        ),
    ]
    for old, new in replacements:
        if old not in raw:
            print(f"  WARN tile pattern not found exactly; leaving that tile unchanged")
            continue
        raw = raw.replace(old, new, 1)
        print(f"  linked tile")
    return raw


def splice_brief(raw: str, block: str, page_id: int) -> str:
    if MARKER in raw:
        print(f"  brief already present on {page_id}; skip splice")
        return raw
    idx = raw.find(INSERT_BEFORE)
    if idx < 0:
        die(f"page {page_id}: insertion marker tc-tech-cat-section not found")
    return raw[:idx] + block + raw[idx:]


def homepage_block() -> str:
    return wrap_block(
        (BRIEF_DIR / "homepage.html").read_text(encoding="utf-8").replace("BINDER_VIEWER_URL", BINDER)
    )


def main() -> None:
    ctx, headers = client()
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    results = []

    for page_id, fname, label in HUBS:
        print(f"\n=== {label} ({page_id}) ===")
        status, page = api("GET", f"/wp-json/wp/v2/pages/{page_id}?context=edit", headers, ctx)
        raw = page["content"]["raw"]
        backup = BACKUP_DIR / f"page-{page_id}-before-{TICKET}-{TODAY}.html"
        backup.write_text(raw, encoding="utf-8")
        print(f"  backup {backup.name} ({len(raw)} chars)")

        html = (BRIEF_DIR / fname).read_text(encoding="utf-8").replace("BINDER_VIEWER_URL", BINDER)
        new_raw = splice_brief(raw, wrap_block(html), page_id)
        if page_id == 111:
            new_raw = fix_tech_tile_links(new_raw)

        if new_raw == raw:
            print("  no content change")
            results.append((page_id, label, "unchanged", page.get("link")))
            continue

        post_status, updated = api(
            "POST",
            f"/wp-json/wp/v2/pages/{page_id}",
            headers,
            ctx,
            {"content": new_raw},
        )
        confirm = updated["content"]["raw"]
        ok = MARKER in confirm
        audio_ok = True
        if page_id == 111:
            audio_ok = "/technology-hub/audio-and-video/" in confirm and "/technology-hub/speakers-home-office-outdoors/" in confirm
        print(f"  POST {post_status} marker={ok} tiles={audio_ok} new_len={len(confirm)}")
        if not ok:
            die(f"page {page_id}: marker missing after POST")
        results.append((page_id, label, "patched", updated.get("link")))

    print("\n=== Homepage (5) ===")
    status, page = api("GET", "/wp-json/wp/v2/pages/5?context=edit", headers, ctx)
    raw = page["content"]["raw"]
    backup = BACKUP_DIR / f"page-5-before-{TICKET}-{TODAY}.html"
    backup.write_text(raw, encoding="utf-8")
    print(f"  backup {backup.name} ({len(raw)} chars)")
    if MARKER in raw:
        print("  brief already present; skip")
        results.append((5, "Homepage", "unchanged", page.get("link")))
    else:
        new_raw = raw.rstrip() + "\n\n" + homepage_block()
        post_status, updated = api("POST", "/wp-json/wp/v2/pages/5", headers, ctx, {"content": new_raw})
        confirm = updated["content"]["raw"]
        ok = MARKER in confirm
        print(f"  POST {post_status} marker={ok} new_len={len(confirm)}")
        if not ok:
            die("homepage: marker missing after POST")
        results.append((5, "Homepage", "patched", updated.get("link")))

    print("\nDONE")
    for row in results:
        print(f"  {row[0]:5} {row[2]:10} {row[1]} {row[3]}")


if __name__ == "__main__":
    main()
