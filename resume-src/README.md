# resume-src

HTML sources for the PDF resumes served from `public/resume/`. Edit the HTML,
rebuild, check, and commit both the source and the regenerated PDF.

## Setup

```bash
pip install playwright pypdf pdfplumber
playwright install chromium
```

Also install [Carlito](https://github.com/google/fonts/tree/main/ofl/carlito)
(metric compatible with Calibri). Without it the renderer falls back to
Calibri or a generic sans, line wrapping changes, and the page may spill.

## Build and check

```bash
python3 resume-src/build.py   # render every target to public/resume/
python3 resume-src/check.py   # must print OK before you commit
python3 resume-src/jd_match.py -v   # keyword match against real job postings
```

`check.py` fails the build if the resume:

- runs past one US Letter page
- contains any non-black text or rule
- contains an em dash anywhere, or dash punctuation in the summary or a bullet
- has any bullet that is not directly under its own title in the text layer
- splits a hyphenated word across two lines ("Fine- tuning" hides the keyword)

## Targets

| Source | Output PDF |
|---|---|
| `ai-ml-engineer.html` | `Amit_Kumar_Mohanty_AI_ML_Engineer_Resume.pdf` |

The other PDFs in `public/resume/` predate this setup and have no source here.

## Style

The layout follows the original resume on the `add-updated-ml-resume` branch
(Carlito, bold caps headings over a thin rule, bold titles with right aligned
dates, round bullets, italic coursework and descriptions), with larger text:
body and bullets 10pt, titles 10.5pt, headings 12.5pt, name 22pt, on US Letter
with 0.5in side margins. Everything is pure black.

**Spacing.** Chromium snaps each text line to a whole pixel (1px = 0.75pt), so
a line height like 10.2pt prints as 9.75pt and 10.5pt on alternating lines.
Every vertical size is therefore a whole number of px, set once in the `:root`
variables at the top of the stylesheet:

| Variable | Value | Used for |
|---|---|---|
| `--lh` | 15px (11.25pt) | every line of text |
| `--g-line` | 1px | between bullets, between skill lines, below a title |
| `--g-entry` | 4px | between schools, jobs, projects, certifications |
| `--g-section` | 8px | above every section heading |
| `--g-rule` | 3px | between a section rule and the text under it |

Change spacing only through these variables and keep them whole px.

## Rules that keep the PDF ATS safe

These are not preferences. Breaking any of them measurably changes what an
applicant tracking system reads.

1. **No `position: absolute` or `position: relative` for bullets or layout.**
   Positioned boxes are painted in a later phase, which moves them to the end
   of the PDF text layer, away from their job titles. Bullets use an in-flow
   `inline-block` marker with a hanging indent.
2. **Keep real text.** Never place words individually or render text as an
   image. Chromium writes real space characters and keeps bold words inside
   their sentence. The `*_Updated.pdf` resumes on the `add-updated-ml-resume`
   branch have no spaces inside bullets, and some parsers read them as one
   run-on word.
3. **Single column.** No floats, grid columns, or tables.
4. **Standard section headings** (Experience, Education, Skills, Projects,
   Certifications). Parsers match on these words.
5. **Heading rules are inline SVG.** Chromium snaps border widths to whole
   device pixels, so a 0.9pt border prints at 0.75pt on some headings and
   1.5pt on others. `build.py` also nudges each heading onto the pixel grid so
   every heading to rule gap is identical.

To see what an ATS sees:

```bash
python3 -c "import pypdf; print(pypdf.PdfReader('public/resume/Amit_Kumar_Mohanty_AI_ML_Engineer_Resume.pdf').pages[0].extract_text())"
```
