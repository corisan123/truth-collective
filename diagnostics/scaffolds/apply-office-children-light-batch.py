#!/usr/bin/env python3
"""Apply Office children light scaffolds. Requires TC_WP_USER / TC_WP_APP_PASSWORD."""
import base64, json, os, sys, urllib.request
from pathlib import Path
BASE = "https://tcstaging.truth-collective.com"
ROOT = Path(__file__).resolve().parent
PAGES = [
    (119, "REST-page-119-executive-chairs-light.html", "Executive Office Chairs and Seating"),
    (113, "REST-page-113-executive-desks-light.html", "Executive Style Desks and Setup"),
    (1165, "REST-page-1165-analog-writing-light.html", "Best Analog Writing Tools"),
    (425, "REST-page-425-desk-essentials-light.html", "Office Desk Essential Products | 2026"),
    (423, "REST-page-423-laptop-stands-light.html", "Laptop Stands and Accessories"),
    (6482, "REST-page-6482-file-cabinets-light.html", "Office File Cabinets, Credenzas, and Filing Essentials"),
]
user = os.environ.get("TC_WP_USER", "").strip()
pw = os.environ.get("TC_WP_APP_PASSWORD", "").strip()
if not user or not pw:
    sys.exit("Set TC_WP_USER and TC_WP_APP_PASSWORD")
auth = base64.b64encode(f"{user}:{pw}".encode()).decode()
HDR = {"Authorization": f"Basic {auth}", "User-Agent": "Mozilla/5.0 (compatible; TruthCollectiveBot/1.0)", "Accept": "application/json", "Content-Type": "application/json"}
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
    before = api("GET", f"/wp-json/wp/v2/pages/{pid}?context=edit")
    (backup_dir / f"page-{pid}-before-office-light-2026-08-19.html").write_text(before["content"]["raw"])
    updated = api("POST", f"/wp-json/wp/v2/pages/{pid}", {"content": (ROOT / fname).read_text(), "title": title, "meta": {"site-post-title": "disabled"}})
    print(f"OK {pid} title={updated['title']['raw']!r} len={len(updated['content']['raw'])} mod={updated.get('modified')}")
