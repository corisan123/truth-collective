#!/usr/bin/env python3
"""Apply Claude SPEC to Billy Graham tribute page 6458."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import requests

BASE = "https://tcstaging.truth-collective.com"
PAGE_ID = 6458
BACKUP = (
    Path(__file__).resolve().parents[1]
    / "backups"
    / "page-6458-before-claude-spec-2026-08-11.html"
)

SIDEBAR_NEW = """<!-- wp:paragraph {"style":{"typography":{"fontSize":"22px","lineHeight":"1.4"},"spacing":{"padding":{"right":"4rem","left":"4rem","top":"var:preset|spacing|60"}}},"fontSize":",,"} -->
<p style="padding-top:var(--wp--preset--spacing--60);padding-right:4rem;padding-left:4rem;font-size:22px;line-height:1.4">417 crusades. 226 in the United States. 195 international. More than 214 million people heard him preach in person or by satellite before his final New York crusade in 2005.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"style":{"spacing":{"padding":{"right":"4rem","left":"4rem","bottom":"var:preset|spacing|60"}},"typography":{"fontSize":"16px","lineHeight":"1.45"}},"fontSize":",,"} -->
<p style="padding-right:4rem;padding-bottom:var(--wp--preset--spacing--60);padding-left:4rem;font-size:16px;line-height:1.45">Figures commonly published by the Billy Graham Evangelistic Association.</p>
<!-- /wp:paragraph -->"""

LEFT_OPEN_OLD = (
    "Beginning in the late 1940s and continuing for more than five decades, "
    "Billy Graham conducted evangelistic crusades in stadiums, arenas, and open fields "
    "on every inhabited continent. He preached to an estimated 215 million people in live "
    "audiences across more than 185 countries. Those numbers are not metaphors. They are "
    "the documented record of a man who spent his life showing up."
)
LEFT_OPEN_NEW = (
    "Beginning in the late 1940s and continuing for more than five decades, "
    "Billy Graham conducted evangelistic crusades in stadiums, arenas, and open fields "
    "on every inhabited continent. Those gatherings were not metaphors. They are the "
    "documented record of a man who spent his life showing up."
)

INTEGRITY_END = (
    "That kind of response does not come from charisma alone. It comes from integrity "
    "made visible over time. People trusted Billy Graham because Billy Graham had spent "
    "decades being trustworthy.</p>\n<!-- /wp:paragraph -->"
)
CRUSADES_PULL = (
    "That kind of response does not come from charisma alone. It comes from integrity "
    "made visible over time. People trusted Billy Graham because Billy Graham had spent "
    "decades being trustworthy.</p>\n<!-- /wp:paragraph -->\n\n"
    "<!-- wp:paragraph {\"style\":{\"spacing\":{\"padding\":{\"right\":\"var:preset|spacing|80\","
    "\"left\":\"var:preset|spacing|80\",\"top\":\"var:preset|spacing|40\",\"bottom\":\"var:preset|spacing|40\"}},"
    "\"typography\":{\"fontSize\":\"22px\",\"lineHeight\":\"1.35\",\"fontStyle\":\"italic\"}}} -->\n"
    "<p style=\"padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--80);"
    "padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--80);"
    "font-size:22px;font-style:italic;line-height:1.35\">"
    "He did not perform. He stood at a podium and told the truth as he understood it.</p>\n"
    "<!-- /wp:paragraph -->"
)

QUOTE_OLD = (
    '<p class="has--font-size" style="padding-right:8rem;padding-left:8rem">'
    "Rev. Billy Graham -</p>"
)
QUOTE_NEW = (
    '<p class="has--font-size" style="padding-right:8rem;padding-left:8rem">'
    "Rev. Billy Graham</p>"
)

BORN_IMG_OLD = (
    '<!-- wp:image {"id":6464,"width":"108px","height":"auto",'
    '"aspectRatio":"0.7939229214579413","sizeSlug":"full","linkDestination":"none",'
    '"align":"center","className":"is-style-rounded"} -->\n'
    '<figure class="wp-block-image aligncenter size-full is-resized is-style-rounded">'
    '<img src="https://tcstaging.truth-collective.com/wp-content/uploads/2026/06/billy-graham.jpg" '
    'alt="Billy Graham photo" class="wp-image-6464" '
    'style="aspect-ratio:0.7939229214579413;width:108px;height:auto"/></figure>\n'
    "<!-- /wp:image -->"
)
BORN_IMG_NEW = (
    '<!-- wp:image {"id":6464,"width":"320px","height":"auto","sizeSlug":"full",'
    '"linkDestination":"none","align":"center"} -->\n'
    '<figure class="wp-block-image aligncenter size-full is-resized">'
    '<img src="https://tcstaging.truth-collective.com/wp-content/uploads/2026/06/billy-graham.jpg" '
    'alt="Billy Graham photo" class="wp-image-6464" '
    'style="width:320px;height:auto;border-radius:12px"/></figure>\n'
    "<!-- /wp:image -->"
)


def replace_sidebar(raw: str) -> str:
    start_phrase = "Concluding his last crusade in 2005"
    end_phrase = "195 in foreign cities."
    a = raw.find(start_phrase)
    b = raw.find(end_phrase)
    if a < 0 or b < 0:
        raise RuntimeError("crusade sidebar markers missing")
    block_start = raw.rfind("<!-- wp:paragraph", 0, a)
    block_end = raw.find("<!-- /wp:paragraph -->", b)
    if block_start < 0 or block_end < 0:
        raise RuntimeError("crusade sidebar block bounds missing")
    block_end = block_end + len("<!-- /wp:paragraph -->")
    return raw[:block_start] + SIDEBAR_NEW + raw[block_end:]


def main() -> int:
    user = os.environ.get("TC_WP_USER")
    password = os.environ.get("TC_WP_APP_PASSWORD")
    if not user or not password:
        print("Missing credentials", file=sys.stderr)
        return 1
    auth = (user, password)
    url = f"{BASE}/wp-json/wp/v2/pages/{PAGE_ID}"
    before = requests.get(url, auth=auth, params={"context": "edit"}, timeout=90)
    before.raise_for_status()
    raw = before.json().get("content", {}).get("raw") or ""
    BACKUP.parent.mkdir(parents=True, exist_ok=True)
    if not BACKUP.exists():
        BACKUP.write_text(raw, encoding="utf-8")

    raw = replace_sidebar(raw)

    if LEFT_OPEN_OLD not in raw:
        print("Left open paragraph missing", file=sys.stderr)
        return 1
    raw = raw.replace(LEFT_OPEN_OLD, LEFT_OPEN_NEW, 1)

    if "He did not perform. He stood at a podium" not in raw:
        if INTEGRITY_END not in raw:
            print("Integrity paragraph missing", file=sys.stderr)
            return 1
        raw = raw.replace(INTEGRITY_END, CRUSADES_PULL, 1)

    if QUOTE_OLD not in raw:
        print("Quote attribution missing", file=sys.stderr)
        return 1
    raw = raw.replace(QUOTE_OLD, QUOTE_NEW, 1)

    if BORN_IMG_OLD not in raw:
        print("Born image block missing", file=sys.stderr)
        return 1
    raw = raw.replace(BORN_IMG_OLD, BORN_IMG_NEW, 1)

    ruth_pull = "She held the private life that made the public life possible."
    if ruth_pull not in raw:
        target = "until her death in 2007."
        if target not in raw:
            print("Ruth 2007 marker missing", file=sys.stderr)
            return 1
        raw = raw.replace(
            target,
            f'{target} <em>{ruth_pull}</em>',
            1,
        )

    raw = raw.replace(
        "Four times a year &mdash; the best new additions",
        "Four times a year. The best new additions",
    )

    born_tail = raw.split("Born to Serve", 1)[1][:1800]
    checks = {
        "no_214_duplicate_sentence": "Beyond his 417 crusades were rallies" not in raw,
        "has_bgea_source": "Figures commonly published by the Billy Graham Evangelistic Association"
        in raw,
        "quote_fixed": "Rev. Billy Graham -" not in raw and "Rev. Billy Graham</p>" in raw,
        "born_larger": "width:320px" in born_tail and "is-style-rounded" not in born_tail,
        "left_softened": "215 million" not in raw,
        "crusades_pull": "He did not perform. He stood at a podium" in raw,
        "sidebar_tight": "417 crusades. 226 in the United States. 195 international." in raw,
        "ruth_pull": ruth_pull in raw,
    }
    print("checks", checks)
    if not all(checks.values()):
        print("Checks failed", file=sys.stderr)
        return 1

    resp = requests.post(url, auth=auth, json={"content": raw}, timeout=120)
    if not resp.ok:
        print(resp.status_code, resp.text[:400], file=sys.stderr)
        return 1
    print("OK page 6458 updated len", len(resp.json().get("content", {}).get("raw") or ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
