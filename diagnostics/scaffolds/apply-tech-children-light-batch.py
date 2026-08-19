#!/usr/bin/env python3
"""Apply Computers + Technology Hub children light scaffolds. Requires TC_WP_USER / TC_WP_APP_PASSWORD."""
import base64, json, os, sys, urllib.request
from pathlib import Path

BASE = "https://tcstaging.truth-collective.com"
ROOT = Path(__file__).resolve().parent
PAGES = [
    (359, "REST-page-359-computers-light.html"),
    (121, "REST-page-121-monitors-light.html"),
    (117, "REST-page-117-audio-video-light.html"),
    (1420, "REST-page-1420-headphones-light.html"),
    (1449, "REST-page-1449-speakers-light.html"),
    (5940, "REST-page-5940-projectors-mics-light.html"),
    (1098, "REST-page-1098-tablets-light.html"),
    (5784, "REST-page-5784-interactive-displays-light.html"),
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
for pid, fname in PAGES:
    if only and pid not in only:
        continue
    scaffold = ROOT / fname
    before = api("GET", f"/wp-json/wp/v2/pages/{pid}?context=edit")
    (backup_dir / f"page-{pid}-before-tech-light-2026-08-19.html").write_text(before["content"]["raw"])
    updated = api("POST", f"/wp-json/wp/v2/pages/{pid}", {"content": scaffold.read_text()})
    print(f"OK {pid} len={len(updated['content']['raw'])} mod={updated.get('modified')}")
