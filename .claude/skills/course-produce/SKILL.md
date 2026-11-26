---
name: course-produce
description: Stage 4 of the course builder. Renders one approved module into the deck (.pptx, full and half day), the learner workbook and the LD specs (.docx and .pdf), runs the QA agent, and publishes the Gate 4 packet. Use when Dan says "run Stage 4 for <course> module <N>" or "/course-produce <course> <N>".
---

# Course produce (Stage 4)

Input: a course id and a module number. Folder: `courses/<course>/`. Source of truth: `docs/PRD.md`, sections "Workbook, deck, talk track, and Pragmatic style", "Quality bar" and "What each gate checks". If this file and the PRD differ, the PRD wins. Tell Dan.

Say what you do and why at each step, in one or two plain sentences. Dan is learning Claude Code. The Claude Code idea for this phase: scripts do the exact work (layouts, fonts, checks) the same way every time. Agents do the judgment work (what to cut to fit a slide, what looks wrong on a page).

## Before you start (stop if a check fails)

1. `status.yaml`: the module entry in `gate_3_modules` has status `content_approved` or `approved`. Only Dan sets this.
2. The reference deck is in `/mnt/project-files/course-builder/reference/AI_Agents.26.07.02.pptx`. Never edit it. The script works on a copy.
3. Tools: `python3 -c "import pptx, docx"`, `soffice --version`, `pdftoppm -v`.

## Steps

| # | Who | Runs | Writes |
| --- | --- | --- | --- |
| 1a | `deck-renderer` agent | In parallel with 1b | `modules/m<N>/slides.json`, `build/<CODE>_m<N>[_half]_DRAFT_v<V>.pptx` and `.json` sidecar |
| 1b | `scripts/render_workbook.py` | Script | `build/<CODE>_m<N>_Workbook_DRAFT_v<V>.docx` and `.pdf` |
| 1c | `scripts/render_ld_spec.py` | Script | `build/<CODE>_m<N>_LD_lab<N>_DRAFT_v<V>.docx` and `.pdf` (module 1 also: build check LD spec) |
| 2 | `qa-agent` | After 1a to 1c | `build/<CODE>_m<N>_QA_report.md` |
| 3 | Fix round (once) | Deck renderer for slide fails. Script fix for layout fails | New renders, QA rerun |

- Commit `slides.json` and script fixes after each step. `build/` is not in git.
- Copy the outputs to `/mnt/project-files/course-builder/<course>/build/` so Dan can open them.
- A content problem found in Stage 4 goes back to the module file only with Dan's yes. List it for Dan.
- Post a short status to Dan after each step.

## Gate 4 packet

1. Publish a Claude Doc: QA report summary (pass and fail counts), the visual review, the designer list, links to the files, and what Dan must check (look at the deck at Zoom size, open one template copy box, read the LD spec). Fallback: a Word file in `build/gates/`.
2. Record it in `status.yaml` under `gate_4` with the module, status `in_review`, the doc link and the version.
3. When Dan approves, set status `approved` with the date, and add fingerprints for `slides.json`.
4. Add a row to `logs/hours-log.csv`.
