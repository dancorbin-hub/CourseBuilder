# Rework brief 2 (Gate 2 comments, 2026-11-22)

Source: Dan's Gate 2 doc comments and `outline/gate-2-decisions.md`. Both the planner and the case builder follow this brief. The planner owns `spec.yaml`, `outline/development-brief.md` and `outline/syllabus.md`. The case builder owns `case/`.

## 1. Replace the PM's bar with a problem backlog (Dan, decision 4)

Dan does not accept a fixed bar. Priority is relative: each problem is judged against the other problems in the backlog. The workbook supports this (skill 1.1D, skill 3.3 "prioritized problem backlog").

New model:

1. The agent keeps a **problem backlog** (rename "insight log" to "problem backlog" everywhere; keep file names short, for example `problem-backlog`).
2. Each problem has an **evidence profile**, reported as facts:
   - interviews (count interviews, not quotes), accounts, segments, personas
   - source type: PM-held, AI-moderated, win/loss, feedback item, past report
   - urgency (with one quote), pervasiveness (how many accounts and segments), willingness to pay clues. These are the Pragmatic terms from skill 1.1D. They replace "intensity", "frequency" and "impact" in learner-facing text.
   - source dates
3. Fact labels only: **single source** (1 interview, however many quotes) and **AI-moderated only** and **one segment only**. These are facts, not verdicts. Single-source problems stay in the backlog for trend tracking.
4. Remove "meets the PM's bar", "emerging" as a status, and the case bar table. Remove any number that acts as a threshold for calling something real.
5. The agent **proposes a ranking with reasons**. The PM decides the order, what is a pattern, and what goes to validation. The agent never writes "pattern" or "validated".
6. Segment rule (decision 3, provisional A): the agent ranks within a segment before it makes any claim about that segment. It never says "<segment> buyers want" from one interview in that segment.
7. Lab 1 planted error: the agent ranks the one vocal buyer (I-104, P05, 3 quotes, 1 interview) near the top. The learner catches it by reading the evidence profile (1.1B noisy 20%). Keep "count interviews, not quotes" in the template (decision 2, provisional C).
8. Module 5 "status proposals" become "ranking and validation proposals by segment". The PM decides.
9. Other bars in the case (win/loss 3 deals, feedback change of 3 accounts, 18-month age limit): keep only what a PM writes as a hand-off rule, framed as the case PM's choice for that rule, not a truth bar. The age limit is a hand-off rule (old evidence goes to the flag report). Win/loss and feedback: report counts and changes; the agent flags; no pass or fail threshold.
10. Recount every expected result in `case/expected-results.md` and `case/planted-errors.md` under the new model.

## 2. Timing (Dan, decision 12)

- Full day unchanged: 09:00 to 16:30, 60-minute lunch, 360 teaching minutes.
- Half days: each 09:00 to 12:30, one 15-minute break, 195 teaching minutes.
  - Day 1: open 25, module 1 80, break 15, module 2 75, day close 15.
  - Day 2: open 10, module 3 60, module 4 55, break 15, module 5 60, course close 10.
- Remove the syllabus line about cutting lunch to 45 minutes.

## 3. Other decisions to apply

- Decision 6 (final): Dan's module 4 example is a Pragmatic or unnamed client story.
- Decision 8 (final): module 4 stays 55 minutes. Drop the P3 15-minute timing check.
- Decision 9 (final, C): module 3 talk track uses the internal platform example. Case builder adds one lab 5 stakeholder question from the Fleet Data Platform (internal) PM, answered from the problem backlog. It must change no planted error and no lab 1 to 4 count.
- Decision 10 (final): core path the same on all 4 platforms. Schedule and second-agent stretch steps only on step cards where verified (likely Claude and ChatGPT; verify in Stage 3). Copilot and Gemini cards stay on core and say the stretch is not available there in this course. Out of scope at launch: Copilot Studio, Power Automate, Google Antigravity. Module 3 and 4 slides name the gap once.

## 4. Capability Standards (decision 7, proposal)

Use `outline/capability-mapping.md`. Replace "Dan to name" with the proposed capability and skills, marked "proposed, Dan to confirm". Use workbook names exactly. Do not invent skills or competencies.

## Rules

ASD-STE100. No em or en dashes. Tables and numbered lists. Fictional case data only. Do not edit files the other agent owns. Do not use the network shared folder.
