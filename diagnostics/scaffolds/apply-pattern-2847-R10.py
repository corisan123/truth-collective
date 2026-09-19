#!/usr/bin/env python3
"""Apply Selection Standards R10 (Claude SPEC) to pattern 2847 and sync 8152/8156."""
from __future__ import annotations

import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = "https://tcstaging.truth-collective.com"
ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = Path(__file__).with_name("pattern-2847-selection-standards-R10.html")
BACKUP_DIR = ROOT / "backups"
IDS = (2847, 8152, 8156)


def main() -> int:
    user = os.environ.get("TC_WP_USER")
    password = os.environ.get("TC_WP_APP_PASSWORD")
    if not user or not password:
        print("Missing TC_WP_USER / TC_WP_APP_PASSWORD", file=sys.stderr)
        return 1

    content = SCAFFOLD.read_text(encoding="utf-8")
    if "style=\"display:flex" in content or "style='display:flex" in content:
        print("Scaffold still contains inline display:flex", file=sys.stderr)
        return 1

    auth = (user, password)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for block_id in IDS:
        url = f"{BASE}/wp-json/wp/v2/blocks/{block_id}"
        before = requests.get(url, auth=auth, params={"context": "edit"}, timeout=60)
        before.raise_for_status()
        raw = before.json().get("content", {}).get("raw") or ""
        backup = BACKUP_DIR / f"pattern-{block_id}-before-R10-{stamp}.html"
        backup.write_text(raw, encoding="utf-8")
        print(f"backup {backup} ({len(raw)} chars)")

        payload = {"content": content}
        # Keep titles; only sync body markup
        resp = requests.post(url, auth=auth, json=payload, timeout=90)
        if not resp.ok:
            print(f"FAIL {block_id}: {resp.status_code} {resp.text[:400]}", file=sys.stderr)
            return 1
        after = resp.json().get("content", {}).get("raw") or ""
        checks = {
            "no_navy_banner": "tc-standards-pattern__banner" not in after,
            "has_num": "tc-standards-pattern__num" in after,
            "has_quote": "tc-standards-pattern__quote" in after,
            "no_inline_flex": 'style="display:flex' not in after,
            "has_stages": "tc-standards-pattern__stages" in after,
        }
        print(f"updated {block_id} len={len(after)} checks={checks}")
        if not all(checks.values()):
            print("Post-apply checks failed", file=sys.stderr)
            return 1

    print("OK R10 applied to", IDS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
