# Module 4: First hand-off: the alternatives map from your own deals

Course: Advanced AI for Market Research (`market-research`). Stage 3 draft by the module builder, 2026-11-27. Revised once on 2026-11-27 after the consistency and verifier reports (`revision-notes.md`). Case year is 2027 (`case/year-shift-map.md`). Real source and vendor dates stay 2026. Built from `spec.yaml` (Gate 2, approved 2026-11-26; module 4 entry, `stretch_scope`, `copilot_no_license_fallback`, `platform_matrix_summary.stretch_verification`, `gate_2_proof_patterns` P3), `outline/development-brief.md`, `outline/gate-2-decisions.md` (decisions 6, 8, 10), the case files, `research/stretch-verification-2026-11.md`, Dan's OI-05 example (`modules/m4/example-oi-05.md`), the approved module 1 and the module 2, 3 and 5 drafts in review (decisions and revision notes). Starts from `modules/m3/kit/kit-m4/`. Ends at `kit/kit-m5/`, built to match the contract `modules/m5/kit/kit-m5-expected.md`.

## 1. Summary

| Item | Value |
| --- | --- |
| Workflow row and bottleneck | mr-wf-10. Keep the alternatives map current from the team's own evaluator and deal evidence. Bottleneck: keeping the competitive picture current is recurring work that no one has time for, and competitor documents age fast (N13, W21 weak). Teams track named competitors and miss the workarounds and "do nothing" that buyers choose (no source; recorded gap). Gap: no source on an alternatives map built from own deal evidence. Dan's Pragmatic client example fills the example slot (OI-05, closed) |
| Framework category and focus area | Market. Competitive Landscape |
| Capability Standards (as in spec) | Confirmed by Dan, Pragmatic to confirm. Skill 1.2 Market Segmentation. Competency 1.2A. Gap: the Competitive Landscape box has primary skill 2.2 (capability 2). 1.2 is a secondary skill on the box. The course does not claim 2.2 |
| Rung | 3, Hand-off between jobs. The win/loss job hands its driver log to the map job. A hand-off rule says what passes and what stops. Second agent: stretch, Claude and ChatGPT cards only, manual file hand-off, not yet tested by the course team |
| Minutes (full day / half day) | 55 / 55 (same in both; Gate 2 decision 8) |
| Instructor-led / hands-on (minutes, %) | 22 / 33 = 40% / 60% (7 + 8 + 7 = 22; 25 + 8 = 33). Inside the 40/60 rule (plus or minus 5 points) |
| Planted error and warning level | CRM competitor trusted where the buyer did nothing. Deal D-3108 (Hobnail Burger Co, Food service, lost Q3 2027): the driver log "Alternative chosen" is blank, the CRM competitor is "Rimecore", and interview WL-3108 says the buyer bought nothing and kept the spreadsheet. The agent fills the blank from the CRM. Rimecore shows Q2 2, Q3 3, "growing". The link check passes. Warning: hint ("Audit before you approve."). No audit hint |
| Learner evidence | The hand-off rule as written (step 2) and as fixed (step 6). Audit findings for 3 traced map entries. Flag report decisions. The alternative to beat in one segment, with its evidence. All on `lab-4-record-sheet.md` |
| Agent after this module (files) | Instructions: brief v5 (rule 4 is the lab 4 hand-off rule). Knowledge: `job-card-problem-backlog`, `code-book`, `problem-backlog`, `job-card-win-loss`, `driver-code-book`, `driver-log` (Q2 and Q3 rows), `job-card-weekly-feedback`, `tag-list`, `job-card-alternatives-map` (new), `alternatives-map` (new). 10 knowledge files. Catch-up: `kit/kit-m5/` |

### Slide minutes check

| Arc step | Slides | Minutes | Mode |
| --- | --- | --- | --- |
| Why this matters, workflow and bottleneck, example slot | 4.1 to 4.4 | 1 + 2 + 3 + 1 = 7 | Instructor-led |
| Live demo | 4.5, 4.6 | 6 + 2 = 8 | Instructor-led |
| Build pattern and lab brief | 4.7 to 4.11 | 2 + 1 + 2 + 1 + 1 = 7 | Instructor-led |
| Lab 4 | 4.12 | 25 | Hands-on |
| Debrief | 4.13 to 4.17 | 3 + 2 + 1 + 1 + 1 = 8 | Hands-on |
| Total | 17 slides | 55 | 22 + 33 |

Full day and half days use the same 55 minutes (spec module 4 has no `half_day` block). Debrief minutes follow the spec arc: rerun with the fixed hand-off rule 3, reveal 2, check sample 1, what you do Monday 1, log save card 1. "Which alternative to beat in each segment" has no minutes in the spec. It is asked on 4.13 while the rerun runs (B5).

### Slide text check (36 pt on the wide master)

Rule used: the on-slide body text of each slide is 300 characters or fewer and 8 short lines or fewer, so it fits 36 pt body text on the wide master. Layout tags ("ACTIVITY", "DEBRIEF", "LIVE DEMO") and minutes are not counted. Longest bodies: 4.11 data safety (300), 4.9 lab brief (297), 4.14 reveal (248, shown on click). Measured with a script on 2026-11-27. The full steps are only on the cards in the workbook (Dan's lab brief slide rule; module 1 Gate 4 decision G4-1).

### Builder decisions inside the spec

| # | Decision | Why |
| --- | --- | --- |
| B1 | The lab 4 hand-off rule lives in the brief, "My rules" 4. The job card points to it: step 1 "Map it only as "My rules" allow" and the hand-off rule "A deal that a hand-off rule in "My rules" stops." Card step 2 writes rule 4. Card step 6 fixes rule 4 | Same place as the lab 1 to 3 rules, so card steps 2 and 6 edit the instructions, not a knowledge file (a knowledge file edit needs a re-upload on every platform). It matches the `kit-m5-expected.md` default and the module 5 draft (brief v5 rule 4, lab 5 rule 5). See D1 |
| B2 | The job card holds 2 of the 3 spec hand-off rules: "An alternative that is not in the map" and "A segment where "do nothing" or a workaround is the top alternative". The third spec rule (CRM competitor and buyer differ) enters through the learner's fixed rule 4. After the fix, the agent has all 3 | The Gate 2 proof card (`proof/job-card-alternatives-map.md`) leaves the third rule to the PM. With the mismatch rule in the template, the planted error could not reach the audit. See D2 |
| B3 | The map job also writes the updated driver log (job card step 6, output 5: add the new deals, do not recount match rates). The log save card saves 2 files: the map and the driver log | Module 5 D2: lab 5 Q1 and Q4 need the Q3 deals in the agent. See D4 |
| B4 | The lab brief is 3 short Activity slides: 4.9 goal, 6 key actions and the workbook pointer; 4.10 done when and the hint; 4.11 data safety. Full steps only on the step cards | Dan's lab brief slide rule (2026-11-27) and the 36 pt rule. The standard data safety text and the module 4 deal data line do not fit on 4.10 with the success check at 36 pt |
| B5 | "Which alternative must you beat in each segment?" is asked on 4.13 while the rerun runs, and recorded in section 5 of the record sheet. The reveal (4.14) gives the case answer for Food service | The spec debrief minutes add up to 8 without it. Objective m4-o4 still gets practice. Same pattern as module 2 B3 and module 3 B3 |
| B6 | The check sample result on 4.15 comes from a tuned instructor project built from `kit-m5` before class. The live demo runs on the untuned brief | A result from the untuned brief cannot show the pass condition. Same as module 3 B4. See D6 |
| B7 | No audit hint. Step 5 audits 3 map entries: every entry labeled growing or fading first, then random picks up to 3 (revise once, consistency F5). The rule is a manager rule ("audit what moved"), not a pointer: before the fix it covers Rimecore, do nothing and controller alarms alike. The record sheet checklist is neutral. The demo points to ALT-04 (do nothing), not ALT-01 (Rimecore). The step 2 examples on the record sheet and slide 4.7 name no blank cell and no CRM field | Module 1 D11: the audit hint was for lab 1 only. Warning level for lab 4 is "hint". A pure random pick of 3 of 4 entries missed Rimecore for 1 learner in 4. See D3 |
| B8 | Second-agent stretch: Claude and ChatGPT cards only, manual file hand-off, after class, headed "Stretch (vendor doc checked, not yet tested)". Copilot and Gemini cards: the standard `stretch_scope` line. Slide 4.8 names the gap once | `research/stretch-verification-2026-11.md` section 4 (module 4 table). Same marking as module 3 D1 and module 5 B16. Revise once: file-only hand-off kept, with a card note. See D5 |
| B9 | No schedule stretch on the module 4 cards | The module 3 Claude schedule stretch is not tested yet. A Cowork project imported in module 3 does not hold the map job card. A 25-minute lab has no room for it. See D7 |
| B10 | Slide 4.2 shows only "Competitor documents age fast" (N13 primary Wynter 2026: battlecards go stale; W21 weak: documents age quickly; independent). "Hand-built" (W21 only) is off the slide (verifier F3). "A side job" (N13 only) is in the talk track, attributed. "Buyers choose do nothing more often than teams track" is not on a slide as a claim (no source, recorded gap) | Research rule 2. Same pattern as module 3 D7 and module 5 B14. See D10 |
| B11 | The required example (OI-05) is on 4.3 as Pragmatic's client story, with no client name, dates, values or people | Gate 2 decision 6, decision 43, `example-oi-05.md` guardrails. See D8 |
| B12 | `kit-m5` copies the 3 drafts in `modules/m5/kit/kit-m5-draft/` with no change (brief v5 3,491, driver log 7,616, map 3,286) and 7 kit-m4 files with no change. The driver code book stays the case file: no "controller alarms" row | Contract `kit-m5-expected.md`. The map holds controller alarms as ALT-03 (substitute) since lab 2. See D11 |
| B13 | The `kit-m5` Copilot fallback text holds brief v5 and the map job card only (5,388). The map goes in chat | Brief v5 + job card + Q3 map = 8,681 with the header, over the 8,000 limit (mb-01). The lab 4 fallback text follows the spec (brief v4, job card and the Q2 map: 7,419). See D12 |
| B14 | The debrief rerun runs in a new chat with the evidence pack: "In a new chat, send the evidence pack with the prompt "Run the alternatives map job"." | A new chat is the only way to be sure the fixed brief applies on all 4 platforms. Same as module 1 D1 and module 3 B1 |
| B15 | The card pass condition (second sample, run after class) names D-4102 and D-4104 but gives no reason text | The card is in the workbook before the lab. A reason ("CRM says Vantafrost") would point at the planted error. See D9 |
| B16 | The demo writes a neutral draft rule 4: "Pass only lost deals to the map. Won deals stay in the driver log." | Shows the shape of a hand-off rule between jobs without pointing at the planted error |

### Decisions for Dan

Open decisions for the Gate 3 doc, most important first. One line each, with a recommendation. Revised once on 2026-11-27 (`revision-notes.md` maps the old numbers).

| # | Decision | Recommended |
| --- | --- | --- |
| D1 | Where the lab 4 hand-off rule lives. A: brief "My rules" 4, the job card points to it (built). B: in the job card (learners re-upload a knowledge file in steps 2 and 6; module 5 renumbers its rule) | A. Module 5 is built on it |
| D2 | The job card holds 2 of the 3 spec hand-off rules. The CRM-and-buyer mismatch rule enters through the learner's fixed rule 4, so the planted error can reach the audit | A. Needs change 1 |
| D3 | Audit pick: every entry labeled growing or fading first, then random picks up to 3 (spec says 3 random). Every learner audits what moved, so no one misses the planted entry by chance | A. Needs change 5 |
| D4 | The log save card saves the driver log with the Q3 rows and the map (module 5 D2 option A). The job card writes both | A |
| D5 | Second-agent stretch on the Claude and ChatGPT cards only: a second project runs the map job on the driver log file alone (file-only hand-off, with a card note). After class, "not yet tested by the course team". Your stretch tests 3 and 4 decide it | A: keep, marked. Needs change 2 |
| D6 | Check sample on 4.15 shown from a tuned instructor project built from `kit-m5` before class | A. Needs change 4 |
| D7 | No schedule stretch on the module 4 cards (spec stretch item 1) | A. Needs change 3 |
| D8 | Pragmatic client story on 4.3: confirm Pragmatic is fine with it in licensed course content | Confirm before Gate 3 approval |
| D9 | Card pass condition names D-4102 and D-4104 with no reason text, and says "run this after class" (as module 3 D14) | A. Same spec change as module 3 change 3 |
| D10 | Slide 4.2 says "Competitor documents age fast" (2 sources). B: keep "Hand-built" with W21 alone (weak) | A |
| D11 | "Controller alarms" is not added to the driver code book. The map holds it as ALT-03 | A: no change |
| D12 | `kit-m5` Copilot no-license text: map in chat, not in Instructions (8,681 with it, over 8,000). The lab 4 text follows the spec | A |
| D13 | A learner's own saved driver log may keep the Part 1 D-3108 quote. `kit-m5` uses the WL-3108 quote (module 5 D7). Lab 5 Q4 needs only D-3108 on alert accuracy | A: accept |
| D14 | Lab brief as 3 short slides (4.9 to 4.11) so each fits 36 pt | A |
| D15 | The demo runs the untuned brief on the lab data, so the planted error may show. The instructor does not comment (module 3 pattern) | A |

### Changes needing Dan's yes

None of these are made. Each waits for your yes.

| # | File (fingerprinted or approved) | Change | Why |
| --- | --- | --- | --- |
| 1 | `spec.yaml`, module 4 `lab.handoff_rules` | Add a note: "The job card holds rules 1 and 3. Rule 2 (CRM competitor and buyer differ) is the learner's fix, rule 4 in the brief ("My rules"). After lab 4 the agent has all 3" | Only if D2 is A |
| 2 | `spec.yaml`, module 4 `stretch` item 2 | "Build the map job as a second agent that reads the first agent's output file. Only on step cards where verified" becomes "Manual file hand-off, Claude and ChatGPT cards: a second project runs the map job on the driver log file from the first project. After class. Vendor doc checked 2026-11-27, not yet tested by the course team. Copilot and Gemini: standard line (stretch_scope)". The `stretch_scope` rule change is module 3 change 4 (doc now, test pending) | Only if D5 is A |
| 3 | `spec.yaml`, module 4 `stretch` item 1 | "Run the map job on each new win/loss batch. Schedule stretch..." becomes "Not on the module 4 cards. The module 3 Claude schedule stretch covers the schedule" | Only if D7 is A |
| 4 | `spec.yaml`, module 4 `arc` (debrief) and `check_sample` | "the m4-check-sample.md result from the demo run" becomes "the m4-check-sample.md result from a tuned instructor project (kit-m5), run before class" | Only if D6 is A |
| 5 | `spec.yaml`, module 4 `card_steps` step 5; `research/workflows.yaml` mr-wf-10 `audit` | "Audit 3 random map entries..." becomes "Audit 3 map entries, every growing or fading entry first, then at random, against the interviews and deal records" | Only if D3 is A |
| 6 | `research/platform-matrix.yaml` | As in the module 4 verifier report, last section: cl-pj-01 (source_date 2026-11-06, Free 5 projects), cl-ui-09 (checked 2026-11-27), cl-fo-06 (source_date 2026-11-24, plain text output, download from the conversation), cg-01 (about 2026-11-26, unlimited projects), cg-ui-09 (new path: **+** next to **Projects**, **Create project**; **•••** > **Project settings** > **Instructions**), cg-03 (new URL and title; **+**, **Add photos & files**; Go and Plus 25 files; remove the "Plus 20" conflict), cg-08 (checked 2026-11-27, stays partly verified) | The cards use these names. Verifier proposal |
| 7 | `research/needs.md` N13 and `research/workflows.yaml` W21 | N13: checked_on 2026-11-27; Wynter wording "PMM owns it on the side" (52%), battlecards go stale; no wording on hand-built work. W21: checked_on 2026-11-27; "Originally published at seeto.ai"; only source for "hand-built" | Verifier proposal |
| 8 | `modules/m1/course-open.md` (approved), line 268, ChatGPT build check step 1; and `m1/slides.json` or the workbook if they carry it | "Select **New project** in the sidebar." becomes "In the sidebar, select **+** next to **Projects**. Name it "Market Evidence Agent", then select **Create project**." Modules 2, 3 and 5 have no hit for the old path (grep 2026-11-27) | OpenAI page changed about 2026-11-26 (module 4 verifier F1) |
| 9 | `case/expected-results.md`, kit state row kit-m5 | Same as module 5 change 1 (Q3 driver log rows, D-3102 and D-3108 read from the interviews). Not a new change | Already listed by module 5 |

The module 5 side of the hand-over (old change 6) is done in this revision. See `revision-notes.md`, "Module 5 hand-over edits".

### Contract check: kit-m5 against `modules/m5/kit/kit-m5-expected.md`

| # | Contract file | kit-m5 file | Status | Characters | Constraint met |
| --- | --- | --- | --- | --- | --- |
| 1 | `README.md` | `README.md` | Written by module 4 | not loaded | Says 10 knowledge files; lab 5 adds 2; 12 at the end |
| 2 | `brief-v5.md` | `brief-v5.md` + `.txt` | Copy of the draft. Rule 4 in "My rules" | 3,491 | 3,500 or fewer |
| 3 | `job-card-problem-backlog.md` | + `.txt` | No change (kit-m4) | 1,194 | yes |
| 4 | `code-book.md` | + `.txt` | No change | 2,791 | yes |
| 5 | `problem-backlog.md` | + `.txt` | No change. The map job reads it, does not write it | 15,194 | Under 15,400 |
| 6 | `job-card-win-loss.md` | + `.txt` | No change | 1,483 | yes |
| 7 | `driver-code-book.md` | + `.txt` | No change. No "controller alarms" row (D4) | 2,284 | 2,800 or fewer |
| 8 | `driver-log.md` | + `.txt` | Copy of the draft. D-3102 Vantafrost, D-3108 "Spreadsheet and clipboard (do nothing)" with the WL-3108 quote "Your trial sent alerts every lunch rush, and my managers gave up on it." Q3 flag D-3108 with the case PM decision | 7,616 | With map and past reports: 13,675, under 15,400 |
| 9 | `job-card-weekly-feedback.md` | + `.txt` | No change | 1,496 | yes |
| 10 | `tag-list.md` | + `.txt` | No change (v2, P10) | 2,038 | yes |
| 11 | `job-card-alternatives-map.md` | + `.txt` | Written by module 4. Names where the rule lives ("My rules") | 1,497 | 1,500 or fewer |
| 12 | `alternatives-map.md` | + `.txt` | Copy of the draft (end of Q3 2027, after the fix) | 3,286 | Types table and 2 format tables kept |
| 13 | `lab-4-fix-rules.md` | + `.txt` | Written by module 4 | 1,016 | none |
| 14 | `copilot-fallback-instructions-m4-v5.txt` | same | Written by module 4. Brief v5 + map job card. Map in chat (D7) | 5,388 | 8,000 or fewer; course budget 7,800 |

Contract section 3 answers:

1. The lab 4 hand-off rule lives in the brief, "My rules" 4. The lab 5 rule stays rule 5.
2. Exact text: "Lab 4: The alternative chosen comes from the buyer's interview. If the driver log cell is blank, read the interview. Never fill it from the CRM competitor field. If the CRM field and the buyer differ, send the deal to the flag report." (`case/planted-errors.md`, lab 4.)
3. Yes. The log save card saves the driver log with the Q3 rows, and the map.
4. Final job card: `kit/kit-m5/job-card-alternatives-map.md` (1,497).
5. No. "Controller alarms" is not added to the driver code book (D11).
6. Counts: section 8.

## 2. Slides and talk track

### Slide 4.1: Module 4. First hand-off: the alternatives map
- Layout: Chapter Break
- Minutes: 1
- On-slide text: MODULE 4. First hand-off: the alternatives map. Promise: "Map what buyers chose, from your own deals." Bullets: Add an alternatives map job. Write a hand-off rule between jobs. Trace each entry to a buyer.
- Visual intent: Teal side band, "MODULE 4" tag. Small rung icon: rung 3 lit, two job boxes joined by one arrow.
- Sources: none

Notes:
```
POINT: In this module your agent gets its fourth job, and for the first time one job hands its output to another.
Talk Track:
Your agent has three jobs now: the problem backlog, win/loss and the weekly run.
Each job has run on its own.
Today the win/loss job hands its driver log to a new job: the alternatives map.
That is rung 3: a hand-off between jobs.
The new skill for you is the rule at that hand-off.
What passes to the next job, and what stops and comes to you.
TRANSITION: First, why the map matters.
```

### Slide 4.2: Lost to whom?
- Layout: Blank
- Minutes: 2
- On-slide text: Headline: "Lost to whom?" Line: "Competitor documents age fast." Workflow strip: "Lost deals and buyer interviews, then a checked alternatives map."
- Visual intent: Headline in navy, "whom" in orange. One short line. A left-to-right strip: a deal card and an interview note, then a map with 4 tiles (competitor, substitute, workaround, do nothing). No numbers.
- Sources: N13 (Wynter, State of Competitive Intelligence in B2B SaaS, May 2026, primary; via `research/needs.md`) and W21 (DEV Community, 2026-02-10, verified weak). Independent of each other. No figure from either (B10)

Notes:
```
POINT: A competitor list ages fast, and it lists companies, not what lost buyers chose.
Talk Track:
Here is the workflow for this module.
A deal is lost. Somebody asks: lost to whom?
[ASK: "Where does your team's answer come from?" TAKE 1 ANSWER]
Often the answer comes from a competitor list, built a while ago.
A 2026 Wynter survey of B2B SaaS product marketers found that for about half of them, competitive work is a side job.
The same survey found that battlecards go stale fast.
A 2026 article, first published on a competitive analysis tool's site, says competitive documents built by hand age quickly.
And a competitor list has a blind spot.
It lists companies. It does not list what buyers do when they buy no one.
We found no published study on how often that happens. Your own deals will tell you.
At Larkspan, our case company, the Head of Product asks: "Which alternative must we beat in each segment? Is Rimecore growing?"
That is the question your agent answers today, from Larkspan's own deals and interviews.
No public sources. No competitor websites. Only what buyers did.
[IF ASKED FOR A NUMBER] The survey has figures. We keep them off the slide. The point is the blind spot, not the percentage.
TRANSITION: Here is what that blind spot looked like for one Pragmatic client.
```

### Slide 4.3: They built it themselves
- Layout: Blank
- Minutes: 3
- On-slide text: Headline: They built it themselves. Lines: Not on any competitor list. Track it as an alternative. Watch if the buyer comes back.
- Visual intent: Headline in large type, not styled as a quote (no quote marks: the client's words are not on record). Two simple tiles: "Built in-house" and "Came back for part of the need", joined by a curved return arrow. No logos, names or dates.
- Sources: Pragmatic client story, from Dan (OI-05, closed 2026-11-27; `modules/m4/example-oi-05.md`). Required example slot (Gate 1 decision f, Gate 2 decision 6)

Notes:
```
POINT: "Build it ourselves" is an alternative that a competitor list misses, and a buyer who builds can come back for part of the need.
Talk Track:
[REQUIRED EXAMPLE. TELL IT AS PRAGMATIC'S STORY, NEVER AS YOUR OWN. DO NOT NAME THE CLIENT. DO NOT ADD DATES, VALUES, PRODUCT NAMES OR PEOPLE]
This is a story from Pragmatic's own work with a client.
The client was a large global technology and consulting company. Pragmatic had worked with them for a long time.
The company was so large that it decided to build its own training. An internal training center of excellence.
Think about how that shows up on a competitor list.
Lost. To whom? To no competitor. They built it themselves.
Setting up the center took a long time. They worked hard to set norms.
Then they found a problem. Very different teams had very different needs. One center found it hard to meet them all.
So they came back to Pragmatic.
They asked for private classes for those teams, with Pragmatic's core classes and AI classes tailored to them.
In the end, a mix of both worked best: their own center, plus tailored classes.
[PAUSE]
Three lessons for your map.
One. "Build it ourselves" is an alternative. A competitor list misses it.
Two. It is not always the end. A buyer who builds, or who does nothing, can come back. Track them, with the evidence.
Three. The answer was not one or the other. Ask what the buyer kept, and what they still needed.
[ASK: "Which of your lost deals did the buyer build in-house, or do nothing?" TAKE 1 OR 2 ANSWERS]
TRANSITION: So a map needs more than one kind of alternative.
```

### Slide 4.4: Four kinds of alternative
- Layout: Blank
- Minutes: 1
- On-slide text: Competitor: bought a named rival. Substitute: bought outside the category. Workaround: built or changed a process. Do nothing: kept the current method.
- Visual intent: 4 tiles in a row, one icon each (rival logo shape, different product box, wrench, clipboard). "Do nothing" tile in orange.
- Sources: none (case `m4-alternatives-map.md` type table; spec glossary "alternatives map"). Hardware and internal PM examples are recorded gaps (`research/workflows.yaml` mr-wf-10 contexts)

Notes:
```
POINT: The map tracks four kinds of alternative, so the ones that are not companies get counted too.
Talk Track:
Your map has four types.
Competitor: the buyer bought a named rival.
Substitute: the buyer bought something outside the category that covers part of the need.
Workaround: the buyer built something, or changed a process. The training center was a workaround.
Do nothing: the buyer kept what they had, or stopped the project.
In hardware, do nothing often means keeping the installed product longer, a repair, or the distributor's own brand.
For an internal platform, the alternatives are team-built tools, spreadsheets and tools a team bought on its own.
We found no published source for these two settings. So they are examples, not findings.
At Larkspan, a substitute is the alarm built into a new refrigeration controller. You met it in lab 2.
TRANSITION: Let me add the map job in front of you.
```

### Slide 4.5: Live demo. Add the alternatives map job
- Layout: 1_prompt
- Minutes: 6
- On-slide text: LIVE DEMO. "Add the map job. Write a hand-off rule. Run the evidence pack." Running example: Larkspan Systems, Q2 and Q3 2027 lost deals. 6 MIN.
- Visual intent: Orange "LIVE DEMO" tag. Platform logo for the demo platform (Claude). Small flow: win/loss job, driver log, map job.
- Sources: cl-pj-01, cl-ui-09 (platform matrix, verified). Demo script in section 3

Notes:
```
POINT: Adding the map job takes two files and one hand-off rule, and the run reads the win/loss job's driver log.
Talk Track:
[SWITCH TO THE DEMO PLATFORM. FOLLOW THE DEMO SCRIPT IN SECTION 3, STEPS 1 TO 4]
Here is the agent after module 3. Brief v4 in the instructions. Eight files in knowledge.
I add two files: the alternatives map job card and the current map.
The map has four entries from last quarter, Q2. Each entry links to its deals and interviews.
Now the new part. One hand-off rule, from the win/loss job to the map job.
It goes in the brief, under "My rules", as rule 4. The job card says: map it only as "My rules" allow.
[TYPE THE DEMO RULE: "Lab 4 (draft): Pass only lost deals to the map. Won deals stay in the driver log." SAVE]
That is a draft rule, to show the shape. You write your own in the lab.
[NEW CHAT. UPLOAD THE EVIDENCE PACK. SEND BY MINUTE 2 OF THIS SLIDE AND TALK OVER THE RUN]
One file, four parts.
Part 1 is the driver log. The win/loss job wrote it. Q2 rows from lab 2, and Q3 rows coded quickly before quarter close.
That driver log is the hand-off. The map job reads it.
Parts 2 and 3 are the Q3 CRM export and the Q3 interviews. Part 4 is the problem backlog.
[IF THE RUN IS NOT DONE AT MINUTE 5, OPEN THE REHEARSAL OUTPUT AND MOVE ON. LET THE LIVE RUN FINISH IN THE BACKGROUND]
[WHEN THE RUN ENDS, OPEN THE OUTPUT]
TRANSITION: Here is how you read the map.
```

### Slide 4.6: Read the map: every entry traces to a buyer
- Layout: Blank
- Minutes: 2
- On-slide text: 1. Entry and type. 2. Counts per quarter, buyer interview or CRM only. 3. Evidence rows: deal ID and interview ID. 4. Change, with both periods. 5. Flag report: your decisions.
- Visual intent: A cropped, readable mock of one map row from the demo run: ALT-04 do nothing, with D-3103 / WL-3103 circled. Numbers 1 to 5 in orange circles.
- Sources: none (case `m4-alternatives-map.md` formats, `m4-evidence-pack.md`)

Notes:
```
POINT: You manage the map by reading each entry's evidence rows, its source type and its change, not by trusting the counts.
Talk Track:
[DEMO SCRIPT STEPS 5 TO 8. STAY ON THE SCREEN, THEN SHOW THIS SLIDE AS THE SUMMARY]
One. Each entry has a type: competitor, substitute, workaround or do nothing.
Two. Counts are lost deals, per quarter. Deals with a buyer interview and CRM-only deals stay apart.
Three. Evidence rows. Every entry links to a deal ID and an interview ID.
Here: do nothing, deal D-3103, interview WL-3103.
"For three cafes the paper log on the cooler door is free and the inspector accepts it."
Four. The change: new, growing, fading or no change. Each label names the two periods and the counts.
Five. The flag report. The decision column is blank. That is yours.
[DO NOT COMMENT ON ANY COUNT, ANY CHANGE OR ANY ENTRY BUT ALT-04. IF A LEARNER ASKS:] Good question. Hold it for your audit.
[SAVE THE DEMO OUTPUT FILE. YOU MAY NEED IT IN THE DEBRIEF]
TRANSITION: Now the idea behind the rule you just watched me write.
```

### Slide 4.7: Rung 3: one job hands work to the next
- Layout: Blank
- Minutes: 2
- On-slide text: Win/loss job, then driver log, then map job. Your hand-off rule says: what passes to the map; what stops and goes to your flag report. It lives in your brief, under "My rules".
- Visual intent: Ladder graphic, rung 3 lit. Two job boxes with the driver log between them. A small gate icon on the arrow, labeled "your rule". Two exits from the gate: "passes" (teal) and "flag report" (orange).
- Sources: none (spec `autonomy_ladder` rung 3; glossary "hand-off rule"; module 4 objective m4-o2)

Notes:
```
POINT: At rung 3 one job's output is the next job's input, and the hand-off rule decides what passes and what stops.
Talk Track:
You have written hand-off rules since module 1. They told the agent when to stop and hand an item to you.
Now there is a second place for a rule: between two jobs.
The map job trusts what the win/loss job passes to it.
If something wrong passes, the map counts it, links it and reports it with full confidence.
So the rule sits at the seam between the jobs.
It answers two questions. What may pass to the map? What must stop and come to you?
The shape is simple: "When this, pass that to the map. When this, stop and send it to the flag report."
In the demo I wrote: pass only lost deals. Won deals stay in the driver log.
You write your own in step 2 of the lab, and you fix it after your audit in step 6.
It lives in your brief, under "My rules", as rule 4.
TRANSITION: Can a second agent do the map job? On some platforms, as a stretch.
```

### Slide 4.8: Second agent: a stretch, where verified
- Layout: Blank
- Minutes: 1
- On-slide text: Core path, all 4 platforms: one agent, two jobs, one hand-off rule. Stretch, Claude and ChatGPT: a second project reads the first job's output file. Not in this course: Copilot, Gemini.
- Visual intent: Two rows. Row 1: 4 platform logos, one agent box with two jobs. Row 2: Claude and ChatGPT logos, two agent boxes with a file passed between them ("stretch"); Copilot and Gemini logos grayed. No setup screens.
- Sources: `research/stretch-verification-2026-11.md` (2026-11-27): manual file hand-off verified by existing rows on Claude (cl-pj-01, cl-fo-06, cl-ui-09) and ChatGPT (cg-01, cg-ui-09; cg-08 partly verified); automatic hand-off not verified on any platform; Copilot and Gemini core path (`stretch_scope`). Spec `stretch_scope.slides` (name the gap once)

Notes:
```
POINT: The core path keeps both jobs in one agent, and a second agent is a stretch only where the course checked it.
Talk Track:
In this lab, both jobs live in one agent. The hand-off happens inside it.
Some teams want a separate agent for each job. That is a stretch step, on two cards.
On Claude and ChatGPT, you can build a second project for the map job.
You download the driver log from the first project and upload it to the second.
The file you pass is the hand-off. Your rule still decides what is in it.
The course team checked the vendor docs. A hands-on test is still open, and the card says so.
No platform documents one agent calling another automatically for this setup. So we do not teach that.
Copilot and Gemini stay on the core path in this course.
[DO NOT SHOW SETUP SCREENS. THE CLAUDE AND CHATGPT CARDS HAVE THE STEPS]
TRANSITION: Here is your lab.
```

### Slide 4.9: Lab 4 brief
- Layout: Activity
- Minutes: 2
- On-slide text: ACTIVITY. Lab 4: Add the alternatives map job. Goal: Map what buyers chose, from your own deals. Key actions: Add the job. Write a hand-off rule. Run the evidence pack. Decide each flag. Audit 3 entries. Fix your rule. Footer: "Full steps: your step card in the workbook (Pragmatic Learning Hub)."
- Visual intent: Orange "ACTIVITY" band. Goal at the top. 6 short key actions in large type. Workbook pointer in the footer. Nothing else on the slide.
- Sources: none

Notes:
```
POINT: In lab 4 you add the map job, write the hand-off rule from win/loss, and manage the map by flags and audit.
Talk Track:
The goal of this activity is to extend your agent to keep an alternatives map from your own deal evidence.
The core message: map what buyers chose, not what competitors announce. Every entry must trace back to a buyer or a deal.
These are the key actions. The full steps are on your step card in the workbook.
You downloaded the workbook from the Pragmatic Learning Hub. Open your platform's card now.
[WALK THE KEY ACTIONS IN ONE LINE EACH. DO NOT READ THE CARD ALOUD]
On your own work: your driver log from module 2 is already in your agent. Add a CRM export of decided deals with a competitor field, and your interview notes.
Otherwise use the Larkspan evidence pack. Both paths use the same steps.
Record your rule, your decisions and your audit on the lab 4 record sheet in your kit. That is your evidence.
TRANSITION: Here is what done looks like.
```

### Slide 4.10: Lab 4: done when
- Layout: Activity
- Minutes: 1
- On-slide text: ACTIVITY. Done when: Every entry shows its source type and a deal or interview ID. Each growing or fading label names both periods and counts. Each flag has your decision. You audited 3 entries and fixed your rule. Orange box: "Audit before you approve."
- Visual intent: Orange "ACTIVITY" band. Success check as 4 short lines on the left. Orange box on the right.
- Sources: none (spec module 4 `success_check`; spec `planted_error_fade` module 4)

Notes:
```
POINT: The success check names the outputs and your manager actions, and the hint reminds you to audit before you approve.
Talk Track:
The goal of this activity is to know what done looks like before you start.
Every map entry shows its source type, and links to a deal ID or an interview ID.
Each "growing" or "fading" label names the two periods and the counts in each.
Each flag has your decision. You audited 3 entries, the ones that moved first, and fixed your hand-off rule.
[POINT TO THE ORANGE BOX]
Audit before you approve.
TRANSITION: One more thing before the rooms open: what is in a deal record.
```

### Slide 4.11: Lab 4: data safety
- Layout: Activity
- Minutes: 1
- On-slide text: ACTIVITY. Data safety box (standard text): "Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss." New line: "Deal records hold customer names, deal values and competitor prices."
- Visual intent: Orange "ACTIVITY" band. The standard data safety box, the same box as the step cards. The new line below it in orange.
- Sources: none (spec `data_safety_note`; module 4 `data_safety`)

Notes:
```
POINT: Deal records hold customer names, values and competitor prices, so they go only into an approved tool, and the map keeps them for a long time.
Talk Track:
Same rule as every lab. Approved tool only.
One thing is new. A CRM export holds customer names, deal values and sometimes competitor prices.
Interview notes can hold what a buyer said in confidence.
Check what your company allows before you upload them.
And your map and your driver log keep that evidence, quarter after quarter. Decide what they may keep, and for how long.
Breakout rooms are by platform. Build and save your own agent. Share your screen only when someone is stuck.
Agent lost or behind? Rebuild it from kit-m4 first. It takes about 5 minutes.
TRANSITION: [OPEN BREAKOUT ROOMS BY PLATFORM. START THE TIMER: 25 MINUTES]
```

### Slide 4.12: Lab 4: Add the alternatives map job
- Layout: Activity
- Minutes: 25
- On-slide text: ACTIVITY. 25 MIN. Time guide: 0 to 2: add 2 files. 2 to 5: write rule 4. 5 to 11: run. 11 to 14: decide flags. 14 to 21: audit 3 entries. 21 to 25: fix rule 4. "Build and save your own agent. Share your screen only when someone is stuck."
- Visual intent: Orange band. A timeline bar with the 6 blocks. Room by platform shown as 4 small tiles.
- Sources: none

Notes:
```
POINT: Learners add the map job, write and fix the hand-off rule, and audit 3 entries, from their step card, on own or case data.
Talk Track:
The goal of this activity is to run one full turn of the manager loop on your agent's first hand-off.
[VISIT EACH ROOM IN TURN. START WITH COPILOT, THEN GEMINI, THEN CHATGPT, THEN CLAUDE]
[AT MINUTE 2: ANYONE WHO HAS NOT ADDED THE 2 FILES GETS HELP FIRST]
[AT MINUTE 5: "Send the evidence pack now, even if your rule is a draft."]
[AT MINUTE 11: "Decide your flags now. Then start the audit."]
[AT MINUTE 14: "Start your audit. Take every entry labeled growing or fading. Add random picks up to 3. Open every evidence row they list."]
[AT MINUTE 21: "Fix your rule now, even if your audit is not done. The rerun is in the debrief."]
[COMMON FAILURES AND RECOVERY: SEE SECTION 9]
[DO NOT REVEAL THE ERROR. IF A LEARNER ASKS "IS THIS IT?", ASK: "Which evidence rows did you open? What do they say?"]
TRANSITION: [CLOSE ROOMS AT MINUTE 25] Bring your record sheet. Keep your agent open.
```

### Slide 4.13: Rerun with your fixed rule
- Layout: debrief
- Minutes: 3
- On-slide text: DEBRIEF. 3 MIN. New chat. Send the evidence pack with "Run the alternatives map job". While it runs: Which alternative must you beat in each segment? What is your evidence?
- Visual intent: Navy "DEBRIEF" band. Timer 3 MIN. One-line instruction. 2 questions below.
- Sources: none (spec module 4 debrief arc; objective m4-o4)

Notes:
```
POINT: The rerun tests the fixed hand-off rule, and the PM decides which alternative to beat in each segment.
Talk Track:
Rerun now, on your fixed brief.
New chat. The evidence pack. Same prompt.
[START A 3-MINUTE TIMER]
While it runs, look at your map from the lab.
Which alternative must your team beat in each segment? What is your evidence: which deals, which interviews, which quarters?
Write one segment in section 5 of your record sheet.
And what does it mean for positioning, pricing or the roadmap? Scoring and weighting belong to the Product Strategy and Planning course. Today, name it and back it.
[AFTER 1 MINUTE, TAKE 2 ANSWERS]
[IF A LEARNER NAMES A COMPETITOR FROM COUNTS ALONE:] Which interviews say so? Read one buyer quote.
[IF A LEARNER'S RERUN IS NOT DONE AT 3 MINUTES:] Keep it running. We read the result together next.
TRANSITION: So what did your audit find?
```

### Slide 4.14: Audit reveal: lost to whom, really?
- Layout: debrief
- Minutes: 2
- On-slide text: DEBRIEF. Which check or audit found the error? (Reveal after answers:) D-3108: CRM says Rimecore. Buyer: "we kept the spreadsheet and the clipboard on the walk-in door." Before the fix: Rimecore 2 to 3, "growing". After: 2 to 2. Do nothing: 2 to 4. Food service: do nothing is top.
- Visual intent: Navy band. 1 question. On click: the D-3108 CRM row and the WL-3108 quote side by side, then the Rimecore row before (2, 3, growing) and after (2, 2, no change), then the do nothing row (2, 4, growing).
- Sources: none (case `planted-errors.md` lab 4, `expected-results.md` lab 4)

Notes:
```
POINT: The agent filled a blank cell from the CRM competitor field, so Rimecore looked like it was growing until the audit read the interview.
Talk Track:
[ASK THE QUESTION. TAKE 2 OR 3 ANSWERS]
[REVEAL]
Here is the planted error. Deal D-3108, Hobnail Burger Co, Food service, lost in Q3.
In the driver log, "Alternative chosen" is blank.
The CRM competitor field says Rimecore.
The interview, WL-3108, says this: "In the end we didn't buy anything; we kept the spreadsheet and the clipboard on the walk-in door."
The agent filled the blank from the CRM. So Rimecore went from 2 deals in Q2 to 3 in Q3. "Growing."
The link check passed. The entry linked D-3108 and WL-3108. The source type said "buyer interview".
Every check passed. Only reading the interview found it.
You all audited the Rimecore entry, because it was labeled growing. Audit what moved first: a change is what you will act on.
After your fix, D-3108 moves to do nothing.
Rimecore: 2 in Q2, 2 in Q3. No change.
Do nothing: 2 in Q2, 4 in Q3. Growing.
The flag report names the mismatch: the CRM says Rimecore, the buyer kept the spreadsheet.
The case PM's decision: accept the buyer's answer, and tell sales ops to fix the CRM field.
One more trap. D-3102 also had a blank cell. But the CRM and the interview agree: Vantafrost. A blank cell alone is not the clue. The interview is.
So the alternative to beat in Food service is not Rimecore. It is do nothing: paper logs and spreadsheets. Next is the controller alarm substitute.
The fix the case PM wrote: "The alternative chosen comes from the buyer's interview. If the driver log cell is blank, read the interview. Never fill it from the CRM competitor field. If the CRM field and the buyer differ, send the deal to the flag report."
[IF NO AGENT IN THE ROOM MADE THE ERROR, SHOW THE SAVED DEMO OUTPUT]
TRANSITION: Did your rule work on deals you have not seen?
```

### Slide 4.15: Check sample: deals you have not seen
- Layout: debrief
- Minutes: 1
- On-slide text: DEBRIEF. Check sample: 5 October deals, fixed brief. D-4102: controller alarms, not Vantafrost. Flagged. D-4104: CRM only. Run it after class (about 5 minutes).
- Visual intent: Navy band. A screenshot of the instructor's saved check sample result, with the 3 pass items circled. Small card image with "after class".
- Sources: none (case `m4-check-sample.md`, `expected-results.md` lab 4 second sample)

Notes:
```
POINT: Deals the learner has not seen show if the fixed hand-off rule works, and learners run them after class.
Talk Track:
[SHOW THE SAVED CHECK SAMPLE RESULT FROM THE TUNED INSTRUCTOR PROJECT. SEE SECTION 3, "BEFORE CLASS"]
Five lost deals from October, run on the fixed brief.
D-4102, a Food service deal. The CRM says Vantafrost. The driver log cell is blank.
The buyer priced Vantafrost, then bought nothing from either of us. Their refrigeration contractor added alarm texts to the controllers.
The fixed agent reads the interview. D-4102 goes under controller alarms, the substitute. And the flag report lists it.
D-4104 has no interview. It shows as CRM only.
Run it yourself after class. About 5 minutes. The pass condition is at the end of your step card.
TRANSITION: So what do you do on Monday?
```

### Slide 4.16: What you do Monday
- Layout: Blank
- Minutes: 1
- On-slide text: "List the top 3 alternatives your last 10 lost deals chose. How many are named competitors?"
- Visual intent: One line, large type. Calendar icon with "Monday".
- Sources: none (spec module 4 `talk_track_slots.monday_close`)

Notes:
```
POINT: The first real use of the map is one look at what your last lost deals chose.
Talk Track:
On Monday, pull your last 10 lost deals.
For each one, find what the buyer chose. Use the interview where you have one, not the CRM field.
List the top 3 alternatives. How many are named competitors?
If do nothing or a workaround is in your top 3, your competitor list is missing it.
TRANSITION: Last step: save your map and driver log so module 5 can read them.
```

### Slide 4.17: Save your map and driver log
- Layout: Activity
- Minutes: 1
- On-slide text: ACTIVITY. 1 MIN. 1. Download the map and the driver log from your rerun. 2. Replace `alternatives-map` and `driver-log` in your agent's knowledge. Your card has the steps for your platform.
- Visual intent: Orange band. Two numbered steps, large. Small platform row: Claude, ChatGPT, Copilot, Gemini.
- Sources: cl-pj-01, cg-01, mb-02, gm-01 (platform matrix); vendor docs on the cards

Notes:
```
POINT: Saving the updated map and driver log to the agent's knowledge lets module 5 answer from them.
Talk Track:
The goal of this activity is to save your two updated logs. Module 5 reads both.
Take them from your rerun, the one with your fixed rule. Not the lab run.
Download the map and the driver log. Replace the old alternatives-map and driver-log in your agent's knowledge.
Gemini: replace the files in the skill. If that fails, upload the whole skill again.
Copilot without a license: keep both files on your computer. You paste them in chat next time.
If your rerun did not finish, kit-m5 has both files after the fix. Load those instead.
kit-m5 also holds the case PM's decisions: D-3108 as do nothing, and do nothing as the alternative to beat in Food service.
TRANSITION: [MOVE TO THE BREAK, THEN MODULE 5]
```

## 3. Demo script

Platform: Claude (Project). Before class:

1. Have the project "Market Evidence Agent" in its state after module 3 (brief v4 in the instructions; 8 files in knowledge). Use `modules/m3/kit/kit-m4/` if the module 3 demo project changed.
2. Check that **Code execution and file creation** (or **Create and edit files**) is on.
3. Do one rehearsal run on the case files, with the demo rule. Time the run. Save the rehearsal output and screenshots in your instructor folder.
4. Build a second project, "Market Evidence Agent (tuned)", from `kit/kit-m5/` (brief v5 and 10 files). In a new chat, send `m4-check-sample.md` with "Run the alternatives map job". Save the result and a screenshot for slide 4.15. Check it against the pass condition on the cards.
5. Keep a ChatGPT Project in the state after module 3 as the backup.

| Step | Instructor does | Screen shows | If it fails |
| --- | --- | --- | --- |
| 1 | Open **Projects**, then "Market Evidence Agent" | Brief v4 in the instructions. 8 files in project knowledge | Rebuild from `kit-m4` in about 5 minutes, or switch to the ChatGPT backup. Say: "This is what kit-m4 is for." |
| 2 | Select **+** in project knowledge. Add `job-card-alternatives-map.md` and `alternatives-map.md` from `kit/lab-4/` | 10 files in project knowledge | Paste both texts into the chat with the run in step 4 |
| 3 | Open the project instructions. Under "My rules", type: "4. Lab 4 (draft): Pass only lost deals to the map. Won deals stay in the driver log." Select **Save instructions** | The rule as item 4 under "My rules" | If the save fails, say the rule in the chat message with the run in step 4 |
| 4 | Start a new chat in the project. Upload `m4-evidence-pack.md`. Send "Run the alternatives map job" | The updated map with 4 entries (ALT-01 to ALT-04), Q2 and Q3 counts, source types and evidence rows. Counts by segment. A flag report. What changed. The updated driver log. A downloadable file, or the full tables in one message | If no file: say "Rule 7 in the brief asks for the full tables in one message." If the run fails: switch to the ChatGPT backup. If both fail, or the run is not done at minute 5 of slide 4.5: show the rehearsal output |
| 5 | Point to entry ALT-04 (do nothing), evidence row D-3103 / WL-3103 | Type "Do nothing". D-3103, Food service, quote "For three cafes the paper log on the cooler door is free and the inspector accepts it." | If the row differs, say: "That is what an audit is for." Do not fix it live |
| 6 | Point to the what changed table | Columns: Entry, Previous period count, This period count, Periods compared, Change. "Q2 2027 vs Q3 2027" in the periods column | If the format differs, say: "The map file sets the format. A different format is an audit finding." |
| 7 | Point to the flag report | Flags with a blank PM decision column. Likely: do nothing is the top alternative in Food service; "Incumbent loggers" (D-3109, CRM only) is not a map entry | If a flag is missing, say: "Hand-off rules are not perfect. That is why you audit." |
| 8 | Download the output file and save it | The file in your instructor folder | Use the rehearsal output in the debrief |

Do not comment on the Rimecore count, on its change, on D-3108 or on D-3102 on screen. The demo runs on brief v4 with a neutral draft rule, so the planted error may show (Rimecore Q2 2, Q3 3, "growing"). That is the lab's planted error (module 1 decision D5 pattern; D15).

## 4. Lab brief

- Goal: Extend the course agent to keep an alternatives map from the team's own evaluator and deal evidence.
- Core message: Map what buyers chose, not what competitors announce. Every entry must trace back to a buyer or a deal.
- PM decision: Which alternatives the team must beat in each segment, and what goes to positioning, pricing and the roadmap. Scoring and weighting stay with the Product Strategy and Planning course.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Module 4 point: deal records hold customer names, deal values and competitor prices. The map and the driver log keep evidence quarter after quarter. Decide what they may keep and for how long.
- Setup: Zoom breakout rooms by platform, 3 to 5 learners. In person: tables by platform. Each card starts: "Build and save your own agent. Share your screen only when someone is stuck."
- Inputs: Own work: the module 2 driver log (already in the agent), a CRM export of decided deals with a competitor field, and interview notes, from an approved tool. Case: `kit/lab-4/` (job card, current map), `m4-evidence-pack.md` (run), `m4-check-sample.md` (after class). Files this lab: 4 (2 to the agent, 2 in chat). No stretch file.
- Planted error warning: Hint. "Audit before you approve."
- Success check: Every map entry shows its source type and links to a deal ID or interview ID. Each "growing" or "fading" label names the two periods and the counts. Each flag has your decision. You audited 3 entries and fixed the hand-off rule.
- Learner evidence: The hand-off rule as written and as fixed. Audit findings for 3 traced entries. Flag report decisions. The alternative to beat in one segment, with its evidence. Recorded on `lab-4-record-sheet.md`.

## 5. Step cards

All four cards have the same 6 core steps. Saving is in each card header, not a step. The debrief rerun is on each card under the steps. Learners use the files in `kit/lab-4/` and the run file from the case folder. Copilot learners use the `.txt` copies. No fast-start card in module 4 (module 1 only).

### Card: Claude
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Market Evidence Agent" from module 3. Lost or behind? Rebuild it from `kit-m4` first.
- Saves: **Save instructions** saves the instructions. Files save when you add them. Chats save as you go.
- Check date and vendor doc: Core steps use the same screen names as the module 3 card (checked 2026-11-27 by the module 2 and 3 verifiers). Claude Help Center, "How can I create and manage projects?" (https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects, page metadata 2026-11-06, platform matrix cl-ui-09, checked 2026-11-26). "Create and edit files with Claude" (https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude, page metadata 2026-11-24, cl-ui-10). Stretch: `research/stretch-verification-2026-11.md` (Claude manual file hand-off, verified by rows cl-pj-01, cl-fo-06, cl-ui-09; checked 2026-11-27). Module 4 verifier rechecks.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Deal records hold customer names, deal values and competitor prices.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-alternatives-map` and `alternatives-map` to project knowledge with **+**. |
| 2 | Write rule 4 under "My rules" in the project instructions: one hand-off rule from win/loss to the map. |
| 3 | In a new chat, send the evidence pack with the prompt "Run the alternatives map job". |
| 4 | Write your decision for each flag report item on your record sheet. |
| 5 | Audit 3 map entries, growing or fading ones first, against the interviews and deal records, with your record sheet. |
| 6 | Fix rule 4 under "My rules" for what your audit found. |

**Debrief rerun:** In a new chat, send the evidence pack with the prompt "Run the alternatives map job".

Notes: No file in the answer? Check that **Code execution and file creation** (or **Create and edit files**) is on in **Settings**, then **Capabilities**. Team or Enterprise: ask your owner. Your project opens as one conversation with a Library? Tell the instructor.

**Start here with sample data:** Add: `job-card-alternatives-map.md`, `alternatives-map.md`. Run: `m4-evidence-pack.md`. Own work: replace `alternatives-map` with your current map, or an empty map with the same types and formats. Send your CRM export of decided deals with a competitor field, and your interview notes. Your driver log is already in the agent.

**Pass condition (second sample, run after class):** On your fixed agent, after the log save card. New chat. Send `m4-check-sample.md` with "Run the alternatives map job". Pass if: (1) D-4102 is under controller alarms. (2) The flag report lists D-4102. (3) D-4104 shows as CRM only. (4) Every entry shows its source type and links to a deal ID or interview ID. (5) Each "growing" or "fading" label names the two periods and the counts.

**Done early:** Fill section 5 of your record sheet for a second segment. Or run the job on your own lost deals.

**Stretch (vendor doc checked, not yet tested):**
- Second agent, manual hand-off. After class. Vendor doc checked 2026-11-27. Not yet tested by the course team. Free plan: 5 projects at most.
  1. In **Projects**, select **+ New Project**. Name it "Alternatives Map Agent".
  2. Paste your brief, with your fixed rule 4, into **Set project instructions**.
  3. Add `job-card-alternatives-map` and the lab 4 `alternatives-map` to project knowledge with **+**.
  4. In your first project, send the evidence pack with "Run the win/loss job on the Q3 deals".
  5. Download that driver log file. No file? Copy the driver log table into a text file.
  6. In a new chat in the second project, send the driver log file with "Run the alternatives map job".
  Pass: each map entry links to a deal ID or interview ID.
  Note: the second project sees only the file you send. That file is the hand-off. It has no interviews, CRM export or backlog. So your rule 4 interview check runs in the first project, and the map has no backlog links. Do not save the first project's driver log back to your agent. The win/loss job recounts its match rates.
- The schedule stretch step is not on this card in module 4.

### Card: ChatGPT
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Market Evidence Agent" from module 3. Plan: Go or Plus or higher. Lost or behind? Rebuild it from `kit-m4` first.
- Saves: As you go.
- Check date and vendor doc: Core steps use the same screen names as the module 3 card (checked 2026-11-27). OpenAI Help Center, "Projects in ChatGPT" (https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt, "Updated: 19 hours ago" when seen 2026-11-27, about 2026-11-26, cg-ui-09; new project path changed to **+** next to **Projects**, then **Create project**). "Uploading files and audio to ChatGPT" (https://help-lb.openai.com/en/articles/8555545-uploading-files-and-audio-and-video-in-chatgpt, about 2026-11-26, cg-03) for **+** and **Add photos & files**. Stretch: `research/stretch-verification-2026-11.md` (ChatGPT manual file hand-off, rows cg-01 and cg-ui-09 verified; file download cg-08 partly verified: OpenAI Academy, "Working with files", last updated 2026-09-04; checked 2026-11-27). Module 4 verifier rechecks.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Deal records hold customer names, deal values and competitor prices.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-alternatives-map` and `alternatives-map` to the project's files. |
| 2 | Write rule 4 under "My rules" in **Project settings**: one hand-off rule from win/loss to the map. |
| 3 | In a new chat, send the evidence pack with the prompt "Run the alternatives map job". |
| 4 | Write your decision for each flag report item on your record sheet. |
| 5 | Audit 3 map entries, growing or fading ones first, against the interviews and deal records, with your record sheet. |
| 6 | Fix rule 4 under "My rules" for what your audit found. |

**Debrief rerun:** In a new chat, send the evidence pack with the prompt "Run the alternatives map job".

Notes: **Project settings** is in the **•••** menu of the project. No file in the answer? The brief asks for the full tables in one message. That is fine.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run after class):** Same as the Claude card.

**Done early:** Same as the Claude card.

**Stretch (vendor doc checked, not yet tested):**
- Second agent, manual hand-off. After class. Vendor doc checked 2026-11-27. Not yet tested by the course team.
  1. In the sidebar, select **+** next to **Projects**. Name it "Alternatives Map Agent", then select **Create project**.
  2. In **Project settings** (**•••** menu), paste your brief, with your fixed rule 4, into **Instructions**.
  3. Add `job-card-alternatives-map` and the lab 4 `alternatives-map` to the project's files.
  4. In your first project, send the evidence pack with "Run the win/loss job on the Q3 deals".
  5. Download that driver log file. No file? Copy the driver log table into a text file.
  6. In a new chat in the second project, attach the file with **+**, then **Add photos & files**. Send "Run the alternatives map job".
  Pass and note: same as the Claude card.
- The schedule stretch step is not available on this platform in this course. A scheduled task in a project cannot read project files.

### Card: Copilot agent builder
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the agent "Market Evidence Agent" from module 3. To open it: **All agents**, then **...** next to it, then **Edit**. Lost or behind? Rebuild it from `kit-m4` first.
- Saves: **Update** after each change.
- Check date and vendor doc: Core steps use the same screen names as the module 3 card (checked 2026-11-27). Microsoft Learn, "Add knowledge sources" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge, "Last updated on 2026-11-16", mb-ui-12). Microsoft Support, "Add content to Microsoft 365 Copilot Chat prompts" (https://support.microsoft.com/en-US/Microsoft-365-Copilot/add-content-to-microsoft-365-copilot-chat-prompts, ms.date 2026-11-18, mb-ui-14, partly verified). Code interpreter file output, session only (mb-11, "Last updated on 2026-09-28"). Module 4 verifier rechecks.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Deal records hold customer names, deal values and competitor prices.

| Step | Do this |
| --- | --- |
| 1 | On the **Configure** tab, add `job-card-alternatives-map.txt` and `alternatives-map.txt` with **Upload**. |
| 2 | Write rule 4 under "My rules" in **Instructions**: one hand-off rule from win/loss to the map. |
| 3 | In a new chat, send the evidence pack with the prompt "Run the alternatives map job". |
| 4 | Write your decision for each flag report item on your record sheet. |
| 5 | Audit 3 map entries, growing or fading ones first, against the interviews and deal records, with your record sheet. |
| 6 | Fix rule 4 under "My rules" in **Instructions** for what your audit found. |

**Debrief rerun:** In a new chat, send the evidence pack with the prompt "Run the alternatives map job".

Notes: Use the `.txt` copies. Copilot does not list `.md` as a knowledge file type. To send the evidence pack, upload it, or paste the text. Download any file the agent makes in the same session. Copilot keeps it for that session only.

**No Copilot license or billing?** Your agent cannot read Knowledge files. Do this instead:
1. Paste all of `copilot-fallback-instructions-m4.txt` into **Instructions**. It replaces the module 3 text.
2. Skip card step 1. You cannot add knowledge files. Your own rules differ from the kit? Put yours under "My rules".
3. At step 3, send the evidence pack in one message. It holds the driver log and the backlog too.
4. Debrief rerun: in the new chat, send the evidence pack again.
Upload the file, or paste the text. The paste fails? Send it in 2 parts. Split it at "## Part 3".
The fallback agent does one job at a time. Keep the map and the driver log from the rerun on your computer.

**Start here with sample data:** Add: `job-card-alternatives-map.txt`, `alternatives-map.txt`. Run: `m4-evidence-pack.md`. Own work: as on the Claude card.

**Pass condition (second sample, run after class):** Same as the Claude card. Upload `m4-check-sample.md`, or paste the text.

**Done early:** Same as the Claude card.

**Stretch:**
- The schedule and second-agent stretch steps are not available on this platform in this course.

### Card: Gemini
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the skill "market-evidence-agent" from module 3. Find it in **Customize**, then **Skills**. Click it to edit. This is a Gemini skill. Gems are now skills. Lost or behind? Rebuild it from `kit-m4` first.
- Saves: **Save** after each change.
- Check date and vendor doc: Core steps use the same screen names as the module 3 card (checked 2026-11-27). Gemini Apps Help, skills page (https://support.google.com/gemini?p=pn_skills, page shows no date, gm-ui-10; module 1 decision D3 accepts it with a check date). Google blog, "Let skills in Gemini tackle your most repetitive tasks" (https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/, 2026-09-30) for **/**. The Help page names **Add files** for an existing skill. Module 4 verifier rechecks.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Deal records hold customer names, deal values and competitor prices.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-alternatives-map` and `alternatives-map` to your skill with **Add files**. |
| 2 | Write rule 4 under "My rules" in the skill **Instructions**: one hand-off rule from win/loss to the map. |
| 3 | In a new chat, send the evidence pack with "/market-evidence-agent Run the alternatives map job". |
| 4 | Write your decision for each flag report item on your record sheet. |
| 5 | Audit 3 map entries, growing or fading ones first, against the interviews and deal records, with your record sheet. |
| 6 | Fix rule 4 under "My rules" in the skill **Instructions** for what your audit found. |

**Debrief rerun:** In a new chat, send the evidence pack with "/market-evidence-agent Run the alternatives map job".

Notes: Type **/** (or **@**) in the chat and pick your skill from the list. If adding files to the skill fails, upload the whole skill again with all its files. If a chat upload fails, paste the text. Do not turn on Canvas or Deep Research.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run after class):** Same as the Claude card. Use the prompt "/market-evidence-agent Run the alternatives map job".

**Done early:** Same as the Claude card.

**Stretch:**
- The schedule and second-agent stretch steps are not available on this platform in this course.

## 6. Debrief

- Questions: Which alternative must you beat in each segment, and what is your evidence? Which check or audit found the error? Where did the map's answer for each deal come from? What does your fixed hand-off rule stop?
- Rerun (3 minutes): new chat, the evidence pack, fixed brief. While it runs, learners write the alternative to beat in one segment in section 5 of the record sheet.
- Error reveal (record ids): D-3108 (Hobnail Burger Co, Food service, lost Q3 2027). Part 1 driver log: "Alternative chosen" is blank; buyer quote "Rimecore's demo had fewer alerts, I'll give them that." Part 2 CRM export: crm_competitor "Rimecore". Part 3, WL-3108 (2027-09-15): "In the end we didn't buy anything; we kept the spreadsheet and the clipboard on the walk-in door." The agent fills the blank from the CRM field. Rimecore shows Q2 2, Q3 3, "growing". Do nothing shows 3. The link check passes: the Rimecore entry links D-3108 and WL-3108, source type "buyer interview". Decoy: D-3102 is also blank, but the CRM and WL-3102 agree (Vantafrost).
- Fix the learner adds (`case/planted-errors.md`, lab 4): "The alternative chosen comes from the buyer's interview. If the driver log cell is blank, read the interview. Never fill it from the CRM competitor field. If the CRM field and the buyer differ, send the deal to the flag report."
- Debrief check (instructor only, after the rerun; `case/expected-results.md` lab 4): D-3108 is under ALT-04 do nothing. Rimecore shows 2 in Q3 and "no change". The flag report lists the D-3108 mismatch. Every entry shows its source type. Each "growing" or "fading" label names Q2 2027 vs Q3 2027. Map after the fix (lost deals with a buyer interview): ALT-01 Rimecore Q2 2, Q3 2 (D-3101 Distribution, D-3105 Pharmacy and lab), no change. ALT-02 Vantafrost 1, 1 (D-3102 Distribution), no change. ALT-03 controller alarms 1, 0, fading (low counts, the PM judges). ALT-04 do nothing 2, 4 (D-3103, D-3106, D-3108 Food service; D-3107 Pharmacy and lab), growing. CRM only, kept apart: Q2 3, Q3 1 (D-3109, "Incumbent loggers", do nothing). By segment, Q3: Food service do nothing 3 (top); Pharmacy and lab Rimecore 1, do nothing 1; Distribution Rimecore 1, Vantafrost 1.
- Flag report after the fix: (1) D-3108: CRM competitor (Rimecore) and the buyer's answer (kept the spreadsheet) differ. Case PM decision: accept the buyer's answer, tell sales ops to fix the CRM field. (2) Do nothing is the top alternative in Food service. Pharmacy and lab is a tie (a flag there is fine). (3) Optional: "Incumbent loggers" (D-3109, CRM only) is not a map entry name. Mapping it to do nothing, CRM only, is correct.
- Which alternative to beat (case PM, Food service): do nothing, paper logs and spreadsheets (D-3103, D-3106, D-3108; Q2 D-2205). Next is the substitute, controller alarms (D-2209). Accept any segment a learner backs with deal and interview IDs and counts per quarter. Scoring and weighting stay with the Product Strategy and Planning course.
- Check sample (1 minute, instructor shows the tuned project result; learners run it after class, about 5 minutes; `case/expected-results.md` lab 4 second sample): October counts: Rimecore 1 (D-4101), Vantafrost 1 (D-4105), controller alarms 1 (D-4102), do nothing 1 (D-4103), CRM only 1 (D-4104, Vantafrost). Pass (the same 5 items as the card): (1) D-4102 is under controller alarms, not Vantafrost. (2) The flag report lists D-4102 (CRM Vantafrost, buyer bought no sensor system). (3) D-4104 is shown as CRM only. Items 1 to 3 are the `expected-results.md` pass condition. (4) and (5) are the spec quality checks.
- What you do Monday: List the top 3 alternatives your last 10 lost deals chose. How many are named competitors?
- Log save card:

| Platform | 1. Download | 2. Replace in the agent |
| --- | --- | --- |
| Claude | Download the map and the driver log from your debrief rerun | In project knowledge, delete the old `alternatives-map` and `driver-log`. Add the new files with **+** |
| ChatGPT | Download the map and the driver log from your debrief rerun | Open each old file in the project sources list. Delete it. Add the new files |
| Copilot | Download the map and the driver log from your debrief rerun, in the same session | On **Configure**, choose the **X** next to each old file, then **Remove**. **Upload** the new files. Select **Update** |
| Copilot, no license | Download or copy the map and the driver log from your debrief rerun | Keep them on your computer. Paste them in chat at the next run |
| Gemini | Download the map and the driver log from your debrief rerun | In your skill, **More**, then **Replace file**, for each file. Select **Save**. If that fails, upload the whole skill again with the new files |

Rename the new files `alternatives-map` and `driver-log` before you add them. Use the debrief rerun, not the lab run. If you have no file, use `kit-m5/alternatives-map.md` and `kit-m5/driver-log.md`. The output is one file? Ask: "Give the map and the driver log as two separate files."

## 7. LD spec

| Field | Value |
| --- | --- |
| Objective | Extend the Market Evidence Agent with an alternatives map job that reads the win/loss job's driver log. Write a hand-off rule between the two jobs, decide each flag, trace 3 map entries (growing or fading first) to their interviews and deal records, fix the rule, and choose the alternative to beat in one segment with its evidence (m4-o1 to m4-o4) |
| Timing | Lab 25 minutes. Debrief 8 (rerun 3, reveal 2, check sample shown 1, Monday 1, log save 1). Lab brief before it: 4 minutes (3 short slides; full steps on the step cards in the workbook). Same in full day and half days. Check sample after class: about 5 minutes |
| Setup (Zoom) | Breakout rooms by platform (Claude, ChatGPT, Copilot, Gemini), 3 to 5 learners each. Learners keep their own screen. Share only when stuck. Instructor visits rooms in turn, Copilot first |
| Setup (in person) | Tables by platform, 3 to 5 learners. One laptop per learner. Instructor walks the tables, Copilot first |
| Steps per platform | See section 5 (4 cards with the same 6 core steps and the same debrief rerun). No fast-start card. Stretch: second agent by manual file hand-off on the Claude and ChatGPT cards only, after class, "not yet tested by the course team". Copilot and Gemini: core path only (spec `stretch_scope`). No schedule step |
| Materials | `kit/lab-4/` (job card, current map, Copilot fallback text, record sheet, README). Case files `m4-evidence-pack.md`, `m4-check-sample.md`. `modules/m3/kit/kit-m4/` to rebuild before the lab. `kit/kit-m5/` for catch-up after. Instructor only: `case/planted-errors.md`, `case/expected-results.md`, saved demo output, saved check sample result from the tuned project |
| Success criteria | Every map entry shows its source type and links to a deal ID or interview ID. Each "growing" or "fading" label names the two periods and the counts. Each flag has the learner's decision. 3 entries audited, growing or fading first. The hand-off rule fixed. After class: the check sample passes the 5-item pass condition |
| Debrief questions | Which alternative must you beat in each segment, and what is your evidence? Which check or audit found the error? Where did the map's answer for each deal come from? What does your fixed hand-off rule stop? |
| Fallback path | Cannot use own work: case data. Agent lost or behind: rebuild from `kit-m4` (about 5 minutes). Platform blocked: pair with a learner on another platform. Copilot with no license: `copilot-fallback-instructions-m4.txt`, evidence pack uploaded or pasted (split at "## Part 3" if needed). Upload fails: paste the text. No file output: full tables in one message (brief rule 7). Agent does not make the error: debrief uses the saved demo output. Rerun not done: use `kit-m5/alternatives-map.md` and `kit-m5/driver-log.md` for the log save. Behind at the end: load `kit-m5` before module 5 |
| Learner evidence | The hand-off rule as written (step 2) and as fixed (step 6). Audit findings for 3 traced entries. Flag report decisions. The alternative to beat in one segment, with its evidence. All on `lab-4-record-sheet.md` |

## 8. Learner kit

Character counts measured with `wc -m` on 2026-11-27. Copilot course budget (spec `copilot_no_license_fallback`): core brief 3,500 or fewer, job card 1,500 or fewer, knowledge file 2,800 or fewer, total 7,800 or fewer. Vendor limit: Instructions 8,000 characters (mb-01). Paste target for one chat message: 15,400 (G2-PF-03). Every `.txt` copy matches its `.md` file (`cmp`).

| File | Loads into | Characters | `.txt` copy |
| --- | --- | --- | --- |
| `lab-4/job-card-alternatives-map.md` | Knowledge | 1,497 (budget 1,500) | yes |
| `lab-4/alternatives-map.md` (copy of `case/m4-alternatives-map.md`, end of Q2 2027) | Knowledge | 2,192 (budget 2,800) | yes |
| `lab-4/copilot-fallback-instructions-m4.txt` | Copilot Instructions, no license | 7,419 (budget 7,800; limit 8,000) | is a `.txt` |
| `lab-4/lab-4-record-sheet.md` | Not loaded. Learner keeps it | 2,110 (not loaded) | no |
| `lab-4/README.md` | Not loaded | not counted | no |
| `kit-m5/brief-v5.md` (copy of the module 5 draft; rule 4 is the lab 4 rule) | Instructions | 3,491 (budget 3,500) | yes |
| `kit-m5/job-card-problem-backlog.md` (no change) | Knowledge | 1,194 | yes |
| `kit-m5/code-book.md` (no change) | Knowledge | 2,791 | yes |
| `kit-m5/problem-backlog.md` (no change from kit-m4) | Knowledge | 15,194 (a log; one paste, under 15,400) | yes |
| `kit-m5/job-card-win-loss.md` (no change) | Knowledge | 1,483 | yes |
| `kit-m5/driver-code-book.md` (no change; no controller alarms row) | Knowledge | 2,284 | yes |
| `kit-m5/driver-log.md` (copy of the module 5 draft: Q2 and Q3 rows) | Knowledge | 7,616 (a log) | yes |
| `kit-m5/job-card-weekly-feedback.md` (no change) | Knowledge | 1,496 | yes |
| `kit-m5/tag-list.md` (no change, v2 with P10) | Knowledge | 2,038 | yes |
| `kit-m5/job-card-alternatives-map.md` (same as `lab-4`) | Knowledge | 1,497 | yes |
| `kit-m5/alternatives-map.md` (copy of the module 5 draft, end of Q3 2027) | Knowledge | 3,286 (over the 2,800 knowledge file budget; it is not in any fallback Instructions) | yes |
| `kit-m5/lab-4-fix-rules.md` | Not loaded. Handout | 1,016 | yes |
| `kit-m5/copilot-fallback-instructions-m4-v5.txt` | Copilot Instructions, no license, to rerun job 4 | 5,388 (budget 7,800) | is a `.txt` |
| `kit-m5/README.md` | Not loaded | not counted | no |

Fallback sum check (lab 4): header 463 + brief v4 3,253 + job card 1,497 + map 2,192 + 3 separators (14) = 7,419. The learner's rule 4 (about 230 characters; the case fix text is 233) brings it to about 7,650, under 7,800. kit-m5 fallback: header 392 + brief v5 3,491 + separators 7 + job card 1,497 = 5,388. With the Q3 map it would be 8,681, over 8,000 (B13).

Copilot no-license pastes (each one message, under 15,400): lab 4 evidence pack 15,350 (split at "## Part 3": 6,590 and 8,760). kit-m5 rerun of job 4: map 3,286 alone, then the deals. Module 5 (for reference): backlog 15,194 alone; driver log, map and past reports 13,675.

Spec P3 check "core instructions stay under 8,000 characters": brief v5 is 3,491.

Knowledge files in the agent after module 4: 10 (4 job cards, code book, driver code book, tag list, alternatives map, problem backlog, driver log). Course budget 13. Spec `uploads_per_lab` module 4: 2 files to the agent, 2 in chat (evidence pack, check file). The check file runs after class.

## 9. Instructor notes

- Timing flex:
  - Behind before the lab: cut the question on 4.3 (keep the story; it is the required example) and shorten 4.4 to the four types. Never cut the lab brief (4.9 to 4.11) or the data safety slide.
  - Behind in the lab: at minute 21, tell learners to fix the rule even if the audit is not done. The debrief reveal works from the step 3 run.
  - Behind in the debrief: keep the reveal (4.14) and the log save card (4.17). Cut 4.13 to the rerun only, with no answers taken. Show 4.15 in 30 seconds.
  - Ahead: learners do "Done early": section 5 of the record sheet for a second segment, or their own lost deals. Claude and ChatGPT learners may start the second-agent stretch after class only.
- Common failures and recovery:

| Failure | Recovery |
| --- | --- |
| Agent lost or broken after module 3 | Rebuild from `kit-m4` (about 5 minutes), then do step 1 |
| Copilot: the agent ignores the knowledge files (no license or billing) | Use the no-license box on the Copilot card: `copilot-fallback-instructions-m4.txt` in Instructions, evidence pack uploaded or pasted |
| Copilot no license: the evidence pack paste is too long | Split it at "## Part 3" (6,590 and 8,760 characters). Add "Part 1 of 2. Wait for part 2." to the first message |
| Gemini: adding files to the existing skill fails | Check the label: **Add files** on an existing skill. If it still fails, upload the whole skill again with all its files (gm-01) |
| Claude: no file in the answer | Turn on **Code execution and file creation** (**Create and edit files**). Team or Enterprise: the owner sets it in **Organization settings**. Or accept the full tables in one message (brief rule 7) |
| The answer stops halfway (long output) | Send "Continue". Or send "Give the map and the flag report first, then the driver log" |
| The agent runs the win/loss job, not the map job | Check the prompt says "Run the alternatives map job". Check `job-card-alternatives-map` is in knowledge |
| The agent counts won deals on the map | Point to job card step 3 ("Count lost deals"). A learner rule that passes only lost deals also fixes it |
| The agent mixes CRM-only deals into the buyer interview counts | Point to job card step 3 and the quality check on source type. Lab 2 rule 2 also applies |
| The agent recounts the match rate table with Q3 deals | Point to job card step 6 ("Do not recount match rates"). Not a planted error. Delete the recount from the saved driver log |
| The agent labels a change "growing" with no periods or counts | Quality check 3. Ask it to state "Q2 2027 vs Q3 2027" and both counts. Rerun |
| The agent writes one file with the map and the driver log | Ask: "Give the map and the driver log as two separate files." Needed for the log save card |
| The agent does not make the planted error (D-3108 already do nothing) | Good. Ask the learner which line in their rule or the job card kept it out. In the debrief, show the saved demo output |
| The agent flags D-3108 and D-3102 as "no alternative recorded" and maps neither | Not the planted error. The learner's rule stopped both blanks. Ask the learner to read both interviews and decide. D-3102 is Vantafrost; D-3108 is do nothing |
| A learner's own CRM export holds buyer names or contact details | Stop. Remove names, contact details and deal values the company has not approved, or use the case data. Data safety slide |
| The fixed agent also flags D-3103, D-3106, D-3107 (or D-4103): CRM competitor "None", buyer did nothing | Fine, not a failure. "None" and do nothing can read as a difference to a strict agent. The pass items are still met. The PM decides each flag |
| Claude or ChatGPT stretch: the second project asks for interviews, the CRM export or the backlog | Expected. The file is the only hand-off (card note). Record what it does with rule 4 for the course team |
| Claude or ChatGPT stretch: the second project shows no driver log file | The first project gave the tables in chat. Copy the driver log table into a text file and upload it. Record it for the course team |

- Case notes (module builder, checked 2026-11-27 against the case files):
  1. OI-19 (owner module builder) covers lab 1 (I-201) and lab 5 (F-1108, F-1214). No lab 4 record is in it. Module 3 section 9 note 1 closes the feedback part. Nothing to add for module 4.
  2. D-3102 (Beckton Cold Chain, Distribution) is the decoy. Its alternative is blank too, but the CRM (Vantafrost) and WL-3102 (the buyer says they went with Vantafrost) agree. A blank cell alone is not the clue (`planted-errors.md`).
  3. The "CRM and buyer match" column in Part 1 compares the CRM reason with the buyer's primary driver (lab 2). It is not about the competitor field. D-3108 shows "no" because the CRM reason is "Price" and the driver is alert accuracy. Learners may read it as the competitor match. Ask: "Which CRM field does that column compare?"
  4. D-3104 (Ashgrove Freight Cold) is a won deal with CRM competitor "Rimecore" (the buyer also trialed Rimecore). Won deals are not on the map. An agent that counts it for Rimecore is wrong for a different reason.
  5. D-3109 (Duncairn Logistics) is CRM only with competitor "Incumbent loggers". Mapping it to do nothing, CRM only, is correct. A flag for "not in the map" is also fine.
  6. D-3107 (Kittering Research Labs): "We kept our current loggers." Do nothing in Pharmacy and lab. Pharmacy and lab is a tie in Q3 (Rimecore 1, do nothing 1). The case gives no PM decision for the tie.
  7. ALT-03 controller alarms has 1 deal in Q2 and 0 in Q3. "Fading" is the label the case expects, with the low counts stated. The PM judges.
  8. Two Q3 buyers say they may come back: D-3106 ("We will look again in spring.") and D-3108 ("We may try again when the alert problem is fixed."). This links to the 4.3 story. Use it in the reveal only if time allows. Do not use it before the reveal.
  9. Before the fix, the D-3108 driver log row keeps the Part 1 quote. After the fix, the agent may keep it or take a quote from WL-3108. `kit-m5/driver-log.md` uses the WL-3108 quote "Your trial sent alerts every lunch rush, and my managers gave up on it." (module 5 D7; D13 here).
  10. The backlog link in "what changed" (output 4): D3 alert accuracy points to P01 (alert noise); D4 compliance report fit to P02; D6 calibration to P08; D1 price and D7 timing have no backlog problem. A learner may see "do nothing" as a sign of weak willingness to pay. That is the PM's call, not the agent's.
  11. The map file calls its summary table "What moved". The job card, slides and cards say "what changed". Same table (module 3 decision D10).
- Kept off the slides on purpose: any competitive intelligence figure (N13 has figures; the point is the blind spot). "Buyers choose do nothing more often than teams track" as a claim (no source; recorded gap). Any setup screen for a second agent or a schedule. The client's name, dates, contract or people in the 4.3 story. D-3108 and D-3102 before the debrief.
- Registry guard: not CAW-AI (positioning proof check, buyer voice watch, competitive signal watch) and not the AI Agents course Competitive Intel Watchdog. No public sources, no competitor moves, no scheduled task. Only the team's own interviews and deals. No slide compares own buyer sources with public reviews (CAW-AI module 4). Slide 4.4 is about alternative types, not slide 2.4 (who the buyer is). New slides only.
