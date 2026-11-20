# Course Builder PRD

Nov 19, 2026 · @Dan Corbin

> Export note: this Markdown copy was taken from the Claude Doc on 2026-11-19 (doc revision 180), after Dan's comments, the quality bar draft, and Dan's decisions on the ChatGPT review were applied. The architecture diagram does not export to Markdown. Its place is marked below.

## Status

**Approved by Dan on 2026-11-19.** Phase 0 (repo setup) can start. Open items that do not block Phase 0: the Pragmatic source list (more decks coming), a second Copilot tester, the fallback case company, and the limits marked proposed.

The PRD draft is complete after 5 interview rounds. It waits for Dan's review. No code starts until Dan approves the architecture section.

| Round | Topic | State |
| --- | --- | --- |
| 1 | Course type, users, form factor, course format, workbook | Answered 2026-11-19 |
| 2 | Research: sources, depth, validation, citations | Answered 2026-11-19 |
| 3 | Quality bar, course structure, modules, learners | Answered 2026-11-19 |
| 4 | Exercises, workbook, deck, talk track, Pragmatic style | Answered 2026-11-19 |
| 5 | Agents, concurrency, review gates, where it runs | Answered 2026-11-19 |

### Decision log

| # | Decision | Source |
| --- | --- | --- |
| 1 | Write the PRD and architecture before any code | Dan, 2026-11-19 |
| 2 | Scope is standalone AI courses, not core course updates | Dan, 2026-11-19 |
| 3 | The V2 AI-first standards do not apply. The bar is higher and more AI-centric | Dan, 2026-11-19 |
| 4 | Dan is the only user. A Claude skill set is the form factor, not a custom app | Dan, 2026-11-19 |
| 5 | Dan owns the course IP. Pragmatic gets an exclusive license | Dan, 2026-11-19 |
| 6 | Course length is one day (7.5 hours with lunch and breaks), often split into two half days | Dan, 2026-11-19 |
| 7 | The system makes workbook content. The LMS hosts it later | Dan, 2026-11-19 |
| 8 | Systems thinking and workflow automation is the spine. Case studies support it | Dan, 2026-11-19 |
| 9 | Research rules: primary source for stats, 2 sources for claims, dated tool checks, 12-month age flag | Dan, 2026-11-19 |
| 10 | Name tools: Claude, ChatGPT, Microsoft Copilot first; Gemini second | Dan, 2026-11-19 |
| 11 | One Pragmatic Framework slide (2027 version), added after the deck is built | Dan, 2026-11-19 |
| 12 | Learners build Claude Projects and skills, ChatGPT projects and skills, Gemini skills, and Copilot agents (no custom GPTs or Gems). The courses are all agent work | Dan, 2026-11-19 |
| 13 | Own work first, fallback case study always ready | Dan, 2026-11-19 |
| 14 | Module arc and 40/60 talk to hands-on split. Keep POINT and Talk Track notes. Capability Map is a toggle. No single challenge point or core demo | Dan, 2026-11-19 |
| 15 | Every lab supports mixed platforms: Claude, ChatGPT, Copilot | Dan, 2026-11-19 |
| 16 | Drop the [AI USE CASE TT] notes block | Dan, 2026-11-19 |
| 17 | No pre-course survey. Platform access is handled in class | Dan, 2026-11-19 |
| 18 | Workbook in Word and PDF. One LD spec per exercise | Dan, 2026-11-19 |
| 19 | AI_Agents.26.07.02.pptx is the style reference and its master is the template | Dan, 2026-11-19 |
| 20 | Four gates: research brief, course spec and syllabus, each module, final QA | Dan, 2026-11-19 |
| 21 | Runs in Claude Code. Dan wants guidance and to learn the tool as it is built | Dan, 2026-11-19 |
| 22 | Gate reviews happen in Claude Docs | Dan, 2026-11-19 |
| 23 | AI Agents is complementary, not a prerequisite. No playbook teaching. Never repeat slides across courses. Labs use the native skill and agent builders | Dan, 2026-11-19 |
| 24 | Ask before rebuilding anything already approved. Platform refresh runs monthly | Dan, 2026-11-19 |

**Decisions from the external review (Dan, 2026-11-19)**

- 25: Research stays broad and scans all new platform features. The Verifier verifies only the features that a lab uses.
- 26: Copilot learners need permission to create agents in Copilot agent builder. Copilot Cowork and Fabric are not required.
- 27: Gate 2 needs a working proof for each build pattern. Gate 3 needs a card test of each lab on each platform. There is no test before each class; failures in class go to the monthly refresh.
- 28: The main time goal is Dan's active hours, compared with his hand-built estimate.
- 29: The ID team scores learners in beta and live classes.
- 30: The checker agents stay separate, and each has one job.

**Decisions after approval (Dan, 2026-11-20)**

- 31: Every lab also has Gemini step cards. Gemini builds use Gemini skills, because Gems are retired. Gemini cards get the same Gate 2 proof and Gate 3 card test as the other platforms.
- 32: The courses launch in 2027, so statistics and studies must be published in 2026 or later. Older ones are not used.
- 33: Boundaries and guardrails can be taught again in any course where learners build agents, with new slides. The AI Agents course will be replaced by an agent course per platform.
- 34: Each lab has a planted AI error. The warning fades over the day: told in the first lab, a hint in the middle labs, no hint in the last lab.
- 35: Modules climb an autonomy ladder across the day. Try it at Gate 2.
- 36: The life cycle stages are the Pragmatic Framework 2027 categories: Market, Focus, Business, Planning, Go-to-Market, Enablement, Operations. Each workflow row names its category and focus area.
- 37: Thin evidence is accepted for now. The monthly refresh adds new evidence as it appears.
- 38: Learners are agent managers. Each course has one agent that learners build in module 1 from a template and extend in each later lab. The agent does the workflow. The learner writes the brief, sets checks and hand-off rules, reviews the flag report and audits. Agent terms avoid the Pragmatic focus area names Exceptions and Escalations. A catch-up template is ready for each module.

## Problem and goals

The course builder cuts the time to make a Pragmatic Institute AI course, from research to a deck with talk track. Dan stays the SME and owns the final content decisions. Instructional designers add some content, and one or two other instructors may review it. The system researches, drafts and checks. Dan approves at each gate.

**Problem.** A new course needs research, an outline, modules, exercises, a workbook, a deck and a talk track. Today Dan does each step by hand, and each step repeats context from the step before.

**Goals (draft, Dan to confirm the numbers).**

| Goal | Measure | Target |
| --- | --- | --- |
| Less of Dan's time | Dan's active hours per module and per course, estimated from Claude Code session activity, plus testing time that Dan logs. Calendar days are also tracked | Baseline: about 160 hours for AI Agents for Product Professionals, built by hand. Proposed: 80 hours or less for course 1 and 50 hours or less for courses 2 and 3, not counting time to build the tool. Calendar target set after the first course |
| Fewer rework loops with Pragmatic | Unique required fixes in the first ID review, duplicates merged | 5 or less |
| Pragmatic standard met first time | Course passes every check in the Quality bar section | All checks pass |
| Traceable content | Claims with a cited source | 100% of factual claims |

**Non-goals (draft).** The system does not make final content decisions. It does not publish to the Learning Hub. It does not build or host agents for learners. Learners cannot reach Dan's skills or agents, so they build their own in class from the workbook step cards and copyable templates.

## Quality bar (draft, Dan to confirm)

A course is ready for Pragmatic only when it passes every check below. Rounds 2 to 4 set most of these rules. They were spread across the PRD; this section puts them in one place and adds pass or fail limits. Lines marked **(new)** are proposals that Dan has not yet confirmed.

**Release checks (the system and Dan run these before Pragmatic sees the course)**

| # | Area | Check | Pass limit | Checked by |
| --- | --- | --- | --- | --- |
| 1 | Workflow spine | Each module is tied to one workflow from the inventory and names the bottleneck it removes | 100% of modules | Critic, Gate 2 |
| 2 | Learners build | Each module has a lab where learners build a working skill, project or agent, not only prompts | 100% of modules | Critic, Gate 2 |
| 3 | Monday value (new) | Gate 2: the plan gives each learner working builds for their own work, plus templates to rebuild them. Beta: the ID team confirms that sampled learners saved and reran them | 3 or more per course | Critic at Gate 2; ID team in beta |
| 4 | Objectives | Each module has 2 to 4 objectives with observable verbs. A lab or debrief practices each objective | 100% | Critic, Gate 2 |
| 5 | Platform coverage | Each build pattern works on each platform (Gate 2 proof). Each complete lab card passes the card test on each platform (Gate 3) | 100% before release | Dan and testers |
| 6 | Clarity | Step cards meet the Clarity first limits: 6 steps or fewer, 1 action per step, 20 words or fewer per sentence | 100% | QA agent |
| 7 | Timing | Each module is 40% instructor-led and 60% hands-on, plus or minus 5 points (new). Slide times match the notes and the agenda | 0 mismatches | QA agent |
| 8 | Evidence | Each factual claim follows the research rules (primary source for stats, 2 sources for other claims) | 100% of claims | Verifier |
| 9 | Currency (new) | Each tool feature claim and step card has a check date | 30 days old or less at release | QA agent |
| 10 | No repeats | No repeat from the cross-course registry. A repeat is the same concept taught with the same agent in the same exercise, or a repeated slide. The same topic area (for example competitive monitoring) is allowed, and so is the same principle (this work should be automated by agents). Brief references to canon items are allowed. No contradiction with the series canon | 0 found | Critic and QA agent |
| 11 | Pragmatic fit | Each conflict in the alignment log has a decision from Dan | 0 open at Gate 2 | Alignment agent |
| 12 | Style | Each slide uses a master layout and has POINT and Talk Track notes | 100% | QA agent |
| 13 | Readability (new) | Body text on slides is large enough to read on Zoom. Screenshots that need a zoom-in are flagged. Dan views the rendered slides at Zoom size | 18 pt minimum | QA agent |

**Outcome checks (after release)**

The release checks prove that the course follows the rules. They do not prove that the course is good. These checks do.

| # | Check | Pass limit | Source |
| --- | --- | --- | --- |
| 14 | Unique required fixes in the first Pragmatic ID review, duplicates merged | 5 or fewer | Pragmatic review |
| 15 | Beta learners who finish the core path of each lab in the lab time and catch the lab's planted AI error (new) | 80% or more | ID team, beta classes |
| 16 | Beta course rating (new) | Set before beta: the evaluation question and the target score (Dan and the ID team) | Pragmatic evaluations |

**How Dan changes the bar.** Dan edits a limit here. The checker agents read their limits from this section, so a change applies to the next run.

## Users and scope

Dan is the only user. The system is a set of Claude skills and agents that Dan runs. It must be robust enough to do deep research and build a full-day course with little rework.

**Course lineup.** Three standalone courses replace the retiring AI for Product Managers course.

| Course | Topic area |
| --- | --- |
| Advanced AI for Market Research | Research, buyer and market insight |
| Advanced AI for Product Strategy and Planning | Strategy, roadmaps, planning |
| Advanced AI for Market and Launch | Positioning, go-to-market, launch |

**Course shape.**

- One day: 7.5 hours with lunch and breaks. Assumption: about 6 hours of teaching time (60 minutes for lunch, two 15-minute breaks). Dan confirmed this as the ideal day. Lunch can drop to 45 minutes when class runs long, which gives a 15-minute buffer. Agendas plan for 60 minutes.
- 4 to 6 modules. Content sets the count, not a fixed rule. That gives about 60 to 90 minutes per module.
- Often split into two half days. The split must fall on a module boundary near the midpoint. Each half day needs its own open and close.
- Mostly live on Zoom. Sometimes in person for one company or as a public course where anyone can sign up. Every exercise must work in Zoom breakout rooms and at a table.

**Deliverables to Pragmatic, in order.**

1. Syllabus and course outline (Pragmatic reviews this first).
2. Complete deck with all slides and talk track.
3. Proposed exercises.
4. Proposed workbook content: materials, resources and exercises that the LMS hosts later.

**Ownership.** Dan owns the course IP and gives Pragmatic an exclusive license. The system keeps Dan's content separate from Pragmatic brand assets (template, logos), so the content stays portable.

**Out of scope.** Publishing to the LMS. Building the Pragmatic template. Core course updates (the deck modernizer skill covers those).

## Pragmatic Institute course format

Round 3 set the house rules for the Advanced AI courses. Some rules come from Dan's core course skills. Others replace them, because these courses go further than the core courses.

**House rules**

1. Every module is built on a real PM workflow and the bottleneck it removes.
2. Learners build, not only prompt. Learners are agent managers: one course agent grows module by module, and the learner manages it (decision 38). Labs build Claude Projects and skills, ChatGPT projects and skills, Gemini skills, and Copilot agents. Labs also use the newest PM-relevant features, for example ChatGPT folders, plugins, scheduled tasks and agents that run on a schedule, and Claude Design for prototyping. No custom GPTs or Google Gems: they are being deprecated. Research always scans for the latest features on each major platform.
3. Learners use their own work when they can. Every lab also has a fallback case study.
4. Time split per module: 40% instructor-led, 60% hands-on.
5. Every slide has notes in this format: `POINT:` (one sentence), then `TALK TRACK:`. Activity talk tracks start with "The goal of this activity is".
6. The Green, Yellow, Red Capability Map is a course setting that Dan turns on or off.
7. No single required challenge point and no single core agent demo. The course favors agentic workflows over a series of prompts. Prompts, projects, folders and plugins still have a place where they fit.
8. Mixed platforms in every class: Claude, ChatGPT, Copilot and Gemini. Every lab works on each platform and has a step card for each (decision 31).
9. File names: `<COURSE>_<version>_DRAFT_vN.pptx`. The system edits copies only.

**Resolved questions**

- Does the `[AI USE CASE TT]:` notes block stay? Resolved: no. All talk track in these courses is AI use cases, so the block is dropped (decision 16).
- Resolved: one LD spec per exercise, fields listed in the workbook section (decision 18).
- Learner prerequisites for "Advanced" Resolved: no prerequisites. Familiarity with building agents and skills is recommended. Because some learners will be new to the builders, the first lab includes a short fast-start card per platform.

## Research stage

Research starts from PM workflows, not from AI tools. Systems thinking is the spine of every course: find the workflows in the topic area, find the bottlenecks, and move low-judgment, high-repetition work to AI. That gives PMs more time for strategy and the market. Case studies and stats support this spine. They do not lead it.

**Research tracks, in priority order**

| # | Track | Question it answers | Main output |
| --- | --- | --- | --- |
| 1 | Workflows and bottlenecks | Which PM workflows in this topic area should AI take, and which stay human? | Workflow inventory |
| 2 | What works | Which AI methods and newest platform features work for each workflow, on which platform? | Method library |
| 3 | PM needs | What do PMs do in this topic area, and where does the time go? | Needs summary |
| 4 | Proof | Which case studies and recent stats show the impact? | Evidence ledger |

**Workflow inventory.** This is the key research output. Each row is one PM workflow in the topic area. The system scores each row on judgment (low to high) and repetition (low to high), names its Pragmatic Framework 2027 category and focus area (the life cycle stage, decision 36), names the bottleneck it removes, and names the decision that stays with the PM. Low judgment and high repetition means a candidate for AI. The inventory drives the module plan in the next stage.

**Sources**

| Tier | Sources | Use |
| --- | --- | --- |
| 1 | Claude, ChatGPT, Microsoft Copilot docs and guides; Gemini to a lesser degree | Methods, features, examples |
| 2 | Studies, academic papers, analyst reports | Stats and evidence, cited |
| 3 | Trusted product leaders and sites with in-depth work on how PMs use AI day to day | Practices, examples, case studies |
| 4 | Pragmatic Framework | Alignment check on terms, rules and messaging; one slide with the 2027 framework, added after the deck is built |

**Rules (approved by Dan)**

1. A statistic needs a primary source.
2. Any other factual claim needs 2 independent sources.
3. A tool feature claim needs one dated vendor doc. It does not need a second source.
4. Statistics and studies must be published in 2026 or later, because the courses launch in 2027 (decision 32). Other sources older than 12 months get a flag. Dan decides if they stay.
5. Use stats only where they make a point. Do not fill slides with stats.
6. Name tools where it helps. Focus on Claude, ChatGPT and Microsoft Copilot. Gemini is secondary.

**Industry coverage.** Many Pragmatic clients are enterprises both in and out of tech: software, FinTech, health care, manufacturing, hardware, services, and internal product management (internal platforms and tools). Research looks for workflows, examples and evidence in these contexts, not only in software products. Hardware and internal product management are a priority. Services and manufacturing are good to have. When research cannot find good material for a context, it records the gap and continues; this is not a failure. Where possible, each workflow row notes how the workflow works in hardware and internal product management.

**Pragmatic alignment check.** All research must fit Pragmatic Institute's framework, language, rules and past messaging. A Pragmatic alignment agent compares the research brief against Pragmatic sources. It does not drop content that conflicts. It logs each conflict for Dan, with three options: align with Pragmatic, update the message because AI changed the work, or keep both and explain the difference in class. Old Pragmatic positions do not limit the course. Dan decides each item.

The alignment log goes to Gate 1 with the research brief. Before the first Stage 1 run, Dan names the Pragmatic sources and their versions that the agent uses (for example framework materials, glossary, course materials, public site and blog). An empty alignment log passes only when Dan can trace the comparison to those sources.

**Quality checks in this stage.** Three independent checkers run before the Synthesizer. After the Synthesizer, the Verifier runs again as a trace check: each recommendation in the final brief must link to verified ledger entries, and the Verifier flags wording that goes past what the sources support. This is necessary because Dan approves the final brief, not the checked claims. The Stage 2 Critic is too late: it checks the outline, and weak research would already be built into it.

| Checker | Question it answers |
| --- | --- |
| Verifier | Is each claim true, sourced and recent enough? It verifies all workflow and evidence claims, and the platform features that a candidate lab uses. Other new features stay in the platform matrix, marked as not verified, for later courses or updates. |
| Research critic | Is the research complete and deep enough? Are key workflows missing? Do sources lean on vendor marketing? Does each workflow show a real bottleneck? Did research look for hardware and internal product management examples, and record the gaps where it found none? |
| Pragmatic alignment agent | Does anything conflict with Pragmatic's framework or messaging? |

If the Research critic finds a gap, the researcher for that track runs again on the gap, one time. Gaps left after that go to Dan at Gate 1.

**Expected risk.** Recent, rigorous studies on how PMs use AI are rare. Track 4 evidence will be thin. The system reports gaps. It does not fill them with old or weak stats. Dan's examples and use cases from the class fill the gap instead. The check that matters most: each chosen workflow must be a common PM bottleneck and a good AI candidate. The Verifier confirms this with at least 2 independent practitioner or vendor sources, even when no study exists.

**Stage outputs (go to Gate 1).** Research brief, workflow inventory, method library, platform matrix (features, tiers, connectors, check dates for Claude, ChatGPT, Copilot, Gemini), evidence ledger (claim, sources, date, status), source register, gaps list, Pragmatic alignment log.

**Gate 1 decision.** The packet shows each candidate workflow in one row: its bottleneck, evidence, open gaps, the decision that stays with the PM, and the proposed lab. Dan marks each row retain, defer or reject.

**Gate 1 acceptance test (proposed).** These are Dan's spot checks, about 45 minutes in total. They do not replace the agents' full verification of the packet. Dan picks the workflows, claims and sources to check. Gate 1 passes when all 7 checks pass.

| # | Check | Pass if |
| --- | --- | --- |
| 1 | Can the research support a full course? | Dan can select 4 to 6 distinct workflows. Each names an input, a recurring bottleneck, an output and the PM decision that the output informs. Two variations of one task count as one workflow. Hardware and internal product management examples are included where research found them, and gaps are recorded |
| 2 | Are the bottlenecks real? (2 workflows) | Two independent sources describe the bottleneck itself. Two articles that repeat one vendor study count as one source. A feature page that shows AI can do a task does not prove that the task is a burden for PMs |
| 3 | Does each workflow teach PM judgment? (same 2 workflows) | Dan can point to the work AI does, the decision the PM keeps, and one specific AI error the PM must catch |
| 4 | Did the final brief keep the evidence? (1 statistic, 1 other claim, 1 tool claim) | Each claim links to a ledger entry. The statistic matches its primary source, including population and time period. The other claim has 2 independent sources. The tool claim has a dated vendor doc. The brief keeps the sources' limits |
| 5 | Is a lab possible on all four platforms? | Each selected workflow maps to a core build with no connectors on Claude, ChatGPT, Copilot agent builder and Gemini skills, with dated vendor evidence. An unknown permission is recorded as open. Hands-on proof comes at Gate 2 |
| 6 | Did the alignment check use the right Pragmatic material? | Dan knows the sources and versions used, one traced comparison is accurate, and each conflict has a decision or a named Gate 2 follow-up |
| 7 | Can Dan make the decision from the packet? | At least 4 workflows earn retain. None depends on an open question that could break its bottleneck, its PM decision or its three-platform path |

**Worked example.** Before the first run, the system drafts one example workflow row for Dan to approve. The researchers use it as the model for every row.

## Organize and outline stage

This stage turns the approved research into one locked course spec and the syllabus. The course spec is the contract that every later agent reads. Parallel work starts only after Dan locks it.

**Inputs.** The research brief, workflow inventory, method library and platform matrix from Gate 1.

**Course spec (locked at Gate 2)**

| Part | What it holds |
| --- | --- |
| Promise | One sentence on what the learner can do after the course |
| Learning objectives | Course objectives and 2 to 4 objectives per module, each with an observable verb |
| Learner profile | Prerequisites, platform mix, data access limits |
| Module plan | 4 to 6 modules, each tied to one workflow from the inventory, with minutes per module |
| Agenda | Full-day agenda and two half-day agendas, split on a module boundary |
| Platform matrix | Per platform: features, access tier, connectors, check date |
| Fallback case | One case company and its data, used when learners cannot use their own work. One company for the whole course: every module and exercise uses the same case. No new company per module or exercise. The case builder makes this data in Stage 2. Gate 2 locks the records that each lab uses and the result that those records support, before module builders start |
| Glossary and voice | Terms, examples, tone. Stops drift between modules made in parallel |
| Settings | Capability Map on or off; other toggles |

**Outputs.** The course spec and the syllabus draft. The syllabus is deliverable 1 to Pragmatic.

**Why one agent, not many.** The outline needs one view of the whole day. A planner agent drafts it. A separate critic agent checks it against the house rules, the timing and the workflow inventory. Dan decides.

## Module, slide, and exercise design

Every module follows one arc, and every lab has one goal with a variant per platform. Across the day, modules climb an autonomy ladder: an agent run by hand on a batch, then an agent on a schedule that sends a flag report, then agents that hand work to other agents (decision 35, tried at Gate 2). Module agents build modules in parallel from the locked course spec.

**Module arc (example: 75-minute module, 40/60 split)**

| Step | Minutes | Mode |
| --- | --- | --- |
| Workflow and its bottleneck | 10 | Instructor-led |
| Live build demo | 12 | Instructor-led |
| Build pattern and lab brief | 8 | Instructor-led |
| Hands-on lab | 35 | Hands-on |
| Debrief and share-out | 10 | Hands-on |
| Capability Map (if on) | in debrief | Instructor-led |

**Lab design rules**

1. One lab goal, stated without a platform, plus one decision the PM makes and one likely AI error the PM must catch. The warning fades over the day: the first lab says an error is planted, middle labs say "Audit before you approve", and the last lab gives no hint. The debrief reveals it (decision 34). Example: "Build an assistant that turns raw interview notes into a coded insight table."
2. A core path that works on every platform. Stretch steps for platforms that can do more.
3. Per-platform step cards for Claude, ChatGPT, Copilot and Gemini (decision 31). The step cards go in the workbook, not on slides. Dan demos on one platform only. Breakout rooms group learners by platform so they help each other. So each step card must be self-serve: a learner can finish the lab from the workbook alone, with no demo on their platform. The Gate 3 card test checks this. Slides show the pattern once. Each card starts with: "Build and save your own agent. Share your screen only when someone is stuck." Each fast-start card has one annotated screenshot of where to start and which field the template goes in.
4. Two input paths: the learner's own work, or the fallback case data. A "Start here with sample data" block sits directly under each platform's steps.
5. A data safety note: what learners must not paste into a tool their company has not approved, for example client data, health data protected by HIPAA, and personal data (PII).
6. Setup for Zoom breakout rooms and for in-person tables.
7. Success criteria on the slide before the lab and at the end of each card: a second sample input and a concrete pass condition, so learners can check their own output in the breakout room. The debrief names what AI did poorly.

**Clarity first (the rule that matters most).** Most learners get stuck on the directions, not the concept. Each exercise teaches one core message and gets learners comfortable with it. It does not try to teach everything. Learners build on it later.

| Check | Limit (draft, Dan tunes after feedback) |
| --- | --- |
| Steps per step card | 6 or fewer |
| Actions per step | 1 |
| Sentence length in directions | 20 words or fewer, plain words |
| Core learning message per exercise | 1, stated in the lab brief |

The QA agent checks every step card against these limits. Dan says when an exercise is too simple or too complex, and the limits change to match.

**Biggest design risk.** Copilot often lags behind Claude and ChatGPT, and learners' connectors and data access are unknown. Pragmatic cannot survey learners before class. Controls: an opening build check in the first 15 minutes (proposed), where each learner creates, saves and runs a minimal build on their platform, and a learner who is blocked changes platform or pairs with another learner, a "know before you design" slide on company limits, a core path that needs no connectors, and the Gate 3 card test. The system cannot test inside a learner's company Copilot. When a build fails for a learner in class, Dan logs it, and the monthly refresh picks it up. Copilot learners must have permission to create agents in Copilot agent builder; Pragmatic's course description says so. Copilot Cowork and Fabric are not required, and no lab depends on them. Whether agent permission also allows Copilot skills is not yet verified.

**Slide spec.** Each slide in the course model holds: the point, the on-slide text, the visual intent, the talk track, sources cited, and timing. The deck agent renders slides from this spec.

## Workbook, deck, talk track, and Pragmatic style

The style reference is Dan's deck AI_Agents.26.07.02.pptx (74 slides). Its slide master holds 30 Pragmatic layouts. The deck agent builds every new deck on a clean copy of that master, so the brand comes from the layouts, not from guesses.

**Slide types to use (from the reference deck)**

| Layout | Use | Look |
| --- | --- | --- |
| Course Cover | Title slide | Teal gradient, white leaf mark, course name in caps |
| Chapter Break | Course module list; each module opener | Teal side band, "MODULE N" tag, title, one-line promise, 3 objective bullets |
| Blank, Blank_No Dots, 1_Blank | Concept slides | Headline with key words in teal or orange; dot grid accent |
| 1_prompt | Instructor live demo | Orange "LIVE DEMO" tag, title, running example name, minutes |
| Activity | Learner lab | Orange side band "ACTIVITY", title, minutes, numbered or STEP steps |
| debrief | After each lab | Navy side band "DEBRIEF", 3 to 4 question prompts |
| Blank_Tiles | Welcome and platform login | Tiles |
| Action Plan, Put it Into Action, Feedback | Close | Course close pattern |

**Brand tokens (from the theme).** Fonts: Roboto Condensed, Roboto Condensed Black, Roboto Medium, Roboto Light, Arial. Colors: teal #059CA0, navy #234874, blue #2462A4, orange #F37720 and #D24C25, gray #696D6E. Footer: logo, copyright line, slide number.

**Patterns to keep**

1. One course thesis line, repeated at the open and the close (the reference uses "Rent the tech. Own the playbook.").
2. One instructor running example threaded through every live demo (the reference uses the Competitive Intel Watchdog).
3. Demo, then activity, then debrief, in that order.
4. A platform translation slide: one concept, the feature name on each platform.
5. An opening poll and a platform login slide.

**Talk track format.** Each slide's notes start with `POINT:` and `Talk Track:` (decision). The `[AI USE CASE TT]:` block is dropped. The talk track keeps Dan's voice from the reference deck: short spoken lines, `[STAGE DIRECTIONS]` in brackets, `TRANSITION:` lines, and an activity header with the minutes.

**Quality checks the reference deck shows we need**

- Timing must match. In the reference, three activity slides show one time and the notes show another (slide 27: 12 MIN vs 15; slide 48: 20 MIN vs 25; slide 66: 12 MIN vs 15). The QA agent checks every slide time against the notes and the agenda.
- Minimum readable text size. Some screenshot slides (for example slide 41) are too dense to read on Zoom. The QA agent flags text under the minimum size and screenshots that need a zoom-in.

**Workbook.** Word and PDF only. The workbook has two jobs. In class, it guides learners through each exercise so they know how to finish it. After class, it is a takeaway they keep using. In class: per-platform step cards, exercise data, the fallback use case, and a workflow inventory worksheet. After class: copyable instruction and skill templates, references, and resources with sources. Rule: anything we want learners to use after class goes in the workbook. Platform screens change often, so every step card carries a check date and goes into the refresh cycle.

**LD spec, one per exercise.** Fields: objective, timing, setup (Zoom and in person), steps per platform, materials, success criteria, debrief questions, fallback path.

## System architecture

The course builder is a set of Claude Code skills and subagents in the CourseBuilder repo. Four stages run in order, with a Dan gate after each. Agents run in parallel inside a stage. All stages read and write one course model in the repo. The deck, workbook and LD specs are built from that model, so an edit in one place reaches every output.

[Diagram not exported: course builder pipeline, 4 stages, 4 gates. See the Claude Doc.]

Read it top down: each stage ends at a gate, and only Dan's approval opens the next stage.

**Concurrency, stated plainly.** Stages cannot overlap, because each gate changes what the next stage builds. Parallel work happens inside stages: 4 research agents, then 4 to 6 module agents, then 3 renderers. The case builder runs in Stage 2, so module builders start from locked case data.

**Agents by stage**

| Stage | Agents | Runs | Output | Gate |
| --- | --- | --- | --- | --- |
| 1 Research | Workflow, Methods and platforms, PM needs, Evidence researchers; then Verifier, Research critic and Pragmatic alignment agent; then Synthesizer | 4 in parallel, then 3 checkers in parallel, then 1 | Research brief, workflow inventory, platform matrix, evidence ledger | Gate 1: Dan approves the brief |
| 2 Outline | Planner, then Case builder, then Critic, then Syllabus writer | In sequence | Locked course spec, locked case data, syllabus, platform proof for each build pattern | Gate 2: Dan approves; Pragmatic reviews the syllabus |
| 3 Modules | One Module builder per module; then Consistency reviewer and Verifier (new claims only) | 4 to 6 in parallel, then 2 | Slide specs, talk track, labs, step cards, LD specs | Gate 3: Dan tests each lab card, then approves each module |
| 4 Production | Deck, Workbook and LD spec renderers; then QA agent | 3 in parallel, then 1 | .pptx, .docx, .pdf, QA report | Gate 4: Dan approves final QA |
| Refresh | Platform check agent | Monthly | Recommended updates: checks all course material against what changed in the market and on the AI platforms (features, step cards, examples, stats) | Dan approves each edit |

**Guardrails across all stages**

1. **No repeats across courses.** A cross-course registry lists the topics and slides in each Advanced course and in the AI Agents course. The Critic and the QA agent flag any repeat. Playbook teaching stays out; playbook markdown files can go in the workbook as handouts. The registry also holds a series canon: the shared themes, principles, concepts, terms and best practices. Every later course reads the canon first. The Critic and QA agent flag any contradiction with it. A course can build on or refer back to a canon item, but must not reteach it or change it. Exception: boundaries and guardrails can be taught again in any course where learners build agents, with new slides (decision 33). New canon items go in only after Dan approves them.
2. **Ask before rework.** The system records a fingerprint of each approved item. If a later change touches an approved item, the system lists what it wants to rebuild and waits for Dan.
3. **Independent checks.** The Verifier, Critic, Consistency reviewer and QA agent do not see the drafting agent's reasoning, only its output. A checker that shares the writer's context tends to agree with it.
4. **Gate packets as Claude Docs.** Each gate publishes a Claude Doc for Dan to read and comment on. The system applies the comments to the course model, not to the doc.

**What each gate checks.** Each gate needs a different kind of proof. Each checker has one job, so two checkers do not check the same thing.

| Gate | Proof Dan sees | Checkers and their one job |
| --- | --- | --- |
| 1 Research brief | Documents: sources, the workflow rows, and dated vendor docs that show a lab is possible on each platform. Dan's acceptance test is a spot check; the agents verify the whole packet | Verifier: sources, before and after the Synthesizer. Research critic: coverage and depth. Alignment agent: Pragmatic conflicts |
| 2 Course spec and syllabus | A working proof: Dan builds, saves and reruns each distinct build pattern on Claude, ChatGPT, Copilot agent builder and Gemini. This is usually 2 to 3 patterns per course, not every lab | Critic: course design (objectives to labs, timing, planned builds, overlap with the registry). It does not check the Gate 1 evidence again |
| 3 Each module | A card test: Dan tests each complete lab card on each platform, from the card alone (see the card test below) | Consistency reviewer: the demo, case data, cards, expected output and debrief agree. Verifier: only claims that are new since Gate 1 |
| 4 Final production | Checks on the delivered .pptx, Word and PDF files | QA agent: rendered files only (layouts, notes, text size at Zoom size, timing, templates that copy correctly). It does not judge content again. If production changed a learner action, Dan tests that path again |

**Card test (Gate 3).** The tester opens the real Word or PDF card and follows it with no other help, until the build is saved and passes the card's second sample input. The tester records the minutes and each place where they got stuck, for each platform separately. Dan tests all cards. At least one other person who did not write the card tests the Copilot card for each module (proposed), because the author of a card knows the missing steps without seeing them. Dan does not test again before each class. When a build fails for a learner in class, Dan logs it, and the monthly refresh picks it up.

**Repo layout (draft)**

```
CourseBuilder/
  CLAUDE.md                 house rules, writing rules, how to run a stage
  .claude/skills/           course-research, course-outline, course-modules, course-produce, course-refresh
  .claude/agents/           one file per subagent role
  shared/                   Pragmatic template, voice guide, cross-course registry
  courses/<course>/
    status.yaml             stage, gate approvals, fingerprints
    research/               sources, claims, workflow inventory, platform matrix
    spec.yaml               locked course spec
    modules/                one file per module: slides, talk track, labs, LD specs
    case/                   fallback case data, running example
    build/                  rendered .pptx, .docx, .pdf
```

**Build plan.** Build one thin slice first: Advanced AI for Market Research, Stage 1 only, end to end to Gate 1. Then add one stage at a time. In Phase 3, one module goes through Gates 3 and 4 before the other modules start, so Dan can compare his hours with his hand-built estimate. Each phase also teaches one Claude Code idea, so Dan learns the tool while it gets built.

| Phase | Builds | Claude Code idea Dan learns |
| --- | --- | --- |
| 0 | Repo, CLAUDE.md, folders, Claude Docs gate test, hours log | CLAUDE.md and project memory |
| 1 | Stage 1 research for one course | Skills and parallel subagents |
| 2 | Stage 2 outline and syllabus | Checker agents and gates |
| 3 | Stage 3 modules | Shared spec as a contract between agents |
| 4 | Pragmatic template setup, Stage 4 renderers and QA | Scripts the agents call; hooks for checks |
| 5 | Monthly refresh | Scheduled runs |

## Risks, assumptions, and open questions

**Early risks**

| Risk | Why it matters | First idea for a fix |
| --- | --- | --- |
| Parallel agents drift apart | Modules made at the same time can use different terms, examples and voice | One locked course spec (objectives, glossary, voice, examples) that every agent reads |
| Separate files per stage go out of sync | An edit to the outline does not reach the deck or workbook | One structured course model; deck, workbook and talk track are views made from it |
| AI research goes stale fast | AI tools and practices change each quarter | A source date rule and the monthly refresh (decision 24) |
| Concurrency is smaller than it looks | Most stages depend on the stage before | Run agents in parallel inside a stage, not across stages |
| Custom app is a large build | Months of work before the first course ships | Resolved: Dan chose a Claude skill set (decision 4) |
| No official Pragmatic master deck | The reference deck master can miss layouts or carry old content | Resolved: the AI_Agents.26.07.02.pptx master is the template (decision 19). The deck agent builds on a clean copy |
| Claude Docs may not be reachable from Claude Code on Dan's computer | Gate reviews depend on it | Test it in Phase 0. Fallback: a Word file per gate |
| Course repeats content from AI Agents or another Advanced course | Learners do not want to pay twice for the same lesson | Cross-course registry, checked by the Critic and QA agents |
| Dan is new to Claude Code | A big first project can stall | Thin slice first; one Claude Code idea per phase |

**Assumptions to confirm**

- Teaching time is about 6 of the 7.5 hours (confirmed). Teaching time = slides + demos + learner activities.
- Output goes to Pragmatic for review, not straight to class (confirmed). Release path: build, then Pragmatic sign-off, then a couple of beta classes with the alumni group, then launch. A beta feedback step maps each piece of feedback to the module, slide or lab it touches, proposes a change, and waits for Dan.
- The three courses share one pipeline and one house style. Only the research and content differ (confirmed). Later courses must not contradict earlier ones: themes, principles, concepts and best practices stay consistent, so moving between courses feels seamless.
- Fast-moving AI content needs a refresh check once a month, not before each class. Dan teaches almost weekly, so a per-class check is too often (decision 24).
