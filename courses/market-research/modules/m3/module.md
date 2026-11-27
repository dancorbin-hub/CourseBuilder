# Module 3: The weekly run: read flags, not every item

Course: Advanced AI for Market Research (`market-research`). Stage 3 draft by the module builder, 2026-11-27. Revised once on 2026-11-27 after the consistency and verifier reports (`revision-notes.md`). Case year is 2027 (`case/year-shift-map.md`). Real source and vendor dates stay 2026. Built from `spec.yaml` (Gate 2, approved 2026-11-26; module 3 entry, `stretch_scope`, `platform_matrix_summary.stretch_verification`, `gate_2_proof_patterns` P2), `outline/development-brief.md`, `outline/gate-2-decisions.md`, the case files, `research/stretch-verification-2026-11.md`, the approved module 1 (`modules/m1/`, Gate 3 decisions D1, D7, D11, D12 and D13, Gate 4 decision G4-1) and the module 2 draft in review (`modules/m2/`, decisions in its section 1 and `revision-notes.md`). Starts from `modules/m2/kit/kit-m3/`.

## 1. Summary

| Item | Value |
| --- | --- |
| Workflow row and bottleneck | mr-wf-03 (folds mr-wf-04 as a stretch step). Route each week's inbound customer feedback into the problem backlog. Bottleneck: feedback is spread across many tools. Tagging by hand is slow, subjective and does not scale. Tags drift, so trends become unreliable (W4, W5) |
| Framework category and focus area | Market. Market Problems |
| Capability Standards (as in spec) | Confirmed by Dan, Pragmatic to confirm. Skills 1.1 Market Problem Identification, 8.1 Market Data Context and Pattern Recognition. Competencies 1.1B, 1.1C, 8.1B, 8.1D |
| Rung | 2, Recurring run with a flag report. Core path: a hand-started run on week 2 on all 4 platforms. Schedule: stretch, Claude card only (test pending) |
| Minutes (full day / half day) | 60 / 60 (same in both) |
| Instructor-led / hands-on (minutes, %) | 24 / 36 = 40% / 60% (8 + 8 + 8 = 24; 28 + 8 = 36). Inside the 40/60 rule (plus or minus 5 points) |
| Planted error and warning level | Forced fit hides a new problem: F-1215 to F-1219 in `m3-feedback-week-2.csv` (5 items, 4 accounts: A-08, A-17, A-22, A-31) ask for inspector read-only remote access. The agent tags them P02 Compliance report effort. P02 jumps from 3 to 7 accounts and the "no fit" group stays near empty. Warning: hint ("Audit before you approve.") |
| Learner evidence | Flag report decisions for week 2. Audit findings for 10 items and the "no fit" group. The "no fit" rule added to the brief (v3 to v4). Which problems move and which need discovery. All on `lab-3-record-sheet.md` |
| Agent after this module (files) | Instructions: brief v4. Knowledge: `job-card-problem-backlog`, `code-book`, `problem-backlog` (updated with feedback, P09 and P10), `job-card-win-loss`, `driver-code-book`, `driver-log`, `job-card-weekly-feedback` (new), `tag-list` (new). 8 knowledge files. Catch-up: `kit/kit-m4/` |

### Slide minutes check

| Arc step | Slides | Minutes | Mode |
| --- | --- | --- | --- |
| Why this matters, workflow and bottleneck | 3.1 to 3.4 | 1 + 2 + 2 + 3 = 8 | Instructor-led |
| Live demo | 3.5, 3.6 | 6 + 2 = 8 | Instructor-led |
| Build pattern and lab brief | 3.7 to 3.11 | 2 + 2 + 1 + 2 + 1 = 8 | Instructor-led |
| Lab 3 | 3.12 | 28 | Hands-on |
| Debrief | 3.13 to 3.17 | 3 + 2 + 1 + 1 + 1 = 8 | Hands-on |
| Total | 17 slides | 60 | 24 + 36 |

Full day and half days use the same 60 minutes (spec module 3 has no `half_day` block). Debrief minutes follow the spec arc: rerun 3, reveal and "what makes an agent say no fit" 2, check sample 1, what you do Monday 1, log save card 1.

### Builder decisions inside the spec

| # | Decision | Why |
| --- | --- | --- |
| B1 | The debrief rerun (3 minutes) runs in a new chat with both exports: "In a new chat, send both exports with the prompt 'Run the weekly feedback job'." The brief runs batches in date order, so week 1 runs first and week 2 compares with it | Same reason as module 1 D1 (approved) and module 2 B1: a new chat is the only way to be sure the tuned brief applies on all 4 platforms. See decision D3 |
| B2 | The lab brief is 2 short slides. 3.10: goal, 6 key actions and a pointer to the step card in the workbook. 3.11: done when, hint and data safety box. Full steps only on the step cards | Dan's lab brief slide rule (2026-11-27). Same pattern as module 2 B2 |
| B3 | "Which problems move in the backlog" has no minutes in the spec debrief. It is asked on 3.13 while the rerun runs, and recorded in section 4 of the record sheet | The spec debrief minutes add up to 8 without it. The PM decision (spec `pm_decision`) still gets practice. Same pattern as module 2 B3 |
| B4 | The check sample result on 3.15 comes from a tuned instructor project built from `kit-m4` before class. The live demo runs on brief v3, which has no "no fit" rule, so its check sample result would show the error | The spec says "the m3-check-sample.md result from the demo run". A result from the untuned brief cannot show the pass condition. See decision D4 |
| B5 | No audit hint beyond the spec step. The record sheet asks for 10 item IDs at random from the week 2 run, and every item in the "no fit" group. Its checklist is neutral ("The tag is right for the item") | Module 1 D11: the audit hint was for lab 1 only. Warning level for lab 3 is "hint". Slide 3.7 does not say where new things show up (consistency finding 10). See decision D13 |
| B6 | The survey wave stretch (row 04 fold) is on all 4 cards, but only after step 6 | The survey CSV column names say "inspector remote access". Before the audit, the stretch file would give the planted error away. See decision D6 |
| B7 | Schedule stretch: Claude card only (Cowork scheduled task, cl-sc-07), marked "not yet tested by the course team", and added to the card test. ChatGPT card: "The schedule stretch step is not available on this platform in this course" plus the reason (cg-06). Copilot and Gemini cards: the standard `stretch_scope` line | Dan, 2026-11-27, and `research/stretch-verification-2026-11.md`. The Claude steps follow the verifier rewrite (6 steps, 1 action each), with the **Scheduled** sidebar path as a fallback. See decisions D1 and D11 |
| B8 | Slide 3.3 uses a general example ("one account, five tickets"), not the case account A-05 | A-05 sends 5 alert items in week 2. It is a secondary check in the debrief (`planted-errors.md`). The rule is taught; the case example stays for the reveal |
| B9 | On-slide bottleneck line on 3.2 uses only the claim with 2 sources: "Tagging by hand is slow and inconsistent" (W4, W5). "Spread across many tools" (W4 only) and "label meanings drift" (W5 only) are in the talk track, attributed to the vendor | Research rule 2: a factual claim needs 2 independent sources. See decision D7 |
| B10 | The job card keeps the tag list's table name "What moved" when it points to the format. Learner-facing text says "what changed summary", as the spec does | `case/m3-tag-list.md` is fingerprinted and says "What moved". The spec and expected results say "what changed". See decision D10 |
| B11 | kit-m4 `tag-list.md` is version 2: it adds P10 Inspector remote access, with a definition written from the case flag entry. The case file `m3-tag-list.md` does not change | `case/planted-errors.md` gives the PM decision "Add P10 to the backlog and the tag list". `case/expected-results.md` names P10 "Inspector remote access". The kit-m4 README and slide 3.17 say kit-m4 holds this decision. See decisions D2 and D8 |
| B12 | kit-m4 `problem-backlog.md` uses the code book format with the facts of `m4-evidence-pack.md` Part 4. It adds the week 1 counts, the agent's proposed ranking and the case PM's lab 3 flag decisions. Flags with no case PM decision (F-1124, F-1232) say "Your decision" | `case/expected-results.md` kit table: kit-m4 "Problem backlog as in Part 4". Same approach as module 2 D4 and D6. See decision D9 |
| B13 | The Copilot no-license fallback holds brief v3 with the kit's lab 1 and lab 2 rules. Total 6,856 characters | Spec P2 runs the fallback for module 3. Under the 7,800 course budget and the 8,000 limit (mb-01). The no-license box sends the backlog in its own message at step 2 and again at the debrief rerun. See decision D5 |

### Decisions for Dan

Open decisions for the Gate 3 doc, most important first. One line each, with a recommendation. Revised once on 2026-11-27 (`revision-notes.md` maps the old numbers).

| # | Decision | Recommended |
| --- | --- | --- |
| D1 | Claude schedule stretch ships before your hands-on test, marked "not yet tested". If your test fails, option B removes it from 5 places: the Claude card stretch, slide 3.9 on-slide text and talk track, section 7 "Steps per platform", and the 2 Claude stretch rows in section 9 | A: keep, marked. Your test uses the card test rows (incl. new Claude experience and cloud move) |
| D2 | After lab 3 the learner's backlog and tag list have no P10; kit-m4 has it (the case PM's decision). A: keep; the kit-m4 README and the 3.17 talk track say so (applied). B: the log save card also loads `kit-m4/tag-list` on the case path (changes the learner path) | A. The module 5 builder checks if lab 5 needs P10 in the learner's own backlog |
| D3 | Debrief rerun in a new chat with both weeks (3 minutes). B: same chat, week 2 only. The card test times it | A. Switch to B if the rerun runs over 3 minutes on 2 or more platforms |
| D4 | Check sample on 3.15 shown from a tuned project built from `kit-m4` before class (brief v3 in the live demo cannot pass) | A: accept |
| D5 | Copilot no-license: each paste is one file group (backlog alone 10,004; then the export or exports, at most 8,873), under the 15,400 target. Microsoft publishes no message limit (Support page, ms.date 2026-10-31). Card test decides | A |
| D6 | Survey wave stretch only after step 6, because its column names give away the new problem | A: accept |
| D7 | Slide 3.2 shows only "Tagging by hand is slow and inconsistent" (W4, W5). "Spread across many tools" and "tags drift" stay in the talk track, attributed | A: accept |
| D8 | kit-m4 tag list v2 adds P10 with a definition written from the case flag entry. B: tag list stays v1, P10 in the backlog only | A |
| D9 | Lab 3 flags with no case PM decision (F-1124, F-1232) say "Your decision" in the kit-m4 backlog | A: keep |
| D10 | The tag list says "What moved"; the spec says "what changed". Keep both (table name and learner text) | A |
| D11 | ChatGPT card: "The schedule stretch step is not available on this platform in this course", with the reason (not the standard line, because module 4 may give ChatGPT the second-agent stretch) | A |
| D12 | Story slot on 3.4 (internal platform team, loudest channel; W18, one source) | Supply one real Pragmatic story, else skip path |
| D13 | Card and record sheet say the audit uses the week 2 run. Too much of a hint? | A: keep. The spec success check is about week 2 |
| D14 | Card pass condition says "run this after class", not "in the debrief" | A: accept |

### Changes needing Dan's yes

None of these are made. Each waits for your yes.

| # | File (fingerprinted or approved) | Change | Why |
| --- | --- | --- | --- |
| 1 | `spec.yaml`, module 3 `arc` (debrief) and `check_sample` | "the m3-check-sample.md result from the demo run" becomes "the m3-check-sample.md result from a tuned instructor project (kit-m4), run before class" | Only if D4 is A |
| 2 | `spec.yaml`, module 3 `arc` (debrief) and `debrief_check` | "Rerun week 2 with the new rule" and "after the rerun of week 2" become "Rerun weeks 1 and 2 in a new chat with the new rule" | Only if D3 is A |
| 3 | `spec.yaml`, `planted_error_fade.success_checks` | Add: "Modules 3 and 4: the card marks the pass condition 'run this after class' (spec `check_sample`)" | Only if D14 is A. The current text says "run this in the debrief" |
| 4 | `spec.yaml`, `stretch_scope.schedule_and_second_agent_stretch` and `platform_matrix_summary.stretch_verification.rule` | Add: "A step verified by a dated vendor doc may ship marked 'not yet tested by the course team' until Dan's test. If the test fails, the card uses the standard line" | Only if D1 is A. The rule asks for a doc and a test |
| 5 | `spec.yaml`, module 3 `stretch` item 1 | "Set a schedule or a file trigger. Only on step cards where verified" becomes "Schedule: Claude card only (Cowork scheduled task, cl-sc-07, Dan test pending). ChatGPT: not available (cg-06). Copilot and Gemini: standard line" | Matches Dan's 2026-11-27 decision, as the module 2 stretch line was updated |
| 6 | `research/platform-matrix.yaml` | cl-sc-07: source_date 2026-11-18, checked_on 2026-11-27, screen names (**Scheduled**, **New task**, **Set up manually**, the "Create scheduled task" fields incl. approval mode, **Save**) and 3 limits (Computer access; tasks move to the cloud on Pro, Max, Ultra; new Claude experience). New row cl-ui-11 (Cowork projects: **Projects**, **+**, **Import from project**, "Search projects in Chat…", save location, **Create**, per-project **Scheduled tasks**; 14116274, 2026-11-12). New row mb-ui-16 (no published Copilot Chat message limit; Support page, ms.date 2026-10-31) | Verifier report, last section. The cards use these names and limits |
| 7 | `research/workflows.yaml`, row mr-wf-03 evidence W4, W5, W18 | checked_on 2026-11-27 (quotes found again) | Verifier report |

## 2. Slides and talk track

### Slide 3.1: Module 3. The weekly run: read flags, not every item
- Layout: Chapter Break
- Minutes: 1
- On-slide text: MODULE 3. The weekly run. Promise: "Read the flags, not every item." Bullets: Add a weekly feedback job. Count accounts, not mentions. Make the agent say "no fit".
- Visual intent: Teal side band, "MODULE 3" tag. Small rung icon: rung 2 lit, with a weekly calendar loop.
- Sources: none

Notes:
```
POINT: In this module your agent gets its third job: it reads each week's customer feedback into the problem backlog.
Talk Track:
Your agent has two jobs now: the problem backlog and win/loss.
Both ran on one batch, by hand. That is rung 1.
Today it climbs to rung 2: a run that repeats every week.
Feedback does not arrive in batches. It arrives every day.
So the job runs each week, and you read only what it hands you.
Same agent. Same brief. One new job card and one tag list.
TRANSITION: First, the workflow and what slows it down.
```

### Slide 3.2: Feedback every day. Who reads it all?
- Layout: Blank
- Minutes: 2
- On-slide text: Headline: "Feedback every day. Who reads it all?" Line: "Tagging by hand is slow and inconsistent." Workflow strip: "Each week's feedback export, then tagged items, a what changed summary and a flag report."
- Visual intent: Headline in navy. Four small channel icons (ticket, call note, install note, request form) feeding one strip. Strip ends in three outputs. No numbers.
- Sources: W4 (claim, ProductPlan, 2026-06-02) and W5 (claim, Enterpret, 2026-07-27). Both are vendors, independent of each other. No figure from either (decision D7)

Notes:
```
POINT: Feedback arrives every day, and tagging it by hand is slow and inconsistent.
Talk Track:
Here is the workflow for this module.
Support tickets. Sales call notes. Install notes. Feature requests. Requests that other teams pass on.
Every item could tell you something about a market problem.
Somebody has to read each one, tag it and count it.
Two vendor pages from 2026 say the same thing about that work.
ProductPlan, a roadmap tool vendor, says tagging feedback is slow and subjective, and insights sit in different tools.
Enterpret, a feedback analytics vendor, says tags get applied in different ways, and their meaning drifts over time.
Both sell tools for this work. So treat it as their experience, not a study.
When the tags drift, the trend lines lie.
[ASK: "What happens to your pile when nobody has time to tag it?" TAKE 1 ANSWER]
At Larkspan, our case company, one of the current market questions is: "Which new problems show up in weekly feedback?"
That is the question your agent answers today.
TRANSITION: Before the agent, one rule for counting.
```

### Slide 3.3: Count accounts, not mentions
- Layout: Blank
- Minutes: 2
- On-slide text: One account, five tickets: 1 account. Pervasiveness: how many accounts and segments. A loud channel is not a widespread problem.
- Visual intent: Left: 5 ticket icons from one building, with "= 1 account" in orange. Right: 5 buildings with one ticket each, "= 5 accounts" in teal.
- Sources: none (spec quality check "Counts are by unique account"; glossary "pervasiveness")

Notes:
```
POINT: The agent counts each problem by unique account, because one loud account is not the same as many accounts.
Talk Track:
You know pervasiveness from discovery work: how many accounts and segments have the problem.
Weekly feedback breaks that count if you are not careful.
One account with a bad week can send five tickets about one freezer.
Count mentions, and that problem jumps by five.
Count accounts, and it moves by one.
The one with five tickets has an urgent problem. That is worth knowing.
But it is one account. It does not tell you how far the problem reaches.
So the job card has a quality check: counts are by unique account.
And the summary shows both: accounts, and items this week.
[ASK: "Which of your feedback channels is the loudest? Is it the widest?" TAKE 1 OR 2 ANSWERS]
TRANSITION: The same trap waits for internal product managers.
```

### Slide 3.4: Internal platforms: the loudest team is not the widest need
- Layout: Blank
- Minutes: 3
- On-slide text: Fleet Data Platform (internal). Customers: Support, Install, Customer Success, Finance. Count teams, not messages. Passed-on feedback: count the customer account.
- Visual intent: One platform tile in the center. Four team tiles around it. One team tile has many message bubbles; the other three have one each. Bottom line in teal.
- Sources: none (case `company.md`, internal PM; Gate 2 decision 9). Story slot: W18 (Enterpret, 2026-11-04, one source, example only)

Notes:
```
POINT: An internal platform PM counts the teams and accounts behind each request, not the number of messages.
Talk Track:
Larkspan has one internal product: the Fleet Data Platform, or FDP.
It shows device health, firmware status and install status.
Its customers are other teams: Support, Install, Customer Success and Finance.
They send requests through an intake form. They also pass on what customers tell them.
The trap is the same as on the last slide.
The risk is that the team that writes the most gets served first.
So the FDP PM counts teams, not messages. Teams are the accounts here.
Second point. When Customer Success passes on a customer's feedback, whose feedback is it?
The customer's. Count the customer account, not the team that passed it on.
You will see items like that in the case export, in the channel "Internal intake (Customer Success)".
In hardware, install notes and technician notes can hold product feedback too.
The Larkspan export has an "Install note" channel for that reason.
[OPTIONAL STORY SLOT, 1 MINUTE. Topic: an internal platform team where the loudest Slack channel got served first, and what changed when the PM counted teams. Use only a story from Pragmatic's work with companies or from a client team. Tell it as their story, never as your own. If you have no such story, skip this slot and ask: "Who is the loudest internal customer you serve?" Take 1 or 2 answers]
[IF ASKED FOR A SOURCE] One vendor page, from Enterpret, describes this for platform PMs. One source, so we use it as an example only.
TRANSITION: Let me add the weekly feedback job in front of you.
```

### Slide 3.5: Live demo. Add the weekly feedback job
- Layout: 1_prompt
- Minutes: 6
- On-slide text: LIVE DEMO. "Add the weekly feedback job. Run week 1, then week 2." Running example: Larkspan Systems, feedback weeks of 2027-11-02 and 2027-11-09. 6 MIN.
- Visual intent: Orange "LIVE DEMO" tag. Platform logo for the demo platform (Claude). Small list: 2 new files, 2 run files.
- Sources: cl-pj-01, cl-ui-09 (platform matrix, verified). Demo script in section 3

Notes:
```
POINT: Adding the weekly job takes two files, and each week is one run with one prompt.
Talk Track:
[SWITCH TO THE DEMO PLATFORM. FOLLOW THE DEMO SCRIPT IN SECTION 3, STEPS 1 TO 4]
Here is the agent after module 2. Brief v3 in the instructions. Six files in knowledge.
I add two files: the weekly feedback job card and the tag list.
The tags are the problem codes from the backlog. Each tag has a definition.
I do not touch the brief.
[ADD THE 2 FILES. SEND WEEK 1 BY MINUTE 1 OF THIS SLIDE, AND TALK OVER THE RUN]
New chat. Week 1 export. One prompt: "Run the weekly feedback job".
[SEND. WHILE IT RUNS:]
Week 1 has 24 items. Five channels. Three segments.
The agent tags each item, or says "no fit". It counts by account. It writes into the same problem backlog as module 1.
[WHEN WEEK 1 ENDS, SAY:] Week 1 has no last week to compare with. Week 2 does.
Same chat. Week 2 export. Same prompt.
[SEND. WHILE IT RUNS:] Week 2 has 32 items. Now the agent compares the two weeks.
[IF WEEK 2 IS NOT DONE AT MINUTE 6, OPEN THE REHEARSAL OUTPUT AND MOVE ON. LET THE LIVE RUN FINISH IN THE BACKGROUND]
[WHEN THE RUN ENDS, OPEN THE OUTPUT]
TRANSITION: Here is how you read it, without reading all 32 items.
```

### Slide 3.6: Read the weekly report: four parts
- Layout: Blank
- Minutes: 2
- On-slide text: 1. Tagged items: one tag or "no fit", with a quoted reason. 2. What changed: accounts per tag, last week and this week. 3. The "no fit" group. 4. Flag report: your decisions go here.
- Visual intent: A cropped, readable mock from the demo run: 2 tagged item rows (F-1222 P04, F-1229 P09), the what changed header row, the flag report header. Large type. Numbers 1 to 4 in orange circles.
- Sources: none (case `m3-tag-list.md` formats, `m3-feedback-week-2.csv`)

Notes:
```
POINT: You manage the weekly job by reading the summary, the "no fit" group and the flags, not every item.
Talk Track:
[DEMO SCRIPT STEPS 5 TO 8. STAY ON THE SCREEN, THEN SHOW THIS SLIDE AS THE SUMMARY]
One. Tagged items. Each item gets one tag, or "no fit". Each tag has a reason that quotes the item.
F-1222, Harlow Bay Foods: "Battery replacements again on 12 sensors." Tag P04, sensor upkeep.
Two. What changed. For every tag: accounts last week, accounts this week, the change, and the items.
Three. The "no fit" group. Items that fit no tag.
Four. The flag report. The decision column is blank. That is yours.
[DO NOT COMMENT ON ANY COUNT, ANY CHANGE OR WHAT IS IN THE "NO FIT" GROUP. IF A LEARNER ASKS:] Good question. Hold it for your audit.
[SAVE THE DEMO OUTPUT FILE. YOU MAY NEED IT IN THE DEBRIEF]
TRANSITION: This is what rung 2 means for you as the manager.
```

### Slide 3.7: Rung 2: read the flags and a sample
- Layout: Blank
- Minutes: 2
- On-slide text: Rung 2: recurring run with a flag report. Each week you read: the flag report, the what changed summary, 10 random items, every "no fit" item. You do not read every item.
- Visual intent: Ladder graphic, rung 2 lit. Right side: a short "You read" list with 4 check marks, and one crossed-out line "every item".
- Sources: none (spec `autonomy_ladder` rung 2)

Notes:
```
POINT: At rung 2 the agent runs each week, and the manager reads the flags and a sample.
Talk Track:
Rung 1 was a hand-run batch. You read every flag and audited a sample.
Rung 2 repeats every week. Your time does not grow with the pile.
Each week you read four things.
The flag report: the items the agent stopped on.
The what changed summary: every tag, with its change in accounts.
A random sample of 10 tagged items. That is your audit.
And every item in the "no fit" group.
You do not read every item. That is the point of the job.
Your sample is how you keep trust in the items you do not read.
TRANSITION: What the agent reports, and what it must never decide for you.
```

### Slide 3.8: Report every change. Call no trend.
- Layout: Blank
- Minutes: 2
- On-slide text: The agent reports the change in accounts for every tag. Every "no fit" group goes to the flag report. No number decides what you see. One week is not a trend. You decide what needs discovery.
- Visual intent: The what changed table header (Tag, Accounts last week, Accounts this week, Change, Items this week) with blank rows. The line "One week is not a trend" in orange.
- Sources: none (spec module 3 `no_threshold`, `handoff_rules`; case `company.md` hand-off rule 4)

Notes:
```
POINT: The agent reports every change and flags every "no fit" group, and only the PM decides which changes matter.
Talk Track:
A "top movers" view lets a number decide what you see.
This job does not.
The case PM's hand-off rule says: report the change in accounts for every tag. Send every "no fit" group to the flag report.
No number in the brief says "a jump of 3 is news".
And the agent never calls a one-week change a trend. One week is a fact. A trend is your call, over time.
One more hand-off rule. Any item that holds personal or health data goes to the flag report.
The agent does not copy that data into the backlog.
You read the changes. You decide which ones need discovery interviews.
TRANSITION: You start this run yourself. Here is why, and where a schedule fits.
```

### Slide 3.9: Who starts the weekly run?
- Layout: Blank
- Minutes: 1
- On-slide text: Core path, all 4 platforms: you start the run when the export arrives. Schedule: stretch on the Claude card only. Not in this course: ChatGPT, Copilot, Gemini.
- Visual intent: Two rows. Row 1: 4 platform logos with a hand icon ("you start it"). Row 2: Claude logo with a clock icon ("stretch"), the other 3 logos grayed. No setup screens.
- Sources: `research/stretch-verification-2026-11.md` (2026-11-27): cl-sc-07 verified by doc (support article 13854387, 2026-11-18), test pending; cg-06 (a project task cannot read project files); mb-06 not verified; gm-07 not for Workspace accounts. Spec `stretch_scope.slides` (name the gap once)

Notes:
```
POINT: You start the weekly run, and a schedule is a stretch only where the course verified it.
Talk Track:
In this lab you start each run by hand.
A schedule with no new input does nothing. With no connectors, the new export has to reach the agent somehow. Today, you bring it.
On Monday, you can also run it by hand when the export lands. That is still rung 2.
A schedule is a stretch step on the Claude card only. It uses Claude Cowork scheduled tasks, on paid plans.
The course team has checked the vendor doc. A hands-on test is still open, and the card says so.
ChatGPT can schedule tasks, but a task in a project cannot read the project's files. So no tag list, no backlog.
Copilot's agent builder schedule has no Microsoft doc we can check yet. Gemini's schedule for skills works on personal accounts only.
So those three cards stay on the core path.
[DO NOT SHOW SETUP SCREENS FOR ANY PLATFORM. THE CLAUDE CARD HAS THE STEPS]
TRANSITION: Here is your lab.
```

### Slide 3.10: Lab 3 brief
- Layout: Activity
- Minutes: 2
- On-slide text: ACTIVITY. Lab 3: Add the weekly feedback job. Goal: Tag a week of feedback against your backlog. Report what changed. Key actions: Add the job. Run week 1. Run week 2. Decide each flag. Audit 10 items and the "no fit" group. Add a "no fit" rule. Footer: "Full steps: your step card in the workbook (Pragmatic Learning Hub)."
- Visual intent: Orange "ACTIVITY" band. Goal at the top. 6 short key actions in large type. Workbook pointer in the footer. Nothing else on the slide.
- Sources: none

Notes:
```
POINT: In lab 3 you add the weekly job, run two weeks, and manage it by flags and audit.
Talk Track:
The goal of this activity is to extend your agent to tag a week of feedback against your backlog.
Then it reports what changed.
The core message: the hard part is not the tagging. It is the rule that makes the agent say "no fit" instead of guessing.
These are the key actions. The full steps are on your step card in the workbook.
You downloaded the workbook from the Pragmatic Learning Hub. Open your platform's card now.
[WALK THE KEY ACTIONS IN ONE LINE EACH. DO NOT READ THE CARD ALOUD]
On your own work: one or two weeks of feedback items, with personal data removed, from an approved tool.
Otherwise use the Larkspan files. Both paths use the same steps.
Record your decisions on the lab 3 record sheet in your kit. That is your evidence.
TRANSITION: Here is what done looks like.
```

### Slide 3.11: Lab 3: done when
- Layout: Activity
- Minutes: 1
- On-slide text: ACTIVITY. Done when: The week 2 what changed summary is complete, counted by account. Each flag has your decision. You audited 10 items and the "no fit" group. You added a "no fit" rule. Orange box: "Audit before you approve." Data safety box (standard text): "Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss."
- Visual intent: Orange "ACTIVITY" band. Success check as 4 short lines on the left. Orange box on the right. Standard data safety box at the bottom, the same box as the step cards.
- Sources: none (spec `planted_error_fade` module 3; spec `data_safety_note`; module 3 `data_safety`)

Notes:
```
POINT: The success check names the outputs and your manager actions, and the data safety rule covers support tickets too.
Talk Track:
The goal of this activity is to know what done looks like before you start.
Done when: a complete week 2 summary, counted by account. Your decision on each flag.
10 audited items and the "no fit" group. And one new "no fit" rule.
[POINT TO THE DATA SAFETY BOX]
Same rule as before. Approved tool only.
One thing is new. Support tickets and call notes can hold health data, account numbers or card data.
Remove it before you upload. Your backlog keeps what the agent writes, week after week.
[POINT TO THE ORANGE BOX]
Audit before you approve.
Breakout rooms are by platform. Build and save your own agent. Share your screen only when someone is stuck.
Agent lost or behind? Rebuild it from kit-m3 first. It takes about 5 minutes.
TRANSITION: [OPEN BREAKOUT ROOMS BY PLATFORM. START THE TIMER: 28 MINUTES]
```

### Slide 3.12: Lab 3: Add the weekly feedback job
- Layout: Activity
- Minutes: 28
- On-slide text: ACTIVITY. 28 MIN. Time guide: 0 to 3: add 2 files. 3 to 9: run week 1. 9 to 14: run week 2. 14 to 18: decide each flag. 18 to 25: audit. 25 to 28: add your rule. "Build and save your own agent. Share your screen only when someone is stuck."
- Visual intent: Orange band. A timeline bar with the 6 blocks. Room by platform shown as 4 small tiles.
- Sources: none

Notes:
```
POINT: Learners add the weekly job and run two weeks from their step card, on own or case data.
Talk Track:
The goal of this activity is to run one full turn of the manager loop on your agent's weekly job.
[VISIT EACH ROOM IN TURN. START WITH COPILOT, THEN GEMINI, THEN CHATGPT, THEN CLAUDE]
[AT MINUTE 3: ANYONE WHO HAS NOT SENT WEEK 1 GETS HELP FIRST]
[AT MINUTE 9: "Send week 2 now, in the same chat, even if you have not read week 1."]
[AT MINUTE 14: "Decide your flags now. Then start the audit."]
[AT MINUTE 18: "Start your audit. Pick 10 item IDs at random. Open the export. Check the tags; do not trust them."]
[AT MINUTE 25: "Write your rule now, even if your audit is not done. The rerun is in the debrief."]
[COMMON FAILURES AND RECOVERY: SEE SECTION 9]
[DO NOT REVEAL THE ERROR. IF A LEARNER ASKS "IS THIS IT?", ASK: "What does that item ask for? Does the tag definition cover it?"]
TRANSITION: [CLOSE ROOMS AT MINUTE 28] Bring your record sheet. Keep your agent open.
```

### Slide 3.13: Rerun week 2 with your rule
- Layout: debrief
- Minutes: 3
- On-slide text: DEBRIEF. 3 MIN. New chat. Send both exports with "Run the weekly feedback job". While it runs: Which problems move? Which need discovery?
- Visual intent: Navy "DEBRIEF" band. Timer 3 MIN. One-line instruction. 2 questions below.
- Sources: none (spec module 3 debrief arc)

Notes:
```
POINT: The rerun tests the new rule, and the PM decides which problems move and which need discovery.
Talk Track:
Rerun now, on your tuned brief.
New chat. Both exports. Same prompt. The agent runs week 1 first, then week 2.
[START A 3-MINUTE TIMER]
While it runs, look at your week 2 summary from the lab.
Which problems move up or down in your backlog? Which need discovery interviews?
Write it in section 4 of your record sheet.
[AFTER 1 MINUTE, TAKE 2 ANSWERS]
[IF A LEARNER SAYS A PROBLEM "IS TRENDING":] One week. Is that a trend, or a fact to watch?
[IF A LEARNER'S RERUN IS NOT DONE AT 3 MINUTES:] Keep it running. We read the result together next.
TRANSITION: So what did your "no fit" group hold, before and after your rule?
```

### Slide 3.14: Audit reveal: what hid in your "no fit" group?
- Layout: debrief
- Minutes: 2
- On-slide text: DEBRIEF. Which check or audit found the error? What was in your "no fit" group? (Reveal after answers:) F-1215 to F-1219: 4 accounts want inspector read-only access, not a report. Tagged P02: 3 accounts became 7.
- Visual intent: Navy band. 2 questions. On click: F-1215 text, the P02 row before (3 to 7, +4) and after (3 to 3, 0), and the new "no fit" group of 4 accounts.
- Sources: none (case `planted-errors.md` lab 3, `expected-results.md` lab 3)

Notes:
```
POINT: The agent forced new items into the nearest tag, so the new problem hid until the audit.
Talk Track:
[ASK THE 2 QUESTIONS. TAKE 2 OR 3 ANSWERS]
[REVEAL]
Here is the planted error. Items F-1215 to F-1219. Five items from four Food service accounts.
F-1215, Bellweather Diners: "The county inspector wants to log in and see our cooler records herself before she visits."
They do not want a report. They want an inspector login, read-only, to the live records.
On brief v3, the agent tags them P02, compliance report effort. The words match: inspection, audit, report.
So P02 jumps from 3 accounts to 7. The biggest change of the week. And the new problem is hidden.
The reason check passes. Each reason quotes the item, and the quote has the words of the tag.
What makes an agent say "no fit"? A rule that checks meaning, not words:
"Tag an item only if it matches the tag definition, not only its words. If the item asks for something the definition does not cover, mark it no fit."
After the rule: P02 stays at 3 accounts. The "no fit" group holds the new problem, 4 accounts, and the flag report names it.
Two more checks in the same data.
A-05, Pellham Distribution, sent 5 alert items. Count mentions and P01 goes from 6 to 11. Count accounts: 6 to 7.
F-1221 holds a name and a phone number. Your hand-off rule must flag it, and the backlog must not keep it.
And one clue for next week: an empty "no fit" group, in a week with new content, is a reason to look.
[IF NO AGENT IN THE ROOM MADE THE ERROR, SHOW THE SAVED DEMO OUTPUT]
TRANSITION: Did your rule work on a week you have not seen?
```

### Slide 3.15: Check sample: a week you have not seen
- Layout: debrief
- Minutes: 1
- On-slide text: DEBRIEF. Check sample: a new week, tuned brief. F-1305 to F-1307: "no fit", not P06. Flagged: 3 accounts. P01: 2 accounts, not 4. Run it after class (about 5 minutes).
- Visual intent: Navy band. A screenshot of the instructor's saved check sample result, with the 3 pass items circled. Small card image with "after class".
- Sources: none (case `m3-check-sample.md`, `expected-results.md` lab 3 second sample)

Notes:
```
POINT: A week the learner has not seen shows if the "no fit" rule works, and learners run it after class.
Talk Track:
[SHOW THE SAVED CHECK SAMPLE RESULT FROM THE TUNED INSTRUCTOR PROJECT. SEE SECTION 3, "BEFORE CLASS"]
This is a third week, run on the tuned brief.
Three items ask for one thing: when an alarm fires, open a repair job with the refrigeration contractor.
None of them names a night or a weekend. So P06, after-hours response, does not fit.
The tuned agent says "no fit", and the flag report names the request across 3 accounts.
P01 shows 2 accounts, not 4. One account sent 3 of the items.
Run it yourself after class. About 5 minutes. The pass condition is at the end of your step card.
TRANSITION: So what do you do on Monday?
```

### Slide 3.16: What you do Monday
- Layout: Blank
- Minutes: 1
- On-slide text: "Export last week's feedback. Run the job. Read only the flag report."
- Visual intent: One line, large type. Calendar icon with "Monday".
- Sources: none

Notes:
```
POINT: The first real use of the weekly job is one export, one run, and one read of the flag report.
Talk Track:
On Monday, export last week's feedback from one approved tool. Remove personal data first.
Run the weekly feedback job on it.
Read only the flag report and the "no fit" group. Audit 10 items.
Do it again next week. That is rung 2.
TRANSITION: Last step: save your backlog so module 4 can read it.
```

### Slide 3.17: Save your backlog
- Layout: Activity
- Minutes: 1
- On-slide text: ACTIVITY. 1 MIN. 1. Download the backlog from your rerun. 2. Replace `problem-backlog` in your agent's knowledge. Your card has the steps for your platform.
- Visual intent: Orange band. Two numbered steps, large. Small platform row: Claude, ChatGPT, Copilot, Gemini.
- Sources: cl-pj-01, cg-01, mb-02, gm-01 (platform matrix); vendor docs on the cards

Notes:
```
POINT: Saving the updated backlog to the agent's knowledge lets module 4 build on it.
Talk Track:
The goal of this activity is to save your updated problem backlog. Module 4 reads it.
Take the backlog from your rerun, the one with your "no fit" rule. Not the lab run.
Download it. Replace the old problem-backlog in your agent's knowledge.
Gemini: replace the file in the skill. If that fails, upload the whole skill again.
Copilot without a license: keep the file on your computer. You paste it in chat next time.
If your rerun did not finish, kit-m4 has the backlog after week 2. Load that instead.
kit-m4 also holds the case PM's decision: P10 added to the tag list and the backlog.
On your own work, add your own new tag the same way.
TRANSITION: [MOVE TO MODULE 4]
```

## 3. Demo script

Platform: Claude (Project). Before class:

1. Have the project "Market Evidence Agent" in its state after module 2 (brief v3 in the instructions; 6 files in knowledge). Use `kit-m3` if the module 2 demo project changed.
2. Check that **Code execution and file creation** (or **Create and edit files**) is on.
3. Do one rehearsal run on the case files. Time each run. Save the rehearsal output and screenshots in your instructor folder.
4. Build a second project, "Market Evidence Agent (tuned)", from `kit-m4` (brief v4 and 8 files). Run `m3-check-sample.md` in it with "Run the weekly feedback job". Save the result and a screenshot for slide 3.15. Check it against the pass condition on the cards.
5. Keep a ChatGPT Project in the state after module 2 as the backup.

| Step | Instructor does | Screen shows | If it fails |
| --- | --- | --- | --- |
| 1 | Open **Projects**, then "Market Evidence Agent" | Brief v3 in the instructions. 6 files in project knowledge | Rebuild from `kit-m3` in about 5 minutes, or switch to the ChatGPT backup. Say: "This is what kit-m3 is for." |
| 2 | Select **+** in project knowledge. Add `job-card-weekly-feedback.md` and `tag-list.md` | 8 files in project knowledge | Paste both texts into the chat with the run in step 3 |
| 3 | Start a new chat in the project. Upload `m3-feedback-week-1.csv`. Send "Run the weekly feedback job" | 24 tagged items, a what changed table with last week "none", a flag report with the "no fit" item F-1124 (A-26, invoice currency), and the backlog. A downloadable file, or the full tables in one message | If no file: say "Rule 7 in the brief asks for the full tables in one message." If the run fails: switch to the ChatGPT backup. If both fail: show the rehearsal output |
| 4 | In the same chat, upload `m3-feedback-week-2.csv`. Send "Run the weekly feedback job" | 32 tagged items. The what changed table with accounts last week and this week for every tag. The "no fit" group. The flag report. The updated backlog | If the run stops halfway: send "Continue". If it fails, or is not done at minute 6 of slide 3.5: show the rehearsal output |
| 5 | Point to the tagged item F-1222 | F-1222, A-06 Harlow Bay Foods, Distribution, P04, reason quotes "Battery replacements again on 12 sensors." | If the tag differs, say: "That is what an audit is for." Do not fix it live |
| 6 | Point to the what changed table header | Columns: Tag, Accounts last week, Accounts this week, Change, Items this week | If the format differs, say: "The tag list sets the format. A different format is an audit finding." |
| 7 | Point to the "no fit" group and the flag report | The "no fit" items with their IDs and accounts. A blank PM decision column | If a flag is missing, say: "Hand-off rules are not perfect. That is why you audit." |
| 8 | Download the output file and save it | The file in your instructor folder | Use the rehearsal output in the debrief |

Do not comment on the P02 or P01 counts, on the size of the "no fit" group or on F-1215 to F-1219 on screen. The demo runs on brief v3, so the planted error may show. That is the lab's planted error (module 1 decision D5 pattern).

## 4. Lab brief

- Goal: Extend the course agent to tag a week of feedback against the problem backlog and report what changed.
- Core message: The hard part is not the tagging. It is the rule that makes the agent say "no fit" instead of guessing.
- PM decision: Which problems move up or down the backlog, and which new problems need discovery interviews.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Teaching point: support tickets can hold health data (PHI), account data or card data. Remove it before upload. The backlog keeps what the agent writes, week after week. Decide what it may keep and for how long.
- Setup: Zoom breakout rooms by platform, 3 to 5 learners. In person: tables by platform. Each card starts: "Build and save your own agent. Share your screen only when someone is stuck."
- Inputs: Own work: one or two weeks of feedback items (tickets, call notes, requests) with personal data removed, from an approved tool. Case: `kit/lab-3/` (job card, tag list), `m3-feedback-week-1.csv` and `m3-feedback-week-2.csv` (run), `m3-check-sample.md` (after class). Files this lab: 5 (2 to the agent, 3 in chat). Stretch: `m3-stretch-survey-wave.csv`.
- Planted error warning: Hint. "Audit before you approve."
- Success check: The week 2 "what changed" summary is complete and counted by unique account. Each flag has your decision. You audited 10 items and the "no fit" group and added a "no fit" rule to the brief.
- Learner evidence: Flag report decisions for week 2. Audit findings for 10 items and the "no fit" group. The "no fit" rule added to the brief (v3 to v4). Recorded on `lab-3-record-sheet.md`, with which problems move and which need discovery.

## 5. Step cards

All four cards have the same 6 core steps. Saving is in each card header, not a step. The debrief rerun is on each card under the steps. Learners use the files in `kit/lab-3/` and the run files from the case folder. Copilot learners use the `.txt` copies. No fast-start card in module 3 (module 1 only).

### Card: Claude
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Market Evidence Agent" from module 2. Lost or behind? Rebuild it from `kit-m3` first.
- Saves: **Save instructions** saves the instructions. Files save when you add them. Chats save as you go.
- Check date and vendor doc: 2026-11-27 (module 2 verifier reopened both docs; same screen names as module 2). Claude Help Center, "How can I create and manage projects?" (https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects, page metadata 2026-11-06, platform matrix cl-ui-09). "Create and edit files with Claude" (https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude, page metadata 2026-11-24, cl-ui-10). Stretch: "Schedule recurring tasks in Claude Cowork" (https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork, page metadata 2026-11-18, cl-sc-07) and "Organize your tasks with projects in Claude Cowork" (https://support.claude.com/en/articles/14116274-organize-your-tasks-in-claude-cowork, page metadata 2026-11-12). Both seen 2026-11-27.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-weekly-feedback` and `tag-list` to project knowledge with **+**. |
| 2 | In a new project chat, send the week 1 export with the prompt "Run the weekly feedback job". |
| 3 | In the same chat, send the week 2 export with the prompt "Run the weekly feedback job". |
| 4 | Write your decision for each flag report item on your record sheet. |
| 5 | Audit 10 random items from week 2 and the "no fit" group, with your record sheet checklist. |
| 6 | Add a "no fit" rule for what you found under "My rules" in the project instructions. |

**Debrief rerun:** In a new chat, send both exports with the prompt "Run the weekly feedback job".

Notes: No file in the answer? Check that **Code execution and file creation** (or **Create and edit files**) is on in **Settings**, then **Capabilities**. Team or Enterprise: ask your owner. Your project opens as one conversation with a Library? Tell the instructor.

**Start here with sample data:** Add: `job-card-weekly-feedback.md`, `tag-list.md`. Week 1: `m3-feedback-week-1.csv`. Week 2: `m3-feedback-week-2.csv`. Own work: replace `tag-list` with your problem codes and a definition for each. Use one or two weeks of feedback with personal data removed.

**Pass condition (second sample, run after class):** On your tuned agent, after the log save card. New chat. Send `m3-check-sample.md` with "Run the weekly feedback job". Pass if: (1) F-1305, F-1306 and F-1307 are "no fit", not P06. (2) The flag report names that "no fit" group: a contractor repair job, 3 accounts. (3) P01 counts 2 accounts, not 4. (4) F-1312 is "no fit". (5) The agent calls no change a trend.

**Done early:** Run the job on one week of your own feedback. Or fill section 4 of your record sheet.

**Stretch (only where verified):**
- Survey wave (all platforms, after step 6 only). Send `m3-stretch-survey-wave.csv` with the prompt "Add this survey wave as a source. Code the open-text answers. Set them next to the closed answers, by segment."
- Schedule (Claude only). Paid plan and Claude Desktop. Vendor doc checked 2026-11-27. Not yet tested by the course team.
  1. In Cowork, select **+** next to **Projects**, then **Import from project**.
  2. Pick "Market Evidence Agent", choose a folder on your computer, and select **Create**.
  3. Save next week's feedback export in that folder.
  4. In the project's **Scheduled tasks**, select **New task**, then **Set up manually**.
  5. Fill in a name, the prompt "Run the weekly feedback job on the newest export", **Weekly** and that folder.
  6. Keep the default approval mode. Select **Save**.
  No **New task** in the project? Select **Scheduled** in the left sidebar, then **New task**. Pick the project folder.
  With a folder, the task runs only while your computer is awake and Claude Desktop is open. Your company must allow Cowork and Computer access. Use no connectors. Your screens look different (new Claude experience)? Stop the stretch and tell the instructor.

### Card: ChatGPT
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Market Evidence Agent" from module 2. Plan: Go or Plus or higher. Lost or behind? Rebuild it from `kit-m3` first.
- Saves: As you go.
- Check date and vendor doc: 2026-11-27 (module 2 verifier reopened the doc; same screen names as module 2). OpenAI Help Center, "Projects in ChatGPT" (https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt, "Updated: 3 days ago" when seen 2026-11-27, platform matrix cg-ui-09). Schedule line: "Scheduled tasks in ChatGPT" (https://help-lb.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt, cg-06, seen 2026-11-27).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-weekly-feedback` and `tag-list` to the project's files. |
| 2 | In a new project chat, send the week 1 export with the prompt "Run the weekly feedback job". |
| 3 | In the same chat, send the week 2 export with the prompt "Run the weekly feedback job". |
| 4 | Write your decision for each flag report item on your record sheet. |
| 5 | Audit 10 random items from week 2 and the "no fit" group, with your record sheet checklist. |
| 6 | Add a "no fit" rule for what you found under "My rules" in **Project settings**. |

**Debrief rerun:** In a new chat, send both exports with the prompt "Run the weekly feedback job".

Notes: **Project settings** is in the **•••** menu of the project. No file in the answer? The brief asks for the full tables in one message. That is fine.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run after class):** Same as the Claude card.

**Done early:** Same as the Claude card.

**Stretch (only where verified):**
- Survey wave: same as the Claude card, after step 6 only.
- The schedule stretch step is not available on this platform in this course. A scheduled task in a project cannot read project files.

### Card: Copilot agent builder
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the agent "Market Evidence Agent" from module 2. To open it: **All agents**, then **...** next to it, then **Edit**. Lost or behind? Rebuild it from `kit-m3` first.
- Saves: **Update** after each change.
- Check date and vendor doc: 2026-11-27 (module 2 verifier reopened all docs; same screen names as module 2). Microsoft Learn, "Add knowledge sources" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge, "Last updated on 2026-11-16", mb-ui-12). "Share and manage agents" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents, "Last updated on 2026-11-16", mb-ui-13). Microsoft Support, "Add content to Microsoft 365 Copilot Chat prompts" (https://support.microsoft.com/en-US/Microsoft-365-Copilot/add-content-to-microsoft-365-copilot-chat-prompts, ms.date 2026-11-18, mb-ui-14, partly verified).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | On the **Configure** tab, add `job-card-weekly-feedback.txt` and `tag-list.txt` with **Upload**. |
| 2 | In the agent chat, send the week 1 export with the prompt "Run the weekly feedback job". |
| 3 | In the same chat, send the week 2 export with the prompt "Run the weekly feedback job". |
| 4 | Write your decision for each flag report item on your record sheet. |
| 5 | Audit 10 random items from week 2 and the "no fit" group, with your record sheet checklist. |
| 6 | Add a "no fit" rule for what you found under "My rules" in **Instructions**. |

**Debrief rerun:** In a new chat, send both exports with the prompt "Run the weekly feedback job".

Notes: Use the `.txt` copies. Copilot does not list `.md` as a knowledge file type. To send an export, upload it, or paste the text. If the `.csv` upload fails, open it and paste the text. Download any file the agent makes in the same session. Copilot keeps it for that session only.

**No Copilot license or billing?** Your agent cannot read Knowledge files. Do this instead:
1. Paste all of `copilot-fallback-instructions-m3.txt` into **Instructions**. It replaces the module 2 text.
2. Your own rules differ from the kit? Put yours under "My rules".
3. Do the steps above, but skip step 1. At step 2, send your `problem-backlog.txt` first, in its own message. Then send week 1.
4. Debrief rerun: in the new chat, send `problem-backlog.txt` first again. Then send both exports in a second message.
Upload each file, or paste the text.
If the instructions do not fit, keep only `brief-v3.txt` in **Instructions**. Paste the job card and the tag list in chat at the start of each run. The fallback agent does one job at a time.

**Start here with sample data:** Add: `job-card-weekly-feedback.txt`, `tag-list.txt`. Week 1: `m3-feedback-week-1.csv`. Week 2: `m3-feedback-week-2.csv`. Own work: as on the Claude card.

**Pass condition (second sample, run after class):** Same as the Claude card. Upload `m3-check-sample.md`, or paste the text.

**Done early:** Same as the Claude card.

**Stretch (only where verified):**
- Survey wave: same as the Claude card, after step 6 only. Upload the file, or paste the text.
- The schedule and second-agent stretch steps are not available on this platform in this course.

### Card: Gemini
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the skill "market-evidence-agent" from module 2. Find it in **Customize**, then **Skills**. Click it to edit. This is a Gemini skill. Gems are now skills. Lost or behind? Rebuild it from `kit-m3` first.
- Saves: **Save** after each change.
- Check date and vendor doc: 2026-11-27 (module 2 verifier reopened all docs; same screen names as module 2). Gemini Apps Help, skills page (https://support.google.com/gemini?p=pn_skills, page shows no date, gm-ui-10; module 1 decision D3 accepts it with a check date). Google blog, "Let skills in Gemini tackle your most repetitive tasks" (https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/, 2026-09-30) for **/**. The Help page names **Add files** for an existing skill.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-weekly-feedback` and `tag-list` to your skill with **Add files**. |
| 2 | In a new chat, send the week 1 export with "/market-evidence-agent Run the weekly feedback job". |
| 3 | In the same chat, send the week 2 export with "/market-evidence-agent Run the weekly feedback job". |
| 4 | Write your decision for each flag report item on your record sheet. |
| 5 | Audit 10 random items from week 2 and the "no fit" group, with your record sheet checklist. |
| 6 | Add a "no fit" rule for what you found under "My rules" in the skill **Instructions**. |

**Debrief rerun:** In a new chat, send both exports with "/market-evidence-agent Run the weekly feedback job".

Notes: Type **/** (or **@**) in the chat and pick your skill from the list. If adding files to the skill fails, upload the whole skill again with all its files. If a chat upload fails, paste the text. Do not turn on Canvas or Deep Research.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run after class):** Same as the Claude card. Use the prompt "/market-evidence-agent Run the weekly feedback job".

**Done early:** Same as the Claude card.

**Stretch (only where verified):**
- Survey wave: same as the Claude card, after step 6 only.
- The schedule and second-agent stretch steps are not available on this platform in this course.

## 6. Debrief

- Questions: Which problems move up or down in your backlog, and which need discovery? Which check or audit found the error? What was in your "no fit" group? What makes an agent say "no fit"?
- Rerun (3 minutes): new chat, both exports, tuned brief. While it runs, learners write which problems move in section 4 of the record sheet.
- Error reveal (record ids): F-1215 (A-17 Bellweather Diners), F-1216 (A-17), F-1217 (A-22 Meadowsweet Cafes), F-1218 (A-31 Sorrel Street Eateries), F-1219 (A-08 Kestle Market). All Food service. 5 items from 4 accounts. Each asks for inspector or auditor read-only, remote access to records. Each uses the words "inspector", "inspection", "audit" or "report". On brief v3, the agent tags them P02 Compliance report effort. P02 shows 7 accounts (+4), the largest change of the week, and the summary may call it the top mover. The "no fit" group holds only F-1232 (A-10, Spanish app) or nothing. The reason check passes because each quote holds "inspection report" or "audit".
- Fix the learner adds (`case/planted-errors.md`, lab 3): "Tag an item only if it matches the tag definition, not only its words. If the item asks for something the definition does not cover, mark it no fit."
- What makes an agent say "no fit" (2 minutes, with the reveal): a rule on meaning, not words. A clue for the manager: an empty "no fit" group in a week with new content.
- Debrief check (instructor only, after the rerun; `case/expected-results.md` lab 3): The new problem is in the "no fit" group with 4 accounts (A-08, A-17, A-22, A-31), and the flag report names it. P02 stays at 3 accounts (change 0). P01 shows 7 accounts, not 11 (A-05 sent 5 items). F-1221 (A-30, a name and a phone number) is flagged. Week 2 after the fix: P01 6 to 7 (+1, 11 items). P02 3 to 3 (0). P03 4 to 2 (-2). P04 2 to 3 (+1). P05 1 to 2 (+1). P06 2 to 1 (-1). P07 1 to 0 (-1). P08 2 to 1 (-1). P09 2 to 3 (+1). No fit 1 to 5 (+4; 6 items: F-1215 to F-1219 and F-1232). The agent calls no one-week change a trend.
- Flag report after the fix: (1) "No fit" group F-1215 to F-1219, 4 accounts: inspectors want read-only remote access. Case PM decision: send to discovery, add P10 to the backlog and the tag list. (2) "No fit" item F-1232 (A-10, Spanish app). (3) Personal data: F-1221. Remove it before the backlog keeps it.
- Which problems move (case PM, `m4-evidence-pack.md` Part 4): the PM order does not change: P01, P02, P08, P03, P06, P05, P04, then P09 (new row), then P07. P10 is not ranked and goes to discovery. Top by segment: Distribution P01 and P02, Food service P03, Pharmacy and lab P08.
- Check sample (1 minute, instructor shows the tuned project result; learners run it after class, about 5 minutes; `case/expected-results.md` lab 3 second sample): P01 2 accounts (A-01, A-03), 4 items. P02, P04, P05, P08 1 account each. No fit 4 accounts: F-1305, F-1306, F-1307 (A-04, A-09, A-15: send alarms to the refrigeration contractor's dispatch) and F-1312 (A-26, invoice email). Pass (the same 5 items as the card): (1) F-1305 to F-1307 are "no fit", not P06. (2) The flag report names the contractor dispatch request across 3 accounts. (3) P01 counts 2 accounts, not 4. Items 1 to 3 are the `expected-results.md` pass condition. (4) F-1312 is "no fit" (from the case table). (5) No change is called a trend (spec `no_threshold`).
- What you do Monday: Export last week's feedback. Run the job. Read only the flag report.
- Log save card:

| Platform | 1. Download | 2. Replace in the agent |
| --- | --- | --- |
| Claude | Download the backlog file from your debrief rerun | In project knowledge, delete the old `problem-backlog`. Add the new file with **+** |
| ChatGPT | Download the backlog file from your debrief rerun | Open the old `problem-backlog` in the project sources list. Delete it. Add the new file |
| Copilot | Download the backlog file from your debrief rerun, in the same session | On **Configure**, choose the **X** next to the old file, then **Remove**. **Upload** the new file. Select **Update** |
| Copilot, no license | Download or copy the backlog from your debrief rerun | Keep it on your computer. Paste it in chat at the next run |
| Gemini | Download the backlog file from your debrief rerun | In your skill, **More**, then **Replace file**. Select **Save**. If that fails, upload the whole skill again with the new file |

Rename the new file `problem-backlog` before you add it. Use the debrief rerun, not the lab run. If you have no file, use `kit-m4/problem-backlog.md`.

## 7. LD spec

| Field | Value |
| --- | --- |
| Objective | Extend the Market Evidence Agent with a weekly feedback job counted by unique account, run two weeks, decide each flag, audit 10 random items and the "no fit" group, add a "no fit" rule, and decide which problems move and which need discovery (m3-o1 to m3-o3) |
| Timing | Lab 28 minutes. Debrief 8 (rerun 3, reveal 2, check sample shown 1, Monday 1, log save 1). Lab brief before it: 3 minutes (2 short slides; full steps on the step cards in the workbook). Same in full day and half days. Check sample after class: about 5 minutes |
| Setup (Zoom) | Breakout rooms by platform (Claude, ChatGPT, Copilot, Gemini), 3 to 5 learners each. Learners keep their own screen. Share only when stuck. Instructor visits rooms in turn, Copilot first |
| Setup (in person) | Tables by platform, 3 to 5 learners. One laptop per learner. Instructor walks the tables, Copilot first |
| Steps per platform | See section 5 (4 cards with the same 6 core steps and the same debrief rerun). No fast-start card. Stretch: survey wave on all 4 cards (after step 6). Schedule on the Claude card only (not yet tested by the course team) |
| Materials | `kit/lab-3/` (job card, tag list, Copilot fallback text, record sheet, README). Case files `m3-feedback-week-1.csv`, `m3-feedback-week-2.csv`, `m3-check-sample.md`, `m3-stretch-survey-wave.csv` (stretch). `modules/m2/kit/kit-m3/` to rebuild before the lab. `kit/kit-m4/` for catch-up after. Instructor only: `case/planted-errors.md`, `case/expected-results.md`, saved demo output, saved check sample result from the tuned project |
| Success criteria | The week 2 what changed summary is complete and counted by unique account. Each flag has the learner's decision. 10 items and the "no fit" group audited. A "no fit" rule added to the brief. After class: the check sample passes the 5-item pass condition |
| Debrief questions | Which problems move up or down in your backlog, and which need discovery? Which check or audit found the error? What was in your "no fit" group? What makes an agent say "no fit"? |
| Fallback path | Cannot use own work: case data. Agent lost or behind: rebuild from `kit-m3` (about 5 minutes). Platform blocked: pair with a learner on another platform. Copilot with no license: `copilot-fallback-instructions-m3.txt`, backlog and exports uploaded or pasted. `.csv` upload fails: paste the text. No file output: full tables in one message (brief rule 7). Agent does not make the error: debrief uses the saved demo output. Rerun not done: use `kit-m4/problem-backlog.md` for the log save. Behind at the end: load `kit-m4` before module 4 |
| Learner evidence | Flag report decisions for week 2. Audit findings for 10 items and the "no fit" group. The "no fit" rule added to the brief (v3 to v4). Which problems move and which need discovery. All on `lab-3-record-sheet.md` |

## 8. Learner kit

Character counts measured with `wc -m` on 2026-11-27. Copilot course budget (spec `copilot_no_license_fallback`): core brief 3,500 or fewer, job card 1,500 or fewer, knowledge file 2,800 or fewer, total 7,800 or fewer. Vendor limit: Instructions 8,000 characters (mb-01). Every `.txt` copy matches its `.md` file (`cmp`).

| File | Loads into | Characters | `.txt` copy |
| --- | --- | --- | --- |
| `lab-3/job-card-weekly-feedback.md` | Knowledge | 1,496 (budget 1,500) | yes |
| `lab-3/tag-list.md` (copy of `case/m3-tag-list.md`) | Knowledge | 1,828 (budget 2,800) | yes |
| `lab-3/copilot-fallback-instructions-m3.txt` | Copilot Instructions, no license | 6,856 (budget 7,800; limit 8,000) | is a `.txt` |
| `lab-3/lab-3-record-sheet.md` | Not loaded. Learner keeps it | 1,393 (not loaded) | no |
| `lab-3/README.md` | Not loaded | not counted | no |
| `kit-m4/brief-v4.md` | Instructions | 3,253 (budget 3,500) | yes |
| `kit-m4/job-card-problem-backlog.md` (no change) | Knowledge | 1,194 | yes |
| `kit-m4/code-book.md` (no change) | Knowledge | 2,791 | yes |
| `kit-m4/problem-backlog.md` (after lab 3: feedback weeks 1 and 2, P09 and P10, case PM order and flag decisions; facts from `case/m4-evidence-pack.md` Part 4) | Knowledge | 15,194 (a log, not in the fallback instructions) | yes |
| `kit-m4/job-card-win-loss.md` (no change) | Knowledge | 1,483 | yes |
| `kit-m4/driver-code-book.md` (no change) | Knowledge | 2,284 | yes |
| `kit-m4/driver-log.md` (no change from kit-m3) | Knowledge | 5,047 (a log) | yes |
| `kit-m4/job-card-weekly-feedback.md` | Knowledge | 1,496 | yes |
| `kit-m4/tag-list.md` (version 2, P10 added) | Knowledge | 2,038 (budget 2,800) | yes |
| `kit-m4/lab-3-fix-rules.md` | Not loaded. Handout | 634 | yes |
| `kit-m4/copilot-fallback-instructions-m3-v4.txt` | Copilot Instructions, no license, to rerun job 3 | 7,194 (budget 7,800) | is a `.txt` |
| `kit-m4/README.md` | Not loaded | not counted | no |

Fallback sum check (module 3): brief v3 3,094 + job card 1,496 + tag list 1,828 = 6,418, plus 438 characters of header (426) and separators (12) = 6,856. A learner "no fit" rule of about 160 characters brings it to about 7,020, still under 7,800. kit-m4 fallback: brief v4 3,253 + 1,496 + tag list v2 2,038 + header 395 + separators 12 = 7,194.

Spec P2 check "core instructions stay under 8,000 characters": brief v4 is 3,253.

Knowledge files in the agent after module 3: 8 (3 job cards, code book, driver code book, tag list, problem backlog, driver log). Course budget 13. Spec `uploads_per_lab` module 3: 2 files to the agent, 3 in chat (2 exports, check file). The check file runs after class.

## 9. Instructor notes

- Timing flex:
  - Behind before the lab: cut the story slot (3.4) and the question on 3.3. Never cut the lab brief (3.10, 3.11) or the data safety box.
  - Behind in the lab: at minute 25, tell learners to write the rule even if the audit is not done. The debrief reveal works from the step 3 run.
  - Behind in the debrief: keep the reveal (3.14) and the log save card (3.17). Cut 3.13 to the rerun only, with no answers taken. Show 3.15 in 30 seconds.
  - Ahead: learners do "Done early": run the job on their own feedback, or fill section 4 of the record sheet. After step 6 only: the survey wave stretch.
- Common failures and recovery:

| Failure | Recovery |
| --- | --- |
| Agent lost or broken after module 2 | Rebuild from `kit-m3` (about 5 minutes), then do step 1 |
| Copilot: the agent ignores the knowledge files (no license or billing) | Use the no-license box on the Copilot card: `copilot-fallback-instructions-m3.txt` in Instructions, backlog and export uploaded or pasted |
| Copilot or Gemini: `.csv` upload fails in chat | Open the file and paste the text. Week 1 is 3,872 characters, week 2 is 5,001 |
| Copilot no license: a pasted message is too long | The card already splits it: backlog alone first (10,004 characters), then the export or exports (week 1 3,872; both weeks 8,873). Add "This is the problem backlog. Wait for the export." to the first message. Microsoft publishes no message limit (Support, "Limits for features in Microsoft Copilot Chat", ms.date 2026-10-31) |
| Gemini: adding files to the existing skill fails | Check the label: **Add files** on an existing skill. If it still fails, upload the whole skill again with all its files (gm-01) |
| Claude: no file in the answer | Turn on **Code execution and file creation** (**Create and edit files**). Team or Enterprise: the owner sets it in **Organization settings**. Or accept the full tables in one message (brief rule 7) |
| The answer stops halfway (long output) | Send "Continue". Or send "Give the what changed table and the flag report first, then the tagged items" |
| The agent runs the problem backlog job or the win/loss job | Check the prompt says "Run the weekly feedback job". Check `job-card-weekly-feedback` is in knowledge |
| Week 2 shows no last week | The week 2 run must be in the same chat as week 1 (step 3). Or send both exports together. The brief runs them in date order |
| The agent counts items, not accounts (P01 shows 11) | Point to the quality check "Counts are by unique account" in the job card. It is a finding for the audit and the debrief, not a planted error |
| The agent drops P09 because the backlog has no P09 row | The tag list has P09. Ask: "Add a backlog row for each tag with feedback." Accept the row |
| The agent counts F-1104 or F-1207 as a Customer Success account | The item is about the customer account (A-09). Count the customer, not the team that passed it on (slide 3.4) |
| The agent copies the name or phone number from F-1221 into the backlog | Audit finding. Point to the hand-off rule on personal data. Delete it from the saved backlog |
| The agent calls a change a trend, or names a "top mover" | Point to the job card line "Never call one week a trend." Rerun |
| The agent does not make the planted error (F-1215 to F-1219 already "no fit") | Good. Ask the learner which line in the tag list or job card kept them out. In the debrief, show the saved demo output |
| The agent tags F-1215 to F-1219 as P08 Calibration records or P05 | Same forced fit, different tag. The fix is the same rule |
| The agent writes "pattern" or "validated" | Audit finding. Point to brief rule 3. Rerun |
| A learner's own feedback export holds personal or health data | Stop. Remove names, contact details and health data, or use the case data. Data safety box |
| Claude schedule stretch: no **New task** in the project | Use **Scheduled** in the left sidebar, then **New task**, and pick the project folder (card note) |
| Claude schedule stretch: no **Scheduled tasks** or no folder option | Cowork may be off for the organization, or Computer access is off. Or the account has the new Claude experience. Stop the stretch. Record it for the course team |

- Case notes (module builder, checked 2026-11-27 against the case files):
  1. OI-19 (owner module builder). F-1108 (week 1, A-07 Quarry Lane Pharmacies) and F-1214 (week 2, A-29 Elmstead Pharmacy) are both P02 feedback items in lab 3. They support the lab 5 report pack answer but are not lab 5 inputs. Both are in the kit-m4 backlog, in P02 "other sources" (A-29 in week 2; A-07 in the week 1 count). The I-201 quote 2 note is a lab 1 item, covered in module 1 section 9.
  2. F-1209 (A-27 Calder Point Logistics) is a prospect, not a customer. The case counts it for P01 (week 2, 7 accounts). Accept it, and say why: it is feedback from an account in the export.
  3. F-1207 (A-09) asks for "quiet hours". It is P01 in the case. An agent may also see it as P06. P06 covers who responds at night, so P01 is right.
  4. F-1221 (A-30 Pikeworth Grill House) counts for P03 (hub placement) and is flagged for personal data. The name and number are fictional (555-01xx range, `case/README.md`).
  5. The check sample items F-1305 to F-1307 name no night or weekend (`case/planted-errors.md`), so they are not P06. An agent that tags them P06 shows the same forced fit. Learners see this only after class.
  6. The case tag list says "What moved". The spec, the slides and the cards say "what changed". Same table (decision D10).
  7. The kit-m4 backlog follows `m4-evidence-pack.md` Part 4 facts, so module 4 starts from the same backlog. Its F-1124 and F-1232 flag decisions are left to the learner (decision D9).
  8. For the module 4 builder (verifier F12): `kit-m4/problem-backlog.txt` is 15,194 characters. A module 4 no-license learner who pastes it is near the 15,400 paste target. Split it, or rely on the evidence pack Part 4.
- Kept off the slides on purpose: any feedback tagging figure (W4 and W5 hour figures are vendor arithmetic, not data; W4's report figure is not opened). "Spread across many tools" and "tags drift" (1 source each; decision D7). Any schedule setup screen (CAW-AI slide 9, registry). "People stop reading" and "tools show only top movers" (no source; verifier F3, F6). The case account A-05 before the debrief (B8).
- Registry guard: CAW-AI buyer voice watch reads public reviews of competitors on a monthly schedule. This job reads the company's own feedback into its own backlog, started by hand on the core path. No scheduled-task setup slide. New slides only.
