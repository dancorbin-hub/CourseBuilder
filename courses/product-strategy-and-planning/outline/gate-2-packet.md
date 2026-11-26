# Gate 2 packet: Advanced AI for Product Strategy and Planning

- Course id: `product-strategy-and-planning`. For Dan. Version 1, 2026-11-26.
- Files under review: `spec.yaml` v0.2, `outline/development-brief.md`, `outline/syllabus.md`, `outline/capability-mapping.md`, `case/` (Larkspan Systems).
- Gate 2 is approved when you say so. Then Pragmatic reviews the syllabus.
- Reading time: about 20 minutes. Sections 1.1 and 1.2 are the long ones. You asked to see them in full.

## How to answer

Answer with the decision number and your choice. I recommend one option in each. Where my view differs from the planner's, I say so.

Count: 8 decisions (section 1), 7 quick-yes items (section 1.9) and 4 yes-or-no items in section 7 (items 2 to 5).

## 1. Decisions for Dan

### 1.1 Decision 1 (PS-10, parked): the module 4 release plan hand-off rule

You said: "I'm having a hard time visualizing this, so I'll have to see it in full." Here is the full module.

**The idea in one line.** The roadmap is direction. The release plan is the promise. The agent works on the roadmap. It never writes a new date and never edits the release plan.

**What Larkspan has (case data).**

| Input | What it holds | Where it comes from |
| --- | --- | --- |
| Roadmap | 16 items in themes, with timeframes | Already in the agent from module 2 |
| Validated problem backlog | 10 problems the PM validated by the PM's own rule | Run file, sent with the refresh |
| Evidence log | Each evidence record: account, source type, date | Run file, sent with the refresh |
| Strategy, OKRs and KPIs | The stated objectives each item must trace to | Module 1 |
| Capacity table | Team capacity and allocation | Module 1 |
| Request decision log | Past decisions. Includes the PM's yes on REQ-112 | Module 2 |
| Release plan | Dated commitments for the next 2 releases | Module 4 knowledge file |
| Roadmap decision log | Past roadmap changes with date, decider and reason | Module 4 knowledge file |
| Confidential terms list | 5 terms the case PM keeps out of text for outsiders | Pasted into the brief |
| CR-07 | A change request from the approved request REQ-112 | Run file |

**What the agent does, in order.**

| Part | Step | Agent action |
| --- | --- | --- |
| A. Refresh | 1 | Read every roadmap item, the validated problem backlog and the evidence log |
| A | 2 | Trace each item to a theme, a validated problem and a stated objective. Write "no trace" where a link is missing |
| A | 3 | Show each item's trace table |
| A | 4 | List validated problems that no item traces to (see decision 6) |
| A | 5 | Flag: no trace, theme with no item, item in two themes, and any item below a rule the PM wrote |
| B. Change | 6 | Restate CR-07 in one line with its source |
| B | 7 | Find what it displaces in the same timeframe, using the capacity table |
| B | 8 | Find dependency hits: shared teams, components, suppliers, other teams |
| B | 9 | Check the release plan. If a displaced or changed item is on it, apply the hand-off rule the PM wrote |
| B | 10 | Run the commitment guard on all agent text: any date or promise not on the release plan, and any confidential term in text for outsiders |
| B | 11 | Write the impact note and a decision log entry with the decision field blank |
| B | 12 | Send the flag report to the PM |

**What the learner does, minute by minute (lab 4 is 30 minutes; 28 in half days).**

| Minute | Card step | Learner does | Agent does |
| --- | --- | --- | --- |
| 0 to 3 | 1. Add the roadmap job card, the release plan and your hand-off rule | Reads the request-to-roadmap rule. Types the release plan rule into the blank slot. Pastes the confidential terms list | Nothing yet |
| 3 to 6 | 2. Send the validated problem backlog and the evidence log: "Run the roadmap refresh" | Sends the files | Steps 1 to 5. RM-16 has no trace. RM-08 is in two themes. Theme T-05 has no item |
| 6 to 11 | 3. Audit 3 roadmap items against the evidence log | Picks 3 items. Opens each item's own evidence ids | Waits |
| 11 to 13 | 4. Write one rule in the brief for what you found | Writes the own-evidence rule and sets the "validated" range | Waits |
| 13 to 18 | 5. Send CR-07: "Run the change assessment" | Sends the file | Steps 6 to 12 |
| 18 to 28 | 6. Decide each flag and write your decision and reason in the decision log entry | Reads 5 flags. Writes the decision log entry | Waits |
| 28 to 30 | Slack | Catches up | None |

The refresh rerun with the fixed brief happens in the debrief (3 minutes). The planted error is validation by association. RM-14 sits in a strong theme but has one sales request of its own. The trace check passes. The audit finds it.

**The three hand-off rule options.**

| Option | Rule text | Gain | Cost |
| --- | --- | --- | --- |
| A. Stop and hand to the PM and the delivery lead | "If a change moves, removes or changes the scope of any item on the release plan, stop. Write the impact note. Mark it 'Release plan change: PM and delivery lead decide'. Do not write a new date. Do not edit the release plan." | The release plan stays the only promise. Fits 2.4C ("Distinguishes between roadmap direction, assumptions, dependencies, and committed delivery"). Fits the 3.4 AI text: "Estimates and commitments are verified with delivery teams" | The agent does less. The PM takes the item to the delivery lead outside the agent |
| B. Report and continue | "If a change touches a release plan item, list it in the flag report and finish the impact note. The PM decides whether the delivery lead needs to see it." | Faster. One pass gives the full picture | The impact note can look settled before the delivery lead sees it. Weak lesson on "the release plan is the promise" |
| C. Draft a release plan delta | "If a change touches a release plan item, draft a proposed release plan change (new scope and new date) for the delivery team." | Saves the delivery team a draft | The agent writes new dates. That is the false commitment the 2.4 AI text warns about. It breaks your rule that the agent never proposes. It crosses into skill 3.4 |

**Sample flag report for CR-07 under option A.** Numbers come from the case records and `case/expected-results.md`.

| # | Flag type | What the agent writes | PM decides |
| --- | --- | --- | --- |
| 1 | Release plan change | "CR-07 (from approved request REQ-112) needs the Firmware team in Q1 2027 at 40 percent. Firmware is at 150 percent before CR-07 and 190 percent with it (module 1 capacity table). RP-01, Hub firmware over-the-air rollback, is due 2027-02-15 and uses that team. Agent stopped. No new date written. Release plan not edited." | PM and delivery lead |
| 2 | Commitment guard | "CR-07 text says 'ships in Q2'. No calibration export item is on the release plan. The phrase is not in the impact note. Source: CR-07, VP Sales, 2026-11-18." | Yes |
| 3 | Dependency | "CR-07 needs a Cloud interface change at 10 percent of the Cloud team. Cloud is at 95 percent before and 105 percent with CR-07. RP-02 and RP-03 use the Cloud team in Q1." | Yes |
| 4 | Past decision | "Request decision log DL-2026-09 set calibration export to 'later' with the condition 'Three pharmacy chains ask'. The roadmap decision log records it as RL-2026-05. The records show 2 chains (A-5101, A-5120)." | Yes. The PM decides if the condition is met |
| 5 | Confidential term | "The impact note quotes Brindle RF Components and Quillfern Pharmacy Group. Both are on your confidential terms list. The note is marked 'Share with the Delivery lead and the Support lead'." | Yes. Before anyone shares it |

The decision log entry has a blank decision field.

**What the same flag 1 looks like under B and C (illustrative, not case data).**

- Option B: "RP-01 is touched by CR-07. Listed for your review." The impact note then says the export "fits in Q1". The delivery lead has not seen it.
- Option C: "Proposed: move RP-01 to 2027-04-15 and add the export on 2027-05-30." The agent has written two dates that nobody owns.

**What you, the PM, decide in this lab.** Accept, defer or reject CR-07, with a reason. Whether to take the release plan change to the delivery lead, and what to ask. The trade-off for displaced work and shared teams. Whether the "later" condition is met. Which items stay or leave. What the agent never decides: any date, any theme, any release plan edit.

**Not in the lab.** Audience versions of the change (your decision c, option 1).

**My recommendation: A.** It is the clearest form of your own theme. The agent still does the hard work: displacement, dependencies and the guard. Option C breaks your rule. Option B teaches the wrong lesson.

**Where the evidence is thin.**

1. No platform has run this rule yet. A model may still write a date in the impact note. Proof pattern P3 tests this on all four platforms. If it fails on two or more, the guard needs a stronger wording.
2. The lab is tight. The planner counts about 12 agent steps in 30 minutes. The 5-minute audit of 3 items is the weak point. The Stage 3 card test measures it.
3. Option A needs a delivery lead. Internal platform teams may have no such role. The rule text says "the person who owns the release plan" in the learner version.

### 1.2 Decision 2 (decision e, parked): data safety in the classroom

You said: "I'm having trouble envisioning how this is gonna work in the classroom." Here is lab 1, minute by minute.

**The three options.**

| Option | What happens | Time in lab 1 | Risk |
| --- | --- | --- | --- |
| A. Note only | The note sits on the lab brief slide and the top of each step card. The instructor reads it once. No learner action | 0 | Learners skip it. Nobody makes or records a choice |
| B. Data check card, confidential terms list and a log keep decision | A 3-question card above step 1 of every step card. The PM keeps a confidential terms list. The log save card asks what the log keeps. Module 4 adds one guard line | About 3 minutes (2 at the start, 1 at the log save card). About 1 minute in labs 2 to 5 | Takes lab time. The 2-minute estimate is not tested |
| C. Option B plus an agent intake scan | The agent scans each upload for personal data and confidential terms and stops before it processes the file | About 5 minutes | The data is already in the tool when the agent scans it. That gives false comfort. No platform has a verified scan. Use it as a talk track point only: "the agent cannot be your data guard" |

**Lab 1 under option B (33 minutes).**

| Minute | What the learner sees | What the learner does | What is recorded |
| --- | --- | --- | --- |
| 0 to 2 | Data check card above step 1. Q1: Is this tool approved by my company for this data? Q2: Does my file hold client data, health data, personal data, unreleased roadmap or release dates, forecasts, pricing, supplier terms or non-public financials? Q3: If Q2 is yes and Q1 is no, use the Larkspan case, or remove names and numbers first | Checks their own file against Q2. Chooses own work or the case | One line on the evidence sheet: "own work" or "case", and why |
| 2 to 6 | Step 1. The template brief | Adds the brief and the strategy inputs | Brief v1 |
| 6 to 10 | Step 2. The Q3 run | Sends the Q3 submissions. Reads the pack | Pack v1 |
| 10 to 16 | Step 3. The flag report | Decides each flag | Flag decisions |
| 16 to 24 | Step 4. Audit | Sums 2 shared teams. Checks 3 links | Audit findings |
| 24 to 28 | Step 5. Brief edit | Adds one quality check | Brief v2 |
| 28 to 33 | Step 6. The Q4 run | Sends Q4. Reads the flag report | Q4 pack and flags |
| Debrief, 1 minute | Log save card: what the pack log keeps | Keeps totals and decisions. Deletes or keeps names, by company rule | The log keep choice |

**Labs 2 to 5.** The data check card repeats. Most learners tick "same as lab 1" in 15 seconds. The log keep choice stays. Lab 4 adds the confidential term line in the commitment guard (flag 5 above).

**My recommendation: B, with one change.** Move the confidential terms list from lab 1 to lab 4. The planner put it in lab 1 (minutes 2 to 6) and added a "data line" to the lab 1 flag report (minutes 6 to 10). Both cost time in the tightest first lab. Neither pays off in lab 1: the pack has no text for outsiders. The list matters in lab 4, where a real hit occurs (flag 5). The freed minutes stay as buffer for first-time builders.

**Where the evidence is thin.**

1. The 2-minute estimate has no test behind it. The Stage 3 card test measures it. If the card takes more than 2 minutes, move Q1 (approved tool) to the pre-class checklist.
2. The planner's "3 or more terms" rule for the list is a number I would remove. It conflicts with your "no magic number" theme. Each PM lists the terms that PM would keep out.
3. The guard in lab 4 matches the strings on the list. It will miss a paraphrase such as "the antenna supplier". Say this in the talk track. It is a good teaching point.
4. Lab 5 has 25 minutes. The 15-second tick is the most it can take.

### 1.3 Decision 3 (DD-03): the title question for Pragmatic

You decided to keep the title (decision g). The open part is what we ask Pragmatic. The Framework has a category named Planning. Our title uses "planning" in a different sense.

| Option | What we send |
| --- | --- |
| 1 | Keep "Advanced AI for Product Strategy and Planning". Add the line "Planning here means annual and quarterly product planning. The course maps to Capability 2, Strategic Direction." Ask: "Does 'planning' in the title conflict with the Framework category Planning for your reviewers or learners? If yes, do you prefer option 2 or 3?" |
| 2 | Offer "Advanced AI for Product Strategy and Roadmaps" as an alternative |
| 3 | Offer "Advanced AI for Product Strategy and Portfolio Planning" as an alternative |

**Recommendation: 1.** You already chose the title. The question lets Pragmatic raise a conflict without reopening your decision. The syllabus has the line under the title. One note: the course touches the Planning category only once, in the module 2 reply step. The modules use the Focus, Market and Business categories. The conflict is real but small.

### 1.4 Decision 4 (DD-05): half-day module lengths

Day 2 holds modules 3 to 5 in 175 minutes. That is 15 fewer than the full day.

| Option | Day 2 module minutes | Effect |
| --- | --- | --- |
| A | Module 3 65, module 4 60, module 5 50. All 6 card steps kept. Debrief discussion trimmed | Split stays on the rung boundary (hand-run on day 1) |
| B | Split after module 3 instead | Day 1 needs 200 module minutes in 155. Does not fit |
| C | Day 2 open of 5 minutes, so module 5 keeps 55 | The reopen check gets 5 minutes. Risky for Copilot and Gemini learners |

**Recommendation: A.** Times can flex in delivery (Market Research lesson). Module 5 at 50 minutes is the tightest. The card test checks it. If it fails, I would trim the debrief, not a card step.

### 1.5 Decision 5 (DD-06): the planted error for module 3

| Option | Error | Check that passes anyway |
| --- | --- | --- |
| A | The hard tooling quote prices 50,000 units a year. The plan is 18,000. The plan uses the 50,000 price | Source, date and sheet recompute |
| B | An adoption assumption backed by stated interest, not real use | Not built in the case |
| C | Market size scope mismatch between two sources | Not built in the case |

**Recommendation: A.** It is hardware, a priority context. The sheet recompute passes, so only reading the quote terms finds it. The case, the expected results and the check sample exist for A only. Choosing B or C means new case data. B is close to a Market Research concept test error. C overlaps the market sizing agent planned for the Focus AI-forward course.

The A result is locked: unit cost USD 52.30 becomes USD 59.10. Year 1 gross profit falls from USD 1,881,200 to USD 1,758,800.

### 1.6 Decision 6 (DD-07): may the agent group validated problems that no roadmap item traces to?

The 2.4 AI text says "cluster validated problems into outcome themes". Your rule is that the agent never proposes strategy.

| Option | What the agent does |
| --- | --- |
| A | Groups the untraced validated problems by shared evidence (same segment, same source type). A group has no name, no theme wording and no advice. The PM names every theme |
| B | No grouping. The agent traces existing items and lists validated problems with no item |

The planner recommends A. **I recommend B.** Reasons:

1. A group is a suggestion about where the roadmap could go. Even unnamed, it nudges. Your Market Research lesson is that people follow an agent's lean (the "54% vs 36%" result).
2. Nothing in the locked case results tests grouping. No expected result, no pass condition and no planted error depends on it. I cannot show you a check for it.
3. B removes one agent step from a lab that the critic called tight.
4. The lab still teaches the 2.4B and 2.4D competencies without it.

If you pick A, the grouping stays as written and the card test checks it. If you pick B, the planner removes one sentence from the module 4 job card and step 4 of the agent steps. No case file changes.

### 1.7 Decision 7 (DD-08): the course aha

Your Market Research aha is win/loss. This course has no win/loss lab.

| Option | Aha |
| --- | --- |
| A | Module 1. The shared Firmware team is planned at 100% in two programs. Every per-program check passes. The sum by team is 200% |
| B | Module 5. The launch looked on track because units shipped stood in for active paid sites (shipped 590 above active in October, 910 in November) |

**Recommendation: A.** It lands early, in the lab where we tell learners about the error. It shows why the PM's audit matters before any strategy talk. B stays as the closing echo. Note: the course close repeats the module 5 point already.

### 1.8 Decision 8 (DD-09): the module 2 rung

The PM decides every flagged card, so module 2 is not a recurring run.

| Option | Rung name |
| --- | --- |
| A | Rung 1 plus: hand-run batch with a decision checkpoint (as drafted) |
| B | Rung 2: recurring weekly run, the PM decides only flagged cards |

**Recommendation: A.** It is honest about how much the PM reads. The ladder still climbs: 1, 1 plus, 2, 3, 3 plus. B would put two modules on rung 2 and blur module 3.

### 1.9 Quick-yes table

Say "yes to all" or name the item you change.

| # | Item | Proposal | Why |
| --- | --- | --- | --- |
| Q1 | Agent name (DD-04) | Strategy Evidence Agent | It says the agent handles evidence, not strategy |
| Q2 | Capability mapping | Confirm `outline/capability-mapping.md`. Tell the Pragmatic reviewer the gaps in its last table (2.2A to 2.2D not covered, 2.2E says "Uses scoring outputs") | Names come from the workbook. No name is invented |
| Q3 | Offering intent | Develop and Apply for all 5 modules. The ID team confirms the learner evidence list can be scored in beta | No change since Gate 1 |
| Q4 | Module 4 box (OI-07) | Focus / Product Roadmap. The research file tags row 08 Planning / Stakeholder Management | No audience drafting, so the stakeholder box does not fit |
| Q5 | Decision c, working choice (OI-05) | Keep option 1: no audience drafting. Module 4 is built on it | Focus already has a one-pass audience version. Rule 9 |
| Q6 | Case date | Let me change `extracted_on` in `m5-metrics-nov.csv` and `.xlsx` to 2026-11-30 | The case says late November 2026. The file says 2026-12-02. I do not edit `case/` without your yes |
| Q7 | Syllabus tags | Show Framework categories Focus, Market and Business with the five focus areas, not "Planning" tags | The spec boxes are Focus, Market and Business. This also avoids the title conflict in decision 3 |

**What the syllabus assumes.** It follows my recommendations. If you choose differently, these lines change:

| If you choose | Syllabus change |
| --- | --- |
| Decision 1 B or C | Module 4 objective 3 and the "Hand-off" text |
| Decision 2 A | The data check sentence in "Data safety" |
| Decision 4 B or C | The half-day agenda and module headings |
| Decision 5 B or C | Module 3 text. Case rework |

## 2. Module plan

Full-day minutes first, half-day minutes in brackets. Every module is 40% instructor-led, 60% hands-on. Overall: 148 of 360 minutes instructor-led (41%).

| # | Module and workflow row | Minutes | Rung | Planted error and warning | Learner evidence | How the agent grows |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quarterly portfolio pack. Row sp-wf-09, with sp-wf-01 folded in. Focus / Product Portfolio | 70 (80) | 1 Hand-run batch | Shared Firmware team at 100% in 2 programs. Total 200%. **Told** | Tuned brief (v1 to v2), flag decisions, audit of 2 teams and 3 links, fund, pause or stop calls with reasons | Builds the agent. Adds the portfolio pack job. 4 knowledge files |
| 2 | Requests. Row sp-wf-12. Market / Market Problems | 60 (75) | 1 plus Decision checkpoint | False duplicate: two "offline mode" requests, different problems. **Hint** | Tuned brief with matching rule, flag decisions, audit of 3 cards and 2 log entries, yes, no or later with reason, matching replies | Adds the request job, problem backlog, request decision log, roadmap. 8 files |
| 3 | Living business case. Row sp-wf-05, folds 03 and 11, check 04. Business / Business Plan | 70 (65) | 2 Refresh with "what changed" | Tooling quote tier (50,000 units) does not match the plan (18,000). **Hint** | Tuned brief with quote terms rule, flag decisions, audit of 2 assumptions, go, hold or stop recommendation, next assumption to test | Adds the business case job, case and sheet. 11 files |
| 4 | Roadmap refresh and change. Rows sp-wf-07 and sp-wf-08. Focus / Product Roadmap | 65 (60) | 3 Hand-off between jobs | RM-14 validated by association: one sales request in a strong theme. **Hint** | Release plan rule as written, tuned brief with own-evidence rule, flag decisions, audit of 3 items, decision log entry | Adds the roadmap job, release plan, roadmap decision log. First hand-off: request to roadmap. 14 files |
| 5 | Outcomes, not output. Row sp-wf-10 (retitled). Business / Business Outcomes | 55 (50) | 3 plus Monthly run across jobs | Units shipped reported as active paid sites. **No hint** | Off-target range and rules, flag decisions, audit of 2 measures, tuned brief, investment review note | Adds the outcome job and sheet. Reads the module 3 baseline and module 1 OKRs. 16 files |

Open 25 minutes (15 instructor-led, 10 hands-on). Close 15 minutes (5 and 10). Half days: day 1 is 09:00 to 12:30, day 2 is 09:00 to 12:30, 195 teaching minutes each, split after module 2.

The ladder climbs across the day: 1, 1 plus, 2, 3, 3 plus. The warning fades: told, hint, hint, hint, none.

## 3. Development brief summary

Full text: `outline/development-brief.md`. The five questions at course level:

| Question | Answer |
| --- | --- |
| 1. Capability and skills | Capability 2 Strategic Direction. Skills 2.1, 2.2 (AI text only), 2.3, 2.4. Supporting 1.1. Proposed, you confirm |
| 2. What the learner can do | Build one agent. Write and tune its brief. Set checks and hand-off rules. Decide each flag. Audit a sample. Connect jobs. Record each decision with a reason |
| 3. How far | Develop and Apply |
| 4. Evidence | Per lab: tuned brief, flag decisions, audit findings, one PM decision record. At the end: the saved agent and a Monday plan with an audit date |
| 5. Experience | One agent that grows each module. Own work first. Larkspan as fallback. Same core steps on four platforms. Catch-up kit per module |

Course themes (from you):

1. Strategy is where product judgment is essential. The agent gathers. The PM decides.
2. There is no magic number. The PM sets every range and threshold.
3. Be great at product management before you are great at AI.
4. The roadmap is direction. The release plan is the promise.

Where the course stops: no Strategy Matrix, no scoring or weights, no tagging and counting (Market Research module 3 owns it), no audience versions of the roadmap, no release estimates. Core courses are not prerequisites. Terms are defined in the course.

Open points in the brief: confirm the mapping, tell the reviewer the gaps, confirm the evidence list with the ID team. All are in section 1.9.

## 4. Fallback case: Larkspan Systems

One company serves the whole course. It is the Market Research case company with new strategy, OKR, KPI, program and team data. Wireless temperature sensors (hardware) and the cloud software that watches them. About 420 employees. External PMs own Probe, Hub, Probe X, Tag and Cloud. An internal PM owns the Fleet Data Platform. All data is fictional and marked so. No number is a standard: each range is "the Larkspan PM's choice for this rule".

**Locked records and results per lab.** Gate 2 locks these. Source: `case/expected-results.md` (instructor only).

| Lab | Records | Locked result | Check sample and pass condition |
| --- | --- | --- | --- |
| 1 | Strategy, OKRs and KPIs; capacity sheet (knowledge). Q3 and Q4 submissions, status exports (run) | Q3: 5 programs, ask USD 4,550 thousand, 0 programs over per program, 2 flags (P-03 status, P-04 no link). Sum by team: Firmware 200%, others 90%. Q4: ask USD 4,750 thousand, Firmware 150% (18 FTE asked, 12 available), 3 flags | Test lab at 130% across P-01 and P-04. Flag report names the team, the total and both programs. No funding or ranking line. No other team flagged |
| 2 | Problem backlog (14 problems), request decision log, roadmap (knowledge). Week 47 requests (run) | 9 requests. 2 executive or named deal. 3 internal. 1 no match. 4 past no or later. 2 true duplicates of a past yes. REQ-112 condition: 2 chains of 3 | Week 48. REQ-117 and REQ-118 get separate cards. No decision field filled. REQ-118 cites neither DL-2025-06 nor DL-2026-04. REQ-119 and REQ-121 flagged |
| 3 | Business case and sheet (knowledge). Source pack and tooling quote (run 1). Q4 evidence (run 2) | Base unit cost USD 52.30. Year 1 gross profit USD 1,881,200. Low and high USD 1,391,360 and 2,312,272. 2 flags (A-02, A-07). After the fix: unit cost USD 59.10, profit USD 1,758,800. Run 2: profit USD 1,718,336, A-05 at 57% below Low of 60% | Quote B-7731: minimum order 30,000 a year against plan 18,000. Flag names both. No go, hold or stop line |
| 4 | Release plan, roadmap decision log (knowledge). Validated problem backlog, evidence log, CR-07 (run). Confidential terms list (pasted) | 16 roadmap items. 10 validated problems. RM-16 no trace. RM-08 in two themes. T-05 no item. RM-14 own evidence 1 account, 1 source type (rule: 3 and 2). CR-07: Firmware 150% to 190%, Cloud 95% to 105%. 2 of 5 confidential terms hit | CR-08: "ships in Q2" flagged, no new date, no release plan hand-off (no item touched) |
| 5 | Outcome sheet (knowledge). October and November exports (run) | OS-1 active paid sites: gap -25.5% and -31.5%, off range 2 months. OS-4: no data. Shipped minus active: 590 and 910 | Attach rate reported as outcome. Trials started labeled output. Outcome moved 0.2 points while output grew 56.1%. No keep, change or stop line |

**Knowledge files.** The agent ends the course with 16 files (limit 20 on ChatGPT Plus and Copilot): 1 core instructions, 5 job cards, 10 case files. Counts by module: 4, 8, 11, 14, 16. The source pack, quote, evidence log, validated problem backlog and confidential terms list are run files or brief text.

**Formats.** Each table ships as `.xlsx` (one sheet each), a Google Sheet template and a CSV copy. Each `.md` knowledge file has a `.txt` copy for Copilot. Three sheets hold formulas: capacity, business case and outcome. Critic and builder recomputed 30 or more numbers by script. All matched.

**The case does not force the error.** The data makes each error likely. A model may not make it. The proof patterns test this. If a platform does not make the error, the debrief shows it from the instructor's demo run.

## 5. Platform proof plan (you run it)

Your decision 27: you build, save and rerun each distinct pattern on Claude, ChatGPT Plus, Copilot agent builder and Gemini. Three patterns cover all five labs. Estimate: 45 to 60 minutes per platform per pattern. Log your hours with `activity=gate-2-proof`.

**Gap to close first.** The proof kit files (brief text and job cards) do not exist yet. Stage 3 writes them. You can run the proof from the brief text in `spec.yaml` and the case files. I recommend the planner writes three draft brief texts first. Say yes to that or tell me otherwise.

**Record for each run:** platform, pass or fail, minutes, what failed. A one-page grid is enough.

### P1. Build from template, run a batch with sheet totals (lab 1)

**Common test.**

1. Build the agent from the module 1 template. Name it "Strategy Evidence Agent".
2. Add `strategy-okrs-kpis` and the capacity sheet as knowledge.
3. Save. Close. Reopen.
4. Send `m1-submissions-q3.md` and `m1-status-q3.csv`: "Run the portfolio pack job".
5. Check the pack, then close and reopen again.
6. Rerun in a new chat in the agent.

**Pass.** The pack has status, capacity and link per program. Totals come from the sheet formulas. The 200% Firmware error is not caught before the fix. The rerun after reopen has the same structure. No funding or strategy line.

| Platform | Exact build | Save and reopen | Rerun and notes |
| --- | --- | --- | --- |
| Claude | New Project. Paste brief v1 in instructions. Add the 2 files as project knowledge. Confirm code execution and file creation are on | Project saves itself. Close the tab. Reopen from the project list | New chat in the project. Attach the Q3 files. Output is `.xlsx` |
| ChatGPT Plus | New Project. Paste instructions. Add the 2 files. Pick the memory mode that allows ChatGPT Work (G2-PF-02). Write down the mode | Project saves itself. Close. Reopen | New chat in the project. Totals through ChatGPT Work file output with formulas. Check that the formulas stay |
| Copilot agent builder | Create agent. Paste instructions (count characters, limit 8,000). Embed `strategy-okrs-kpis.txt` and `capacity-sheet.xlsx`. Turn the code interpreter on (G2-PF-01, 03) | Select Save. Close. Reopen the agent | Upload the Q3 files and the sheet in chat. Download the output in the same session. Also run the no-license path (G2-PF-05): core brief plus job card under 8,000 characters, files pasted |
| Gemini | New skill with instructions. Upload the 2 files. Open the Google Sheet template | Save the skill. Close. Reopen | Run the skill. Ask it to write inputs to the Sheet and read results (G2-PF-04). Re-upload the whole skill to update a file. Time it |

### P2. Decision checkpoint and refresh with formulas (labs 2 and 3)

**Common test.**

1. Start from the P1 agent. Add the request job card, the problem backlog, the request decision log and the roadmap.
2. Send `m2-requests-week-47`: "Run the request job".
3. Check that every decision field is blank and the agent waits.
4. Write one decision per flagged card. Send them: "Draft the replies".
5. Add the business case job card, the business case and the sheet. Send the source pack and quote: "Run the business case job".
6. Send `m3-evidence-q4`. Read the "what changed" note.
7. Save, close, reopen, rerun step 6.

**Pass.** Decision fields are blank until you decide. Replies match your decisions and hold no new date. The false duplicate (REQ-113 and REQ-114) appears before the fix. The sheet gets inputs and returns results. The Q4 run lists changes for A-02, A-05 and A-07.

| Platform | Exact build | Save and reopen | Rerun and notes |
| --- | --- | --- | --- |
| Claude | Add 4 files, then 3 files to project knowledge. Code execution writes inputs to the sheet | Close and reopen the project | New chat. Q4 file. Output `.xlsx` |
| ChatGPT Plus | Same, in the Project. Run the sheet step with ChatGPT Work. Record whether it fails in project-only memory | Close and reopen | Run the check sample in a new chat outside the project (decision f5). Note any memory leak from run 1 |
| Copilot | Embed `.xlsx` copies (one sheet each) and `.txt` copies. Count files (limit 20). Test whether the embedded sheet works with the code interpreter, or whether you must upload it in chat (mb-04 and mb-15 conflict) | Select Update. Reopen | Upload the sheet in chat. Download in the same session. Close the chat and note that the output is gone (session only) |
| Gemini | Re-upload the whole skill with the new files. Import `.xlsx` into Google Sheets. Check that formulas stay | Reopen the skill | One run that asks for a Sheet. Upload the new evidence yourself. Note any time lost to re-upload |

### P3. Hand-off between jobs and a monthly run across jobs (labs 4 and 5)

**Common test.**

1. Start from the P2 agent. Add the roadmap job card, the release plan and the roadmap decision log. Paste the confidential terms list into the brief. Write hand-off rule A (decision 1).
2. Send the validated problem backlog and evidence log: "Run the roadmap refresh". Audit RM-14. Add the own-evidence rule. Rerun.
3. Send `m4-change-request-cr-07`: "Run the change assessment".
4. Add the outcome job and the outcome sheet. Send the October and November exports: "Run the outcome job".
5. Rebuild the whole agent from the kit-m5 state in about 5 minutes. Time it.

**Pass.** The agent stops on RP-01 and writes no new date. The guard flags "ships in Q2". The guard finds Brindle RF Components and Quillfern Pharmacy Group. RM-14 is flagged after the rule. The outcome job reports OS-1 off range from site activations, after the fix. The rebuild takes about 5 minutes.

| Platform | Exact build | Save and reopen | Rerun and notes |
| --- | --- | --- | --- |
| Claude | 2 files, then 2 files to knowledge. Test a second agent only as stretch | Close and reopen | Rebuild from the kit in a new Project. Time it |
| ChatGPT Plus | Same in the Project. Count files (limit 20) | Close and reopen | Rebuild in a new Project. Time it |
| Copilot | Embed `.xlsx` and `.txt` copies. Upload the change request in chat. Run the no-license path one job at a time | Update. Reopen | Rebuild from the kit. Measure each kit against 8,000 characters (G2-PF-05). If upload and paste both fail, pair with another platform |
| Gemini | Re-upload the whole skill. Use the Sheet for the outcome step | Reopen | Rebuild from the kit. Time the re-upload |

### Proof items outside the patterns

| Id | Platform | Check |
| --- | --- | --- |
| G2-PF-01 | Copilot | `.txt` copies of `.md` files work as knowledge. `.xlsx` with one sheet each works |
| G2-PF-02 | ChatGPT | ChatGPT Work file output with formulas on Plus. Which project memory mode allows it |
| G2-PF-03 | Copilot | Code interpreter toggle and the embedded copy of the sheet |
| G2-PF-04 | Gemini | One skill run that asks for a Google Sheet with formulas. Whole-skill re-upload fits in the log save card time |
| G2-PF-05 | Copilot | No-license path: core brief 3,500 characters or fewer, job card 1,500 or fewer, one knowledge text 2,800 or fewer. Measure each kit |
| G2-PF-06 | All | 16 knowledge files at the end. Limit 20 |

**What to do if a test fails.** One platform fails: the step card says so and offers a pair or a changed step. Two or more fail the same step: bring it back to me before Gate 2 locks.

**My view on the evidence.** Platform facts rest on vendor docs dated 2026-09 to 2026-11. Gemini skills (gm-01) have no dated vendor doc, and Copilot's code interpreter on embedded files conflicts between two docs. These are the real risks. P2 and P3 test them.

## 6. Critic results and what changed

The critic saw only the spec, the case and the rules. Not the planner's reasoning. It found 5 must-fix items and several consider items. The planner revised once.

**Must fix: all 5 fixed.**

| # | Critic finding | What the planner changed | Why |
| --- | --- | --- | --- |
| 1 | The module 4 template already held the fix for the planted error | Removed own-evidence checks and rules from the template. The learner writes the own-evidence rule in step 4 | With them in, the agent flags RM-14 on run 1 and the audit finds nothing |
| 2 | Module 2 check said "serves strategy". That contradicts the rule that the agent never judges fit | Now: strategy or OKR text that may relate, quoted, or "none found". No fit statement | Keeps your core rule |
| 3 | The spec listed 18 knowledge files. The budget said 16 | Aligned to the case README: 16 files, counts 4, 8, 11, 14, 16 | Strategy and OKRs are one file. The source pack is a run file |
| 4 | Module 4 inputs were wrong. The validated problem backlog is a module 4 run file | Step 2 now sends the validated problem backlog and the evidence log. The evidence log is in the inputs | The audit of own evidence needs the log |
| 5 | Module 4 objectives pointed to steps that do not practice them | Step 4 is now the rule write. Old steps 5 and 6 merged into one. The rerun stays in the debrief | Six steps kept |

**Consider items: changed.**

| Critic point | Change |
| --- | --- |
| Module 5 card text told learners where the error is | Step 5 is "Audit 2 'on track' measures". The rule write moved to the debrief. The range stays in step 2 |
| Module 2 card text pointed at the error | The step is "Audit 3 cards and 2 cited log entries" |
| Module 3 "ranks assumptions" was close to the core rule | Now "lists in the order of the sheet's swing column" |
| Sample flag report had wrong ids and marking | Fixed. DL-2026-09 is in the request decision log. The note is marked "Share with the Delivery lead and the Support lead". The packet uses the case facts |
| Rung 3 had no written rule text | Added: only a request with a recorded yes passes to the roadmap job |
| Module 4 had two core messages | One remains: roadmap is direction, release plan is the promise. Own evidence is the audit finding |
| The roadmap job was missing from the take-home builds | Added |

**Consider items: not changed, with reasons.**

| Critic point | Why not |
| --- | --- |
| m3-o4 (gate recommendation) is practiced only in the debrief | Kept as a debrief objective. It is the PM decision record. I would accept this. If the card test shows it is too thin, add a step |
| 2.3F claimed with no practicing step | Dropped 2.3F instead (a change in the mapping, not in the lab) |
| 2.2E says "uses scoring outputs" | No spec change. The reviewer note is in the mapping, gap 2 |
| Module 5 lab is tight (25 minutes, 6 steps) | Not changed. The card test measures it. I share this concern. Decision 2 adds up to 15 seconds there |
| Lab 1 data line in the flag report | Waits for decision 2. I recommend dropping it |
| Grouping of validated problems (DD-07) | Left open as decision 6. I disagree with the planner here |
| Case date mismatch | Not edited. Needs your yes (Q6) |

**Critic passes worth knowing.** One workflow and bottleneck per module. Timing: 360 teaching minutes, 195 and 195 in half days. Gate 1 decisions a to k reflected. No scoring, no Strategy Matrix lab, no CAW-AI agent. Zero em or en dashes in spec, brief and case.

## 7. Open items

| # | Item | Owner | Need from you |
| --- | --- | --- | --- |
| 1 | **Bond story.** Held to the module 1 deck build (Stage 3). Lean: Trendslop. Intel plus Trendslop is a possible pair. No HBR numbers on slides until a licensed copy is read. The syllabus does not name a story. Do not reuse Juicero, WeWork, Jitterbug or "maxed out employees" | Dan | None now. Pick before module 1 is built |
| 2 | **Fingerprinted research text that conflicts with your Gate 1 decisions.** See the table below. The spec follows your decisions. Later agents read these files | Dan | **Yes or no** to fix the 4 files and record new fingerprints |
| 3 | **sp-wf-13 (funding scenarios) placement.** `gate-1-decisions.md` makes it a stretch in module 1. `stage-2-inputs.md` says module 2. The spec follows module 1. It fits there: the PM names both scenarios and the agent shows what slips | Dan | **Yes or no** to module 1 |
| 4 | **Name-check.** Larkspan suppliers and customers need a check against real firms: Brindle RF Components (antenna supplier), Corvane Tooling (tooling supplier), Quillfern Pharmacy Group (customer). They appear in 11 case files and in the lab 4 flag. I cannot search the web from this task. Run a web and trademark search. Rimecore and Vantafrost carry over from Market Research | Dan | **Yes or no** to rename if a match is found. Rename cost: one find-and-replace across the case, plus the expected results |
| 5 | Proof kit draft briefs (section 5) | Planner | Yes or no |
| 6 | Overlap checks: workshops on strategic transformation and on implementation and action planning (capability 2), and the partner roadmap course (module 4) | Dan | Before the Pragmatic review |
| 7 | House rule 11 recheck when the Focus AI-forward version is final. It will include a market sizing agent and a roadmap translator. Module 3 has a basis check inside the business case. Module 4 has no audience drafting | Dan | When Focus is final |
| 8 | Evidence before slides: open the primary Atlassian report and the fieldwork method for N21 before any figure goes on a slide. Licensed HBR copy for E3. Several module claims have gaps (no 2026 product-team source on stale business cases or outcome tracking). Say "warning signs include", not a statistic | Research rerun | Before modules 1 and 2 are built |
| 9 | Recheck the platform matrix within 30 days of release | Researcher | Before release |
| 10 | Schedule and second-agent features need dated vendor docs before any stretch step is on a card | Stage 3 | Before module 3 is built |

**Item 2 detail: fingerprinted files and the conflicts.**

| File | Text | Conflicts with | Proposed fix |
| --- | --- | --- | --- |
| `research/workflows.yaml`, sp-wf-07 input | "the latest scored opportunity list" | Decision d: no scoring | "validated problem backlog" |
| `research/workflows.yaml`, sp-wf-08 | Audience notes and Now, Next, Later | Decision c option 1 and PS-05 | Remove audience notes. Use "timeframes" |
| `research/workflows.yaml`, sp-wf-03 | "layer", top-down and bottom-up | PS-06: use Pragmatic terms, define them | Use market, market segment, evaluator adoption, projected share |
| `research/worked-example-row.yaml` | The provisional decision e data safety text | Decision e is now a design question (decision 2) | Update after decision 2 |

I recommend yes. Old text left in these files would bring scoring and audience drafting back when Stage 3 agents read them.

**Gate 1 follow-ups already applied.** Title line (decision g). ChatGPT Plus as a prerequisite (f1). Copilot, Gemini, search, blind run and CSV rules (f2 to f6). Larkspan with strategy, OKRs and KPIs (j). Problem backlog term. Validated problem backlog term (PS-09). No audience drafting (c, working choice).
