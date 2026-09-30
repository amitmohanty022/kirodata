#!/usr/bin/env python3
"""Render the HTML resume source to a print-ready, ATS-friendly PDF.

Usage:
    python3 resume-src/build.py                  # build all known resumes
    python3 resume-src/build.py ai-ml-engineer   # build one by source stem

Requirements:
    pip install playwright && playwright install chromium

Fonts:
    The stylesheet asks for Carlito (metric-compatible with Calibri). If it is
    not installed the renderer falls back to Calibri, then Noto Sans. Install
    Carlito for output identical to the committed PDFs.
"""

from __future__ import annotations

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

SRC_DIR = Path(__file__).resolve().parent
OUT_DIR = SRC_DIR.parent / "public" / "resume"

# source stem -> output PDF filename
TARGETS = {
    "ai-ml-engineer": "Amit_Kumar_Mohanty_AI_ML_Engineer_Resume.pdf",
}


# Chromium paints SVG heading rules on the whole-pixel grid but lays text out
# at fractional positions, so the gap between each heading and its rule drifts
# by up to 0.75pt from section to section. Nudging every <h2> onto the pixel
# grid before printing makes all heading-to-rule gaps identical. Adds at most
# one pixel of space per heading.
SNAP_HEADINGS = """
() => {
  for (const h of document.querySelectorAll("h2")) {
    const top = h.getBoundingClientRect().top + window.scrollY;
    const frac = top - Math.floor(top);
    if (frac > 0.01) {
      const base = parseFloat(getComputedStyle(h).marginTop);
      h.style.marginTop = `${base + (1 - frac)}px`;
    }
  }
}
"""


def render(stem: str, out_name: str) -> Path:
    src = SRC_DIR / f"{stem}.html"
    if not src.exists():
        raise FileNotFoundError(f"No such resume source: {src}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / out_name

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page()
        page.goto(src.as_uri(), wait_until="load")
        page.emulate_media(media="print")
        page.evaluate(SNAP_HEADINGS)
        page.pdf(
            path=str(out),
            format="Letter",
            print_background=True,
            prefer_css_page_size=True,
        )
        browser.close()

    return out


def main() -> int:
    stems = sys.argv[1:] or list(TARGETS)
    for stem in stems:
        if stem not in TARGETS:
            print(f"unknown target {stem!r}; known: {', '.join(TARGETS)}")
            return 1
        out = render(stem, TARGETS[stem])
        print(f"built {out.relative_to(SRC_DIR.parent)} ({out.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
