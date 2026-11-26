# Advanced AI for Market Research

Syllabus and course outline. Draft for Pragmatic review, 2026-11-22.

## Course promise

After this course, you can build and manage one AI agent that turns your interviews, win/loss deals, weekly feedback and past research into a checked problem backlog. You decide what the evidence means and which problems come first.

## At a glance

| Item | Detail |
| --- | --- |
| Length | One day, 7.5 hours with lunch and breaks. Also runs as two half days of 3.5 hours each |
| Delivery | Live on Zoom or in person. Labs run in breakout rooms or at tables, grouped by platform |
| Format | 5 modules. Each module is 40% instructor-led and 60% hands-on |
| Offering intent | Develop and Apply |
| Pragmatic Framework 2027 | Category: Market. Focus areas: Market Problems, Win/Loss Analysis, Competitive Landscape |
| Capability Standards (proposed) | Capability 1 Market Intelligence. Skills 1.1 Market Problem Identification, 1.2 Market Segmentation and 1.3 Market Discovery. Supporting skills 8.1 Market Data Context and Pattern Recognition and 8.4 Data Narrative and Stakeholder Communication |
| Platforms | Claude, ChatGPT, Microsoft Copilot agent builder and Gemini. Every lab has a step card for each, with the same core steps |

## Who this course is for

- Experienced product managers who run or use market research.
- Product marketers and product leaders who act on buyer, deal and feedback evidence.
- PMs in software, hardware, services and internal platform teams.

This course is not an introduction to AI prompts. It does not teach persona creation, market definition or market sizing.

## What you learn to do

You become the **agent manager**. The agent does the routine research work. You do the work that needs product judgment:

1. Write the agent's brief: its job, inputs, code book and output.
2. Set quality checks that the agent runs on its own output.
3. Set hand-off rules: when the agent stops and gives an item to you.
4. Read the flag report and decide each item.
5. Audit a sample of the agent's output against the sources.
6. Read the agent's proposed ranking and decide the order of problems yourself.
7. Tune the brief for what the audit found, and run again.

**The big idea.** AI can gather far more market signal than you can read: online sources, customer feedback, deals and any data you give it. All of it is noise until you put it in context: what matters to your customers and what your business is trying to do. The agent gathers and organizes. You bring the context and make the call.

**Ideas that run through the day:**

- **There is no magic number.** The agent reports the evidence and proposes a ranking. You decide the order.
- **Be great at product management before you are great at AI.**
- **Win/loss is the data most teams do not get.** Module 2 shows what it reveals.

## Course objectives

By the end of the course, you can:

1. Build a market evidence agent from a template on your platform and run it on your own research inputs.
2. Write and tune the agent brief (job, inputs, code book, quality checks, hand-off rules, output) after each audit.
3. Decide each flag report item and audit a sample of agent output against its sources.
4. Connect agent jobs so that one job's output feeds the next, with hand-off rules that control what passes and what stops.
5. Rank market problems against each other from their evidence profiles, by segment, and defend each priority decision with sourced evidence, not a count alone.

## How the course works

**One agent, five jobs.** You build the Market Evidence Agent in module 1 from a template. Each later module adds one job. You leave with one agent that does five jobs.

**A problem backlog, not a fixed bar.** The agent keeps a backlog of market problems. Each problem has an evidence profile:

| Part of the profile | What it shows |
| --- | --- |
| Interviews | How many interviews (not quotes), accounts, segments and personas |
| Source type | PM-held interview, win/loss, feedback item or past report. Also AI-moderated interview, where a team uses them |
| Urgency | How pressing the problem is, with one buyer quote |
| Pervasiveness | How many accounts and segments have the problem |
| Willingness to pay clues | Signs that buyers spend money or effort on the problem |
| Source dates | When each piece of evidence was collected |

You know urgency, pervasiveness and willingness to pay from Pragmatic Foundations and Product Discovery with AI. In this course the agent reports them, and you check its report.

The agent also states facts such as "single source" (one interview, however many quotes) and "one segment only". These are facts, not verdicts. The problem stays in the backlog, so you can track it over time. The agent proposes a ranking with a reason for each problem. You decide the order, what is a pattern and what goes to validation. Priority is relative: you judge each problem against the others.

**The agent climbs a ladder.** Each module gives the agent more room, and you check it in a different way.

| Step | What the agent does | What you check | Modules |
| --- | --- | --- | --- |
| 1. Hand-run batch | Runs on a batch you give it | Every flag and a sample | 1, 2 |
| 2. Recurring run | Runs on each new week of input | Only the flag report and a sample | 3 |
| 3. Hand-off between jobs | One job's output feeds the next job | The hand-off rule and traced entries | 4, 5 |
| 3 plus. Faces other people | Answers stakeholder questions | Each answer before it goes out | 5 |

**Each lab has a planted AI error.** In module 1 we tell you that it is there. In modules 2 to 4 you get a hint. In module 5 you get no hint. The debrief shows where it was and which check or audit found it.

**Each lab has a check sample.** After you fix the brief, you run the agent on a second sample and compare the result with a pass condition. In modules 1, 2 and 5 you run it in the debrief. In modules 3 and 4 the instructor shows the result, and you run it after class in about 5 minutes.

**Your own work first.** Use your own interviews, deals, feedback and reports when your company allows it. If you cannot, use the case company: Larkspan Systems, a fictional maker of wireless temperature sensors and the cloud software that watches them. It has product teams for external customers and an internal platform team. One case serves the whole course.

**You do not fall behind.** Each module has a catch-up kit. You can rebuild the agent at the start of any module in about 5 minutes.

## Modules

Minutes show the one-day format first, then the two-half-day format where it differs.

### Module 1. Run your first batch and manage it by flags (70 minutes; 80 in half days)

**Promise:** Hand interview synthesis to an agent that keeps a problem backlog, and manage it by its checks and flags.

- **Workflow:** Turn each new batch of buyer interviews into an updated, checked problem backlog.
- **Bottleneck it removes:** Synthesis takes days per study, so insight reaches the roadmap late.
- **Objectives:**
  1. Build the Market Evidence Agent from the template, with a brief, a code book, an evidence profile and an output format.
  2. Decide each item in the flag report (keep, fix or send to discovery).
  3. Audit 3 random problems in the backlog against the source interviews and record what you find.
  4. Add a flag rule to the brief for what the audit found, rerun, and decide the order of your top problems by segment.
- **Lab:** Build the agent. Run two batches of interviews. Read the evidence profiles and the proposed ranking. Audit, tune and rerun. A fast-start card per platform helps learners who are new to the builders.
- **Your input:** 5 to 15 of your own interview notes or transcripts, or the case interviews.
- **Learner evidence:** Your tuned brief (with one new flag rule), your flag report decisions, your audit findings for 3 problems and your order of the top problems by segment.
- **Stretch:** Screen the next round of study applicants and hand only edge cases to the PM. Turn the job into a custom skill.

### Module 2. Win/loss and the match rate (70 minutes; 75 in half days)

**Promise:** Find out how often your sales loss reasons match what buyers say.

- **Workflow:** Run a win/loss program that turns each decided deal into an updated, checked decision-driver report.
- **Bottleneck it removes:** Manual win/loss is slow and does not scale. Sales-entered loss reasons often differ from buyer reasons. Many teams do not run win/loss at all.
- **Objectives:**
  1. Extend the agent with a win/loss job that labels each deal "interview" or "CRM only".
  2. Compare CRM loss reasons with buyer reasons in a match rate table.
  3. Audit the deal source labels on 2 random deals and correct the brief.
  4. Decide which findings go to sales, marketing or leadership, and frame them so that sales does not read them as blame.
- **Lab:** Add the win/loss job. Join a CRM export and win/loss interview notes. Read the match rate table and the deal counts for each driver. Audit and tune.
- **Your input:** An export of recent decided deals and any win/loss notes, or the case deals.
- **Learner evidence:** The match rate table with your one-sentence read of it, your flag report decisions, your audit findings for 2 deals and your brief change.

### Module 3. The weekly run: read flags, not every item (60 minutes)

**Promise:** Let the agent read every piece of feedback, so you read only what changed.

- **Workflow:** Route each week's inbound customer feedback into the problem backlog.
- **Bottleneck it removes:** Feedback is spread across many tools. Tagging by hand is slow and subjective, and tags drift.
- **Objectives:**
  1. Extend the agent to tag a week of feedback against the problem backlog, counted by unique account.
  2. Write a "no fit" rule that makes the agent say "no fit" instead of guessing.
  3. Audit a sample of 10 tagged items and the whole "no fit" group, and decide which changes need discovery.
- **Lab:** Add the weekly feedback job. Run week 1, then week 2. Read only the flag report and a sample. Decide which problems move up or down the backlog.
- **Your input:** One or two weeks of feedback items with personal data removed, or the case feedback exports.
- **Learner evidence:** Your flag report decisions for week 2, your audit findings and the "no fit" rule in your brief.
- **Stretch:** Add a survey wave as a source for the evidence profile. Set a schedule or a file trigger, on the platforms whose step card includes this step.

### Module 4. First hand-off: the alternatives map from your own deals (55 minutes)

**Promise:** Map what buyers chose instead of you, from your own deals, not from competitor news.

- **Workflow:** Keep the alternatives map current from the team's own evaluator and deal evidence.
- **Bottleneck it removes:** Keeping the competitive landscape current is recurring work that no one has time for. Hand-built documents age quickly.
- **Objectives:**
  1. Connect the win/loss job to a new alternatives map job, so that the driver log feeds the map.
  2. Write a hand-off rule that says which evidence passes to the map and which goes to the flag report.
  3. Trace 3 map entries back to their interviews and deal records.
  4. Choose the alternative your team must beat in one segment, and state the evidence for it.
- **Lab:** Add the map job. Write the hand-off rule from the win/loss job. Run, audit and fix the rule.
- **Your input:** Your module 2 driver log or a deal export with a competitor field, or the case evidence pack.
- **Learner evidence:** Your hand-off rule as written and as fixed, your audit findings for 3 traced entries, and the alternative to beat in one segment with its evidence.
- **Stretch:** Build the map job as a second agent that reads the first agent's output, on the platforms whose step card includes this step.

### Module 5. The agent answers stakeholders, and you stay accountable (65 minutes; 60 in half days)

**Promise:** Answer "what do we know about X?" in minutes, with sources, dates and limits.

- **Workflow:** Answer stakeholder questions from past research and the problem backlog with sourced, dated answers.
- **Bottleneck it removes:** People cannot find past insights. Teams commission new studies on questions they already answered.
- **Objectives:**
  1. Extend the agent to answer stakeholder questions with a citation, date and segment for each claim, and a "what we do not know" line.
  2. Write hand-off rules that limit what the agent may tell stakeholders.
  3. Decide to send, change or hold each answer after you open each citation.
  4. Judge the agent's ranking and validation proposals by segment, and decide the order and what goes to validation.
- **Lab:** Add the answer job. Set an age limit and hand-off rules. Ask it three stakeholder questions, including one from an internal platform team. Open the citations before anything goes out. In the debrief, fix the brief and ask one more question to check it.
- **Your input:** Your logs from this course plus one or two past study reports, or the case reports.
- **Learner evidence:** Your send, change or hold decisions, your audit findings for one cited answer, your hand-off rules, and your order and validation decisions by segment.

## Agendas

### Full day

| Time | Minutes | Item |
| --- | --- | --- |
| 09:00 | 25 | Course open: opening story, build check (create, save and reopen a starter agent), course frame |
| 09:25 | 70 | Module 1. Run your first batch and manage it by flags |
| 10:35 | 15 | Break |
| 10:50 | 70 | Module 2. Win/loss and the match rate |
| 12:00 | 60 | Lunch |
| 13:00 | 60 | Module 3. The weekly run: read flags, not every item |
| 14:00 | 55 | Module 4. First hand-off: the alternatives map from your own deals |
| 14:55 | 15 | Break |
| 15:10 | 65 | Module 5. The agent answers stakeholders, and you stay accountable |
| 16:15 | 15 | Course close: your Monday plan |
| 16:30 | | End |

Teaching time is 360 minutes.

### Two half days

Each half day is 3.5 hours with one 15-minute break. The split falls after module 2. Day 1 builds the agent and runs it by hand. Day 2 gives it more room. Teaching time is 195 minutes per day.

**Day 1**

| Time | Minutes | Item |
| --- | --- | --- |
| 09:00 | 25 | Course open: opening story, build check, course frame |
| 09:25 | 80 | Module 1. Run your first batch and manage it by flags |
| 10:45 | 15 | Break |
| 11:00 | 75 | Module 2. Win/loss and the match rate |
| 12:15 | 15 | Day 1 close: recap, save your agent, download the module 3 catch-up kit, note one audit finding |
| 12:30 | | End |

**Day 2**

| Time | Minutes | Item |
| --- | --- | --- |
| 09:00 | 10 | Day 2 open: recap, reopen check (rebuild from the catch-up kit if needed) |
| 09:10 | 60 | Module 3. The weekly run: read flags, not every item |
| 10:10 | 55 | Module 4. First hand-off: the alternatives map from your own deals |
| 11:05 | 15 | Break |
| 11:20 | 60 | Module 5. The agent answers stakeholders, and you stay accountable |
| 12:20 | 10 | Course close: your Monday plan |
| 12:30 | | End |

## What you need before class

You get a platform readiness checklist before class. Run it. It takes a few minutes and finds access problems before the class starts.

| Platform | What you build | What you need |
| --- | --- | --- |
| Claude | A Project with instructions and knowledge files | Any plan. Code execution and file creation must be on. Your org owner can turn them off |
| ChatGPT | A Project with instructions and files | Go or Plus, or a business plan |
| Microsoft Copilot | An agent in Copilot agent builder | Permission to create agents in agent builder. A Microsoft 365 Copilot license or pay-as-you-go billing for knowledge files. Not GCC. Learners with Copilot Chat only use a reduced path that runs one job at a time |
| Gemini | A Gemini skill with instructions and files | The Gemini app on a personal or Workspace account |

The core lab steps are the same on all four platforms. Some stretch steps (a scheduled run, a second agent) are only on the step cards of platforms that support them. Copilot Studio, Power Automate and Google Antigravity are not used in this course.

Also bring:

1. Your company's rules on approved AI tools, connectors and sharing. The course open has a "know before you design" check.
2. Your own inputs if your company allows it: interview notes, a deal export, a week of feedback and one or two past study reports. If you cannot use them, the case data is ready for you.

No connectors are needed. You upload or paste files.

## Data safety

Every lab has this note:

> Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

An agent that keeps a backlog keeps sensitive data longer than a one-off prompt. In each lab you decide what the backlog and logs may keep, and for how long.

## What you take home

1. **The Market Evidence Agent with five jobs**, saved on your platform: problem backlog, win/loss, weekly feedback, alternatives map and stakeholder answers.
2. **Jobs already run on your own work**, where you used your own inputs in class.
3. **The final catch-up kit**: the complete brief and knowledge files, to rebuild the agent on any of the four platforms.
4. **Templates**: the brief template, the five job cards, the evidence profile format and the audit checklist.
5. **A Monday plan**: the first job you run on your own work, and the date of your first audit.
