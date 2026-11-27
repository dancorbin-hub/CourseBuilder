# Module 2: Win/loss and the match rate

Course: Advanced AI for Market Research (`market-research`). Stage 3 draft by the module builder, 2026-11-27. Built from `spec.yaml` (Gate 2, approved 2026-11-26), `outline/development-brief.md`, `outline/gate-2-decisions.md`, the case files and the approved module 1 (`modules/m1/`, Gate 3 decisions D9, D11, D12 and D13, Gate 4 decision G4-1).

## 1. Summary

| Item | Value |
| --- | --- |
| Workflow row and bottleneck | mr-wf-02. Run a win/loss program that turns each decided deal into an updated, checked decision-driver report. Bottleneck: manual win/loss is slow and does not scale. Sales-entered loss reasons often differ from buyer reasons. Many teams do not run win/loss at all (W1, W2; claims only, no figure on slides) |
| Framework category and focus area | Market. Win/Loss Analysis |
| Capability Standards (as in spec) | Confirmed by Dan, Pragmatic to confirm. Skills 1.3 Market Discovery, 8.1 Market Data Context and Pattern Recognition. Competencies 1.3A, 1.3C, 8.1B. Gap: the Win/Loss Analysis box has no primary skill (`capability-mapping.md` gap 2) |
| Rung | 1, Hand-run batch, two sources joined |
| Minutes (full day / half day) | 70 / 75 |
| Instructor-led / hands-on (minutes, %) | Full day: 28 / 42 = 40% / 60% (8 + 10 + 10 = 28; 32 + 10 = 42). Half day: 30 / 45 = 40% / 60% (8 + 11 + 11 = 30; 34 + 11 = 45). Inside the 40/60 rule (plus or minus 5 points) |
| Planted error and warning level | A CRM-only deal leaks into the buyer findings: WL-2214 (deal D-2214) holds only a sales note, "Lost on price." CRM-only lost deals D-2204 and D-2210 also say "Price". Price then looks like a top buyer driver. Warning: hint ("Audit before you approve.") |
| Learner evidence | Match rate table with the learner's one-sentence read of it. Flag report decisions. Audit findings for 2 deals. The brief change (v2 to v3). All on `lab-2-record-sheet.md` |
| Agent after this module (files) | Instructions: brief v3. Knowledge: `job-card-problem-backlog`, `code-book`, `problem-backlog` (no change), `job-card-win-loss`, `driver-code-book`, `driver-log` (new). 6 knowledge files. Catch-up: `kit/kit-m3/` |

### Slide minutes check

| Arc step | Slides | Full day | Half day | Mode |
| --- | --- | --- | --- | --- |
| Why this matters, workflow and bottleneck | 2.1 to 2.4 | 1 + 3 + 2 + 2 = 8 | 1 + 3 + 2 + 2 = 8 | Instructor-led |
| Live demo | 2.5, 2.6 | 7 + 3 = 10 | 8 + 3 = 11 | Instructor-led |
| Build pattern and lab brief | 2.7 to 2.11 | 2 + 3 + 2 + 2 + 1 = 10 | 2 + 3 + 3 + 2 + 1 = 11 | Instructor-led |
| Lab 2 | 2.12 | 32 | 34 | Hands-on |
| Debrief | 2.13 to 2.17 | 3 + 2 + 3 + 1 + 1 = 10 | 4 + 2 + 3 + 1 + 1 = 11 | Hands-on |
| Total | 17 slides | 70 | 75 | 28 + 42; 30 + 45 |

Half day: the slide minutes follow spec `half_day.arc_minutes` (8, 11, 11, 34, 11). The spec note names the match rate read in the debrief (4 minutes, slide 2.13) and the lab (34). To fit the arc minutes, this draft also gives 1 extra minute to the demo (2.5) and to counts, not verdicts (2.9). See decision D9.

### Builder decisions inside the spec

| # | Decision | Why |
| --- | --- | --- |
| B1 | Card step 6 runs in a new chat: "In a new chat, send the same 2 files with the prompt 'Run the win/loss job'." | Same reason as module 1 decision D1 (approved): a new chat is the only way to be sure the tuned brief applies on all 4 platforms. The spec card text is an outline (spec `card_rules`). See decision D1 |
| B2 | The lab brief is 2 short slides. 2.10: goal, 5 key actions and a pointer to the step card in the workbook. 2.11: pass check, hint and data safety box. The full 6 steps are only on the step cards (kit and workbook) | Dan's rule for lab brief slides (2026-11-27, same idea as G4-1 option C for slide 1.10): the slide shows a short version and points to the workbook, which learners download from the Pragmatic Learning Hub. Same minutes (3). See decision D4 |
| B3 | "How to share findings with sales" has no minutes in the spec debrief. It is taught on slide 2.8 (the match rate is a data gap, not a score for sales) and practiced on slide 2.13 (who hears it, and how) | The spec debrief minutes add up to 10 without it. m2-o4 still has a place to practice. See decision D3 |
| B4 | No audit hint beyond the spec step. The record sheet asks for 2 random deals and a read of the deal source column, as in spec `card_steps` 4 and objective m2-o3. It does not say which deals or which driver to check | Module 1 decision D11: the audit hint was for lab 1 only. Warning level for lab 2 is "hint": the slide says "Audit before you approve." only |
| B5 | The slides and talk track never use the term the spec bans for the match rate (PA-04). The talk track says what the match rate does not tell you | Spec `voice.terms_never_used` and `registry_guard` |
| B6 | Module 2 adds no empty driver log to the agent. The first run makes the driver log. The log save card adds it to knowledge (nothing to replace the first time) | Spec `uploads_per_lab`: module 2 adds 2 files to the agent. `case/company.md` says the same |
| B7 | The Copilot no-license fallback text holds brief v2 with the kit's lab 1 rule. The card tells learners to put their own lab 1 rule there if it differs | Module 1 decision D13. Total 7,171 characters, under the 7,800 course budget and the 8,000 limit (mb-01) |

### Decisions for Dan

Most important first. Each decision has a recommended answer.

| # | Decision | Options | Recommended |
| --- | --- | --- | --- |
| D1 | **Card step 6 in a new chat.** Spec `card_steps` 6 says "Send the same files again with the prompt 'Run the win/loss job'". The draft adds "In a new chat", as in module 1 D1 | A: keep the draft. Update spec `card_steps` 6 to match. B: same chat. Risk: the new rule may not apply in an open chat on some platforms | A. Confirm in your card test |
| D2 | **Schedule stretch is on no card.** Spec stretch: "Run the job on each new batch when the export file arrives", only where verified. Nothing is verified yet (cl-sc-07, cg-06 not verified; check is due before module 3). Also, a schedule with no new input does nothing in a no-connector lab (methods M8), and a ChatGPT task cannot read project files (cg-06). Each card has a "Done early" line instead: run the job on your own deal export, or draft your note to sales. Neither uses a new platform feature | A: no schedule stretch in module 2. Module 3 owns the schedule stretch (spec `stretch_scope.slides`). B: hold module 2 until the module 3 verification, then add it to the Claude and ChatGPT cards | A |
| D3 | **Share findings with sales has no debrief minutes in the spec.** Taught on 2.8, practiced on 2.13 (B3) | A: accept. B: take 1 minute from the check sample (3 to 2) for a separate slide | A |
| D4 | **Lab brief as 2 short slides (B2), per your lab brief rule.** 2.10 has the goal, 5 key actions and the workbook pointer. 2.11 has the pass check, the hint and the data safety box. PRD rule 7 wants the success criteria "on the slide before the lab": that is 2.11. The spec places the data safety note on the lab brief slide: it is on 2.11 | A: keep 2 short slides. B: merge into one short slide (goal, key actions, pass check, hint, data safety box) | A. The data safety box and the pass check together fill one slide at 36 pt |
| D5 | **Case wording conflicts with Gate 2 decision v2-7.** `case/expected-results.md`, lab 2 second sample, says "10 deals (program minimum met)". Dan removed the 10-deal minimum. The module does not repeat the phrase. The file is fingerprinted | A: the case builder deletes "(program minimum met)" and records a new fingerprint. B: leave it (instructor-only file) | A |
| D6 | **The audit step names the deal source column.** This is the spec wording (card step 4, objective m2-o3). It points near the error. With only 2 random deals out of 14, the chance to draw D-2214 is about 1 in 7. The read of the whole deal source column is what finds it | A: keep the spec wording. It is a step, not a hint about the error. B: drop "and the deal source column" (the error becomes hard to find in 32 minutes) | A |
| D7 | **kit-m3 driver log has no case PM flag decisions.** The case gives the lab 2 flags but no PM decisions for them. The kit does not invent them: the decision column says "From your lab 2 record sheet" | A: keep. B: you give the case PM's decisions, and the case builder adds them to `expected-results.md` | A |
| D8 | **Copilot CSV in chat is not verified** (G2-PF-02). The card says "upload, or paste the text" (module 1 D9). The no-license path pastes the CRM export as text (spec). No `.xlsx` copy is in the kit: the spec adds one only if `.csv` fails | A: card test checks `.csv` upload. If it fails, the next build adds an `.xlsx` copy. B: add an `.xlsx` copy now | A |
| D9 | **Half-day minutes.** The arc minutes need 1 extra minute on the demo (2.5) and on 2.9, which the spec note does not name | A: accept, as module 1 D16 | A |
| D10 | **Story slot (slide 2.2).** No story written, to avoid an invented story (decision 43). Topic from the spec: a sales leader who changed a pricing plan from CRM loss reasons | A: you supply one real Pragmatic story. B: leave it optional with the skip path (module 1 D12) | A if you have one, else B |
| D11 | **"Many teams do not run win/loss at all."** The spec bottleneck cites W1 and W2 for it. In the ledger, W1 and W2 support "CRM reasons often differ" and "manual win/loss is slow and does not scale". Only W3 (2022, not verified) says "underused". So the slide does not say it. The talk track says "Win/loss is the data most teams do not get" as the course's view (Dan's theme, Gate 2 C1), not as a finding | A: keep it off the slide. Verifier confirms. B: find a 2026 source first | A |
| D12 | **Pragmatic guide and the 10-deal rule.** The Pragmatic Framework 2027 guide (page 7) says to repeat win/loss "across at least 10 deals to find patterns". You removed the minimum (v2-7). Slide 2.3 says "Do not wait for a minimum number of deals." The talk track says some programs wait for 10 or more, and why this course does not. It does not say the guide is wrong. Pragmatic reviewers may still notice | A: keep the wording. B: name the guide rule and the reason for the change on the slide | A |
| D13 | **Old Pragmatic source for the no-blame frame.** Slide 2.8 talk track uses the Pragmatic frame: win/loss is about the buyer's experience, not a judgment of sales (PA-04, market visit article, modified 2025-08-27, older than 12 months) | A: keep. It is Pragmatic guidance, not a statistic. B: drop the line | A |
| D14 | **Driver log columns.** The code book format has "Secondary drivers". The case state for the log (`m4-evidence-pack.md` Part 1) has "Period" and no "Secondary drivers". `kit-m3/driver-log.md` follows the case state, so module 4 matches it. Agent runs follow the code book format | A: accept. Tell the module 4 builder. B: the case builder aligns the two (fingerprinted files) | A |

### Changes needing Dan's yes

None of these are made. Each waits for your yes.

| # | File (fingerprinted or approved) | Change | Why |
| --- | --- | --- | --- |
| 1 | `case/expected-results.md` | Delete "(program minimum met)" in lab 2, second sample. New fingerprint | D5 |
| 2 | `spec.yaml` | Module 2 `card_steps` 6: add "In a new chat". Module 2 `stretch`: "Module 3 owns the schedule stretch". New fingerprint | D1, D2 |
| 3 | `modules/m1/kit/kit-m2/` (module 1 kit) | No change needed. Its README already says module 2 adds its own Copilot fallback. The fallback is in `modules/m2/kit/lab-2/`. If you want it inside kit-m2 too, it is a copy only | D13 of module 1 |

## 2. Slides and talk track

### Slide 2.1: Module 2. Win/loss and the match rate
- Layout: Chapter Break
- Minutes: 1 (half day 1)
- On-slide text: MODULE 2. Win/loss and the match rate. Promise: "Add the win/loss job. Label every source. Read the gap." Bullets: Add a win/loss job to your agent. Label each deal "interview" or "CRM only". Read the match rate and decide who hears it.
- Visual intent: Teal side band, "MODULE 2" tag. Small rung icon: rung 1 lit, with two input icons (CRM row, interview note) joined.
- Sources: none

Notes:
```
POINT: In this module you add a second job to your agent: win/loss on a batch of decided deals.
Talk Track:
Your agent has one job now: the problem backlog.
In this module it gets its second job.
Win/loss: why you win and lose deals, in the buyer's own words.
Win/loss is the data most teams do not get.
Today you see what it shows, and how an agent can keep it up to date.
Same agent. Same brief. One new job card and one new code book.
TRANSITION: First, the workflow and what slows it down.
```

### Slide 2.2: Sales says price. Is that what buyers say?
- Layout: Blank
- Minutes: 3 (half day 3)
- On-slide text: Headline: "Sales says price. Is that what buyers say?" Line 1: "CRM loss reasons often differ from buyer reasons." Line 2: "Manual win/loss is slow and does not scale." Workflow strip: "Decided deals and win/loss interviews, then an updated, checked driver report."
- Visual intent: Headline with "price" in orange. Two short lines. A left-to-right strip: a CRM row and an interview note, then a driver report.
- Sources: W1 (claim, Clozd, 2026-04-20), W2 (claim, Corporate Visions, updated 2026-07-30). No figure from either (spec `claims_on_slides`)

Notes:
```
POINT: Teams act on the CRM loss reason because buyer interviews are slow to collect and code, and the two reasons often differ.
Talk Track:
Here is the workflow for this module.
A deal closes, won or lost.
Someone types a reason into the CRM. Usually the sales rep, at the end of a busy quarter.
A win/loss program asks the buyer instead.
Two win/loss firms, Clozd and Corporate Visions, both wrote in 2026 that the CRM reason often differs from what the buyer says.
Both sell win/loss services. So treat this as their experience, not a study.
Both also say a manual program is slow.
Someone books the calls, takes notes, codes them and writes a quarterly report.
By the time the report lands, the chance to act has passed.
So many teams act on the CRM field alone.
At Larkspan, our case company, the Head of Product asks it plainly: "Why do we lose deals? Sales says price. Is that what buyers say?"
[OPTIONAL STORY SLOT, 1 MINUTE. Topic: a sales leader who changed a pricing plan from CRM loss reasons, and what the buyers really said. Use only a story from Pragmatic's work with companies or from a client team. Tell it as their story, never as your own. If you have no such story, skip this slot and spend the minute on the Larkspan question.]
[IF ASKED FOR A NUMBER] Vendor figures exist. None has a dated primary study, so we do not use them.
TRANSITION: Before the agent, the program rules. They decide what the agent can trust.
```

### Slide 2.3: Win/loss program rules
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: Someone outside sales runs the interview. Interview 2 to 4 weeks after the decision. Add each interview as it arrives. Do not wait for a minimum number of deals. One interview covers the whole buyer journey.
- Visual intent: Four short rules, one per line, with a small icon each (person, calendar, plus sign, journey line). "Add each interview as it arrives" in teal.
- Sources: Pragmatic Framework 2027 guide, page 7 (alignment log PA-04). Gate 2 decision v2-7 (Dan, no minimum)

Notes:
```
POINT: Win/loss interviews are run by someone outside sales, soon after the decision, and each one goes into the log as soon as it is coded.
Talk Track:
These rules come from Pragmatic, with one change Dan made for this course.
One. Someone outside sales runs the interview. The buyer gives more honest answers to someone who did not sell to them.
Two. Interview 2 to 4 weeks after the decision. The decision is final, and the buyer still remembers why.
Three. Add each interview as soon as it is coded.
Some programs wait for 10 or more deals before they look for patterns.
You do not need to wait. Win/loss interviews are rarer than discovery interviews.
And one interview covers the whole buyer journey: the trial, the pilot, the price, the install, the people.
So one interview can change a decision.
The agent shows the deal count next to every driver. You always see how far a finding reaches.
At Larkspan, the product team or an outside firm runs every interview. Sales runs none.
TRANSITION: Who is "the buyer" depends on how you sell.
```

### Slide 2.4: Where is the buyer in your deals?
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: Direct deals: the buyer who signed. Reseller and distributor deals: the end buyer, not only the channel. Internal platforms: the team that adopted it, or kept its own tool.
- Visual intent: Three tiles in a row: a handshake (direct), a truck with a store (channel), a building with two team icons (internal platform).
- Sources: none. Examples only. Hardware and internal PM win/loss sources are recorded gaps (`research/workflows.yaml` mr-wf-02 contexts)

Notes:
```
POINT: Win/loss works for hardware sold through a channel and for internal platforms, if you know who the buyer is.
Talk Track:
Win/loss is not only for direct software deals.
Hardware first. Many hardware deals go through distributors and resellers.
The PM may never meet the end buyer. Ask the channel for an introduction, and interview the end buyer.
Larkspan sells most Food service sites through refrigeration contractors. You will see one in the case data.
Internal product management has wins and losses too.
A team that adopted your internal platform is a win. A team that kept its own tool is a loss.
Same job, same labels, same audit.
We found no published source on win/loss in these two settings. So these are examples, not findings.
[ASK: "In your work, who is the buyer of a decided deal?" TAKE 1 OR 2 ANSWERS]
TRANSITION: Let me add the win/loss job in front of you.
```

### Slide 2.5: Live demo. Add the win/loss job
- Layout: 1_prompt
- Minutes: 7 (half day 8)
- On-slide text: LIVE DEMO. "Add the win/loss job." Running example: Larkspan Systems, Q2 2027 decided deals. 7 MIN (half day: 8 MIN).
- Visual intent: Orange "LIVE DEMO" tag. Platform logo for the demo platform (Claude). Small list of the 2 new files and the 2 run files.
- Sources: cl-pj-01, cl-ui-09 (platform matrix, verified). Demo script in section 3

Notes:
```
POINT: Adding a job takes two files, and the first run joins the CRM export and the interview notes into one driver log.
Talk Track:
[SWITCH TO THE DEMO PLATFORM. FOLLOW THE DEMO SCRIPT IN SECTION 3, STEPS 1 TO 4]
Here is the agent from module 1. Brief v2 in the instructions. Three files in knowledge.
I add two files. The win/loss job card and the driver code book.
I do not touch the brief. The brief holds the rules for every job.
[ADD THE 2 FILES]
The driver code book has the decision drivers, the alternatives buyers chose, and two deal source labels.
New chat. Two files: the CRM export and the win/loss notes. One prompt: "Run the win/loss job".
[SEND. WHILE IT RUNS:]
This is new. In module 1, every source was an interview.
Here the agent joins two sources by deal ID.
Some deals have a buyer interview. Some have only a CRM row.
The agent must keep them apart. Watch for that when you read the output.
[HALF DAY: USE THE EXTRA MINUTE TO SCROLL THE WIN/LOSS NOTES FILE WHILE THE RUN ENDS. READ ONE NOTE ALOUD: WL-2203]
[WHEN THE RUN ENDS, OPEN THE OUTPUT FILE]
TRANSITION: Here is how you read it.
```

### Slide 2.6: Read the driver log: where did each finding come from?
- Layout: Blank
- Minutes: 3 (half day 3)
- On-slide text: 1. Deal source: "interview" or "CRM only". 2. Match rate table: CRM reason against the buyer's reason. 3. Driver counts: interviewed deals, accounts, segments. 4. Flag report: your decisions go here.
- Visual intent: A cropped, readable mock from the demo run: 2 driver log rows (D-2203 interview, D-2204 CRM only), the match rate table header row, 2 flag rows. Large type. Numbers 1 to 4 in orange circles.
- Sources: none (case output, `case/m4-evidence-pack.md` Part 1, `case/expected-results.md`)

Notes:
```
POINT: You manage the win/loss job by reading where each finding came from, not by recoding the deals.
Talk Track:
[DEMO SCRIPT STEPS 5 TO 8. STAY ON THE SCREEN, THEN SHOW THIS SLIDE AS THE SUMMARY]
One. The deal source column.
D-2203, Stonemere Cold Storage. Source: interview, WL-2203.
The buyer says: "Your hub kept dropping the sensors in our two blast freezers, and Rimecore's didn't drop once in three weeks."
The CRM says: Price.
D-2204, Lantern Row Bakeries. Source: CRM only. No quote.
Two. The match rate table. How often the CRM reason matches the buyer's primary driver.
Three. Driver counts. Each driver shows its interviewed deals, its accounts and its segments.
Four. The flag report.
D-2207: the CRM says "Feature gap: multi-site dashboard". The buyer says the trial had over forty alerts in the first week.
D-2209: the buyer chose alarms in a new refrigeration controller. That alternative is not in the code book.
The decision column is blank. That is yours.
[DO NOT COMMENT ON THE MATCH RATE NUMBERS OR THE DRIVER TOTALS. IF A LEARNER ASKS:] Good question. Hold it for your audit.
[SAVE THE DEMO OUTPUT FILE. YOU MAY NEED IT IN THE DEBRIEF]
TRANSITION: The deal source label is the heart of this lab. Here is why.
```

### Slide 2.7: Label where each finding comes from
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: interview: a buyer win/loss interview exists for the deal. CRM only: no buyer interview. Only the CRM record exists. Bottom line: "The report is only as true as its sources."
- Visual intent: Two labels as large tags, teal (interview) and gray (CRM only). Bottom line in orange.
- Sources: none (case `m2-driver-code-book.md`; spec lab core message)

Notes:
```
POINT: The agent labels each deal by its source, so you can see which findings come from buyers and audit the label.
Talk Track:
In module 1 every source was an interview, labeled PM-held or AI-moderated.
Win/loss has a new kind of source: the CRM record.
So each deal gets one of two labels.
"Interview": a buyer win/loss interview exists for the deal.
"CRM only": there is no buyer interview. Only the CRM record.
A CRM-only deal still matters. It shows what sales recorded, and it tells you which buyers to interview next.
It is just not the buyer's voice.
[POINT TO THE BOTTOM LINE]
This is the core message of the lab. The agent's report is only as true as its sources.
So make the agent label where each finding comes from. Then audit the labels.
TRANSITION: Once deals are labeled, you can compare the two sources.
```

### Slide 2.8: The match rate: how often CRM and buyer agree
- Layout: Blank
- Minutes: 3 (half day 3)
- On-slide text: Match rate: of the deals with a buyer interview, how often the CRM reason matches the buyer's primary driver. Shown for won, lost and total. "A gap in the data. Not a score for sales."
- Visual intent: The empty match rate table (Outcome, Deals with an interview, CRM reason matches buyer primary driver, Match rate) with 3 rows. Bottom line in teal.
- Sources: case `m2-driver-code-book.md` (table format). Alignment log PA-04 (Pragmatic: match rate wording; frame win/loss around the buyer's experience, not as a judgment of sales; market visit article, modified 2025-08-27, see D13)

Notes:
```
POINT: The match rate shows how often two sources agree, and you share it as a gap in the data, not as a score for sales.
Talk Track:
The match rate compares two sources on the same deal.
Of the deals where you heard from the buyer, how often does the CRM reason match the buyer's main reason?
The table shows it for won deals, lost deals and the total.
We call it a match rate on purpose.
It tells you how often two sources agree. It does not tell you which one is right.
A rep may hear "price" because price is the easiest thing for a buyer to say at the end of a call.
Now, how sales hears it.
Pragmatic frames win/loss around the buyer's experience, not as a judgment of sales.
So when you share a low match rate:
Lead with the buyer quotes, not the percentage.
Say what the program fixes: we now hear from more buyers.
Ask sales for help: which lost deals should we interview next?
And show the deal counts, so nobody over-reads one quarter.
TRANSITION: Counts matter for every driver, not only the match rate.
```

### Slide 2.9: Report counts, not verdicts
- Layout: Blank
- Minutes: 2 (half day 3)
- On-slide text: Every driver shows its interviewed deals, accounts and segments. No pass or fail number on a driver. No top driver for a segment from one deal. You decide what to act on.
- Visual intent: One driver row as a card: "D1 Price and value: interviewed deals __, accounts __, segments __". Blank counts. Last line in orange.
- Sources: none (spec module 2 `no_threshold`; case `company.md` hand-off rule 3; brief rule 4)

Notes:
```
POINT: The agent reports the count behind every driver and claims no verdict, and the PM decides what to act on.
Talk Track:
In module 1 you saw it for problems: no magic number. The same holds for drivers.
The agent does not write "price is our top loss reason".
It writes the driver, then the count: interviewed deals, accounts, segments.
The case PM's hand-off rule says it: show the count of interviewed deals behind every driver statement.
No number in the brief says "3 deals makes it real".
The segment rule from your brief still applies.
The agent names no top driver for a segment from one deal in that segment.
You read the counts and the quotes. You decide what to act on.
[HALF DAY: USE THE EXTRA MINUTE. ASK: "Name a decision where one buyer's story of a lost deal was enough to act on." TAKE 2 ANSWERS]
TRANSITION: Here is your lab.
```

### Slide 2.10: Lab 2 brief
- Layout: Activity
- Minutes: 2 (half day 2)
- On-slide text: ACTIVITY. Lab 2: Add the win/loss job. Goal: Run win/loss on decided deals. Report the gap between sales and buyer reasons. Key actions: Add the win/loss job. Run it. Decide each flag. Audit the deal source labels. Add one rule. Footer: "Full steps: your step card in the workbook (Pragmatic Learning Hub)."
- Visual intent: Orange "ACTIVITY" band. Goal at the top. 5 short key actions in large type. Workbook pointer in the footer. Nothing else on the slide.
- Sources: none

Notes:
```
POINT: In lab 2 you add the win/loss job, run it on decided deals, and manage it by its flags and your audit.
Talk Track:
The goal of this activity is to extend your agent to run win/loss on a batch of decided deals, and report the gap between sales reasons and buyer reasons.
The core message: the agent's report is only as true as its sources. Make the agent label where each finding comes from, then audit the labels.
These are the key actions. The full steps are on your step card in the workbook.
You downloaded the workbook from the Pragmatic Learning Hub. Open your platform's card now.
[WALK THE KEY ACTIONS IN ONE LINE EACH. DO NOT READ THE CARD ALOUD]
On your own work: an export of recent decided deals and any win/loss notes, from an approved tool, with confidentiality agreed.
Otherwise use the Larkspan files. Both paths use the same steps.
Record your decisions on the lab 2 record sheet in your kit. That is your evidence.
TRANSITION: Here is what done looks like.
```

### Slide 2.11: Lab 2: done when
- Layout: Activity
- Minutes: 1 (half day 1)
- On-slide text: ACTIVITY. Done when: The match rate table is complete. Each deal has a source label. Each driver shows its counts. Each flag has your decision. You audited 2 deals and added a rule to the brief. Orange box: "Audit before you approve." Data safety box (standard text): "Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss."
- Visual intent: Orange "ACTIVITY" band. Success check as 5 short lines on the left. Orange box on the right. Standard data safety box at the bottom, the same box as the step cards.
- Sources: none (spec `planted_error_fade` module 2; spec `data_safety_note`)

Notes:
```
POINT: The success check names the outputs and your manager actions, and the data safety rule covers deal data too.
Talk Track:
Done when: a complete match rate table, a source label on each deal, counts on each driver, your decision on each flag, 2 audited deals and one new rule.
[POINT TO THE DATA SAFETY BOX]
Same rule as module 1. Approved tool. Confidentiality agreed for win/loss.
One thing is new. Interview notes and CRM exports hold customer names and deal values.
Your driver log keeps them after the lab. Decide what it may keep, and for how long.
[POINT TO THE ORANGE BOX]
Audit before you approve.
Breakout rooms are by platform. Build and save your own agent. Share your screen only when someone is stuck.
Agent lost or behind? Rebuild it from kit-m2 first. It takes about 5 minutes.
TRANSITION: [OPEN BREAKOUT ROOMS BY PLATFORM. START THE TIMER: 32 MINUTES, HALF DAY 34]
```

### Slide 2.12: Lab 2: Add the win/loss job
- Layout: Activity
- Minutes: 32 (half day 34)
- On-slide text: ACTIVITY. 32 MIN (half day 34 MIN). Time guide, full day: 0 to 4: add 2 files. 4 to 11: run. 11 to 16: decide each flag. 16 to 23: audit. 23 to 26: add your rule. 26 to 32: run again, new chat. Half day: 0 to 4 files. 4 to 11 run. 11 to 16 flags. 16 to 24 audit. 24 to 28 rule. 28 to 34 run again. "Build and save your own agent. Share your screen only when someone is stuck."
- Visual intent: Orange band. A timeline bar with the 6 blocks. Room by platform shown as 4 small tiles.
- Sources: none

Notes:
```
POINT: Learners add the win/loss job and run it from their step card, on their own deals or the case data.
Talk Track:
The goal of this activity is to run one full turn of the manager loop on your agent's new job.
[VISIT EACH ROOM IN TURN. START WITH COPILOT, THEN GEMINI, THEN CHATGPT, THEN CLAUDE]
[CUES: FULL DAY MINUTE, HALF DAY MINUTE IN BRACKETS]
[AT MINUTE 4 (4): ANYONE WHO HAS NOT SENT THE 2 RUN FILES GETS HELP FIRST]
[AT MINUTE 11 (11): "If your run is not done, open the win/loss notes and read two of them while you wait."]
[AT MINUTE 16 (16): "Start your audit now. Open the CRM export and the notes. Check the log; do not trust it."]
[AT MINUTE 23 (24): "Write your rule now, even if your audit is not done."]
[AT MINUTE 26 (28): "Run again now, in a new chat, with the same 2 files."]
[AT MINUTE 29 (31): "Not sent step 6 yet? Skip it. Run it after class." THE DEBRIEF WORKS FROM THE STEP 2 RUN AND THE SLIDE]
[COMMON FAILURES AND RECOVERY: SEE SECTION 9]
[DO NOT REVEAL THE ERROR. IF A LEARNER ASKS "IS THIS IT?", ASK: "Which source does that finding come from?"]
TRANSITION: [CLOSE ROOMS AT MINUTE 32, HALF DAY 34] Bring your record sheet and your match rate table.
```

### Slide 2.13: What does your match rate table show?
- Layout: debrief
- Minutes: 3 (half day 4)
- On-slide text: DEBRIEF. Write one sentence: what does your match rate table show? Who hears it: sales, marketing or leadership? How do you say it so sales does not hear blame?
- Visual intent: Navy "DEBRIEF" band. 3 questions. On click: the case match rate table (won 3 / 2 / 67%, lost 6 / 2 / 33%, total 9 / 4 / 44%) and one line: "CRM says Price on 7 of 9 lost deals. Interviewed buyers name price on 1 of 6."
- Sources: none (case `expected-results.md` lab 2)

Notes:
```
POINT: The match rate table shows that the reason sales records and the reason buyers give are often not the same, and the PM decides who hears it and how.
Talk Track:
Take one minute. On your record sheet, write one sentence: what does your match rate table show?
Then mark who hears it, and how you would say it.
[1 MINUTE. HALF DAY: 2 MINUTES]
[TAKE 2 OR 3 SENTENCES, ONE FROM EACH PLATFORM IF YOU CAN]
[CLICK TO SHOW THE CASE TABLE]
Here is the Larkspan table, from the 9 deals with a buyer interview.
Won: 3 deals, the CRM reason matches on 2. Lost: 6 deals, it matches on 2.
The CRM says "Price" on 7 of 9 lost deals. Interviewed buyers name price on 1 of 6.
The other lost buyers name the hub in blast freezers, alert noise in the trial, the audit export, a budget delay, and new refrigeration controllers.
No driver repeats. Every driver has 1 interviewed lost deal. That is a reason to interview more buyers, not a reason to pick a winner.
Who hears it? One way to split it:
Product and hardware hear the trial findings: the hub and the alerts.
Marketing hears the audit report findings, won and lost.
Sales hears the gap, framed as data, with a request: which deals should we interview next?
[HALF DAY: TAKE ONE MORE ANSWER ON "HOW DO YOU SAY IT"]
[IF A LEARNER'S TABLE SHOWS PRICE AS A TOP BUYER DRIVER: "Hold that. We look at it next."]
TRANSITION: So where did your agent's price findings come from?
```

### Slide 2.14: Audit reveal: where did "price" come from?
- Layout: debrief
- Minutes: 2 (half day 2)
- On-slide text: DEBRIEF. Which check or audit found the error? Which deals did your agent treat as buyer evidence? (Reveal after answers:) WL-2214: the buyer did not attend. Only a sales note: "Lost on price." Only 1 interviewed buyer named price (WL-2205). One interview can change a decision. The count shows how far it reaches.
- Visual intent: Navy band. 2 questions. The reveal appears on click: the WL-2214 entry, and the D-2204 and D-2210 CRM rows, each marked "CRM only".
- Sources: none (case `planted-errors.md` lab 2, `expected-results.md`)

Notes:
```
POINT: A deal with no buyer interview leaked into the buyer findings, and only an audit of the deal source column showed it.
Talk Track:
[ASK THE 2 QUESTIONS. TAKE 2 OR 3 ANSWERS]
[REVEAL]
Here is the planted error.
WL-2214, deal D-2214, Highcastle Foods. The interview was scheduled. The buyer did not attend.
The entry holds only a note copied from the CRM: "Lost on price. Rimecore came in about 15% lower."
On the template brief, the agent treats that entry as an interview. Or it fills the gaps from the CRM: D-2204 and D-2210 are CRM only, both "Price".
So price shows 2 to 4 buyer deals and looks like the top buyer driver.
The quote check passes. These deals have no buyer quote, so there is nothing to check.
Only one interviewed buyer named price: WL-2205, Juniper Yard Cafes. "Four site subscriptions was more than we spend on the coolers' service contract, so we stayed with paper logs."
The fix is one rule: a deal with no buyer interview is CRM only. Never use the CRM reason or a sales note as a buyer driver. Count only deals with an interview in the match rate table.
And the other side. One interview can change a decision. D-2207 was an 88,300 dollar deal. The CRM said a dashboard gap. The buyer said alert noise in the trial.
The count, 1 deal, tells you how far that finding reaches today.
[IF NO AGENT IN THE ROOM MADE THE ERROR, SHOW THE SAVED DEMO OUTPUT]
TRANSITION: Did your rule fix it? Test it on deals you have not seen.
```

### Slide 2.15: Check sample
- Layout: Activity
- Minutes: 3 (half day 3)
- On-slide text: ACTIVITY. 3 MIN. New chat on your tuned agent. Send `m2-check-sample.md` with "Run the win/loss job". Compare with the pass condition at the end of your step card.
- Visual intent: Orange band, timer 3 MIN. One-line instruction. Small image of the card's pass condition box.
- Sources: none (case `m2-check-sample.md`, `expected-results.md`)

Notes:
```
POINT: A second sample the learner has not seen shows if the tuned brief works.
Talk Track:
The goal of this activity is to test your tuned brief on new deals.
New chat. Send the check sample. Same prompt.
It holds 10 Q1 deals and their win/loss notes, in one file. Then compare with the pass condition on your card.
[START A 3-MINUTE TIMER]
[AFTER 3 MINUTES, ASK: "Hands up if your agent passed all 5 items." THEN: "Which item failed?"]
[IF D-1307 IS IN THE BUYER DRIVERS: "The buyer declined. The note is the account owner's. Check that your rule names a sales note, not only the CRM reason."]
[IF THE AGENT CODES D-1302 AS D2 INSTALL INSTEAD OF D8 RESELLER AND INSTALL SUPPORT: "Fair reading. It is still a mismatch with the CRM reason, Price."]
TRANSITION: So what do you do on Monday?
```

### Slide 2.16: What you do Monday
- Layout: Blank
- Minutes: 1 (half day 1)
- On-slide text: "Pull your last 10 decided deals. Find out how many have a buyer interview."
- Visual intent: One line, large type. Calendar icon with "Monday".
- Sources: none

Notes:
```
POINT: The first real use of the win/loss job starts with knowing how many of your decided deals have a buyer's voice at all.
Talk Track:
On Monday, pull your last 10 decided deals from your CRM.
Count how many have a buyer interview.
If the answer is few or none, that is your first finding. Book interviews, run by someone outside sales.
Then run your agent on the export and the notes you have, in your approved tool.
TRANSITION: Last step: save your driver log so later jobs can read it.
```

### Slide 2.17: Save your driver log
- Layout: Activity
- Minutes: 1 (half day 1)
- On-slide text: ACTIVITY. 1 MIN. 1. Download the driver log from your step 6 run. 2. Add it to your agent's knowledge as `driver-log`. Your card has the steps for your platform.
- Visual intent: Orange band. Two numbered steps, large. Small platform row: Claude, ChatGPT, Copilot, Gemini.
- Sources: cl-pj-01, cg-01, mb-02, gm-01 (platform matrix); vendor docs on the cards

Notes:
```
POINT: Saving the driver log to the agent's knowledge lets module 4 build on it.
Talk Track:
The goal of this activity is to save your driver log. Module 4 reads it.
Take the log from your step 6 run. Not the check sample run.
Download it. Add it to your agent's knowledge, named driver-log.
This is your first driver log, so there is nothing to replace.
Copilot without a license: keep the file on your computer. You paste it in chat when a job needs it.
If you are behind, kit-m3 has the driver log after the Q2 batch. You can load that instead.
TRANSITION: [FULL DAY: LUNCH. HALF DAY: DAY 1 CLOSE]
```

## 3. Demo script

Platform: Claude (Project). Before class: have the project "Market Evidence Agent" in its state after module 1 (brief v2 in the instructions; `job-card-problem-backlog`, `code-book` and `problem-backlog` in knowledge). Use `kit-m2` if the module 1 demo project changed. Check that **Code execution and file creation** (or **Create and edit files**) is on. Do one rehearsal run on the case files. Save the rehearsal output and screenshots in your instructor folder. Keep a ChatGPT Project in the same state as the backup.

| Step | Instructor does | Screen shows | If it fails |
| --- | --- | --- | --- |
| 1 | Open **Projects**, then "Market Evidence Agent" | Brief v2 in the instructions. 3 files in project knowledge | Rebuild from `kit-m2` in about 5 minutes, or switch to the ChatGPT backup. Say: "This is what kit-m2 is for." |
| 2 | Select **+** in project knowledge. Add `job-card-win-loss.md` and `driver-code-book.md` | 5 files in project knowledge | Paste both texts into the chat with the run in step 3 |
| 3 | Start a new chat in the project. Upload `m2-crm-export-q2.csv` and `m2-winloss-notes-q2.md`. Send "Run the win/loss job" | The agent matches 14 deals to the notes. It returns a downloadable file, or the full tables in one message, and a short summary with the number of flags | If no file: say "Rule 7 in the brief asks for the full tables in one message." If the run fails: switch to the ChatGPT backup. If both fail: show the rehearsal output |
| 4 | Open the output file | Driver log (14 rows), match rate table, driver counts, flag report, "what changed" | Show the rehearsal output file |
| 5 | Point to rows D-2203 and D-2204 | D-2203: interview, WL-2203, D2 Install and connectivity, Rimecore, CRM reason "Price", match "no". D-2204: CRM only, no quote, CRM reason "Price" | If a label differs, say: "That is what an audit is for." Do not fix it live |
| 6 | Point to the match rate table header | Columns: Outcome, Deals with an interview, CRM reason matches buyer primary driver, Match rate | If the format differs, say: "The code book sets the format. A different format is an audit finding." |
| 7 | Point to the flag report | Flags for CRM and buyer reasons that differ (for example D-2207: CRM "Feature gap: multi-site dashboard", buyer: over forty alerts in the first week of the trial). Flag for D-2209: alternative not in the code book (alarms in a new refrigeration controller). Blank PM decision column | If a flag is missing, say: "Hand-off rules are not perfect. That is why you audit." |
| 8 | Download the output file and save it | The file in your instructor folder | Use the rehearsal output in the debrief |

Do not comment on the match rate numbers, the price row or D-2214 on screen. The demo runs on brief v2, so the planted error may show. That is the lab's planted error (module 1 decision D5 pattern).

## 4. Lab brief

- Goal: Extend the course agent to run win/loss on a batch of decided deals and report the gap between sales reasons and buyer reasons.
- Core message: The agent's report is only as true as its sources. Make the agent label where each finding comes from, then audit the labels.
- PM decision: Which market problems, pricing or positioning issues and sales gaps to act on, and who hears about them.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Teaching point: interview notes and CRM exports hold customer names and deal values. The driver log keeps them longer than a one-off prompt. Decide what it may keep and for how long.
- Setup: Zoom breakout rooms by platform, 3 to 5 learners. In person: tables by platform. Each card starts: "Build and save your own agent. Share your screen only when someone is stuck."
- Inputs: Own work: an export of recent decided deals and any win/loss notes, from an approved tool, with confidentiality agreed. Case: `kit/lab-2/` (job card, driver code book), `m2-crm-export-q2.csv` and `m2-winloss-notes-q2.md` (run), `m2-check-sample.md` (debrief check). Files this lab: 5 (2 to the agent, 3 in chat).
- Planted error warning: Hint. "Audit before you approve."
- Success check: The match rate table is complete. Each deal has a source label. Each driver shows its counts. Each flag has your decision. You audited 2 deals and added a rule to the brief.
- Learner evidence: Match rate table with the learner's one-sentence read of it. Flag report decisions. Audit findings for 2 deals. The brief change (v2 to v3). Recorded on `lab-2-record-sheet.md`.

## 5. Step cards

All four cards have the same 6 core steps. Saving is in each card header, not a step. Learners use the files in `kit/lab-2/` and the run files from the case folder. Copilot learners use the `.txt` copies. No fast-start card in module 2 (module 1 only).

### Card: Claude
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Market Evidence Agent" from module 1. Lost or behind? Rebuild it from `kit-m2` first.
- Saves: **Save instructions** saves the instructions. Files save when you add them. Chats save as you go.
- Check date and vendor doc: 2026-11-26. Claude Help Center, "How can I create and manage projects?" (https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects, page metadata 2026-11-06, seen 2026-11-26, platform matrix cl-ui-09). "Create and edit files with Claude" (https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude, page metadata 2026-11-24, seen 2026-11-26, cl-ui-10).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-win-loss` and `driver-code-book` to project knowledge with **+**. |
| 2 | In a new project chat, send the CRM export and notes with the prompt "Run the win/loss job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit 2 random deals and the deal source column, with the checklist on your record sheet. |
| 5 | Add one rule for what you found under "My rules" in the project instructions. |
| 6 | In a new chat, send the same 2 files with the prompt "Run the win/loss job". |

Notes: No file in the answer? Check that **Code execution and file creation** (or **Create and edit files**) is on in **Settings**, then **Capabilities**. Your project opens as one conversation with a Library? Tell the instructor.

**Start here with sample data:** Add: `job-card-win-loss.md`, `driver-code-book.md`. Run files: `m2-crm-export-q2.csv` and `m2-winloss-notes-q2.md`. Own work: replace `driver-code-book` with your drivers in the same format. Use an export of recent decided deals and your win/loss notes.

**Pass condition (second sample, run in the debrief):** New chat. Send `m2-check-sample.md` with "Run the win/loss job". Pass if: (1) D-1307 is labeled CRM only. It is not in the buyer drivers or the match rate table. (2) The match rate table counts 6 deals: won 2 of 2 match, lost 1 of 4. (3) Price is the buyer driver on 1 lost deal only (D-1306). (4) The flag report lists D-1302, D-1304 and D-1309: CRM and buyer reasons differ. (5) Each driver shows its interviewed deals by segment. No top driver is named for a segment.

**Done early:** Run the job on your own deal export. Or write your note to sales in section 4 of your record sheet.

**Stretch (only where verified):** The schedule stretch is not on this card. It is not yet verified for this course.

### Card: ChatGPT
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Market Evidence Agent" from module 1. Plan: Go or Plus or higher. Lost or behind? Rebuild it from `kit-m2` first.
- Saves: As you go.
- Check date and vendor doc: 2026-11-26. OpenAI Help Center, "Projects in ChatGPT" (https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt, "Updated: 3 days ago", seen 2026-11-26, platform matrix cg-ui-09).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-win-loss` and `driver-code-book` to the project's files. |
| 2 | In a new project chat, send the CRM export and notes with the prompt "Run the win/loss job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit 2 random deals and the deal source column, with the checklist on your record sheet. |
| 5 | Add one rule for what you found under "My rules" in **Project settings**. |
| 6 | In a new chat, send the same 2 files with the prompt "Run the win/loss job". |

Notes: **Project settings** is in the **•••** menu of the project. No file in the answer? The brief asks for the full tables in one message. That is fine.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run in the debrief):** Same as the Claude card.

**Done early:** Same as the Claude card.

**Stretch (only where verified):** The schedule stretch is not on this card. It is not yet verified for this course.

### Card: Copilot agent builder
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the agent "Market Evidence Agent" from module 1. To open it: **All agents**, then **...** next to it, then **Edit**. Lost or behind? Rebuild it from `kit-m2` first.
- Saves: **Update** after each change.
- Check date and vendor doc: 2026-11-26. Microsoft Learn, "Add knowledge sources" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge, "Last updated on 2026-11-16", mb-ui-12). "Share and manage agents" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents, "Last updated on 2026-11-16", mb-ui-13). Microsoft Support, "Add content to Microsoft 365 Copilot Chat prompts" (https://support.microsoft.com/en-US/Microsoft-365-Copilot/add-content-to-microsoft-365-copilot-chat-prompts, ms.date 2026-11-18, mb-ui-14, partly verified). All seen 2026-11-26.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | On the **Configure** tab, add `job-card-win-loss.txt` and `driver-code-book.txt` with **Upload**. |
| 2 | In the agent chat, send the CRM export and notes with the prompt "Run the win/loss job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit 2 random deals and the deal source column, with the checklist on your record sheet. |
| 5 | Add one rule for what you found under "My rules" in **Instructions**. |
| 6 | In a new chat, send the same 2 files with the prompt "Run the win/loss job". |

Notes: Use the `.txt` copies. Copilot does not list `.md` as a knowledge file type. To send the run files, upload, or paste the text. If the `.csv` upload fails, open it and paste the text. Download any file the agent makes in the same session. Copilot keeps it for that session only.

**No Copilot license or billing?** Your agent cannot read Knowledge files. Do this instead:
1. Paste all of `copilot-fallback-instructions-m2.txt` into **Instructions**. It replaces the module 1 text.
2. Your own lab 1 rule differs from the kit? Put yours under "My rules".
3. Do the steps above, but skip step 1. Paste the CRM export as text. Upload the notes, or paste the text.
If the instructions do not fit, keep only `brief-v2.txt` in **Instructions**. Paste the job card and the driver code book in chat at the start of each run. The fallback agent does one job at a time.

**Start here with sample data:** Add: `job-card-win-loss.txt`, `driver-code-book.txt`. Run files: `m2-crm-export-q2.csv` and `m2-winloss-notes-q2.md`. Own work: as on the Claude card.

**Pass condition (second sample, run in the debrief):** Same as the Claude card. Upload `m2-check-sample.md`, or paste the text.

**Done early:** Same as the Claude card.

**Stretch (only where verified):** The schedule and second-agent stretch steps are not available on this platform in this course.

### Card: Gemini
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the skill "market-evidence-agent" from module 1. Find it in **Customize**, then **Skills**. Click it to edit. This is a Gemini skill. Gems are now skills. Lost or behind? Rebuild it from `kit-m2` first.
- Saves: **Save** after each change.
- Check date and vendor doc: 2026-11-26. Gemini Apps Help, skills page (https://support.google.com/gemini?p=pn_skills, page shows no date, seen 2026-11-26, gm-ui-10; module 1 decision D3 accepts it with a check date). Google blog, "Automate tasks with skills" (https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/, 2026-09-30) for **/**.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | Add `job-card-win-loss` and `driver-code-book` to your skill with **Add**, **files**, **Upload**. |
| 2 | In a new chat, send the CRM export and notes with "/market-evidence-agent Run the win/loss job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit 2 random deals and the deal source column, with the checklist on your record sheet. |
| 5 | Add one rule for what you found under "My rules" in the skill **Instructions**. |
| 6 | In a new chat, send the same 2 files with "/market-evidence-agent Run the win/loss job". |

Notes: Type **/** (or **@**) in the chat and pick your skill from the list. If adding files to the skill fails, upload the whole skill again with all its files. If a chat upload fails, paste the text. Do not turn on Canvas or Deep Research.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run in the debrief):** Same as the Claude card. Use the prompt "/market-evidence-agent Run the win/loss job".

**Done early:** Same as the Claude card.

**Stretch (only where verified):** The schedule and second-agent stretch steps are not available on this platform in this course.

## 6. Debrief

- Questions: What does your match rate table show, in one sentence? Who hears it, and how do you say it so sales does not hear blame? Which check or audit found the error? Which deals did your agent treat as buyer evidence?
- Match rate read (case, from `case/expected-results.md`): 14 decided deals. 9 with an interview, 5 CRM only (D-2204, D-2208, D-2210, D-2213, D-2214). Won: 3 interviewed, 2 match (D-2201, D-2206), 67%. Lost: 6 interviewed, 2 match (D-2205, D-2211), 33%. Total: 9, 4, 44%. CRM says "Price" on 7 of 9 lost deals. Interviewed buyers name price on 1 of 6. Buyer drivers on lost deals: D1 Price 1 (D-2205), D2 Install 1 (D-2203), D3 Alert accuracy 1 (D-2207), D4 Report fit 1 (D-2212), D7 Timing 1 (D-2211), D10 Current equipment 1 (D-2209). No driver repeats.
- Error reveal (record ids): WL-2214 (deal D-2214, Highcastle Foods, Distribution, lost). The buyer did not attend. Two reschedule requests got no reply. The entry holds only a note from the account owner, copied from CRM: "Lost on price. Rimecore came in about 15% lower." D-2204 (Lantern Row Bakeries) and D-2210 (Wexley Pharmacy Group) are CRM-only lost deals with the CRM reason "Price". On the template brief, the agent treats WL-2214 as interview evidence, or fills missing interviews from the CRM reason. Price then shows 2 to 4 buyer deals and looks like the top buyer driver. The quote check passes because these deals have no buyer quote. Only 1 interviewed buyer names price: WL-2205 (D-2205, Juniper Yard Cafes), "Four site subscriptions was more than we spend on the coolers' service contract, so we stayed with paper logs."
- Fix the learner adds (`case/planted-errors.md`, lab 2): "A deal with no buyer interview is CRM only. Never use the CRM reason or a sales note as a buyer driver. Count only deals with an interview in the match rate table."
- Debrief check (instructor only): The match rate table counts only the 9 interviewed deals. No CRM-only deal (including D-2214) is in the buyer driver findings. The flag report lists the 5 deals where the CRM reason and the buyer reason differ: D-2202, D-2203, D-2207, D-2209, D-2212. It also lists D-2209 (alternative not in the code book: alarms in a new refrigeration controller) and D-2214 (no interview, CRM only). Counts by segment (case hand-off rule 3): interviewed deals Distribution 4, Food service 3, Pharmacy and lab 2. Interviewed lost deals Distribution 3, Food service 2, Pharmacy and lab 1. No driver repeats across the lost deals of any segment, so the agent states no top loss driver for a segment.
- One interview can change a decision: D-2207 (Breckwood Distribution, USD 88,300, lost to Rimecore). CRM: "Feature gap: multi-site dashboard". Buyer (WL-2207): "We got over forty alerts in the first week of the trial, and most were dock doors during loading." Count: 1 interviewed deal.
- Check sample: each learner runs `m2-check-sample.md` in a new chat on the tuned brief (3 minutes). Pass condition on the cards, from `case/expected-results.md`, lab 2 second sample: 6 interviewed deals (D-1301, D-1302, D-1304, D-1306, D-1308, D-1309). CRM only: D-1303, D-1305, D-1307 (declined, sales note "Price"), D-1310. Won 2 of 2 match (100%). Lost 1 of 4 (D-1306, 25%). Total 3 of 6 (50%). Mismatches flagged: D-1302, D-1304, D-1309. Interviewed deals by segment: Distribution 3, Food service 1, Pharmacy and lab 2.
- Share with sales (practiced on 2.13): lead with buyer quotes, not the percentage. Say what the program fixes. Ask sales which lost deals to interview next. Show the deal counts.
- What you do Monday: Pull your last 10 decided deals. Find out how many have a buyer interview.
- Log save card:

| Platform | 1. Download | 2. Add to the agent |
| --- | --- | --- |
| Claude | Download the driver log file from your step 6 run | Add it to project knowledge with **+** |
| ChatGPT | Download the driver log file from your step 6 run | Add it to the project's files |
| Copilot | Download the driver log file from your step 6 run, in the same session | On **Configure**, **Upload** the file. Select **Update** |
| Copilot, no license | Download or copy the driver log from your step 6 run | Keep it on your computer. Paste it in chat when a job needs it |
| Gemini | Download the driver log file from your step 6 run | In your skill, **Add**, **files**, **Upload**. Select **Save**. If that fails, upload the whole skill again with the new file |

Name the file `driver-log` before you add it. Use the step 6 run, not the check sample run. This is the first driver log, so there is no old file to replace. Later runs replace it. If you have no file, use `kit-m3/driver-log.md`.

## 7. LD spec

| Field | Value |
| --- | --- |
| Objective | Extend the Market Evidence Agent with a win/loss job, run it on a CRM export and win/loss notes, decide each flag, audit 2 deals and the deal source column, add a rule to the brief, read the match rate table, and decide who hears the findings and how (m2-o1 to m2-o4) |
| Timing | Full day: lab 32 minutes, debrief 10 (match rate read 3, check sample 3). Half day: lab 34, debrief 11 (match rate read 4). Lab brief before it: 3 minutes (2 short slides; full steps on the step cards in the workbook) |
| Setup (Zoom) | Breakout rooms by platform (Claude, ChatGPT, Copilot, Gemini), 3 to 5 learners each. Learners keep their own screen. Share only when stuck. Instructor visits rooms in turn, Copilot first |
| Setup (in person) | Tables by platform, 3 to 5 learners. One laptop per learner. Instructor walks the tables, Copilot first |
| Steps per platform | See section 5 (4 cards with the same 6 core steps). No fast-start card. No stretch step in module 2 (decision D2) |
| Materials | `kit/lab-2/` (job card, driver code book, Copilot fallback text, record sheet, README). Case files `m2-crm-export-q2.csv`, `m2-winloss-notes-q2.md`, `m2-check-sample.md`. `modules/m1/kit/kit-m2/` to rebuild before the lab. `kit/kit-m3/` for catch-up after. Instructor only: `case/planted-errors.md`, `case/expected-results.md`, saved demo output |
| Success criteria | The match rate table is complete. Each deal has a source label. Each driver shows its counts. Each flag has the learner's decision. 2 deals audited and a rule added to the brief. One-sentence read of the match rate table written. Check sample passes the 5-item pass condition |
| Debrief questions | What does your match rate table show, in one sentence? Who hears it, and how do you say it so sales does not hear blame? Which check or audit found the error? Which deals did your agent treat as buyer evidence? |
| Fallback path | Cannot use own work: case data. Agent lost or behind: rebuild from `kit-m2` (about 5 minutes). Platform blocked: pair with a learner on another platform. Copilot with no license: `copilot-fallback-instructions-m2.txt`, CRM export pasted as text, notes uploaded or pasted. `.csv` upload fails: paste the text. No file output: full tables in one message (brief rule 7). Agent does not make the error: debrief uses the saved demo output. Behind at the end: load `kit-m3` before module 3 |
| Learner evidence | Match rate table with the learner's one-sentence read of it. Flag report decisions. Audit findings for 2 deals. The brief change (v2 to v3). All on `lab-2-record-sheet.md` |

## 8. Learner kit

Character counts measured with `wc -m` on 2026-11-27. Copilot course budget (spec `copilot_no_license_fallback`): core brief 3,500 or fewer, job card 1,500 or fewer, knowledge file 2,800 or fewer, total 7,800 or fewer. Vendor limit: Instructions 8,000 characters (mb-01). Every `.txt` copy matches its `.md` file (`cmp`).

| File | Loads into | Characters | `.txt` copy |
| --- | --- | --- | --- |
| `lab-2/job-card-win-loss.md` | Knowledge | 1,483 (budget 1,500) | yes |
| `lab-2/driver-code-book.md` (copy of `case/m2-driver-code-book.md`) | Knowledge | 2,284 (budget 2,800) | yes |
| `lab-2/copilot-fallback-instructions-m2.txt` | Copilot Instructions, no license | 7,171 (budget 7,800; limit 8,000) | is a `.txt` |
| `lab-2/lab-2-record-sheet.md` | Not loaded. Learner keeps it | 1,337 (not loaded) | no |
| `lab-2/README.md` | Not loaded | not counted | no |
| `kit-m3/brief-v3.md` | Instructions | 3,094 (budget 3,500) | yes |
| `kit-m3/job-card-problem-backlog.md` (no change) | Knowledge | 1,194 | yes |
| `kit-m3/code-book.md` (no change) | Knowledge | 2,791 | yes |
| `kit-m3/problem-backlog.md` (no change from kit-m2) | Knowledge | 10,004 (a log, not in the fallback instructions) | yes |
| `kit-m3/job-card-win-loss.md` | Knowledge | 1,483 | yes |
| `kit-m3/driver-code-book.md` | Knowledge | 2,284 | yes |
| `kit-m3/driver-log.md` (Q2 rows of `case/m4-evidence-pack.md` Part 1, match rate table, driver counts, flags) | Knowledge | 5,047 (a log, not in the fallback instructions) | yes |
| `kit-m3/lab-2-fix-rules.md` | Not loaded. Handout | 582 | yes |
| `kit-m3/copilot-fallback-instructions-m2-v3.txt` | Copilot Instructions, no license, to rerun job 2 | 7,314 (budget 7,800) | is a `.txt` |
| `kit-m3/README.md` | Not loaded | not counted | no |

Fallback sum check (module 2): brief v2 2,920 + job card 1,483 + driver code book 2,284 = 6,687, plus a 470-character header and separators = 7,171. A learner rule of about 230 characters brings it to about 7,400, still under 8,000. Module 1 D13 estimated about 2,600 characters left for the job card and header: actual use is 1,967.

Knowledge files in the agent after module 2: 6 (2 job cards, code book, driver code book, problem backlog, driver log). Course budget 13.

## 9. Instructor notes

- Timing flex:
  - Behind before the lab: cut the story slot (2.2) and the question on 2.4. Never cut the lab brief (2.10, 2.11) or the data safety box.
  - Behind in the lab: at minute 29 (half day 31), tell learners who have not sent step 6 to skip it. Run it after class. The debrief works from the step 2 run and the case table on 2.13.
  - Behind in the debrief: keep the reveal and the check sample. Cut the match rate read to 2 answers.
  - Ahead: learners do "Done early": run the job on their own deal export, or write the note to sales.
- Common failures and recovery:

| Failure | Recovery |
| --- | --- |
| Agent lost or broken after module 1 | Rebuild from `kit-m2` (about 5 minutes), then do step 1 |
| Copilot: the agent ignores the knowledge files (no license or billing) | Use the no-license box on the Copilot card: `copilot-fallback-instructions-m2.txt` in Instructions, CRM export pasted as text |
| Copilot or Gemini: `.csv` upload fails in chat | Open the file and paste the text. It is 1,855 characters |
| Gemini: adding files to the existing skill fails | Upload the whole skill again with all its files (gm-01) |
| Claude: no file in the answer | Turn on **Code execution and file creation** (**Create and edit files**). Or accept the full tables in one message (brief rule 7) |
| The answer stops halfway (long output) | Send "Continue". Or send "Give the driver log and the match rate table only, then the flag report" |
| The agent runs the problem backlog job instead | Check the prompt says "Run the win/loss job". Check `job-card-win-loss` is in knowledge |
| The agent adds win/loss drivers to the problem backlog | The job card says the job does not change the backlog. Point to it. Rerun. Module 4 joins the two logs |
| The agent proposes a ranking of drivers | The job card says it gives no ranking. Accept the counts. Ignore the ranking, or rerun |
| The agent does not make the planted error (price not near the top, D-2214 CRM only) | Good. Ask the learner which line in the brief or code book kept it out. In the debrief, show the saved demo output |
| The agent codes price as a secondary driver on D-2201, D-2202, D-2203 or D-2212 | These notes mention price but say it did not decide the deal ("Price was a little higher for Rimecore. It did not matter after the pilot." WL-2203). Accept a secondary driver. The match rate uses the primary driver only |
| The agent writes "Distribution buyers leave for alerts" | It breaks the segment rule (brief rule 4): 1 interviewed lost deal on D3 in Distribution. Point to it |
| The agent writes "pattern" or "validated" | Audit finding. Point to brief rule 3. Rerun |
| A learner's own CRM export holds personal data | Stop. Remove names and contact details, or use the case data. Data safety box |
| A learner has no win/loss notes of their own | Use the case data for the lab. Monday action: count the decided deals with a buyer interview |

- Case notes (module builder, checked 2026-11-27 against the case files):
  1. D-2202 (Copperleaf Kitchens, won): the case codes the primary driver as D8 Reseller and install support (`m4-evidence-pack.md` Part 1). An agent may code D2 Install and connectivity. Both are a mismatch with the CRM reason "Price", so the match rate does not change. Accept either and say why.
  2. D-2207 (Breckwood Distribution): the buyer calls the multi-site dashboard "nice to have". D5 as a secondary driver is fair. The primary driver is D3 Alert accuracy.
  3. D-2209 (Ferrow Street Grill Group): the alternative, alarms in a new refrigeration controller, is a substitute in `company.md` but not in the driver code book. So it is a correct flag. CRM competitor "Unknown".
  4. WL-2214 is in the notes file with a WL id. Learners may argue it is an interview. The code book says "interview: a buyer win/loss interview exists for the deal". The buyer did not attend, so it is CRM only.
  5. `case/expected-results.md` says "10 deals (program minimum met)" for the second sample. Do not say it in class. Dan removed the minimum (Gate 2 v2-7). See decision D5.
  6. The driver log in `kit-m3` follows the case state (`m4-evidence-pack.md` Part 1, Q2 rows), so module 4 starts from the same log. Its flag decisions are left to the learner (decision D7).
  7. OI-19 items (I-201 quote 2; F-1108 and F-1214 in lab 5) are covered in module 1 section 9. No module 2 item in OI-19.
- Kept off the slides on purpose: any win/loss figure (W1, W2 figures have no dated primary study; spec `claims_on_slides`). "Many teams do not run win/loss at all" as a finding (decision D11). The term the spec bans for the match rate (PA-04).
