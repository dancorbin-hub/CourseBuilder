#!/usr/bin/env python3
"""Stage 4 QA checks for one module's rendered files. Deterministic. The qa-agent runs it, then looks at the pages.

Checks (PRD and CLAUDE.md house rules):
 D1  Deck: every slide has notes that start "POINT:" and hold "Talk Track:" (cover is exempt)
 D2  Deck: no "[AI USE CASE TT]" block
 D3  Deck: body text 18 pt or larger, and text fits (from the render sidecar .json)
 D4  Deck: module slide minutes add up to spec minutes (full day), and match module.md
 T1  All outputs: no em dash or en dash (deck text and notes, workbook, LD specs)
 C1  Step cards: 6 steps or fewer per card
 C2  Step cards: 20 words or fewer per sentence in each step
 C3  Step cards: each card has a data safety line
 C4  Step cards: check dates 30 days old or less (platform features change monthly)

Usage:
  python3 scripts/qa_check.py --course market-research --module 1 [--today 2026-11-26]
Output: courses/<course>/build/<CODE>_m<N>_QA_report.md. Exit code 1 when a check fails.
"""
import argparse
import datetime as dt
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import course_model  # noqa: E402
from render_workbook import COURSE_CODES  # noqa: E402

DASHES = re.compile("[–—]")
MAX_STEPS, MAX_WORDS, MAX_AGE_DAYS = 6, 20, 30


class Report:
    def __init__(self):
        self.rows = []  # (check, status, detail)

    def add(self, check, ok, detail=""):
        self.rows.append((check, "PASS" if ok else "FAIL", detail))

    def warn(self, check, detail):
        self.rows.append((check, "WARN", detail))

    @property
    def failed(self):
        return any(s == "FAIL" for _, s, _ in self.rows)


def dash_hits(label, text):
    out = []
    for line in text.splitlines():
        if DASHES.search(line):
            out.append("%s: %s" % (label, line.strip()[:90]))
    return out


def check_deck(r, pptx_path, sidecar_path, target_minutes, md_minutes, half=False):
    from pptx import Presentation
    name = os.path.basename(pptx_path)
    prs = Presentation(pptx_path)
    side = json.load(open(sidecar_path)) if os.path.exists(sidecar_path) else []
    ids = [s.get("id", "") for s in side]
    bad_notes, tt_block, dashes = [], [], []
    for i, slide in enumerate(prs.slides):
        sid = ids[i] if i < len(ids) else "slide %d" % (i + 1)
        notes = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""
        cover = sid == "cover" or (i < len(side) and side[i].get("layout", "").endswith("Course Cover") and not notes)
        if not cover and not (notes.lstrip().startswith("POINT:") and "Talk Track:" in notes):
            bad_notes.append(sid)
        if "[AI USE CASE TT]" in notes:
            tt_block.append(sid)
        body = "\n".join(sh.text_frame.text for sh in slide.shapes if sh.has_text_frame)
        dashes += dash_hits(sid + " slide", body) + dash_hits(sid + " notes", notes)
    r.add("D1 notes POINT and Talk Track (%s)" % name, not bad_notes, ", ".join(bad_notes))
    r.add("D2 no AI USE CASE TT block (%s)" % name, not tt_block, ", ".join(tt_block))
    r.add("T1 no em or en dash (%s)" % name, not dashes, "; ".join(dashes[:8]))
    if not side:
        r.add("D3 18 pt and fit (%s)" % name, False, "no sidecar .json; rerun render_deck.py")
        return
    small = [s["id"] for s in side if s.get("body_pt") is not None and s["body_pt"] < s.get("min_pt", 18)]
    nofit = [s["id"] for s in side if not s.get("fits", True)]
    r.add("D3 body 18 pt or larger, scaled to slide width (%s)" % name, not small, ", ".join(small))
    r.add("D3 text fits (%s)" % name, not nofit, ", ".join(nofit))
    mod_min = sum(s.get("minutes") or 0 for s in side if not str(s.get("id", "")).startswith(("O.", "cover")))
    if not half and target_minutes:
        r.add("D4 deck minutes = spec minutes (%s)" % name, mod_min == target_minutes,
              "deck %d, spec %d" % (mod_min, target_minutes))
    if md_minutes is not None:
        r.add("D4 deck minutes = module.md (%s)" % name, mod_min == md_minutes, "deck %d, module.md %d" % (mod_min, md_minutes))


def check_docx(r, path):
    from docx import Document
    d = Document(path)
    texts = [p.text for p in d.paragraphs]
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                texts.append(c.text)
    hits = dash_hits(os.path.basename(path), "\n".join(texts))
    r.add("T1 no em or en dash (%s)" % os.path.basename(path), not hits, "; ".join(hits[:8]))


def card_tables(cards_body):
    """Yield (card name, [step texts], body) for each '### Card' block."""
    parts = re.split(r"^### (.+)$", cards_body, flags=re.M)
    for i in range(1, len(parts), 2):
        head, body = parts[i].strip(), parts[i + 1]
        steps = []
        for line in body.splitlines():
            m = re.match(r"^\|\s*(\d+)\s*\|(.+)\|\s*$", line.strip())
            if m:
                steps.append(m.group(2).split("|")[0].strip())
        yield head, steps, body


def long_sentences(text):
    plain = re.sub(r"[*`]", "", text)
    out = []
    for s in re.split(r"(?<=[.!?])\s+", plain):
        n = len(s.split())
        if n > MAX_WORDS:
            out.append("%d words: %s" % (n, s[:70]))
    return out


def check_cards(r, label, cards_body, today):
    for head, steps, body in card_tables(cards_body):
        if not steps:
            continue  # fast-start table or intro
        name = "%s %s" % (label, head)
        r.add("C1 6 steps or fewer (%s)" % name, len(steps) <= MAX_STEPS, "%d steps" % len(steps))
        longs = [x for st in steps for x in long_sentences(st)]
        r.add("C2 sentences 20 words or fewer (%s)" % name, not longs, "; ".join(longs[:4]))
        if head.lower().startswith("card"):
            r.add("C3 data safety line (%s)" % name, "data safety" in body.lower())
            dates = re.findall(r"Check date[^:]*:\s*(\d{4}-\d{2}-\d{2})", body)
            if not dates:
                r.warn("C4 check date (%s)" % name, "no check date found")
            for d in dates:
                age = (today - dt.date.fromisoformat(d)).days
                r.add("C4 check date 30 days or less (%s)" % name, age <= MAX_AGE_DAYS,
                      "%s, %d days old, expires %s" % (d, age, dt.date.fromisoformat(d) + dt.timedelta(days=MAX_AGE_DAYS)))


def spec_minutes(spec_text, module):
    m = re.search(r"^\s*-\s*id:\s*m%d\s*$(.*?)^\s*minutes:\s*(\d+)" % module, spec_text, re.M | re.S)
    return int(m.group(2)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True)
    ap.add_argument("--module", required=True, type=int)
    ap.add_argument("--version", default="1")
    ap.add_argument("--today", default=dt.date.today().isoformat())
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.today)
    root = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "courses", a.course))
    mdir = os.path.join(root, "modules", "m%d" % a.module)
    build = os.path.join(root, "build")
    code = COURSE_CODES.get(a.course, a.course.upper())
    mod = open(os.path.join(mdir, "module.md"), encoding="utf-8").read()
    target = spec_minutes(open(os.path.join(root, "spec.yaml"), encoding="utf-8").read(), a.module)
    md_slides = course_model.slides(mod)
    md_min = sum(int(s.get("minutes") or 0) for s in md_slides)
    md_half = sum(int(s.get("minutes_half") or s.get("minutes") or 0) for s in md_slides)

    r = Report()
    for half in (False, True):
        tag = "_half" if half else ""
        p = os.path.join(build, "%s_m%d%s_DRAFT_v%s.pptx" % (code, a.module, tag, a.version))
        if os.path.exists(p):
            check_deck(r, p, p[:-5] + ".json", target, md_half if half else md_min, half)
        else:
            r.add("Deck exists (%s)" % os.path.basename(p), False, "not rendered")
    docs = sorted(glob.glob(os.path.join(build, "%s_m%d_Workbook_DRAFT_v%s.docx" % (code, a.module, a.version))) +
                  glob.glob(os.path.join(build, "%s_m*_LD_*_DRAFT_v%s.docx" % (code, a.version))))
    if not docs:
        r.add("Workbook and LD specs exist", False, "not rendered")
    for p in docs:
        check_docx(r, p)
    _, cards = course_model.find_section(mod, "Step cards")
    check_cards(r, "lab %d" % a.module, cards or "", today)
    co = os.path.join(mdir, "course-open.md")
    if a.module == 1 and os.path.exists(co):
        _, bc = course_model.find_section(open(co, encoding="utf-8").read(), "Build check cards")
        check_cards(r, "build check", bc or "", today)

    out = os.path.join(build, "%s_m%d_QA_report.md" % (code, a.module))
    fails = sum(1 for _, s, _ in r.rows if s == "FAIL")
    with open(out, "w", encoding="utf-8") as f:
        f.write("# QA report: %s module %d\n\nRun %s. %d checks, %d fail.\n\n" % (a.course, a.module, today, len(r.rows), fails))
        f.write("| Check | Result | Detail |\n| --- | --- | --- |\n")
        for c, s, d in sorted(r.rows, key=lambda x: {"FAIL": 0, "WARN": 1, "PASS": 2}[x[1]]):
            f.write("| %s | %s | %s |\n" % (c, s, d.replace("|", "/")))
    print("wrote", out, "|", len(r.rows), "checks,", fails, "fail")
    sys.exit(1 if r.failed else 0)


if __name__ == "__main__":
    main()
