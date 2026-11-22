# Gate 2 packet: Advanced AI for Market Research

- Course id: `market-research`. For Dan. Written 2026-11-22.
- Reading time: about 20 minutes. The platform proof (section 6) is hands-on work for you. It takes longer.
- Files under review: `spec.yaml` (v0.2), `outline/development-brief.md` (v0.2), `outline/syllabus.md`, `case/` (Larkspan Systems).
- Gate 2 is approved only when you change `gate_2_spec` in `status.yaml`. Then Pragmatic reviews the syllabus.

## 1. Summary

1. **The course.** One day, 5 modules, 360 teaching minutes, 41% instructor-led. Two half days split after module 2.
2. **The agent.** One Market Evidence Agent. Built in module 1 from a template. One new job per module. Five jobs at the end.
3. **The ladder.** Hand-run batch (modules 1, 2). Recurring run (module 3). Hand-off between jobs (modules 4, 5). Agent that faces stakeholders (module 5).
4. **The case.** Larkspan Systems: hardware sensors plus SaaS, with an internal platform PM. One planted error per lab. The warning fades: told, hint, hint, hint, none.
5. **The critic** found 7 must-fix items. The planner and the case builder fixed all 7. Two of the fixes need your yes (decisions 1 and 3).
6. **What blocks the lock.** 11 decisions below, and the platform proof. Copilot file types, Copilot and Gemini chat limits and the Copilot no-license path are not verified yet.
7. **I found 3 small case file problems** while I wrote this packet (section 8, items 1 to 3). The case builder fixes them after your decisions.

## 2. Decisions for Dan

Each decision has options and my recommendation. Reply with the number and your choice, for example "2: A".

### Decision 1. Pattern wording (OI-13)

The critic found that the case let the agent write "Pattern". Your Gate 1 answer (PA-01) says the agent never labels a pattern.

| Option | What it means |
| --- | --- |
| A | The agent writes "meets the PM's bar", "emerging" or "single source". Only the PM promotes an insight to "pattern". Only the PM calls a problem "validated" |
| B | The agent may write "pattern" when the evidence meets the bar the PM wrote in the brief |

**Recommendation: A.** It matches your Gate 1 words. It also gives every lab a clear manager action: the PM promotes. The case files already use A.

### Decision 2. Template content and the lab 1 planted error (OI-14)

The approved worked example row (v3) puts "count interviews, not quotes" in the template. v0.1 left it out so learners would add it. v0.2 puts it back. The PM's bar stays blank. The planted error now depends on the blank bar: with no bar, the agent ranks one vocal buyer (3 quotes, 1 interview) near the top.

Risk: with the count rule in the template, a strong model may label that insight correctly. Then the lab 1 error does not show.

| Option | What it means |
| --- | --- |
| A | Keep v3. Count rule in the template, bar blank. Proof P1 tests that the error shows on all 4 platforms |
| B | Remove the count rule from the template (v0.1). The error shows more often. This changes the approved v3 row |
| C | A, and if the error does not show on a platform, the debrief uses the instructor's demo run (as `case/planted-errors.md` already says) |

**Recommendation: C.** Keep your approved v3 row. Let P1 tell us if the error shows. Change to B only if P1 fails on 2 or more platforms. Note: `case/planted-errors.md` lab 1 still says "the template has no count rule". It must match your choice (section 8, item 2).

### Decision 3. Segment rule: course rule or case choice (OI-15)

The rule: a claim about one segment (for example "food service buyers want") needs the PM's bar met inside that segment. The critic found the lab 5 results broke it. The fix puts it in the lab 1 template, the lab 5 hand-off rules and the lab 5 status proposals.

| Option | What it means |
| --- | --- |
| A | Course rule. Every learner's agent checks it. The template has the hand-off rule |
| B | Case choice only. The Larkspan Head of Product chose it. Learners decide on their own work |

**Recommendation: A.** It is a logic rule, not a number. It does not set the bar. It says where the bar applies. This keeps "no magic number" intact. With B, a learner can let an agent say "food service buyers want" from 1 food service interview.

### Decision 4. The example case PM bar

Learners on the case path need a bar to get the expected results. `case/company.md` shows "the Larkspan Head of Product's bar for this study". It says it is one PM's choice, not a rule.

| Item | Case value |
| --- | --- |
| Meets the PM's bar | 3 or more interviews (not quotes), from 2 or more accounts, with 1 or more PM-held interview |
| Emerging | 2 interviews, or 3 or more with no PM-held interview |
| Single source | 1 interview, however many quotes |
| Win/loss | 3 or more interviewed deals in a segment |
| Weekly feedback | A change of 3 or more accounts |
| Stakeholder answers | Age limit 18 months |

| Option | What it means |
| --- | --- |
| A | Approve these values as the case example |
| B | Change one or more values. The case builder recounts the expected results |

**Recommendation: A.** The values produce every planted error and every expected result. The risk is that learners copy the numbers as a rule. The controls: the "one PM's choice" text, the module 1 debrief with your test ("can you predict that the next buyer of this persona will raise it?") and learners write their own bar.

### Decision 5. Bond story (OI-01)

You said "hold off" at Gate 1. The slot is 5 minutes in the course open. You must pick before module 1 is built (Stage 3). It does not block Gate 2.

**Recommendation: candidate 1 (JAMIA 2026, AI quotes in health interviews).** It is a 2026 primary source. It names the exact error that lab 1 teaches learners to catch. If you pick candidate 2 (Pew), the synthetic respondent caution in module 1 must move, so the Pew finding is shown once.

### Decision 6. Your own example for module 4 vs decision 43 (OI-05)

At Gate 1 (item f) you offered one real example for the alternatives map from win/loss deals. Decision 43 says stories are never told as the instructor's own experience. Will or another instructor may deliver this course.

| Option | What it means |
| --- | --- |
| A | Script it as a story from Pragmatic's work with companies, or from an unnamed client team |
| B | Script it as your own experience. This breaks decision 43 |

**Recommendation: A.** Remove names and details that identify the company. Any instructor can then tell it. Send me the example before module 4 is built.

### Decision 7. Capability and skill names (OI-11)

The Capability Standards Workbook is not available. The development brief says **Dan to name** for the capability and each skill. The syllabus says the same. Working descriptions are placeholders only.

**Recommendation:**

1. Name the capability and the five skills, or give me the workbook and I map them.
2. Confirm offering intent **Develop and Apply** for all five modules.
3. Confirm the learner evidence list with the ID team (decision 29). They score it in beta.

Pragmatic sees "Dan to name" in the syllabus if this is not done before their review.

### Decision 8. Module 4 is 55 minutes (OI-17)

The PRD says about 60 to 90 minutes per module. Module 4 is 55 minutes (22 instructor-led, 33 hands-on, lab 25). More time breaks the 7.5-hour day unless another module gives time.

| Option | What it means |
| --- | --- |
| A | Accept 55 minutes |
| B | Move 5 minutes from module 2 (70 to 65). Module 4 becomes 60 |

**Recommendation: A, with a check.** Module 4 has the fewest files (4) and one evidence pack. Time your P3 run of the map job. If build, run and audit take you more than 15 minutes, choose B.

### Decision 9. Internal PM is not used in any lab (OI-18)

Internal PM is a priority context. The case has an internal PM (Fleet Data Platform). No lab uses it.

| Option | What it means |
| --- | --- |
| A | Talk track only. Module 3 uses the internal platform example (W18) |
| B | Add one internal PM item to the case. For example, a lab 5 question from the FDP PM, answered from the insight log (install and connectivity) |
| C | A and B |

**Recommendation: C.** One lab 5 question shows that an internal PM uses the same evidence. It changes no planted error and no lab 1 to 4 count. The case builder adds it before Gate 2 locks the records. The critic checks it again.

### Decision 10. Rung 2 and rung 3 scope (OI-02, OI-03)

The PRD ladder says "an agent on a schedule" and "agents that hand work to other agents" (decision 35). The spec does this:

| Rung | Spec scope | Why |
| --- | --- | --- |
| 2 | A hand-started run on week 2. The PM reads only the flag report and a sample. A schedule or file trigger is a stretch step | No schedule feature is verified on all 4 platforms. A schedule with no new input does nothing in a lab with no connectors |
| 3 | A hand-off between jobs inside the one course agent. A second agent is a stretch step | House rule 12 says one agent per course. Second agents are not verified on all 4 platforms |

**Recommendation: accept both.** The manager skill is the same: read flags, not items, and write the hand-off rule. Say it plainly on the module 3 and 4 slides. Recheck the platform matrix in Stage 3. If a schedule feature works on all 4 platforms, move it to the core path.

### Decision 11. Screening as a lab 1 stretch (OI-04)

Row 05 (screen study applicants) folds into module 1. It is a stretch step, not a core step, so the step card stays at 6 steps.

**Recommendation: accept.** The case has the stretch file (`m1-stretch-applicants.md`). Its expected results need one cleanup (section 8, item 1).

### Quick yes or no

| # | Item | Recommendation |
| --- | --- | --- |
| 12 | OI-07. Half days are 3 hours 10 minutes and 3 hours 45 minutes | Accept. Day 2 has the most build work. If you want balance, move the module 5 debrief time only, not the lab |
| 13 | OI-06. `research/workflows.yaml` row 01 has the old "2 or more interviews" rule. The spec follows v3. The file is fingerprinted | Yes to fix row 01 to match v3. It stops later agents from reading the old rule |
| 14 | Syllabus line: Copilot Chat users with no license "use a reduced path that runs one job at a time" | Keep it if P1 to P3 pass for the fallback. If not, change it to "need a license or pay-as-you-go billing" before Pragmatic sees it |

## 3. Module plan

| Module | Workflow row | Minutes (led / hands-on) | Rung | Planted error and warning | Learner evidence | How the agent grows |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Run your first batch and manage it by flags | mr-wf-01 (folds 05) | 70 (28 / 42) | 1. Hand-run batch | One vocal buyer (3 quotes, 1 interview) looks like strong evidence. **Told** | Tuned brief v1 to v2 (bar plus one rule). Flag decisions, batch 1. Audit of 3 insights | Built from template. Insight log job, code book, flag report |
| 2. Win/loss and the match rate | mr-wf-02 | 70 (28 / 42) | 1. Hand-run batch, two sources | CRM-only "price" leaks into buyer drivers. **Hint** | Match rate table and one-sentence read. Flag decisions. Audit of 2 deals. Brief change | Win/loss job, driver code book, driver log |
| 3. The weekly run | mr-wf-03 (folds 04) | 60 (24 / 36) | 2. Recurring run | Forced fit hides a new problem (4 accounts). **Hint** | Flag decisions, week 2. Audit of 10 items and the "no fit" group. "No fit" rule | Weekly feedback job, tag list. Writes to the module 1 insight log |
| 4. First hand-off: the alternatives map | mr-wf-10 | 55 (22 / 33) | 3. Hand-off between jobs | CRM says Rimecore; the buyer kept the spreadsheet (D-3108). **Hint** | Hand-off rule as written and as fixed. Audit of 3 traced entries. Alternative to beat in one segment | Alternatives map job. Reads the driver log and insight log |
| 5. The agent answers stakeholders | mr-wf-09 (folds 07) | 65 (26 / 39) | 3 plus. Faces other people | 2-year-old study for another segment shown as "buyers want". **None** | Send, change or hold for 3 answers. Audit of one cited answer. Hand-off rules. Validated-status decisions | Stakeholder answer job with status proposals by segment. Five jobs |

Course open 25 minutes, close 15 minutes. Total 360 teaching minutes. Instructor-led 148 of 360 (41%).

## 4. Development brief summary

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Dan to name** (decision 7). Category: Market. Focus areas: Market Problems, Win/Loss Analysis, Competitive Landscape |
| 2. What the learner can do | Build one agent from a template. Write and tune its brief. Set checks and hand-off rules. Decide flags. Audit samples. Connect jobs. Set the evidence bar |
| 3. How far | Develop and Apply, all five modules. Workshops Introduce. Validate stays with the ID team |
| 4. Evidence | Per lab: tuned brief, flag report decisions, audit findings. Plus the match rate table, the hand-off rule and the send, change or hold decisions. End: saved agent with five jobs and a Monday plan |
| 5. Experience | One agent that grows each module. Autonomy ladder. 40/60 split. Own work first. Four step cards per lab. Breakout rooms by platform. Catch-up kit per module |

Not taught here (known from workshops): one-pass synthesis and the quote check (PDW-AI), persona creation (BPW-AI), public competitor watching and scheduled-task setup (CAW-AI), first teaching of boundaries (AI Agents course), prompt structure (PRW-AI). Market sizing and concept tests moved to the Strategy course.

## 5. Fallback case and locked records

**Larkspan Systems** (fictional). Wireless temperature sensors (hardware) plus cloud software. About 420 employees. Segments: Distribution, Food service, Pharmacy and lab. External PMs own Probe, Hub, Tag and Cloud. An internal PM owns the Fleet Data Platform. Not a copy of BadgeWorks, Entrilo or FieldPro.

Gate 2 locks these records and the results they support (`case/expected-results.md`).

| Lab | Records | Planted error location | Locked result (after the fix) |
| --- | --- | --- | --- |
| 1 | `m1-code-book`, `m1-interviews-batch-1`, `m1-interviews-batch-2`, `m1-check-sample`. Stretch: `m1-stretch-applicants` | I-104 (P05, 3 quotes) | P05 is "single source", then "emerging" after batch 2. P06 contradiction is flagged. The agent writes "pattern" nowhere |
| 2 | `m2-driver-code-book`, `m2-crm-export-q2.csv` (14 decided deals), `m2-winloss-notes-q2`, `m2-check-sample` | WL-2214 (no-show), D-2204, D-2210 | Match rate counts the 9 interviewed deals only. No CRM-only deal in buyer findings. 5 mismatched deals flagged |
| 3 | `m3-tag-list`, `m3-feedback-week-1.csv` (24), `m3-feedback-week-2.csv` (32), `m3-check-sample`. Stretch: `m3-stretch-survey-wave.csv` | F-1215 to F-1219 | New problem (remote inspector access, 4 accounts) in "no fit" and flagged. P02 stays at 3 accounts. P01 shows 7 accounts, not 11. F-1221 (personal data) flagged |
| 4 | `m4-alternatives-map`, `m4-evidence-pack`, `m4-check-sample` | D-3108 | D-3108 moves to "do nothing". Rimecore 2 in Q2, 2 in Q3, no change. Do nothing is the top alternative in Food service |
| 5 | `m5-past-reports` (R-2024-07 is 2024, Food service), `m5-stakeholder-questions` (Q4 is the check) | R-2024-07, asked by Q2 | Answer names the date and segment of every source. R-2024-07 flagged. No "buyers want". Status proposals by segment |

Each knowledge file has a `.txt` copy for Copilot. The agent ends with 12 knowledge files (budget 13).

## 6. Platform proof plan (Dan runs these)

Decision 27: you build, save and rerun each build pattern on all four platforms. Use the case data. Use your own accounts. Record pass or fail in the Result column, then send me the results.

Before you start:

1. Have one Claude, one ChatGPT (Go or Plus), one Copilot (licensed) and one Gemini account ready.
2. For Copilot, also have one account with Copilot Chat only (no license, no billing).
3. For Gemini, test on a Workspace account and a personal account.
4. Record your hours with `activity=gate-2-proof` in `logs/hours-log.csv`.

### Pattern P1. Build from the template and run a batch with file output (modules 1, 2)

| Platform | Build | Save and reopen | Rerun test and pass condition | Result |
| --- | --- | --- | --- | --- |
| Claude | New Project "Market Evidence Agent". Paste the kit-m1-template brief into instructions. Add the code book and the empty insight log to knowledge. Check code execution and file creation are on | Saves as you go. Close the Project. Reopen it | Send batch 1 with "Run the insight log job". Pass: insight log as a downloadable file, a flag report, P05 looks strong (the error shows). Reopen and run again: same structure | |
| ChatGPT | New Project. Paste the brief into instructions. Add the code book and the empty insight log to project files | Saves as you go. Close and reopen | Same test as Claude | |
| Copilot | New agent in agent builder. Paste the core brief into instructions (under 8,000 characters). Embed the `.txt` copies of the code book and insight log | Select Create, then Update. Close and reopen | Same test. Also try the `.md` file as knowledge (G2-PF-01). Then on the Chat-only account: m1 and m2 fallback instructions, batch files in chat (G2-PF-02) | |
| Gemini | New Gemini skill. Paste the brief. Upload the code book and the empty insight log | Select Save. Close and reopen | Same test, on Workspace and personal accounts. Count files that the skill and the chat accept (G2-PF-04) | |

### Pattern P2. Extend the agent and rerun with the prior log (module 3)

| Platform | Build | Save and reopen | Rerun test and pass condition | Result |
| --- | --- | --- | --- | --- |
| Claude | Add the weekly feedback job card and the tag list to the P1 Project | Saves as you go. Use the log save card: replace the insight log in knowledge | Send week 1, then week 2. Pass: "what moved" compares the 2 weeks, counts by unique account, the forced-fit error shows. Add the "no fit" rule and rerun week 2: the new problem shows. A new chat reads the saved log | |
| ChatGPT | Add the job card and tag list to project files | Replace the log in project files | Same test | |
| Copilot | Embed the job card and the `.txt` tag list. Check the core instructions stay under 8,000 characters | Replace the embedded log. Select Update | Same test. On the Chat-only account: m3 fallback with the insight log pasted in chat | |
| Gemini | Add the job card and tag list to the skill | Re-upload the whole skill with the new log. Time it: it must fit the debrief (G2-PF-04) | Same test | |

### Pattern P3. Hand-off between jobs and a cited answer (modules 4, 5)

| Platform | Build | Save and reopen | Rerun test and pass condition | Result |
| --- | --- | --- | --- | --- |
| Claude | Delete the P2 Project. Rebuild from kit-m5 and time it (target about 5 minutes). Add the map job card, the map, the answer job card and the past reports | Saves as you go. Close and reopen | Run win/loss, then the map job on its output, then the answer job. Pass: each map entry links to a deal or interview id; the D-3108 error and the R-2024-07 error both show; the answer cites date and segment and has a "what we do not know" line. Time the map job run and audit (decision 8) | |
| ChatGPT | Same rebuild from kit-m5 | Close and reopen | Same test | |
| Copilot | Same rebuild, `.txt` files | Select Update. Close and reopen | Same test. On the Chat-only account: m4 and m5 fallback, one job at a time. Paste `m4-evidence-pack.md` (about 12,400 characters) in one message (G2-PF-03) | |
| Gemini | Same rebuild | Select Save. Close and reopen | Same test | |

### Proof items (facts to find, not guess)

| Id | Platform | Check | Need to pass | If it fails |
| --- | --- | --- | --- | --- |
| G2-PF-01 | Copilot | Embedded knowledge takes the `.txt` copies. Is `.md` accepted? Find a dated vendor doc | `.txt` works | Ship `.docx` copies |
| G2-PF-02 | Copilot | Chat upload: files per message, `.csv` and `.md`, unlicensed upload | 3 files in chat in one lab; `.csv` run files | Paste as text. Add `.xlsx` copies of each CSV |
| G2-PF-03 | Copilot | Longest message in chat | 12,400 characters (evidence pack) | Kit splits the pack in 2 parts. Last resort: pair with a learner on another platform |
| G2-PF-04 | Gemini | Chat upload limits, files per skill, skill re-upload time | 3 files in chat; 3 added in lab 1; 12 in the skill at the end | Paste as text. Keep logs in chat |
| G2-PF-05 | Copilot | Fallback text per module: core brief plus one job card plus one knowledge file | Under 8,000 characters for each kit | Keep only the core brief in instructions; paste the rest in chat |

Gate 2 passes the proof when each pattern passes on each platform, or a failure has a tested fallback that you accept.

## 7. What the critic found and what changed

The critic checked v0.1. The planner made one revision (v0.2). The case builder fixed the case files first.

| Id | Finding | What changed, or why not |
| --- | --- | --- |
| M1 | CSV notice line breaks plain import | Fixed in case. Notice moved to `case/README.md` |
| M2 | Case bar visible to the instructor only | Fixed in case. Bar is in `company.md` as the Head of Product's choice |
| M3 | Lab 5 proposals contradict the case bar | Fixed. Proposals by segment. New segment rule. Needs your yes (decision 3) |
| M4 | Agent wrote "Pattern", against PA-01 | Fixed. Agent writes "meets the PM's bar" at most. Needs your yes (decision 1) |
| M5 | Copilot does not list `.md` | Fixed. `.txt` copies shipped. Proof G2-PF-01 |
| M6 | Copilot no-license path fails after module 2 | Fixed on paper. One job at a time, under 8,000 characters. Not verified: P1 to P3 and G2-PF-02, 03, 05 |
| M7 | Lunch 45 minutes, not 60 | Fixed. Lunch 60. Module 1 from 80 to 70, module 5 from 70 to 65 |
| S1 | One case line made a fixed rule | Fixed in case. Your test is in the module 1 debrief |
| S2 | Success checks named the planted error | Fixed. General success check before the lab. Error check in the debrief only |
| S3 | File counts and log save not defined | Fixed. Per-lab counts, a 2-step log save card, proof items for limits |
| S4 | Spec case section out of date | Fixed. Names Larkspan and lists the files |
| S5 | Card steps with 2 actions | Fixed. 6 steps, 1 action each. Rerun moved to the debrief |
| S6 | One ambiguous lab 3 check item | Fixed in case |
| S7 | Template differs from approved v3 | Fixed. Count rule back in. Needs your yes (decision 2) |
| S8 | Wrong edge reasons in the lab 1 stretch | Fixed in the main table. A stale copy is still in the file (section 8, item 1) |
| N1 | Module 4 is 55 minutes | Not changed. More time breaks the day. Decision 8 |
| N2 | Minimum of 10 deals: decided or interviewed? | Fixed. Counts decided deals |
| N3 | Three tests taught in PDW-AI | Fixed. Referred to as known. No new slide |
| N4 | Internal PM not in any lab | Not changed yet. Decision 9 |
| N5, N6 | Case notes for the instructor | Not changed. Instructor guide notes in Stage 3 (OI-19) |
| N7 | Larkspan close to FieldPro? | No action. The critic agrees it is not a copy |

## 8. Open items

| # | Item | Owner | Due |
| --- | --- | --- | --- |
| 1 | `case/expected-results.md` lines 103 to 107 hold a stale copy of the stretch table with the old wrong reasons (S8). Remove it | Case builder | Before the lock |
| 2 | `case/planted-errors.md` lab 1 says "the template has no count rule". This does not match spec v0.2. Update it after decision 2 | Case builder | Before the lock |
| 3 | `case/expected-results.md` labels its pass conditions "spec success check". The spec now splits success check and debrief check. Relabel them "debrief check" | Case builder | Before the lock |
| 4 | Bond story pick (decision 5) | Dan | Before module 1 is built |
| 5 | Your module 4 example (decision 6) | Dan | Before module 4 is built |
| 6 | Therapy preference study needs a 2026 primary source before any slide use (OI-08) | Research rerun | Before module 1 is built |
| 7 | Tell the PDW-AI owner about the AI-moderated interview rules (OI-09, Gate 1 follow-up) | Dan | Before Pragmatic review |
| 8 | Tell Pragmatic that MKT slide 7 uses old Framework names (OI-10, Gate 1 follow-up) | Dan | Before Pragmatic review |
| 9 | Case notes for the instructor guide (OI-19) | Module builder | Stage 3 |
| 10 | Recheck the platform matrix within 30 days of release (checked 2026-11-20) | Researcher | Before release |
