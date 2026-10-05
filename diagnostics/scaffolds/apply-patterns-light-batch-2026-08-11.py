#!/usr/bin/env python3
"""Apply light facelifts to Why TC, intro, social, Truth Untold patterns."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import requests

BASE = "https://tcstaging.truth-collective.com"
HERE = Path(__file__).resolve().parent
BACKUP = HERE.parent / "backups"

TARGETS = [
    (5545, "pattern-5545-why-tc-light.html", ("tc-why", "Why Truth Collective")),
    (7648, "pattern-7648-truth-collective-light.html", ("tc-intro", "Leadership Collection")),
    (7532, "pattern-7532-social-light.html", ("tc-social", "https://x.com/collective_07")),
    (7672, "pattern-7532-social-light.html", ("tc-social", "Medium")),
    (7827, "pattern-7827-truth-untold-light.html", ("tc-untold", "Truth Untold Series")),
]


def main() -> int:
    user = os.environ.get("TC_WP_USER")
    password = os.environ.get("TC_WP_APP_PASSWORD")
    if not user or not password:
        print("Missing TC_WP_USER / TC_WP_APP_PASSWORD", file=sys.stderr)
        return 1
    auth = (user, password)
    BACKUP.mkdir(parents=True, exist_ok=True)

    for block_id, scaffold_name, checks in TARGETS:
        scaffold = HERE / scaffold_name
        content = scaffold.read_text(encoding="utf-8")
        if 'style="display:flex' in content:
            print(f"inline flex in {scaffold_name}", file=sys.stderr)
            return 1
        url = f"{BASE}/wp-json/wp/v2/blocks/{block_id}"
        before = requests.get(url, auth=auth, params={"context": "edit"}, timeout=60)
        before.raise_for_status()
        raw = before.json().get("content", {}).get("raw") or ""
        # keep first pre-light backup if already written
        backup = BACKUP / f"pattern-{block_id}-before-light-2026-08-11.html"
        if not backup.exists():
            backup.write_text(raw, encoding="utf-8")
            print(f"backup {backup.name} ({len(raw)})")
        else:
            print(f"backup exists {backup.name}")

        resp = requests.post(url, auth=auth, json={"content": content}, timeout=90)
        if not resp.ok:
            print(f"FAIL {block_id}: {resp.status_code} {resp.text[:300]}", file=sys.stderr)
            return 1
        after = resp.json().get("content", {}).get("raw") or ""
        ok = all(token in after for token in checks)
        print(f"updated {block_id} len={len(after)} checks_ok={ok} tokens={checks}")
        if not ok:
            return 1
        if 'style="display:flex' in after:
            print(f"inline flex remained in {block_id}", file=sys.stderr)
            return 1

    print("OK light batch applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
