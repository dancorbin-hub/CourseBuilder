# Course open: Advanced AI for Product Strategy and Planning

Course: `product-strategy-and-planning`. Stage 3 draft by the module builder, 2026-11-27. Runs before module 1. Same 25 minutes on the full day and at the start of half day 1 (spec `course_open`). Built from `spec.yaml` (Gate 2, approved 2026-11-27), `research/bond-stories.md` (candidate 1), `research/evidence-ledger.yaml` (E3) and `outline/gate-2-decisions.md`.

## 1. Summary

| Item | Value |
| --- | --- |
| Minutes | 25 (full day and half day 1) |
| Instructor-led / hands-on | 15 / 10 (60% / 40%). The module 40/60 rule applies to modules. The spec sets this split for the open |
| Segments | Bond story 5 (instructor-led). Opening build check 10 (hands-on, ends by minute 15). Course frame 10 (instructor-led), of which "know before you design" is 5 (slides O.7 and O.8) |
| Bond story | Trendslop (E3), picked by Dan (Gate 2, 2026-11-26). The finding is told in words only. No figure or number from the HBR article on a slide or in the talk track until a licensed copy is read (OI-10) |
| Build check pass | The agent answers after reopen |
| Evidence | Each learner has a saved agent named "Strategy Evidence Agent" (Gemini: strategy-evidence-agent) that lists the capacity sheet columns after reopen |

### Slide minutes check

| Segment | Slides | Minutes | Mode |
| --- | --- | --- | --- |
| Bond story | O.1 to O.3 | 1 + 3 + 1 = 5 | Instructor-led |
| Opening build check | O.4 | 10 | Hands-on |
| Course frame | O.5 to O.8 | 2 + 3 + 3 + 2 = 10 | Instructor-led |
| Total | 8 slides | 25 | 15 + 10 |

### Questions for Dan

All open questions for the course open and module 1 are in one list: `module.md`, section 1, "Questions for Dan". Question 5 (Trendslop) and question 7 (Gemini labels) touch the open.

### No repeated slide

The Market Research course open (`courses/market-research/modules/m1/course-open.md`) has slides on the agent manager, "Know before you design", data safety and the "Be great at product management" theme. This open covers the same spec items with new slides: a different headline, visual and content on each. The theme line is a footer line on O.5, not a headline slide. "Know before you design" is O.7 ("What may your plan go into?"), built on planning data. O.8 shows the data check card next to the standard text.

## 2. Slides and talk track

### Slide O.1: Advanced AI for Product Strategy and Planning
- Layout: Course Cover
- Minutes: 1
- On-slide text: ADVANCED AI FOR PRODUCT STRATEGY AND PLANNING. "The agent gathers the evidence. You make the call."
- Visual intent: Teal gradient, white leaf mark, course name in caps. Thesis line in white under the title. The course close repeats the same thesis line.
- Sources: none

Notes:
```
POINT: This course teaches you to build and manage one AI agent for product strategy and planning, while you make every strategy call.
Talk Track:
Welcome.
Today you build one AI agent and manage it through five planning jobs.
The quarterly portfolio pack. Requests. The business case. Roadmap changes. Outcomes.
You leave with the agent, saved on your own platform, ready for your own plans.
Here is the line for the day.
[POINT TO THE THESIS LINE]
The agent gathers the evidence. You make the call.
Let me tell you why that line matters more for strategy than for any other part of the job.
TRANSITION: It starts with a study from 2026.
```

### Slide O.2: Ask AI for a strategy. Get everyone's strategy
- Layout: Blank
- Minutes: 3
- On-slide text: Headline: "Ask AI for a strategy. Get everyone's strategy." Line 1: "Researchers asked leading AI models for strategic advice across many scenarios." Line 2: "The models almost always picked the same trendy option, whatever the context." Line 3: "The authors' name for it: trendslop." Source line: Romasanta, Thomas and Levina, Harvard Business Review, March 2026.
- Visual intent: Headline with "everyone's" in orange. Many different scenario cards on the left, each with an arrow into one AI icon, and one identical answer card on the right. No numbers on the slide.
- Sources: E3 (study, partly verified; finding, authors and date verified). Bond story sources S-T1 (HBR, primary, body paywalled), S-T2 (NYU Stern summary), S-T3 (Fortune, independent). Words only (OI-10)

Notes:
```
POINT: A 2026 study found that AI models give strategy advice that sounds tailored but steers every company to the same trendy choices.
Talk Track:
In March 2026, a team of researchers published a finding in Harvard Business Review.
They are strategy researchers at Esade, the University of Sydney and NYU Stern.
They asked leading AI models for strategic advice.
Models from the big vendors, including ChatGPT, Gemini and Claude.
Yes, Claude. One of the platforms some of you use today. That makes the point stronger, not weaker.
They gave the models hard trade-offs. The kind your leadership team argues about.
Long-term growth or short-term results.
Automate a job, or help the people who do it.
They ran this across many scenarios.
[PAUSE]
The models almost always picked the same option. The trendy one. Whatever the context.
The researchers warn that an answer can sound tailored to your situation and still not fit it.
The authors gave it a name: trendslop.
Their advice to leaders: use AI to widen your options. Do not let it make the choice.
[DO NOT QUOTE PERCENTAGES OR RUN COUNTS FROM THE ARTICLE. IF ASKED FOR NUMBERS:] The full article has the detail. We use the finding, not the figures, until we have read the licensed copy.
TRANSITION: So here is the question for your company.
```

### Slide O.3: Whose strategy is it?
- Layout: Blank
- Minutes: 1
- On-slide text: "If every competitor asks the same model, whose strategy is it?"
- Visual intent: One line, large type, centered. "whose" in orange.
- Sources: none (hook line from `research/bond-stories.md`, candidate 1)

Notes:
```
POINT: Strategy is a forced choice that stays with the PM, so today's agent never proposes strategy and only checks the plan against the strategy you give it.
Talk Track:
If every competitor asks the same model, whose strategy is it?
Not yours.
So today the agent never writes your strategy. It never proposes one. It never ranks your programs.
You give it your strategy. Your objectives. Your rules.
It checks your plans, requests and business cases against them, and shows you the evidence.
You make the forced choice. That is the job no model can do for you.
TRANSITION: Before we talk more, let's make sure your platform works. You build right now.
```

### Slide O.4: Build, save, reopen
- Layout: Activity
- Minutes: 10
- On-slide text: ACTIVITY. 10 MIN. 1. Create a Project (Claude, ChatGPT), an agent (Copilot) or a skill (Gemini) named "Strategy Evidence Agent". 2. Paste the 3-line starter instruction. 3. Upload `capacity-sheet.xlsx` from kit-m1-template. 4. Ask: "List the columns in the capacity sheet." 5. Save, close and reopen. Ask again. Pass: it answers after reopen. Blocked? Change platform or pair with someone.
- Visual intent: Orange band. 5 steps, large. Pass line in a teal box. Four platform tiles.
- Sources: cl-pj-01, cl-up-10, cg-01, cg-14, mb-01, mb-02, mb-14, gm-01 (platform matrix). Screen names and check dates are on the build check cards in section 3

Notes:
```
POINT: Every learner creates, saves and reopens a minimal agent with one spreadsheet in the first 15 minutes, so platform problems surface now and not in the lab.
Talk Track:
The goal of this activity is to prove that your platform can build, save and reopen an agent with a spreadsheet in it, before we need it.
Open the build check card for your platform in your workbook.
The starter instruction is on the card. Three lines.
The file is the capacity sheet from your kit. It is a spreadsheet with formulas. You use it in lab 1.
Ask the agent to list its columns.
Then save, close it and open it again. Ask again.
If it answers after you reopen it, you pass.
[START A 10-MINUTE TIMER. WALK THE ROOM OR VISIT THE BREAKOUT ROOMS. COPILOT FIRST]
[AT MINUTE 5, ASK: "Hands up if you are blocked." FOR EACH BLOCKED LEARNER: change platform, or pair with a learner on another platform for today]
[CLAUDE LEARNER WHOSE .XLSX UPLOAD FAILS: "Turn on Code execution and file creation in Settings, then Capabilities. Or upload the CSV copy."]
[CHATGPT LEARNER: "Did you pick Default memory? You need it for file output later. A memory change can take a few hours, so fix it now, not in the lab."]
[COPILOT LEARNER WHOSE AGENT CANNOT SEE THE FILE: "You may have no Copilot license or billing. Your lab card has a no-license path. You use it in lab 1."]
[GEMINI LEARNER WHOSE NAME IS REJECTED: "Skill names use lowercase and hyphens: strategy-evidence-agent."]
[LOG EVERY BLOCKED BUILD: platform, plan, what failed. It goes to the monthly refresh]
TRANSITION: [AT MINUTE 10] Keep that agent open. It is the one you build on all day.
```

### Slide O.5: Strategy is where your judgment counts
- Layout: Blank
- Minutes: 2
- On-slide text: Headline: "Strategy is where your judgment counts." Left, "The agent": Gathers. Totals. Traces. Flags. Right, "You": Write the brief. Set checks and hand-off rules. Decide each flag. Audit a sample. Make the call and record why. Bottom line: "The agent never sets, proposes, ranks or rewrites strategy. It never recommends funding." Footer line: "Be great at product management before you are great at AI."
- Visual intent: Two columns of very different weight: four short verbs on the left in gray, five actions on the right in teal. Bottom line in orange. Footer line small, in navy.
- Sources: none (spec `course.themes`, `course_agent.core_rule`)

Notes:
```
POINT: The agent does the evidence work and the PM, as agent manager, makes every strategy, priority and funding call.
Talk Track:
Strategy is where product judgment matters most.
So here is the split for the day.
The agent gathers, totals, traces and flags.
You are the agent manager. You write its brief. That is its instructions.
You set its quality checks. Those are tests it runs on its own work before it reports.
You set its hand-off rules. Those say when it stops and hands an item to you.
Those items come to you in a flag report: a short list of what you must decide.
You audit a sample of its work. And you make the call, with a reason you write down.
[POINT TO THE BOTTOM LINE]
The agent never sets, proposes, ranks or rewrites strategy. It never recommends funding.
The AI gathers evidence and filters first. You decide. Many factors matter that are not in any file.
[POINT TO THE FOOTER]
One more idea for the day. Be great at product management before you are great at AI.
The agent makes a good PM faster. It does not make the calls a good PM makes.
TRANSITION: So what will the agent do for you today?
```

### Slide O.6: Five jobs across your planning year
- Layout: Blank
- Minutes: 3
- On-slide text: Headline: "Five jobs across your planning year." A year timeline with five job markers: Module 1, quarterly portfolio pack (each quarter). Module 2, request decisions (each request batch). Module 3, the living business case (before an investment commit). Module 4, roadmap refresh and change (at your cadence, often each quarter). Module 5, outcome check (each month). Line under it: "One agent: the Strategy Evidence Agent. Planning here means annual and quarterly product planning."
- Visual intent: A 12-month timeline strip. Quarterly diamonds for modules 1 and 4, small dots through the year for module 2, one flag for module 3, monthly ticks for module 5. A small 5-step ladder icon in the corner.
- Sources: none (spec `course_agent.growth`, `autonomy_ladder`, `course.title_note`)

Notes:
```
POINT: The course builds one agent that grows by one planning job per module, each at its own place in the planning year.
Talk Track:
One agent all day. Its name is the Strategy Evidence Agent.
When we say planning in this course, we mean annual and quarterly product planning. The roadmap, the portfolio, the investment calls.
[POINT TO EACH MARKER IN TURN]
Module 1. Each quarter, someone builds the portfolio pack for the review. Your agent builds it and checks it against the strategy.
Module 2. Requests arrive all the time. Your agent builds a decision card for each one. You make the call.
Module 3. Before a big investment commit, the business case. Your agent keeps its assumptions current and shows what changed.
Module 4. The roadmap. Your agent traces every item to evidence and checks what a change would move. At your cadence, often each quarter.
Module 5. Each month, are the outcomes the business case promised really happening?
You set how often each job runs. Review too often and your team gets whiplash.
[POINT TO THE LADDER]
Each module also gives the agent a little more room. First you run it by hand on one batch. By the end, it runs each month across jobs. You read the flags and audit a sample.
Fall behind? Each module has a catch-up kit. You rebuild in about 5 minutes.
TRANSITION: Before you put a real plan into this agent, know your company's limits.
```

### Slide O.7: What may your plan go into?
- Layout: Blank
- Minutes: 3
- On-slide text: Headline: "What may your plan go into?" Left, "Your planning data": spend and headcount, unreleased roadmap and release dates, forecasts, pricing, supplier terms. Right, "Your tool": Approved for this data? Code execution and file creation on? Agent or skill creation allowed? Copilot knowledge files: license or billing? Sharing allowed? Connectors: none needed today. Bottom line: "No answer? Use the Larkspan case today. Ask on Monday."
- Visual intent: Left column as a stack of document icons, each labeled. Right column as five check boxes. Bottom line in teal.
- Sources: cl-fo-06, mb-03, cg-09 (platform matrix). Spec `data_access_limits`, `learner_profile.readiness_checklist`

Notes:
```
POINT: Planning data is some of the most sensitive data a PM holds, so check the company limits on your tool before you design the agent.
Talk Track:
This check was in your pre-class email. Few people get to it, so we do it now. Three minutes.
[POINT TO THE LEFT COLUMN]
Look at what a quarterly plan holds.
Spend and headcount. Release dates that are not public. Forecasts. Pricing. Supplier terms.
That is more sensitive than most of what a PM handles.
[POINT TO THE RIGHT COLUMN]
Now your tool. Answer each one for yourself.
Is this tool approved by your company for this data?
Is code execution and file creation on? Your agent needs it to total a sheet. Some admins turn it off.
Can you create an agent or a skill? On Copilot, the agent reads knowledge files only with a Microsoft 365 Copilot license or pay-as-you-go billing. Your card has a path if you have neither.
Can you share an agent with your team? Some companies turn this off.
Connectors: today's labs need none. You upload files.
If you do not know an answer, use the Larkspan case today. It is fictional. Ask your IT or security team on Monday.
[HALF A MINUTE OF SILENCE. "Write your answers on the readiness checklist from the email, or on paper."]
TRANSITION: And one rule for every lab today.
```

### Slide O.8: Three questions before every upload
- Layout: Blank
- Minutes: 2
- On-slide text: Standard data safety box: "Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Do not put unreleased roadmaps or release dates, forecasts, pricing, supplier terms or other non-public financial data into a tool your company has not approved. Do not put confidential names in web search queries." Next to it, "Data check card": 1. Is this tool approved by my company for this data? 2. Does my file hold client data, health data, personal data, unreleased roadmap or release dates, forecasts, pricing, supplier terms or non-public financials? 3. If 2 is yes and 1 is no, use the Larkspan case or remove names and numbers first.
- Visual intent: The standard data safety box on the left, the same box that sits on every step card. The data check card on the right as a small card with 3 numbered questions.
- Sources: none (spec `data_safety_note.standard_text`, `data_check_card`)

Notes:
```
POINT: Every lab follows one data safety rule, and every step card starts with a three-question data check.
Talk Track:
This box is on every step card today.
[READ THE BOX ALOUD]
And this card sits above step 1 of every card. Three questions.
Is this tool approved for this data?
Does my file hold anything on that list?
If yes, and the tool is not approved, use the Larkspan case, or remove names and numbers first.
It takes two minutes in lab 1 and one minute after that.
One more thing. An agent keeps files in its knowledge and uses them on every run. This agent keeps a pack, logs and sheets.
So at the end of each lab you decide what it may keep. We do that together.
TRANSITION: Let's build the first job. Module 1.
```

## 3. Build check cards

Each card starts: "Build and save your own agent. Share your screen only when someone is stuck."

Vendor docs and check dates are the same as the module 1 step cards (`module.md`, section 5). Screen names come from dated vendor docs recorded in `courses/market-research/research/platform-matrix.yaml` (rows cl-ui-09, cl-ui-10, cg-ui-09, mb-ui-12, mb-ui-13, gm-ui-10, checked 2026-11-26) and this course's matrix (cg-14, mb-04). Labels not in a vendor doc are written in plain words. The verifier list is in `module.md`, section 1.

Starter instruction (paste all 3 lines):

```
You are the Strategy Evidence Agent. You help a product manager.
Use only the files I give you. Do not guess.
When I ask, list the columns in each sheet I gave you.
```

Question: "List the columns in the capacity sheet." Expected answer: Quarter, Team, Team_FTE, Program, Alloc_pct, Team_capacity_pct, Alloc_FTE, Per_program_check. The agent may also mention the notice line in cell A1 ("Fictional data for training"). That is fine.

Data safety (all cards): Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Do not put unreleased roadmaps or release dates, forecasts, pricing, supplier terms or other non-public financial data into a tool your company has not approved. Do not put confidential names in web search queries.

### Claude
Saves: **Save instructions** saves the instructions. Files save when you add them.

| Step | Do this |
| --- | --- |
| 1 | In **Projects**, select **+ New Project**. Name it "Strategy Evidence Agent". |
| 2 | Paste the starter instruction into **Set project instructions**. Select **Save instructions**. |
| 3 | Add `capacity-sheet.xlsx` to project knowledge with **+**. |
| 4 | In a new chat in the project, ask the question. |
| 5 | Close the browser tab. |
| 6 | Open the project again from **Projects**. Ask the question in a new chat. |

Pass: it answers after you reopen it. Upload fails? Turn on **Code execution and file creation** in **Settings**, then **Capabilities**. Or add `capacity-sheet.csv` instead.

### ChatGPT
Saves: as you go. Plan: ChatGPT Plus or higher.

| Step | Do this |
| --- | --- |
| 1 | Select **New project** in the sidebar. Name it "Strategy Evidence Agent". Pick **Default memory**, not **Project-only memory**. |
| 2 | Paste the starter instruction in **•••**, then **Project settings**. |
| 3 | Add `capacity-sheet.xlsx` to the project's files. |
| 4 | In a new chat in the project, ask the question. |
| 5 | Close the browser tab. |
| 6 | Open the project again from the sidebar. Ask the question in a new chat. |

Pass: it answers after you reopen it. Why **Default memory**: ChatGPT Work, which makes spreadsheet files, does not run in a project with project-only memory (cg-14).

### Copilot agent builder
Saves: **Create** the first time. **Update** after each change.

| Step | Do this |
| --- | --- |
| 1 | Select **New agent**, then **Skip to configure**. In **Name**, type "Strategy Evidence Agent". |
| 2 | Paste the starter instruction into **Instructions**. |
| 3 | In **Knowledge**, add `capacity-sheet.xlsx` with **Upload**. Select **Create**. |
| 4 | In the agent chat, ask the question. |
| 5 | Close the browser tab. |
| 6 | Open the agent again from **All agents**. Ask the question. |

Pass: it answers after you reopen it. If it answers but cannot see the file, you may have no Copilot license or billing. Use the no-license path on your lab 1 card. Use the `.xlsx` file. Copilot does not take CSV as knowledge.

### Gemini
Saves: **Create** the first time. **Save** after each change.

| Step | Do this |
| --- | --- |
| 1 | Select **Customize**, then **Skills**, then **Create**, then **Create manually**. Name it "strategy-evidence-agent". |
| 2 | Paste the starter instruction into the skill instructions. |
| 3 | Add `capacity-sheet.xlsx` with **Add**, then **images or files**, then **Upload**. Select **Create**. |
| 4 | In a new chat, type **/**, pick your skill and ask the question. |
| 5 | Close the browser tab. |
| 6 | Open Gemini again. Ask the question with your skill in a new chat. |

Pass: it answers after you reopen it. Skill names use lowercase and hyphens. Gems are now skills. No **Customize**? Select **More** first.

Blocked on any platform: change platform, or pair with a learner on another platform for the day. Tell the instructor what failed.

## 4. LD spec: opening build check

| Field | Value |
| --- | --- |
| Objective | Each learner creates, saves, reopens and runs a minimal agent with one spreadsheet on their platform, so platform problems surface before lab 1 |
| Timing | 10 minutes, ends by minute 15 of the course |
| Setup (Zoom) | Main room. The instructor opens breakout rooms by platform only for blocked learners. Learners share a screen only when stuck |
| Setup (in person) | Learners at tables by platform. Instructor walks the room, Copilot first |
| Steps per platform | Section 3 build check cards |
| Materials | Starter instruction (3 lines, on the card). `kit-m1-template/capacity-sheet.xlsx` (Claude fallback: `capacity-sheet.csv`). Platform readiness checklist, sent before class (decision 44), with the "know before you design" questions |
| Success criteria | The agent lists the capacity sheet columns after the learner closes and reopens it |
| Debrief questions | None. One question at minute 5: "Hands up if you are blocked." |
| Fallback path | Change platform, or pair with a learner on another platform. Claude upload fails: turn on code execution and file creation, or use the CSV copy. Copilot with no license or billing: the agent cannot use knowledge files; the learner uses the no-license path in lab 1. The instructor logs each blocked build for the monthly refresh |
| Learner evidence | A saved agent named "Strategy Evidence Agent" (Gemini: strategy-evidence-agent) that answers after reopen |
