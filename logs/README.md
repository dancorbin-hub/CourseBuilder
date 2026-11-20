# Hours log

The main time goal is Dan's active hours per course, compared with the hand-built baseline (PRD decision 28).

| Item | Value |
| --- | --- |
| Baseline | About 160 hours for AI Agents for Product Professionals, built by hand |
| Target, course 1 (proposed) | 80 hours or less |
| Target, courses 2 and 3 (proposed) | 50 hours or less each |
| Not counted | Time to build the tool (`activity=tool-build`) |

## Columns in `hours-log.csv`

| Column | Values |
| --- | --- |
| date | YYYY-MM-DD |
| course | `market-research`, `strategy-planning`, `market-launch`, or `all` |
| phase_or_stage | `phase-0` to `phase-5` for tool build; `stage-1` to `stage-4` or `refresh` for course work |
| module | Module number for Stage 3 and 4 work. Empty for other work |
| activity | `tool-build`, `course-work`, `gate-review`, `testing` |
| hours | Decimal hours, for example 1.5 |
| source | `session-estimate` (from the script) or `manual` (Dan types it) |
| notes | Short text |

## How to log

1. After a work session, run `python3 scripts/estimate_hours.py --since <date>` on your computer.
2. Add one row per day with `source=session-estimate`.
3. Add testing time (card tests, platform proofs) and gate review time by hand, with `source=manual`.

The script sees only time in Claude Code. It does not see time in a Claude Doc or on a test platform. That is why manual rows are necessary.
