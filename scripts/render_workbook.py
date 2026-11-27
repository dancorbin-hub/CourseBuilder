#!/usr/bin/env python3
"""Render the learner workbook for one module (.docx, then .pdf with LibreOffice).

The workbook has two jobs (PRD): guide learners through each exercise in class, and stay
useful after class. So it holds only learner content:
- Course open build check cards (module 1 only)
- Lab brief, data safety, step cards (one platform per page), log save card, Monday action
- Copyable templates from the module kit (brief, job card, code book, backlog, record sheet)
- The catch-up kit for the next module
Instructor-only content (debrief check, error reveal, instructor notes) is left out.

Usage:
  python3 scripts/render_workbook.py --course market-research --module 1 [--version 1] [--no-pdf]
Output: courses/<course>/build/<CODE>_m<N>_Workbook_DRAFT_v<version>.docx and .pdf
"""
import argparse
import glob
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import course_model  # noqa: E402
import md_to_docx as M  # noqa: E402

COURSE_CODES = {"market-research": "MR", "product-strategy-and-planning": "PSP", "market-and-launch": "ML"}
LEARNER_DEBRIEF_KEYS = ("What you do Monday", "Log save card")


def debrief_for_learners(body):
    """Keep only the Monday action and the log save card (with its table and notes)."""
    out = []
    keep = False
    for line in body.splitlines():
        m = re.match(r"^- ([^:]+):", line)
        if m:
            keep = m.group(1).strip() in LEARNER_DEBRIEF_KEYS
        if keep:
            out.append(line)
    return "\n".join(out)


def step_cards(body):
    """Split section 5 into its intro and one chunk per '### Card' or '### Fast-start'."""
    parts = re.split(r"^(### .+)$", body, flags=re.M)
    intro = parts[0]
    cards = [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]
    return intro, cards


def kit_block(doc, folder, title):
    files = sorted(f for f in glob.glob(os.path.join(folder, "*")) if not f.endswith(".txt") or "fallback" in f)
    doc.add_heading(title, 2)
    readme = os.path.join(folder, "README.md")
    if os.path.exists(readme):
        M.add_markdown(doc, open(readme, encoding="utf-8").read(), shift=2)
    for f in files:
        if f.endswith("README.md"):
            continue
        name = os.path.basename(f)
        doc.add_heading(name, 3)
        txt = open(f, encoding="utf-8").read()
        if name.endswith(".md") and "record-sheet" in name:
            M.add_markdown(doc, txt, shift=2)
        else:
            p = doc.add_paragraph("Copy this text into your agent. Copilot users add the .txt copy of the file.")
            M._code(doc, txt.splitlines())


def to_pdf(path):
    try:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", os.path.dirname(path), path],
                       check=True, timeout=240, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return path[:-5] + ".pdf"
    except Exception as e:  # PDF is optional; the .docx is the source
        print("PDF conversion failed:", e)
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True)
    ap.add_argument("--module", required=True, type=int)
    ap.add_argument("--version", default="1")
    ap.add_argument("--no-pdf", action="store_true")
    a = ap.parse_args()
    root = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "courses", a.course))
    mdir = os.path.join(root, "modules", "m%d" % a.module)
    mod = open(os.path.join(mdir, "module.md"), encoding="utf-8").read()
    title = re.search(r"^# (.+)$", mod, re.M).group(1)
    course_title = re.search(r"^\s*title:\s*(.+)$", open(os.path.join(root, "spec.yaml"), encoding="utf-8").read(), re.M).group(1)

    doc = M.new_document(course_title, "Workbook. " + title + ". Draft for review.")
    doc.add_paragraph("Fictional case data for training. Use your own work first. Use the case data if you cannot.")

    if a.module == 1 and os.path.exists(os.path.join(mdir, "course-open.md")):
        co = open(os.path.join(mdir, "course-open.md"), encoding="utf-8").read()
        _, cards = course_model.find_section(co, "Build check cards")
        if cards:
            M.page_break(doc)
            doc.add_heading("Course open: opening build check", 1)
            M.add_markdown(doc, cards, shift=0)

    M.page_break(doc)
    doc.add_heading(title, 1)
    _, lab = course_model.find_section(mod, "Lab brief")
    doc.add_heading("Lab brief", 2)
    M.add_markdown(doc, lab, shift=1)

    _, cards = course_model.find_section(mod, "Step cards")
    intro, chunks = step_cards(cards)
    M.add_markdown(doc, intro, shift=1)
    for head, body in chunks:
        M.page_break(doc)
        doc.add_heading(head.lstrip("# ").strip(), 2)
        M.add_markdown(doc, body, shift=1)

    _, deb = course_model.find_section(mod, "Debrief")
    M.page_break(doc)
    doc.add_heading("After the lab", 2)
    M.add_markdown(doc, debrief_for_learners(deb), shift=1)

    kit = os.path.join(mdir, "kit")
    subs = sorted(d for d in glob.glob(os.path.join(kit, "*")) if os.path.isdir(d))
    for i, d in enumerate(subs):
        M.page_break(doc)
        label = "Templates for this module" if i == 0 else "Catch-up kit for the next module"
        kit_block(doc, d, "%s (%s)" % (label, os.path.basename(d)))

    code = COURSE_CODES.get(a.course, a.course.upper())
    os.makedirs(os.path.join(root, "build"), exist_ok=True)
    out = os.path.join(root, "build", "%s_m%d_Workbook_DRAFT_v%s.docx" % (code, a.module, a.version))
    doc.save(out)
    print("wrote", out)
    if not a.no_pdf:
        pdf = to_pdf(out)
        if pdf:
            print("wrote", pdf)


if __name__ == "__main__":
    main()
