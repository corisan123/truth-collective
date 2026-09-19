#!/usr/bin/env python3
"""R8b: restore Claude Welcome prose under cover; keep explore-hub grid."""
from __future__ import annotations

import base64
import json
import os
import ssl
import urllib.request
from datetime import date
from pathlib import Path

PAGE_ID = 111
BASE = os.environ.get("STAGING", "https://tcstaging.truth-collective.com").rstrip("/")
ROOT = Path(__file__).resolve().parents[2]
BACKUP_DIR = ROOT / "diagnostics" / "backups"

INTRO_CSS = """
/* R8b — restore Claude editorial prose under cover */
body.page-id-111 .tc-tech-intro-prose {
  background: #f8f4ec;
  padding: clamp(2rem, 4vw, 3rem) clamp(1.25rem, 4vw, 3rem) 0.5rem;
  max-width: 1180px;
  margin: 0 auto;
}
body.page-id-111 .tc-tech-intro-prose__eyebrow {
  margin: 0 0 0.5rem;
  font-family: Inter, sans-serif;
  font-size: 0.78rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #b8944b;
}
body.page-id-111 .tc-tech-intro-prose__title {
  margin: 0 0 1rem;
  font-family: "Playfair Display", serif;
  font-size: clamp(1.9rem, 3vw, 2.6rem);
  font-weight: 600;
  color: #1e3a5f !important;
  line-height: 1.15;
}
body.page-id-111 .tc-tech-intro-prose__title em {
  color: #b8944b;
  font-style: italic;
}
body.page-id-111 .tc-tech-intro-prose p.lead {
  margin: 0 0 1rem;
  max-width: 42rem;
  font-family: Inter, sans-serif;
  font-size: 1.05rem;
  line-height: 1.65;
  color: #334155;
}
body.page-id-111 .tc-tech-meta-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 0.75rem;
  margin-top: 1.25rem;
  padding: 0.85rem 0 1.25rem;
  border-top: 1px solid rgba(30,58,95,0.12);
  font-family: Inter, sans-serif;
  font-size: 0.8rem;
  color: #64748b;
}
body.page-id-111 .tc-tech-meta-row a {
  color: #1e3a5f !important;
  text-decoration: underline;
  text-underline-offset: 3px;
}
"""

INTRO_HTML = """
<section class="tc-tech-intro-prose tc-tech-reveal" aria-label="Welcome to the Technology Hub">
  <p class="tc-tech-intro-prose__eyebrow">Welcome to the</p>
  <h2 class="tc-tech-intro-prose__title">Technology <em>Hub</em></h2>
  <p class="lead">The Technology Hub is the largest of Truth Collective's six hubs. It brings together the digital products that shape how people work, create, and live, from computers and displays to the tools just now reaching everyday use. Every category below has been reviewed and graded against the Truth Collective Trusted Selection Standards before it earns a place here.</p>
  <p class="lead">Each category leads to a dedicated page where the top products are ranked, graded, and explained in full. A closing section looks at the technologies still ahead, framed as what is worth watching, not as speculation.</p>
  <div class="tc-tech-meta-row">
    <p style="margin:0;">By Truth Collective Editorial · Updated 2026</p>
    <p style="margin:0;"><a href="https://tcstaging.truth-collective.com/product-selection-standards/">Reviewed against our Trusted Selection Standards →</a></p>
  </div>
</section>
"""

OLD_LEAD = (
    "Trusted tools for work, focus, and clear decisions. "
    "Selected and graded against one standard before they earn a place here."
)
NEW_LEAD = (
    "The largest of Truth Collective's six hubs. Digital products that shape how people "
    "work, create, and live, reviewed before they earn a place here."
)

OLD_STATS = """<div class="tc-tech-stats tc-tech-reveal" aria-label="Technology Hub at a glance">
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Standard</p>
    <p class="tc-tech-stats__value">Reviewed and graded</p>
  </div>
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Scope</p>
    <p class="tc-tech-stats__value">Eight trusted paths</p>
  </div>
  <div class="tc-tech-stats__item">
    <p class="tc-tech-stats__label">Currency</p>
    <p class="tc-tech-stats__value">Kept current for 2026</p>
  </div>
</div>"""

NEW_STATS = """<div class="tc-tech-stats tc-tech-reveal" aria-label="Technology Hub highlights">
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
</div>"""


def main() -> None:
    user = os.environ["TC_WP_USER"].strip()
    pw = os.environ["TC_WP_APP_PASSWORD"].strip()
    auth = base64.b64encode(f"{user}:{pw}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "User-Agent": "TC-REST-R8b",
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
    backup = BACKUP_DIR / f"page-{PAGE_ID}-before-REST-hub-technology-R8b-{date.today().isoformat()}.html"
    backup.write_text(raw, encoding="utf-8")
    print("backup", backup)

    if "tc-tech-intro-prose" not in raw:
        if 'id="tc-tech-hub-r8"' in raw or 'id="tc-tech-hub-r8b"' in raw:
            # inject CSS before first </style> inside r8 block
            style_end = raw.find("</style>")
            if style_end == -1:
                raise SystemExit("no style block")
            raw = raw[:style_end] + INTRO_CSS + raw[style_end:]
        marker = '<div class="tc-tech-stats'
        i = raw.find(marker)
        if i == -1:
            raise SystemExit("stats marker missing")
        raw = raw[:i] + INTRO_HTML + "\n" + raw[i:]

    raw = raw.replace(OLD_LEAD, NEW_LEAD)
    raw = raw.replace(OLD_STATS, NEW_STATS)
    raw = raw.replace("TECH-HUB-R8:", "TECH-HUB-R8b:", 1)
    raw = raw.replace('id="tc-tech-hub-r8"', 'id="tc-tech-hub-r8b"', 1)

    for must in (
        "Welcome to the",
        "largest of Truth Collective",
        "Each category leads",
        "tc-explore-hub",
    ):
        if must not in raw:
            raise SystemExit(f"missing after patch: {must}")

    updated = api("POST", f"/wp-json/wp/v2/pages/{PAGE_ID}", {"content": raw})
    print("updated", updated["id"])
    print("view", f"{BASE}/technology-hub/")


if __name__ == "__main__":
    main()
