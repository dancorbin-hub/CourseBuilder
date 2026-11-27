#!/usr/bin/env python3
"""Render one LD spec per exercise (.docx, then .pdf), for Pragmatic's instructional designers.

PRD: one LD spec per exercise. Fields: objective, timing, setup (Zoom and in person), steps per
platform, materials, success criteria, debrief questions, fallback path. The module file holds
the LD spec table in its "LD spec" section. Module 1 also has the course open build check LD
spec in course-open.md. The step cards from the module are attached, because the LD spec says
"steps per platform: see the cards".

Usage:
  python3 scripts/render_ld_spec.py --course market-research --module 1 [--version 1] [--no-pdf]
Output: courses/<course>/build/<CODE>_m<N>_LD_<exercise>_DRAFT_v<version>.docx and .pdf
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import course_model  # noqa: E402
import md_to_docx as M  # noqa: E402
from render_workbook import COURSE_CODES, to_pdf  # noqa: E402


def build(out, course_title, ex_title, ld_body, cards_body, no_pdf):
    doc = M.new_document(course_title, "LD spec. " + ex_title + ". Draft for review.")
    M.add_markdown(doc, ld_body, shift=1)
    if cards_body:
        M.page_break(doc)
        doc.add_heading("Attachment: step cards per platform", 1)
        M.add_markdown(doc, cards_body, shift=0)
    doc.save(out)
    print("wrote", out)
    if not no_pdf:
        to_pdf(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True)
    ap.add_argument("--module", required=True, type=int)
    ap.add_argument("--version", default="1")
    ap.add_argument("--no-pdf", action="store_true")
    a = ap.parse_args()
    root = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "courses", a.course))
    mdir = os.path.join(root, "modules", "m%d" % a.module)
    course_title = re.search(r"^\s*title:\s*(.+)$", open(os.path.join(root, "spec.yaml"), encoding="utf-8").read(), re.M).group(1)
    code = COURSE_CODES.get(a.course, a.course.upper())
    os.makedirs(os.path.join(root, "build"), exist_ok=True)

    mod = open(os.path.join(mdir, "module.md"), encoding="utf-8").read()
    _, ld = course_model.find_section(mod, "LD spec")
    _, cards = course_model.find_section(mod, "Step cards")
    build(os.path.join(root, "build", "%s_m%d_LD_lab%d_DRAFT_v%s.docx" % (code, a.module, a.module, a.version)),
          course_title, "Lab %d" % a.module, ld, cards, a.no_pdf)

    co_path = os.path.join(mdir, "course-open.md")
    if a.module == 1 and os.path.exists(co_path):
        co = open(co_path, encoding="utf-8").read()
        _, ld2 = course_model.find_section(co, "LD spec")
        _, cards2 = course_model.find_section(co, "Build check cards")
        if ld2:
            build(os.path.join(root, "build", "%s_m0_LD_build-check_DRAFT_v%s.docx" % (code, a.version)),
                  course_title, "Opening build check", ld2, cards2, a.no_pdf)


if __name__ == "__main__":
    main()
