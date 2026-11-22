# Development brief: Advanced AI for Market Research

- Course id: `market-research`. Stage 2 draft by the course planner, 2026-11-22. Revised once (v0.2) after `outline/critic-report.md`. See the revision log at the end.
- Purpose: answer the 5 questions from "How the Capability Standards Drive Learning Development" (PRD decision 40) for the course and for each module.
- The 5 questions: (1) What capability, and which skills? (2) What can the learner do? (3) How far: Introduce, Develop, Apply or Validate? (4) What evidence shows it? (5) What experience gets them there?
- The Capability Standards Workbook is not available. This brief does not name a standard, a skill or a competency. Where a name is needed, it says **Dan to name**. The working descriptions in plain words are placeholders only.
- Offering intent for every module: **Develop and Apply** (decision 41). The workshops Introduce. Validate stays with the instructional designers (decision 29).
- Companion file: `spec.yaml` (module plan, minutes, agenda).

## 1. Course level

| Question | Answer |
| --- | --- |
| 1. Capability and skills | Capability: **Dan to name**. Working description: turn market evidence into product decisions, with an AI agent that does the routine work and a PM who manages it. Skills: **Dan to name**. Working descriptions: run interview synthesis at scale; run win/loss; route feedback to market problems; keep an alternatives map; answer stakeholders from past research. Pragmatic Framework 2027 category: Market. Focus areas: Market Problems, Win/Loss Analysis, Competitive Landscape |
| 2. What the learner can do | Build one agent from a template. Write and tune its brief. Set quality checks and hand-off rules. Decide each flag report item. Audit a sample against sources. Connect jobs so one output feeds the next. Set the evidence bar and defend decisions with sourced evidence |
| 3. How far | Develop and Apply. Develop: learners build the skill through a demo, a lab, a planted error and feedback in each module, with more complex input each time. Apply: learners use their own work first and make the judgment calls themselves. The warning on the planted error fades, so by module 5 they find it with no hint |
| 4. Evidence | Per lab (decision 42): the tuned brief, the flag report decisions and the audit findings. Plus the match rate table (module 2), the hand-off rule (module 4) and the send, change or hold decisions (module 5). At the end: the saved agent with five jobs and a Monday plan with an audit date |
| 5. Experience | One course agent that grows in each module (house rule 12). An autonomy ladder: hand-run batch, recurring run with a flag report, hand-off between jobs, an agent that faces other people. 40% instructor-led and 60% hands-on per module. Own work first, one fallback case company. Step cards on Claude, ChatGPT, Copilot agent builder and Gemini. Breakout rooms by platform. Catch-up kit per module |

### Course themes (from Dan)

1. There is no magic number. The agent reports evidence. The PM's judgment sets the bar.
2. Be great at product management before you are great at AI.
3. Win/loss is the big aha. Most teams do not get this data.

### Where the course starts and stops

| Not taught here (known from elsewhere) | Taught here |
| --- | --- |
| One-pass AI synthesis, the quote check, frequency vs intensity (PDW-AI) | Running an agent on batches, the log over time, flags, audits and tuning |
| Persona creation (BPW-AI, Market core course) | Labeling sources by persona and segment |
| Public competitor watching, scheduled-task setup (CAW-AI) | Alternatives map from the team's own deals. Schedule only as stretch, new slides |
| Boundaries and guardrails as first taught (AI Agents course) | The same ideas applied to an agent that answers stakeholders, with new slides (decision 33) |
| Prompt structure JOB AND CONTEXT, RULES, OUTPUT (PRW-AI) | Referred to as known. The brief adds checks, hand-off rules and audits |
| Market sizing and concept tests | Moved to the Product Strategy and Planning course |

## 2. Module level

### Module 1. Run your first batch and manage it by flags (row mr-wf-01, folds 05)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Dan to name**. Working description: run interview synthesis at scale with an agent, and manage it by checks and flags |
| 2. What the learner can do | Build the agent from the template. Decide each flag. Audit 3 insights against the interviews. Add a rule to the brief and rerun |
| 3. How far | Develop and Apply. First build, so a fast-start card supports new builders. Planted error warning: **told** |
| 4. Evidence | Tuned brief (v1 to v2: the learner writes the PM's bar and one new rule; the template already has "count interviews, not quotes", as in worked example v3). Flag report decisions for batch 1. Audit findings for 3 insights |
| 5. Experience | Opening build check, then a live demo on one platform, then the lab on own interviews or case batches 1 and 2. Planted error: one vocal buyer looks like strong evidence. The agent writes "meets the PM's bar", "emerging" or "single source", never "pattern". Only the PM promotes an insight to "pattern". Debrief: who sets the bar (no magic number), and Dan's test: can you predict that the next buyer of this persona will raise it? Rung 1, hand-run batch. 70 minutes |

### Module 2. Win/loss and the match rate (row mr-wf-02)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Dan to name**. Working description: run win/loss on decided deals and report sales reasons against buyer reasons. Focus area: Win/Loss Analysis |
| 2. What the learner can do | Add a win/loss job. Label each deal "interview" or "CRM only". Read the match rate. Audit source labels. Frame findings for sales without blame |
| 3. How far | Develop and Apply. Two inputs joined for the first time. Planted error warning: **hint** ("Audit before you approve") |
| 4. Evidence | Match rate table and the learner's read of it. Flag report decisions. Audit findings for 2 deals. The brief change |
| 5. Experience | Pragmatic program rules (10 or more deals, interviews 2 to 4 weeks after the decision, by someone outside sales). Lab on own deal export or the case CRM export. Planted error: a CRM-only "price" reason leaks into buyer findings. Debrief is the aha moment. Rung 1, two sources |

### Module 3. The weekly run: read flags, not every item (row mr-wf-03, folds 04)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Dan to name**. Working description: route high-volume feedback to market problems and manage the run by flags and a sample |
| 2. What the learner can do | Add a weekly feedback job counted by unique account. Write a "no fit" rule. Audit 10 items and the "no fit" group. Decide which moves need discovery |
| 3. How far | Develop and Apply. High volume: the learner reads flags and a sample, not each item. Planted error warning: **hint** |
| 4. Evidence | Flag report decisions for week 2. Audit findings. The "no fit" rule added to the brief |
| 5. Experience | Two runs (week 1, week 2) on own feedback or case exports. Planted error: forced fit hides a new problem. Stretch: schedule where verified, or a survey wave with the three tests (urgent, pervasive, willing to pay). Rung 2, recurring run |

### Module 4. First hand-off: the alternatives map from your own deals (row mr-wf-10)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Dan to name**. Working description: keep an alternatives map from the team's own evaluator and deal evidence. Focus area: Competitive Landscape |
| 2. What the learner can do | Connect the win/loss job to a map job. Write a hand-off rule. Trace 3 entries to interviews and deals. Choose the alternative to beat in one segment |
| 3. How far | Develop and Apply. First hand-off between jobs. Planted error warning: **hint** |
| 4. Evidence | The hand-off rule as written and as fixed. Audit findings for 3 traced entries. The alternative to beat, with its evidence |
| 5. Experience | Dan's real example in the talk track (decision f), scripted so any instructor can tell it. Lab on own driver log or case data. Planted error: CRM says "Rimecore", buyer kept the spreadsheet (case deal D-3108). Rung 3, hand-off between jobs |

### Module 5. The agent answers stakeholders, and you stay accountable (row mr-wf-09, folds 07)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Dan to name**. Working description: answer stakeholder questions from past research with sourced, dated answers, and keep the PM accountable for validation |
| 2. What the learner can do | Add an answer job with citations, dates, segments and a "what we do not know" line. Write rules for what the agent may say. Send, change or hold each answer. Judge status proposals, given by segment. A claim about one segment needs the PM's bar met inside that segment |
| 3. How far | Develop and Apply. The agent faces other people. Planted error warning: **none** |
| 4. Evidence | Send, change or hold decisions for 3 answers. Audit findings for one cited answer. The hand-off rules. Validated-status decisions |
| 5. Experience | Lab on own logs and past reports or case reports. Planted error: an old study for another segment presented as "buyers want". Close: Monday plan and kit-final. Rung 3 plus, agent that faces other people. 65 minutes. No hint: the success check before the lab names no error |

## 3. Notes for an instructor who did not build the course (decision 45)

1. Demo on one platform only. Step cards in the workbook carry each platform. Breakout rooms group learners by platform.
2. Say "flags", "flag report" and "hand-off rules". Do not say "exceptions" or "escalations".
3. Tell each story as one heard from client teams, executives or Pragmatic's work with companies. Never as your own experience (decision 43).
4. Reveal the planted error only in the debrief. Ask which check or audit found it. The success check before each lab is general. The error-specific check is in the debrief only.
5. A learner who falls behind rebuilds from the module's catch-up kit in about 5 minutes.

## 4. Open items for this brief

| # | Item | Owner |
| --- | --- | --- |
| 1 | Name the capability and the skills for the course and each module. The workbook is not available | Dan |
| 2 | Confirm offering intent Develop and Apply for all five modules | Dan |
| 3 | Confirm the learner evidence list is what the ID team can score in beta (decision 29) | Dan with the ID team |
| 4 | Confirm the PA-01 wording: the agent writes "meets the PM's bar"; only the PM promotes to "pattern" (spec OI-13) | Dan |
| 5 | Confirm the segment rule: a claim about one segment needs the PM's bar met inside that segment. Course rule or case choice only (spec OI-15) | Dan |
| 6 | Confirm "count interviews, not quotes" back in the template, to match worked example v3 (spec OI-14) | Dan |

## 5. Revision log (v0.2, 2026-11-22)

One revision after `outline/critic-report.md`. Edited files: `spec.yaml` and this brief. The case builder fixed the case files before this revision. This revision did not edit them.

### Must fix

| Id | Result | What changed, or why not |
| --- | --- | --- |
| M1 | Fixed in case | CSV notice line removed by the case builder. Notice is in `case/README.md`. No spec change |
| M2 | Fixed in case | The bar is in `case/company.md` as "the Larkspan Head of Product's bar for this study". The spec `fallback_case` points to it |
| M3 | Fixed in case and spec | Case gives lab 5 proposals by segment. The spec adds `course_agent.segment_rule`, a lab 1 template hand-off rule, a lab 5 hand-off rule and per-segment status proposals. Open item OI-15 asks Dan to confirm |
| M4 | Fixed | Agent statuses are "meets the PM's bar", "emerging" and "single source". Only the PM promotes to "pattern". Changed: glossary (new "meets the PM's bar", "pattern", and "single source and emerging" rows), lab 1 success check, lab 1 planted error text, module 1 row in this brief. Open item OI-13 asks Dan to confirm |
| M5 | Fixed | Knowledge files ship as `.md` plus a `.txt` copy for Copilot (the case has them). Removed the `.docx` and `.xlsx` copies the case does not ship. Added Gate 2 proof item G2-PF-01 for Copilot file types and G2-PF-02 for `.csv` in chat |
| M6 | Fixed, with a Gate 2 risk | `copilot_no_license_fallback` defines each module: core brief plus one job card plus one knowledge file under 8,000 characters, run files and logs in chat. Proof patterns P1, P2 and P3 now run the fallback for every module. G2-PF-03 tests the longest paste (evidence pack, about 12,400 characters). G2-PF-05 measures each kit. Risk plan in OI-16 |
| M7 | Fixed | Lunch is 60 minutes. Module 1 from 80 to 70 minutes, module 5 from 70 to 65. Math: modules 70 + 70 + 60 + 55 + 65 = 320. Plus open 25 and close 15 = 360 teaching minutes. Plus breaks 15 + 15 and lunch 60 = 90. Total 450 minutes = 7.5 hours. Instructor-led 148 of 360 = 41 percent. Half days are now 190 and 225 minutes |

### Should fix

| Id | Result | What changed, or why not |
| --- | --- | --- |
| S1 | Fixed in case | "Nothing from 1 interview is called a pattern" is now the case Head of Product's choice. Dan's test is in the module 1 debrief arc |
| S2 | Fixed | Each lab now has a general `success_check` (outputs and manager actions) and a `debrief_check` for the error. Lab 5 success check names no error. Card steps name no error |
| S3 | Fixed | `uploads_per_lab` now uses the per-lab counts in `case/company.md` (6, 5, 5, 4, 3 files; peak 3 to the agent and 3 in chat; 12 knowledge files at the end). Added G2-PF-02 (Copilot chat) and G2-PF-04 (Gemini chat and skill). No limit numbers invented. Log save card and P2 test say how the log persists on each platform |
| S4 | Fixed | `fallback_case` names Larkspan Systems, points to `case/`, lists files per lab and the instructor files |
| S5 | Fixed | Cards for modules 3, 4 and 5 now have 6 steps, 1 action each. The rerun after the fix moves to the debrief. Objective "practiced in" lines updated |
| S6 | Fixed in case | F-1307 has no night reference. Spec has no change |
| S7 | Fixed | Template quality checks include "count interviews, not quotes" again, to match v3. The PM's bar stays blank. OI-14 records it for Dan |
| S8 | Fixed in case | Stretch edge reasons are in case files only. Spec has no change |
| Lab 4 text | Fixed | "Competitor X" replaced with Rimecore (case deal D-3108) in the spec and this brief |

### Notes

| Id | Result | What changed, or why not |
| --- | --- | --- |
| N1 | Open item | Module 4 stays 55 minutes. A longer module 4 breaks the 7.5-hour math. OI-17 asks Dan |
| N2 | Fixed | Module 2 `program_rules` and debrief say the PA-04 minimum of 10 counts decided deals |
| N3 | Fixed | Module 3 stretch refers to urgent, pervasive and willing to pay as known from PDW-AI. No new slide |
| N4 | Open item | No case edit in this revision. OI-18 gives Dan two options for an internal PM item |
| N5 | Open item | Instructor guide note in Stage 3 (OI-19). The P07 result holds |
| N6 | Open item | Instructor guide note in Stage 3 (OI-19) |
| N7 | No action | The critic asks for no action. Larkspan is not a close copy of FieldPro |
