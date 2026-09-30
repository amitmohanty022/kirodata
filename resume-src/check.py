#!/usr/bin/env python3
"""Verify a rendered resume fits on exactly one A4 page.

Measures the HTML source at true A4 print width and also asserts the built PDF
is a single page. Run after editing any resume source:

    python3 resume-src/check.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pypdf
from playwright.sync_api import sync_playwright

from build import OUT_DIR, SRC_DIR, TARGETS  # noqa: E402

PX_PER_MM = 96 / 25.4

# Must stay in sync with the @page rule in the HTML sources.
PAGE_W_MM, PAGE_H_MM = 210, 297
MARGIN_X_MM = 11 * 2
MARGIN_Y_MM = 10 + 9

PRINT_W = round((PAGE_W_MM - MARGIN_X_MM) * PX_PER_MM)
PRINT_H = (PAGE_H_MM - MARGIN_Y_MM) * PX_PER_MM


def measure(stem: str) -> float:
    """Return content height in px at A4 print width."""
    src = SRC_DIR / f"{stem}.html"
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        # Viewport is deliberately much taller than a page: scrollHeight is
        # clamped to the viewport height, which would mask any headroom.
        page = browser.new_page(viewport={"width": PRINT_W, "height": 4000})
        page.goto(src.as_uri(), wait_until="load")
        page.emulate_media(media="print")
        height = page.evaluate(
            "() => {"
            "  const kids = [...document.body.children];"
            "  const bottom = Math.max(...kids.map(el =>"
            "    el.getBoundingClientRect().bottom + window.scrollY));"
            "  return bottom - document.body.getBoundingClientRect().top;"
            "}"
        )
        browser.close()
    return height


def main() -> int:
    failures = 0

    for stem, pdf_name in TARGETS.items():
        height = measure(stem)
        headroom = PRINT_H - height
        print(f"{stem}.html")
        print(f"  content  : {height}px / {PRINT_H:.0f}px printable")
        print(f"  headroom : {headroom:+.0f}px (~{headroom / 11.8:+.1f} lines)")

        if headroom < 0:
            print("  FAIL: content overflows the page")
            failures += 1
        elif headroom < 10:
            print("  WARN: almost no headroom; a font substitution could spill")

        pdf_path = OUT_DIR / pdf_name
        if not pdf_path.exists():
            print(f"  SKIP: {pdf_name} not built yet")
            continue

        pages = len(pypdf.PdfReader(str(pdf_path)).pages)
        print(f"  pdf      : {pages} page(s)")
        if pages != 1:
            print("  FAIL: PDF is not a single page")
            failures += 1

    print("\nOK" if not failures else f"\n{failures} check(s) failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
