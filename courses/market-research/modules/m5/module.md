# Module 5: The agent answers stakeholders, and you stay accountable

Course: Advanced AI for Market Research (`market-research`). Stage 3 draft by the module builder, 2026-11-27. Revised once on 2026-11-27 after the consistency and verifier reports (`revision-notes.md`). Last module. It also holds the course close (section 10). Case year is 2027 (`case/year-shift-map.md`). Real source and vendor dates stay 2026. Built from `spec.yaml` (Gate 2, approved 2026-11-26; module 5 entry, `course_close`, `copilot_no_license_fallback`, `stretch_scope`, `gate_2_proof_patterns` P3), `outline/development-brief.md`, `outline/gate-2-decisions.md`, the case files, `research/stretch-verification-2026-11.md`, the approved module 1 and the module 2 and 3 drafts in review (decisions and revision notes).

Module 5 starts from kit-m5, the state after module 4: `modules/m4/kit/kit-m5/`. This draft defined that start state from the spec and the case before module 4 was built (`kit/kit-m5-expected.md`). The module 4 builder delivered kit-m5 to match it on 2026-11-27 (module 4 draft, revised once; decision D1). Hand-over edits are recorded in `modules/m4/revision-notes.md`.

## 1. Summary

| Item | Value |
| --- | --- |
| Workflow row and bottleneck | mr-wf-09 (folds mr-wf-07: ranking and validation proposals by segment). Answer stakeholder questions from past research and the problem backlog with sourced, dated answers. Bottleneck: people cannot find past insights, product managers do not remember study names, and teams commission new studies on questions already answered (W13, age flag kept by Dan; W20) |
| Framework category and focus area | Market. Market Problems |
| Capability Standards (as in spec) | Confirmed by Dan, Pragmatic to confirm. Skills 1.1 Market Problem Identification, 8.4 Data Narrative and Stakeholder Communication. Competencies 1.1C, 1.1D, 8.4A, 8.4C |
| Rung | 3 plus, an agent that faces other people. The chain ends in an answer to a person. The PM sends, changes or holds each answer |
| Minutes (full day / half day) | 65 / 60. Course close after it: 15 / 10 (section 10) |
| Instructor-led / hands-on (minutes, %) | Full day 26 / 39 = 40% / 60% (8 + 9 + 9 = 26; 30 + 9 = 39). Half day 24 / 36 = 40% / 60% (7 + 8 + 9 = 24; 28 + 8 = 36). Inside the 40/60 rule (plus or minus 5 points). Course close: 5 / 10 (half day 4 / 6), as the spec sets it |
| Planted error and warning level | Old research for another segment presented as current. Q2 (Head of Hardware) asks about pharmacy and lab. The agent answers "Buyers want a one-click inspection binder" from R-2025-07 (2025-09-12, Food service only, date and segment in a small-print header). The citation check passes. Warning: none (last lab). No audit hint |
| Agent after this module (files) | Instructions: brief v6 (rules 1 to 6). Knowledge: 12 files: 5 job cards (problem backlog, win/loss, weekly feedback, alternatives map, stakeholder answers), 5 case knowledge files (code book, driver code book, tag list, alternatives map, past reports), 2 logs (problem backlog, driver log). Take-home: `kit/kit-final/` |

### Start state (the agent after lab 4)

This is the state module 5 assumes. Module 4 delivers it in `modules/m4/kit/kit-m5/` (all contract rows met; see `kit/kit-m5-expected.md`).

| Part | State after lab 4 | Status |
| --- | --- | --- |
| Instructions | Brief v5: brief v4 (kit-m4) plus "My rules" 4, the lab 4 fix text in `case/planted-errors.md` ("The alternative chosen comes from the buyer's interview..."). 3,491 characters | Module 4: rule 4 lives in "My rules" (module 4 D1) |
| Knowledge, unchanged from kit-m4 | `job-card-problem-backlog`, `code-book`, `problem-backlog` (kit-m4 file, same facts as Part 4 of `m4-evidence-pack.md`, 15,194), `job-card-win-loss`, `driver-code-book`, `job-card-weekly-feedback`, `tag-list` (v2, P10) | No change |
| Knowledge, changed in lab 4 | `driver-log`: Q2 rows plus the 10 Q3 rows of the evidence pack, with D-3102 and D-3108 alternatives read from the interviews (7,616). `alternatives-map`: end of Q3 2027, the lab 4 result after the fix (3,286) | From the case. Delivered in `modules/m4/kit/kit-m5/` (same as the drafts). Module 4 log save card saves both (module 4 D4) |
| Knowledge, new in lab 4 | `job-card-alternatives-map` (1,497) | Set by module 4 |
| Count | 10 knowledge files. Lab 5 adds 2. 12 at the end (spec `knowledge_file_budget`) | |

### Slide minutes check

| Arc step | Slides | Minutes (full day) | Minutes (half day) | Mode |
| --- | --- | --- | --- | --- |
| Why this matters, workflow and bottleneck | 5.1 to 5.4 | 1 + 2 + 2 + 3 = 8 | 1 + 2 + 2 + 2 = 7 | Instructor-led |
| Live demo | 5.5, 5.6 | 6 + 3 = 9 | 5 + 3 = 8 | Instructor-led |
| Build pattern and lab brief | 5.7 to 5.11 | 2 + 2 + 1 + 2 + 2 = 9 | 2 + 2 + 1 + 2 + 2 = 9 | Instructor-led |
| Lab 5 | 5.12 | 30 | 28 | Hands-on |
| Debrief | 5.13 to 5.17 | 2 + 2 + 3 + 1 + 1 = 9 | 2 + 1 + 3 + 1 + 1 = 8 | Hands-on |
| Total | 17 slides | 65 (26 + 39) | 60 (24 + 36) | |

Debrief minutes follow the spec arc: reveal 2, brief fix 2 (half day 1), Run Q4 and compare 3, segment rule and the PM decides 1, what you do Monday 1. The spec module 5 arc has no log save card (B9). Course close slides C.1 to C.4 are in section 10.

### Builder decisions inside the spec

| # | Decision | Why |
| --- | --- | --- |
| B1 | The demo asks Q3 (Support lead), the optional lab question | Q2 holds the planted error and Q4 is the check question, so neither can be the demo. Q1 and Q5 are core lab questions. Q3 also shows the "sources disagree" flag, which the lab tests only for learners who ask Q3 (spec `case_question_plan`). See D11 |
| B2 | Step 3 sends the whole questions file with the prompt "Run the stakeholder answer job for Q1, Q2 and Q5". The debrief Q4 run uses "...for Q4" | The case file holds Q1 to Q5. The plain prompt would answer Q4 before the fix and add Q3. One file, one prompt stays one action. See D4 |
| B3 | Lab brief is 2 short slides. 5.10: goal, 6 key actions, pointer to the workbook card. 5.11: done when and the data safety box. No warning box on 5.11 | Dan's lab brief slide rule (2026-11-27). Fade level none: no warning (spec `planted_error_fade` module 5) |
| B4 | Step 5 audits one answer picked at random. Slide 5.4 uses Q1 and Q5 as examples, not Q2. Slide 5.8 has no roadmap line | Revise once (consistency blocker 1): a risk rule ("the answer you would least like to get wrong") plus the Q2 stake on 5.4 and 5.8 steered learners to the planted answer. Last lab: no hint (house rule 13). A random pick is neutral. About 1 in 3 learners audits Q2; the reveal covers the rest |
| B5 | Record sheet audit checklist is neutral: the source is in the files, the claim's words or numbers are in the source, the citation's date and segment are the source's own | No audit hint (module 1 D11, fade level none). All three items pass for the planted error; the learner must still judge the answer against the question |
| B6 | Step 2 writes "rule 5" under "My rules": the age limit and what the agent may say. The record sheet gives the case PM's age limit (18 months, `company.md` rule 1) and 3 example "may say" rules (draft only, name no person, no commitment for the team) | Spec card step 2 and objective m5-o2. The examples are boundaries for an agent that faces people (decision 33). None names a source, a date rule beyond the age limit, or a segment rule, so none gives the error away. See D14 |
| B7 | The card pass condition item 4 is general: "The flag report lists old sources, thin evidence (a fact label) and sources that disagree." The debrief slide names the records (R-2025-07, I-105) | The card is in the workbook before the lab. A record id on the card would point at the old report. Same idea as module 1 D7 (pass condition on the card, run in the debrief) |
| B8 | Proposals by segment read the backlog that is already in the agent. Lab 5 adds no log | Spec `uploads_per_lab` module 5: 2 to the agent, 1 in chat. Logs already in the agent |
| B9 | No log save card in module 5. The course close (C.4) saves kit-final and the learner's logs and brief | The spec module 5 debrief arc has no log save step, and lab 5 writes no log. Instructions save as on every card header. See D9 |
| B10 | Spec step order is kept: decide send, change or hold (step 4), then open every citation in one answer (step 5). The record sheet adds "My decision after the audit". 5.13 asks if the audit changed a decision | Spec `card_steps` is the contract. Objective m5-o3 says to decide after the citations; the second column covers that. See D10 |
| B11 | Copilot no-license: Instructions hold brief v5 and the job card (5,293). The past reports go in chat, with the driver log and the map | Brief v5, the job card and the past reports are 7,662 before any lab 5 rule. Rule 5 and rule 6 add about 590, over the 8,000 limit (mb-01). Spec backup path allows knowledge files in chat. See D3 |
| B12 | Course close is section 10 of this file, slides C.1 to C.4. The recap slide (C.1) shows the five audits and the five rules. It does not show the manager loop circle again | Slide 1.7 is the manager loop. House rule 9: no repeated slide. C.2 shows the five PM calls, not slide 1.14 again |
| B13 | Slide 5.4 carries the spec theme ("be great at product management before you are great at AI") as one line. The slide is about the decision behind the question | Slide O.9 already has the theme as its headline. A new slide with a new point, no repeat |
| B14 | Slide 5.2 shows only "Past research is hard to find and reuse" (W13, W20). "Product managers do not remember study names" and "teams commission new studies" (W20 only) are in the talk track, attributed | Research rule 2. Same pattern as module 3 D7 |
| B15 | kit-final is released on the Learning Hub after slide 5.13, not with the workbook | Revise once (consistency finding 2): brief v6 rule 6, the lab 5 rules handout and the README decisions table hold the lab 5 fix. Released before the lab, they are a full hint. See D6 |
| B16 | Share stretch steps only on the Claude and ChatGPT cards, headed "Stretch (vendor doc checked, not yet tested)". Copilot and Gemini cards: share plan only | Revise once (consistency finding 6): `stretch_scope` keeps the Copilot and Gemini cards on the core path. Same "not yet tested by the course team" wording as module 3 D1. See D5 |

### Decisions for Dan

Open decisions for the Gate 3 doc, most important first. One line each, with a recommendation. Revised once on 2026-11-27 (`revision-notes.md` maps the old numbers). The audit pick is no longer a decision: step 5 uses a random pick (B4).

| # | Decision | Recommended |
| --- | --- | --- |
| D1 | Start state before module 4 exists: kit-m5 as listed in `kit/kit-m5-expected.md`. Module 4 must match it. B: wait for module 4 | A |
| D2 | Lab 5 Q1 and Q4 need the Q3 deals in the agent. A: module 4's log save card also saves the driver log with Q3 rows. B: the map carries the Q3 evidence; the driver log stays Q2 | A. Needs change 1 |
| D3 | Copilot no-license: past reports in chat, not in Instructions (the spec says Instructions; with them, rules 5 and 6 pass 8,000) | A. Needs change 2 |
| D4 | Step 3 prompt names the questions ("for Q1, Q2 and Q5"); Q4 uses "for Q4" | A. Needs change 3 |
| D5 | Share stretch: steps on Claude (Team, Enterprise) and ChatGPT, after class, "not yet tested by the course team". Copilot and Gemini: share plan only (`stretch_scope`). B: plan only on all 4. C: add Copilot and Gemini steps (needs a `stretch_scope` change) | A. Needs change 4 |
| D6 | kit-final is released on the Learning Hub only after slide 5.13, because it holds the lab 5 fix | A |
| D7 | kit-m5 driver log: D-3108 quote is the WL-3108 quote "Your trial sent alerts every lunch rush, and my managers gave up on it." (matches Q4 expected evidence). Module 4 must match | A |
| D8 | Resolved 2026-11-27: kit-final holds the module 4 `job-card-alternatives-map` (1,497), copied from `modules/m4/kit/kit-m5/` | Closed. No decision needed |
| D9 | No log save card in module 5; the course close saves the brief, the logs and kit-final | A. Needs change 5 |
| D10 | Spec order kept: decide (step 4) before the audit (step 5), with a "decision after the audit" column | A. Or swap steps 4 and 5 in the spec |
| D11 | Demo asks Q3, the optional lab question | A |
| D12 | Card pass condition item 4 is general; record ids only on the debrief slide | A |
| D13 | Course close in this file (section 10). C.3 (kit-final) moved into the hands-on Monday plan segment | A |
| D14 | Example "may say" rules on the record sheet (draft only, name no person, no commitment) | A |
| D15 | Story slot on 5.4 (an executive who repeated an old finding as current) | Supply one real story, else skip path |
| D16 | Brief v6 is 4,008 characters, over the 3,500 core brief budget (limit 8,000) | Accept |
| D17 | Lab 5 does not need P10 in the learner's own backlog (module 3 D2 follow-up) | Keep module 3 D2 option A |

### Changes needing Dan's yes

None of these are made. Each waits for your yes.

| # | File (fingerprinted or approved) | Change | Why |
| --- | --- | --- | --- |
| 1 | `case/expected-results.md`, "State files for the catch-up kits", row kit-m5 | "Adds the map after lab 4" becomes "Adds the map after lab 4 and the Q3 driver log rows (Part 1 of `m4-evidence-pack.md`; D-3102 and D-3108 alternatives and the D-3108 quote read from the interviews)" | Only if D2 and D7 are A |
| 2 | `spec.yaml`, `copilot_no_license_fallback.per_module` module 5 | Instructions: "Core brief + stakeholder answer job card". Paste in chat: "Problem backlog (alone); then driver log, alternatives map and past reports; then the questions" | Only if D3 is A |
| 3 | `spec.yaml`, module 5 `card_steps` step 3 and `check_sample` | Prompt "Run the stakeholder answer job for Q1, Q2 and Q5". Q4: "...for Q4" | Only if D4 is A |
| 4 | `spec.yaml`, module 5 `stretch` | "Share the agent ... (not verified)" becomes "Share plan on all 4 cards. Share steps on Claude (Team, Enterprise) and ChatGPT from dated vendor docs (2026-11-27), after class, not yet tested by the course team. Copilot and Gemini: plan only (stretch_scope)". Option C also edits `stretch_scope.copilot_and_gemini_cards` | Only if D5 is A (or C) |
| 5 | `spec.yaml`, `module_arc` (debrief step) | Add: "Module 5 has no log save card. The course close saves the brief, the logs and kit-final" | Only if D9 is A |
| 6 | `research/platform-matrix.yaml`, rows cl-pj-02, cg-02, mb-05, gm-04, gm-ui-10 | As in the verifier report, last section: checked_on 2026-11-27; status verified (doc) for the Claude, ChatGPT and Copilot share steps, partly verified for Gemini; screen names (**Share project**, **Can view**, **Share**, **Remove access**; **Share**, chat or edit access, **Only those invited**; **Share**, **Add a name, group, or email**, **Can chat**, **Add**, **Send notification**, **Remove**; Gemini labels on the undated Help page only); limits (what a shared member sees; Claude project memory not documented for members) | The cards use these names. Verifier proposal |
| 7 | `research/workflows.yaml`, row mr-wf-09 evidence W13, W20 | checked_on 2026-11-27 (quotes found again). W20 note: "The source says product managers, not stakeholders, do not remember study names" | Verifier proposal |

### Notes for the module 4 builder

Done 2026-11-27. Module 4 delivered `modules/m4/kit/kit-m5/` and answered the 6 choices (`modules/m4/module.md`, contract check). Kept as a record.

1. Build `modules/m4/kit/kit-m5/` to match `modules/m5/kit/kit-m5-expected.md`. Copy the 3 drafts in `modules/m5/kit/kit-m5-draft/` if your lab keeps them.
2. Tell module 5 the 6 choices in `kit-m5-expected.md` section 3: where the lab 4 rule lives, its text, the driver log save, the final map job card, the driver code book, and the character counts.
3. Keep brief v5 at 3,500 characters or fewer. The draft is 3,491. A longer lab 4 rule breaks the module 4 fallback budget.
4. Keep the backlog at 15,194 characters (one Copilot paste, under the 15,400 target). Keep the driver log, the map and the past reports together under 15,400 (draft: 13,675).
5. Lab 5 needs these Q3 deals in the agent: D-3105, D-3107 (Q1) and D-3108 (Q4). D-3108 must show do nothing, not Rimecore.
6. The kit-m5 draft driver log gives D-3108 the WL-3108 quote "Your trial sent alerts every lunch rush, and my managers gave up on it." (D3 alert accuracy), not the Part 1 quote. Q4 expected evidence names it (D7). Keep it, or tell module 5.
7. Slide registry inside this course: module 5 uses no second-agent step and no schedule slide. The platform gap slide for the second agent stays in module 4 only (spec `stretch_scope.slides`).

## 2. Slides and talk track

### Slide 5.1: Module 5. The agent answers stakeholders
- Layout: Chapter Break
- Minutes: 1 (half day 1)
- On-slide text: MODULE 5. The agent answers stakeholders. Promise: "Sourced, dated answers. You send them." Bullets: Add a stakeholder answer job. Write what it may say. Send, change or hold each answer.
- Visual intent: Teal side band, "MODULE 5" tag. Small rung icon: rung 3 plus lit, with a person at the end of the chain.
- Sources: none

Notes:
```
POINT: In this module your agent gets its fifth and last job: it answers other people's questions from your research.
Talk Track:
Your agent has four jobs now.
The problem backlog. Win/loss. The weekly feedback run. The alternatives map.
Each job writes to a log or a file in your agent. Together they are your research store.
Today the agent gets its last job. It answers questions from other people.
A sales leader. A hardware lead. An internal product manager.
That changes one thing. The answer leaves your desk.
So the agent drafts, and you decide what gets sent.
TRANSITION: First, the workflow and what slows it down.
```

### Slide 5.2: "What do we know about X?"
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: Headline: "What do we know about X?" Line: "Past research is hard to find and reuse." Workflow strip: "A stakeholder question, then a sourced, dated draft, a 'what we do not know' line and a flag report."
- Visual intent: Headline in navy. A chat bubble with the question on the left. The strip runs to three outputs on the right. No numbers.
- Sources: W13 (claim, Nielsen Norman Group, 2024-07-26, age flag kept by Dan) and W20 (claim, UserTesting, 2026-07-08). Independent of each other. No figure from either (B14)

Notes:
```
POINT: Stakeholders ask what the team already knows every week, and past research is hard to find and reuse.
Talk Track:
Here is the workflow for this module.
Someone asks: "What do we know about pharmacy buyers?" In Slack, in email, in a planning meeting.
The answer is somewhere in past research. Finding it is the problem.
Two sources say this.
Nielsen Norman Group, a research firm, says research repositories fail. Adding to them is too much work, and people cannot find past insights. That article is from 2024, so we use it as a claim only.
UserTesting, a research platform vendor, wrote in 2026 that product managers do not remember study names. Teams commission new studies on questions already answered. That is a vendor's experience, not a study.
So two things go wrong. The team pays for the same study twice.
The risk this job removes: someone answers from memory, and the answer goes further than the evidence.
[ASK: "When did someone in your team last answer a 'what do we know' question from memory?" TAKE 1 ANSWER]
At Larkspan, our case company, one current market question is: "What can we tell stakeholders now, and what needs new research?"
That is today's job.
TRANSITION: This job is the top of the ladder.
```

### Slide 5.3: Rung 3 plus: an agent that faces other people
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: Your logs feed one answer. The agent drafts. You send, change or hold. The stakeholder gets only what you send.
- Visual intent: Four file tiles on the left (problem backlog, driver log, alternatives map, past reports) feeding one "answer job" tile. Then a "draft" tile, then a PM tile with three buttons (send, change, hold), then a stakeholder icon. Ladder at the side with rung 3 plus lit.
- Sources: none (spec `autonomy_ladder` rung 3 plus)

Notes:
```
POINT: At rung 3 plus the chain of jobs ends in an answer to a person, so the PM reviews every answer before it goes.
Talk Track:
In module 4 one job handed its output to the next job.
Today the chain ends at a person.
The answer job reads every log you built.
The problem backlog from modules 1 and 3. The driver log from module 2. The alternatives map from module 4. And past study reports.
A wrong number in a log stays in a file until your next audit.
A wrong answer goes into a sales kickoff, a roadmap or a board deck. Someone acts on it.
So this agent never sends. It drafts.
You make one of three calls on each answer: send it, change it, or hold it.
Internal product managers ask questions too. In the lab, the Fleet Data Platform PM asks one. Internal teams are stakeholders.
TRANSITION: Before you send anything, know what the question is for.
```

### Slide 5.4: Know the decision behind the question
- Layout: Blank
- Minutes: 3 (half day 2, no story slot)
- On-slide text: Before you send: Who asks? What will they decide with it? What would change that decision? Bottom line: "Be great at product management before you are great at AI."
- Visual intent: Three questions in large type, stacked. The bottom line small, in teal, as a callback to the course open.
- Sources: none (spec `course.themes`; case `m5-stakeholder-questions.md`)

Notes:
```
POINT: The agent answers the question as written, and the PM knows the decision behind it and how much is at stake.
Talk Track:
You heard this theme this morning: be great at product management before you are great at AI.
Here is what it means for answers.
The agent answers the question as it is written.
You know the decision behind the question.
Look at two of today's case questions.
The VP Sales asks if pharmacy and lab deals are lost on price. It goes into the sales kickoff.
The Fleet Data Platform PM asks about hub signal loss. She must place a request in her backlog.
Same agent. Same evidence. Different stakes.
So ask three things before you send. Who asks? What will they decide? What would change that decision?
[OPTIONAL STORY SLOT, 1 MINUTE. FULL DAY ONLY. Topic: an executive who repeated an old finding as current in a board deck, and what happened when someone checked the date. Use only a story you heard from executives or from Pragmatic's work with companies. Tell it as their story, never as your own. If you have no such story, skip this slot and ask: "Which question in your queue has the biggest decision behind it?" Take 1 or 2 answers]
TRANSITION: Let me add the answer job in front of you.
```

### Slide 5.5: Live demo. Add the stakeholder answer job
- Layout: 1_prompt
- Minutes: 6 (half day 5)
- On-slide text: LIVE DEMO. "Add the answer job. Ask one stakeholder question." Running example: Larkspan Systems, Q3 from the Support lead. 6 MIN.
- Visual intent: Orange "LIVE DEMO" tag. Platform logo for the demo platform (Claude). Small list: 2 new files, 1 rule, 1 question.
- Sources: cl-pj-01, cl-ui-09 (platform matrix, verified). Demo script in section 3

Notes:
```
POINT: Adding the answer job takes two files and one rule, and one prompt runs it on a question.
Talk Track:
[SWITCH TO THE DEMO PLATFORM. FOLLOW THE DEMO SCRIPT IN SECTION 3, STEPS 1 TO 4]
Here is the agent after module 4. Brief v5 in the instructions. Ten files in knowledge.
I add two files: the stakeholder answer job card and the past reports. Two past studies from the Larkspan research store.
Now one rule in the brief. My age limit.
Any number in a hand-off rule is the PM's choice. The case PM chose 18 months.
I write it under "My rules" as rule 5, with what the agent may say: every answer is a draft, no names, no commitments.
[SAVE THE INSTRUCTIONS. START A NEW CHAT]
I send the questions file. One prompt: "Run the stakeholder answer job for Q3".
Q3 is from the Support lead. In the lab it is optional, so you have seen it here.
[SEND BY MINUTE 2 OF THIS SLIDE. WHILE IT RUNS:]
The Support lead asks: should Support plan for a night monitoring service for distribution customers?
The agent looks in the backlog, the driver log, the map and the past reports.
[IF THE RUN IS NOT DONE AT MINUTE 5, OPEN THE REHEARSAL OUTPUT AND MOVE ON. LET THE LIVE RUN FINISH IN THE BACKGROUND]
TRANSITION: Here is how you read the draft.
```

### Slide 5.6: Read the draft: what it says, and what it hands you
- Layout: Blank
- Minutes: 3 (half day 3)
- On-slide text: 1. Each claim: source, date, segment, counts. 2. "What we do not know." 3. "Draft. The PM decides." 4. Proposals by segment. 5. Flag report: your decisions go here.
- Visual intent: A cropped, readable mock from the demo run: the Q3 answer with one citation (R-2027-03, 2027-05-20, Distribution) circled, the "what we do not know" line, and the flag report header. Numbers 1 to 5 in orange circles.
- Sources: none (case `expected-results.md` lab 5, Q3 row; `m5-past-reports.md`)

Notes:
```
POINT: You manage the answer job by checking each citation, the "what we do not know" line, the proposals and the flags.
Talk Track:
[DEMO SCRIPT STEPS 5 TO 9. STAY ON THE SCREEN, THEN SHOW THIS SLIDE AS THE SUMMARY]
One. Each claim has a source, a date, a segment and counts.
Here: P06, after-hours response. 4 interviews, 3 accounts, Distribution only, September to October 2027.
Two buyers want their own managers on night alarms. Two want a service. And two of the four work at the same account.
Then a past report, R-2027-03, from May 2027, Distribution. 5 of 9 want a service option. 4 of 9 want their own managers.
Two. "What we do not know." Here: no price for a monitoring service was ever tested.
Three. The label "Draft. The PM decides."
Four. Proposals by segment. The agent ranks the problems inside each segment, and proposes what goes to validation.
In Distribution it proposes P01 and P02 for validation, and P06 for research first.
Five. The flag report. Here: sources disagree, and the question needs new research. The decision column is blank.
The case PM's call on Q3: change it, then send it as "split; test a priced offer before Support plans staff."
[DO NOT COMMENT ON ANY OTHER QUESTION, ANY OTHER REPORT, OR THE FOOD SERVICE OR PHARMACY AND LAB PROPOSALS. IF A LEARNER ASKS:] Good question. Hold it for your lab.
[SAVE THE DEMO OUTPUT FILE]
TRANSITION: So what may this agent say, and what must it hand to you?
```

### Slide 5.7: What your agent may tell other people
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: It may say: what we know, with sources, dates, segments and counts. What we do not know. It hands you: sources over your age limit, sources that disagree, questions that need new research, thin evidence. It never: sends, commits the team, writes "validated".
- Visual intent: Three columns: "May say" (teal), "Hands to you" (orange flag icon), "Never" (gray). Short lines.
- Sources: none (spec module 5 `quality_checks`, `handoff_rules`; AI Agents course boundaries referred to, new slide, decision 33)

Notes:
```
POINT: Hand-off rules set what an agent that faces other people may say, what it must hand to the PM, and what it never does.
Talk Track:
If you took an agent course, you know boundaries and guardrails. Here they are, written for one job: answering people.
It may say what we know. Each claim with its source, date, segment and counts.
And it must say what we do not know. An answer is only as good as what it admits it does not know.
It hands you four things, in the flag report.
A source older than your age limit. Sources that disagree. A question that needs new research.
And thin evidence: a claim that rests on evidence with a fact label, like single source. Then it states the label and does not write "buyers want".
It never sends. It never commits the team to a roadmap item, a date or a price. It never writes "validated".
The age limit is your number. The case PM chose 18 months. Pick yours by how fast your market moves.
TRANSITION: Then the call is yours: send, change or hold.
```

### Slide 5.8: Send, change or hold
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: Send: it says what the sources say. Change: fix the words, then send. Hold: do not send yet. Before you send: open every citation.
- Visual intent: Three large buttons in a row: Send (teal), Change (navy), Hold (orange). Under them, one line with a magnifier icon.
- Sources: none (spec module 5 `pm_decision`, objective m5-o3)

Notes:
```
POINT: The PM makes one of three calls on each answer, and opens every citation before an answer is sent.
Talk Track:
Three calls.
Send. The answer says what its sources say, and no more.
Change. The facts are right, but the words go too far, or a count is missing. You fix it, then send.
Hold. Do not send yet. Maybe the question needs new research. Maybe it needs a conversation first.
Hold is not failure.
Your audit in this job: open every citation in one answer. Not glance at it. Open it.
Which answer? Pick one at random. Every answer you send carries your name.
TRANSITION: One more call is yours: what goes to validation.
```

### Slide 5.9: Validation is your call
- Layout: Blank
- Minutes: 1 (half day 1)
- On-slide text: Per segment, the agent proposes: an order, then "validation", "research" or "keep and watch". Every line says "proposal". You decide.
- Visual intent: Three segment columns (Distribution, Food service, Pharmacy and lab), each with 3 short rows tagged "proposal". An empty "your decision" box under each column.
- Sources: none (spec module 5 `build`, objective m5-o4, `segment_rule`; glossary "ranking and validation proposal")

Notes:
```
POINT: The agent proposes an order and a next step for each problem inside each segment, and the PM decides what goes to validation.
Talk Track:
In module 1 the agent proposed one ranking across the backlog.
Now it ranks inside each segment first. You know the segment rule: rank within a segment before any claim about it.
Then, for each problem, it proposes a next step. Validation research. Other research. Or keep and watch.
Every line says "proposal".
You decide the order and what goes to validation.
"Validated" is a word only you write, after the validation research is done.
TRANSITION: Here is your lab.
```

### Slide 5.10: Lab 5 brief
- Layout: Activity
- Minutes: 2 (half day 2)
- On-slide text: ACTIVITY. Lab 5: Add the stakeholder answer job. Goal: Answer stakeholder questions from your research store and backlog. Key actions: Add the job. Write your rules. Send 3 questions. Send, change or hold. Open every citation in one answer. Decide order and validation. Footer: "Full steps: your step card in the workbook (Pragmatic Learning Hub)."
- Visual intent: Orange "ACTIVITY" band. Goal at the top. 6 short key actions in large type. Workbook pointer in the footer. Nothing else on the slide.
- Sources: none

Notes:
```
POINT: In lab 5 you add the answer job, run three stakeholder questions, and decide what gets sent and what goes to validation.
Talk Track:
The goal of this activity is to extend your agent to answer stakeholder questions from your research store and your problem backlog.
The core message: an answer is only as good as what it admits it does not know.
These are the key actions. The full steps are on your step card in the workbook.
You downloaded the workbook from the Pragmatic Learning Hub. Open your platform's card now.
[WALK THE KEY ACTIONS IN ONE LINE EACH. DO NOT READ THE CARD ALOUD]
On your own work: your logs from this course, one or two of your own past study reports, and your last three stakeholder questions.
Otherwise use the Larkspan files: Q1, Q2 and Q5. Q3 is optional if you have time.
Record your decisions on the lab 5 record sheet in your kit. That is your evidence.
TRANSITION: Here is what done looks like.
```

### Slide 5.11: Lab 5: done when
- Layout: Activity
- Minutes: 2 (half day 2)
- On-slide text: ACTIVITY. Done when: Each answer has your send, change or hold. You opened every citation in one answer. Each segment has your order and validation decisions. Data safety box (standard text), plus: "Share answers only inside approved tools."
- Visual intent: Orange "ACTIVITY" band. Success check as 3 short lines. Standard data safety box at the bottom, the same box as the step cards, with the one added line. No warning box.
- Sources: none (spec module 5 `success_check`, `data_safety`; spec `data_safety_note`)

Notes:
```
POINT: The success check names your three manager decisions, and the data safety rule now covers what leaves your desk.
Talk Track:
The goal of this activity is to know what done looks like before you start.
Done when each answer has your call: send, change or hold.
You opened every citation in one answer.
And each segment has your order and your validation decisions.
[POINT TO THE DATA SAFETY BOX]
Same rule as every lab. Approved tool only.
One thing is new. Your research store holds customer names and quotes.
An answer leaves your desk. Share answers only inside approved tools.
Breakout rooms are by platform. Build and save your own agent. Share your screen only when someone is stuck.
Agent lost or behind? Rebuild it from kit-m5 first. It takes about 5 minutes.
[DO NOT ADD ANY WARNING. IF A LEARNER ASKS "IS THERE A PLANTED ERROR?", SAY:] Manage this agent the way you will on Monday.
TRANSITION: [OPEN BREAKOUT ROOMS BY PLATFORM. START THE TIMER: 30 MINUTES. HALF DAY: 28]
```

### Slide 5.12: Lab 5: Add the stakeholder answer job
- Layout: Activity
- Minutes: 30 (half day 28)
- On-slide text: ACTIVITY. 30 MIN. Time guide: 0 to 3: add 2 files. 3 to 7: write rule 5. 7 to 10: send 3 questions. 10 to 16: send, change or hold. 16 to 21: open every citation in one answer. 21 to 27: order and validation. 27 to 30: spare. "Build and save your own agent. Share your screen only when someone is stuck."
- Visual intent: Orange band. A timeline bar with the 7 blocks. Room by platform shown as 4 small tiles. Half day version: 21 to 26 order and validation, 26 to 28 spare.
- Sources: none (spec module 5 `card_step_minutes`: full day 3, 4, 3, 6, 5, 6; half day 3, 4, 3, 6, 5, 5)

Notes:
```
POINT: Learners add the answer job, run three questions from their step card, and make the PM calls on own or case data.
Talk Track:
The goal of this activity is to run one full turn of the manager loop on an agent that faces other people.
[VISIT EACH ROOM IN TURN. START WITH COPILOT, THEN GEMINI, THEN CHATGPT, THEN CLAUDE]
[AT MINUTE 3: ANYONE WHO HAS NOT ADDED THE 2 FILES GETS HELP FIRST]
[AT MINUTE 7: "Send your questions now, even if your rule is short."]
[AT MINUTE 10: "Read each answer. Write send, change or hold, and why."]
[AT MINUTE 16: "Pick one answer at random. Open every citation in it."]
[AT MINUTE 21: "Now the proposals. Write your order and validation decisions for each segment."]
[AT MINUTE 27: "Spare time: ask Q3, or one of your own questions."]
[COPILOT NO-LICENSE LEARNERS USE THE SPARE TIME FOR THE PASTES. CHECK THEY SENT THE BACKLOG FIRST, ALONE]
[COMMON FAILURES AND RECOVERY: SEE SECTION 9]
[DO NOT REVEAL THE ERROR. IF A LEARNER ASKS "IS THIS IT?", ASK: "Would you send this answer to that person today? Why?"]
TRANSITION: [CLOSE ROOMS AT MINUTE 30. HALF DAY: 28] Bring your record sheet. Keep your agent open.
```

### Slide 5.13: Audit reveal: whose evidence was it?
- Layout: debrief
- Minutes: 2 (half day 2)
- On-slide text: DEBRIEF. Which check or audit found the error? Did your audit change a decision? (Reveal after answers:) Q2 answer: "Buyers want a one-click inspection binder." Source: R-2025-07. 2025-09-12. Food service only.
- Visual intent: Navy band. 2 questions. On click: the Q2 draft sentence, then the R-2025-07 small-print header line enlarged, with date and segment circled in orange. Then the 2027 pharmacy and lab evidence: P08 and P02 rows.
- Sources: none (case `planted-errors.md` lab 5, `expected-results.md` lab 5, `m5-past-reports.md`)

Notes:
```
POINT: The agent answered a pharmacy and lab question from an old food service study, and only opening the citation showed it.
Talk Track:
[ASK THE 2 QUESTIONS. TAKE 2 OR 3 ANSWERS]
[REVEAL]
Here is the planted error. Q2, from the Head of Hardware: what do pharmacy and lab buyers want in a compliance report?
The draft says: "Buyers want a one-click inspection binder." It cites R-2025-07.
The citation is real. The report is in scope. So the citation check passes.
Now open it. The header is in small print: report date 2025-09-12. Segment: Food service only.
About 26 months old, past the 18-month age limit. And a different segment from the question.
Your age limit flag may have fired. The answer text still said "buyers want".
That is why you open the citation. A flag does not change the words that get sent.
What does the 2027 evidence say for pharmacy and lab? Two different needs.
One. Calibration certificates with the probe serial number. P08: 3 interviews, 3 accounts, September to October 2027. A won deal, D-2206. A lost deal, D-3105.
Two. Audit exports in the accreditor's or state board's format. P02 in pharmacy and lab: 1 interview, I-108, AI-moderated. Plus feedback from 2 accounts, A-14 and A-29.
The case PM held the roadmap commitment, and started 4 to 6 PM-held pharmacy and lab interviews on report needs.
[ASK: "Who changed their send, change or hold call after the audit?" TAKE 1 ANSWER]
[IF NO AGENT IN THE ROOM MADE THE ERROR, SHOW THE SAVED Q2 REHEARSAL OUTPUT. SEE SECTION 3, "BEFORE CLASS"]
[RELEASE KIT-FINAL ON THE LEARNING HUB NOW. NOT BEFORE THIS SLIDE: IT HOLDS THE LAB 5 FIX]
TRANSITION: So add a rule for what your audit found.
```

### Slide 5.14: Fix your brief
- Layout: debrief
- Minutes: 2 (half day 1)
- On-slide text: DEBRIEF. Add rule 6 under "My rules": "Do not use a source for a segment it did not study. ... Write what we know, with counts, dates and segments, and what we do not know."
- Visual intent: Navy band. The rule in a box, first and last sentence in full, the middle as "...". Timer 2 MIN.
- Sources: none (case `planted-errors.md` lab 5, "Fix the learner adds")

Notes:
```
POINT: The learner adds a rule that stops the agent from using a source for a segment it did not study.
Talk Track:
Write a rule for what your audit found. Put it under "My rules" as rule 6.
Here is the case PM's rule. Yours can be different.
"Do not use a source for a segment it did not study. Flag any source older than my age limit. Rank within a segment before any claim about it. Never write '<segment> buyers want' from 1 interview in that segment. Write what we know, with counts, dates and segments, and what we do not know."
The full text is in kit-final, in the lab 5 rules handout. Kit-final is on the Learning Hub now.
[1 MINUTE TO WRITE. HALF DAY: 30 SECONDS, THEN MOVE ON]
Save it. Gemini: select Save. Copilot: select Update.
TRANSITION: Did your rule work on a question you have not asked?
```

### Slide 5.15: Run Q4 and compare
- Layout: debrief
- Minutes: 3 (half day 3)
- On-slide text: DEBRIEF. 3 MIN. New chat. Send the questions file: "Run the stakeholder answer job for Q4". Pass: your step card, 4 items.
- Visual intent: Navy band. Timer 3 MIN. One-line instruction. Q4 quoted small: "Can I tell the reseller team that food service buyers want quiet hours?" Small card image with "pass condition".
- Sources: none (case `m5-stakeholder-questions.md` Q4; `expected-results.md` lab 5 second sample)

Notes:
```
POINT: Q4 tests the fixed brief and the segment rule on a question the learner has not asked.
Talk Track:
Run the check question now, on your fixed brief.
New chat. Send the questions file with: "Run the stakeholder answer job for Q4."
Q4 is from the PM of Larkspan Cloud. Can I tell the reseller team that food service buyers want quiet hours?
[START A 3-MINUTE TIMER. AFTER 2 MINUTES, READ THE PASS ITEMS]
Compare with the pass condition on your card.
One. The answer does not say "food service buyers want quiet hours".
Two. Each claim shows its date and segment.
Three. There is a "what we do not know" line.
Four. The flag report lists the old source, the thin evidence and the sources that disagree.
Here is what the evidence holds. Alert noise in Food service rests on 1 interview, I-105, AI-moderated, from September 2027.
Plus feedback from 2 Food service accounts in November, and one lost deal, D-3108.
No interview asks for quiet hours. The 2025 food service study says alert noise was minor, but it is past the age limit.
That is the segment rule test: no "food service buyers want" from 1 interview in that segment.
[TAKE 1 ANSWER: "Who passed all 4?" IF A RUN IS NOT DONE, SAY:] Finish it after class. The pass condition is on your card.
TRANSITION: One rule ties this all together.
```

### Slide 5.16: Rank within a segment before you claim anything
- Layout: debrief
- Minutes: 1 (half day 1)
- On-slide text: DEBRIEF. Rank within a segment before you claim anything about it. Case PM: validation for P01 and P02 (Distribution), P03 (Food service), P08 (Pharmacy and lab). Research: P06. Discovery: P10.
- Visual intent: Navy band. Three segment columns with the case PM's validation picks in teal. P06 and P10 in a small row below.
- Sources: none (case `expected-results.md` lab 5, "Expected PM decision")

Notes:
```
POINT: The PM, not the agent, decides the order in each segment and what goes to validation.
Talk Track:
The agent proposed. Here is what the case PM decided.
Validation: P01 and P02 in Distribution. P03 in Food service. P08 in Pharmacy and lab.
Research first: P06, the night alarm question. The buyers disagree, so test a priced offer.
Discovery: P10, inspector remote access. It has feedback, but no interview yet.
Everything else: keep and watch. The case PM sent nothing to validation on feedback counts alone.
Your calls can differ. What matters is that you rank inside the segment first, and defend each call with the evidence.
TRANSITION: So what do you do on Monday?
```

### Slide 5.17: What you do Monday
- Layout: Blank
- Minutes: 1 (half day 1)
- On-slide text: "Ask your agent the last stakeholder question you got. Open every citation before you send it."
- Visual intent: One line, large type. Calendar icon with "Monday".
- Sources: none

Notes:
```
POINT: The first real use of the answer job is your last stakeholder question, with every citation opened before you send.
Talk Track:
On Monday, find the last "what do we know" question someone asked you.
Ask your agent. Use your own logs and one or two past reports, in your approved tool.
Open every citation before you send the answer.
If you would not defend a line in a meeting, change it or hold it.
Your agent saves as you go. Gemini: you selected Save. Copilot: you selected Update.
TRANSITION: That was the last job. Let's close the course.
```

## 3. Demo script

Platform: Claude (Project). Before class:

1. Have the project "Market Evidence Agent" in its state after module 4: brief v5 in the instructions, 10 files in knowledge. Build it from `modules/m4/kit/kit-m5/` (brief v5 and 10 knowledge files).
2. Check that **Code execution and file creation** (or **Create and edit files**) is on.
3. Rehearse steps 1 to 9. Time the Q3 run. Save the output and screenshots in your instructor folder.
4. In the same rehearsal project, in a new chat, send the questions file with "Run the stakeholder answer job for Q2". Save the output. It is the backup for slide 5.13 if no agent in the room makes the error. Do not show it before the debrief.
5. Build a second project, "Market Evidence Agent (final)", from `kit/kit-final/`. Send the questions file with "Run the stakeholder answer job for Q4". Save the result. It is the backup for slide 5.15.
6. Keep a ChatGPT Project in the state after module 4 as the backup.

| Step | Instructor does | Screen shows | If it fails |
| --- | --- | --- | --- |
| 1 | Open **Projects**, then "Market Evidence Agent" | Brief v5 in the instructions. 10 files in project knowledge | Rebuild from `kit-m5` in about 5 minutes, or switch to the ChatGPT backup. Say: "This is what the catch-up kit is for." |
| 2 | Select **+** in project knowledge. Add `job-card-stakeholder-answers.md` and `past-reports.md` | 12 files in project knowledge | Paste both texts into the chat with the question in step 4 |
| 3 | Open the project instructions. Under "My rules", add rule 5: "Lab 5: Age limit: 18 months. Send any source older than 18 months to the flag report. Every answer is a draft for me. Name no person in an answer. Make no commitment for the team: no roadmap item, date or price." Select **Save instructions** | Rule 5 under "My rules" | Paste the rule at the top of the chat message in step 4 |
| 4 | Start a new chat in the project. Upload `m5-stakeholder-questions.md`. Send "Run the stakeholder answer job for Q3" | A draft answer to Q3, proposals by segment and a flag report. A file, or the full text in one message | If the agent answers all questions: say "The prompt names the question. That is why." Stop it and resend. If the run fails: switch to the ChatGPT backup. If both fail: show the rehearsal output |
| 5 | Point to the P06 claim | P06: 4 interviews (I-101, I-106, I-110, I-112), 3 accounts, Distribution only, 2027-09-08 to 2027-10-09. I-106 and I-112 are the same account | If a count differs, say: "That is what the citation audit is for." Do not fix it live |
| 6 | Point to the R-2027-03 citation | R-2027-03, 2027-05-20, Distribution: 5 of 9 want a service option, 4 of 9 want their own managers | If the date or segment is missing, say: "A quality check missed. That goes in your audit." |
| 7 | Point to "What we do not know" | No price for a monitoring service was tested (R-2027-03 limits; I-110 says "I'd pay") | If the line is missing, say: "The job card asks for it. Missing is an audit finding." |
| 8 | Point to the Distribution proposals | P01 and P02 proposed for validation. P06 proposed for research, not validation. Each line says "proposal" | If the agent writes "validated", say: "Only the PM writes that. Rule 3 in the brief." |
| 9 | Point to the flag report. Then download the output and save it | Flags: sources disagree; needs new research. A blank PM decision column | If a flag is missing, say: "Hand-off rules are not perfect. That is why you audit." |

Do not comment on R-2025-07, the Food service or Pharmacy and lab proposals, or any other question on screen. The demo shows the answer job working. The error is in Q2, which only the learners ask.

## 4. Lab brief

- Goal: Extend the course agent to answer stakeholder questions from the team's own research store and problem backlog.
- Core message: An answer is only as good as what it admits it does not know.
- PM decision: Whether a question needs new research or can be answered now, what to tell the stakeholder, the order of the problems in each segment, and which problems go to validation.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Module line: the research store holds customer names and quotes. Share answers only inside approved tools. Teaching point: an agent that faces other people sends your data further than a backlog does. Decide what it may say, and to whom.
- Setup: Zoom breakout rooms by platform, 3 to 5 learners. In person: tables by platform. Each card starts: "Build and save your own agent. Share your screen only when someone is stuck."
- Inputs: Own work: your logs from this course plus one or two past study reports, from an approved tool, and your last three stakeholder questions. Case: `kit/lab-5/` (job card, past reports), `m5-stakeholder-questions.md` (run: Q1, Q2 and Q5 core, Q3 optional; Q4 in the debrief). Files this lab: 3 (2 to the agent, 1 in chat). The logs are already in the agent.
- Planted error warning: None (last lab). No warning box, no hint, no audit hint.
- Success check: Each answer has your send, change or hold decision. You opened every citation in one answer. Each segment has your decided order and your validation decisions.
- Learner evidence: Send, change or hold decisions for the answers. Audit findings for the cited answer. The hand-off rules for what the agent may say (rule 5) and the rule added after the audit (rule 6). The PM's order and validation decisions by segment. Recorded on `lab-5-record-sheet.md`.

## 5. Step cards

All four cards have the same 6 core steps. Saving is in each card header, not a step. The debrief steps are on each card under the steps. Learners use the files in `kit/lab-5/` and the questions file from the case folder. Copilot learners use the `.txt` copies. No fast-start card (module 1 only). Card step minutes (spec): 3, 4, 3, 6, 5, 6 (half day 3, 4, 3, 6, 5, 5).

### Card: Claude
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Market Evidence Agent" from module 4. Lost or behind? Rebuild it from `kit-m5` first.
- Saves: **Save instructions** saves the instructions. Files save when you add them. Chats save as you go.
- Check date and vendor doc: Core steps use the same screen names as the module 3 card (checked 2026-11-27 by the module 2 and 3 verifiers; module 5 verifier rechecks). Claude Help Center, "How can I create and manage projects?" (https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects, page metadata 2026-11-06, cl-ui-09; share section: page metadata 2026-11-06, "Updated over 3 weeks ago" when seen 2026-11-27, cl-pj-02). "Create and edit files with Claude" (https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude, cl-ui-10).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Share answers only inside approved tools.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-stakeholder-answers` and `past-reports` to project knowledge with **+**. |
| 2 | Write rule 5 under "My rules" in the project instructions: your age limit and what the agent may say. |
| 3 | In a new chat, send the questions file with "Run the stakeholder answer job for Q1, Q2 and Q5". |
| 4 | Write send, change or hold for each answer on your record sheet. |
| 5 | Open every citation in one answer, picked at random, with your record sheet checklist. |
| 6 | Write your order and validation decisions for each segment on your record sheet. |

**Debrief:**
1. Add rule 6 under "My rules" for what your audit found.
2. In a new chat, send the questions file with "Run the stakeholder answer job for Q4".

Notes: No file in the answer? Check that **Code execution and file creation** (or **Create and edit files**) is on in **Settings**, then **Capabilities**. Team or Enterprise: ask your owner. The agent answers every question in the file? Check the prompt names the questions.

**Start here with sample data:** Add: `job-card-stakeholder-answers.md`, `past-reports.md`. Questions: `m5-stakeholder-questions.md`. Rule 5 on the case path: the case PM's age limit is 18 months. Own work: replace `past-reports` with one or two of your past study reports. Ask your last three stakeholder questions with "Run the stakeholder answer job".

**Pass condition (second sample, run in the debrief):** On your fixed brief, in a new chat. Send the questions file with "Run the stakeholder answer job for Q4". Pass if: (1) The answer does not say "food service buyers want quiet hours". (2) Each claim shows its date and segment. (3) The answer has a "what we do not know" line. (4) The flag report lists old sources, thin evidence (a fact label) and sources that disagree.

**Done early:** Ask Q3. Or ask one question from your own work.

**Stretch (vendor doc checked, not yet tested):**
- Share plan (all platforms). Fill in section 7 of your record sheet.
- Share the agent (Team or Enterprise plan only). After class, with a colleague in your company. Vendor doc checked 2026-11-27. Not yet tested by the course team.
  1. A **Can view** member sees the instructions and all knowledge files. If any file must stay private, stop here.
  2. Project memory may also carry what you said in this project. If that must stay private, stop here.
  3. Open the project. Select **Share project**.
  4. Add one colleague by name or email.
  5. Choose **Can view**, then select **Share**.
  6. Ask your colleague to send you their first answer. Audit it with your record sheet checklist.
  To stop sharing, open the sharing menu. Select their role, then **Remove access**. Your admin can turn project sharing off. Then stop the stretch.

### Card: ChatGPT
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Market Evidence Agent" from module 4. Plan: Go or Plus or higher. Lost or behind? Rebuild it from `kit-m5` first.
- Saves: As you go.
- Check date and vendor doc: Core steps use the same screen names as the module 3 card (checked 2026-11-27; module 5 verifier rechecks). OpenAI Help Center, "Projects in ChatGPT" (https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt, "Updated: 3 days ago" when seen 2026-11-27, cg-ui-09; share section cg-02).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Share answers only inside approved tools.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-stakeholder-answers` and `past-reports` to the project's files. |
| 2 | Write rule 5 under "My rules" in **Project settings**: your age limit and what the agent may say. |
| 3 | In a new chat, send the questions file with "Run the stakeholder answer job for Q1, Q2 and Q5". |
| 4 | Write send, change or hold for each answer on your record sheet. |
| 5 | Open every citation in one answer, picked at random, with your record sheet checklist. |
| 6 | Write your order and validation decisions for each segment on your record sheet. |

**Debrief:**
1. Add rule 6 under "My rules" for what your audit found.
2. In a new chat, send the questions file with "Run the stakeholder answer job for Q4".

Notes: **Project settings** is in the **•••** menu of the project. No file in the answer? The brief asks for the full text in one message. That is fine.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run in the debrief):** Same as the Claude card.

**Done early:** Same as the Claude card.

**Stretch (vendor doc checked, not yet tested):**
- Share plan (all platforms). Fill in section 7 of your record sheet.
- Share the project. After class, with a colleague in your company. Vendor doc checked 2026-11-27. Not yet tested by the course team.
  1. Members see all chats, files and instructions in the project, and can download the files. If any must stay private, stop here.
  2. Open the project. Select **Share**.
  3. Keep **Only those invited**. Do not share a link.
  4. Enter your colleague's name or email.
  5. Choose chat access, not edit access.
  6. Ask your colleague to send you their first answer. Audit it with your record sheet checklist.
  Only the owner can remove a member. Your workspace settings can limit sharing.

### Card: Copilot agent builder
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the agent "Market Evidence Agent" from module 4. To open it: **All agents**, then **...** next to it, then **Edit**. Lost or behind? Rebuild it from `kit-m5` first.
- Saves: **Update** after each change.
- Check date and vendor doc: Core steps use the same screen names as the module 3 card (checked 2026-11-27; module 5 verifier rechecks). Microsoft Learn, "Add knowledge sources" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge, "Last updated on 2026-11-16", mb-ui-12). "Share and manage agents" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents, "Last updated on 2026-11-16", mb-ui-13). Microsoft Support, "Add content to Microsoft 365 Copilot Chat prompts" (ms.date 2026-11-18, mb-ui-14, partly verified).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Share answers only inside approved tools.

| Step | Do this |
| --- | --- |
| 1 | On the **Configure** tab, add `job-card-stakeholder-answers.txt` and `past-reports.txt` with **Upload**. |
| 2 | Write rule 5 under "My rules" in **Instructions**: your age limit and what the agent may say. |
| 3 | In a new chat, send the questions file with "Run the stakeholder answer job for Q1, Q2 and Q5". |
| 4 | Write send, change or hold for each answer on your record sheet. |
| 5 | Open every citation in one answer, picked at random, with your record sheet checklist. |
| 6 | Write your order and validation decisions for each segment on your record sheet. |

**Debrief:**
1. Add rule 6 under "My rules" for what your audit found. Select **Update**.
2. In a new chat, send the questions file with "Run the stakeholder answer job for Q4".

Notes: Use the `.txt` copies. To send the questions file, upload it, or paste the text. Download any file the agent makes in the same session. Copilot keeps it for that session only.

**No Copilot license or billing?** Your agent cannot read Knowledge files. Do this instead:
1. Paste all of `copilot-fallback-instructions-m5.txt` into **Instructions**. It replaces the module 4 text.
2. Skip card step 1. You cannot add knowledge files. Your own rules differ from the kit? Put yours under "My rules".
3. Before step 3, in the new chat, send `problem-backlog.txt` in its own message.
4. Then send `driver-log.txt`, `alternatives-map.txt` and `past-reports.txt` in a second message.
5. Debrief Q4: in the new chat, send the same 2 messages first.
Upload each file, or paste the text. The backlog does not fit in one message? Split it at "## Proposed ranking after lab 3".
The past reports go in chat because your rules would take Instructions over 8,000 characters. The fallback agent does one job at a time.

**Start here with sample data:** Add: `job-card-stakeholder-answers.txt`, `past-reports.txt`. Questions: `m5-stakeholder-questions.md`. Rule 5 and own work: as on the Claude card.

**Pass condition (second sample, run in the debrief):** Same as the Claude card. Upload the questions file, or paste the text.

**Done early:** Same as the Claude card.

**Stretch:**
- Share plan (all platforms). Fill in section 7 of your record sheet. Do not share the agent.
- The share step is not on this card. Copilot and Gemini cards stay on the core path in this course.

### Card: Gemini
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the skill "market-evidence-agent" from module 4. Find it in **Customize**, then **Skills**. Click it to edit. This is a Gemini skill. Gems are now skills. Lost or behind? Rebuild it from `kit-m5` first.
- Saves: **Save** after each change.
- Check date and vendor doc: Core steps use the same screen names as the module 3 card (checked 2026-11-27; module 5 verifier rechecks). Gemini Apps Help, skills page (https://support.google.com/gemini?p=pn_skills, page shows no date, gm-ui-10; module 1 decision D3 accepts it with a check date). Google blog, "Let skills in Gemini tackle your most repetitive tasks" (https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/, 2026-09-30) for **/**. Share: Google Workspace Updates post (https://workspaceupdates.googleblog.com/2026/11/share-skills-add-files-from-Drive-Notebook-Photos-to-skills-Gemini-app.html, 2026-11-16, seen 2026-11-27, gm-04).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Share answers only inside approved tools.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-stakeholder-answers` and `past-reports` to your skill with **Add files**. |
| 2 | Write rule 5 under "My rules" in the skill **Instructions**: your age limit and what the agent may say. |
| 3 | In a new chat, send the questions file with "/market-evidence-agent Run the stakeholder answer job for Q1, Q2 and Q5". |
| 4 | Write send, change or hold for each answer on your record sheet. |
| 5 | Open every citation in one answer, picked at random, with your record sheet checklist. |
| 6 | Write your order and validation decisions for each segment on your record sheet. |

**Debrief:**
1. Add rule 6 under "My rules" for what your audit found. Select **Save**.
2. In a new chat, send the questions file with "/market-evidence-agent Run the stakeholder answer job for Q4".

Notes: Type **/** (or **@**) in the chat and pick your skill from the list. If adding files to the skill fails, upload the whole skill again with all its files. If a chat upload fails, paste the text. Do not turn on Canvas or Deep Research.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run in the debrief):** Same as the Claude card. Use the prompt "/market-evidence-agent Run the stakeholder answer job for Q4".

**Done early:** Same as the Claude card.

**Stretch:**
- Share plan (all platforms). Fill in section 7 of your record sheet. Do not share the skill.
- The share step is not on this card. Copilot and Gemini cards stay on the core path in this course. The dated Google post names no screen labels for it.

## 6. Debrief

- Questions: Which check or audit found the error? Did your audit change a send, change or hold decision? Would you send the fixed Q2 answer to the Head of Hardware? Which problems in each segment would you send to validation?
- Error reveal (record ids): Q2 in `m5-stakeholder-questions.md` (Head of Hardware: "What do pharmacy and lab buyers want in a compliance report? I want to commit a report pack for them in the 2028 roadmap."). Before the fix, the answer says "Buyers want a one-click inspection binder" and cites R-2025-07 in `m5-past-reports.md`. R-2025-07: report date 2025-09-12 (about 26 months old in November 2027), Food service only, date and segment in a small-print header, finding 1 in bold. The citation check passes because the report is in scope and the citation is real. The age limit flag may fire, but the answer text still says "buyers want". What finds it: opening the citation.
- 2027 pharmacy and lab evidence (`case/expected-results.md`, Q2 row): (1) calibration certificates with probe serial numbers: P08, 3 interviews, 3 accounts (I-107, I-108, I-113, September to October 2027); won D-2206; lost D-3105. (2) Audit exports in the accreditor's or state board's format: P02 in Pharmacy and lab, 1 interview (I-108, AI-moderated, September 2027) and feedback from 2 accounts (A-14, A-29, November 2027).
- Fix the learner adds (`case/planted-errors.md`, lab 5): "Do not use a source for a segment it did not study. Flag any source older than my age limit. Rank within a segment before any claim about it. Never write '<segment> buyers want' from 1 interview in that segment. Write what we know, with counts, dates and segments, and what we do not know."
- Debrief check (instructor only; `case/expected-results.md` lab 5): The fixed Q2 answer names the date and segment of every source. The flag report lists R-2025-07 as old evidence for another segment. The answer does not say "buyers want". The agent ranks within each segment before any segment claim. Ranking and validation proposals stay labeled as proposals until the PM decides. The agent does not write "food service buyers want" from the one Food service interview (I-105; decision 3 test, in Q4).
- Expected answers and PM decisions (`case/expected-results.md`, lab 5):

| Question | Answer says | Flags | Case PM decision |
| --- | --- | --- | --- |
| Q1 VP Sales | Interviewed buyers do not name price. D-2211 and D-3107: budget or grant timing. D-3105: Rimecore's on-site calibration. Only D-2210 says price, and it is CRM only. 3 interviewed Pharmacy and lab losses in 2 quarters (Q2 and Q3 2027). What we do not know: price sensitivity in this segment | Small count, stated in the answer. D-2210 is CRM only | Change, then send: "the 3 interviews we have do not point to price". Add the next pharmacy losses to the interview list |
| Q2 Head of Hardware (planted) | See above. R-2025-07 not used | Old evidence for another segment. Report effort in Pharmacy and lab is 1 interview: single source in this segment, AI-moderated only. Needs new research | Hold the roadmap commitment. Change the answer and start research |
| Q3 Support lead (optional; demo) | Buyers disagree. P06: 4 interviews, 3 accounts, Distribution only. R-2027-03: 5 of 9 want a service option, 4 of 9 own managers. No price tested | Sources disagree. Needs new research | Change, then send as "split; test a priced offer before Support plans staff" |
| Q5 FDP PM (internal) | P03: 3 interviews (I-103, I-111 PM-held; I-105 AI-moderated), 2 accounts, all Food service. Feedback A-04, A-30. 1 Distribution lost deal D-2203 (Q2 2027). No Pharmacy and lab evidence. What we do not know: how many sites in the whole fleet lose hub signal; FDP device-health data can answer it | One segment only. "Many customer sites" not supported. The FDP backlog order is the internal PM's decision | Send. Add one line: pull hub drop counts by segment from FDP before placing the request |

- Q5 pass condition (instructor only): The answer does not say "hubs lose signal at many customer sites" or name all segments. It names Food service as the only segment with interviews, and shows D-2203 with its segment and quarter. It has a "what we do not know" line that points to FDP fleet data. It leaves the FDP backlog order to the FDP PM.
- Check question Q4 (3 minutes; `case/expected-results.md` lab 5 second sample): Expected evidence: P01 has 1 Food service interview (I-105, AI-moderated, 2027-09-14). Feedback from 2 Food service accounts (A-09, A-28, week of 2027-11-09). Lost deal D-3108. Inside Food service, P01 is not the top proposed rank. No interview asks for quiet hours. R-2025-07 says alert noise was minor in 2025, but it is over the age limit. Pass (the same 4 items as the card; the card's item 4 is general): (1) No "food service buyers want quiet hours". (2) Each claim shows its date and segment. (3) A "what we do not know" line. (4) The flag report lists R-2025-07 as over the age limit, the Food service interview evidence as 1 interview (single source in this segment, AI-moderated only), and the 2025 and 2027 sources as in disagreement.
- Proposals by segment, case PM decision: Send to validation: P01 and P02 (Distribution), P03 (Food service), P08 (Pharmacy and lab). Research: P06. Discovery: P10. Keep and watch: the rest. No problem goes to validation on feedback counts alone (for example P04 and P09: 3 accounts each in week 2).
- What you do Monday: Ask your agent the last stakeholder question you got. Open every citation before you send it.
- Log save card: none in module 5 (B9, D9). Lab 5 writes no log. The course close saves the brief, the logs and kit-final (C.4).

## 7. LD spec

| Field | Value |
| --- | --- |
| Objective | Extend the Market Evidence Agent with a stakeholder answer job that cites a source, date and segment for each claim and states what we do not know; write rules for what it may say; decide send, change or hold for each answer after opening every citation in one; and decide the order and what goes to validation in each segment (m5-o1 to m5-o4) |
| Timing | Lab 30 minutes (half day 28). Card step minutes 3, 4, 3, 6, 5, 6 (half day 3, 4, 3, 6, 5, 5), 3 minutes slack (half day 2). Debrief 9 (reveal 2, brief fix 2, Q4 3, segment rule 1, Monday 1). Half day 8 (brief fix 1). Lab brief before it: 4 minutes (2 short slides; full steps on the step cards in the workbook) |
| Setup (Zoom) | Breakout rooms by platform (Claude, ChatGPT, Copilot, Gemini), 3 to 5 learners each. Learners keep their own screen. Share only when stuck. Instructor visits rooms in turn, Copilot first |
| Setup (in person) | Tables by platform, 3 to 5 learners. One laptop per learner. Instructor walks the tables, Copilot first |
| Steps per platform | See section 5 (4 cards with the same 6 core steps and the same 2 debrief steps). No fast-start card. Stretch: share plan on all 4 cards. Share steps on Claude (Team, Enterprise) and ChatGPT only, after class, "not yet tested by the course team". Copilot and Gemini stay on the core path (spec `stretch_scope`). No second-agent or schedule step (spec) |
| Materials | `kit/lab-5/` (job card, past reports, Copilot fallback text, record sheet, README). Case file `m5-stakeholder-questions.md`. `modules/m4/kit/kit-m5/` to rebuild before the lab. `kit/kit-final/` for the course close: release it on the Learning Hub only after slide 5.13 (it holds the lab 5 fix). Instructor only: `case/planted-errors.md`, `case/expected-results.md`, saved demo output (Q3), saved Q2 rehearsal output, saved Q4 result from the final project |
| Success criteria | Each answer has the learner's send, change or hold decision. Every citation in one answer opened and recorded. Each segment has the learner's order and validation decisions. Debrief: rule 6 added; Q4 passes the 4-item pass condition |
| Debrief questions | Which check or audit found the error? Did your audit change a send, change or hold decision? Would you send the fixed Q2 answer? Which problems in each segment go to validation? |
| Fallback path | Cannot use own work: case data. Agent lost or behind: rebuild from `kit-m5` (about 5 minutes). Platform blocked: pair with a learner on another platform. Copilot with no license: `copilot-fallback-instructions-m5.txt`, then the backlog alone, then the driver log, map and past reports, then the questions. Upload fails: paste the text. No file output: full text in one message (brief rule 7). Agent does not make the error: show the saved Q2 rehearsal output. Q4 not done in 3 minutes: finish after class |
| Learner evidence | Send, change or hold decisions for the answers. Audit findings for the cited answer. Rule 5 (age limit and what the agent may say) and rule 6 (after the audit). The PM's order and validation decisions by segment. All on `lab-5-record-sheet.md` |

## 8. Learner kit

Character counts measured with `wc -m` on 2026-11-27. Copilot course budget (spec `copilot_no_license_fallback`): core brief 3,500 or fewer, job card 1,500 or fewer, knowledge file 2,800 or fewer, total 7,800 or fewer. Vendor limit: Instructions 8,000 characters (mb-01). Every `.txt` copy matches its `.md` file (`cmp`).

| File | Loads into | Characters | `.txt` copy |
| --- | --- | --- | --- |
| `lab-5/job-card-stakeholder-answers.md` | Knowledge | 1,398 (budget 1,500) | yes |
| `lab-5/past-reports.md` (copy of `case/m5-past-reports.md`) | Knowledge | 2,773 (budget 2,800) | yes |
| `lab-5/copilot-fallback-instructions-m5.txt` (brief v5 and job card) | Copilot Instructions, no license | 5,293 (limit 8,000) | is a `.txt` |
| `lab-5/lab-5-record-sheet.md` | Not loaded. Learner keeps it | 2,272 (not loaded) | no |
| `lab-5/README.md` | Not loaded | not counted | no |
| `modules/m4/kit/kit-m5/brief-v5.md` (start state; rule 4 in "My rules") | Instructions | 3,491 (budget 3,500) | yes |
| `modules/m4/kit/kit-m5/driver-log.md` (Q2 and Q3; D2) | Knowledge | 7,616 (a log) | yes |
| `modules/m4/kit/kit-m5/alternatives-map.md` (end of Q3 2027) | Knowledge | 3,286 (a case knowledge file, updated in lab 4; Copilot no license pastes it in chat) | yes |
| `modules/m4/kit/kit-m5/job-card-alternatives-map.md` | Knowledge | 1,497 (budget 1,500) | yes |
| `kit-m5-draft/` (same text as the delivered kit-m5 files), `kit-m5-expected.md` | Not loaded. Hand-over record | not counted | no |
| `kit-final/brief-v6.md` (rules 1 to 6) | Instructions | 4,008 (over the 3,500 budget; D16) | yes |
| `kit-final/job-card-problem-backlog.md`, `job-card-win-loss.md`, `job-card-weekly-feedback.md` (no change) | Knowledge | 1,194; 1,483; 1,496 | yes |
| `kit-final/job-card-alternatives-map.md` (from module 4 kit-m5; D8 closed) | Knowledge | 1,497 | yes |
| `kit-final/job-card-stakeholder-answers.md` | Knowledge | 1,398 | yes |
| `kit-final/code-book.md`, `driver-code-book.md`, `tag-list.md` (no change) | Knowledge | 2,791; 2,284; 2,038 | yes |
| `kit-final/alternatives-map.md`, `past-reports.md` | Knowledge | 3,286; 2,773 | yes |
| `kit-final/problem-backlog.md` (no change from kit-m4), `driver-log.md` | Knowledge | 15,194; 7,616 | yes |
| `kit-final/lab-5-fix-rules.md` | Not loaded. Handout | 1,155 | yes |
| `kit-final/copilot-fallback-instructions-m5-v6.txt` | Copilot Instructions, no license, to rerun job 5 | 5,813 (limit 8,000) | is a `.txt` |
| `kit-final/monday-plan.md` | Not loaded. Course close sheet | 2,048 (not loaded) | no |
| `kit-final/README.md` (with the rebuild card) | Not loaded | not counted | no |

Fallback sum check (module 5): header 399 + brief v5 3,491 + separator 5 + job card 1,398 = 5,293. Learner rule 5 (about 220) and rule 6 (about 330) bring it to about 5,850, under 8,000. With the past reports in Instructions it would be 7,662 before rule 5, and about 8,210 after rule 6 (over the limit; D3). kit-final fallback: header 402 + brief v6 4,008 + separator 5 + job card 1,398 = 5,813.

Copilot no-license pastes (target 15,400 each): message 1, `problem-backlog.txt` 15,194. Message 2, `driver-log.txt` 7,616 + `alternatives-map.txt` 3,286 + `past-reports.txt` 2,773 = 13,675. Message 3, the questions file 1,667. Debrief: messages 1 and 2 again, then the questions file.

Spec P3 check "core instructions stay under 8,000 characters": brief v5 3,491; brief v6 4,008.

Knowledge files in the agent after module 5: 12 (5 job cards, 5 case knowledge files, 2 logs). Course budget 13. Spec `uploads_per_lab` module 5: 2 files to the agent, 1 in chat (the questions file, which holds the check question).

## 9. Instructor notes

- Timing flex:
  - Behind before the lab: cut the story slot (5.4) and the question on 5.2. Never cut the lab brief (5.10, 5.11) or the data safety box.
  - Behind in the demo: at minute 5 of 5.5, open the rehearsal output. Teach 5.6 from it.
  - Behind in the lab: at minute 21, tell learners to fill section 4 of the record sheet from the proposals, even if the audit is not done. The reveal works from the step 3 run.
  - Behind in the debrief: keep the reveal (5.13) and Q4 (5.15). Cut 5.14 to the rule on screen, written after class. Cut 5.16 to one line.
  - Ahead: learners do "Done early": Q3, or one question from their own work. Or the share plan (record sheet section 7).
- Half day: the module is 60 minutes (spec `half_day`). 5.4 has no story slot. 5.5 is 5 minutes. The lab is 28 minutes, step 6 has 5 minutes. 5.14 is 1 minute.
- Common failures and recovery:

| Failure | Recovery |
| --- | --- |
| Agent lost or broken after module 4 | Rebuild from `kit-m5` (about 5 minutes), then do step 1 |
| The agent answers all questions in the file, including Q4 | Check the prompt names the questions: "for Q1, Q2 and Q5". Tell the learner to skip the Q4 answer until the debrief. Q4 still works as the check on the fixed brief |
| The agent runs another job (for example the problem backlog job) | Check the prompt says "Run the stakeholder answer job". Check `job-card-stakeholder-answers` is in knowledge |
| The agent cannot find the driver log, the map or the backlog | Check the 3 logs are in knowledge. Copilot no license: they must be pasted in chat, in 2 messages, before the questions |
| Copilot: the agent ignores the knowledge files (no license or billing) | Use the no-license box on the Copilot card |
| Copilot no license: a pasted message is too long | Split the backlog at "## Proposed ranking after lab 3". Send part 1 with "This is part 1 of the problem backlog. Wait for part 2." Microsoft publishes no message limit (module 3 D5) |
| Copilot no license: rule 5 or 6 does not fit in Instructions | It should fit (about 5,850 in total). If the learner pasted the past reports into Instructions, remove them and paste them in chat |
| Gemini: adding files to the existing skill fails | Use **Add files** on the existing skill. If it still fails, upload the whole skill again with all its files (gm-01) |
| Claude: no file in the answer | Turn on **Code execution and file creation** (**Create and edit files**). Or accept the full text in one message (brief rule 7) |
| The answer stops halfway (long output) | Send "Continue". Or send "Give the answers and the flag report first, then the proposals" |
| An answer has no "what we do not know" line, or a citation has no date or segment | Audit finding. Point to the job card quality checks. Rerun the one question |
| The agent writes "validated" or "pattern" | Audit finding. Point to brief rule 3. Rerun |
| The agent says "food service buyers want" or "buyers want" from 1 interview | Audit finding. Point to brief rule 4 (the segment rule). It is the Q4 test in the debrief |
| The agent does not make the planted error (Q2 already flags R-2025-07 and avoids "buyers want") | Good. Ask the learner which line in the brief or job card stopped it. In the debrief, show the saved Q2 rehearsal output |
| The learner's random pick is Q1 or Q5 and the audit finds nothing | Fine. A clean audit is a real result. The reveal shows Q2. Ask in 5.13: "What would have found it, if you had picked Q2?" |
| A learner's own past report or question holds client names or personal data | Stop. Use the case data, or remove the names. Data safety box |
| Share stretch: "Share project" or "Share" is missing | The plan or the admin does not allow sharing. Stop the stretch. Keep the share plan |

- Case notes (module builder, checked 2026-11-27 against the case files):
  1. OI-19 (owner module builder). F-1108 (week 1, A-07 Quarry Lane Pharmacies) and F-1214 (week 2, A-29 Elmstead Pharmacy) are P02 feedback items from lab 3. They support the Q2 report pack answer but are not lab 5 inputs. In the agent's backlog, A-29 is named in P02 "other sources" (week 2, with A-14). A-07 is only in the week 1 count ("Week 1: 3 accounts"). The expected Q2 answer uses A-14 and A-29 only. Accept an answer that also counts week 1.
  2. R-2027-03 (2027-05-20) is within the 18-month limit. An agent that flags it as old has misread the date. That is an audit finding.
  3. R-2025-07 finding 4 says calibration certificates came up in 1 of 14 food service interviews. An agent may use it to play down P08 in Pharmacy and lab. That is the same error (another segment's study), in a second form.
  4. The expected Q2 flag says report effort in Pharmacy and lab is "single source in this segment, AI-moderated only". P02 has no fact label across the whole backlog (6 interviews, 3 segments). The label applies inside the segment. Accept either wording if the answer states 1 interview, I-108, AI-moderated.
  5. Q1: D-2206 (Pharmacy and lab, won, calibration certificates) may appear in the answer. It is a win, not a loss. Fine if labeled.
  6. Q4: if the learner pasted week 2 feedback, the agent may add that 1 account asks for quiet hours (A-09, F-1207). That is still 1 account.
  7. P10 (module 3 D2): lab 5 needs P10 only in the Food service proposals ("Not ranked", discovery). A learner whose own backlog has no P10 row gets no P10 line. Accept it.
  8. The case question file holds the line "The case PM's hand-off rule: evidence older than 18 months goes to the flag report." It tells learners the case age limit for rule 5. It does not say which report is old.
  9. The demo answers Q3 on brief v5 with rule 5. Learners who ask Q3 in the spare time see the same flags.
- Kept off the slides on purpose: any repository or duplicate-research figure (W13 survey figures fail the 2026 rule; W20 has no data). "Product managers do not remember study names" and "teams commission new studies" (W20 only; B14). The manager loop circle (slide 1.7) and the "no magic number" slide (1.14) in the course close (B12). Any second-agent or schedule slide (spec: not in module 5).
- Registry guard: No workshop teaches research reuse (spec `registry_guard`). AI Agents course boundaries and guardrails are referred to as known; slide 5.7 is new and written for an agent that faces other people (decision 33). Not the Competitive Intel Watchdog. CAW-AI "exit packet with two scheduled tasks" is not used: the course close saves a text kit and a Monday plan, with no scheduled task.

## 10. Course close

Runs after module 5. Full day 15 minutes (5 instructor-led, 10 hands-on). Half days 10 minutes (4 instructor-led, 6 hands-on). Spec `course_close`. C.3 (kit-final) sits in the hands-on Monday plan segment, because the spec puts "saves kit-final" there (consistency finding 11). The C.1 extra minute (full day) goes to one learner answer: "Which audit surprised you most?"

### Close minutes check

| Segment | Slides | Minutes (full day) | Minutes (half day) | Mode |
| --- | --- | --- | --- | --- |
| Recap of the manager loop. Theme: there is no magic number | C.1, C.2 | 3 + 2 = 5 | 2 + 2 = 4 | Instructor-led |
| Monday plan: take home kit-final, then plan | C.3, C.4 | 1 + 9 = 10 | 1 + 5 = 6 | Hands-on |
| Total | 4 slides | 15 | 10 | |

### Slide C.1: Five audits, five rules
- Layout: Blank
- Minutes: 3 (half day 2)
- On-slide text: Table. Lab 1: quote check passed; evidence profile found it; single-source rule. Lab 2: quote check; deal source; CRM-only rule. Lab 3: reason check; no fit group; no fit rule. Lab 4: link check; the interview; buyer's answer rule. Lab 5: citation check; the source header; segment rule.
- Visual intent: A 5-row table with 4 columns: Lab, The check that passed, What found it, The rule you added. Short words, large type. "What found it" column in orange.
- Sources: none (case `planted-errors.md` summary table; spec `course_agent.manager_loop`)

Notes:
```
POINT: In every lab a quality check passed while the error was still there, and the audit and a new rule fixed it.
Talk Track:
Look back at the day.
Five labs. Five planted errors.
Every time, a quality check passed. The quotes were real. The links were real. The citations were real.
And every time, the error was still there.
Your audit found it. The evidence profile. The deal source column. The "no fit" group. The interview behind the CRM field. The header of an old report.
Then you wrote a rule. Your brief now has six rules. Five came from your audits.
That is the manager loop, five times. Brief, checks, hand-off rules, run, review, audit, tune, run again.
The checks catch what you predicted. Your audit catches what you did not.
[FULL DAY: ASK "Which audit surprised you most?" TAKE 1 ANSWER]
TRANSITION: And in every lab, one call stayed with you.
```

### Slide C.2: Five calls the agent never made
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: You decided: the order of problems by segment. What sales hears. Which problems need discovery. The alternative to beat. What gets sent, and what goes to validation. Bottom line: "No magic number. The agent proposes. You decide."
- Visual intent: Five short lines, one per module, with a small module number in a circle. The bottom line in orange.
- Sources: none (spec `course_close`, `course.themes`; module `pm_decision` fields)

Notes:
```
POINT: The agent proposed in every module, and every decision stayed with the PM, because there is no magic number.
Talk Track:
In every module the agent proposed. It never decided.
Module 1: you decided the order of your top problems in each segment.
Module 2: you decided which win/loss findings go to sales, and how to frame them.
Module 3: you decided which problems move, and which need discovery.
Module 4: you decided which alternative to beat in each segment.
Module 5: you decided what gets sent, and what goes to validation.
No number in the brief made those calls. There is no magic number.
The agent proposes. You decide.
TRANSITION: Now take it home.
```

### Slide C.3: Take it home: kit-final
- Layout: Activity
- Minutes: 1 (half day 1)
- On-slide text: ACTIVITY. Download kit-final from the Learning Hub: brief v6, 5 job cards, 5 knowledge files, 2 logs, a rebuild card. On your work: change the [EDIT] line and your age limit. Use your own code book. Start the logs empty.
- Visual intent: A folder icon labeled kit-final with 3 small stacks (brief, job cards, files). A 4-item checklist on the right.
- Sources: none (spec `catch_up_kits` kit-final; `kit/kit-final/README.md`)

Notes:
```
POINT: kit-final holds the complete agent, so each learner can rebuild it on their own work in about 5 minutes.
Talk Track:
The goal of this activity is to download kit-final and know what is in it.
Download kit-final from the Learning Hub now. It is the folder you got after the lab 5 reveal.
It holds the complete agent. Brief v6 with all your rules. Five job cards. Five knowledge files and two logs.
And a rebuild card for your platform. About 5 minutes.
On your own work, change four things.
The [EDIT] line: your product, your market, your segments.
Your age limit.
Your own code book, tags and drivers.
And start the logs empty. Your evidence, not Larkspan's.
TRANSITION: One last activity. Your Monday plan.
```

### Slide C.4: Your Monday plan
- Layout: Activity
- Minutes: 9 (half day 5)
- On-slide text: ACTIVITY. 9 MIN. 1. Pick the first job you run on your own work. 2. Set your audit date. 3. Save kit-final with your brief and your logs. Sheet: `monday-plan.md` in kit-final.
- Visual intent: Orange band. Three numbered steps, large. A calendar icon with an empty date. Timer 9 MIN (half day 5).
- Sources: none (spec `course_close` segment 2)

Notes:
```
POINT: Each learner leaves with a first job to run on their own work, an audit date and a saved kit.
Talk Track:
The goal of this activity is to leave with a plan you will run on Monday.
Open monday-plan.md in your kit-final folder.
One. Pick the first job you will run on your own work. One job, not five.
Pick the one where your team loses the most time today.
Two. Set the date of your first audit. Write what you will audit. Use the same sample size as in the lab.
Three. Save kit-final. Copy your brief text into my-brief.txt. Download your logs into the folder.
[START A 9-MINUTE TIMER. HALF DAY: 5. WALK THE ROOM OR VISIT THE BREAKOUT ROOMS]
[AT MINUTE 6, HALF DAY MINUTE 3: TAKE 2 ANSWERS: "Which job first, and when is your audit?"]
[IF A LEARNER CANNOT USE THEIR OWN WORK IN THEIR TOOL:] Then step one is a question for your IT or security team. Write it down as your first job.
Thank you. You came in with a platform. You leave with an agent you manage.
[END OF COURSE]
```
