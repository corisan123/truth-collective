"""Dimension-labeled SVG placeholders for TC scaffolds (Media Replace later)."""
from __future__ import annotations
import html as H
import urllib.parse

def svg_placeholder(w: int, h: int, label: str, slot: str = "") -> str:
    lab = H.escape(label)
    slot_e = H.escape(slot) if slot else ""
    lines = [
        f'<text x="50%" y="42%" text-anchor="middle" fill="#b8944b" font-family="Inter,Arial,sans-serif" font-size="{max(28, w // 18)}" font-weight="700">{w} × {h}</text>',
        f'<text x="50%" y="54%" text-anchor="middle" fill="#ffffff" font-family="Inter,Arial,sans-serif" font-size="{max(18, w // 36)}" font-weight="600">REPLACE THIS IMAGE</text>',
        f'<text x="50%" y="64%" text-anchor="middle" fill="#cbd5e1" font-family="Inter,Arial,sans-serif" font-size="{max(14, w // 48)}">{lab}</text>',
    ]
    if slot_e:
        lines.append(
            f'<text x="50%" y="74%" text-anchor="middle" fill="#94a3b8" font-family="Inter,Arial,sans-serif" font-size="{max(12, w // 55)}">{slot_e}</text>'
        )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <rect width="100%" height="100%" fill="#f8f4ec"/>
  <rect x="0" y="0" width="100%" height="{max(8, h // 80)}" fill="#b8944b"/>
  <rect x="{int(w * 0.14)}" y="{int(h * 0.29)}" width="{int(w * 0.72)}" height="{int(h * 0.42)}" fill="#1e3a5f"/>
  {''.join(lines)}
  <text x="50%" y="{h - max(36, h // 22)}" text-anchor="middle" fill="#64748b" font-family="Inter,Arial,sans-serif" font-size="{max(12, w // 60)}">Truth Collective · Media Replace</text>
</svg>"""
    return "data:image/svg+xml;charset=utf-8," + urllib.parse.quote(svg)

HERO = lambda slot="": svg_placeholder(1600, 1000, "Hub / hero / category tile", slot)
PRODUCT = lambda slot="": svg_placeholder(1200, 750, "Product card (16:10)", slot)
SQUARE = lambda slot="": svg_placeholder(1000, 1000, "Square product / cover", slot)
