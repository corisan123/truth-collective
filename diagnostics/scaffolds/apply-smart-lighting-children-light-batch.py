#!/usr/bin/env python3
"""Apply Smart Lighting children light scaffolds. Requires TC_WP_USER / TC_WP_APP_PASSWORD."""
import base64, json, os, sys, urllib.request
from pathlib import Path

BASE = "https://tcstaging.truth-collective.com"
ROOT = Path(__file__).resolve().parent
PAGES = [
    (4863, "REST-page-4863-smart-bulbs-light.html", "Smart Bulbs and Light Strips"),
    (4877, "REST-page-4877-smart-ai-lighting-light.html", "Smart AI Lighting and Rechargeable Devices"),
    (4896, "REST-page-4896-smart-lighting-controls-light.html", "Smart Lighting Controls"),
    (5099, "REST-page-5099-smart-security-lighting-light.html", "Smart Security Lighting and Cameras"),
    (4886, "REST-page-4886-advanced-lighting-light.html", "Advanced Lighting for Indoors and Outdoors | 2026"),
]

user = os.environ.get("TC_WP_USER", "").strip()
pw = os.environ.get("TC_WP_APP_PASSWORD", "").strip()
if not user or not pw:
    sys.exit("Set TC_WP_USER and TC_WP_APP_PASSWORD")

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

backup_dir = ROOT.parent / "backups"
backup_dir.mkdir(parents=True, exist_ok=True)
only = set(int(x) for x in sys.argv[1:]) if len(sys.argv) > 1 else None
for pid, fname, title in PAGES:
    if only and pid not in only:
        continue
    scaffold = ROOT / fname
    before = api("GET", f"/wp-json/wp/v2/pages/{pid}?context=edit")
    (backup_dir / f"page-{pid}-before-lighting-light-2026-08-19.html").write_text(before["content"]["raw"])
    payload = {
        "content": scaffold.read_text(),
        "title": title,
        "meta": {"site-post-title": "disabled"},
    }
    updated = api("POST", f"/wp-json/wp/v2/pages/{pid}", payload)
    print(f"OK {pid} title={updated['title']['raw']!r} len={len(updated['content']['raw'])} mod={updated.get('modified')}")
