# Module 1: The quarterly portfolio pack: is the work consistent with the strategy?

Course: Advanced AI for Product Strategy and Planning (`product-strategy-and-planning`). Stage 3 draft by the module builder, 2026-11-27. Built from `spec.yaml` (Gate 2, approved 2026-11-27), `outline/development-brief.md`, `outline/gate-2-decisions.md` (rows 1 to 17), `outline/gate-2-changes.md`, `outline/proof-kit-drafts.md` (P1) and the case files. The course open (25 minutes before this module) is in `course-open.md`. Format model: `courses/market-research/modules/m1/` (no content or slide copied).

## 1. Summary

| Item | Value |
| --- | --- |
| Workflow row and bottleneck | sp-wf-09 (folds sp-wf-01). Assemble the quarterly portfolio review pack and check that planned work stays consistent with the stated strategy. Bottleneck: the pack runs on decks that are stale before the meeting. One person stitches updates by hand, so the meeting becomes data reconciliation instead of decisions. Leaders say strategy is clear, but few can show the work is linked to it (W22; W1 with W2 as one source; W3). On slides in words only (OI-10) |
| Framework category and focus area | Focus. Product Portfolio |
| Capability Standards (as in spec) | Confirmed by Dan (Gate 2 Q2). Skill 2.1 Strategy Alignment. Competency 2.1B Explicit vs. Implicit Strategy Analysis. Not taught: 2.1C Strategy Matrix Application, 2.1A Strategic Definition |
| Rung | 1, Hand-run batch |
| Minutes (full day / half day) | 70 / 80 |
| Instructor-led / hands-on (minutes, %) | Full day: 28 / 42 = 40% / 60% (8 + 11 + 9 = 28; 33 + 9 = 42). Half day: 32 / 48 = 40% / 60% (9 + 12 + 11 = 32; 38 + 10 = 48). Inside the 40/60 rule (plus or minus 5 points) |
| Planted error and warning level | Capacity counted twice. The shared Firmware team is planned at 100 percent in P-01 Probe X cellular and 100 percent in P-02 Hub firmware (Q3). Each per-program check passes. The sum by team is 200 percent (24 FTE against 12). Warning: told ("This batch has one planted AI error. Find it in your audit.") |
| Learner evidence | Tuned brief (v1 to v2 with the shared-team total check). Flag report decisions for Q3. Audit findings for 2 shared teams and 3 linked items. Fund, pause or stop calls with reasons, and a note on whether the work or the strategy needs to change. All on `lab-1-record-sheet.md` |
| Agent after this module (files) | Instructions: brief v2. Knowledge: `job-card-portfolio-pack`, `strategy-okrs-kpis`, `capacity-sheet` (4 files, counting the instructions, as spec `course_agent.growth`). Catch-up: `kit/kit-m2/` |

### Slide minutes check

| Arc step | Slides | Full day | Half day | Mode |
| --- | --- | --- | --- | --- |
| Why this matters, workflow and bottleneck | 1.1 to 1.4 | 1 + 3 + 2 + 2 = 8 | 1 + 3 + 2 + 3 = 9 | Instructor-led |
| Live demo | 1.5, 1.6 | 8 + 3 = 11 | 9 + 3 = 12 | Instructor-led |
| Build pattern and lab brief | 1.7 to 1.10 | 2 + 3 + 1 + 3 = 9 | 2 + 4 + 2 + 3 = 11 | Instructor-led |
| Lab 1 | 1.11 | 33 | 38 | Hands-on |
| Debrief | 1.12 to 1.16 | 2 + 3 + 2 + 1 + 1 = 9 | 2 + 3 + 3 + 1 + 1 = 10 | Hands-on |
| Total | 16 slides | 70 | 80 | 28 + 42; 32 + 48 |

Debrief split against the spec arc: reveal 2 (1.12), check sample 3 (1.13), fund, pause or stop 2 (1.14), Monday 1 (1.15), log save card 1 (1.16). Half day: the spec gives the extra time to the fast-start card (lab, +5) and the fund, pause or stop discussion (1.14, 3 minutes). To fit the arc minutes (9, 12, 11), this draft also gives 1 extra minute each to the hardware and internal note (1.4), the demo (1.5), the hand-off rule (1.8) and the data check (1.9).

### Builder decisions inside the spec

| # | Decision | Why |
| --- | --- | --- |
| B1 | The new check goes under "My rules" at the end of the core brief (Instructions), not into the job card file | Editing the Instructions is one action on all 4 platforms. Editing a knowledge file needs a re-upload (Gemini: the whole skill). Same pattern Dan approved in Market Research |
| B2 | Card steps 2 and 6 run in a new chat | A new chat is the only way to be sure the tuned brief applies on all 4 platforms (Market Research Gate 3 D1). Q4 does not need the Q3 run, so nothing is lost |
| B3 | Copilot card step 2 and step 6 also send `capacity-sheet.xlsx` in chat | Spec `platform_cards.copilot` and decision f3: code interpreter reads files uploaded in chat (mb-13). Reading knowledge files with code interpreter is not documented |
| B4 | The optional story slot sits in the debrief (slide 1.14), not in "why this matters" | The spec story topic (two programs counting on one scarce team) is the planted error. Told before the lab, it gives the answer away. See question 5 |
| B5 | The demo runs Q3 on brief v1 and shows the pack before the audit. The talk track does not comment on capacity | The demo shows what learners get. The saved demo output is the debrief fallback if no platform in the room makes the error |
| B6 | The audit hint on the record sheet: "Pick 2 teams that work on more than one program" | The spec audit is "2 shared teams". The line defines a shared team. It does not name the Firmware team. Lab 1 only (warning: told) |
| B7 | The build check uploads `capacity-sheet.xlsx` (course open) | It tests the `.xlsx` upload that the lab needs. A Claude learner with code execution off, or a Copilot learner with no license, finds out in the open, not in the lab |

### Questions for Dan

Most important first. Each has a recommended answer.

| # | Question | Options | Recommended |
| --- | --- | --- | --- |
| 1 | **W1, W3 and N21 (OI-10 is open).** No W1 or W3 figure is on a slide. Slide 1.2 states the bottleneck in words. The talk track uses one figure: N21, "72.2% spend 25% or less of their time on product strategy" (fieldwork Q4 2025, nearly 250 product professionals, sponsored by ProductPlan). N21 is "verified" in `rerun-track-3.md`, and the spec `talk_track_slots` names it. W1 is told in words only (vendor reports its own study; W2 not opened) | A: keep N21 in the talk track only, with "fieldwork Q4 2025". B: drop N21 until OI-10 closes | A |
| 2 | **Trendslop numbers.** The open uses no number from the article. Fortune (S-T3, independent) reports the model count, but it repeats the HBR study, so it counts as the same source. The open says "leading AI models" and "many company scenarios" | A: words only until someone reads the licensed HBR copy (OI-10). B: allow the model count from Fortune now | A |
| 3 | **OI-08 platform proof is open.** The spec says the proof runs before modules are built. Status says Dan started Stage 3 first. This card test can double as proof P1 (`card-test.md` has the P1 checks). Differences from the P1 draft in `outline/proof-kit-drafts.md`: (a) the brief has a "My rules" section for the new check (B1); (b) the brief adds "How you work", the [EDIT] line, a "Numbers" rule and a file-or-tables "Output" rule; (c) the job card adds the plan quarter, a step that writes asks into the capacity sheet, and a capacity table in the output; (d) steps 2 and 6 run in a new chat (B2); (e) Copilot uploads the sheet in chat each run (B3); (f) "Run Q3 after reopen" is a proof step, not a learner step | A: the card test doubles as P1 with these differences. B: run P1 from the draft first, then the card test | A |
| 4 | **ChatGPT check sample outside the project (decision f5).** Outside the project the agent has no brief. The card tells the learner to paste brief v2 and attach the job card, the strategy file and the check sample in one message. This may not fit in 3 minutes | A: keep, and record the time in the card test. B: for module 1 only, run it in a new chat inside the project (the check sample is a different quarter, so a memory leak cannot give the answer) | A, then B if the card test shows more than 4 minutes |
| 5 | **Story slot (slide 1.14).** No story is written, to avoid an invented client story (decision 43). The spec topic is placed after the reveal (B4) | A: you supply one real client or Pragmatic story. B: leave it optional with the skip path | A if you have one, else B |
| 6 | **Lab brief slide (1.10) is the short version** (your rule: goal, key actions, pass check, then the workbook). The full data safety text is not on 1.10. It is on O.8, on 1.9 (data check card) and on every step card. 1.10 has the planted error line and "Data check card first" | A: accept. B: add the full standard text to 1.10 (spec `placement` lists the lab brief slide) | A |
| 7 | **Screen names from another course's matrix.** This course's matrix has no screen name rows. The cards use rows cl-ui-09, cl-ui-10, cg-ui-09, mb-ui-12, mb-ui-13 and gm-ui-10 from `courses/market-research/research/platform-matrix.yaml` (checked 2026-11-26), plus cl-cl-03, cg-14 and mb-04 from this course's matrix. The verifier list is below | A: the verifier rechecks them and appends them to this course's matrix. B: new vendor research first | A |
| 8 | **Gemini log save.** Spec `log_save_card` says re-upload the whole skill (gm-01). The card gives **More**, then **Replace file** first, and the whole-skill upload as the backup (your Market Research Gate 3 D4) | A: keep both on the card. The card test records which works. B: whole-skill upload only | A |
| 9 | **Gemini and `.xlsx` in a skill.** gm-01 lists legacy `.xls` as not supported and does not name `.xlsx`. The build check and the lab add `capacity-sheet.xlsx` to the skill | A: keep; the card test confirms; the CSV copy is the backup. B: Gemini uses the CSV copy from the start | A |
| 10 | **Google Sheet template does not exist yet.** Every card offers the Google Sheet option. Someone must make the Google Sheet template of the capacity sheet and its share link | A: Stage 4 (workbook renderer) or you make it before the card test. B: drop the option from module 1 cards | A |
| 11 | **kit-m2 contents.** (a) `job-card-requests` belongs to the module 2 builder; kit-m2 lists it as "added by the module 2 builder". (b) `kit-m2/capacity-sheet.xlsx` holds Quarter "Q1 2028" and each team ask from `m1-submissions-q4.md`. It is a filled copy of the course sheet, not a change to `case/`. Module 4 reads it as the capacity table | A: accept both. B: the case builder adds a filled capacity sheet to `case/` | A |
| 12 | **Data safety text has sentences over 20 words** (the second and third sentences). Every card carries it word for word | A: keep it word for word as the standard text (same as Market Research D15). B: ask the planner to shorten it in the spec | A |
| 13 | **Check sample quarter.** `m1-check-sample.md` is plan quarter Q2 2027 (submitted March 2027), earlier than the Q3 and Q4 runs. The cards call it "a second quarter". No case change needed | A: accept. B: case builder retitles it "earlier quarter" | A |
| 14 | **Half-day minutes.** The arc minutes need 1 extra minute on slides 1.4, 1.5, 1.8 and 1.9 that the spec note does not name | A: accept | A |

Information only: OI-09 (workshop overlap for capability 2) is still open and touches this module. OI-14 (names) is open. Neither blocks the draft.

### Screen names for the verifier

| Platform | Name on the card | Source row (doc, date) | Status |
| --- | --- | --- | --- |
| Claude | **Projects**, **+ New Project**, **Set project instructions**, **Save instructions**, **+** in project knowledge | cl-ui-09 (Claude Help Center 9519177, 2026-11-06, checked 2026-11-26), Market Research matrix | Verified there. Append here |
| Claude | **Settings**, **Capabilities**, **Code execution and file creation** (also **Create and edit files**); **Organization settings**, **Capabilities** | cl-ui-10 (Help Center 12111783, 2026-11-24, checked 2026-11-26), Market Research matrix | Verified there. Append here |
| Claude | **Customize**, **Skills** (stretch) | cl-cl-03, this matrix (approx 2026-10-28, checked 2026-11-20) | Verified |
| Claude | Delete a file from project knowledge (log save card) | None. Written in plain words | Not in any doc |
| ChatGPT | **New project**, **•••**, **Project settings**, project sources list | cg-ui-09 (Help 10169521, approx 2026-11-23, checked 2026-11-26), Market Research matrix | Verified there. Append here |
| ChatGPT | Project memory "default" and "project-only" | cg-14, this matrix. Modes named, no control label | Plain words. Check the label |
| ChatGPT | ChatGPT Work (how to start it in a project) | cg-09, cg-10. No control label | Plain words. Check |
| ChatGPT | Add files to a project, start a new chat in a project | None | Plain words |
| Copilot | **New agent**, **Skip to configure**, **Configure**, **Name**, **Instructions**, **Knowledge**, **Upload**, **X** then **Remove** | mb-ui-12 (Learn add-knowledge, 2026-11-16, checked 2026-11-26), Market Research matrix | Verified there. Append here |
| Copilot | **All agents**, **...**, **Edit**, **Create**, **Update** | mb-ui-13 (Learn share-manage, 2026-11-16, checked 2026-11-26), Market Research matrix | Verified there. Append here |
| Copilot | **Create documents, charts, and code** toggle | mb-04, this matrix (2026-11-16) | Verified. mb-11 says always on in Agent Builder (conflict) |
| Copilot | Upload a file in the agent chat | mb-ui-14 (Copilot Chat only, partly verified) | Plain words. Check in the agent chat |
| Gemini | **Customize**, **Skills**, **Create**, **Create manually**, **Add**, **files**, **Upload**, **Save**, **/**, **More**, **Replace file** | gm-ui-10 (Gemini Apps Help skills page, no date, checked 2026-11-26), Market Research matrix. **/** dated by blog.google 2026-09-30 | Undated page. Dan accepted it with a check date in Market Research (D3) |
| Gemini | The skill instructions field | None ("No exact Instructions label shown", gm-ui-10) | Plain words |

## 2. Slides and talk track

### Slide 1.1: Module 1. The quarterly portfolio pack
- Layout: Chapter Break
- Minutes: 1 (half day 1)
- On-slide text: MODULE 1. The quarterly portfolio pack: is the work consistent with the strategy? Promise: "Hand the pack to an agent that totals, links and flags. Manage it by its checks and flags." Bullets: Build the Strategy Evidence Agent from a template. Decide each flag and audit capacity and links. Add a check, rerun, and make the fund, pause or stop calls.
- Visual intent: Teal side band, "MODULE 1" tag. Small rung icon: rung 1 of the ladder lit. Small tag: "Focus / Product Portfolio".
- Sources: none

Notes:
```
POINT: In this module you build the Strategy Evidence Agent and give it its first job, the quarterly portfolio pack.
Talk Track:
You checked in the opening that your platform works.
Now you build the agent you keep all day.
Its first job is the quarterly portfolio pack.
The portfolio pack is the set of tables a leadership team reads at the quarterly review. Every program: its status, what it asks for, which teams it needs, and which objective it serves.
You will not build the pack yourself.
You write the brief, read the flags, audit a sample and make the calls.
TRANSITION: First, why this workflow, and what slows it down.
```

### Slide 1.2: The pack is stale before the meeting
- Layout: Blank
- Minutes: 3 (half day 3)
- On-slide text: Headline: "The pack is stale before the meeting." Line 1: "One person stitches team updates by hand." Line 2: "The review turns into reconciling numbers, not deciding." Line 3: "Leaders say the strategy is clear. Few can show the work links to it." Workflow strip: "Team submissions, status export, capacity, then a checked pack."
- Visual intent: Headline with "stale" in orange. Three short lines, no figures. A left-to-right strip: three input icons (submissions, tracker, capacity sheet), then one pack icon with a check mark.
- Sources: W22 (claim, verified, vendor). W1 (statistic, vendor; words only on the slide and in the talk track until W2 is opened, OI-10). W3 (strategy link gap, words only). N21 (statistic, verified, fieldwork Q4 2025; talk track only)

Notes:
```
POINT: The quarterly pack takes days of manual stitching, so the review spends its time reconciling numbers instead of making decisions.
Talk Track:
Here is the workflow for this module.
Before each quarterly review, every program sends its plan for next quarter.
Status. Ask. Which teams it needs. Which objective it serves.
Someone has to stitch that into one pack.
That person chases updates, copies numbers and checks the status against the tracker.
By the meeting, some of it is already out of date.
So the first half of the review is "whose number is right?" Not "what do we fund?"
Product portfolio software vendors describe this pattern. One of them calls that person the human integration layer.
Leaders also say their strategy is clear. But when you ask them to show which work links to which objective, few can.
[POINT TO LINE 3]
And PMs have little time for strategy work to begin with.
In the State of Product Management 2026 report, fieldwork in Q4 2025, 72.2% of nearly 250 product professionals said they spend 25% or less of their time on product strategy. A tool vendor sponsored that survey.
So the question is not "can AI build the pack?" It can.
It is "can you trust the pack enough to decide from it?"
[IF ASKED FOR MORE FIGURES:] There are vendor surveys on this. We do not put their figures on slides until we have read the primary report.
TRANSITION: Trust starts with what the agent does, and what it never does.
```

### Slide 1.3: Strategy stays a forced choice. Yours
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: Headline: "Strategy stays a forced choice. Yours." Left, "You give the agent": your strategy overview, your OKRs, your KPIs. Middle, "The agent shows": where money and teams go, by objective. Work with no clear link, listed, not judged. Right, "You decide": fund, pause or stop. Change the work, or change the strategy.
- Visual intent: Three columns with arrows left to right. "Yours" in orange in the headline. The middle column titled "Strategy consistency check" in small gray type.
- Sources: none (spec `capability_mapping` module 1: 2.1 AI text "Strategy stays a forced-choice human decision"; 2.1B workbook text; glossary "strategy consistency check")

Notes:
```
POINT: The agent compares the stated strategy with where the plan puts money and teams, and the PM makes the forced choice.
Talk Track:
Three terms, so we all mean the same thing.
A strategy overview: where you play, how you win, and what you will not do.
OKRs: objectives and key results. An objective is what you want. A key result is how you measure it, with a baseline and a target.
KPIs: the business metrics you track all the time. Attach rate, margin, install days.
You give the agent all three. You bring the strategy. This course does not teach you to write one.
[POINT TO THE MIDDLE]
The agent runs what we call a strategy consistency check.
It shows where the plan's money and teams go, by objective.
And it lists work with no clear link to any objective.
It lists it. It does not judge it. Maybe that work is a good bet the strategy forgot. Maybe it is a pet project. That is your call.
Pragmatic's Capability Standards put it this way: compare what leaders say they prioritize with where resources really go. And they say strategy stays a forced-choice human decision.
[POINT TO THE RIGHT]
So you decide: fund, pause or stop. And one more call that people forget. When work and strategy disagree, do you change the work, or change the strategy?
TRANSITION: In hardware and internal platforms, the plan has one more trap.
```

### Slide 1.4: Plans that touch each other
- Layout: Blank
- Minutes: 2 (half day 3)
- On-slide text: Headline: "Plans that touch each other." Line 1: "Hardware programs share firmware teams, test labs and suppliers." Line 2: "A delay in one program spreads to others." Line 3: "Internal platforms serve many teams at once." Case strip: "Larkspan Systems: 5 programs, 5 teams, 1 internal platform (Fleet Data Platform)."
- Visual intent: Five program boxes in a row, with lines from several boxes into shared team boxes below. Do not highlight any one team. Case strip in teal at the bottom.
- Sources: W19 (claim, verified, consultancy), W22 (claim, verified, vendor). Case `company.md`

Notes:
```
POINT: In hardware and internal platform work, programs share teams and suppliers, so one program's plan affects the others.
Talk Track:
Two kinds of product work make the pack harder.
Hardware. Programs share firmware engineers, test labs and suppliers.
Hardware runs on stage gates of months. Software ships in weeks. That gap hides dependencies.
When one program slips, the shared team slips for everyone.
Internal platforms. An internal platform team serves Support, Install, Finance and more, all at once.
[POINT TO THE CASE STRIP]
Our case company is Larkspan Systems. It is fictional. It makes wireless temperature sensors and the cloud software that watches them.
It has five programs in the pack. Probe X cellular, a new sensor with its own cellular radio. Hub firmware. Cloud compliance reports. Tag 2, a shipment logger. And the Fleet Data Platform, an internal platform with an internal PM.
Five teams do the work. Some work on more than one program.
The case is set in late November 2027. They are planning 2028.
[HALF DAY: ASK: "Which teams in your company work on more than one program?" TAKE 2 ANSWERS]
TRANSITION: Let me build the agent in front of you.
```

### Slide 1.5: Live demo. Build the Strategy Evidence Agent from the template
- Layout: 1_prompt
- Minutes: 8 (half day 9)
- On-slide text: LIVE DEMO. "Build the Strategy Evidence Agent from the template." Running example: Larkspan Systems, Q3 team submissions (5 programs). 8 MIN (half day: 9 MIN).
- Visual intent: Orange "LIVE DEMO" tag. Platform logo for the demo platform (Claude). Small list of the 4 kit files: brief, job card, strategy file, capacity sheet.
- Sources: cl-pj-01, cl-fo-06 (platform matrix, verified). Demo script in section 3

Notes:
```
POINT: Building the agent from the template takes a few minutes, and the first run gives you a pack, a strategy consistency section and a flag report to manage.
Talk Track:
[SWITCH TO THE DEMO PLATFORM. FOLLOW THE DEMO SCRIPT IN SECTION 3, STEPS 1 TO 5]
I demo on Claude. Your step card has the same steps for your platform.
Here is the kit. Four files.
The brief goes into the instructions. It holds the rules for every job the agent will ever run.
Look at the core rule. Never set, propose, rank or rewrite strategy. Never recommend funding.
Look at the bottom. "My rules. None yet." You fill that after your audit.
[PASTE THE BRIEF. SAVE]
The job card goes into knowledge. It holds this job's steps, its quality checks and its hand-off rules.
The strategy file goes in too. Larkspan's 2028 strategy, OKRs and KPIs.
The capacity sheet is already there from the build check. It has formulas. The agent writes the asks in, and the sheet does the math.
[ADD THE 2 FILES]
If you have built prompts with a job, context, rules and an output, the brief will look familiar. What is new: quality checks, hand-off rules and a decision field the agent never fills.
Now the run. New chat. The Q3 submissions and the status export, and one prompt: "Run the portfolio pack job".
[SEND. WHILE IT RUNS:]
Notice what I did not do. I did not write a prompt per step. I did not paste the strategy into the chat.
The brief and the job card hold all of that. That is what makes it an agent, not a prompt.
[WHEN THE RUN ENDS, OPEN THE OUTPUT]
TRANSITION: Now the part that matters: how you read what it gives you.
```

### Slide 1.6: Read the consistency section, then the flags
- Layout: Blank
- Minutes: 3 (half day 3)
- On-slide text: 1. Pack table: status, ask and link for each program. 2. Strategy consistency section, Q3 asks by objective: O1 USD 910 thousand. O2 USD 3,000 thousand. O3 USD 0. No link USD 640 thousand. 3. Flag report: P-03 status differs from the tracker. P-04 states no link. "PM decides."
- Visual intent: A cropped, readable mock of the demo output: four objective bars (O3 empty, "No link" in gray), then two flag rows with a blank "PM decides" column. Numbers 1 to 3 in orange circles. No capacity table on this slide.
- Sources: none (case data, `case/expected-results.md`, lab 1, Q3 run; not a statistic)

Notes:
```
POINT: You manage the agent by reading the consistency section and the flag report, not by rebuilding the pack.
Talk Track:
[DEMO SCRIPT STEPS 6 TO 8. STAY ON THE SCREEN, THEN SHOW THIS SLIDE AS THE SUMMARY]
Part one, the pack table. One row per program. Status, ask, link.
Part two, the strategy consistency section. Where the Q3 asks go, by objective.
O2, put each site into service faster and at lower cost: 3 million dollars across three programs.
O1, win Pharmacy and lab: 910 thousand.
O3, grow recurring Cloud revenue: zero. No program states a link to it.
And 640 thousand with no stated link at all. That is Tag 2.
Is zero on O3 a problem? Is Tag 2 a problem? The agent does not say. Good. That is your call.
Part three, the flag report. Two items.
P-03, Cloud compliance reports. The team says "On track". The program tracker says "At risk".
P-04, Tag 2. No link to an objective. The reason given: Sales asked for it.
Each line ends with "PM decides". No recommended action.
[DO NOT COMMENT ON THE CAPACITY TABLE. IF A LEARNER ASKS ABOUT CAPACITY:] Good question. Hold it for your audit.
I am not auditing this run now. That is your job in the lab.
[SAVE THE DEMO OUTPUT. YOU MAY NEED IT IN THE DEBRIEF]
TRANSITION: Before you build, here is the turn of the loop you run in the lab.
```

### Slide 1.7: One turn of the loop in lab 1
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: Headline: "One turn of the loop in lab 1." Track: Brief, checks and hand-off rules (from the template). Run Q3 (step 2). Decide each flag (step 3). Audit 2 shared teams and 3 links (step 4). Add one check (step 5). Run Q4 (step 6). Make the call and record why (debrief).
- Visual intent: A straight track from left to right, not a circle. Lab step numbers 1 to 6 under the track. "Audit" and "Add one check" in orange. A return arrow from the end back to "Brief" labeled "every quarter".
- Sources: none (spec `course_agent.manager_loop`)

Notes:
```
POINT: In lab 1 you go once round the agent manager's loop, and the audit is the step that makes the loop work.
Talk Track:
This is the loop you run all day. Today you go round it once.
The template gives you the brief, the checks and the hand-off rules.
You run Q3. You decide each flag.
Then you audit. You pick 2 teams that work on more than one program, and 3 linked items, and you check them against the source files.
Then you add one check to the brief, for what your audit found.
You run the next quarter, Q4, in a new chat.
And in the debrief you make the calls, and write down why.
A check tests what you thought of in advance.
An audit finds what you did not think of.
That is why the loop has both.
[POINT TO THE RETURN ARROW]
On your own work, you run this every quarter. Each audit makes the brief a little better.
TRANSITION: One part of the brief matters more than the rest: where the agent stops.
```

### Slide 1.8: The hand-off rule stops before the call
- Layout: Blank
- Minutes: 3 (half day 4)
- On-slide text: Headline: "The hand-off rule stops before the call." Three rules from the template: 1. A status that differs from the source system: flag it. 2. Work with no clear link to a stated objective: list it. Do not judge it. 3. Any step that would recommend funding, ranking or a strategy change: stop. Hand it to the PM. Bottom line: "You set the rules in the brief."
- Visual intent: A vertical stop line down the middle. Left side "Agent: evidence" in gray. Right side "PM: the call" in teal. Rule 3 sits on the line with a stop icon. Bottom line in orange.
- Sources: none (spec `modules.m1.lab.template_contents.handoff_rules`, `course_agent.core_rule`). New slide (house rule 14)

Notes:
```
POINT: The template's hand-off rules send status gaps and unlinked work to the PM, and stop the agent before any funding, ranking or strategy step.
Talk Track:
A hand-off rule says when the agent stops and gives an item to you.
Here are the three in the template.
One. A status that differs between the team's submission and the source system. The agent flags it. It does not decide who is right.
Two. Work with no clear link to a stated objective. The agent lists it. It does not judge it.
Three. The one that matters most. Any step that would recommend funding, ranking or a strategy change. The agent stops and hands it to you.
Remember trendslop. A model will happily tell you what to fund. Its answer will sound tailored. This rule keeps that answer out of your pack.
What the agent hands you goes into the flag report. One line per flag: the type, the record, what it found, the evidence with a source and a date, and "PM decides".
The decision field stays blank. Only you fill it.
[POINT TO THE BOTTOM LINE]
You set the rules in the brief. Every range, every threshold, every limit is your choice.
The Larkspan files show one PM's choices. They are choices, not standards. On your own plan, write your own.
If you have taken an agent course, you have seen boundaries and guardrails. A hand-off rule is the same idea, written for one job, and checked on every run.
[HALF DAY: ASK: "Which call from your last portfolio review should never go to an agent?" TAKE 2 ANSWERS]
TRANSITION: One last thing before you upload a plan.
```

### Slide 1.9: Data check before you upload a plan
- Layout: Blank
- Minutes: 1 (half day 2)
- On-slide text: Headline: "Data check before you upload a plan." Data check card: 1. Is this tool approved by my company for this data? 2. Does my file hold client data, health data, personal data, unreleased roadmap or release dates, forecasts, pricing, supplier terms or non-public financials? 3. If 2 is yes and 1 is no, use the Larkspan case or remove names and numbers first. Line under it: "Plans hold spend, headcount and unreleased dates. Your pack and sheet keep them."
- Visual intent: The data check card from the step cards, enlarged. Second line in teal. A small icon of a plan document with "spend", "headcount" and "dates" tags.
- Sources: none (spec `data_safety_note.data_check_card`, `modules.m1.lab.data_safety`)

Notes:
```
POINT: A portfolio plan holds spend, headcount and unreleased dates, so each learner runs the data check card before step 1 and chooses own work or the case.
Talk Track:
You saw the data safety rule in the opening. Here is how you apply it in this lab.
The data check card sits above step 1 on your card. Two minutes.
A team plan holds spend, headcount and dates that are not public.
So answer the three questions for your own file.
If your tool is not approved for it, remove names and spend, or use the Larkspan case. Both paths use the same steps.
Write your choice on your record sheet.
One thing is new with an agent. Your capacity sheet stays in the agent after the lab. At the end, you decide what it keeps.
[HALF DAY: ASK ONE LEARNER WHAT THEIR COMPANY ALLOWS IN THEIR TOOL]
TRANSITION: Here is your lab.
```

### Slide 1.10: Lab 1 brief
- Layout: Activity
- Minutes: 3 (half day 3)
- On-slide text: ACTIVITY. Lab 1: The quarterly portfolio pack. Goal: Hand the pack to an agent that totals, links and flags. Manage it by its checks and flags. Key actions: Data check card first. 1. Add the kit. 2. Run Q3. 3. Decide each flag. 4. Audit 2 shared teams and 3 links. 5. Add one check. 6. Run Q4 in a new chat. Pass check: Q4 pack with status, capacity and links. Every flag has your decision. Audit recorded, one check added. No funding or strategy line from the agent. Orange box: "This batch has one planted AI error. Find it in your audit." Footer: "Full steps: your step card in the workbook."
- Visual intent: Orange "ACTIVITY" band. Goal at the top. Key actions numbered on the left. Pass check on the right. Planted error line in an orange box at the bottom. Workbook pointer small, bottom right.
- Sources: none

Notes:
```
POINT: In lab 1 you build the agent, run two quarters, audit the pack and add one check.
Talk Track:
The goal of this activity is to hand the quarterly pack to an agent and manage it by its checks and flags.
The core message: the meeting is for decisions, not reconciliation. The agent reconciles and shows the evidence. You make the strategy and funding calls.
Your step card has the full steps for your platform. Here is the short version.
[WALK THE 6 KEY ACTIONS IN ONE LINE EACH]
Start with the data check card. Then add the kit. Run Q3. Decide each flag. Audit. Add one check. Run Q4 in a new chat.
On your own work: your team plan submissions, a status export and capacity by team for one quarter. Remove names and spend if your tool is not approved.
Otherwise use the Larkspan files. Both paths use the same steps.
Record your decisions and audit findings on the lab 1 record sheet in your kit. That is your evidence for this lab.
[POINT TO THE ORANGE BOX]
This batch has one planted AI error. Find it in your audit.
The agent's own checks will not find it for you.
Breakout rooms are by platform. Build and save your own agent. Share your screen only when someone is stuck.
New to your platform's builder? Start with the fast-start card for your platform.
Done early? The stretch steps are at the end of your card.
TRANSITION: [OPEN BREAKOUT ROOMS BY PLATFORM. START THE TIMER: 33 MINUTES, HALF DAY 38]
```

### Slide 1.11: Lab 1: The quarterly portfolio pack
- Layout: Activity
- Minutes: 33 (half day 38)
- On-slide text: ACTIVITY. 33 MIN (half day 38 MIN). Time guide, full day: 0 to 2: data check card. 2 to 6: add the kit (fast-start card if new). 6 to 10: Q3 run. 10 to 16: decide each flag. 16 to 24: audit. 24 to 28: add your check. 28 to 33: Q4 run, new chat. Half day: 0 to 2 data check. 2 to 8 kit. 8 to 12 Q3 run. 12 to 18 flags. 18 to 27 audit. 27 to 31 your check. 31 to 38 Q4 run. "Build and save your own agent. Share your screen only when someone is stuck."
- Visual intent: Orange band. A simple timeline bar with the 7 blocks. Rooms by platform shown as 4 small tiles.
- Sources: none (spec `gate_2_designs.decision_e.minute_by_minute_lab_1`)

Notes:
```
POINT: Learners build and run the agent from their step card, on their own work or the case data.
Talk Track:
The goal of this activity is to run one full turn of the manager loop on your own agent.
[VISIT EACH ROOM IN TURN. START WITH COPILOT, THEN GEMINI, THEN CHATGPT, THEN CLAUDE]
[CUES: FULL DAY MINUTE, HALF DAY MINUTE IN BRACKETS]
[AT MINUTE 2 (2): "Data check done? Write your choice on the record sheet and start step 1."]
[AT MINUTE 6 (8): ANYONE WHO HAS NOT SENT THE Q3 FILES GETS HELP FIRST]
[AT MINUTE 10 (12): "If your run is not done, open the Q3 submissions and read the team asks while you wait."]
[AT MINUTE 16 (18): "Start your audit now. Open the source files. Do not trust the pack; check it."]
[AT MINUTE 24 (27): "Write your check now, even if your audit is not done."]
[AT MINUTE 28 (31): "Send the Q4 files now, in a new chat."]
[AT MINUTE 30 (35): "Not sent step 6 yet? Skip it. Run it after class." THE DEBRIEF WORKS FROM THE Q3 RUN]
[COMMON FAILURES AND RECOVERY: SEE SECTION 9]
[DO NOT REVEAL THE ERROR. IF A LEARNER ASKS "IS THIS IT?", ASK: "What does the source file say when you add it up yourself?"]
TRANSITION: [CLOSE ROOMS AT MINUTE 33, HALF DAY 38] Bring your record sheet. Let's see what you found.
```

### Slide 1.12: What did your audit find?
- Layout: debrief
- Minutes: 2 (half day 2)
- On-slide text: DEBRIEF. Which 2 teams did you total? What did the pack say about their capacity? Which check or audit found the error? (Reveal after answers:) Firmware team, Q3: P-01 100 + P-02 100 = 200 percent. 24 FTE asked, 12 available. Every per-program check passed.
- Visual intent: Navy "DEBRIEF" band. 3 questions. The reveal appears on click: two bars at 100 each, stacked into one bar at 200 against a line at 100. "Every per-program check passed" in orange.
- Sources: none (case `planted-errors.md` lab 1, `expected-results.md` lab 1)

Notes:
```
POINT: The shared Firmware team was planned at 100 percent in two programs, so every per-program check passed while the team total was 200 percent.
Talk Track:
[ASK THE 3 QUESTIONS. TAKE 2 OR 3 ANSWERS, ONE FROM EACH PLATFORM IF YOU CAN]
[REVEAL]
Here is the planted error.
In Q3, P-01 Probe X cellular asks the Firmware team for 100 percent.
P-02 Hub firmware asks the same team for 100 percent.
The Firmware team has 12 people. Together the two programs ask for 24.
On the template brief, the agent checks capacity per program. Each ask is 100 percent or less. Every row says "inside". The capacity sheet says the same, because it checks each row alone.
So the pack says capacity is fine.
[PAUSE]
Every check passed. And the team is booked twice over.
The other shared teams are fine. Cloud team, Hardware design team, Test lab: 90 percent each.
That is why you audit. Your check tested what the template predicted. Your audit added it up by team.
[IF NO PLATFORM IN THE ROOM MADE THE ERROR, SHOW THE SAVED DEMO OUTPUT]
[IF A LEARNER'S AGENT TOTALED THE TEAMS ON ITS OWN: "Good. Did it flag the 200 percent, or only show it? A number in a table is not a flag."]
TRANSITION: Did your new check fix it? Let's test it on a quarter you have not seen.
```

### Slide 1.13: Check sample
- Layout: Activity
- Minutes: 3 (half day 3)
- On-slide text: ACTIVITY. 3 MIN. New chat on your tuned agent. Send `m1-check-sample.md` with "Run the portfolio pack job". ChatGPT: a new chat outside the project (your card says how). Compare with the pass condition at the end of your step card.
- Visual intent: Orange band, timer 3 MIN. One-line instruction. Small image of the card's pass condition box.
- Sources: none (case `m1-check-sample.md`, `expected-results.md` lab 1 check sample)

Notes:
```
POINT: A second quarter the learner has not seen shows if the tuned brief works.
Talk Track:
The goal of this activity is to test your tuned brief on new data.
New chat. Send the check sample. Same prompt.
It is a different quarter, with four programs. Then compare with the pass condition on your card.
ChatGPT: run it in a new chat outside your project, so the project memory does not help. Paste your tuned brief and attach the three files your card names.
[START A 3-MINUTE TIMER]
[AFTER 3 MINUTES, ASK: "Hands up if your agent passed." THEN: "What did it flag?"]
[EXPECTED: the Test lab at 130 percent, P-01 70 plus P-04 60. 7.8 FTE asked, 6 available. No other team over]
[IF THE AGENT FLAGS NO TEAM: "Read your check. Does it say total each shared team across all programs?"]
[IF THE AGENT WRITES "pause P-04" OR ANY FUNDING LINE: "That breaks the core rule. It is an audit finding. Add it to your record sheet."]
TRANSITION: So the agent found the gap. Who decides what to do about it?
```

### Slide 1.14: Fund, pause or stop. Change the work or the strategy
- Layout: debrief
- Minutes: 2 (half day 3)
- On-slide text: DEBRIEF. The Q4 flags are yours: Firmware team at 150 percent (P-01 90 + P-02 60). P-02 status differs from the tracker. P-04 link names only "O2". Your calls: fund, pause or stop? Where does the Firmware team go next quarter? Does the work need to change, or the strategy?
- Visual intent: Navy band. Three flag cards across the top with blank "PM decides" fields. Two large questions under them. No agent icon on this slide.
- Sources: none (case `expected-results.md` lab 1, Q4 run and the case PM's example decisions)

Notes:
```
POINT: The agent reports the over-capacity team and the unlinked work, and only the PM decides fund, pause or stop, and whether to change the work or the strategy.
Talk Track:
Here is the Q4 flag report on the tuned brief. Three flags.
The Firmware team at 150 percent. P-01 asks 90, P-02 asks 60. 18 people asked, 12 available.
P-02 Hub firmware: the team says "On track", the tracker says "At risk".
P-04 Tag 2: the link says only "O2". It does not say what the work does.
And one thing that is not a flag. The Test lab is at exactly 100 percent. Under the Larkspan PM's rule, that is not over.
Take one minute. On your record sheet, write your calls. Fund, pause or stop. And where the Firmware team goes.
[1 MINUTE. HALF DAY: 2 MINUTES, THEN TAKE 2 ANSWERS]
Here is what one Larkspan PM decided. A choice, not an answer.
Keep P-02 at 60 percent. Ask the Head of Product to choose the P-01 level.
Pause Tag 2 until it states a link to a key result.
And the strategy question. O3, grow recurring Cloud revenue, has no program with a stated link. This PM decided the work does not change the strategy, and noted O3 for the next review.
Your calls can differ. What matters: the agent made none of them, and you can defend yours with the evidence.
[OPTIONAL STORY SLOT, 30 SECONDS, 1 MINUTE IN THE HALF DAY. Topic: a leadership team that found two programs counting on the same scarce team. Use only a story you heard from a client team or from Pragmatic's work with companies. Tell it as their story, never as your own. If you have no such story, skip this slot.]
TRANSITION: So what do you do on Monday?
```

### Slide 1.15: What you do Monday
- Layout: Blank
- Minutes: 1 (half day 1)
- On-slide text: "Take last quarter's plan. Total each shared team across all programs before the next review."
- Visual intent: One line, large type. Calendar icon with "Monday".
- Sources: none (spec `talk_track_slots.monday_close`)

Notes:
```
POINT: The first real use of this job is on last quarter's plan, with every shared team totaled across programs before the next review.
Talk Track:
On Monday, find last quarter's plan.
Total each shared team across all programs. With the agent, or by hand.
Do it before your next review, not in it.
Your kit has the template and the record sheet, so you can do this without the class.
TRANSITION: Last step: decide what your agent keeps.
```

### Slide 1.16: Save your log
- Layout: Activity
- Minutes: 1 (half day 1)
- On-slide text: ACTIVITY. 1 MIN. 1. Decide what the log keeps and delete the rest. 2. Replace the old capacity sheet in your agent's knowledge with the one from your Q4 run. Your card has the steps for your platform.
- Visual intent: Orange band. Two numbered steps, large. Small platform row: Claude, ChatGPT, Copilot, Gemini.
- Sources: cl-pj-01, cg-01, mb-02, gm-01 (platform matrix); vendor docs on the cards. Spec `course_agent.log_save_card`

Notes:
```
POINT: The capacity sheet from the Q4 run is the log that later jobs read, so the learner decides what it keeps and saves it in the agent.
Talk Track:
The goal of this activity is to save the capacity table that module 4 will read.
First, decide what it keeps. Totals and allocations, yes. Team names, yes. People's names or spend? Your company's rule decides.
Then take the capacity sheet from your Q4 run, not the check sample run.
Replace the old capacity sheet in your agent's knowledge. Your card says how for your platform.
No sheet file from your run? Use the one in kit-m2.
Copilot without a license: keep the file on your computer. You upload it in chat next time.
Behind? kit-m2 has the whole agent as it should be now. You can load that instead before module 2.
TRANSITION: [BREAK]
```

## 3. Demo script

Platform: Claude (Project). Before class: build the project "Strategy Evidence Agent" as in the opening build check (starter instruction and `capacity-sheet.xlsx`). Check that **Code execution and file creation** is on (now also called **Create and edit files**). Do one rehearsal run of Q3 on brief v1. Save the rehearsal output and screenshots in your instructor folder. Keep a ChatGPT Project with the same kit as the backup.

| Step | Instructor does | Screen shows | If it fails |
| --- | --- | --- | --- |
| 1 | Open **Projects**, then the project "Strategy Evidence Agent" | The project page with the 3-line starter instruction and `capacity-sheet.xlsx` from the build check | Create it now: **+ New Project**, name "Strategy Evidence Agent". Add `capacity-sheet.xlsx`. Say: "This is what you did in the build check." |
| 2 | Select **Set project instructions**. Replace the starter text with all of `brief-v1.md`. Select **Save instructions** | The brief in the instructions panel. "My rules: None yet." at the end | If the panel will not save, paste the brief as the first chat message instead and say so. Continue |
| 3 | Select **+** in project knowledge. Add `job-card-portfolio-pack.md` and `strategy-okrs-kpis.md` | 3 files in project knowledge | Paste the two file texts into the chat with the run in step 4 |
| 4 | Start a new chat in the project. Upload `m1-submissions-q3.md` and `m1-status-q3.csv`. Send "Run the portfolio pack job" | The agent reads 5 programs. It writes the asks into the capacity sheet and returns an `.xlsx` file or the full tables in one message, then the flag report | No file: say "No file today. The brief asks for every table in full in one message." Run fails: switch to the ChatGPT backup. Both fail: show the rehearsal output |
| 5 | Open the output | Pack table, strategy consistency section, capacity table, flag report | Show the rehearsal output |
| 6 | Point to the pack table | 5 programs. Total ask USD 4,550 thousand. P-03 shows "On track" (submission) and "At risk" (tracker). P-04 link "None stated" | If a total differs, say: "That is exactly what an audit is for." Do not fix it live |
| 7 | Point to the strategy consistency section | O1 USD 910 thousand (P-03). O2 USD 3,000 thousand (P-01, P-02, P-05). O3 USD 0. No link USD 640 thousand (P-04). No judgment words | If the agent judges P-04 ("should be stopped"): say "The hand-off rule says list, not judge. That is an audit finding." |
| 8 | Point to the flag report | 2 flags: P-03 status differs from the tracker; P-04 has no stated link. Each line ends "PM decides". No recommended action | If a flag is missing: "Hand-off rules are not perfect. That is why you audit." |
| 9 | Download the output and save it | The file in your instructor folder | Use the rehearsal output in the debrief |

Do not audit or comment on the capacity table on screen. Every row shows "inside", including the Firmware team rows for P-01 and P-02 at 100 percent each. That is the lab's planted error.

## 4. Lab brief

- Goal: Delegate the quarterly pack to an agent that totals, links and flags, and manage it by its checks and flags.
- Core message: The meeting is for decisions, not reconciliation. The agent reconciles and shows the evidence. You make the strategy and funding calls.
- PM decision: Which programs to fund, pause or stop, where capacity goes next quarter, and whether the work or the stated strategy needs to change. The agent never recommends any of these.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Do not put unreleased roadmaps or release dates, forecasts, pricing, supplier terms or other non-public financial data into a tool your company has not approved. Do not put confidential names in web search queries. Plus the 3-question data check card above step 1 (about 2 minutes). Plans hold spend, headcount and unreleased dates. Remove names and spend, or use the case, if the tool is not approved. No confidential terms list in this lab (it is in lab 4). The capacity sheet (the pack log) keeps totals and allocations; decide if it keeps names.
- Setup: Zoom breakout rooms by platform, 3 to 5 learners. In person: tables by platform. Each card starts: "Build and save your own agent. Share your screen only when someone is stuck."
- Inputs: Own work: your team plan submissions, a status export and capacity by team for one quarter, with names and spend removed if the tool is not approved. Case: `kit-m1-template` (brief v1, job card, strategy file, capacity sheet), `m1-submissions-q3.md` and `m1-status-q3.csv` (run 1), `m1-submissions-q4.md` and `m1-status-q4.csv` (run 2), `m1-check-sample.md` (debrief check). `m1-pack-q2.md` is an optional format example (last quarter's pack, built by hand). No connector lane in this lab.
- Planted error warning: Told. "This batch has one planted AI error. Find it in your audit."
- Success check: The Q4 pack shows status, capacity and the link to an objective for each program. Each flag has your decision. You recorded audit findings for 2 shared teams and 3 linked items and added a check to the brief. The agent made no funding or strategy recommendation.
- Learner evidence: Tuned brief (v1 to v2 with the shared-team total check). Flag report decisions for Q3. Audit findings for 2 shared teams and 3 linked items. Fund, pause or stop calls with reasons, and a note on whether the work or the strategy needs to change. Recorded on `lab-1-record-sheet.md`.

## 5. Step cards

All four cards have the same 6 core steps. Saving is in each card header, not a step. The data check card and "Start here with sample data" sit outside the 6 steps. Learners use the kit in `kit/kit-m1-template/` and the run files from the case folder. Copilot learners use the `.txt` copies and the `.xlsx` sheet.

**Data check card (above step 1 on every card, about 2 minutes):**
1. Is this tool approved by my company for this data?
2. Does my file hold client data, health data, personal data, unreleased roadmap or release dates, forecasts, pricing, supplier terms or non-public financials?
3. If 2 is yes and 1 is no, use the Larkspan case or remove names and numbers first.

Write your choice on your record sheet.

**Google Sheet option (every card):** Work in your copy of the capacity sheet Google Sheet template. Download it as `.xlsx` or CSV. Upload it to your agent or in chat. The agent does not write live into your Sheet.

### Card: Claude
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Strategy Evidence Agent" from the opening build check.
- Saves: **Save instructions** saves the instructions. Files save when you add them. Chats save as you go.
- Check date and vendor doc: 2026-11-26. Claude Help Center, "How can I create and manage projects?" (https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects, dateModified 2026-11-06, platform matrix cl-pj-01 and cl-ui-09). "Create and edit files with Claude" (https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude, dateModified 2026-11-24, cl-fo-06 and cl-ui-10). "How to create custom skills" (https://support.claude.com/en/articles/12512198-how-to-create-custom-skills, approx 2026-10-28, cl-cl-03) for the stretch.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Do not put unreleased roadmaps or release dates, forecasts, pricing, supplier terms or other non-public financial data into a tool your company has not approved. Do not put confidential names in web search queries.

| Step | Do this |
| --- | --- |
| 1 | Add the kit: `brief-v1` in **Set project instructions**, the job card and strategy file in project knowledge with **+**. |
| 2 | In a new project chat, send the Q3 submissions and status export with the prompt "Run the portfolio pack job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit capacity for 2 shared teams and 3 linked items against the source files, on your record sheet. |
| 5 | Add one quality check for what you found under "My rules" in the project instructions. |
| 6 | In a new project chat, send the Q4 submissions and status export with the prompt "Run the portfolio pack job". |

Notes: `capacity-sheet.xlsx` is already in knowledge from the build check. No file in the answer? Check that **Code execution and file creation** (or **Create and edit files**) is on in **Settings**, then **Capabilities**. Team or Enterprise: ask your owner. It is in **Organization settings**, then **Capabilities**. If the `.xlsx` will not upload, use the CSV copy. Your project opens as one conversation with a Library? Tell the instructor. Claude is moving some projects to a new version.

**Start here with sample data:** Kit: `brief-v1.md`, `job-card-portfolio-pack.md`, `strategy-okrs-kpis.md`, `capacity-sheet.xlsx`. Q3 (step 2): `m1-submissions-q3.md`, `m1-status-q3.csv`. Q4 (step 6): `m1-submissions-q4.md`, `m1-status-q4.csv`. Own work: replace the strategy file with your strategy, OKRs and KPIs. Put your teams and programs in the capacity sheet rows.

**Pass condition (second sample, run in the debrief):** New chat in the project. Send `m1-check-sample.md` with "Run the portfolio pack job". Pass if: (1) The flag report names the Test lab with its cross-program total, 130 percent. (2) It names both programs, P-01 and P-04. (3) No other team is flagged as over capacity. (4) No funding, ranking or "pause" line appears.

**Stretch (only where verified):**
- Funding scenarios (all platforms): after step 6, send "Compare two scenarios I name. A: pause P-01 for Q1 2028. B: pause P-02 for Q1 2028. Fund all other programs at their ask. For each, show each team's total and which milestones slip. Do not recommend one." On your own work, name your own scenarios.
- Custom skill (Claude, all plans, code execution on; cl-cl-03, verified 2026-11-20). Turn the portfolio pack job into a skill in **Customize**, then **Skills**.

### Card: ChatGPT
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Strategy Evidence Agent" from the opening build check. Plan: ChatGPT Plus or higher. Project memory: default, not project-only.
- Saves: As you go.
- Check date and vendor doc: 2026-11-26. OpenAI Help Center, "Projects in ChatGPT" (https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt, "Updated: 3 days ago" on 2026-11-26, cg-01, cg-14 and cg-ui-09). "Creating and editing documents, spreadsheets and presentations with ChatGPT Work" (https://help-lb.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work, approx 2026-11-22, cg-10).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Do not put unreleased roadmaps or release dates, forecasts, pricing, supplier terms or other non-public financial data into a tool your company has not approved. Do not put confidential names in web search queries.

| Step | Do this |
| --- | --- |
| 1 | Add the kit: `brief-v1` in **•••**, then **Project settings**, the job card and strategy file to the project's files. |
| 2 | In a new project chat, send the Q3 submissions and status export with the prompt "Run the portfolio pack job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit capacity for 2 shared teams and 3 linked items against the source files, on your record sheet. |
| 5 | Add one quality check for what you found under "My rules" in **Project settings**. |
| 6 | In a new project chat, send the Q4 submissions and status export with the prompt "Run the portfolio pack job". |

Notes: `capacity-sheet.xlsx` is already in the project from the build check. For a sheet file with formulas, ChatGPT Work must be on your plan. Work does not run in a project with project-only memory (cg-14). No file in the answer? The brief asks for every table in full in one message. That is fine.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run in the debrief):** Open a new chat outside the project. Paste your tuned brief from **Project settings** as the first message. Attach `job-card-portfolio-pack.md`, `strategy-okrs-kpis.md` and `m1-check-sample.md`. Send "Run the portfolio pack job". Pass if: same 4 items as the Claude card.

**Stretch (only where verified):**
- Funding scenarios: same as the Claude card.
- Skill: ChatGPT skills are on business plans only and not verified for this course (cg-04). Not on this card.

### Card: Copilot agent builder
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the agent "Strategy Evidence Agent" from the opening build check. To open it: **All agents**, then **...** next to it, then **Edit**.
- Saves: **Create** the first time. **Update** after each change.
- Check date and vendor doc: 2026-11-26. Microsoft Learn, "Build agents with Agent Builder" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents, last updated 2026-11-16, mb-01, mb-04). "Add knowledge sources" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge, last updated 2026-11-16, mb-02, mb-14, mb-ui-12). "Share and manage agents" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents, last updated 2026-11-16, mb-ui-13). "Code interpreter" (https://learn.microsoft.com/microsoft-365-copilot/extensibility/code-interpreter, last updated 2026-11-16, mb-11, mb-13).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Do not put unreleased roadmaps or release dates, forecasts, pricing, supplier terms or other non-public financial data into a tool your company has not approved. Do not put confidential names in web search queries.

| Step | Do this |
| --- | --- |
| 1 | On the **Configure** tab, add the kit: `brief-v1.txt` text in **Instructions**, the other `.txt` files with **Upload**. |
| 2 | In the agent chat, send the Q3 submissions, status export and `capacity-sheet.xlsx` with the prompt "Run the portfolio pack job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit capacity for 2 shared teams and 3 linked items against the source files, on your record sheet. |
| 5 | Add one quality check for what you found under "My rules" in **Instructions**. |
| 6 | In a new chat, send the Q4 submissions, status export and `capacity-sheet.xlsx` with the prompt "Run the portfolio pack job". |

Notes: Use the `.txt` copies and the `.xlsx` sheet. Copilot does not take `.md` or CSV as knowledge. Send the `.xlsx` status files (`m1-status-q3.xlsx`, `m1-status-q4.xlsx`). If a chat upload fails, paste the text. Check that **Create documents, charts, and code** is on. Download any file the agent makes in the same session. Copilot keeps it for that session only.

**No Copilot license or billing?** Your agent cannot read Knowledge files. Do this instead:
1. Paste all of `copilot-fallback-instructions-m1.txt` into **Instructions**. Add no Knowledge files.
2. Do the steps above. Upload or paste the run files and `capacity-sheet.xlsx` in chat each run.
3. At step 5, add your check under "My rules" in **Instructions**.

The fallback agent does one job at a time.

**Start here with sample data:** Kit: `brief-v1.txt`, `job-card-portfolio-pack.txt`, `strategy-okrs-kpis.txt`, `capacity-sheet.xlsx`. Q3 (step 2): `m1-submissions-q3.md`, `m1-status-q3.xlsx`. Q4 (step 6): `m1-submissions-q4.md`, `m1-status-q4.xlsx`. Own work: as on the Claude card.

**Pass condition (second sample, run in the debrief):** New chat. Send `m1-check-sample.md` and `capacity-sheet.xlsx` with "Run the portfolio pack job". Pass if: same 4 items as the Claude card.

**Stretch (only where verified):**
- Funding scenarios: same as the Claude card.
- The custom skill stretch is not available on this platform in this course.

### Card: Gemini
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the skill "strategy-evidence-agent" from the opening build check. Find it in **Customize**, then **Skills**. This is a Gemini skill. Gems are now skills.
- Saves: **Create** the first time. **Save** after each change.
- Check date and vendor doc: 2026-11-26. Gemini Apps Help, skills page (https://support.google.com/gemini?p=pn_skills, page shows no date, gm-01 and gm-ui-10). Gemini Apps Help, Gems moved to skills (https://support.google.com/gemini/answer/18560919, gm-02, gm-06). Google blog, "Let skills in Gemini tackle your most repetitive tasks" (2026-09-30) for **/**. Google Workspace Updates, skills in the Gemini app (https://workspaceupdates.googleblog.com/2026/09/skills-gemini-app-workspace.html, 2026-09-30, updated 2026-11-09, gm-03).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Do not put unreleased roadmaps or release dates, forecasts, pricing, supplier terms or other non-public financial data into a tool your company has not approved. Do not put confidential names in web search queries.

| Step | Do this |
| --- | --- |
| 1 | Add the kit to your skill: `brief-v1` in the instructions, the job card and strategy file with **Add**, **files**, **Upload**. |
| 2 | In a new chat, send the Q3 submissions and status export with "/strategy-evidence-agent Run the portfolio pack job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit capacity for 2 shared teams and 3 linked items against the source files, on your record sheet. |
| 5 | Add one quality check for what you found under "My rules" in the skill instructions. |
| 6 | In a new chat, send the Q4 submissions and status export with "/strategy-evidence-agent Run the portfolio pack job". |

Notes: Type **/** in the chat and pick your skill from the list. Totals: your skill reports each value. Check the sums in your Google Sheet copy of the capacity sheet. The sheet formulas do the math. A live write by the skill into your Sheet is not verified. Do not turn on Canvas or Deep Research. They do not work in skills (gm-06). If an upload fails, paste the text.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run in the debrief):** Same as the Claude card. Use the prompt "/strategy-evidence-agent Run the portfolio pack job".

**Stretch (only where verified):**
- Funding scenarios: same as the Claude card.
- The custom skill stretch does not apply: your agent is already a skill.

### Fast-start cards (module 1 only)

For learners new to the builder. One annotated screenshot per card (Stage 4 adds it): where to start, and which field the brief goes in.

| Platform | 1. Open | 2. The brief goes in | 3. Files go in | 4. Run it in |
| --- | --- | --- | --- | --- |
| Claude | **Projects**, then your project | **Set project instructions**, then **Save instructions** | Project knowledge, **+** | A new chat in the project |
| ChatGPT | Your project in the sidebar | **•••**, then **Project settings** | The project's files | A new chat in the project |
| Copilot | **All agents**, then **...**, then **Edit** | **Configure** tab, **Instructions**. Then **Update** | **Knowledge**, **Upload** (`.txt` and `.xlsx` only) | The agent chat |
| Gemini | **Customize**, then **Skills**, then your skill | The skill instructions. Then **Save** | **Add**, then **files**, then **Upload** | A new chat. Type **/** and pick the skill |

## 6. Debrief

- Questions: Which 2 teams did you total? What did the pack say about their capacity? Which check or audit found the error? What are your fund, pause or stop calls, and why? Does the work need to change, or the strategy?
- Error reveal (record ids): `m1-submissions-q3.md`, Team asks: P-01 Probe X cellular asks the Firmware team for 100 percent; P-02 Hub firmware asks the same team for 100 percent. Firmware team 12 FTE (`company.md`). Total 200 percent, 24 FTE against 12. On brief v1 every per-program row is "inside", and the capacity sheet shows 0 rows "over" because it checks each row alone. Other shared teams in Q3: Cloud team 90 (P-01 25 + P-03 55 + P-05 10), Hardware design team 90 (P-01 50 + P-04 40), Test lab 90 (P-01 40 + P-02 20 + P-04 30). Data platform team 90 (P-05 only).
- Debrief check (instructor only, `case/expected-results.md`): After the fix, the Q4 flag report names the Firmware team over capacity: P-01 90 + P-02 60 = 150 percent, 18 FTE asked, 12 available (evidence `m1-submissions-q4.md`, submitted 2027-11-16 and 2027-11-17). It also flags P-02 status ("On track" against tracker "At risk") and P-04 link (tag "O2" only). 3 flags in total. Test lab at exactly 100 percent is not over. Cloud team 95 percent, inside. Work with no clear link is listed, not judged. Q4 total ask USD 4,750 thousand. Ask by objective: O1 USD 760 thousand, O2 with a key result USD 3,400 thousand, O2 tag only USD 590 thousand, O3 USD 0. No funding or strategy line.
- Check sample: each learner runs `m1-check-sample.md` in a new chat on the tuned brief (ChatGPT: outside the project), 3 minutes. Expected: Test lab 130 percent (P-01 70 + P-04 60), 7.8 FTE asked, 6 available. 0 programs over on the per-program check. 0 status differences. Highest other team: Hardware design team 95 percent, inside. Pass condition on the cards.
- Fund, pause or stop (2 minutes, half day 3): each learner writes calls and a reason on the record sheet. Case PM's example (a choice, not an answer): Firmware team, keep P-02 at 60 percent and ask the Head of Product to choose the P-01 level. P-04 Tag 2, pause until a link to a key result is stated. Strategy: the work does not change the strategy; O3 has no program with a stated link; noted for the next review.
- What you do Monday: Take last quarter's plan. Total each shared team across all programs before the next review.
- Log save card (1 minute):

| Platform | 1. Decide what the log keeps | 2. Replace in the agent |
| --- | --- | --- |
| Claude | Download the capacity sheet from your step 6 run. Delete names or spend your company does not allow | In project knowledge, delete the old `capacity-sheet`. Add the new file with **+** |
| ChatGPT | Same as Claude | Open the old `capacity-sheet` in the project sources list. Delete it. Add the new file |
| Copilot | Download the sheet from your step 6 run, in the same session. Same check | On **Configure**, choose the **X** next to the old file, then **Remove**. **Upload** the new file. Select **Update** |
| Copilot, no license | Download or copy the sheet. Same check | Keep it on your computer. Upload it in chat at the next run |
| Gemini | Update your Google Sheet copy, then download it as `.xlsx`. Same check | In your skill, **More**, then **Replace file**. Select **Save**. If that fails, upload the whole skill again with the new file |

Name the new file `capacity-sheet` before you add it. Use the step 6 run, not the check sample run. No sheet file from your run? Use `kit-m2/capacity-sheet.xlsx`.

## 7. LD spec

| Field | Value |
| --- | --- |
| Objective | Build the Strategy Evidence Agent from the template, run 2 quarters of team submissions, decide each flag, audit capacity for 2 shared teams and 3 linked items, add a quality check, and make fund, pause or stop calls with reasons (m1-o1 to m1-o4) |
| Timing | Full day: lab 33 minutes, debrief 9 (check sample 3). Half day: lab 38, debrief 10. Lab brief before it: 3 minutes |
| Setup (Zoom) | Breakout rooms by platform (Claude, ChatGPT, Copilot, Gemini), 3 to 5 learners each. Learners keep their own screen. Share only when stuck. Instructor visits rooms in turn, Copilot first |
| Setup (in person) | Tables by platform, 3 to 5 learners. One laptop per learner. Instructor walks the tables, Copilot first |
| Steps per platform | See section 5 (4 cards with the same 6 core steps, data check card, fast-start cards, stretch) |
| Materials | `kit/kit-m1-template/` (brief v1, job card, strategy file, capacity sheet `.xlsx` and CSV, Copilot fallback text, record sheet, README with rebuild card). Case files `m1-submissions-q3.md`, `m1-status-q3.csv` / `.xlsx`, `m1-submissions-q4.md`, `m1-status-q4.csv` / `.xlsx`, `m1-check-sample.md`, `m1-pack-q2.md` (optional format example). Google Sheet template of the capacity sheet (to be made, question 10). `kit/kit-m2/` for catch-up. Instructor only: `case/planted-errors.md`, `case/expected-results.md`, saved demo output |
| Success criteria | The Q4 pack shows status, capacity and the link to an objective for each program. Each flag has the learner's decision. Audit findings for 2 shared teams and 3 linked items recorded. A check added to the brief. The agent made no funding or strategy recommendation. Check sample passes the 4-item pass condition |
| Debrief questions | Which 2 teams did you total? What did the pack say about their capacity? Which check or audit found the error? What are your fund, pause or stop calls, and why? Does the work need to change, or the strategy? |
| Fallback path | Cannot use own work: case data. Platform blocked: change platform or pair with a learner on another platform. Copilot with no license: fallback instructions text, run files and the sheet uploaded or pasted in chat. No file output: every table in full in one message (brief "Output"). Code execution off: the agent shows each sum in full (brief "Numbers"). Agent does not make the error: debrief uses the saved demo output. Behind at the end: load `kit-m2` before module 2 |
| Learner evidence | Tuned brief (v1 to v2 with the shared-team total check). Flag report decisions for Q3. Audit findings for 2 shared teams and 3 linked items. Fund, pause or stop calls with reasons, and a note on whether the work or the strategy needs to change. All on `lab-1-record-sheet.md` |

## 8. Learner kit

Character counts measured with Python `len` on 2026-11-27 (characters, line breaks included). Copilot course budget (spec `copilot_no_license_fallback`, a course design budget, not a vendor number): core brief 3,500 or fewer, job card 1,500 or fewer, one knowledge text 2,800 or fewer. Vendor limit: Instructions 8,000 characters (mb-01).

| File | Loads into | Characters | `.txt` copy |
| --- | --- | --- | --- |
| `kit-m1-template/brief-v1.md` | Instructions | 2,164 (budget 3,500) | yes |
| `kit-m1-template/job-card-portfolio-pack.md` | Knowledge | 1,365 (budget 1,500) | yes |
| `kit-m1-template/strategy-okrs-kpis.md` (copy of `case/strategy-okrs-kpis.md`) | Knowledge | 2,770 for the `.txt` (budget 2,800) | yes (copy of `case/strategy-okrs-kpis.txt`) |
| `kit-m1-template/capacity-sheet.xlsx` (copy of the case file) | Knowledge (Copilot: also in chat each run) | sheet, not counted | n/a; `capacity-sheet.csv` copy for Claude, ChatGPT, Gemini |
| `kit-m1-template/copilot-fallback-instructions-m1.txt` | Copilot Instructions, no license | 6,673 (limit 8,000) | is a `.txt` |
| `kit-m1-template/lab-1-record-sheet.md` | Not loaded. Learner keeps it | 1,683, not counted | no |
| `kit-m1-template/README.md` (rebuild card) | Not loaded | not counted | no |
| `kit-m2/brief-v2.md` | Instructions | 2,469 (budget 3,500) | yes |
| `kit-m2/job-card-portfolio-pack.md` | Knowledge | 1,365 | yes |
| `kit-m2/strategy-okrs-kpis.md` | Knowledge | 2,770 for the `.txt` | yes |
| `kit-m2/capacity-sheet.xlsx` (Quarter "Q1 2028", asks from `m1-submissions-q4.md`) | Knowledge | sheet, not counted | n/a; CSV copy with calculated values |
| `kit-m2/problem-backlog`, `request-decision-log`, `roadmap` (`.xlsx` and `.csv`, copies of the case files) | Knowledge (module 2) | sheets, not counted | n/a |
| `kit-m2/job-card-requests.md` | Knowledge (module 2) | Added by the module 2 builder | yes, by the module 2 builder |
| `kit-m2/lab-1-pack-decisions.md` | Not loaded. Handout | 1,705 | yes |
| `kit-m2/copilot-fallback-instructions-m1-v2.txt` | Copilot Instructions, no license, to rerun job 1 | 6,997 (limit 8,000) | is a `.txt` |
| `kit-m2/README.md` | Not loaded | not counted | no |

Fallback sum check: header 358 + brief v1 2,164 + job card 1,365 + strategy 2,770 + 2 separators = 6,673. Module 2 budget after brief v2 (2,469): the module 2 fallback holds brief v2 and the request job card (1,500 or fewer), plus one knowledge text (2,800 or fewer): at most about 7,200 with a header, under 8,000.

Knowledge files in the agent after module 1: 4, counting the instructions (spec count). On the platform: 3 knowledge files plus the instructions. Course limit 20 on ChatGPT Plus and Copilot; course plan 16 at the end.

## 9. Instructor notes

- Timing flex:
  - Behind before the lab: cut the half-day questions on 1.4 and 1.8. Shorten 1.4 to the case strip. Never cut the hand-off rule (1.8), the data check (1.9) or the lab brief (1.10).
  - Behind in the lab: at minute 30 (half day 35), tell learners who have not sent step 6 to skip it and go to the debrief. Run step 6 after class. The debrief still works from the Q3 run.
  - Behind in the debrief: keep the reveal (1.12) and the check sample (1.13). Cut 1.14 to "write your calls on your record sheet after class", and read the case PM's example in one line. Skip the story slot.
  - Ahead: learners do the funding scenario stretch. In the debrief, ask one learner which milestones slipped under each scenario, and whether their agent stayed out of the choice.
- Common failures and recovery:

| Failure | Recovery |
| --- | --- |
| Claude: `.xlsx` upload fails or no file in the answer | Turn on **Code execution and file creation** (**Create and edit files**). Or use `capacity-sheet.csv`. Or accept every table in full in one message (brief "Output") |
| ChatGPT: no sheet file | Work is not on the plan, or project memory is project-only (cg-14). Accept the tables in one message. Do not rebuild the project in class |
| ChatGPT: check sample takes too long outside the project | Paste only "My rules" and the core rule from the brief, attach the 3 files, and send. Record the time on the card test sheet |
| Copilot: the agent ignores the knowledge files (no license or billing) | Use the no-license box on the Copilot card: `copilot-fallback-instructions-m1.txt` in **Instructions**, files uploaded or pasted in chat |
| Copilot: `.md` or CSV upload refused | Use the `.txt` copies and the `.xlsx` status files. In chat, paste the text if upload fails |
| Copilot: output file gone | Files last for the session only (mb-11). Rerun step 6, or use `kit-m2/capacity-sheet.xlsx` at the log save card |
| Gemini: skill name rejected | Use lowercase and hyphens: strategy-evidence-agent |
| Gemini: `.xlsx` will not add to the skill | Add `capacity-sheet.csv` instead |
| The agent reads row 1 of the sheet (the notice line) as the header | Tell it: "The header row is row 3. Data starts in row 4." This is in `case/README.md` |
| The answer stops halfway (long output) | Send "Continue". Or send "Give the capacity table and the flag report only" |
| The agent does not make the planted error (it totals the Firmware team on brief v1) | Good. Ask the learner whether it flagged the 200 percent or only showed it. In the debrief, show the saved demo output |
| The agent writes a funding or priority line ("pause P-04", "fund P-01 first") | Audit finding. Point to the core rule and hand-off rule 3. Add it to the record sheet. Rerun |
| The agent judges unlinked work ("Tag 2 is off strategy") | Audit finding. Hand-off rule 2 says list, not judge |
| After the fix, the agent flags the Test lab in Q4 | Test lab is at exactly 100 percent. Over means more than 100 percent (the Larkspan PM's choice). Ask the learner to read their own check: did they write "over" or "at or over"? |
| A learner's own plan has no capacity by team | Use the case data for this lab. On Monday, start with team asks per program in the capacity sheet rows |
| A learner is far behind | Load `kit-m2` at the start of module 2. About 5 minutes |

- Case notes (rechecked 2026-11-27 against the case files; no `open_items` entry is owned by the module builder in this spec):
  1. Q3 statuses: P-03 is the only mismatch (submission "On track", tracker "At risk"). P-05 reports "At risk" in both, so it is not a flag.
  2. Q4 statuses: P-02 is the only mismatch. P-03 and P-05 changed to "On track" in both the submission and the tracker.
  3. Links: P-03 writes "KR1.2 Pharmacy and lab records at audit". The strategy file names KR1.2 "Customers with no missing records at last audit (survey)". The id matches and the text names what the work does, so the case PM treats it as a good link. A learner may note the wording gap in the 3-link audit. Accept it as a finding, not an error.
  4. Q4 P-04 link is "O2" only. It names an objective, not what the work does. The template link check catches it.
  5. Capacity sheet rows match the Q3 and Q4 team asks (11 rows). The check sample has no P-02, so the Firmware team P-02 row and the Test lab P-02 row stay empty for that run. The check sample also gives team sizes in its own text.
  6. The check sample is plan quarter Q2 2027, submitted March 2027, so it is an earlier quarter than the lab runs. It has no status differences.
  7. `m1-pack-q2.md` shows the old hand-built pack. It shows only the largest single team ask per program, so it also misses shared team totals. Use it as a "before" picture if a learner asks what the review looked like.
  8. The Firmware team writes firmware for Hub, Probe X and Tag (`company.md`). Tag 2 (P-04) does not ask the Firmware team in Q3 or Q4.
- Kept off the slides on purpose: every W1 and W3 figure (OI-10). Every Trendslop figure (OI-10). The Expedia anecdote (W1, not data). E1 ("54% vs 36%") belongs to module 2. The Strategy Matrix (Dan, row 01).
