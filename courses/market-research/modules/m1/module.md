# Module 1: Run your first batch and manage it by flags

Course: Advanced AI for Market Research (`market-research`). Stage 3 draft by the module builder, 2026-11-26. Built from `spec.yaml` (Gate 2, approved 2026-11-26), `outline/development-brief.md`, `outline/gate-2-decisions.md` and the case files. The course open (25 minutes before this module) is in `course-open.md`.

## 1. Summary

| Item | Value |
| --- | --- |
| Workflow row and bottleneck | mr-wf-01 (folds mr-wf-05 as a stretch step, decision 11). Turn each new batch of buyer interviews into an updated, checked problem backlog. Bottleneck: synthesis takes days per study, so insight reaches the roadmap late. AI cuts the analysis time, but the work moves to checking AI output (E4, E10, E5) |
| Framework category and focus area | Market. Market Problems |
| Capability Standards (as in spec) | Confirmed by Dan, Pragmatic to confirm. Skills 1.1 Market Problem Identification, 1.3 Market Discovery. Competencies 1.1A, 1.1B, 1.3D |
| Rung | 1, Hand-run batch |
| Minutes (full day / half day) | 70 / 80 |
| Instructor-led / hands-on (minutes, %) | Full day: 28 / 42 = 40% / 60% (8 + 11 + 9 = 28; 33 + 9 = 42). Half day: 32 / 48 = 40% / 60% (9 + 12 + 11 = 32; 38 + 10 = 48). Inside the 40/60 rule (plus or minus 5 points) |
| Planted error and warning level | One vocal buyer ranks near the top: I-104 (P05 Multi-site visibility, 3 quotes, 1 interview). Warning: told ("This batch has one planted AI error. Find it in your audit.") |
| Learner evidence | Tuned brief (v1 to v2 with the single-source flag rule). Flag report decisions for batch 1. Audit findings for 3 problems. The PM's order of the top problems by segment. All on `lab-1-record-sheet.md` |
| Agent after this module (files) | Instructions: brief v2. Knowledge: `job-card-problem-backlog`, `code-book`, `problem-backlog` (after batch 2). Catch-up: `kit/kit-m2/` |

### Slide minutes check

| Arc step | Slides | Full day | Half day | Mode |
| --- | --- | --- | --- | --- |
| Why this matters, workflow and bottleneck | 1.1 to 1.4 | 1 + 3 + 2 + 2 = 8 | 1 + 3 + 2 + 3 = 9 | Instructor-led |
| Live demo | 1.5, 1.6 | 8 + 3 = 11 | 9 + 3 = 12 | Instructor-led |
| Build pattern and lab brief | 1.7 to 1.10 | 2 + 3 + 1 + 3 = 9 | 2 + 4 + 2 + 3 = 11 | Instructor-led |
| Lab 1 | 1.11 | 33 | 38 | Hands-on |
| Debrief | 1.12 to 1.16 | 2 + 3 + 2 + 1 + 1 = 9 | 2 + 3 + 3 + 1 + 1 = 10 | Hands-on |
| Total | 16 slides | 70 | 80 | 28 + 42; 32 + 48 |

Half day: the extra minutes go to the story slot (1.4), the evidence profile (1.8), data safety (1.9), the lab and the order by segment in the debrief (1.14), as in spec `half_day.note`.

### Builder decisions inside the spec

| # | Decision | Why |
| --- | --- | --- |
| B1 | Card step 6 sends batch 1 and batch 2 together in a new chat, with the same prompt. The brief says: run batches in date order, give a flag report per batch, then one backlog | A new chat is the only way to be sure the tuned brief applies on all 4 platforms. A new chat does not see the batch 1 backlog, so the agent reruns batch 1 first. See Questions for Dan, item 1 |
| B2 | Fact labels on slides and cards: "single source" and "one segment only". The source label stays (PM-held or AI-moderated, AI-moderated listed last) | Gate 2 decision C2 drops "AI-moderated only" from learner-facing fact labels. Brief v1 follows C2. See Questions for Dan, item 4 |
| B3 | Opening build check uploads `code-book` as its one sample file | It tests the knowledge upload the lab needs. A Copilot learner with no license finds out in the course open, not in the lab |
| B4 | Audit method: 3 random problems, and at least 1 of them from the top 3 of the proposed ranking | Managers audit what goes into the deck. The rule does not name the error. See Questions for Dan, item 7 |

### Questions for Dan

1. **Step 6 (B1).** The spec card says "Send batch 2". On a new chat, the agent does not see the batch 1 backlog, and the brief change may not apply to an open chat. I send both batches in a new chat. The prompt stays "Run the problem backlog job". The debrief check still works: the batch 1 flag report lists P05, the batch 2 flag report lists P06. Your card test confirms this. OK?
2. **Step 1 is one "add" with two places.** The brief goes in Instructions and 3 files go in Knowledge. I kept it as one step, as in the spec card. If the card test shows people stall here, the fix is a 7th step, which breaks the 6-step rule. Which do you prefer if it fails?
3. **The demo shows the error.** The spec demo runs batch 1 on the template brief, so P05 may show near the top on screen before the lab. The talk track does not comment on it and says "I am not auditing this now. That is your job." The saved demo output is also the debrief fallback (case/planted-errors.md). Option: demo the build only and run batch 1 on screen with the ranking hidden. Keep as written?
4. **"AI-moderated only" (decision C2).** Brief v1, slides and cards drop it. But `case/m1-code-book.md` (fingerprinted) still lists it in the fact label column header, and `case/expected-results.md` uses it for P08 and P07. The agent will likely still apply it. That is harmless: it is a true fact. Do you want the case builder to change the code book header? That needs your yes (fingerprint).
5. **Gemini log save.** The spec (gm-01) says: re-upload the whole skill to update a file. The current Gemini Apps Help skills page (seen 2026-11-26) lists **More**, then **Replace file**, and **Save**. That page shows no date, so it is not a dated vendor doc. The card uses Replace file, with whole-skill re-upload as the backup. The verifier needs a dated Google doc. OK?
6. **Screen names I could not verify** (written generically on the cards): ChatGPT, the button that adds files to a project (the page says only "project sources list"). Claude, how to delete a knowledge file and how to start a chat inside a project. Gemini, the name of the field for the skill name and the Edit button for an existing skill. Copilot, how to send a file in the agent chat (the page names **Upload images and files** under **+** on the Describe tab only). Please note the real labels in the card test.
7. **Audit hint (B4).** "Include at least 1 from the top 3" is good practice, but it makes the error easier to find. Keep it for lab 1 (warning: told), and drop it from later labs?
8. **Copilot chat upload and paste** are still not verified (G2-PF-02, G2-PF-03). The Copilot card says "upload, or paste the text". Your card test of the Copilot card answers this. A second tester who did not write the card should also test it (PRD card test).
9. **kit-m2 Copilot fallback for module 2** needs the win/loss job card, which the module 2 builder writes. Brief v2 is 2,878 characters and the driver code book is 2,284, so the win/loss job card has about 2,600 characters left under the 7,800 course budget. I put a module 1 rerun fallback (`copilot-fallback-instructions-m1-v2.txt`, 7,139) in kit-m2 for now.
10. **Story slot (1.4).** I did not write a story. The slot tells the instructor what kind of story fits and to skip it if they have none. Inventing a client story would break decision 43. Do you have a real one to add?
11. **ChatGPT files per project.** The Projects page (seen 2026-11-26) now says Go and Plus have 25 files. The File uploads FAQ (cg-03) said 20 for Plus. Lab 1 adds 3 files, so no impact. The spec rule "use 20" stays.
12. **Claude setting name.** The Claude files page (seen 2026-11-26) says the toggle **Code execution and file creation** is now called **Create and edit files** in the updated Settings layout. The readiness checklist should name both.
13. **Check sample pass condition on the card.** PRD rule 7 puts it at the end of each card. It names P07 "1 interview, not 3", which points at the kind of error. The card labels it "run this in the debrief". OK for a "told" lab?

## 2. Slides and talk track

### Slide 1.1: Module 1. Run your first batch and manage it by flags
- Layout: Chapter Break
- Minutes: 1 (half day 1)
- On-slide text: MODULE 1. Run your first batch and manage it by flags. Promise: "Build the agent. Run a batch. Decide what the flags mean." Bullets: Build the Market Evidence Agent from a template. Decide each flag and audit 3 problems. Tune the brief and decide the order of your top problems.
- Visual intent: Teal side band, "MODULE 1" tag. Small rung icon: rung 1 of the ladder lit.
- Sources: none

Notes:
```
POINT: In this module you build the Market Evidence Agent and manage its first batch of interviews by its flags.
Talk Track:
You checked in the opening that your platform works.
Now you build the agent you keep all day.
Its first job: turn a batch of buyer interviews into a problem backlog.
A problem backlog is a running list of market problems, with the evidence for each one.
You will not do the synthesis yourself.
You will write the brief, read the flags, audit a sample and decide.
That is the agent manager's job.
TRANSITION: First, why this workflow, and what slows it down.
```

### Slide 1.2: Interviews pile up. Insight reaches the roadmap late
- Layout: Blank
- Minutes: 3 (half day 3)
- On-slide text: Headline: "Interviews pile up. Insight reaches the roadmap late." Line 1: "71% of 677 product people say they do not spend enough time with customers or on the market." (Product Focus, 2026). Line 2: "AI cuts the analysis time. The work moves to checking." Workflow strip: "New batch of interviews, then an updated, checked problem backlog."
- Visual intent: Headline with "late" in orange. One large figure "71%" in teal with its source line under it. A simple left-to-right strip: interview notes, then the backlog table.
- Sources: N5 (statistic, primary, Product Focus 2026). E4 (claim, 3 sources). E10 (vendor, talk track only). E12 (peer-reviewed study, talk track only)

Notes:
```
POINT: Interview synthesis is slow, AI makes it faster, and the real work moves to checking what the AI produced.
Talk Track:
Here is the workflow for this module.
A new batch of buyer interviews arrives, every few weeks.
Someone has to turn it into a list of market problems, with the evidence for each one.
That takes days per study.
So by the time the insight reaches the roadmap, the roadmap has moved on.
[POINT TO THE 71%]
And PMs do not have spare time to do it.
In a 2026 survey of 677 product people, 71% said they do not spend enough time with customers or on the market.
AI changes the work.
It codes interviews much faster than you can.
But the work does not go away. It moves.
In a 2026 survey by Condens, a research tool vendor, 71% of 332 research practitioners said that checking AI output still takes significant time.
A 2026 peer-reviewed study went further. Two leading models applied more codes than a human coder did, and agreed with the human far less than two humans agreed with each other. The chat-based workflow saved no time.
So the question is not "can AI do synthesis?"
It is "how do you manage an AI that does synthesis, batch after batch?"
[IF ASKED ABOUT SPEED FIGURES] Vendor speed figures exist. We do not use them. They come from tool vendors with their own data.
TRANSITION: You may already know how to do one pass of AI synthesis. This module starts where that stops.
```

### Slide 1.3: Start where one-pass synthesis stops
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: Left, "You already know": One-pass synthesis: AI codes one set of interviews, once. The quote check: each quote is found word for word in its source. Right, "New today": Batch after batch. A problem backlog that grows. Flags you decide. Audits you run. A brief you tune.
- Visual intent: Two columns. Left column gray (known). Right column teal (new). Right column is larger.
- Sources: none (registry: PDW-AI)

Notes:
```
POINT: This module does not reteach one-pass synthesis or the quote check; it teaches how to manage an agent that runs synthesis on every new batch.
Talk Track:
Two ideas you may know from Product Discovery with AI.
One-pass synthesis: you give the AI one set of interviews, and it codes them once.
The quote check: each quote must be found word for word in its source interview.
We take both as given. Your agent runs the quote check on its own output.
What is new today is time.
Interviews arrive in batches. The backlog grows. Problems grow or fade.
So you need an agent that keeps the backlog, and a way to manage it without reading every line.
That way is flags, audits and a brief you tune.
[IF A LEARNER HAS NOT TAKEN PRODUCT DISCOVERY WITH AI] You do not need it. The two definitions on the left are all you need.
TRANSITION: So who does what?
```

### Slide 1.4: The agent does the workflow. You manage it
- Layout: Blank
- Minutes: 2 (half day 3)
- On-slide text: Left, "The agent": Codes each interview. Checks each quote. Merges new problems into the backlog. Proposes a ranking with reasons. Sends flags to you. Right, "You, the agent manager": Write the brief. Set quality checks and hand-off rules. Decide each flag. Audit a sample. Decide the order.
- Visual intent: Two columns with a dividing line. Right column header in orange. Small icon of a flag next to "Decide each flag".
- Sources: none

Notes:
```
POINT: The agent does the routine work of the workflow, and the PM manages it by the brief, the checks, the flags and the audit.
Talk Track:
Here is the split for the whole day.
The agent codes, checks quotes, merges and proposes.
You write the brief, set the checks and the hand-off rules, decide each flag, audit, and decide.
Two words you will hear all day.
A quality check is a test the agent runs on its own output before it reports. For example: each quote found word for word.
A hand-off rule says when the agent stops and gives an item to you. That item goes into the flag report.
The flag report is the short list of items the agent hands you to decide.
[OPTIONAL STORY SLOT, 1 MINUTE, 2 IN THE HALF DAY. Topic: a client team that put a reworded customer quote into a roadmap deck, and what it cost them. Use only a story you heard from a client team or from Pragmatic's work with companies. Tell it as their story, never as your own. If you have no such story, skip this slot and spend the minute on the split above.]
TRANSITION: Let me build it in front of you.
```

### Slide 1.5: Live demo. Build the Market Evidence Agent from the template
- Layout: 1_prompt
- Minutes: 8 (half day 9)
- On-slide text: LIVE DEMO. "Build the Market Evidence Agent from the template." Running example: Larkspan Systems, batch 1 (8 interviews). 8 MIN (half day: 9 MIN).
- Visual intent: Orange "LIVE DEMO" tag. Platform logo for the demo platform (Claude). Small list of the 4 kit files.
- Sources: cl-pj-01 (platform matrix, verified). Demo script in section 3

Notes:
```
POINT: Building the agent from the template takes a few minutes, and the first run gives you a backlog, a proposed ranking and a flag report to manage.
Talk Track:
[SWITCH TO THE DEMO PLATFORM. FOLLOW THE DEMO SCRIPT IN SECTION 3, STEPS 1 TO 5]
I demo on Claude. Your step card has the same steps for your platform.
The case company is Larkspan Systems. It makes wireless temperature sensors and the cloud software that watches them.
Three segments: Distribution, Food service, Pharmacy and lab.
Here is the kit. Four files.
The brief goes into the instructions. It holds the rules for every job.
The job card, the code book and the empty problem backlog go into knowledge.
[PASTE THE BRIEF. SAVE]
Look at "My rules" at the bottom of the brief. It is empty. You fill it after your audit.
[ADD THE 3 FILES]
Now the run. New chat. Batch 1, and one prompt: "Run the problem backlog job".
[SEND BATCH 1. WHILE IT RUNS:]
While it runs, notice what I did not do.
I did not write a prompt per step. I did not paste the code book into the chat.
The brief and the job card hold all of that. This is what makes it an agent, not a prompt.
[WHEN THE RUN ENDS, OPEN THE OUTPUT FILE]
TRANSITION: Now the part that matters: how you read what it gives you.
```

### Slide 1.6: Read three things: the evidence profile, the proposed ranking, the flag report
- Layout: Blank
- Minutes: 3 (half day 3)
- On-slide text: 1. Evidence profile: the facts for each problem. 2. Proposed ranking: the agent's order, with a reason for each. "The PM decides the order." 3. Flag report: what the agent stopped on. Your decisions go here.
- Visual intent: A cropped, readable mock of the three output parts from the demo run (P01 row only, the ranking title, two flag rows). Large type, no full table. Numbers 1 to 3 in orange circles.
- Sources: none (case output, `case/expected-results.md`)

Notes:
```
POINT: You manage the agent by reading three parts of its output, not by redoing its work.
Talk Track:
[DEMO SCRIPT STEPS 6 TO 8. STAY ON THE SCREEN, THEN SHOW THIS SLIDE AS THE SUMMARY]
Part one, the evidence profile. One row per problem.
Look at P01, alert fatigue. 4 interviews. 4 accounts. All 3 segments. One urgency quote, from I-101.
Part two, the proposed ranking. Look at the title: "Proposed ranking. The PM decides the order."
The agent proposes. It gives a reason for each rank. You decide.
Part three, the flag report. These are items the agent stopped on.
Here: a note from I-102 that fits no code. And Pharmacy and lab has no PM-held interview.
The decision column is blank. That is your column.
[DO NOT COMMENT ON THE LOWER RANKS. IF A LEARNER ASKS ABOUT ONE:] Good question. Hold it for your audit.
I am not auditing this run now. That is your job in the lab.
[SAVE THE DEMO OUTPUT FILE. YOU MAY NEED IT IN THE DEBRIEF]
TRANSITION: Before you build, here is the loop you will run.
```

### Slide 1.7: The manager loop
- Layout: Blank
- Minutes: 2 (half day 2)
- On-slide text: Write the brief. Set quality checks. Set hand-off rules. Run. Review the flag report and the proposed ranking. Audit a sample. Tune the brief. Run again.
- Visual intent: A circle of 8 steps. "Audit a sample" and "Tune the brief" in orange. A small "You are here: lab 1" marker on the first full turn.
- Sources: none (spec `course_agent.manager_loop`)

Notes:
```
POINT: The agent manager runs one loop: brief, checks, hand-off rules, run, review, audit, tune, run again.
Talk Track:
This loop is the whole course.
Today in lab 1 you go round it once.
The template gives you the brief, the checks and the hand-off rules.
You run it, review the flag report and the ranking, and audit a sample.
Then you tune the brief: you add one rule for what your audit found.
And you run again.
If you have seen boundaries and guardrails in an agent course: hand-off rules are the same idea, written for one job and checked every run.
Your audit is the step that makes the loop work.
The checks catch what you predicted. The audit catches what you did not.
TRANSITION: To audit, you need to read an evidence profile well. Here is what is in it.
```

### Slide 1.8: How the agent reports the evidence
- Layout: Blank
- Minutes: 3 (half day 4)
- On-slide text: Evidence profile, facts only: Interviews (count interviews, not quotes). Accounts, segments, personas. Urgency, with one quote. Pervasiveness: how many accounts and segments. Willingness to pay clues. Source dates. Source type: PM-held interview (AI-moderated, where a team uses them). Fact labels: "single source" (1 interview, however many quotes). "one segment only". Bottom line: "No magic number. Priority is relative."
- Visual intent: One evidence profile card, laid out as a vertical list. Fact labels shown as two gray tags. Bottom line in orange.
- Sources: none (spec `course_agent.problem_backlog`; workbook skill 1.1D terms)

Notes:
```
POINT: The agent reports each problem's evidence as facts in a profile, and no number in the brief decides that a problem is real.
Talk Track:
Three terms first. They come from Pragmatic's way of judging a market problem.
Urgency: how pressing the problem is for the buyer. The agent shows it with one quote.
Pervasiveness: how many buyers have it. Here: how many accounts and how many segments.
Willingness to pay clues: signs that buyers spend, or would spend, money or effort to solve it.
Now the counts. The agent counts interviews, not quotes.
One buyer can give you five great quotes. That is still one interview.
The source type says who ran the interview. Usually a PM.
Some teams use AI-moderated interviews: an AI tool runs the interview and a PM reads the transcript. Few enterprise teams do this today. The label just tells you which is which.
Fact labels are facts, not verdicts.
"Single source" means one interview, however many quotes.
"One segment only" means all the evidence comes from one segment.
A labeled problem stays in the backlog. You track it over time.
[POINT TO THE BOTTOM LINE]
And there is no magic number. Nothing in the brief says "3 interviews makes it real".
Priority is relative. You judge each problem against the others in the backlog.
[HALF DAY: USE THE EXTRA MINUTE. ASK: "Which of these facts would you check first in a problem ranked number 1?" TAKE 2 ANSWERS]
TRANSITION: One more thing before you start: what this backlog keeps.
```

### Slide 1.9: Know what your backlog keeps
- Layout: Blank
- Minutes: 1 (half day 2)
- On-slide text: "Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss." Line under it: "A backlog keeps data longer than a one-off prompt. Decide what it may keep, and for how long."
- Visual intent: Standard data safety box (same on every lab). Second line in teal.
- Sources: none (spec `data_safety_note`)

Notes:
```
POINT: An agent that keeps a backlog stores interview data longer than a one-off prompt, so you decide what it keeps and for how long.
Talk Track:
This is the data safety note. It is on every lab and every step card.
[READ THE BOX ALOUD]
One thing is new with an agent.
A one-off prompt forgets your interview when you close the chat.
This agent keeps a backlog file, and you save it after every lab.
So decide what it may keep. Account names? Quotes? For how long?
On your own work: use the tool your company approved, and only interviews you have consent for.
If you cannot, use the Larkspan case data. It is fictional.
[HALF DAY: ASK ONE LEARNER WHAT THEIR COMPANY ALLOWS IN THEIR TOOL]
TRANSITION: Here is your lab.
```

### Slide 1.10: Lab 1 brief
- Layout: Activity
- Minutes: 3 (half day 3)
- On-slide text: ACTIVITY. Lab 1: Run your first batch. Goal: Delegate interview synthesis to an agent that keeps a problem backlog. Manage it by its checks and flags. Steps: 1. Add the kit to your agent. 2. Send batch 1: "Run the problem backlog job". 3. Decide each flag. 4. Audit 3 random problems. 5. Add one flag rule to the brief. 6. Send both batches in a new chat. Success check: The backlog updates after batch 2. Each problem has an evidence profile and any fact labels that apply. The agent proposes a ranking with a reason for each problem. The agent writes "pattern" and "validated" nowhere. Each flag has your decision. You recorded 3 audit findings and added a flag rule. Orange box: "This batch has one planted AI error. Find it in your audit."
- Visual intent: Orange "ACTIVITY" band. Steps numbered on the left. Success check on the right. Planted error line in an orange box at the bottom.
- Sources: none

Notes:
```
POINT: In lab 1 you build the agent, run two batches, and manage it by its flags and your audit.
Talk Track:
The goal of this activity is to delegate interview synthesis to an agent and manage it by its checks and flags.
The core message: do not do the work between AI steps. Set the job, the checks and the hand-off rules. Read the evidence, then decide the order.
Six steps. Your step card has them for your platform.
[WALK THE 6 STEPS IN ONE LINE EACH]
On your own work: 5 to 15 of your own interview notes, from an approved tool, with consent.
Otherwise use the Larkspan batches. Both paths use the same steps.
Record your flag decisions and audit findings on the lab 1 record sheet in your kit. That is your evidence for this lab.
[POINT TO THE ORANGE BOX]
This batch has one planted AI error. Find it in your audit.
The quote check will not find it for you.
Breakout rooms are by platform. Build and save your own agent. Share your screen only when someone is stuck.
New to your platform's builder? Start with the fast-start card for your platform.
Done early? The stretch steps are at the end of your card.
TRANSITION: [OPEN BREAKOUT ROOMS BY PLATFORM. START THE TIMER: 33 MINUTES, HALF DAY 38]
```

### Slide 1.11: Lab 1: Run your first batch
- Layout: Activity
- Minutes: 33 (half day 38)
- On-slide text: ACTIVITY. 33 MIN (half day 38 MIN). Time guide: Minutes 0 to 5: add the kit (fast-start card if new). 5 to 12: batch 1 run. 12 to 17: decide each flag. 17 to 25: audit 3 problems. 25 to 28: add your flag rule. 28 to 33: both batches, new chat. Half day: add 5 minutes to the audit and your flag rule. "Build and save your own agent. Share your screen only when someone is stuck."
- Visual intent: Orange band. A simple timeline bar with the 6 blocks. Room by platform shown as 4 small tiles.
- Sources: none

Notes:
```
POINT: Learners build and run the agent from their step card, on their own work or the case data.
Talk Track:
The goal of this activity is to run one full turn of the manager loop on your own agent.
[VISIT EACH ROOM IN TURN. START WITH COPILOT, THEN GEMINI, THEN CHATGPT, THEN CLAUDE]
[AT MINUTE 5: ANYONE WHO HAS NOT SENT BATCH 1 GETS HELP FIRST]
[AT MINUTE 12: "If your run is not done, read the flag report while you wait."]
[AT MINUTE 17: "Start your audit now. Open the source interviews. Do not trust the profile; check it."]
[AT MINUTE 25: "Write your rule now, even if your audit is not done."]
[AT MINUTE 30: "Send both batches now, in a new chat."]
[COMMON FAILURES AND RECOVERY: SEE SECTION 9]
[DO NOT REVEAL THE ERROR. IF A LEARNER ASKS "IS THIS IT?", ASK: "Which fact in the profile tells you?"]
TRANSITION: [CLOSE ROOMS AT MINUTE 33, HALF DAY 38] Bring your record sheet. Let's see what you found.
```

### Slide 1.12: What did your audit find?
- Layout: debrief
- Minutes: 2 (half day 2)
- On-slide text: DEBRIEF. Which problem did your agent rank near the top? What did its evidence profile say? Which check or audit found the error? (Reveal after answers:) I-104: 3 quotes, 1 interview, 1 account. The quote check passed.
- Visual intent: Navy "DEBRIEF" band. 3 questions. The reveal line appears on click, with the P05 profile row from the demo output.
- Sources: none (case `planted-errors.md` lab 1, `expected-results.md`)

Notes:
```
POINT: One vocal buyer looked like a top market problem, and only the evidence profile and the audit showed it was one interview.
Talk Track:
[ASK THE 3 QUESTIONS. TAKE 2 OR 3 ANSWERS, ONE FROM EACH PLATFORM IF YOU CAN]
[REVEAL]
Here is the planted error.
Interview I-104. Marrowby Grocers, Food service. Director of operations. A PM-held interview, the longest in the batch.
Three strong quotes on one problem: P05, multi-site visibility. One is a renewal threat.
On the template brief, the agent ranks P05 near the top, or first in Food service.
Why? Three quotes and high urgency look strong.
The quote check passes. All 3 quotes are word for word.
But look at the evidence profile. 1 interview. 1 account. 1 segment.
P01 and P02 have 4 interviews and 4 accounts each, across all 3 segments.
The other two Food service interviews, I-103 and I-105, do not raise P05 at all.
And I-104 says the alerts and the reports are "fine".
This is the noisy few against the quiet many. A loud buyer can feel like the market.
In batch 2, a second buyer, I-111, mentions it: "it's not my top problem".
[IF NO PLATFORM IN THE ROOM MADE THE ERROR, SHOW THE SAVED DEMO OUTPUT]
[IF A LEARNER'S AGENT WROTE "food service buyers want": "That breaks the segment rule. One interview in a segment is not a segment claim."]
TRANSITION: Did your new rule fix it? Let's test it on data you have not seen.
```

### Slide 1.13: Check sample
- Layout: Activity
- Minutes: 3 (half day 3)
- On-slide text: ACTIVITY. 3 MIN. New chat on your tuned agent. Send `m1-check-sample.md` with "Run the problem backlog job". Compare with the pass condition at the end of your step card.
- Visual intent: Orange band, timer 3 MIN. One-line instruction. Small image of the card's pass condition box.
- Sources: none (case `m1-check-sample.md`, `expected-results.md`)

Notes:
```
POINT: A second sample the learner has not seen shows if the tuned brief works.
Talk Track:
The goal of this activity is to test your tuned brief on new data.
New chat. Send the check sample. Same prompt.
It has 4 interviews you have not seen. Then compare with the pass condition on your card.
[START A 3-MINUTE TIMER]
[AFTER 3 MINUTES, ASK: "Hands up if your agent passed all 5 items." THEN: "Which item failed?"]
[IF P07 IS RANKED ABOVE P01 OR P04, OR SHOWS 3 INTERVIEWS: "Look at your rule. Does it say interviews, not quotes? Add the optional ranking rule from your card after class."]
[IF THE AGENT ALSO CODES I-201 QUOTE 2 AS P02: "That is a fair reading. The insurer asks for records. P07 still shows 1 interview."]
TRANSITION: So who decides what comes first?
```

### Slide 1.14: No magic number. You decide the order
- Layout: debrief
- Minutes: 2 (half day 3)
- On-slide text: DEBRIEF. Priority is relative: judge each problem against the others. Decide the order of your top problems in each segment. The test: can you predict that the next buyer of this persona will raise it? Only you call a pattern.
- Visual intent: Navy band. Three segment columns (Distribution, Food service, Pharmacy and lab) with an empty "your top problem" slot in each.
- Sources: none (case `expected-results.md` lab 1)

Notes:
```
POINT: The agent proposes a ranking, but only the PM decides the order by segment and calls a pattern.
Talk Track:
Your agent proposed a ranking. That is a proposal.
Now you decide. Take one minute. On your record sheet, write your top problem in each segment.
[1 MINUTE. HALF DAY: 2 MINUTES, THEN TAKE ANSWERS FROM 2 SEGMENTS]
Here is a test you can use. Can you predict that the next buyer of this persona will raise it?
If you cannot, it may not be a pattern yet. That is your call, not the agent's.
The agent never writes "pattern" or "validated". You do.
Here is what the case PM decided after batch 2.
Order: P01, P02, P08, P03, P06, P05, P04, P07.
Top in Distribution: P01 and P02. Food service: P03. Pharmacy and lab: P08.
P06 moved down. Buyers disagree on it: two want their own managers on night alarms, two want a service. So it is a research question first.
Your order can differ. What matters is that you can defend it with the evidence profile.
TRANSITION: So what do you do on Monday?
```

### Slide 1.15: What you do Monday
- Layout: Blank
- Minutes: 1 (half day 1)
- On-slide text: "Run your agent on your last interview batch. Audit 3 problems before you share anything."
- Visual intent: One line, large type. Calendar icon with "Monday".
- Sources: none

Notes:
```
POINT: The first real use of the agent is on your own last batch of interviews, with an audit before anything is shared.
Talk Track:
On Monday, find your last batch of interview notes.
Run your agent on it, in your approved tool.
Then audit 3 problems before you share anything with anyone.
Your kit has the template and the record sheet, so you can do this without the class.
TRANSITION: Last step: save your log so the next module can read it.
```

### Slide 1.16: Save your log
- Layout: Activity
- Minutes: 1 (half day 1)
- On-slide text: ACTIVITY. 1 MIN. 1. Download the updated backlog from your batch 2 run (step 6). 2. Replace the old problem-backlog file in your agent's knowledge. Your card has the steps for your platform.
- Visual intent: Orange band. Two numbered steps, large. Small platform row: Claude, ChatGPT, Copilot, Gemini.
- Sources: cl-pj-01, cg-01, mb-02, gm-01 (platform matrix); vendor docs on the cards

Notes:
```
POINT: Saving the backlog to the agent's knowledge is what lets the next job build on this one.
Talk Track:
The goal of this activity is to save your backlog so module 3 can add to it.
Take the backlog from your batch 2 run. Not the check sample run.
Download it. Then replace the old problem-backlog file in your agent's knowledge.
Your card says how for your platform.
Copilot without a license: keep the file on your computer. You paste it in chat next time.
If you are behind, kit-m2 has the backlog after batch 2. You can load that instead.
TRANSITION: [BREAK, OR MODULE 2 IN THE HALF DAY]
```

## 3. Demo script

Platform: Claude (Project). Before class: build the project "Market Evidence Agent" as in the opening build check, turn on **Code execution and file creation** (now also called **Create and edit files**), and do one rehearsal run of batch 1. Save the rehearsal output and screenshots of it in your instructor folder. Keep a ChatGPT Project with the same kit as the backup.

| Step | Instructor does | Screen shows | If it fails |
| --- | --- | --- | --- |
| 1 | Open **Projects**, then the project "Market Evidence Agent" | The project page with the 3-line starter instruction and `code-book` from the build check | Create it now: **+ New Project**, name "Market Evidence Agent". Say: "This is what you did in the build check." |
| 2 | Select **Set project instructions**. Replace the starter text with all of `brief-v1.md`. Select **Save instructions** | The brief in the instructions panel. "My rules: None yet." at the end | If the panel will not save, paste the brief as the first chat message instead and say so. Continue |
| 3 | Select **+** in project knowledge. Add `job-card-problem-backlog.md` and `problem-backlog.md` (`code-book.md` is already there) | 3 files in project knowledge | Paste the file texts into the chat with the run in step 4 |
| 4 | Start a new chat in the project. Upload `m1-interviews-batch-1.md`. Send "Run the problem backlog job" | The agent codes 8 interviews. It returns a downloadable file, or the full tables in one message, and a short summary with the number of flags | If no file: say "No file today. Rule 7 in the brief asks for the full tables in one message." If the run fails: switch to the ChatGPT backup. If both fail: show the rehearsal output |
| 5 | Open the output file | Problem backlog table, proposed ranking, flag report, "what changed" bullets | Show the rehearsal output file |
| 6 | Point to the P01 row | P01 Alert fatigue: 4 interviews (I-101 PM-held; I-102, I-105, I-107 AI-moderated), 4 accounts, Distribution 2, Food service 1, Pharmacy and lab 1. Urgency quote from I-101 | If the counts differ, say: "That is exactly what an audit is for." Do not fix it live |
| 7 | Point to the ranking title and 2 reasons | "Proposed ranking. The PM decides the order." Each rank with a reason from the profile | If the title is missing, say: "The brief asks for it. A missing title is an audit finding." |
| 8 | Point to the flag report | Flags for the I-102 note that fits no code (temperature proof for a distributor's customers) and for Pharmacy and lab with no PM-held interview (I-107, I-108). Blank PM decision column | If a flag is missing, say: "Hand-off rules are not perfect. That is why you audit." |
| 9 | Download the output file and save it | The file in your instructor folder | Use the rehearsal output in the debrief |

Do not audit or comment on lower ranks on screen. P05 may show near the top. That is the lab's planted error.

## 4. Lab brief

- Goal: Delegate interview synthesis to an agent that keeps a problem backlog, and manage it by its checks and flags.
- Core message: Do not do the work between AI steps. Set the job, the checks and the hand-off rules. Read the evidence, then decide the order.
- PM decision: The order of the market problems in each segment, which problems go forward to prioritization, and which need more discovery. The agent proposes a ranking. Only the PM decides the order and calls a pattern.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Teaching point: an agent that keeps a backlog stores sensitive data longer than a one-off prompt. Decide what the backlog may keep and for how long.
- Setup: Zoom breakout rooms by platform, 3 to 5 learners. In person: tables by platform. Each card starts: "Build and save your own agent. Share your screen only when someone is stuck."
- Inputs: Own work: 5 to 15 of your own interview notes or transcripts, from an approved tool, with consent. Case: `kit-m1-template` (brief, job card, code book, empty backlog), `m1-interviews-batch-1.md` and `m1-interviews-batch-2.md` (run), `m1-check-sample.md` (debrief check). Files this lab: 6 (3 to the agent, 3 in chat).
- Planted error warning: Told. "This batch has one planted AI error. Find it in your audit."
- Success check: Batch 2 run. The backlog updates. Each problem has an evidence profile and any fact labels that apply. The agent proposes a ranking with a reason for each problem. The agent writes "pattern" and "validated" nowhere. Each flag report item has your decision. You recorded 3 audit findings and added a flag rule to the brief.
- Learner evidence: Tuned brief (v1 to v2 with the single-source flag rule). Flag report decisions for batch 1. Audit findings for 3 problems. The PM's order of the top problems by segment. Recorded on `lab-1-record-sheet.md`.

## 5. Step cards

All four cards have the same 6 core steps. Saving is in each card header, not a step. Learners use the kit in `kit/kit-m1-template/` and the run files from the case folder. Copilot learners use the `.txt` copies.

### Card: Claude
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Market Evidence Agent" from the opening build check.
- Saves: **Save instructions** saves the instructions. Files save when you add them. Chats save as you go.
- Check date and vendor doc: 2026-11-26. Claude Help Center, "How can I create and manage projects?" (https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects, "Updated over 2 weeks ago", seen 2026-11-26). "Create and edit files with Claude" (https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude, "Updated yesterday", seen 2026-11-26).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | Add the kit: `brief-v1` in **Set project instructions**, the other files in project knowledge with **+**. |
| 2 | In a new chat in the project, send batch 1 with the prompt "Run the problem backlog job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit 3 random problems against the source interviews, with the checklist on your record sheet. |
| 5 | Add one flag rule for what you found under "My rules" in the project instructions. |
| 6 | In a new chat, send batch 1 and batch 2 with the prompt "Run the problem backlog job". |

Notes: `code-book` may already be in knowledge from the build check. Skip a file that is already there. No file in the answer? Check that **Code execution and file creation** is on in **Settings**, then **Capabilities**.

**Start here with sample data:** Kit: `brief-v1.md`, `job-card-problem-backlog.md`, `code-book.md`, `problem-backlog.md`. Batch 1: `m1-interviews-batch-1.md`. Batch 2: `m1-interviews-batch-2.md`. Own work: replace `code-book` with your codes in the same format. Label each interview with its date, segment and PM-held or AI-moderated.

**Pass condition (second sample, run in the debrief):** New chat. Send `m1-check-sample.md` with "Run the problem backlog job". Pass if: (1) P07 shows 1 interview, not 3, with the labels "single source" and "one segment only". (2) The proposed ranking puts P07 below P01 and P04, and the reason names the interview count. (3) The agent writes "pattern" or "validated" for no problem. (4) The flag report says Pharmacy and lab has no PM-held interview (I-204), and lists P07 (all 3 quotes from I-201). (5) Every quote is word for word in the sample.

**Stretch (only where verified):**
- Screening (all platforms): send `m1-stretch-applicants.md` with the prompt "Screen these applicants against the study criteria. Give me only the edge cases."
- Custom skill (Claude, all plans, code execution on; platform matrix cl-cl-03, verified 2026-11-20): turn the problem backlog job into a skill in **Customize**, then **Skills**.

### Card: ChatGPT
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the Project "Market Evidence Agent" from the opening build check. Plan: Go or Plus or higher.
- Saves: As you go.
- Check date and vendor doc: 2026-11-26. OpenAI Help Center, "Projects in ChatGPT" (https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt, "Updated: 3 days ago", seen 2026-11-26).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | Add the kit: `brief-v1` in **•••**, then **Project settings**, the other files to the project's files. |
| 2 | In a new chat in the project, send batch 1 with the prompt "Run the problem backlog job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit 3 random problems against the source interviews, with the checklist on your record sheet. |
| 5 | Add one flag rule for what you found under "My rules" in **Project settings**. |
| 6 | In a new chat, send batch 1 and batch 2 with the prompt "Run the problem backlog job". |

Notes: `code-book` may already be in the project from the build check. Skip a file that is already there. No file in the answer? The brief asks for the full tables in one message. That is fine.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run in the debrief):** Same as the Claude card.

**Stretch (only where verified):**
- Screening: same as the Claude card.
- Skill: ChatGPT skills are on business plans only, and not verified for this course. Not on this card.

### Card: Copilot agent builder
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the agent "Market Evidence Agent" from the opening build check. To open it: **All agents**, then **...** next to it, then **Edit**.
- Saves: **Create** the first time. **Update** after each change.
- Check date and vendor doc: 2026-11-26. Microsoft Learn, "Build agents with Agent Builder" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents, "Last updated on 2026-11-16"). "Add knowledge sources" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge, "Last updated on 2026-11-16"). "Share and manage agents" (https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents, "Last updated on 2026-11-16"). All seen 2026-11-26.
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | On the **Configure** tab, add the kit: `brief-v1.txt` text in **Instructions**, the other `.txt` files with **Upload**. |
| 2 | In the agent chat, send batch 1 with the prompt "Run the problem backlog job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit 3 random problems against the source interviews, with the checklist on your record sheet. |
| 5 | Add one flag rule for what you found under "My rules" in **Instructions**. |
| 6 | In a new chat, send batch 1 and batch 2 with the prompt "Run the problem backlog job". |

Notes: Use the `.txt` copies. Copilot does not list `.md` as a knowledge file type. To send a batch, upload the file in chat. If upload fails, paste the text. Download any file the agent makes in the same session. Copilot keeps it for that session only.

**No Copilot license or billing?** Your agent cannot read Knowledge files. Do this instead:
1. Paste all of `copilot-fallback-instructions-m1.txt` into **Instructions**. Add no Knowledge files.
2. Do the steps above. Paste each batch as text in chat.
3. At step 5, add your rule under "My rules" in **Instructions**.
If the instructions do not fit, keep only `brief-v1.txt` in **Instructions**. Paste the job card and the code book in chat at the start of each run. The fallback agent does one job at a time.

**Start here with sample data:** Kit: `brief-v1.txt`, `job-card-problem-backlog.txt`, `code-book.txt`, `problem-backlog.txt`. Batch 1: `m1-interviews-batch-1.md`. Batch 2: `m1-interviews-batch-2.md`. Own work: as on the Claude card.

**Pass condition (second sample, run in the debrief):** Same as the Claude card.

**Stretch (only where verified):**
- Screening: same as the Claude card.
- The schedule and second-agent stretch steps are not available on this platform in this course.

### Card: Gemini
Build and save your own agent. Share your screen only when someone is stuck.
- Your agent: the skill "market-evidence-agent" from the opening build check. Skill names use lowercase and hyphens. Find it in **Customize**, then **Skills**. This is a Gemini skill. Gems are now skills.
- Saves: **Create** the first time. **Save** after each change.
- Check date and vendor doc: 2026-11-26. Gemini Apps Help, skills page (https://support.google.com/gemini?p=pn_skills, page shows no date, seen 2026-11-26). Google Workspace Updates, "Share skills and add files from Drive, Notebook and Photos to skills in the Gemini app" (https://workspaceupdates.googleblog.com/2026/11/share-skills-add-files-from-Drive-Notebook-Photos-to-skills-Gemini-app.html, 2026-11-16).
- Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

| Step | Do this |
| --- | --- |
| 1 | Add the kit to your skill: `brief-v1` text in **Instructions**, the other files with **Add**. |
| 2 | In a new chat, send batch 1 with the prompt "/market-evidence-agent Run the problem backlog job". |
| 3 | Write your decision for each flag report item on your record sheet. |
| 4 | Audit 3 random problems against the source interviews, with the checklist on your record sheet. |
| 5 | Add one flag rule for what you found under "My rules" in the skill **Instructions**. |
| 6 | In a new chat, send batch 1 and batch 2 with the prompt "/market-evidence-agent Run the problem backlog job". |

Notes: Type **/** in the chat and pick your skill from the list. Do not turn on Canvas or Deep Research. They do not work in skills. If an upload fails, paste the text.

**Start here with sample data:** Same files as the Claude card.

**Pass condition (second sample, run in the debrief):** Same as the Claude card. Use the prompt "/market-evidence-agent Run the problem backlog job".

**Stretch (only where verified):**
- Screening: same as the Claude card.
- The schedule and second-agent stretch steps are not available on this platform in this course.

### Fast-start cards (module 1 only)

For learners new to the builder. One annotated screenshot per card (Stage 4 adds it): where to start, and which field the brief goes in.

| Platform | 1. Open | 2. The brief goes in | 3. Files go in | 4. Run it in |
| --- | --- | --- | --- | --- |
| Claude | **Projects**, then your project | **Set project instructions**, then **Save instructions** | Project knowledge, **+** | A new chat in the project |
| ChatGPT | Your project in the sidebar | **•••**, then **Project settings** | The project's files | A new chat in the project |
| Copilot | **All agents**, then **...**, then **Edit** | **Configure** tab, **Instructions**. Then **Update** | **Knowledge**, **Upload** (`.txt` only) | The agent chat |
| Gemini | **Customize**, then **Skills**, then your skill | **Instructions**. Then **Save** | **Add**, then files | A new chat. Type **/** and pick the skill |

## 6. Debrief

- Questions: Which problem did your agent rank near the top? What did its evidence profile say? Which check or audit found the error? Which segment would you act on first, and why?
- Error reveal (record ids): I-104 (Marrowby Grocers, Food service, PM-held, 52 minutes) gives 3 word-for-word quotes on P05 Multi-site visibility, including the renewal threat "If I can't compare all nine stores on one page by next spring, I'm not renewing, it's that simple." On brief v1, P05 ranks in the top 3, or first in Food service. Profile: 1 interview, 1 account, 1 segment. P01 and P02: 4 interviews and 4 accounts each, all 3 segments. I-103 and I-105 (Food service) do not raise P05. Batch 2: I-111 says "It would help to see all my sites on one screen, but honestly it's not my top problem."
- Debrief check (instructor only): After the fix, the batch 1 flag report lists P05: all 3 quotes come from 1 interview (I-104). P05 is not ranked near the top on quotes. Its reason states its interview count. It stays in the backlog. The batch 2 flag report lists the P06 disagreement (I-101 and I-106 want their own managers; I-110 and I-112 want a service; I-106 and I-112 are the same account, Pellham Distribution). The agent wrote "pattern" nowhere. Counts after batch 2 (`case/expected-results.md`): 14 interviews, 11 accounts. P01 7 interviews, 6 accounts. P02 6 and 6. P06 4 and 3. P08 3 and 3. P03 3 and 2. P05 2 and 2. P04 1 and 1. P07 1 and 1. P05 ranks below P01, P02, P03, P06 and P08.
- Check sample: each learner runs `m1-check-sample.md` in a new chat on the tuned brief, with the empty backlog (3 minutes). Pass condition on the cards, from `case/expected-results.md`, lab 1 second sample.
- Order by segment: each learner writes the top problem in each segment. Case PM order after batch 2: P01, P02, P08, P03, P06, P05, P04, P07. Top in Distribution: P01 and P02. Food service: P03. Pharmacy and lab: P08. Test: can you predict that the next buyer of this persona will raise it?
- What you do Monday: Run your agent on your last interview batch. Audit 3 problems before you share anything.
- Log save card:

| Platform | 1. Download | 2. Replace in the agent |
| --- | --- | --- |
| Claude | Download the backlog file from your step 6 run | In project knowledge, delete the old `problem-backlog`. Add the new file with **+** |
| ChatGPT | Download the backlog file from your step 6 run | In the project's files, delete the old `problem-backlog`. Add the new file |
| Copilot | Download the backlog file from your step 6 run, in the same session | On **Configure**, choose the **X** next to the old file, then **Remove**. **Upload** the new file. Select **Update** |
| Copilot, no license | Download or copy the backlog from your step 6 run | Keep it on your computer. Paste it in chat at the next run |
| Gemini | Download the backlog file from your step 6 run | In your skill, **More**, then **Replace file**. Select **Save**. If that fails, upload the whole skill again with the new file |

Rename the new file `problem-backlog` before you add it. Use the step 6 run, not the check sample run. If you have no file, use `kit-m2/problem-backlog.md`.

## 7. LD spec

| Field | Value |
| --- | --- |
| Objective | Build the Market Evidence Agent from the template, run 2 interview batches, decide each flag, audit 3 problems, add a flag rule, and decide the order of the top problems by segment (m1-o1 to m1-o4) |
| Timing | Full day: lab 33 minutes, debrief 9 (check sample 3). Half day: lab 38, debrief 10. Lab brief before it: 3 minutes |
| Setup (Zoom) | Breakout rooms by platform (Claude, ChatGPT, Copilot, Gemini), 3 to 5 learners each. Learners keep their own screen. Share only when stuck. Instructor visits rooms in turn, Copilot first |
| Setup (in person) | Tables by platform, 3 to 5 learners. One laptop per learner. Instructor walks the tables, Copilot first |
| Steps per platform | See section 5 (4 cards with the same 6 core steps, fast-start cards, stretch) |
| Materials | `kit/kit-m1-template/` (brief v1, job card, code book, empty backlog, Copilot fallback text, record sheet). Case files `m1-interviews-batch-1.md`, `m1-interviews-batch-2.md`, `m1-check-sample.md`, `m1-stretch-applicants.md` (stretch). `kit/kit-m2/` for catch-up. Instructor only: `case/planted-errors.md`, `case/expected-results.md`, saved demo output |
| Success criteria | Batch 2 run. The backlog updates. Each problem has an evidence profile and any fact labels that apply. The agent proposes a ranking with a reason for each problem. The agent writes "pattern" and "validated" nowhere. Each flag report item has the learner's decision. 3 audit findings recorded and a flag rule added. Check sample passes the 5-item pass condition |
| Debrief questions | Which problem did your agent rank near the top? What did its evidence profile say? Which check or audit found the error? Which segment would you act on first, and why? |
| Fallback path | Cannot use own work: case data. Platform blocked: change platform or pair with a learner on another platform. Copilot with no license: fallback instructions text, run files pasted in chat. No file output: full tables in one message (brief rule 7). Agent does not make the error: debrief uses the saved demo output. Behind at the end: load `kit-m2` before module 2 |
| Learner evidence | Tuned brief (v1 to v2 with the single-source flag rule). Flag report decisions for batch 1. Audit findings for 3 problems. The PM's order of the top problems by segment. All on `lab-1-record-sheet.md` |

## 8. Learner kit

Character counts measured with `wc -m` on 2026-11-26. Copilot course budget (spec `copilot_no_license_fallback`): core brief 3,500 or fewer, job card 1,500 or fewer, knowledge file 2,800 or fewer, total 7,800 or fewer. Vendor limit: Instructions 8,000 characters (mb-01).

| File | Loads into | Characters | `.txt` copy |
| --- | --- | --- | --- |
| `kit-m1-template/brief-v1.md` | Instructions | 2,730 (budget 3,500) | yes |
| `kit-m1-template/job-card-problem-backlog.md` | Knowledge | 1,194 (budget 1,500) | yes |
| `kit-m1-template/code-book.md` (copy of `case/m1-code-book.md`) | Knowledge | 2,791 (budget 2,800) | yes |
| `kit-m1-template/problem-backlog.md` (empty) | Knowledge | 319 | yes |
| `kit-m1-template/copilot-fallback-instructions-m1.txt` | Copilot Instructions, no license | 6,973 (budget 7,800; limit 8,000) | is a `.txt` |
| `kit-m1-template/lab-1-record-sheet.md` | Not loaded. Learner keeps it | not counted | no |
| `kit-m1-template/README.md` (rebuild card) | Not loaded | not counted | no |
| `kit-m2/brief-v2.md` | Instructions | 2,878 (budget 3,500) | yes |
| `kit-m2/job-card-problem-backlog.md` | Knowledge | 1,194 | yes |
| `kit-m2/code-book.md` | Knowledge | 2,791 | yes |
| `kit-m2/problem-backlog.md` (after batch 2, case PM order) | Knowledge | 9,958 (a log, not in the fallback instructions) | yes |
| `kit-m2/lab-1-fix-rules.md` | Not loaded. Handout | 580 | yes |
| `kit-m2/copilot-fallback-instructions-m1-v2.txt` | Copilot Instructions, no license, to rerun job 1 | 7,139 (budget 7,800) | is a `.txt` |
| `kit-m2/README.md` | Not loaded | not counted | no |

Fallback sum check: brief v1 2,730 + job card 1,194 + code book 2,791 = 6,715, plus a 258-character header and separators = 6,973. Module 2 budget left after brief v2 (2,878) and the driver code book (2,284): about 2,600 characters for the win/loss job card and header under 7,800.

Knowledge files in the agent after module 1: 3 (job card, code book, problem backlog). Course budget 13.

## 9. Instructor notes

- Timing flex:
  - Behind before the lab: cut the story slot (1.4) and the half-day question on 1.8. Never cut the lab brief or the data safety note.
  - Behind in the lab: at minute 30, tell learners to skip step 6 and go to the debrief. Run step 6 after class. The debrief still works from the batch 1 run.
  - Behind in the debrief: keep the reveal and the check sample. Cut the order by segment to "write it on your record sheet after class".
  - Ahead: learners do the screening stretch. In the debrief, ask a learner who did it to say which applicants went to the PM.
- Common failures and recovery:

| Failure | Recovery |
| --- | --- |
| Copilot: the agent ignores the knowledge files (no license or billing) | Use the no-license box on the Copilot card: `copilot-fallback-instructions-m1.txt` in Instructions, batches pasted in chat |
| Copilot: upload of a `.md` file fails in chat | Paste the text of the file |
| Claude: no file in the answer | Turn on **Code execution and file creation** (**Create and edit files**). Or accept the full tables in one message (brief rule 7) |
| The answer stops halfway (long output) | Send "Continue". Or send "Give the problem backlog table only, then the flag report" |
| Gemini: skill name rejected | Use lowercase and hyphens: market-evidence-agent |
| ChatGPT Free: upload limit reached | Paste the text. Free has 3 uploads per day (cg-03). The readiness checklist asks for Go or Plus |
| The agent does not make the planted error (P05 not near the top) | Good. Ask the learner why. In the debrief, show the saved demo output |
| After the fix, the agent drops P05 from the backlog | Point to the rule: "Keep single-source problems in the backlog." Rerun |
| The agent writes "food service buyers want one view across stores" | Part of the same error. It breaks the segment rule (brief rule 4): 1 Food service interview on P05 |
| The agent writes "pattern" | Audit finding. Point to brief rule 3. Rerun |
| A learner's own notes have no codes | Use the case code book as a start, or switch to the case data for this lab |
| A learner is far behind | Load `kit-m2` at the start of module 2. About 5 minutes |
| The agent still labels a problem "AI-moderated only" | That comes from the code book column. It is a true fact. Accept it |

- Case notes (OI-19, owner module builder; rechecked 2026-11-26 against the case files):
  1. Check sample: I-201 quote 2 ("Our insurer now asks for every temperature record before they pay a claim.") can also code as P02. Accept it. P07 still shows 1 interview, and the pass condition still holds.
  2. Lab 5 (for the module 5 builder): F-1108 (week 1, A-07 Quarry Lane Pharmacies) and F-1214 (week 2, A-29 Elmstead Pharmacy) support the report pack answer, but they are not lab 5 inputs. Both are still in the case CSVs as described.
  3. I-102 and I-110 are the same account (Teller Creek Foods). I-106 and I-112 are the same account (Pellham Distribution). I-103 and I-111 are the same account (Saltgrass Kitchens). Account counts depend on this. Learners who count interviews as accounts get P01 at 7 accounts after batch 2 instead of 6.
  4. The I-102 note (proof of cold chain for a distributor's own customers) fits no code. The case PM sends it to discovery. It becomes P09 in the module 3 tag list.
  5. Pharmacy and lab has no PM-held interview in batch 1 (I-107, I-108 are AI-moderated). I-113 in batch 2 is PM-held, so that flag clears.
  6. The 71% on slide 1.2 (N5) comes from a survey with 83% European respondents. Say so if asked.
- Kept off the slides on purpose: the therapy preference study (OI-08, no 2026 primary source). The Pew synthetic respondents finding (E16) is not used in module 1. No vendor speed figure (E1, E2).
