# Resume Review: AI/ML Engineer (v5)

**File:** `public/resume/Amit_Kumar_Mohanty_AI_ML_Engineer_Resume.pdf`
**Source:** `resume-src/ai-ml-engineer.html`
**Target roles:** AI/ML Engineer, Machine Learning Engineer, AI Engineer
**Reviewed:** 30 Sep 2026

---

## Overall score: 94 / 100 (your original: 77)

> This is my own rubric, not a score from a commercial ATS vendor. The
> measured numbers below (page count, keyword coverage, reading order, colors,
> dashes) come from the built PDF. The weights and judgement calls are mine.

| Dimension | Weight | Your original | v3 | Notes |
|---|---|---|---|---|
| ATS parseability & format | 20 | 14 | **20** | Original bullets contain no space characters (see below) |
| Keyword / JD alignment | 20 | 18 | **19** | 51/51 common AI/ML Engineer JD terms present |
| Impact & quantification | 20 | 15 | **16** | 9 of 15 bullets carry a hard number |
| Clarity & plain language | 15 | 10 | **15** | Plain English, and every bullet opens with a strong past tense verb |
| Role targeting | 15 | 11 | **15** | Summary opens with "AI/ML Engineer"; focused skills |
| Credibility signals | 10 | 9 | **9** | Award, paper, BITS, CGPA all kept |
| **Total** | **100** | **77** | **94** | |

Last round I scored your original 81. I lowered it to 77 after finding the
missing spaces problem described below, which I had not checked for before.

---

## Measured facts about the built PDF

| Check | Result |
|---|---|
| Page | 1 page, US Letter, same as your original |
| Layout | Your original's design, larger text (10pt body), even whole pixel spacing |
| Colors | Pure black text and rules only (verified per character) |
| Em dashes | 0 |
| Dashes in summary or bullets | 0 (the only dashes left are in dates and job title lines, as in your original) |
| Reading order | Every bullet sits directly under its own job or project title |
| Word spacing | Real spaces between words; reads identically in pypdf, pdfminer.six and pdfplumber |
| Fonts | Carlito (Calibri metrics), fully embedded |
| Links | 3 working links: email, GitHub, LinkedIn |
| JD keyword coverage | 51/51 (Python, PyTorch, LLM, RAG, Agentic, A/B test, OCR, inference, model serving, and more) |
| Length | 735 words, 15 bullets |

`python3 resume-src/check.py` verifies the page count, colors, dashes and
reading order automatically on every build.

---

## A problem in your original PDF

Every bullet line in your original has **zero space characters**, and every
bold phrase is stored separately from the sentence around it. On screen it
looks fine. To software it does not. The same bullet, read by three common PDF
text libraries:

| Library | What it reads from your original |
|---|---|
| pypdf | `Trained and optimized models to autonomously execute ... improving .` with the bold words ("enterprise-grade Agentic AI", "task-completion reliability") moved to the end of the page |
| pdfminer.six | `Trained and optimized` / `enterprise-grade Agentic AI` / `models to...` split into separate fragments |
| pdfplumber | `Trainedandoptimizedenterprise-gradeAgenticAImodelstoautonomously...` as one run-on word |

Your bold phrases are your best keywords and metrics, so these are the words
that get lost. All four `*_Updated.pdf` resumes on the `add-updated-ml-resume`
branch have this problem. The new PDF gives the same clean, in-order text in
all three libraries, bold words included.

---

## What changed in v5

1. **Removed the "AI/ML Engineer" line under your name.** The title still
   appears as the first words of the summary, where recruiters and ATS read it.
2. **Bigger text.** Body and bullets 9.4pt to 10pt, titles 10 to 10.5pt,
   headings 12 to 12.5pt, name 21 to 22pt, contact line 9.3 to 10pt.
3. **Even spacing everywhere.** The old 10.2pt line height printed as 9.75pt
   and 10.5pt on alternating lines, because Chromium snaps text to whole
   pixels. Every spacing value is now a whole pixel, and each kind of gap uses
   one shared value. Measured on the PDF: every wrapped line is 11.25pt below
   the one above, every bullet 12pt, every new entry 15pt, every section
   heading 19.5pt, and every heading to rule gap identical.
4. **Side margins 0.6in to 0.5in** so the larger text still fits on one page.
5. **Two bullets lightly reworded so no line ends with a single stray word:**
   the multimodal assistant bullet, and the A/B testing bullet, which now leads
   with its result ("Reduced hallucinations by 20% through A/B tests...").
   OOP and DSA moved to the Data & Cloud line so the Languages line fits on one
   line. No facts changed.

## What changed in v4

Only the summary and bullet wording changed. The layout was not touched: the
name, headline, every heading, title, date and rule sits at exactly the same
position as in v3 (verified from the PDF), and it is still 27 lines of summary
and bullets on one page.

1. **Summary opens with "AI/ML Engineer"**, so the title a recruiter
   searches for is the first thing in the summary.
2. **Marathon line reads "I am also a marathon runner"**, as you asked.
3. **Every bullet starts with a strong past tense verb.** Weak openers are
   gone: "Helped build" is now "Co-developed", "Named" is "Awarded", and "As the
   first member..." now starts with "Built".
4. **More ATS keywords inside the bullets**, not just in Skills: A/B tests,
   prompt engineering, data pipelines, OCR pipeline, image classification,
   concurrent inference, task completion reliability.
5. **Metrics kept whole.** "hallucinations (false answers) by 20%" can no
   longer split across two lines.
6. **Nothing new was claimed.** Every bullet maps to a statement in your
   original resume. No numbers, tools or results were added.

## What changed in v3

1. **Headline "AI/ML Engineer" under your name** (removed again in v5).
2. **Your original styling, measured, not eyeballed.** I extracted the exact
   values from your original PDF and matched them: US Letter, 0.6 inch side
   margins, Carlito, name 21pt, section headings 12pt bold caps over a 0.9pt
   rule, titles and dates 10pt bold, body 9.4pt, round bullets at the same
   indent, italic coursework and certification lines, full month names.
3. **Section order matches your original:** Summary, Education, Experience,
   Projects, Skills, Certifications.
4. **No dashes in the summary or any bullet.** Every em dash I had added is
   gone, and no bullet uses a dash as punctuation. Hyphens inside standard
   terms remain (peer-reviewed, Fine-tuned, Scikit-learn, ViT-B/16,
   co-authored).
5. **Black and white only.** Your original set body text in dark grey; this
   version uses pure black for everything, which prints and photocopies
   cleanly.
6. **Experience back to "1.5+ years".** Last version said 2 years, which only
   holds if you count internships. 1.5+ matches your original and what you
   would enter as total experience on job portals.
7. **Removed the tech tags under project titles.** The "TensorFlow, OpenCV"
   tag I had put on the Currency Detection app was my guess, not something
   from your files, so it should not have been there.

## Plain language rewrite (carried over and refined)

| Before (your original) | Now |
|---|---|
| "Trained and optimized enterprise-grade Agentic AI models to autonomously execute complex multi-step workflows" | "Trained and optimized **Agentic AI models** that complete complex tasks on their own, such as booking flights, placing online orders, and collecting web data, improving **task completion reliability**" |
| "Contributed to a cutting-edge web-automation AI agent that visually interprets on-screen content and ... autonomously plans and executes browser actions" | "Co-developed a **web automation AI agent** that reads the screen, follows plain English instructions, and clicks, types, and navigates websites by itself" |
| "Designed and A/B-tested prompt-engineering strategies ... reducing hallucinations by 20%" | "Ran **A/B tests** on prompt engineering strategies with automated LangSmith evaluation, reducing **hallucinations (false answers) by 20%**" |

Keeping "hallucinations" next to the plain phrase means a recruiter understands
it and the ATS still matches the keyword.

**Marathon runner** closes the summary: *"I am also a marathon runner and
bring that same discipline and consistency to everything I build."* The
seven-item hobby list was cut so it no longer pushes your engineering pitch
down.

**Trimmed:** Keywords Studios 5 bullets to 4, Infosys 4 to 3, Diabetic
Optiscan 3 to 2. R and Power BI were dropped from skills because they are
analyst tools that dilute an ML Engineer profile.

**Restored from your earlier resumes in this repo:** the QL2 Software
internship (fills the gap before Infosys) and CGPA 8.5/10.

---

## Please verify before sending

1. **CGPA 8.5/10** and the **QL2 internship** both came from your older resume
   versions. Confirm they are right, or delete them.
2. **"As the first member of a global team"** is your original wording. It can
   be read as "first person hired onto the team" or "first person to get data
   into production". Know which one you mean, because you will be asked.
3. **Metrics you will be asked to defend:** the 50% precision gain (over which
   baseline?), 85% of training data (out of how much?), 35% accuracy and 25%
   latency (measured how?). Have a one sentence answer for each.

---

## Remaining weaknesses

These need new facts, not better wording:

1. **No large scale training.** Nothing shows multi-GPU training, very large
   datasets, or tools like Spark, Ray or Airflow. Senior ML Engineer roles
   often filter on this. If you have any of it, it is the most valuable bullet
   you could add.
2. **Kubernetes, MLflow, AWS and Vertex AI appear in Skills but in no bullet.**
   An interviewer may probe this. Either use one in a bullet or be ready to
   describe real usage.
3. **No links on projects.** Dynamic Screen Companion and Diabetic Optiscan
   both have code in this repo. Linking each title to its folder adds
   credibility.
4. **The paper is not cited.** Adding the venue and year, or a DOI, makes
   "peer-reviewed" much stronger.
5. **Your website disagrees with the resume.** `src/lib/data.ts` still says
   "~1 year of experience" and shows a `1+` years stat.

---

## Sending checklist

- Send the **PDF**, never the HTML, and keep the filename.
- Match the posting's exact title in the first words of the summary when it differs
  ("Machine Learning Engineer" vs "AI Engineer"), then run
  `python3 resume-src/build.py`.
- There is about one line of spare room. After any edit, run
  `python3 resume-src/check.py` to confirm it is still one page and still
  black only with no dashes.
- Do not add a photo or switch to a two column template. Both hurt ATS
  parsing.
