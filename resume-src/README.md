# resume-src

HTML sources for the PDF resumes served from `public/resume/`. Edit the HTML,
rebuild, and commit both the source and the regenerated PDF.

## Setup

```bash
pip install playwright pypdf
playwright install chromium
```

Optional but recommended — install [Carlito](https://github.com/google/fonts/tree/main/ofl/carlito)
(metric-compatible with Calibri). Without it the renderer falls back to Calibri,
then Noto Sans, and line wrapping will differ slightly from the committed PDFs.

## Build

```bash
python3 resume-src/build.py                 # build all targets
python3 resume-src/build.py ai-ml-engineer  # build one
```

## Check

```bash
python3 resume-src/check.py
```

Verifies each resume still fits on **one** A4 page, and reports the remaining
vertical headroom. Run it after every content edit.

## Targets

| Source | Output PDF |
|---|---|
| `ai-ml-engineer.html` | `Amit_Kumar_Mohanty_AI_ML_Engineer_Resume.pdf` |

The other PDFs in `public/resume/` (Data Analyst, Data Scientist, and the older
AI Engineer / ML Engineer variants) predate this build setup and have no source
here.

## Editing rules that matter for ATS

These are not stylistic preferences — breaking them measurably degrades how
applicant tracking systems read the PDF.

1. **Never use `position: absolute` / `position: relative` for bullet markers or
   layout.** Positioned elements are painted in a later phase, which reorders
   the PDF text layer and detaches every bullet from its job heading. Use real
   `list-style` markers. See `RESUME_REVIEW.md` for what this looked like.
2. **Keep it single-column.** No floats, no grid columns, no tables.
3. **No text inside images.** Everything must stay in the text layer.
4. **Keep standard section headings** (`Experience`, `Education`, `Skills`,
   `Projects`, `Certifications`) — parsers match on these literal words.
5. **Spell keywords the way job postings do.** Prefer unhyphenated
   "Computer Vision" over "computer-vision"; an exact-phrase match misses the
   hyphenated form.

After any structural change, confirm the text layer still reads top-to-bottom:

```bash
python3 -c "import pypdf; print(pypdf.PdfReader('public/resume/Amit_Kumar_Mohanty_AI_ML_Engineer_Resume.pdf').pages[0].extract_text())"
```

Each job title should be immediately followed by its own bullets.
