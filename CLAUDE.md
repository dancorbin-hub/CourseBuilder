# CourseBuilder

This repo builds Advanced AI courses that Dan Corbin licenses to Pragmatic Institute. Claude Code skills and subagents do the research, outline, modules and production. Dan approves each stage at a gate.

The approved PRD is `docs/PRD.md`. It is the source of truth. If this file and the PRD differ, the PRD wins. Tell Dan about the difference.

## Who you work for

- Dan is the only user, the SME and the final decision maker. He owns the course IP.
- Dan is new to large Claude Code projects. At each step, say what you do and why, in plain words.
- Push back when you disagree. Flag weak reasoning and assumptions. No flattery or filler.

## Writing rules (all output)

1. Docs, summaries and status reports use ASD-STE100 Simplified Technical English: short sentences (20 words or fewer for directions), one instruction per sentence, active voice, common words.
2. Do not use em dashes or en dashes. Use a period, a comma, a colon or "to".
3. Prefer tables, numbered steps and bullets to long prose.
4. Audience for course content: experienced PMs. Use practical, real-world examples. Explain jargon.

## House rules for course content

1. Every module is built on one real PM workflow and the bottleneck it removes.
2. Learners build skills, projects and agents. Not only prompts. No custom GPTs or Google Gems.
3. Every lab has a core path and a step card for Claude, ChatGPT, Microsoft Copilot agent builder and Gemini (skills, not Gems).
4. Learners use their own work first. One fallback case company serves the whole course.
5. 40% instructor-led, 60% hands-on per module.
6. Slide notes: `POINT:` then `Talk Track:`. No `[AI USE CASE TT]` block.
7. Every lab has a data safety note: no client data, HIPAA health data or PII in a tool the company has not approved.
8. Clarity first: 6 steps or fewer per step card, 1 action per step, 20 words or fewer per sentence.
9. Never repeat a slide, or the same concept with the same agent in the same exercise, across courses. See `shared/registry/`.
10. Do not teach the Playbook method. Playbook markdown files can be workbook handouts.
11. Do not reuse the agents from Dan's workshops (for example CAW-AI). Course labs must be clearly stronger builds.
12. Learners are agent managers: the agent does the workflow; the learner writes the brief, sets checks, reviews exceptions and audits.
13. Each lab has a planted AI error. The warning fades: told in lab 1, a hint in middle labs, no hint in the last lab.
14. Boundaries and guardrails can be taught again when learners build agents, with new slides.

## Research rules

1. A statistic needs a primary source.
2. Any other factual claim needs 2 independent sources. Two articles that repeat one study count as one source.
3. A tool feature claim needs one dated vendor doc.
4. Statistics and studies must be published in 2026 or later (the courses launch in 2027). Do not use older ones.
5. Flag any other source older than 12 months. Dan decides if it stays.
6. Look for examples in software, FinTech, health care, manufacturing, hardware, services and internal product management. Hardware and internal product management are a priority. Record a gap when none exist. A gap is not a failure.
7. Tag each workflow with its Pragmatic Framework 2027 category and focus area.

## Gates and approvals

| Gate | Dan approves | Where |
| --- | --- | --- |
| 1 | Research brief and workflow inventory | Claude Doc |
| 2 | Course spec and syllabus, then Pragmatic reviews | Claude Doc |
| 3 | Each module, one at a time, after the card test | Claude Doc |
| 4 | Final QA of deck, workbook and LD specs | Claude Doc |

- Do not start a stage until its gate before is approved in `courses/<course>/status.yaml`.
- Ask before rework. Do not change an approved item without Dan's yes. List what you want to change and wait.
- Apply Dan's gate comments to the course files in the repo, not to the doc. The repo is the source of truth.
- Fallback when Claude Docs fails: write a Word file per gate in `courses/<course>/build/gates/`.

## Repo layout

```
CLAUDE.md                  this file
docs/PRD.md                approved PRD (export of the Claude Doc)
docs/gate-reviews.md       how gate reviews work, and the Phase 0 test
.claude/skills/            one folder per skill (course-research, course-outline, ...)
.claude/agents/            one file per subagent role
shared/registry/           cross-course registry and series canon
shared/templates/          schemas the agents fill (workflow row, ...)
shared/pragmatic-template/ Pragmatic brand assets (Phase 4). Not Dan's content
courses/<course>/
  status.yaml              stage, gate approvals, fingerprints
  research/                sources, claims, workflow inventory, platform matrix
  spec.yaml                locked course spec (Gate 2)
  modules/                 one file per module
  case/                    fallback case data
  build/                   rendered .pptx, .docx, .pdf (not in git)
logs/hours-log.csv         Dan's active hours
scripts/                   helper scripts the agents and Dan call
```

## Hours log

After each work session on a course, add a row to `logs/hours-log.csv`. Run `python3 scripts/estimate_hours.py --since <date>` to estimate Claude Code session time. Dan adds testing and review time by hand. Tool-build hours use `activity=tool-build` and do not count toward the course target.

## Source files

Reference decks are large and are Pragmatic or Dan material. They are not in git. They are in the project files folder `course-builder/reference/` (style reference `AI_Agents.26.07.02.pptx`, Pragmatic sources in `pragmatic-sources/`). Never edit an original. Edit copies only, named `<COURSE>_<version>_DRAFT_vN.pptx`.
