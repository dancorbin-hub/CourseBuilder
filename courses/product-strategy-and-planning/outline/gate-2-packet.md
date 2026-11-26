# Gate 2 packet v3: Advanced AI for Product Strategy and Planning

- Course id: `product-strategy-and-planning`. For Dan. Version 3, 2026-11-26. It replaces version 2.
- Files under review: `spec.yaml` v0.4, `outline/development-brief.md`, `outline/syllabus.md` (v2), `outline/capability-mapping.md` (v2), `outline/proof-kit-drafts.md`, `case/` (Larkspan Systems, late November 2027, plan year 2028).
- Gate 2 is not approved. It is approved when you say so. Then Pragmatic reviews the syllabus.
- Reading time: about 20 minutes. Section 1 shows what changed. Section 2 lists only what is still open.
- Case facts for this version: the case is dated 2027. The plan year is 2028. The supplier is Ostrelane Tooling. The bond story is Trendslop. It goes in the module 1 deck only, with no HBR figures on slides.

## How to answer

Answer with the item number and your choice. I recommend one option where there is a choice.

Count: 9 open items in section 2.1 (items O1 to O11, O1 and O9 are closed) and 6 smaller items in section 2.2.

## 1. What changed since your first read

Your answers are on the left. The files that now hold each answer are on the right. Detail of each change: `outline/gate-2-changes.md`.

| Your answer | What landed | Where |
| --- | --- | --- |
| Decision 1: option A for the release plan hand-off rule | The agent stops, writes no new date, does not edit the release plan. It hands the change to the PM and the release plan owner (the Delivery lead in the case). Options table removed | spec `gate_2_designs.ps_10`, module 4, rung 3. Syllabus module 4 |
| Decision 2: option B, plus "go one step further" | Data check card kept. Confidential terms list moved to lab 4. Lab 1 data line and the "3 or more terms" rule dropped. Lab 4 talk track: the agent is a second check, not the control, and it misses paraphrases. Take-home Production readiness checklist (7 items: what to test, who signs off) tells learners to test with data science, privacy and compliance | spec `data_safety_note`, `gate_2_designs.decision_e`. Syllabus "Data safety" and "What you take home" |
| Decision 3: keep the title | Title and planning line stay. Question for Pragmatic kept (O4) | spec `course.title_note`. Syllabus top. Mapping gap 9 |
| Decision 4: option A, 65, 60, 50 | Day 2 modules at 65, 60 and 50 minutes. All 6 card steps kept. Debrief is trimmed first. Times can flex. Script check: 360 teaching minutes in a full day. 195 in each half day | spec `agenda`. Syllabus agendas |
| Decision 5: option A in plain words | Module 3 error: the lower price needs a minimum yearly order of 50,000 sets. The plan buys 18,000. Glossary line: bulk pricing, like a seat license or an API tier. No hardware terms in core steps. Card test: a non-hardware PM must explain the error in one sentence | spec module 3, glossary. Syllabus terms table |
| Decision 6: no grouping | Grouping removed from the module 4 job card and agent step 4. Talk track lines added: a one-off problem can reach the product backlog on merit and impact. One problem can become several epics and many user stories. Themes help, but are not required. Epic, user story and product backlog are in the glossary | spec module 4, `ps_10`, glossary. Syllabus module 4 |
| Decision 7: module 1 aha | Firmware team at 100% in two programs. Every per-program check passes. The total is 200%. Module 5 (units shipped against active paid sites) is the closing echo. Not linked to win/loss | spec `course.aha_moment` |
| Decision 8: module 2 rung 1 plus | Ladder: 1, 1 plus, 2, 3, 3 plus | spec `autonomy_ladder`. Syllabus ladder table |
| Q1 to Q7 | Agent name final. Mapping confirmed. Intent Develop and Apply. Module 4 box Focus / Product Roadmap. No audience drafting. Syllabus tags Focus, Market, Business | spec `gate_2_decisions_applied`. Mapping v2 |
| Q6: case in 2027 | Every date, id and file name moved by one script. Plan year 2028. Supplier renamed Ostrelane Tooling. Numbers rechecked against `case/expected-results.md` | `case/`, `case/year-shift-map.md`, spec |
| Cadence and evidence order | The PM sets every cadence. Request intake can be frequent. The agent logs and flags. The PM reviews the problem backlog at the PM's cadence, often once a quarter. The agent may order it by market evidence. The column is "evidence order", never "priority". "Week 47 and 48" became "request batch 1 and 2". The module 5 monthly run changes no priority | spec core rule, m2, m3, m4, m5, glossary. Syllabus module 2 |
| Bond story: Trendslop | Chosen. Module 1 deck only. No HBR figures on slides until a licensed copy is read. The Intel pair is dropped | spec `decided`. The `status.yaml` record is still to do (O13) |
| Section 7 item 2: yes, fix the 4 research files | Approved. Not applied yet. A later step edits `research/` and records new fingerprints | spec OI-04 |
| Section 7 item 4: name check | Quick search found no exact match. Near miss: "Corvaer". The tooling supplier is now Ostrelane Tooling, not searched. Your decision is still open | O12 |
| Section 7 item 5: "The plans look good, so yes" | Read as yes. Three draft proof briefs, five job cards and a Copilot test checklist exist | `outline/proof-kit-drafts.md`. O2 |
| Late 9: do not overemphasize "no magic number" | The phrase is out of all learner text. The syllabus says: the AI gathers evidence and filters first, the PM decides, and the PM sets every threshold in the brief | Syllabus "What you learn to do". Spec themes and voice |
| Late 10: examples of other factors | Module 2 shows a worked example. PB-02 (audit preparation) ranks first on evidence. The case PM says yes and acts on it. Another PM could defer it for build time and dependencies. A table lists strategy, risk, investment level, build time, customer relations, dependencies and resource allocation. The PM writes the reason on the card | Syllabus module 2. Spec m2 talk track |
| Late 11: Google Sheet on every platform | Each course sheet ships as .xlsx, CSV and a Google Sheet template. Core path on Claude, ChatGPT and Copilot: work in the Sheet copy, download .xlsx or CSV, upload in chat. A Drive connector is a stretch step, only with a dated vendor doc. No live-write claim | Syllabus "How the course works" and platform table. Spec `google_sheet_option` |
| Late 12: pre-class plus in-class check | "Know before you design" goes in the pre-class email. It repeats in the course open (about 5 minutes) | Syllabus "What you need before class". Spec `readiness_checklist`, `course_open` |
| Late 13 and 14: optional connector lane | One optional card in labs 3, 4 and 5 only (your late item 14). Labs 1 and 2 have none. The card sits outside the 6 steps and outside the pass condition. Core path has no connector. Data check first. Approved connectors only. No connector is named until a dated vendor doc exists. No troubleshooting promise | Syllabus "Optional connector lane" and each module. Spec `module_arc.connector_lane_rule` |

Syllabus change: the module 2 headings, the "request batch" wording, the connector lane lines (labs 3 to 5) and the Google Sheet lines are new. The structure and section order follow the Market Research syllabus that Pragmatic approved.

## 2. Open items

### 2.1 Items that need you

#### O1. Funding scenario stretch (closed)

Closed by you (late item 16): the funding scenario step (sp-wf-13) stays in module 1 as a stretch step inside the lab. It never replaces the lab. The PM names both scenarios. The agent shows what slips.

#### O2. Proof kit drafts (was section 7 item 5)

You said "The plans look good, so yes." I read this as a yes to the drafts in `outline/proof-kit-drafts.md`. Please confirm or ask for changes. See O3 and O11.

#### O3. Platform proof on 4 platforms (you run it)

You build, save and rerun each pattern on Claude, ChatGPT Plus, Copilot agent builder and Gemini. Three patterns cover all five labs. Estimate: 45 to 60 minutes per platform per pattern, or about 90 minutes for a first Copilot run. Log your hours with `activity=gate-2-proof`. Use only the Larkspan case files. All brief texts, job cards and character counts are in `outline/proof-kit-drafts.md`. The Copilot test checklist is in its section 7.

**Record for each run:** platform, plan, pass or fail, minutes, what failed, and the memory mode (ChatGPT). A one-page grid is enough.

**Google Sheet check on every platform.** Run the sheet step once in the Google Sheet copy. On Claude, ChatGPT and Copilot, download .xlsx or CSV and upload it in chat. On Gemini, ask the skill to write to the Sheet. Do not claim a live write on any platform without a dated vendor doc.

##### P1. Build from template and run a batch with sheet totals (lab 1)

Brief: CORE plus job card J1 (brief v1). Knowledge: `strategy-okrs-kpis` (.txt for Copilot) and `capacity-sheet.xlsx`. Run files: `m1-submissions-q3.md` and `m1-status-q3.xlsx`. Prompt: "Run the portfolio pack job".

Common steps:

1. Build the agent from the module 1 kit. Name it "Strategy Evidence Agent".
2. Save. Close. Reopen.
3. Run Q3. Sum each team by hand.
4. Add the shared-team total check (brief v2).
5. Run Q4. Close and reopen. Rerun in a new chat.

Pass: the pack shows status, capacity and link per program. Totals come from the sheet formulas. Before the fix, the Firmware team at 200% is missed. After the fix, Q4 shows Firmware at 150% (P-01 90 plus P-02 60). No funding or strategy line. Same structure after reopen.

| Platform | Exact build | Save and reopen | Rerun and notes |
| --- | --- | --- | --- |
| Claude | New Project. Paste CORE plus J1 in instructions. Add the 2 knowledge files. Confirm code execution and file creation are on | The Project saves itself. Close the tab. Reopen from the project list | New chat in the Project. Attach the Q3 files. Output is .xlsx. Test the Google Sheet copy: download .xlsx, upload in chat |
| ChatGPT Plus | New Project. Paste instructions. Add the 2 files. Pick the memory mode that allows ChatGPT Work (G2-PF-02). Write down the mode | The Project saves itself. Close. Reopen | New chat in the Project. Totals through ChatGPT Work file output with formulas. Check that the formulas stay. Run the check sample in a new chat outside the Project |
| Copilot agent builder | Create agent. Paste CORE (count characters, limit 8,000). Embed `strategy-okrs-kpis.txt` and `capacity-sheet.xlsx`. Find the code interpreter toggle (G2-PF-01, G2-PF-03) | Select Save. Close. Reopen the agent | Upload the Q3 files and the sheet in chat. Download the output in the same session. Also run the no-license path (G2-PF-05): CORE plus J1 as 2,409 characters in Copilot Chat, files pasted |
| Gemini | New skill with CORE plus J1. Upload the 2 files. Open the Google Sheet template | Save the skill. Close. Reopen | Run the skill. Ask it to write inputs to the Sheet and read results (G2-PF-04). Also try upload or paste. Re-upload the whole skill to update a file. Time it |

##### P2. Decision checkpoint, then refresh with formulas (labs 2 and 3)

Module 2 brief: CORE plus J2. Knowledge: `problem-backlog.xlsx`, `request-decision-log.xlsx`, `roadmap.xlsx`. Run file: `m2-requests-batch-1.xlsx`. Module 3 brief: CORE plus J3. Knowledge: `business-case` (.txt), `business-case-sheet.xlsx`. Run files: `m3-source-pack.md`, `m3-tooling-quote.md`, then `m3-evidence-q4.md`. Test one module at a time on the no-license path.

Common steps:

1. Start from the P1 agent. Add the module 2 files. Send request batch 1: "Run the request job".
2. Check that every decision field is blank and the agent waits.
3. Send the decisions from `case/expected-results.md`: "Draft the replies". Check that replies match and hold no date.
4. Add the module 3 files. Send the business case, source pack and quote: "Run the business case job".
5. Add the rule "A price that needs a minimum yearly order above the plan volume goes to the flag report".
6. Send `m3-evidence-q4.md`. Read the "what changed" note. Save, close, reopen, rerun step 6.

Pass: decision fields are blank until you decide. The two "offline mode" requests (REQ-113 and REQ-114) are merged before the fix and separate after it. REQ-114 is "no match". The sheet gets inputs and returns results. The flag names the quote minimum (50,000 sets) and the plan (18,000). The "what changed" note lists A-02, A-05 and A-07. No go, hold or stop line.

| Platform | Exact build | Save and reopen | Rerun and notes |
| --- | --- | --- | --- |
| Claude | Add 4 files, then 3 files to Project knowledge. Code execution writes inputs to the sheet and reads results | Close and reopen the Project | New chat. Send the Q4 file. Output .xlsx. Test the Google Sheet copy once |
| ChatGPT Plus | Same, in the Project. Run the sheet step with ChatGPT Work. Record whether it fails in project-only memory (cg-14) | Close and reopen | Run the check sample in a new chat outside the Project. Note any memory leak from run 1 |
| Copilot | Embed .xlsx copies (one sheet each) and .txt copies. Count files (limit 20). Test whether the embedded sheet works with the code interpreter, or whether you must upload it in chat (mb-04 and mb-15 conflict) | Select Update. Reopen | Upload the sheet in chat. Download in the same session. Close the chat and note that the output is gone (session only) |
| Gemini | Re-upload the whole skill with the new files. Import .xlsx into Google Sheets. Check that formulas stay | Reopen the skill | One run that asks for a Sheet. Also upload the new evidence yourself. Note any time lost to re-upload |

##### P3. Hand-off between jobs and a monthly run across jobs (labs 4 and 5)

Module 4 brief: CORE plus J4, with the release plan rule written by you. Knowledge: `release-plan.xlsx`, `roadmap-decision-log.xlsx`, `roadmap.xlsx`, `request-decision-log.xlsx`, `capacity-sheet.xlsx`. Run files: `validated-problem-backlog.xlsx`, `evidence-log.xlsx`, `m4-change-request-cr-07.md`. Paste `confidential-terms-list` into the brief. Module 5 brief: CORE plus J5. Knowledge: `outcome-sheet.xlsx`. Run files: `m5-metrics-oct.xlsx`, `m5-metrics-nov.xlsx`.

Common steps:

1. Start from the P2 agent. Add the module 4 files. Paste the confidential terms list. Write the release plan rule: "If a change moves, removes or changes the scope of any item on the release plan, stop. Write the impact note. Mark it 'Release plan change: PM and release plan owner decide'. Write no new date. Do not edit the release plan."
2. Send the validated problem backlog and evidence log: "Run the roadmap refresh". Audit RM-14. Add the own-evidence rule. Rerun.
3. Send CR-07: "Run the change assessment".
4. Add the outcome job and sheet. Write the off-target range (more than 15 percent below target, 2 months). Send the October and November exports: "Run the outcome job".
5. Rebuild the whole agent from the module 5 kit in about 5 minutes. Time it.

Pass: the agent stops on RP-01 and writes no new date. It does not edit the release plan. The guard flags "ships in Q2". Firmware is at 190% and Cloud at 105% with CR-07. Two confidential terms are found (Brindle RF Components and Quillfern Pharmacy Group). RM-14 is flagged after the rule. The outcome job reads "active paid Probe X sites" from site activations, not units shipped. It is off range in both months. OS-4 is "no current data". No keep, change or stop line. No priority changes.

| Platform | Exact build | Save and reopen | Rerun and notes |
| --- | --- | --- | --- |
| Claude | 2 files, then 2 files to Project knowledge. Test a second agent only as stretch | Close and reopen | Rebuild from the kit in a new Project. Time it |
| ChatGPT Plus | Same in the Project. Count files (limit 20) | Close and reopen | Rebuild in a new Project. Time it |
| Copilot | Embed .xlsx and .txt copies. Upload the change request in chat. Run the no-license path one job at a time | Update. Reopen | Rebuild from the kit. Measure each kit against 8,000 characters (G2-PF-05). If upload and paste both fail, pair with another platform |
| Gemini | Re-upload the whole skill. Use the Sheet for the outcome step. Also try upload or paste | Reopen | Rebuild from the kit. Time the re-upload |

##### Proof items outside the patterns

| Id | Platform | Check |
| --- | --- | --- |
| G2-PF-01 | Copilot | .txt copies of .md files work as knowledge. .xlsx with one sheet each works |
| G2-PF-02 | ChatGPT | ChatGPT Work file output with formulas on Plus. Which project memory mode allows it |
| G2-PF-03 | Copilot | Code interpreter toggle and the embedded copy of the sheet |
| G2-PF-04 | Gemini | One skill run that asks for a Google Sheet with formulas. Whole-skill re-upload fits in the log save card time |
| G2-PF-05 | Copilot | No-license path: core brief 3,500 characters or fewer, job card 1,500 or fewer, one knowledge text 2,800 or fewer. Measure each kit |
| G2-PF-06 | All | 16 knowledge files at the end (limit 20). Counts by module: 4, 8, 11, 14, 16 |

If one platform fails a step, the step card says so and offers a pair or a changed step. If two or more fail the same step, bring it back to me before Gate 2 locks.

#### O4. Questions for Pragmatic review

Send these with the syllabus. You tell the reviewers.

| # | Question | Why |
| --- | --- | --- |
| a | Title. Does "planning" in the title conflict with the Framework category Planning? If yes, do you prefer "Advanced AI for Product Strategy and Roadmaps" or "Advanced AI for Product Strategy and Portfolio Planning"? | Your decision 3. The title stays unless they object |
| b | Mapping gaps. 2.2A to 2.2D (attribute selection, scoring model, weighting, calibration) are not covered because scoring is out. 2.2E says "Uses scoring outputs", and the course uses evidence cards and a blank decision field. 2.1C, 2.3A, 2.3D, 2.3F, 2.4A and 2.4E are not covered. Product Portfolio and Business Outcomes have no primary skill in the workbook | Mapping v2, gaps 1 to 7. You confirmed the mapping. The reviewers should know the gaps |
| c | Learner evidence. Can the evidence list in each module be scored in beta? | Decision 29. Reviewers and the ID team check |

#### O5. Market Research case is still dated 2026

The Market Research case says November 2026 and a 2027 plan. This course shows Larkspan in 2027, plan year 2028. You asked for one year in both courses. I did not edit the Market Research case. It is a separate course and a separate approval.

| Option | Effect |
| --- | --- |
| A. Shift the Market Research case to 2027 now | Both courses show Larkspan in the same year. Needs one script pass and a recheck of its expected results. Pragmatic has seen its syllabus, so check the syllabus for dates |
| B. Shift it before Market Research modules are built | Same result later. Learners in a combined cohort could see 2 different years in the meantime |

**Recommendation: A.** Do you want me to edit the Market Research case? I wait for your yes.

#### O6. Overlap checks

Check capacity 2 overlap with the workshops Strategic Transformation and Implementation and Action Planning, and with the partner course Mastering the Product Roadmap (module 4). Owner: you. Due before Pragmatic review.

#### O7. Evidence before slides

Open the primary Atlassian report (W2) and the N21 fieldwork method before any W1 or W3 figure goes on a slide. Read a licensed HBR copy before any Trendslop figure appears. Until then, state the finding in words. Several claims have no 2026 product-team source (stale business cases, outcome tracking). Say "warning signs include", not a statistic. Owner: research rerun. Due before modules 1 and 2 are built.

#### O8. Platform matrix recheck

The matrix was checked on 2026-11-22. Recheck it within 30 days of release. Gemini skills (gm-01) have no dated vendor doc. The Copilot code interpreter conflict (mb-04 and mb-15) stays open until O3 runs. Owner: researcher.

#### O9. Connector lane scope (closed)

Closed by you (late item 14): the connector lane is in labs 3 to 5 only. The lane lines are removed from modules 1 and 2 in the spec, the development brief and the syllabus. Each lane card still needs a dated vendor doc per platform before it names a connector.

#### O10. Gemini live write to a Sheet is not verified

Gate 1 decision f2 assumes a Gemini skill can write to a Google Sheet. No dated vendor doc says so (gm-09 covers file output in the app only, not skills). The Gemini card now tells the learner to write in the Sheet or to upload or paste the data. G2-PF-04 (in O3) tests it. If it fails, the card keeps the upload and paste path and drops the live write. No spec change is needed now.

#### O11. Job card J4 is over budget

The J4 template (module 4) is 1,567 characters. The no-license design budget is 1,500. The sum with the core brief is 2,919, far inside the Copilot limit of 8,000. The learner adds the release plan rule and the own-evidence rule, so the card grows by about 300 characters in class. The budget is a course design number, not a vendor number.

| Option | Effect |
| --- | --- |
| A. Trim J4 by about 70 characters | Keeps the 1,500 budget for the template. Possible loss of one hand-off line |
| B. Set a higher budget for module 4 (for example 2,000 for the card after the learner adds rules) | No lost text. The budget has a reason |
| C. Split J4 into part A and part B for the no-license path | Fits the limit. Adds a step for no-license learners |

**Recommendation: B.** The limit that matters is 8,000, and J4 plus core plus learner rules stays near 3,300. Related: `strategy-okrs-kpis.txt` (3,639) and `business-case.txt` (3,214) are over the 2,800 budget for one knowledge text. Either the case builder shortens them, or you raise the budget. I recommend shortening, because a shorter file also helps the card test.

### 2.2 Smaller open items

| # | Item | Owner | Need from you |
| --- | --- | --- | --- |
| O12 | **Names.** Quick search found no exact match for Brindle RF, Corvane Tooling, Quillfern Pharmacy Group or Larkspan Systems. The tooling supplier is now Ostrelane Tooling (invented, not searched). Run a fuller search before release. Rename if a match appears | Dan | Keep for training, or rename (DD-11). I recommend keep, and search first |
| O13 | **Bond story record.** Write the Trendslop pick in `status.yaml` | Session | None |
| O14 | **Research file fixes.** Apply the 4 fixes you approved in `research/workflows.yaml` and `worked-example-row.yaml`. Record new fingerprints | Session | None |
| O15 | **Case wording.** `case/m3-evidence-q4.md` title says "Q4 refresh". `expected-results.md` says "roadmap refresh and change". Suggest "Q4 evidence" and "quarterly refresh at the PM's cadence". I do not edit `case/`. Also add RL ids to `year-shift-map.md` | Case builder | None |
| O16 | **Critic run 2 done.** Critic report v2 read spec v0.3. It found 1 must-fix item and 6 smaller items. All are fixed in v0.4 except 3 case items for the case builder (see section 6). Run a third pass only if Dan wants one | Dan | None. Optional |
| O17 | **Release plan role.** Internal platform teams may have no Delivery lead. The learner text says "the person who owns the release plan". The card test checks it | Stage 3 | None |

## 3. Module plan

Full-day minutes first, half-day minutes in brackets. Every module is 40% instructor-led and 60% hands-on. Overall: 148 of 360 minutes instructor-led (41%).

| # | Module and workflow row | Minutes | Rung | Planted error and warning | Learner evidence | How the agent grows |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quarterly portfolio pack. Row sp-wf-09, with sp-wf-01 folded in. Focus / Product Portfolio | 70 (80) | 1 Hand-run batch | Shared Firmware team at 100% in 2 programs. Total 200%. **Told** | Tuned brief (v1 to v2), flag decisions, audit of 2 teams and 3 links, fund, pause or stop calls with reasons | Builds the agent. Adds the portfolio pack job. 4 knowledge files |
| 2 | Requests. Row sp-wf-12. Market / Market Problems | 60 (75) | 1 plus Decision checkpoint | False duplicate: two "offline mode" requests, different problems. **Hint** | Tuned brief with matching rule, flag decisions, audit of 3 cards and 2 log entries, yes, no or later with reason, matching replies | Adds the request job, problem backlog, request decision log, roadmap. 8 files |
| 3 | Living business case. Row sp-wf-05, folds 03 and 11, check 04. Business / Business Plan | 70 (65) | 2 Update with "what changed" | Quote price needs a minimum yearly order (50,000 sets). Plan buys 18,000. **Hint** | Tuned brief with quote terms rule, flag decisions, audit of 2 assumptions, go, hold or stop recommendation, next assumption to test | Adds the business case job, case and sheet. 11 files |
| 4 | Roadmap refresh and change. Rows sp-wf-07 and sp-wf-08. Focus / Product Roadmap | 65 (60) | 3 Hand-off between jobs | RM-14 validated by association: one sales request in a strong theme. **Hint** | Release plan rule as written, tuned brief with own-evidence rule, flag decisions, audit of 3 items, decision log entry | Adds the roadmap job, release plan, roadmap decision log. First hand-off: request to roadmap. 14 files |
| 5 | Outcomes, not output. Row sp-wf-10 (retitled). Business / Business Outcomes | 55 (50) | 3 plus Monthly run across jobs | Units shipped reported as active paid sites. **No hint** | Off-target range and rules, flag decisions, audit of 2 measures, tuned brief, investment review note | Adds the outcome job and sheet. Reads the module 3 baseline and module 1 OKRs. 16 files |

Open 25 minutes (15 instructor-led, 10 hands-on). Close 15 minutes (5 and 10). The ladder climbs: 1, 1 plus, 2, 3, 3 plus. The warning fades: told, hint, hint, hint, none. Labs 3 to 5 each have one optional connector card, outside the 6 steps. Labs 1 and 2 have none (O9 closed).

## 4. Development brief summary

Full text: `outline/development-brief.md`. The five questions at course level:

| Question | Answer |
| --- | --- |
| 1. Capability and skills | Capability 2 Strategic Direction. Skills 2.1, 2.2 (AI text only), 2.3, 2.4. Supporting 1.1. Confirmed by you |
| 2. What the learner can do | Build one agent. Write and tune its brief. Set checks and hand-off rules. Decide each flag. Audit a sample. Connect jobs. Record each decision with a reason |
| 3. How far | Develop and Apply |
| 4. Evidence | Per lab: tuned brief, flag decisions, audit findings, one PM decision record. At the end: the saved agent and a Monday plan with an audit date |
| 5. Experience | One agent that grows each module. Own work first. Larkspan as fallback. Same core steps on four platforms. Catch-up kit per module. Optional connector lane in labs 3 to 5 |

Course themes: the AI gathers evidence and filters first, and the PM decides. The PM sets the rules in the brief. Review too often and the team gets whiplash. Be great at product management before you are great at AI. The roadmap is direction. The release plan is the promise.

Where the course stops: no Strategy Matrix, no scoring or weights, no tagging and counting (Market Research module 3 owns it), no audience versions of the roadmap, no release estimates, no grouping of problems. Core courses are not prerequisites. Terms are defined in the course.

## 5. Fallback case and locked records

Larkspan Systems (fictional). Late November 2027, plan year 2028. Wireless temperature sensors (hardware) and the cloud software that watches them. External PMs own Probe, Hub, Probe X, Tag and Cloud. An internal PM owns the Fleet Data Platform. The tooling supplier is Ostrelane Tooling. All data is fictional and marked so. No number is a standard: each range is "the Larkspan PM's choice for this rule".

Gate 2 locks these records and results. Source: `case/expected-results.md` (instructor only).

| Lab | Records | Locked result | Check sample and pass condition |
| --- | --- | --- | --- |
| 1 | Strategy, OKRs and KPIs; capacity sheet (knowledge). Q3 and Q4 submissions, status exports (run) | Q3: 5 programs, ask USD 4,550 thousand, 0 programs over per program, 2 flags (P-03 status, P-04 no link). Sum by team: Firmware 200%, others 90%. Q4: ask USD 4,750 thousand, Firmware 150% (18 FTE asked, 12 available), 3 flags | Test lab at 130% across P-01 and P-04. Flag report names the team, the total and both programs. No funding or ranking line. No other team flagged |
| 2 | Problem backlog (14 problems), request decision log, roadmap (knowledge). Request batch 1 (run) | 9 requests. 2 executive or named deal. 3 internal. 1 no match. 4 past no or later. 2 true duplicates of a past yes. REQ-112 condition: 2 chains of 3 | Request batch 2. REQ-117 and REQ-118 get separate cards. No decision field filled. REQ-118 cites neither DL-2026-06 nor DL-2027-04. REQ-119 and REQ-121 flagged |
| 3 | Business case and sheet (knowledge). Source pack and tooling quote (run 1). Q4 evidence (run 2) | Base unit cost USD 52.30. Year 1 gross profit USD 1,881,200. Low and high USD 1,391,360 and 2,312,272. 2 flags (A-02, A-07). After the fix: unit cost USD 59.10, profit USD 1,758,800. Run 2: profit USD 1,718,336, A-05 at 57% below Low of 60% | Quote B-7731: minimum order 30,000 units a year against plan 18,000. Flag names both. No go, hold or stop line |
| 4 | Release plan, roadmap decision log (knowledge). Validated problem backlog, evidence log, CR-07 (run). Confidential terms list (pasted) | 16 roadmap items. 10 validated problems. RM-16 no trace. RM-08 in two themes. T-05 no item. RM-14 own evidence 1 account, 1 source type (rule: 3 and 2). CR-07: Firmware 150% to 190%, Cloud 95% to 105%. 2 of 5 confidential terms hit | CR-08: "ships in Q2" flagged, no new date, no release plan hand-off (no item touched) |
| 5 | Outcome sheet (knowledge). October and November exports (run) | OS-1 active paid sites: gap -25.5% and -31.5%, off range 2 months. OS-4: no data. Shipped minus active: 590 and 910 | Attach rate reported as outcome. Trials started labeled output. Outcome moved 0.2 points while output grew 56.1%. No keep, change or stop line |

**Knowledge files.** The agent ends the course with 16 files (limit 20 on ChatGPT Plus and Copilot): 1 core instructions, 5 job cards, 10 case files. Counts by module: 4, 8, 11, 14, 16. Run files and brief text do not count.

**Formats.** Each table ships as .xlsx (one sheet each), a Google Sheet template and a CSV copy. Each .md knowledge file has a .txt copy for Copilot. Three sheets hold formulas: capacity, business case and outcome.

**The case does not force the error.** The data makes each error likely. A model may not make it. O3 tests this. If a platform does not make the error, the debrief shows it from the instructor's demo run.

## 6. Critic results

The critic saw only the spec, the case and the rules. It found 5 must-fix items in v0.1. All 5 were fixed in v0.2 (module 4 template held its own fix, module 2 "serves strategy" wording, 18 files against a 16 limit, module 4 inputs, module 4 steps). Items not changed, with reasons, are in `outline/revision-notes.md`. Critic report v2 read spec v0.3. It found 1 must-fix item and 6 smaller items. v0.4 fixes them: Copilot Google Sheet option on labs 1, 3 and 5, the Cloud team numbers in the sample flag report (95% before CR-07, 105% with it), the lab 5 audit rule (start with the outcome the business case names), the PB-02 example (the case PM says yes), the case year label (Q6) and the stale note in `gate-2-changes.md`. Open for the case builder: the CR-08 source in `case/m4-check-sample.md`, the OS-3 gap sign in `case/expected-results.md`, and the Ostrelane name check (O12).

## 7. Source notes

- Platform facts rest on vendor docs dated 2026-09 to 2026-11. Two risks stay: Gemini skills (O10) and the Copilot code interpreter on embedded files.
- Statistics on slides need a 2026 or later primary source. O7 lists the gaps.
- The bond story figures stay off slides. State the finding in words.
