# Development brief: Advanced AI for Market Research

- Course id: `market-research`. Stage 2 draft by the course planner, 2026-11-22. Revised once (v0.2) after `outline/critic-report.md`. Revised again (v0.3) for `outline/rework-brief-2.md` (Gate 2 comments). Revision 3 fixes the points from the critic recheck. See the revision logs at the end.
- Purpose: answer the 5 questions from "How the Capability Standards Drive Learning Development" (PRD decision 40) for the course and for each module.
- The 5 questions: (1) What capability, and which skills? (2) What can the learner do? (3) How far: Introduce, Develop, Apply or Validate? (4) What evidence shows it? (5) What experience gets them there?
- Capability and skill names come from the Capability Standards Workbook 2027, through `outline/capability-mapping.md`. Ids and names are copied exactly. Nothing is invented. Status: **proposed, Dan to confirm** (Gate 2 decision 7).
- Offering intent for every module: **Develop and Apply** (decision 41). The workshops Introduce. Validate stays with the instructional designers (decision 29).
- Companion files: `spec.yaml` (module plan, minutes, agenda) and `outline/syllabus.md` (Pragmatic-facing).

## 1. Course level

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Proposed, Dan to confirm.** Capability: 1 Market Intelligence. Primary skills: 1.1 Market Problem Identification, 1.2 Market Segmentation, 1.3 Market Discovery. Secondary skills (capability 8 Data-Driven Insight): 8.1 Market Data Context and Pattern Recognition, 8.4 Data Narrative and Stakeholder Communication. Pragmatic Framework 2027 category: Market. Focus areas: Market Problems, Win/Loss Analysis, Competitive Landscape |
| 2. What the learner can do | Build one agent from a template. Write and tune its brief. Set quality checks and hand-off rules. Decide each flag report item. Audit a sample against sources. Connect jobs so one output feeds the next. Read each problem's evidence profile, decide the order of problems by segment and defend it with sourced evidence |
| 3. How far | Develop and Apply. Develop: learners build the skill through a demo, a lab, a planted error and feedback in each module, with more complex input each time. Apply: learners use their own work first and make the judgment calls themselves. The warning on the planted error fades, so by module 5 they find it with no hint |
| 4. Evidence | Per lab (decision 42): the tuned brief, the flag report decisions and the audit findings. Plus the PM's order of top problems by segment (module 1), the match rate table (module 2), the hand-off rule (module 4), and the send, change or hold decisions and the order and validation decisions by segment (module 5). At the end: the saved agent with five jobs and a Monday plan with an audit date |
| 5. Experience | One course agent that grows in each module (house rule 12). The agent keeps a problem backlog and proposes a ranking. The PM decides. An autonomy ladder: hand-run batch, recurring run with a flag report, hand-off between jobs, an agent that faces other people. 40% instructor-led and 60% hands-on per module. Own work first, one fallback case company. Same core steps on Claude, ChatGPT, Copilot agent builder and Gemini. Breakout rooms by platform. Catch-up kit per module |

### What the workbook confirms

| Workbook text (from `capability-mapping.md`) | Course design |
| --- | --- |
| Capability 1: "separating evidence from inference, and requiring real-market validation before decisions" | The agent states facts and proposes. Only the PM calls a pattern or a validated problem |
| Skill 1.1D: urgency, pervasiveness, willingness to pay | The evidence profile uses these terms in learner-facing text |
| Competency 1.1B: noisy 20% versus quiet 80% | Lab 1 planted error: one vocal buyer ranks near the top |
| Skill 1.3: n=1 versus N=many | Fact label "single source" and the count rule "count interviews, not quotes" |
| Competency 1.2A: learn from competitors' customers and evaluators what the competitor does not solve and why they buy | Module 4 alternatives map, built from the team's own deals and interviews |
| Skill 3.3: "a prioritized problem backlog" | The agent keeps a problem backlog. Priority is relative across the backlog, not a fixed bar |
| Skill 1.3 AI text: synthetic respondents never replace research with real people | Gate 1 rule on AI personas and AI-moderated interviews (PA-02) |

### Big idea and themes (from Dan)

**Big idea:** AI can gather far more market signal than you can read. All of it is noise until you put it in context: what matters to your customers and what your business is trying to do. The agent gathers and organizes. You bring the context and make the call. Workbook skill 8.1 supports it: collected data has no value until value is extracted.

Ideas that run through the day:

1. There is no magic number. The agent reports the evidence and proposes a ranking. The PM decides the order.
2. Be great at product management before you are great at AI.
3. Win/loss is the data most teams do not get. Module 2 highlight, not a course theme.

### Where the course starts and stops

| Not taught here (known from elsewhere) | Taught here |
| --- | --- |
| One-pass AI synthesis and the quote check (PDW-AI). PDW-AI maps to the same skills at Introduce | Running an agent on batches, the problem backlog over time, flags, audits and tuning, at Develop and Apply |
| Urgency, pervasiveness and willingness to pay, and a planted outlier (PDW-AI and Foundations) | Referred to as known. New slides only on how the agent reports the three tests in the evidence profile and how the manager audits that report |
| Persona creation (BPW-AI, Market core course) | Labeling sources by persona and segment |
| Public competitor watching, scheduled-task setup (CAW-AI) | Alternatives map from the team's own deals. Schedule only as stretch where verified, new slides |
| Boundaries and guardrails as first taught (AI Agents course) | The same ideas applied to an agent that answers stakeholders, with new slides (decision 33) |
| Prompt structure JOB AND CONTEXT, RULES, OUTPUT (PRW-AI) | Referred to as known. The brief adds checks, hand-off rules and audits |
| Opportunity scoring and weighting (skill 2.2, Product Strategy and Planning course) | Ranking market problems by evidence. The alternative to beat, with its evidence |
| Market sizing and concept tests | Moved to the Product Strategy and Planning course |

## 2. Module level

Minutes: full day, then half days in brackets where they differ (Gate 2 decision 12).

### Module 1. Run your first batch and manage it by flags (row mr-wf-01, folds 05)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Proposed, Dan to confirm.** 1.1 Market Problem Identification, 1.3 Market Discovery. Competencies 1.1A, 1.1B, 1.3D. Box: Market Problems |
| 2. What the learner can do | Build the agent from the template. Decide each flag. Audit 3 problems against the interviews. Add a flag rule to the brief and rerun. Decide the order of the top problems by segment |
| 3. How far | Develop and Apply. First build, so a fast-start card supports new builders. Planted error warning: **told** |
| 4. Evidence | Tuned brief (v1 to v2: the learner adds the flag rule "If all quotes for a problem come from 1 interview, send it to the flag report"; the template already has "count interviews, not quotes", as in worked example v3). A ranking rule is an optional second rule. Flag report decisions for batch 1. Audit findings for 3 problems. The PM's order of the top problems by segment |
| 5. Experience | Opening build check, then a live demo on one platform, then the lab on own interviews or case batches 1 and 2. The agent keeps a problem backlog with an evidence profile per problem and fact labels (single source, AI-moderated only, one segment only). It proposes a ranking with reasons. Planted error: the vocal buyer (I-104, 3 quotes, 1 interview) ranks near the top. The learner catches it in the evidence profile and the audit. Debrief: each learner runs the check sample (3 minutes). Priority is relative (no magic number), and the Pragmatic test: can you predict that the next buyer of this persona will raise it? Only the PM calls a pattern. Rung 1, hand-run batch. 70 minutes (80) |

### Module 2. Win/loss and the match rate (row mr-wf-02)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Proposed, Dan to confirm.** 1.3 Market Discovery, 8.1 Market Data Context and Pattern Recognition. Competencies 1.3A, 1.3C, 8.1B. Box: Win/Loss Analysis (no primary skill in the workbook) |
| 2. What the learner can do | Add a win/loss job. Label each deal "interview" or "CRM only". Read the match rate. Audit source labels. Frame findings for sales without blame |
| 3. How far | Develop and Apply. Two inputs joined for the first time. Planted error warning: **hint** ("Audit before you approve") |
| 4. Evidence | Match rate table and the learner's read of it. Flag report decisions. Audit findings for 2 deals. The brief change |
| 5. Experience | Pragmatic program rules (interviews 2 to 4 weeks after the decision, by someone outside sales). Each interview goes into the driver log as it arrives, with no minimum number of deals (Gate 2 decision 7). The agent reports counts and changes per driver, with no pass or fail number. Lab on own deal export or the case CRM export. Hand-off rules match the case: flag a deal where the CRM reason and the buyer differ, and show the count of interviewed deals behind every driver. Planted error: a CRM-only "price" reason leaks into buyer findings. Debrief is the aha moment, and each learner runs the check sample (3 minutes). Rung 1, two sources. 70 minutes (75) |

### Module 3. The weekly run: read flags, not every item (row mr-wf-03, folds 04)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Proposed, Dan to confirm.** 1.1 Market Problem Identification, 8.1 Market Data Context and Pattern Recognition. Competencies 1.1B, 1.1C, 8.1B, 8.1D. Box: Market Problems |
| 2. What the learner can do | Add a weekly feedback job counted by unique account. Write a "no fit" rule. Audit 10 items and the "no fit" group. Decide which problems move in the backlog and which need discovery |
| 3. How far | Develop and Apply. High volume: the learner reads flags and a sample, not each item. Planted error warning: **hint** |
| 4. Evidence | Flag report decisions for week 2. Audit findings. The "no fit" rule added to the brief |
| 5. Experience | Talk track uses the case internal platform example (Fleet Data Platform, decision 9). Two runs (week 1, week 2) on own feedback or case exports. Feedback adds to pervasiveness in the problem backlog. The agent reports the change in accounts for every tag and sends every "no fit" group to the flag report. No number decides what the PM sees (case rule 4). Planted error: forced fit hides a new problem. Debrief: the instructor shows the check sample result (1 minute); learners run it after class. Stretch: schedule only where verified (decision 10), or the survey wave as a source for the evidence profile. Rung 2, recurring run. 60 minutes |

### Module 4. First hand-off: the alternatives map from your own deals (row mr-wf-10)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Proposed, Dan to confirm.** 1.2 Market Segmentation (competency 1.2A: what competitors' customers and evaluators say). Box: Competitive Landscape. 1.2 is a secondary skill on this box. Gap: the box's primary skill is 2.2 Opportunity Prioritization (capability 2). The course does not claim 2.2. 1.3 is not mapped to this box. Dan may still choose 1.3 (competency 1.3A, win/loss) |
| 2. What the learner can do | Connect the win/loss job to a map job. Write a hand-off rule. Trace 3 entries to interviews and deals. Choose the alternative to beat in one segment |
| 3. How far | Develop and Apply. First hand-off between jobs. Planted error warning: **hint** |
| 4. Evidence | The hand-off rule as written and as fixed. Audit findings for 3 traced entries. The alternative to beat, with its evidence |
| 5. Experience | Dan's example in the talk track, told as a Pragmatic or unnamed client story (decision 6). Lab on own driver log or case data. Planted error: CRM says "Rimecore", buyer kept the spreadsheet (case deal D-3108). One slide names the second-agent platform gap (decision 10). Debrief: the instructor shows the check sample result (1 minute); learners run it after class. Rung 3, hand-off between jobs. 55 minutes (decision 8) |

### Module 5. The agent answers stakeholders, and you stay accountable (row mr-wf-09, folds 07)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Proposed, Dan to confirm.** 1.1 Market Problem Identification, 8.4 Data Narrative and Stakeholder Communication. Competencies 1.1C, 1.1D, 8.4A, 8.4C. Box: Market Problems |
| 2. What the learner can do | Add an answer job with citations, dates, segments and a "what we do not know" line. Write rules for what the agent may say. Send, change or hold each answer. Judge the ranking and validation proposals by segment, then decide the order and what goes to validation |
| 3. How far | Develop and Apply. The agent faces other people. Planted error warning: **none** |
| 4. Evidence | Send, change or hold decisions for the answers. Audit findings for one cited answer. The hand-off rules. The PM's order and validation decisions by segment |
| 5. Experience | Lab on own logs and past reports or case reports. Learners ask 3 run questions: case Q1, Q2 and Q5. Q3 is optional on the case path. Q5 is the question from the internal Fleet Data Platform PM, answered from the problem backlog (decision 9). Each card step has a minute budget (27 of 30 lab minutes; 26 of 28 in half days). Hand-off rule: any source older than the age limit goes to the flag report. Planted error: an old study for another segment presented as "buyers want". Debrief: fix the brief, then run Q4 and compare (3 minutes). Q4 is the segment rule test: the agent must not say "food service buyers want" from one Food service interview (I-105; decision 3). Close: Monday plan and kit-final. Rung 3 plus, agent that faces other people. 65 minutes (60) |

## 3. Notes for an instructor who did not build the course (decision 45)

1. Demo on one platform only. Step cards in the workbook carry each platform. Breakout rooms group learners by platform.
2. Say "flags", "flag report" and "hand-off rules". Do not say "exceptions" or "escalations".
3. Say "problem backlog", "evidence profile", "urgency", "pervasiveness" and "willingness to pay clues". Do not say "the PM's bar", "intensity", "frequency" or "impact".
4. The agent proposes a ranking. The learner decides the order. Never let the agent's ranking stand as the answer in a debrief.
5. Tell each story as one heard from client teams, executives or Pragmatic's work with companies. Never as your own experience (decision 43).
6. Reveal the planted error only in the debrief. Ask which check or audit found it. The success check before each lab is general. The error-specific check is in the debrief only.
7. Schedule and second-agent stretch steps are only on the step cards of platforms where they are verified. Copilot and Gemini learners stay on the core path (decision 10).
8. A learner who falls behind rebuilds from the module's catch-up kit in about 5 minutes.

## 4. Open items for this brief

| # | Item | Owner |
| --- | --- | --- |
| 1 | Confirm the proposed capability and skills, and the 4 gaps in `capability-mapping.md` (spec OI-11, decision 7) | Dan |
| 2 | Confirm offering intent Develop and Apply for all five modules | Dan |
| 3 | Confirm the learner evidence list is what the ID team can score in beta (decision 29). Tell the ID team that the Win/Loss Analysis box has no primary skill | Dan with the ID team |
| 4 | Say yes to the problem backlog model (decision 4). `gate-2-decisions.md` still shows it as waiting (spec OI-20) | Dan |
| 5 | Segment rule is provisional A until Dan runs the exercises (decision 3, spec OI-15) | Dan |
| 6 | Template and lab 1 error are provisional C until proof P1 (decision 2, spec OI-14) | Dan |
| 7 | Confirm the half-day module lengths: module 5 is 5 minutes shorter than in the full day (spec OI-21) | Dan |
| 8 | Say yes to update `worked-example-row.yaml` v3. Lines 43 and 79 still say "below the PM's bar" and "emerging". The file is fingerprinted (spec OI-23) | Dan |
| 9 | Change the case lab 5 files to "Q1, Q2 and Q5 core, Q3 optional" (spec OI-24) | Case builder |
| 10 | Done: `m1-code-book.md` trimmed to 2,791 characters, under the 2,800 fallback budget | Case builder | 

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

## 6. Revision log 2 (v0.3, 2026-11-22)

Source: `outline/rework-brief-2.md` (Dan's Gate 2 comments), `outline/gate-2-decisions.md` and `outline/capability-mapping.md`. Edited files: `spec.yaml` (v0.2 to v0.3), this brief and `outline/syllabus.md`. The case builder edits `case/` in parallel. This revision did not edit case files.

### Brief section 1. Problem backlog replaces the PM's bar (decision 4)

| Item | What changed |
| --- | --- |
| 1.1 Rename to problem backlog | "Insight log" is "problem backlog" everywhere: promise, objectives, growth, kits, Copilot fallback, uploads, glossary, proof patterns. File names: `problem-backlog`, `job-card-problem-backlog`. Old term added to `voice.terms_never_used` |
| 1.2 Evidence profile | New `course_agent.problem_backlog.evidence_profile`: interviews (not quotes), accounts, segments, personas; source type (PM-held, AI-moderated, win/loss, feedback item, past report); urgency with one quote; pervasiveness; willingness to pay clues; source dates. Lab 1 template quality checks use it. Glossary adds evidence profile, urgency, pervasiveness and willingness to pay clues. "Intensity", "frequency" and "impact" removed from learner-facing text and added to `terms_never_used`. Module 1 registry guard no longer names "frequency vs intensity" |
| 1.3 Fact labels | New `fact_labels`: single source, AI-moderated only, one segment only. Stated as facts, not verdicts. Labeled problems stay in the backlog for trend tracking. Glossary rows "fact label" and "single source" |
| 1.4 Remove the bar | Removed "meets the PM's bar", "emerging" as a status, the `status_labels` block and the bar line in the template. `fallback_case` no longer points to a bar in `company.md`. New `no_threshold` rule. CO5 rewritten: rank problems against each other from evidence profiles, by segment |
| 1.5 Agent proposes, PM decides | New `ranking` block: the agent proposes a ranking with reasons; the PM decides the order, what is a pattern and what goes to validation; the agent never writes "pattern" or "validated". New quality check: each ranked problem has a reason that cites its evidence profile. Glossary adds proposed ranking and validated. Course theme 1 and the course close reworded |
| 1.6 Segment rule | `segment_rule` rewritten as a course rule, provisional A (decision 3): rank within a segment before any segment claim; never "<segment> buyers want" from one interview in that segment. Lab 1 and lab 5 hand-off rules and the lab 5 debrief check (I-105 test) use it |
| 1.7 Lab 1 planted error | Error rewritten: the agent ranks the vocal buyer (I-104, P05, 3 quotes, 1 interview) near the top. The learner catches it in the evidence profile and the audit (competency 1.1B). "Count interviews, not quotes" stays in the template (decision 2, provisional C). What the template leaves out is now a ranking rule, not a bar. Card step 5 is "Add one ranking rule". Success check and debrief check rewritten. P1 test names the error and the option B trigger |
| 1.8 Module 5 proposals | "Status proposals" are now "ranking and validation proposals by segment". The PM decides the order and what goes to validation. Changed: m5 build, objective m5-o4, card step 6, success check, debrief check, learner evidence, glossary |
| 1.9 Other case numbers | Win/loss: quality check "each pattern rests on the minimum number of deals" removed; the agent reports counts and changes, with a new `no_threshold` note. Hand-off rule "segment with too few deals" replaced by the fact label "one segment only". Feedback change and no-fit repeat: written as numbers the PM writes in the brief, with the case PM's choice in `case/company.md`. Age limit: a hand-off rule, old evidence goes to the flag report, case PM's choice. The PA-04 minimum of 10 decided deals stays as a Gate 1 program rule (new OI-22) |
| 1.10 Recount expected results | Case builder task. The spec no longer repeats case counts in debrief checks where the model can change them. Each debrief check names record ids and points to `case/expected-results.md`. Raw data counts that do not depend on the model stay (Rimecore 2 in Q2, 2 in Q3) |

### Brief section 2. Timing (decision 12)

| Item | What changed |
| --- | --- |
| Full day | Unchanged: 09:00 to 16:30, 60-minute lunch, 360 teaching minutes, 41% instructor-led. Removed the "cut lunch to 45 minutes" buffer line. New `lunch_note`: a shorter lunch is case by case |
| Half days | Each day 09:00 to 12:30, one 15-minute break, 195 teaching minutes. Day 1: open 25, module 1 80, break 15, module 2 75, close 15. Day 2: open 10, module 3 60, module 4 55, break 15, module 5 60, close 10. Total 390 teaching minutes, 161 instructor-led (41%) |
| Module minutes | Modules 1, 2 and 5 get a `half_day` block with minutes, a 40/60 split and arc minutes. Course close and day 1 close and day 2 open have half-day splits. Brief module rows show half-day minutes in brackets. New OI-21 asks Dan to confirm that module 5 is 5 minutes shorter in the half days |
| Syllabus | New half-day agenda. Lunch line removed |

### Brief section 3. Other decisions

| Decision | What changed |
| --- | --- |
| 6 (final) | Module 4 story slot: Dan's example, told as a Pragmatic or unnamed client story with identifying details removed. OI-05 set to decided, with Dan's send action open |
| 8 (final) | Module 4 stays 55 minutes. P3 says there is no separate timing check. OI-17 closed |
| 9 (final, C) | Module 3 talk track adds the internal platform example (Fleet Data Platform). Module 5 inputs name one FDP PM question, answered from the problem backlog, added by the case builder. OI-18 set to decided |
| 10 (final) | New `stretch_scope` and `platform_matrix_summary.stretch_verification`: core path the same on all 4 platforms; schedule and second-agent stretch only on verified cards (likely Claude and ChatGPT); Copilot and Gemini cards say the stretch is not available in this course; Copilot Studio, Power Automate and Google Antigravity out of scope at launch. Module 3 and 4 arcs name the gap once. Ladder rungs 2 and 3 updated. OI-02 and OI-03 closed |

### Brief section 4. Capability Standards (decision 7)

| Item | What changed |
| --- | --- |
| Course level | "Dan to name" replaced with capability 1 Market Intelligence, skills 1.1 and 1.3 (primary), 8.1 and 8.4 (secondary), marked "proposed, Dan to confirm". New `course.capability_standards` in the spec. New table "What the workbook confirms" in this brief |
| Module level | Each module row 1 and each spec module have skills and competencies from the module map in `capability-mapping.md`. Gaps named: module 2 box has no primary skill; module 4 does not claim 2.2 |
| Open items | OI-11 now holds the proposal and the 4 gaps. Brief open item 1 updated. Syllabus shows the mapping as proposed |

### Other changes

1. Spec version 0.3. Header comment and `course.length` updated.
2. Open items: OI-13 superseded by the backlog model (new OI-20, decision 4 still "waiting for Dan yes" in `gate-2-decisions.md`). OI-14 and OI-15 show their provisional status. New OI-21 (half-day module lengths) and OI-22 (PA-04 minimum).
3. Syllabus: internal notes removed (decision numbers, "Dan to name", the lunch buffer). New model, new half-day agenda, platform stretch note.

## 7. Revision log 3 (v0.3, revision 3, 2026-11-22)

Source: `outline/critic-report.md` (recheck after rework 2) and the corrected `outline/capability-mapping.md`. Edited files: `spec.yaml`, this brief and `outline/syllabus.md`. This revision did not edit case files. Timing totals do not change: 360 teaching minutes in the full day, 195 per half day, 40/60 in every module. Only the minutes inside debriefs and lab 5 have new budgets.

### Must fix

| Id | Result | What changed, or why not |
| --- | --- | --- |
| M1 | Fixed | Module 3 hand-off rules now match `company.md` rule 4. The agent reports the change in accounts for every tag (new quality check). Every "no fit" group goes to the flag report, with item IDs and accounts. The two numbers are gone. `hand_off_numbers_note` is replaced by a `no_threshold` note. Debrief check, `fallback_case.learner_files` and the module 3 row in this brief updated |
| M2 | Fixed | Lab 5 card steps have minute budgets: 3, 4, 3, 6, 5, 6 (27 of 30 minutes). Half days: 3, 4, 3, 6, 5, 5 (26 of 28). Four run questions did not fit, so Q3 is optional on the case path. Q1, Q2 and Q5 are core. The debrief now holds "Run Q4 and compare" (3 minutes). Full-day debrief: reveal 2, brief fix 2, Q4 3, segment rule 1, Monday 1. Half days: brief fix 1. Cost: the "sources disagree" rule is tested only by learners who ask Q3 |
| M3 | Case builder | Count error is in `expected-results.md`. Not a planner file |

### Should fix

| Id | Result | What changed, or why not |
| --- | --- | --- |
| S1 | Fixed, not as the critic proposed | The lab 1 fix is now the flag rule from `planted-errors.md`: "If all quotes for a problem come from 1 interview, send it to the flag report." The ranking rule is an optional second rule. Why not the critic's way: the case expected results (batch 1 flag 3, check sample pass condition 4) already depend on the flag rule, and the case is shared. Changed: growth, kits, template "left out on purpose", card step 5, objective m1-o4, fix, success check, debrief check, learner evidence, OI-14, syllabus |
| S2 | Fixed | Removed the module 2 rule "a driver that rests on deals from one segment only". Rule 3 in the case already counts deals by segment, and the quality check shows the counts |
| S3 | Fixed | Module 5 rule: "Any source older than the age limit the PM writes in the brief goes to the flag report" (case: 18 months, rule 1) |
| S4, S5, S6 | Fixed in `capability-mapping.md` | Spec, brief and syllabus now match it. Primary skills 1.1, 1.2 and 1.3. Secondary 8.1 and 8.4. Module 4: 1.2 Market Segmentation, competency 1.2A. Module 5 adds 8.4A and 8.4C. OI-11 says 1.3 is not a box 05 skill and that Dan may still choose 1.3 |
| S7 | Fixed in spec and brief | "Dan's test" is now "the Pragmatic test". `expected-results.md` line 19 still says "Dan's test". Case builder action |
| S8 | Fixed | Module 1 registry guard: urgency, pervasiveness and willingness to pay, and the planted outlier, are known from PDW-AI and Foundations. New slides only on how the agent reports them. Module 3 stretch is now "add the survey wave as a source for the evidence profile". New row in "Where the course starts and stops". Syllabus says learners know the three tests |
| S9 | Open item | New OI-23. `worked-example-row.yaml` v3 is fingerprinted, so an edit needs Dan's yes |
| S10 | Fixed | Each lab now has a `check_sample` slot. Labs 1 and 2: learners run it in the debrief (3 minutes each). Labs 3 and 4: the instructor shows the demo run result in the debrief (1 minute), and learners run it after class (about 5 minutes). Lab 5: Q4 in the debrief (3 minutes). Each debrief arc lists its minutes |
| S11 | Case builder | Heading in `expected-results.md`. Not a planner file |

### Notes

| Id | Result | What changed, or why not |
| --- | --- | --- |
| N1 | Recorded | G2-PF-05 now names `m1-code-book.md` at 2,906 characters, over the 2,800 budget. Brief open item 10. The case builder trims it, or Dan accepts a higher budget |
| N2 | Fixed | Evidence pack is about 15,400 characters in `gate_2_risk` and G2-PF-03. Total of the 5 knowledge files is now about 11,900 characters |
| N3 | Fixed | "12 knowledge files. They are 5 job cards, 5 case knowledge files and 2 logs (the problem backlog and the driver log)" |
| N4, N5, N6, N9 | Case builder or mapping file | Not planner files |
| N7 | No change | Decision 4 is still waiting for Dan (OI-20) |
| N8 | No change | "(proposed)" stays in the syllabus until Dan confirms the mapping |
| N10 | No action | Pass |

### Actions for others

1. Case builder: change `company.md` and `m5-stakeholder-questions.md` to "Q1, Q2 and Q5 core, Q3 optional" (OI-24).
2. Case builder: change "Dan's test" to "the Pragmatic test" in `expected-results.md`.
3. Dan: say yes or no to the v3 row update (OI-23), and confirm the capability mapping (OI-11).
