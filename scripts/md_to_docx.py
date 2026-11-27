#!/usr/bin/env python3
"""Convert the markdown used in module files to a Word document.

Supports: headings (#, ##, ###, ####), paragraphs, bullets, numbered lists, pipe tables,
fenced code blocks (shown as a gray box, for copyable templates), **bold** and `code`.
Brand: Roboto Condensed / Arial, Pragmatic teal headings (#059CA0), navy tables (#234874).

Used by render_workbook.py and render_ld_spec.py. Can also run alone:
  python3 scripts/md_to_docx.py in.md out.docx
"""
import re
import sys

from docx import Document
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Inches

TEAL = RGBColor(0x05, 0x9C, 0xA0)
NAVY = RGBColor(0x23, 0x48, 0x74)
GRAY = RGBColor(0x40, 0x40, 0x40)
BODY_FONT = "Arial"
HEAD_FONT = "Roboto Condensed"


def new_document(title=None, subtitle=None):
    doc = Document()
    for s in doc.sections:
        s.left_margin = s.right_margin = Inches(0.9)
        s.top_margin = s.bottom_margin = Inches(0.8)
    st = doc.styles["Normal"]
    st.font.name = BODY_FONT
    st.font.size = Pt(11)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)
    for lvl, size in ((1, 22), (2, 16), (3, 13), (4, 12)):
        h = doc.styles["Heading %d" % lvl]
        h.font.name = HEAD_FONT
        h.font.size = Pt(size)
        h.font.color.rgb = TEAL if lvl < 3 else NAVY
        h.font.bold = lvl != 1
    if title:
        doc.add_heading(title, 0).runs[0].font.color.rgb = NAVY
    if subtitle:
        p = doc.add_paragraph(subtitle)
        p.runs[0].font.color.rgb = GRAY
    return doc


def page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def _shade(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def add_inline(par, text):
    """Add text with **bold** and `code` spans."""
    for tok in re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text):
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**"):
            par.add_run(tok[2:-2]).bold = True
        elif tok.startswith("`") and tok.endswith("`"):
            r = par.add_run(tok[1:-1])
            r.font.name = "Consolas"
        else:
            par.add_run(tok)


def _table(doc, rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not all(re.fullmatch(r":?-{3,}:?", c) for c in r)]
    if not cells:
        return
    ncol = max(len(r) for r in cells)
    t = doc.add_table(rows=len(cells), cols=ncol)
    t.style = "Table Grid"
    t.autofit = False
    # Column widths follow content length, so a "Step" number column stays narrow.
    lens = [max(min(len(r[j]) if j < len(r) else 0, 60) for r in cells) + 4 for j in range(ncol)]
    total_w = 6.7
    widths = [max(0.6, total_w * l / sum(lens)) for l in lens]
    scale = total_w / sum(widths)
    widths = [w * scale for w in widths]
    for j, col in enumerate(t.columns):
        col.width = Inches(widths[j])
    for i, r in enumerate(cells):
        for j in range(ncol):
            cell = t.cell(i, j)
            cell.width = Inches(widths[j])
            cell.text = ""
            add_inline(cell.paragraphs[0], r[j] if j < len(r) else "")
            for run in cell.paragraphs[0].runs:
                run.font.size = Pt(10)
                if i == 0:
                    run.bold = True
                    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            if i == 0:
                _shade(cell, "234874")
    doc.add_paragraph()


def _code(doc, lines):
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    c = t.cell(0, 0)
    _shade(c, "F2F2F2")
    c.text = ""
    p = c.paragraphs[0]
    for i, line in enumerate(lines):
        r = p.add_run(line)
        r.font.name = "Consolas"
        r.font.size = Pt(9.5)
        if i < len(lines) - 1:
            r.add_break()
    doc.add_paragraph()


def add_markdown(doc, text, shift=0):
    """Append markdown text. shift adds to heading levels (## with shift 1 -> Heading 3)."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("<!--"):
            while i < len(lines) and "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        if s.startswith("```"):
            j = i + 1
            buf = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                buf.append(lines[j])
                j += 1
            _code(doc, buf)
            i = j + 1
            continue
        if s.startswith("|"):
            j = i
            buf = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                buf.append(lines[j])
                j += 1
            _table(doc, buf)
            i = j
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lvl = min(4, len(m.group(1)) + shift)
            doc.add_heading(m.group(2), lvl)
            i += 1
            continue
        m = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        if m:
            style = "List Bullet 2" if len(m.group(1)) >= 2 else "List Bullet"
            add_inline(doc.add_paragraph(style=style), m.group(2))
            i += 1
            continue
        m = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if m:
            # Literal numbers: Word auto-numbering would run on across step cards.
            p = doc.add_paragraph()
            indent = 0.5 if len(m.group(1)) >= 2 else 0.25
            p.paragraph_format.left_indent = Inches(indent + 0.25)
            p.paragraph_format.first_line_indent = Inches(-0.25)
            add_inline(p, "%s. %s" % (m.group(2), m.group(3)))
            i += 1
            continue
        if s:
            add_inline(doc.add_paragraph(), s)
        i += 1
    return doc


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    d = new_document()
    add_markdown(d, open(src, encoding="utf-8").read())
    d.save(dst)
    print("wrote", dst)
