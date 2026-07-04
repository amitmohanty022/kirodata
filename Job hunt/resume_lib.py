#!/usr/bin/env python3
"""Reusable ATS-friendly one-page resume renderer (DOCX + PDF).

A `content` dict drives both renderers. Expected keys:
    NAME, CONTACT, TARGET, SUMMARY (str)
    EDUCATION: list of (school, dates, degree)
    EXPERIENCE: list of (role, loc, dates, [bullets])
    PROJECTS:   list of (name, dates, [bullets])
    SKILLS:     list of (category, items)
    CERTIFICATIONS: list of str
"""


# ---------------------------------------------------------------------------
# DOCX GENERATION
# ---------------------------------------------------------------------------
def build_docx(c, path):
    from docx import Document
    from docx.shared import Pt, RGBColor, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.4)
        s.bottom_margin = Inches(0.4)
        s.left_margin = Inches(0.6)
        s.right_margin = Inches(0.6)

    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(9.5)
    style.paragraph_format.space_after = Pt(0)
    style.paragraph_format.space_before = Pt(0)
    style.paragraph_format.line_spacing = 1.0

    def set_spacing(p, before=0, after=0, line=1.0):
        pf = p.paragraph_format
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        pf.line_spacing = line

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(c["NAME"]); r.bold = True; r.font.size = Pt(20)
    set_spacing(p, 0, 1)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(c["CONTACT"]); r.font.size = Pt(9)
    set_spacing(p, 0, 1)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Target Role: " + c["TARGET"]); r.font.size = Pt(9.5); r.italic = True
    set_spacing(p, 0, 4)

    def heading(text):
        p = doc.add_paragraph()
        r = p.add_run(text.upper()); r.bold = True; r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)
        set_spacing(p, 5, 1)
        pPr = p._p.get_or_add_pPr()
        pbdr = OxmlElement("w:pBdr")
        bottom = OxmlElement("w:bottom")
        bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), "6")
        bottom.set(qn("w:space"), "1"); bottom.set(qn("w:color"), "1F3A5F")
        pbdr.append(bottom); pPr.append(pbdr)

    def bullet(text):
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.left_indent = Inches(0.18)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run(text); r.font.size = Pt(9.5)

    def title_line(left_bold, right):
        p = doc.add_paragraph()
        set_spacing(p, 2, 0)
        section_w = Inches(8.5) - Inches(0.6) - Inches(0.6)
        p.paragraph_format.tab_stops.add_tab_stop(section_w, WD_TAB_ALIGNMENT.RIGHT)
        r = p.add_run(left_bold); r.bold = True; r.font.size = Pt(10)
        r2 = p.add_run("\t" + right); r2.font.size = Pt(9); r2.bold = True

    def sub_line(text):
        p = doc.add_paragraph(); set_spacing(p, 0, 0)
        r = p.add_run(text); r.italic = True; r.font.size = Pt(9.5)

    heading("Professional Summary")
    p = doc.add_paragraph(); set_spacing(p, 2, 0)
    r = p.add_run(c["SUMMARY"]); r.font.size = Pt(9.5)

    heading("Education")
    for school, dates, degree in c["EDUCATION"]:
        title_line(school, dates); sub_line(degree)

    heading("Experience")
    for role, loc, dates, bullets in c["EXPERIENCE"]:
        title_line(role + "  -  " + loc, dates)
        for b in bullets:
            bullet(b)

    heading("Projects")
    for name, dates, bullets in c["PROJECTS"]:
        title_line(name, dates)
        for b in bullets:
            bullet(b)

    heading("Skills")
    for cat, items in c["SKILLS"]:
        p = doc.add_paragraph(); set_spacing(p, 1, 0)
        r = p.add_run(cat + ": "); r.bold = True; r.font.size = Pt(9.5)
        r2 = p.add_run(items); r2.font.size = Pt(9.5)

    heading("Certifications")
    for cert in c["CERTIFICATIONS"]:
        bullet(cert)

    doc.save(path)


# ---------------------------------------------------------------------------
# PDF GENERATION
# ---------------------------------------------------------------------------
def build_pdf(c, path):
    from fpdf import FPDF

    NAVY = (31, 58, 95)
    BLACK = (0, 0, 0)

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.set_margins(left=15, top=10, right=15)
    pdf.add_page()
    epw = pdf.w - 30

    def name_header():
        pdf.set_font("Helvetica", "B", 22); pdf.set_text_color(*BLACK)
        pdf.cell(0, 9, c["NAME"], align="C", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 8.5)
        pdf.cell(0, 4.5, c["CONTACT"], align="C", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "I", 9); pdf.set_text_color(*NAVY)
        pdf.cell(0, 4.5, "Target Role: " + c["TARGET"], align="C", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1.5)

    def heading(text):
        pdf.ln(1.2)
        pdf.set_font("Helvetica", "B", 10.5); pdf.set_text_color(*NAVY)
        pdf.cell(0, 5, text.upper(), new_x="LMARGIN", new_y="NEXT")
        pdf.set_draw_color(*NAVY); pdf.set_line_width(0.3)
        pdf.line(15, pdf.get_y(), 15 + epw, pdf.get_y())
        pdf.ln(0.8); pdf.set_text_color(*BLACK)

    def body(text, size=9.3):
        pdf.set_font("Helvetica", "", size); pdf.set_text_color(*BLACK)
        pdf.multi_cell(0, 4.2, text, new_x="LMARGIN", new_y="NEXT")

    def title_line(left, right):
        pdf.set_font("Helvetica", "B", 10); pdf.set_text_color(*BLACK)
        rw = pdf.get_string_width(right) + 1
        pdf.cell(epw - rw, 4.8, left, new_x="RIGHT", new_y="TOP")
        pdf.set_font("Helvetica", "B", 8.8)
        pdf.cell(rw, 4.8, right, align="R", new_x="LMARGIN", new_y="NEXT")

    def sub_line(text):
        pdf.set_font("Helvetica", "I", 9.2)
        pdf.multi_cell(0, 4.2, text, new_x="LMARGIN", new_y="NEXT")

    def bullet(text, size=9.3):
        pdf.set_font("Helvetica", "", size); pdf.set_text_color(*BLACK)
        x0 = pdf.get_x()
        pdf.cell(4, 4.2, chr(149), new_x="RIGHT", new_y="TOP")
        pdf.set_x(x0 + 4)
        pdf.multi_cell(epw - 4, 4.2, text, new_x="LMARGIN", new_y="NEXT")

    def cat_line(cat, items, size=9.3):
        pdf.set_x(15); pdf.set_font("Helvetica", "B", size)
        cw = pdf.get_string_width(cat + ": ")
        pdf.cell(cw, 4.2, cat + ": ", new_x="RIGHT", new_y="TOP")
        pdf.set_x(15 + cw); pdf.set_font("Helvetica", "", size)
        pdf.multi_cell(epw - cw, 4.2, items, new_x="LMARGIN", new_y="NEXT")

    name_header()
    heading("Professional Summary"); body(c["SUMMARY"])
    heading("Education")
    for school, dates, degree in c["EDUCATION"]:
        title_line(school, dates); sub_line(degree)
    heading("Experience")
    for role, loc, dates, bullets in c["EXPERIENCE"]:
        title_line(role + "  -  " + loc, dates)
        for b in bullets:
            bullet(b)
        pdf.ln(0.6)
    heading("Projects")
    for name, dates, bullets in c["PROJECTS"]:
        title_line(name, dates)
        for b in bullets:
            bullet(b)
        pdf.ln(0.6)
    heading("Skills")
    for cat, items in c["SKILLS"]:
        cat_line(cat, items)
    heading("Certifications")
    for cert in c["CERTIFICATIONS"]:
        bullet(cert)

    pdf.output(path)
    return pdf.page_no(), pdf.get_y()
