#!/usr/bin/env python3
"""Read a module file (courses/<course>/modules/m<N>/module.md or course-open.md).

The module file is the course model for one module. The deck, workbook and LD spec
renderers read it through this file, so they all see the same content.

Functions:
- sections(text): top-level "## " sections, as {title: body}.
- slides(text): slide specs from "### Slide" blocks (layout, minutes, on-slide text,
  visual intent, sources, notes).
"""
import re

SLIDE_HEAD = re.compile(r"^### Slide ([0-9A-Za-z.]+):\s*(.+)$", re.M)


def sections(text):
    """Return an ordered list of (title, body) for each '## ' section."""
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    out = []
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1]))
    return out


def find_section(text, startswith):
    for title, body in sections(text):
        if re.sub(r"^\d+\.\s*", "", title).lower().startswith(startswith.lower()):
            return title, body
    return None, ""


def _field(block, name):
    m = re.search(r"^- %s:\s*(.*)$" % re.escape(name), block, re.M)
    return m.group(1).strip() if m else ""


def _minutes(value):
    """'3 (half day 4)' -> (3, 4). '8' -> (8, 8)."""
    nums = re.findall(r"\d+", value)
    if not nums:
        return 0, 0
    full = int(nums[0])
    half = int(nums[1]) if "half" in value and len(nums) > 1 else full
    return full, half


def slides(text):
    heads = list(SLIDE_HEAD.finditer(text))
    out = []
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        block = text[h.end():end]
        # A slide block ends at the next "## " section too.
        nxt = re.search(r"^## ", block, re.M)
        if nxt:
            block = block[: nxt.start()]
        notes = ""
        m = re.search(r"```[a-z]*\n(.*?)```", block, re.S)
        if m:
            notes = m.group(1).rstrip()
        full, half = _minutes(_field(block, "Minutes"))
        out.append({
            "id": h.group(1),
            "title": h.group(2).strip(),
            "layout": _field(block, "Layout"),
            "minutes": full,
            "minutes_half": half,
            "on_slide": _field(block, "On-slide text"),
            "visual": _field(block, "Visual intent"),
            "sources": _field(block, "Sources"),
            "notes": notes,
        })
    return out
