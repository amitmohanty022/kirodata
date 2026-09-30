#!/usr/bin/env python3
"""Verify a rendered resume fits on one US Letter page and stays ATS-clean.

Measures the HTML source at true print width, then inspects the built PDF:

  * exactly one page
  * every character and rule is pure black (black and white only)
  * no em dashes anywhere, and no dash punctuation in the summary or bullets
    (hyphens inside words such as "peer-reviewed" are fine)
  * each bullet lands under its own job or project title in the text layer

Run after editing any resume source:

    python3 resume-src/check.py
"""

from __future__ import annotations

import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

import pdfplumber
import pypdf
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import OUT_DIR, SNAP_HEADINGS, SRC_DIR, TARGETS  # noqa: E402

PX_PER_IN = 96
PAGE_W_IN, PAGE_H_IN = 8.5, 11.0  # US Letter

EM_DASH, EN_DASH = "\u2014", "\u2013"


def print_area(stem: str) -> tuple[int, float]:
    """Printable width and height in px, read from the source's @page rule."""
    css = (SRC_DIR / f"{stem}.html").read_text(encoding="utf-8")
    m = re.search(r"@page\s*{[^}]*margin:\s*([\d.]+)in\s+([\d.]+)in"
                  r"(?:\s+([\d.]+)in\s+([\d.]+)in)?", css)
    if not m:
        raise SystemExit(f"{stem}.html: expected '@page {{ margin: <top>in <side>in ... }}'")
    top, right = float(m[1]), float(m[2])
    bottom = float(m[3]) if m[3] else top
    left = float(m[4]) if m[4] else right
    return (round((PAGE_W_IN - left - right) * PX_PER_IN),
            (PAGE_H_IN - top - bottom) * PX_PER_IN)
# A dash used as punctuation: an em/en dash anywhere, or a hyphen with a
# space on at least one side ("word - word", "word -word").
DASH_PUNCT = re.compile(rf"[{EM_DASH}{EN_DASH}]|\s-|-\s")


# --------------------------------------------------------------------------
# Source parsing
# --------------------------------------------------------------------------
class _Outline(HTMLParser):
    """Collect the summary text and each entry's title and bullets."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.summary = ""
        self.entries: list[tuple[str, list[str]]] = []
        self._in_summary = False
        self._in_li = False
        self._row_depth = 0
        self._span_idx = 0
        self._capture_title = False
        self._title = ""
        self._li = ""

    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get("class", "") or ""
        if tag == "p" and "summary" in cls.split():
            self._in_summary = True
        elif tag == "div" and "row" in cls.split():
            self._row_depth, self._span_idx, self._title = 1, 0, ""
        elif tag == "span" and self._row_depth:
            self._span_idx += 1
            self._capture_title = self._span_idx == 1
        elif tag == "li":
            self._in_li, self._li = True, ""

    def handle_endtag(self, tag):
        if tag == "p" and self._in_summary:
            self._in_summary = False
        elif tag == "span" and self._capture_title:
            self._capture_title = False
        elif tag == "div" and self._row_depth:
            self._row_depth = 0
            self.entries.append((_squash(self._title), []))
        elif tag == "li" and self._in_li:
            self._in_li = False
            if self.entries:
                self.entries[-1][1].append(_squash(self._li))

    def handle_data(self, data):
        if self._in_summary:
            self.summary += data
        if self._capture_title:
            self._title += data
        if self._in_li:
            self._li += data


def _squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _key(text: str) -> str:
    """Normalise for text-layer matching: fold ligatures, drop whitespace."""
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", text))


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------
def measure(stem: str, width: int) -> float:
    """Return content height in px at print width."""
    src = SRC_DIR / f"{stem}.html"
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        # Viewport is deliberately much taller than a page: scrollHeight is
        # clamped to the viewport height, which would mask any headroom.
        page = browser.new_page(viewport={"width": width, "height": 4000})
        page.goto(src.as_uri(), wait_until="load")
        page.emulate_media(media="print")
        page.evaluate(SNAP_HEADINGS)  # measure exactly what build.py prints
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


def _is_black(color) -> bool:
    if color is None:
        return True
    values = color if isinstance(color, (list, tuple)) else (color,)
    # Gray (0,), RGB (0,0,0) and CMYK (0,0,0,1) all mean black.
    if len(values) == 4:
        return all(v == 0 for v in values[:3]) and values[3] == 1
    return all(v == 0 for v in values)


def check_pdf(stem: str, pdf_path: Path) -> list[str]:
    problems: list[str] = []

    reader = pypdf.PdfReader(str(pdf_path))
    print(f"  pdf      : {len(reader.pages)} page(s)")
    if len(reader.pages) != 1:
        problems.append("PDF is not a single page")

    with pdfplumber.open(str(pdf_path)) as pdf:
        page = pdf.pages[0]
        colors = {str(c.get("non_stroking_color")) for c in page.chars
                  if not _is_black(c.get("non_stroking_color"))}
        colors |= {str(l.get("stroking_color")) for l in page.lines
                   if not _is_black(l.get("stroking_color"))}
        print(f"  color    : {'black only' if not colors else 'NOT black: ' + ', '.join(sorted(colors))}")
        if colors:
            problems.append("non-black text or rules found")

    text = reader.pages[0].extract_text()
    em = text.count(EM_DASH)
    print(f"  em dash  : {em}")
    if em:
        problems.append(f"{em} em dash(es) in the PDF")

    outline = _Outline()
    outline.feed((SRC_DIR / f"{stem}.html").read_text(encoding="utf-8"))

    dashed = [s for s in [outline.summary, *(b for _, bs in outline.entries for b in bs)]
              if DASH_PUNCT.search(s)]
    print(f"  dashes   : {len(dashed)} summary/bullet line(s) with dash punctuation")
    for s in dashed:
        problems.append(f"dash punctuation in: {_squash(s)[:70]}...")

    # Reading order: title_i < its bullets < title_{i+1} in the text layer.
    flat = _key(text)
    cursor, misplaced = 0, []
    for title, bullets in outline.entries:
        t = flat.find(_key(title), cursor)
        if t < 0:
            misplaced.append(f"title not found in order: {title}")
            continue
        cursor = t + len(_key(title))
        for b in bullets:
            pos = flat.find(_key(b)[:60], cursor)
            if pos < 0:
                misplaced.append(f"bullet not under '{title}': {b[:50]}...")
                continue
            # The bullet glyph must sit right before its text, otherwise the
            # markers were painted out of flow and pile up elsewhere.
            if flat[pos - 1:pos] != "\u2022":
                misplaced.append(f"bullet marker not in reading order: {b[:50]}...")
            cursor = pos
    print(f"  order    : {'every bullet under its own title' if not misplaced else f'{len(misplaced)} problem(s)'}")
    problems += misplaced

    return problems


def main() -> int:
    failures = 0

    for stem, pdf_name in TARGETS.items():
        width, printable = print_area(stem)
        height = measure(stem, width)
        headroom = printable - height
        print(f"{stem}.html")
        print(f"  content  : {height:.0f}px / {printable:.0f}px printable")
        print(f"  headroom : {headroom:+.0f}px (~{headroom / 15:+.1f} lines)")

        problems: list[str] = []
        if headroom < 0:
            problems.append("content overflows the page")
        elif headroom < 8:
            print("  WARN: almost no headroom; a font substitution could spill")

        pdf_path = OUT_DIR / pdf_name
        if pdf_path.exists():
            problems += check_pdf(stem, pdf_path)
        else:
            print(f"  SKIP: {pdf_name} not built yet")

        for p in problems:
            print(f"  FAIL: {p}")
        failures += len(problems)

    print("\nOK" if not failures else f"\n{failures} check(s) failed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
