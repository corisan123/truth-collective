#!/usr/bin/env python3
"""Apply Computers light rebuild to staging page 359."""
import base64, json, os, sys, urllib.request
from pathlib import Path

BASE = "https://tcstaging.truth-collective.com"
PAGE_ID = 359
SCAFFOLD = Path(__file__).with_name("REST-page-359-computers-light.html")
BACKUP = Path(__file__).resolve().parents[1] / "backups" / "page-359-before-computers-light-2026-08-19.html"

def die(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

user = os.environ.get("TC_WP_USER", "").strip()
pw = os.environ.get("TC_WP_APP_PASSWORD", "").strip()
if not user or not pw:
    die("Set TC_WP_USER and TC_WP_APP_PASSWORD")

auth = base64.b64encode(f"{user}:{pw}".encode()).decode()
HDR = {
    "Authorization": f"Basic {auth}",
    "User-Agent": "Mozilla/5.0 (compatible; TruthCollectiveBot/1.0)",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

def api(method, path, data=None):
    body = None if data is None else json.dumps(data).encode()
    req = urllib.request.Request(f"{BASE}{path}", data=body, headers=HDR, method=method)
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)

content = SCAFFOLD.read_text()
before = api("GET", f"/wp-json/wp/v2/pages/{PAGE_ID}?context=edit")
BACKUP.parent.mkdir(parents=True, exist_ok=True)
BACKUP.write_text(before["content"]["raw"])
print(f"Backup wrote {BACKUP} ({len(before['content']['raw'])} chars)")
updated = api("POST", f"/wp-json/wp/v2/pages/{PAGE_ID}", {"content": content})
print(f"Applied page {PAGE_ID} len={len(updated['content']['raw'])} modified={updated.get('modified')}")
print(f"Public: {BASE}/technology-hub/computers-digital-devices/")
