#!/usr/bin/env python3
"""Render a module deck (.pptx) on the Pragmatic master (PRD decision 19).

Two inputs per module, both in courses/<course>/modules/m<N>/:
- module.md (and course-open.md for module 1): the course model. Speaker notes come from here,
  word for word.
- slides.json: the slide layout plan made by the deck-renderer agent from module.md. It holds
  only words that are in module.md, cut down to fit a slide (title, lead, items, tiles, callout).

How it works:
1. Copy the style reference deck AI_Agents.26.07.02.pptx with all slides removed. Only the
   master, its layouts and the theme stay. The original file is never edited.
2. Put the course name on the cover layout of the copy.
3. Add one slide per slides.json entry on its layout, with brand fonts and colors.
   Text shrinks to fit, never below 18 pt (quality bar 13).
4. Copy the notes block of the same slide id from module.md into the speaker notes.
5. Write a sidecar JSON per slide (font size, fit, minutes) for the QA check.

Usage:
  python3 scripts/render_deck.py --course market-research --module 1 [--half-day] [--version 1]
Output: courses/<course>/build/<CODE>_m<N>[_half]_DRAFT_v<version>.pptx and .json
"""
import argparse
import json
import math
import os
import re
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import course_model  # noqa: E402

REFERENCE = "/mnt/project-files/course-builder/reference/AI_Agents.26.07.02.pptx"
TEAL = RGBColor(0x05, 0x9C, 0xA0)
NAVY = RGBColor(0x23, 0x48, 0x74)
ORANGE = RGBColor(0xF3, 0x77, 0x20)
GRAY = RGBColor(0x40, 0x40, 0x40)
LIGHT = RGBColor(0x9A, 0x9A, 0x9A)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PALE = RGBColor(0xF2, 0xF6, 0xF7)
MIN_PT = 18
COURSE_CODES = {"market-research": "MR", "product-strategy-and-planning": "PSP", "market-and-launch": "ML"}

# layout key -> (master layout name, content left edge in inches)
LAYOUTS = {
    "course cover": ("1_Course Cover", 11.5),
    "chapter break": ("Chapter Break", 9.5),
    "blank": ("Blank", 2.2),
    "blank_no dots": ("Blank_No Dots", 2.2),
    "1_blank": ("1_Blank", 2.2),
    "activity": ("Activity", 3.4),
    "debrief": ("debrief", 3.4),
    "1_prompt": ("1_prompt", 3.4),
    "blank_tiles": ("Blank_Tiles", 2.2),
    "action plan": ("Action Plan", 2.2),
    "put it into action": ("Put it Into Action", 2.2),
}


def pick_layout(name):
    key = name.split("(")[0].split(",")[0].strip().lower()
    if key in LAYOUTS:
        return LAYOUTS[key]
    for k, v in LAYOUTS.items():
        if key.startswith(k):
            return v
    return LAYOUTS["blank"]


def clean_copy(src, dst, title, subtitle, version):
    prs = Presentation(src)
    ids = prs.slides._sldIdLst
    for sid in list(ids):
        prs.part.drop_rel(sid.rId)
        ids.remove(sid)
    for m in prs.slide_masters:
        for lay in m.slide_layouts:
            if lay.name == "1_Course Cover":
                sub_top = next((sh.top for sh in lay.shapes if sh.name == "TextBox 35"), None)
                for sh in lay.shapes:
                    if sh.name == "TextBox 36" and sh.has_text_frame:
                        _set_keep_format(sh.text_frame, title.upper())
                        _fit_cover_title(sh, title.upper(), sub_top)
                    elif sh.name == "TextBox 35" and sh.has_text_frame:
                        _set_keep_format(sh.text_frame, subtitle.upper())
                    elif sh.name == "TextBox 3" and sh.has_text_frame:
                        _set_keep_format(sh.text_frame, version)
    prs.save(dst)


def _wrap_lines(words, cpl):
    lines, cur = 1, 0
    for w in words:
        need = len(w) if cur == 0 else cur + 1 + len(w)
        if need > cpl and cur:
            lines, cur = lines + 1, len(w)
        else:
            cur = need
    return lines


def _fit_cover_title(sh, title, sub_top):
    """The cover title box grows down and covered the subtitle for long course names.
    Shrink the title to 2 lines or fewer and move the box up so it ends above the subtitle."""
    width_in = sh.width / 914400
    words = title.split()
    size, lines = 150, 1
    for size in range(150, 59, -6):
        lines = _wrap_lines(words, int(width_in * 72 / (size * 0.66)))
        if lines <= 2:
            break
    for p in sh.text_frame.paragraphs:
        for r in p.runs:
            r.font.size = Pt(size)
    if sub_top is not None:
        need = Inches(lines * size * 1.15 / 72 + 0.25)
        sh.top = max(Inches(0.5), sub_top - need)


def _set_keep_format(tf, text):
    p = tf.paragraphs[0]
    runs = p.runs
    if runs:
        runs[0].text = text
        for r in runs[1:]:
            r.text = ""
    for extra in tf.paragraphs[1:]:
        for r in extra.runs:
            r.text = ""


def fit_size(lines, width_in, height_in, start=32, gap=0.45):
    for size in range(start, MIN_PT - 1, -2):
        cpl = max(8, int(width_in * 72 / (size * 0.50)))
        rows = sum(max(1, math.ceil(len(l) / cpl)) for l in lines)
        need = rows * size * 1.2 / 72 + len(lines) * size * gap / 72
        if need <= height_in:
            return size, True
    return MIN_PT, False


def text(slide, left, top, width, height, lines, size, color=GRAY, font="Roboto Condensed",
         bold=False, align=None, anchor=MSO_ANCHOR.TOP, highlight=None, prefix=None, prefix_color=None):
    tb = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if align:
            p.alignment = align
        p.space_after = Pt(size * 0.45)
        if prefix:
            r = p.add_run()
            r.text = prefix(i)
            r.font.size = Pt(size)
            r.font.name = "Roboto Medium"
            r.font.color.rgb = prefix_color or ORANGE
        pieces = [line]
        if highlight and highlight in line:
            a, b = line.split(highlight, 1)
            pieces = [a, (highlight,), b]
        for piece in pieces:
            r = p.add_run()
            hl = isinstance(piece, tuple)
            r.text = piece[0] if hl else piece
            r.font.size = Pt(size)
            r.font.name = font
            r.font.bold = bold
            r.font.color.rgb = (ORANGE if hl else color)
    return tb


def box(slide, left, top, width, height, fill, line_color=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line_color:
        shp.line.color.rgb = line_color
    else:
        shp.line.fill.background()
    shp.shadow.inherit = False
    return shp


def tag(slide, left, top, label, fill):
    shp = box(slide, left, top, 0.27 * len(label) + 0.7, 0.62, fill)
    tf = shp.text_frame
    tf.text = label
    r = tf.paragraphs[0].runs[0]
    r.font.size = Pt(22)
    r.font.name = "Roboto Medium"
    r.font.color.rgb = WHITE


def render_slide(prs, by_name, W, spec, notes, module_no, half_day):
    layout_name, left = pick_layout(spec.get("layout", "Blank"))
    s = prs.slides.add_slide(by_name[layout_name])
    lay = layout_name.lower()
    width = W - left - 1.8
    sizes = []
    fits = True
    minutes = spec.get("minutes_half" if half_day else "minutes", spec.get("minutes", 0)) or 0
    kind = spec.get("kind", "bullets")

    if lay == "1_course cover":
        s.notes_slide.notes_text_frame.text = notes
        return s, {"body_pt": None, "fits": True}

    top = 1.1
    if lay == "chapter break":
        tag(s, left, 2.6, "MODULE %s" % module_no, TEAL)
        top = 3.5
    elif lay == "1_prompt":
        tag(s, left, 0.55, "LIVE DEMO", ORANGE)
        top = 1.45
    title = spec.get("title", "")
    if kind == "statement":
        tsize, ok = fit_size([title], W - 4.4, 3.0, start=66)
        text(s, 2.2, 3.0, W - 4.4, 3.2, [title], tsize, font="Roboto Medium", align=PP_ALIGN.CENTER,
             highlight=spec.get("highlight"), anchor=MSO_ANCHOR.MIDDLE)
        sizes.append(tsize)
        y = 6.8
    else:
        tsize, ok = fit_size([title], width, 1.5, start=48 if lay != "chapter break" else 44)
        text(s, left, top, width, 1.6, [title], tsize, font="Roboto Medium",
             color=TEAL if lay == "chapter break" else GRAY, highlight=spec.get("highlight"))
        sizes.append(tsize)
        y = top + 1.75
    if minutes and lay in ("activity", "1_prompt"):
        text(s, left, y - 0.2, 5, 0.55, ["%d MIN" % minutes], 22, color=ORANGE, font="Roboto Condensed Medium")
        y += 0.55
    lead = spec.get("lead")
    if lead:
        lsize, ok = fit_size([lead], width if kind != "statement" else W - 4.4, 1.3, start=32)
        fits &= ok
        lx, lw = (left, width) if kind != "statement" else (2.2, W - 4.4)
        text(s, lx, y, lw, 1.4, [lead], lsize, font="Roboto Light",
             align=PP_ALIGN.CENTER if kind == "statement" else None)
        sizes.append(lsize)
        y += 1.4 if lsize > 26 else 1.1

    callout = spec.get("callout")
    safety = spec.get("box")
    bottom = 12.9 - (1.3 if callout else 0) - (1.9 if safety else 0)
    items = spec.get("items", [])
    tiles = spec.get("tiles", [])
    if tiles:
        n = len(tiles)
        gap = 0.35
        tw = (width - gap * (n - 1)) / n
        th = bottom - y
        heads = [t.get("head", "") for t in tiles]
        bodies = [t.get("text", "") for t in tiles]
        hsize, ok1 = fit_size([max(heads, key=len)], tw - 0.5, 1.2, start=32)
        bsize, ok2 = fit_size([max(bodies, key=len)], tw - 0.5, th - 1.6, start=28)
        fits &= ok1 and ok2
        for i, t in enumerate(tiles):
            x = left + i * (tw + gap)
            box(s, x, y, tw, th, PALE)
            box(s, x, y, tw, 0.12, TEAL if i % 2 == 0 else NAVY)
            text(s, x + 0.25, y + 0.35, tw - 0.5, 1.3, [t.get("head", "")], hsize, color=TEAL,
                 font="Roboto Condensed Medium")
            text(s, x + 0.25, y + 1.6, tw - 0.5, th - 1.8, [t.get("text", "")], bsize)
        sizes += [hsize, bsize]
    elif items:
        size, ok = fit_size(items, width, bottom - y, start=32)
        fits &= ok
        if kind == "steps":
            pre = lambda i: "%d.  " % (i + 1)
            pc = ORANGE
        elif kind == "questions":
            pre = lambda i: "?  "
            pc = NAVY
        else:
            pre = lambda i: "•  "
            pc = TEAL
        text(s, left, y, width, bottom - y, items, size, prefix=pre, prefix_color=pc,
             color=NAVY if kind == "questions" else GRAY)
        sizes.append(size)
    yb = bottom + 0.15
    if callout:
        b = box(s, left, yb, width, 1.05, ORANGE)
        csize, ok = fit_size([callout], width - 0.6, 0.9, start=26)
        fits &= ok
        text(s, left + 0.3, yb + 0.05, width - 0.6, 0.95, [callout], csize, color=WHITE,
             font="Roboto Medium", anchor=MSO_ANCHOR.MIDDLE)
        sizes.append(csize)
        yb += 1.3
    if safety:
        box(s, left, yb, width, 1.7, WHITE, line_color=NAVY)
        ssize, ok = fit_size([safety.get("label", "") + " " + safety.get("text", "")], width - 0.6, 1.5, start=22)
        fits &= ok
        text(s, left + 0.3, yb + 0.1, width - 0.6, 1.5, [safety.get("text", "")], ssize, color=NAVY,
             prefix=lambda i: safety.get("label", "DATA SAFETY") + "   ", prefix_color=NAVY)
        sizes.append(ssize)
    if spec.get("visual_todo"):
        text(s, left, 13.05, width, 0.45, ["VISUAL TO ADD: " + spec["visual_todo"]], 10, color=LIGHT, font="Arial")
    s.notes_slide.notes_text_frame.text = notes
    return s, {"body_pt": min(sizes) if sizes else None, "fits": fits}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True)
    ap.add_argument("--module", required=True, type=int)
    ap.add_argument("--half-day", action="store_true")
    ap.add_argument("--version", default="1")
    ap.add_argument("--template", default=REFERENCE)
    a = ap.parse_args()
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "courses", a.course)
    root = os.path.normpath(root)
    mdir = os.path.join(root, "modules", "m%d" % a.module)
    md = ""
    for f in ("course-open.md", "module.md"):
        p = os.path.join(mdir, f)
        if os.path.exists(p):
            md += open(p, encoding="utf-8").read() + "\n"
    notes = {s["id"]: s["notes"] for s in course_model.slides(md)}
    minutes_md = {s["id"]: (s["minutes"], s["minutes_half"]) for s in course_model.slides(md)}
    plan = json.load(open(os.path.join(mdir, "slides.json"), encoding="utf-8"))
    title = re.search(r"^\s*title:\s*(.+)$", open(os.path.join(root, "spec.yaml"), encoding="utf-8").read(), re.M).group(1)
    os.makedirs(os.path.join(root, "build"), exist_ok=True)
    code = COURSE_CODES.get(a.course, a.course.upper())
    out = os.path.join(root, "build", "%s_m%d%s_DRAFT_v%s.pptx" % (code, a.module, "_half" if a.half_day else "", a.version))
    tmp = out + ".tmp.pptx"
    clean_copy(a.template, tmp, title, "Workbook and templates in your course materials", "27.1")
    prs = Presentation(tmp)
    os.remove(tmp)
    by_name = {l.name: l for m in prs.slide_masters for l in m.slide_layouts}
    W = prs.slide_width / 914400
    report = []
    for spec in plan["slides"]:
        sid = spec["id"]
        if sid in minutes_md:
            spec.setdefault("minutes", minutes_md[sid][0])
            spec.setdefault("minutes_half", minutes_md[sid][1])
        _, r = render_slide(prs, by_name, W, spec, notes.get(sid, ""), a.module, a.half_day)
        r.update({"id": sid, "title": spec.get("title"), "layout": spec.get("layout"),
                  "minutes": spec.get("minutes_half" if a.half_day else "minutes", 0),
                  "has_notes": bool(notes.get(sid))})
        report.append(r)
    prs.save(out)
    json.dump(report, open(out.replace(".pptx", ".json"), "w"), indent=1)
    bad = [r["id"] for r in report if not r["fits"]]
    print("wrote %s: %d slides, %d minutes. Too dense at 18 pt: %s"
          % (out, len(report), sum(r["minutes"] or 0 for r in report), ", ".join(bad) or "none"))


if __name__ == "__main__":
    main()
