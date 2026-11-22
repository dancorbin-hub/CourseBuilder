# Gate 2 packet v2: Advanced AI for Market Research

- Course id: `market-research`. For Dan. Version 2, 2026-11-22. Version 1 (with your comments) is the second tab, and in git history.
- Files under review: `spec.yaml` v0.3, `outline/development-brief.md`, `outline/syllabus.md` (third tab), `outline/capability-mapping.md`, `case/` (Larkspan Systems).
- Gate 2 is approved when you say so. Then Pragmatic reviews the syllabus.

## 1. What changed since version 1

| # | Change | Why |
| --- | --- | --- |
| 1 | **Problem backlog replaces the PM's bar.** The agent keeps a problem backlog. Each problem has an evidence profile: interviews (not quotes), accounts, segments, source type, urgency with a quote, pervasiveness, willingness to pay clues, dates. The agent proposes a ranking with reasons. The PM decides the order, what is a pattern and what goes to validation | Your comment on decision 4: priority is relative across the backlog. The workbook agrees (skill 1.1D, skill 3.3) |
| 2 | **Fact labels only:** "single source", "AI-moderated only", "one segment only". No status, no threshold. Single-source problems stay for trend tracking | Same. The agent never writes "pattern" or "validated" |
| 3 | **Pragmatic terms.** Learner text uses urgency, pervasiveness and willingness to pay, not frequency, intensity and impact. Referred to as known from Foundations and PDW-AI | Workbook skill 1.1D |
| 4 | **Capability and skills proposed** from the 2027 workbook (section 3) | Your upload |
| 5 | **Half days fixed:** each 09:00 to 12:30, 195 teaching minutes. The 45-minute lunch line is gone | Your comment on item 12 |
| 6 | **Decisions 6, 8, 9 and 10 applied.** Module 4 story told as Pragmatic or client story. Module 4 stays 55 minutes. A Fleet Data Platform (internal PM) question is in lab 5 (Q5). Stretch steps diverge by platform; Copilot Studio, Power Automate and Antigravity are out of scope | Your answers |
| 7 | **Critic ran twice more.** All must-fix items are fixed. Every case count was recounted by hand | Quality |

Full day timing is unchanged: 09:00 to 16:30, 60-minute lunch, 360 teaching minutes, 41% instructor-led, every module 40/60.

## 2. Decisions for you

Answer with the number and your choice. I recommend the first option in each.

| # | Decision | Options | My recommendation and why |
| --- | --- | --- | --- |
| 1 | **Confirm the problem backlog model** (section 1, items 1 to 3). The spec and case already use it | A: confirm. B: roll back to v0.2 | **A.** It is your view, and the workbook supports it. Everything in v0.3 depends on it |
| 2 | **Confirm the capability and skills** (section 3) | A: confirm as proposed. B: module 4 uses 1.3 instead of 1.2. C: change others | **A.** Skill 1.2A ("what prevents switching", "why and how evaluators buy") fits the alternatives map better than 1.3 |
| 3 | **Confirm offering intent Develop and Apply** for all 5 modules, and that the ID team confirms the learner evidence list | A: yes. B: change | **A.** No change since Gate 1 |
| 4 | **Lab 1 fix.** The template leaves out one rule on purpose. The learner adds it after the planted error: "If all quotes for a problem come from 1 interview, send it to the flag report." A ranking rule is an optional second rule | A: flag rule as the fix. B: ranking rule as the fix | **A.** It is a hand-off rule, not a threshold, and the case results already use it. Risk: the new evidence profile shows the interview count next to the quotes, so the error may show less often. Proof P1 tests this |
| 5 | **Lab 5 questions.** 4 run questions did not fit in 30 minutes. Q1, Q2 and Q5 are core; Q3 is optional on the case path; Q4 is the check in the debrief | A: accept. B: drop Q5 (internal PM) instead | **A.** Q5 keeps the internal PM in the course (your decision 9). Cost: the "sources disagree" rule is tested only by learners who ask Q3, or on their own work |
| 6 | **Half-day module lengths.** Module 1 is 80, module 2 is 75 and module 5 is 60 minutes in the half days (full day: 70, 70, 65). Day 2 open and course close are 10 minutes each | A: accept. B: other split | **A.** Day 1 is the build day. New builders need the extra time |
| 7 | **Win/loss program rule.** "Minimum 10 decided deals per batch" (Gate 1, PA-04) stays as a rule for how often to run a batch, not as a test of what is real | A: keep. B: remove | **A.** It is a Pragmatic program practice and it decides cadence only |
| 8 | **Screening as a lab 1 stretch step** (decision 11 in v1, no answer yet) | A: accept. B: drop it | **A.** It keeps the step card at 6 steps. The case has the file and checked results |
| 9 | **Update 2 fingerprinted Gate 1 files** to the backlog model: workflows.yaml row 01 (old "2 or more interviews" rule) and the worked example row v3 ("PM's bar", "emerging"). I record new fingerprints | A: yes. B: leave them | **A.** Later agents read these files. Old rules there would bring the bar back |

Provisional until your proof (from your comments, no action needed now):

| Decision | Status |
| --- | --- |
| v1 decision 2: keep "count interviews, not quotes" in the template | Provisional C. Final after proof P1. If the error fails on 2 or more platforms, I bring option B back |
| v1 decision 3: segment rule as a course rule | Provisional A. Test in lab 5: the agent must not say "food service buyers want" from 1 Food service interview (I-105) |

Still deferred: the bond story (pick before module 1 is built; I recommend candidate 1, JAMIA).

## 3. Capability and skills (proposal from the 2027 workbook)

| Item | Workbook id and name | Modules |
| --- | --- | --- |
| Capability | 1 Market Intelligence | All |
| Primary skill | 1.1 Market Problem Identification | 1, 3, 5 |
| Primary skill | 1.2 Market Segmentation | 4 |
| Primary skill | 1.3 Market Discovery | 1, 2 |
| Secondary skill | 8.1 Market Data Context and Pattern Recognition | 2, 3 |
| Secondary skill | 8.4 Data Narrative and Stakeholder Communication | 5 |

| Module | Framework box | Key competencies |
| --- | --- | --- |
| 1. Problem backlog | Market Problems | 1.1A, 1.1B (noisy 20%: the planted error), 1.3D |
| 2. Win/loss and match rate | Win/Loss Analysis | 1.3A, 1.3C, 8.1B |
| 3. Weekly run | Market Problems | 1.1B, 1.1C, 8.1B, 8.1D |
| 4. Alternatives map | Competitive Landscape | 1.2A |
| 5. Stakeholder answers | Market Problems | 1.1C, 1.1D, 8.4A, 8.4C |

What the workbook confirms: the Market Intelligence AI text says to keep source provenance, separate evidence from inference and require real-market validation before decisions. That is the agent manager design.

Gaps to know:

1. The Competitive Landscape box has primary skill 2.2 Opportunity Prioritization, which belongs to the Focus (Strategy) course. Module 4 uses 1.2, a secondary skill on that box, and does not claim 2.2.
2. The Win/Loss Analysis box has no primary skill. Module 2 uses 1.3. Tell the ID team.
3. PDW-AI maps to the same skills (1.1, 1.2, 1.3, 8.1, 8.4). It is a workshop (Introduce). This course is Develop and Apply, with an agent managed over time. The no-repeat rule covers slides and exercises, not skills.

## 4. Your actions (not decisions)

| # | Action | When |
| --- | --- | --- |
| 1 | Run the platform proof: patterns P1, P2 and P3 on Claude, ChatGPT, Copilot and Gemini, plus items G2-PF-01 to 05 (v1 tab, section 6; updates below) | Before the Gate 2 lock |
| 2 | Send the module 4 story (Pragmatic or unnamed client) | Before module 4 is built |
| 3 | Tell the PDW-AI owner about the AI-moderated interview rules | Before Pragmatic review |
| 4 | Tell Pragmatic that MKT slide 7 uses old Framework names | Before Pragmatic review |
| 5 | Log your proof hours with `activity=gate-2-proof` | As you go |

Proof updates since v1:

- P1 pass now means: the agent returns a problem backlog with an evidence profile, fact labels and a proposed ranking, and the vocal buyer (I-104) ranks near the top before the fix.
- P3 has no timing check (decision 8).
- G2-PF-03: the evidence pack is now about 15,400 characters. Test that Copilot chat accepts it, or the kit splits it.
- Stretch steps: schedule and second agent appear only on Claude and ChatGPT cards, after a Stage 3 check.

## 5. Open items after Gate 2

| # | Item | Owner | When |
| --- | --- | --- | --- |
| 1 | Bond story pick | Dan | Before module 1 is built |
| 2 | Therapy preference study needs a 2026 primary source before any slide use | Research rerun | Before module 1 is built |
| 3 | Verify schedule and second-agent features with dated vendor docs | Stage 3 | Before module 3 is built |
| 4 | Instructor guide notes from the case (2 coding edge cases, 2 extra feedback items) | Module builder | Stage 3 |
| 5 | Recheck the platform matrix within 30 days of release | Researcher | Before release |
