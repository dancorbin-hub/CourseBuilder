# Method library: managing the strategy course agent

Course: product-strategy-and-planning. Stage 1, track 2. Written 2026-11-22.

Platform facts come from `platform-matrix.yaml` (ids in brackets). Each new feature there is "not verified" until the Verifier checks it.

## What this file is

- These are design methods for an agent manager. They are not research findings.
- No study was opened in this run that shows one method works better than another. See gaps.md, Track 2.
- Market Research methods M1 to M11 still apply. This file refers to them and does not repeat them. Source: `courses/market-research/research/methods.md`.
- New methods S1 to S10 cover what strategy work needs: numbers, weights, scenarios and refresh.

## Reused methods (by reference)

| Id | Method | Change for this course |
| --- | --- | --- |
| M1 | The brief | Add 2 headings: "Decisions the PM owns" and "Numbers rules". Keep the brief under 6,000 characters (Copilot 8,000 limit, mb-01) |
| M2 | Quality checks | Add numeric checks (S5, S8). A self-check can pass and still be wrong |
| M3 | Hand-off rules | Add the human-owned decisions from S9 |
| M4 | Flag report | Add 3 flag types: untraced number, rank flip, scorer gap |
| M5 | Audit | Audit numbers, not only text: pick 3 numbers at random and trace each to its source |
| M6 | Tuning | Same. Add one dated change log line per tuning |
| M7 | Runs over time | Strategy reruns are quarterly or event-driven. See S7 |
| M8, M9 | Schedules and triggers | Stretch only. CAW-AI already teaches scheduled tasks. See S10 |
| M10 | Catch-up kit | Same. The kit adds the scoring sheet (.xlsx and .csv copies) and the assumption register |
| M11 | Planted error | Same fading warning. Strategy errors are numeric. See "Planted error ideas" |

## How the four builds hold the new parts

| Part | Claude | ChatGPT | Copilot agent builder | Gemini skill |
| --- | --- | --- | --- | --- |
| Run math in code | Code execution, all plans (cl-fo-06). Must be on | Data analysis, Python on uploaded files (cg-11). Plans not named | Code interpreter, all 3 license states (mb-04, mb-13) | Not documented. Skill scripts can be uploaded, but no doc says they run (gm-11) |
| Read the scoring sheet | XLSX needs code execution on. CSV always. Project file 30 MB (cl-up-10) | .xls, .xlsx, .csv, about 50 MB (cg-03, cg-11) | Upload in chat: Excel, CSV/TSV (mb-13). As knowledge: .xlsx only, one sheet, 30 MB (mb-14) | 10 files per prompt, 100 MB (gm-10). Skill files 100 MB total (gm-01) |
| Spreadsheet file out | .xlsx with formulas, 30 MB (cl-fo-06) | ChatGPT Work, Plus and up, not Free or Go (cg-09, cg-10). Plain chat download not documented | Excel file, session only (mb-11) | Gemini app .xlsx, .csv, Sheets, one file per prompt (gm-09). From a skill: unproven |
| Web search for refresh | All plans. Team and Enterprise need owner opt-in (cl-ws-08) | All plans (cg-13) | 4 URLs or "Search all websites", all license states (mb-12, mb-03) | Not documented for skills. Deep Research does not work in skills (gm-06) |
| Deep research | Research, paid plans only (cl-rs-09) | Varies by plan (cg-12) | Not checked | Not in skills (gm-06) |
| Schedule (stretch) | Cowork tasks, paid plans (cl-sc-07) | Scheduled tasks; Work adds schedule, trigger, monitor (cg-06, cg-09) | Scheduled workflows rollout to mid-December 2026 (mb-06) | A skill can be named in a scheduled action (gm-12); personal accounts (gm-07) |

## New methods

### S1. Scoring model as a file the PM owns

- **What the learner does:** Gives the agent a scoring sheet with criteria, 1 to 5 scales and weights. The agent fills scores and evidence. The PM owns the weights.
- **Why:** Workbook skill 2.2 says weights and final priorities stay human-owned. A file makes that visible.
- **Rule for the brief:** "Do not change weights. Do not change the criteria. Put each score next to its evidence and source."
- **Where it works:**
  - Claude: core lab yes. Output .xlsx with live formulas (cl-fo-06).
  - ChatGPT: core lab yes, as an on-screen table from data analysis (cg-11). File output with formulas needs Work (cg-10), so Plus or higher.
  - Copilot: core lab yes. Upload the sheet in chat for each run. Download the output in the same session (mb-11, mb-13).
  - Gemini: core lab yes, with a condition. Gemini app file output exists (gm-09). From a skill, test at Gate 2.
- **No-repeat note:** Focus 28.01 teaches the 4-attribute scoring table as a one-pass activity. Here the PM manages an agent that rescores over time. Use different criteria and a different case.

### S2. Sensitivity runs

- **What the learner does:** Asks the agent to move each weight up and down by a set step (for example plus or minus 10 points). The agent reports which ranks change.
- **Why:** Workbook skill 2.2 names "run sensitivity tests". A ranking that flips on a small weight change is a weak ranking.
- **Flag report line:** "Rank flip: item, weight changed, old rank, new rank."
- **Numbers rule:** The agent must compute in code or in spreadsheet formulas. It must not do arithmetic in prose.
- **Where it works:** Claude, ChatGPT and Copilot: core lab yes (code execution). Gemini: risk. No doc says a skill runs code (gm-11). Fallback to test: the Gemini agent writes a sheet with formulas, and the learner changes the weight cell.

### S3. Scenario runs

- **What the learner does:** Keeps an assumption register (assumption, value, source or owner, range). Asks for low, base and high scenarios. Each scenario changes only named assumptions.
- **Why:** Workbook 2.1 says "run scenarios". Workbook 2.4 says "simulate sequencing and dependency scenarios". Business cases (2.3) need cost and market ranges.
- **Quality check:** "Each scenario lists the assumptions it changed. All other values match base."
- **Where it works:** All 4 platforms as text. Math needs code (see S2 for Gemini risk). Core lab: yes on Claude, ChatGPT, Copilot.

### S4. Consistency check between scorers

- **What the learner does:** Gets 2 independent score sets for the same items. Options: the agent and the PM; 2 stakeholders; or 2 fresh agent runs. The agent lists each item where scores differ by 2 or more points, with both reasons.
- **Why:** Workbook 2.2 names "surface scoring inconsistencies". The gap is the decision input. The agent must not average it away.
- **Hand-off rule:** "When scorers differ by 2 or more, stop. Show both reasons. The PM decides."
- **Platform catch:** A second agent run must not see the first run.
  - ChatGPT: a project with default memory can draw on other chats in that project (cg-14). Run the second scorer in a new chat outside the project, or use project-only memory.
  - Claude: chats in a project do not share context (cl-pj-01). A new chat is enough.
  - Copilot and Gemini: start a new chat. Memory behavior not checked in this run.
- **Where it works:** All 4. Core lab: yes.

### S5. Trace-to-source for numbers

- **What the learner does:** Requires a source tag on every number in the business case or market size: source id and date, or "assumption" with an owner.
- **Why:** Workbook 2.3 says "data and calculations stay auditable". The Market Research planted error "fake triangulation" (mr-wf-06) shows the risk: 2 sources that repeat one study look like 2.
- **Quality checks:**
  1. Every number has a tag.
  2. Each source is dated. Flag a statistic older than 12 months.
  3. "Independent" sources must not cite the same original study.
- **Audit (M5):** Pick 3 numbers at random. Open each source. Check the number and the date.
- **Where it works:** All 4. Core lab: yes. ChatGPT search citations are optional on the page (cg-13), so the brief must ask for a link per number.

### S6. Assumption register and red-team pass

- **What the learner does:** Asks the agent to attack its own business case: list the 3 assumptions that most change the result, and what evidence would break each.
- **Why:** Workbook 2.3 names "find assumptions and risks, red-team the case".
- **Rule:** The red-team output goes in the flag report. The agent does not change the case on its own.
- **Where it works:** All 4. Core lab: yes. Text only, no code needed.

### S7. Refresh with web search

- **What the learner does:** Each quarter (or on a trigger event), the agent searches for new data on the market size inputs. It reports a "what changed" table: input, old value, new value, source, date.
- **Why:** Market sizes go stale. Carries mr-wf-06 ("refresh a sourced market size model").
- **Hand-off rule:** "A new number that moves the base case by more than the set threshold goes to the PM. The agent does not update the model." The PM sets the threshold (no magic number, Dan theme).
- **Where it works:**
  - Claude: web search all plans (cl-ws-08). Core lab yes, if the company turned it on.
  - ChatGPT: web search all plans (cg-13). Core lab yes.
  - Copilot: "Search all websites" or up to 4 named URLs (mb-12). Core lab yes.
  - Gemini skill: web search in a skill is not documented. Deep Research does not work in skills (gm-06). Fallback: the learner pastes or uploads the new source. Test at Gate 2.
- **Data safety note:** Web search sends the query outside the company. Do not put client names or unreleased product names in the search.

### S8. Commitment guard for roadmap narratives

- **What the learner does:** Adds a check: "Flag any date, 'will ship', or 'committed' that is not in the approved release plan."
- **Why:** Workbook 2.4: AI "must not turn uncertain direction into false delivery commitments". Focus 28.01: "the roadmap is the vision, the release plan is the promise".
- **Where it works:** All 4. Core lab: yes. Text check.
- **No-repeat note:** Focus has an optional "one roadmap, two audiences" AI activity. Here the new part is the check and the flag, not the tailoring.

### S9. Human-owned decisions list

- **What the learner does:** Writes the list of decisions the agent never makes. Starter list from the workbook: strategy choices (2.1), weights and final priorities (2.2), case approval (2.3), delivery commitments (2.4).
- **Why:** Workbook 2.1: "Strategy stays a forced-choice human decision."
- **Where it works:** All 4, as hand-off rules in the brief. Core lab: yes.

### S10. Schedules and triggers for refresh (stretch only)

- **Scope:** CAW-AI already teaches scheduled tasks. Teach only the new part: what the scheduled run reports (S7 table and flag report), not how to set a schedule.
- **Where it works:** See the table above. New in this run: a Gemini skill can be named in a scheduled action (gm-12). ChatGPT Work adds tasks that repeat, trigger or monitor (cg-09).
- **Catch:** A ChatGPT task in a project cannot read project files (cg-06). Copilot schedules run only for the creator and not for unpublished agents (mb-06).
- **Core lab:** No.

## Planted error ideas (for the Outline stage)

| Error | Method that catches it | Lab fit |
| --- | --- | --- |
| A weight changed by the agent "to make the ranking sensible" | S1 rule and audit | Scoring lab |
| A rank that flips on a 5-point weight change, reported as robust | S2 | Prioritization lab |
| Two "independent" market sources that cite one study | S5 | Business case lab |
| An arithmetic error in prose math (the model did not use code) | S2 numbers rule, M5 audit | Any numeric lab. Most likely on Gemini (gm-11), so check card parity at Gate 2 |
| A roadmap line that reads as a delivery date | S8 | Roadmap lab |

## Risks for the core path (new for this course)

1. **Gemini math.** No doc says a Gemini skill runs code (gm-11). Scoring and sensitivity labs need a tested fallback.
2. **ChatGPT file output.** Spreadsheet output is documented only through ChatGPT Work, which is not on Free or Go (cg-09). Dan's Market Research decision set "Go or Plus minimum". For file output labs, Go is not enough. Dan decides.
3. **ChatGPT memory.** Default project memory can leak run 1 into a "blind" run 2 (cg-14).
4. **Copilot session files.** Output files are lost when the session ends (mb-11). Code interpreter use of knowledge files is not documented (mb-13).
5. **Claude admin settings.** Code execution and web search can be off at the company level (cl-fo-06, cl-ws-08). Add both to the pre-class check.
6. **Claude upload size.** Two Claude pages disagree: 30 MB or 500 MB per chat file (cl-up-10). Use 30 MB.

## Sources

All sources, dates and check dates are in `platform-matrix.yaml`. Workbook text is from `stage-1-inputs.md`, section 2.
