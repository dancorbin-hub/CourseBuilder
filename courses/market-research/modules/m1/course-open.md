# Course open: Advanced AI for Market Research

Course: `market-research`. Stage 3 draft by the module builder, 2026-11-26. Runs before module 1. Same 25 minutes on the full day and at the start of half day 1 (spec `course_open`).

## 1. Summary

| Item | Value |
| --- | --- |
| Minutes | 25 (full day and half day 1) |
| Instructor-led / hands-on | 15 / 10 (60% / 40%). The module 40/60 rule applies to modules. The spec sets this split for the open |
| Segments | Bond story 5 (instructor-led). Opening build check 10 (hands-on, ends by minute 15). Course frame 10 (instructor-led) |
| Bond story | Decision 5 (OI-01): candidate 1, the JAMIA 2026 study of AI quotes in heart failure interviews. Source S-B1 (`research/bond-stories.md`) |
| Build check pass | The agent answers after reopen |
| Evidence | Each learner has a saved agent named "Market Evidence Agent" (Gemini: market-evidence-agent) that answers after reopen |

### Slide minutes check

| Segment | Slides | Minutes | Mode |
| --- | --- | --- | --- |
| Bond story | O.1 to O.3 | 1 + 3 + 1 = 5 | Instructor-led |
| Opening build check | O.4 | 10 | Hands-on |
| Course frame | O.5 to O.9 | 2 + 3 + 2 + 1 + 2 = 10 | Instructor-led |
| Total | 9 slides | 25 | 15 + 10 |

### Questions for Dan

1. The open is 15 instructor-led and 10 hands-on, as in the spec. Slide O.1 is the Course Cover with welcome lines. There is no separate opening poll or platform login slide (PRD "patterns to keep" 5). The build check does the platform login job. Add a poll?
2. The bond story uses only the figures in `research/bond-stories.md`: 122 transcripts; 68%, 20%, 3%, 9%. The hook line "almost 1 in 3 quotes" is also from that file (20 + 3 + 9 = 32%). OK to say it aloud? It is not on the slide.
3. The build check uploads `code-book` from kit-m1-template as its sample file, so the lab starts with it in place (module.md, decision B3). OK?

## 2. Slides and talk track

### Slide O.1: Advanced AI for Market Research
- Layout: Course Cover
- Minutes: 1
- On-slide text: ADVANCED AI FOR MARKET RESEARCH. "Build one agent. Manage it by its evidence."
- Visual intent: Teal gradient, white leaf mark, course name in caps.
- Sources: none

Notes:
```
POINT: This course teaches you to build and manage one AI agent for market research.
Talk Track:
Welcome.
Today you build one AI agent and manage it through five market research jobs.
Interviews, win/loss deals, weekly feedback, the alternatives map and stakeholder questions.
You leave with the agent, on your own platform, ready for your own work.
Let me start with a study from this year.
TRANSITION: It is about quotes. The thing every PM puts in a deck.
```

### Slide O.2: The themes were good. The quotes were not
- Layout: Blank
- Minutes: 3
- On-slide text: Headline: "The themes were good. The quotes were not." 122 interview and consultation transcripts. AI quotes checked against the source: 68% word for word. 20% paraphrased. 3% cut short. 9% partly or fully made up. Source line: Bang et al., JAMIA, 2026.
- Visual intent: One horizontal bar split into 4 parts: 68 (teal), 20, 3 and 9 (orange shades). Large type. Source line under it.
- Sources: S-B1 (primary study, JAMIA 33(11), published 2026-08-06)

Notes:
```
POINT: A 2026 study found that AI found good themes in interviews, but about a third of its quotes were not what the person said.
Talk Track:
In 2026, a research team published a study in JAMIA, a peer-reviewed medical informatics journal.
They gave 122 interview and consultation transcripts to an AI-assisted workflow.
The interviews were with heart failure patients.
The AI found valid themes. They matched the human team well.
Then the team checked every quote the AI gave back against the transcript.
[POINT TO THE BAR]
68% were word for word.
20% were paraphrased.
3% were cut short.
And 9% were partly or fully made up.
[PAUSE]
The authors said that human checks of each quote stayed essential.
They called AI "analytic partners rather than autonomous coders".
One more detail. The team worked in a setup approved for health data protected by HIPAA.
They did not paste patient interviews into any tool they liked. Remember that. We come back to it.
[IF A LEARNER SAYS "MY INTERVIEWS ARE NOT CLINICAL"] The errors come from the model, not the topic.
TRANSITION: So ask yourself one question.
```

### Slide O.3: Would your stakeholders know?
- Layout: Blank
- Minutes: 1
- On-slide text: "Would your stakeholders know?"
- Visual intent: One line, large type, centered. Key word "know" in orange.
- Sources: none

Notes:
```
POINT: A reworded quote that sounds right is the AI error nobody sees, and today you learn to manage an agent so that you see it.
Talk Track:
Almost 1 in 3 quotes was not what the person said.
Would your stakeholders know? Would you?
A quote check finds most of these. Many of you already run one.
Today goes further.
You will meet errors that pass the quote check. Every word is right, and the conclusion is still wrong.
That is the agent manager's job: set the checks, then find what the checks miss.
TRANSITION: First, make sure your platform works. You build right now.
```

### Slide O.4: Opening build check
- Layout: Activity
- Minutes: 10
- On-slide text: ACTIVITY. 10 MIN. 1. Create a Project (Claude, ChatGPT), an agent (Copilot) or a skill (Gemini). Name it "Market Evidence Agent". 2. Paste the 3-line starter instruction. 3. Upload `code-book` from kit-m1-template. 4. Ask: "List the file you have and its first heading." 5. Save, close and reopen it. Ask again. Pass: it answers after reopen. Blocked? Change platform or pair with someone.
- Visual intent: Orange band. 5 steps, large. Pass line in a teal box. Four platform tiles.
- Sources: cl-pj-01, cg-01, mb-01, mb-02, gm-01 (platform matrix). Vendor docs and dates on the module 1 step cards

Notes:
```
POINT: Every learner creates, saves and reopens a minimal agent in the first 15 minutes, so platform problems surface now and not in the lab.
Talk Track:
The goal of this activity is to prove that your platform can build, save and reopen an agent before we need it.
Open the build check card for your platform in your workbook.
The starter instruction is on the card. Three lines.
The file is the code book from your kit. Copilot: use the .txt copy.
Ask it to list the file and its first heading.
Then save, close it and open it again. Ask again.
If it answers after you reopen it, you pass.
[START A 10-MINUTE TIMER. WALK THE ROOM OR THE BREAKOUT ROOMS. COPILOT FIRST]
[AT MINUTE 5, ASK: "Hands up if you are blocked." FOR EACH BLOCKED LEARNER: change platform, or pair with a learner on another platform for today]
[COPILOT LEARNER WHOSE AGENT CANNOT SEE THE FILE: "You may have no Copilot license or billing. Your lab card has a no-license path. You will use it in lab 1."]
[GEMINI LEARNER WHOSE NAME IS REJECTED: "Skill names use lowercase and hyphens: market-evidence-agent."]
[LOG EVERY BLOCKED BUILD: platform, plan, what failed. It goes to the monthly refresh]
TRANSITION: [AT MINUTE 10] Keep that agent open. It is the one you build on all day.
```

### Slide O.5: The big idea
- Layout: Blank
- Minutes: 2
- On-slide text: "AI can gather far more market signal than you can read. All of it is noise until you put it in context: what matters to your customers and what your business is trying to do. The agent gathers and organizes. You bring the context and make the call."
- Visual intent: Headline-style quote. "noise" in orange, "context" in teal. No image.
- Sources: none (course big idea, spec `course.big_idea`, decision C1)

Notes:
```
POINT: AI gathers market signal at scale, but only the PM's context about customers and the business turns it into a decision.
Talk Track:
Here is the one idea under the whole day.
[READ THE SLIDE]
Your agent can read every interview, every deal note and every feedback ticket.
More than you ever could.
But a pile of coded quotes is not an insight.
It becomes one when someone asks: does this matter to our customers? Does it matter to what we are trying to do?
That someone is you.
TRANSITION: So what is your job, if the agent does the reading?
```

### Slide O.6: You are the agent manager. One agent, five jobs
- Layout: Blank
- Minutes: 3
- On-slide text: Left, "You": Write the brief. Set quality checks and hand-off rules. Decide each flag. Audit a sample. Decide. Right, "The Market Evidence Agent": Module 1: problem backlog from interviews. Module 2: win/loss. Module 3: weekly feedback. Module 4: alternatives map. Module 5: stakeholder answers. Bottom: the ladder. Hand-run batch (modules 1, 2). Recurring run with a flag report (3). Hand-off between jobs (4, 5). An agent that faces other people (5).
- Visual intent: Left column short. Right column as 5 stacked job tiles, added one per module. A 4-step ladder along the bottom.
- Sources: none (spec `course_agent`, `autonomy_ladder`)

Notes:
```
POINT: Each learner builds one agent in module 1 and adds one job per module, and the learner's role is agent manager.
Talk Track:
You are the agent manager.
The agent does the workflow. You write its brief, set its checks and its hand-off rules, read its flags, audit it and decide.
One agent all day. It is called the Market Evidence Agent.
In module 1 you build it from a template and give it its first job: a problem backlog from your interviews.
A problem backlog is the agent's running list of market problems, with the evidence for each one.
Each later module adds one job.
[POINT TO THE LADDER]
And each module gives the agent a little more room.
First you run it by hand on a batch. Then it runs each week and you read only its flags.
Then one job hands its output to the next. At the end, it answers other people's questions, and you decide what gets sent.
Fall behind? Each module has a catch-up kit. You rebuild in about 5 minutes.
TRANSITION: Before you design anything, know your company's limits.
```

### Slide O.7: Know before you design
- Layout: Blank
- Minutes: 2
- On-slide text: Headline: "Know before you design." Approved tools: which AI tool may hold research data? Connectors: may the tool connect to your files and apps? Today's labs need none. Sharing: may you share an agent with your team? Code execution and file creation: is it on? Line at the bottom: "No answer? Use the case data today. Ask on Monday."
- Visual intent: Four tiles with icons: shield, plug, people, file. Bottom line in teal.
- Sources: cl-fo-06, mb-03 (platform matrix)

Notes:
```
POINT: Company limits on tools, connectors, sharing and code execution shape what you can build, so know them before you design.
Talk Track:
Four questions to answer for your company.
One. Approved tools. Which AI tool may hold research data? Interview notes can hold customer names.
Two. Connectors. Can the tool connect to your drives, CRM or ticket system? Today's labs need no connectors. You upload files.
Three. Sharing. Can you share an agent with your team? Some companies turn this off.
Four. Code execution and file creation. Some admins turn it off. Then your agent gives tables in chat instead of a file. That still works today.
On Copilot, an agent can use its knowledge files only with a Microsoft 365 Copilot license or pay-as-you-go billing. Your card has a path if you have neither.
If you do not know the answers, use the case data today. Ask your IT or security team on Monday.
TRANSITION: And one rule for every lab.
```

### Slide O.8: Data safety
- Layout: Blank
- Minutes: 1
- On-slide text: "Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss."
- Visual intent: Standard data safety box, the same one that sits on every lab slide and step card.
- Sources: none (spec `data_safety_note`)

Notes:
```
POINT: Every lab follows one data safety rule: approved tools only, and no client data, HIPAA health data or PII in a tool the company has not approved.
Talk Track:
This box is on every lab slide and every step card today.
[READ IT ALOUD]
Remember the heart failure study. That team used a setup approved for health data. Do the same.
If your own work cannot go in your tool, use the Larkspan case data. It is fictional.
TRANSITION: Last thing before we build.
```

### Slide O.9: Be great at product management before you are great at AI
- Layout: Blank
- Minutes: 2
- On-slide text: Headline: "Be great at product management before you are great at AI." Agenda strip, full day: Open. Module 1. Break. Module 2. Lunch. Module 3. Module 4. Break. Module 5. Close. Half days: day 1 modules 1 and 2, day 2 modules 3 to 5.
- Visual intent: Headline with "product management" in teal. A thin agenda strip at the bottom.
- Sources: none (spec `course.themes`, `agenda`)

Notes:
```
POINT: The agent amplifies the PM's judgment, so product management skill comes first and AI skill second.
Talk Track:
One more idea that runs through the day.
Be great at product management before you are great at AI.
The agent will code faster than you. It will never know which customer matters to your strategy.
Every lab ends with a call that only a PM can make.
Which problem comes first. Which deal finding goes to sales. What you tell a stakeholder.
[POINT TO THE AGENDA]
Here is the day. Five modules, one agent.
[HALF DAY: "Today is modules 1 and 2. Next time, modules 3 to 5."]
TRANSITION: Let's build the first job. Module 1.
```

## 3. Build check cards

Each card starts: "Build and save your own agent. Share your screen only when someone is stuck." Vendor docs and check dates are the same as the module 1 step cards (`module.md`, section 5). Check date 2026-11-26.

Starter instruction (paste all 3 lines):

```
You are the Market Evidence Agent for a product team.
Use only the files I give you. Never invent content.
When I ask, list each file you have and its first heading.
```

Question: "List the file you have and its first heading." Expected answer: the code book file and its first heading, "Code book: market problems (Larkspan Systems)".

Data safety (all cards): Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss.

### Claude
Saves: **Save instructions** saves the instructions. Files save when you add them.

| Step | Do this |
| --- | --- |
| 1 | In **Projects**, select **+ New Project**. Name it "Market Evidence Agent". |
| 2 | Paste the starter instruction into **Set project instructions**. |
| 3 | Add `code-book.md` to project knowledge with **+**. |
| 4 | In a new chat in the project, ask the question. |
| 5 | Close the browser tab. |
| 6 | Open the project again from **Projects**, and ask the question in a new chat. |

Pass: it answers after you reopen it.

### ChatGPT
Saves: as you go.

| Step | Do this |
| --- | --- |
| 1 | Select **New project** in the sidebar. Name it "Market Evidence Agent". |
| 2 | Paste the starter instruction in **•••**, then **Project settings**. |
| 3 | Add `code-book.md` to the project's files. |
| 4 | In a new chat in the project, ask the question. |
| 5 | Close the browser tab. |
| 6 | Open the project again from the sidebar, and ask the question in a new chat. |

Pass: it answers after you reopen it.

### Copilot agent builder
Saves: **Create** the first time. **Update** after each change.

| Step | Do this |
| --- | --- |
| 1 | Select **New agent**, then **Skip to configure**. In **Name**, type "Market Evidence Agent". |
| 2 | Paste the starter instruction into **Instructions**. |
| 3 | In **Knowledge**, add `code-book.txt` with **Upload**. |
| 4 | In the agent chat, ask the question. |
| 5 | Close the browser tab. |
| 6 | Open the agent again from **All agents**, and ask the question. |

Pass: it answers after you reopen it. If it answers but cannot see the file, you may have no Copilot license or billing. Use the no-license path on your lab 1 card.

### Gemini
Saves: **Create** the first time. **Save** after each change.

| Step | Do this |
| --- | --- |
| 1 | Select **Customize**, then **Skills**, then **Create**, then **Create manually**. Name it "market-evidence-agent". |
| 2 | Paste the starter instruction into **Instructions**. |
| 3 | Add `code-book.md` with **Add**, then files. |
| 4 | In a new chat, type **/**, pick your skill and ask the question. |
| 5 | Close the browser tab. |
| 6 | Open Gemini again, and ask the question with your skill in a new chat. |

Pass: it answers after you reopen it. Skill names use lowercase and hyphens. Gems are now skills.

Blocked on any platform: change platform, or pair with a learner on another platform for the day. Tell the instructor what failed.

## 4. LD spec: opening build check

| Field | Value |
| --- | --- |
| Objective | Each learner creates, saves, reopens and runs a minimal agent on their platform, so platform problems surface before lab 1 |
| Timing | 10 minutes, ends by minute 15 of the course |
| Setup (Zoom) | Main room. The instructor opens breakout rooms by platform only for blocked learners. Learners share a screen only when stuck |
| Setup (in person) | Learners at tables by platform. Instructor walks the room, Copilot first |
| Steps per platform | Section 3 build check cards |
| Materials | Starter instruction (3 lines, on the card). `kit-m1-template/code-book.md` (Copilot: `code-book.txt`). Platform readiness checklist, sent before class (decision 44) |
| Success criteria | The agent answers the question after the learner closes and reopens it |
| Debrief questions | None. One question at minute 5: "Hands up if you are blocked." |
| Fallback path | Change platform, or pair with a learner on another platform. Copilot with no license or billing: the agent cannot use knowledge files; the learner uses the no-license path in lab 1. The instructor logs each blocked build for the monthly refresh |
| Learner evidence | A saved agent named "Market Evidence Agent" (Gemini: market-evidence-agent) that answers after reopen |
