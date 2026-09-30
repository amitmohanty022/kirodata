# Resume Review — AI/ML Engineer (v2)

**File:** `public/resume/Amit_Kumar_Mohanty_AI_ML_Engineer_Resume.pdf`
**Source:** `resume-src/ai-ml-engineer.html`
**Target roles:** AI/ML Engineer, Machine Learning Engineer, AI Engineer
**Reviewed:** 30 Sep 2026

---

## Overall score: 92 / 100

> This is a rubric-based assessment, not a score from a commercial ATS vendor.
> The measured numbers below (page count, keyword coverage, reading order,
> quantification rate) are real values extracted from the built PDF; the weights
> and judgement calls are mine.

| Dimension | Weight | v1 (old) | v2 (new) | Notes |
|---|---|---|---|---|
| ATS parseability & format | 20 | 18 | **20** | Fixed a real reading-order bug (see below) |
| Keyword / JD alignment | 20 | 18 | **19** | 40/40 common JD terms present |
| Impact & quantification | 20 | 15 | **16** | 62% of bullets carry a number |
| Clarity & plain language | 15 | 10 | **14** | Main focus of this rewrite |
| Role targeting | 15 | 11 | **14** | Added explicit headline, cut noise |
| Credibility signals | 10 | 9 | **9** | Award, paper, BITS, GPA all retained |
| **Total** | **100** | **81** | **92** | |

---

## Measured facts about the built PDF

| Check | Result |
|---|---|
| Pages | 1 (17px headroom — verified by `check.py`) |
| Word count | 696 |
| Text layer | Real, selectable text — no images, no scanned content |
| Fonts | Carlito subset, fully embedded (Type0), renders identically anywhere |
| Columns / tables | None — single-column, the safest layout for ATS |
| Reading order | Correct — every bullet parses directly under its own job heading |
| Live links | 3 (email, GitHub, LinkedIn) |
| Bullets | 13 total, 8 contain a hard number (62%) |
| JD keyword coverage | 40/40 (100%) of common AI/ML Engineer JD terms |

### The parseability bug that got fixed

The first build of this resume used absolutely positioned `::before` bullet
markers. CSS paints positioned elements in a **later paint phase**, so Chromium
wrote every bullet to the end of the PDF content stream. An ATS reading the text
layer linearly saw this:

```
Research Associate – AI, Keywords Studios India     May 2025 – Present
Artificial Intelligence Intern, Infosys             Nov 2024 – Feb 2025
Data Analytics & ML Intern, QL2 Software            Jun 2024 – Aug 2024
PROJECTS
...
CERTIFICATIONS
...
Train and improve AI agents that finish multi-step jobs...   <- all bullets
Helped build a web-automation agent...                          orphaned here
```

Three job titles with **zero accomplishments attached**, then an unattributed
blob of text. That is exactly the failure mode that gets a resume auto-scored
low. Switching to real `list-style` markers put everything back in flow. This is
worth knowing because it is invisible on screen and in print — it only shows up
when you extract the text layer. If you ever rebuild this in Word/Canva/LaTeX,
re-run the extraction check.

---

## What changed, and why

### 1. Added an explicit target headline

`AI / MACHINE LEARNING ENGINEER` now sits directly under the name. Recruiters
categorise a resume in a few seconds, and many ATS pull a "current title"
field. Previously the role had to be inferred from prose.

### 2. Plain-language rewrite of every experience bullet

This was your main request. The pattern: lead with a plain verb, say what the
thing actually *does*, keep the metric.

| Before | After |
|---|---|
| "Trained and optimized enterprise-grade Agentic AI models to autonomously execute complex multi-step workflows" | "Train and improve **AI agents that finish multi-step jobs on their own** — booking flights, placing online orders, and pulling data from websites" |
| "Contributed to a cutting-edge web-automation AI agent that visually interprets on-screen content and, from a natural-language instruction, autonomously plans and executes browser actions" | "Helped build a **web-automation agent** that reads what is on the screen, takes a plain-English instruction, and then clicks, types, and navigates a browser to get the job done" |
| "reducing hallucinations by 20%" | "**reduced made-up answers (hallucinations) by 20%**" |
| "delivered 85% of self-generated training datasets directly to production" | "pushed **85% of the training data I generated straight into production**" |

Words deliberately removed: *cutting-edge, enterprise-grade, autonomously,
leveraged, elevating, streamlining*. Keeping "hallucinations" in parentheses
after the plain phrase means a non-technical recruiter understands it **and**
the ATS still matches the keyword.

### 3. Marathon runner added

Placed as the closing line of the summary, tied to a work trait rather than
listed as a hobby:

> **Marathon runner** — the same patience and consistency I bring to systems
> that keep working long after launch.

The old hobby list (*drawing, tennis, running, philosophy, ASL, reading,
exploring new technology*) was cut. Seven hobbies in a summary reads as filler
and pushed your actual engineering pitch below the fold; one distinctive,
demanding hobby with a point lands much harder.

### 4. Trimmed the density

- Keywords Studios: 5 bullets → 4 (merged the dataset-QC bullet into the
  web-agent bullet, which covered the same work)
- Infosys: 4 bullets → 3 (merged the latency metric into the main build bullet)
- Certifications: 4 lines → 1 line (the descriptions were restating the titles)
- Job locations moved onto the title line (saved 3 lines)
- Coursework kept for the M.Tech only, and shortened

### 5. Moved Technical Skills above Experience

For an IC engineering role, the stack is the first filter for both a recruiter
skimming and a keyword matcher. Education still appears in full, just lower.

### 6. Restored two things that were missing

Both were in your earlier resume versions in this repo but absent from the
version you sent:

- **QL2 Software internship** (Jun–Aug 2024) — one compact bullet. It fills the
  gap before Infosys and makes the experience timeline continuous.
- **GPA 8.5/10** — a good number; many Indian-market screens filter on it.

### 7. Reworded for keyword coverage

"computer vision" previously appeared only hyphenated as "computer-vision", so
an exact-phrase match would miss it. Added **Computer Vision** and **Deep
Learning** as unhyphenated skill entries. Coverage went 38/41 → 40/40.

---

## Please verify these before you send it

These are changes or claims I could not confirm from the files. **Check each
one.**

1. **"2 years of experience"** — I counted from your first internship (Jun 2024)
   to now (Sep 2026). Your old resume said "around 1.5 years", which matches
   Keywords Studios alone (17 months). Both are defensible, but pick one and use
   it everywhere. If you want the conservative version, change the summary to
   *"over 1.5 years"*.
2. **GPA 8.5/10** — carried over from an older resume in this repo. Confirm it
   is final-transcript accurate.
3. **QL2 Software internship** — you had dropped it. If that was deliberate,
   delete the entry.
4. **M.Tech dates (Jul 2026 – Jul 2028)** — as written you started ~2 months
   ago. Confirm.
5. **Marathon runner** — only keep it if you have actually run a full marathon.
   If you run half-marathons, say "half-marathon runner". This is the kind of
   detail interviewers enjoy asking about, so it must be true.
6. **Metrics you will be asked to defend:** the 50% precision gain (over what
   baseline?), 85% of training data (out of how much?), 35% accuracy and 25%
   latency improvements (measured how?). Have a one-sentence answer for each.

---

## Honest remaining weaknesses

Things I could not fix by editing, in rough order of how much they cost you:

1. **No large-scale / distributed training signal.** Nothing shows work above
   single-GPU scale — no multi-GPU training, no dataset in the millions, no
   Spark/Ray/Airflow. Senior ML Engineer postings often screen for this. If you
   have any of it, it is the highest-value bullet you could add.
2. **Kubernetes, MLflow, AWS and Vertex AI are claimed in skills but appear in
   no bullet.** A careful interviewer will notice that gap and probe it. Either
   work one of them into a project bullet, or be ready to describe concrete
   usage.
3. **No GitHub links on individual projects.** Both `Dynamic Screen Companion`
   and `Diabetic Optiscan` have real code in this repo. Linking each project
   title straight to its folder is cheap credibility — say the word and I will
   add it.
4. **The publication is not cited.** "Peer-reviewed research paper" is much
   stronger with a venue name, year, or DOI. Add it if it is published.
5. **Website copy is now inconsistent with the resume.** `src/lib/data.ts` still
   says "~1 year of experience" and a `1+` years stat, while the resume says
   2 years. I did not change that copy since you only asked about the resume,
   but someone checking both will see the mismatch.

---

## Sending checklist

- Send as **PDF**, never .docx, and keep the filename as-is — it contains your
  name and the role.
- For each application, mirror the posting's exact job title in the headline
  ("Machine Learning Engineer" vs "AI Engineer") — a 5-second edit in
  `ai-ml-engineer.html`, then `python3 resume-src/build.py`.
- Re-order the first skills line so the posting's primary framework leads.
- If a posting names a tool you know but the resume omits, add it to the
  matching skills line. There is ~1.4 lines of vertical headroom; run
  `python3 resume-src/check.py` afterwards to confirm it still fits one page.
- Do **not** add a photo, and do not switch to a two-column template. Both
  reliably degrade ATS parsing.
