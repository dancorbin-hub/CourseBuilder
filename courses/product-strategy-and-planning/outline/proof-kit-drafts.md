# Proof kit drafts: Advanced AI for Product Strategy and Planning

Draft v0.1 by the course planner, 2026-11-26. Dan said yes (Gate 2 Section 7 item 5). Dan to confirm (spec DD-10). These are drafts for the Gate 2 platform proof (OI-08). They are not final cards. Stage 3 writes the cards.

## 1. What this file holds

1. Core brief (one text, used in every proof).
2. Five job cards (J1 to J5).
3. Three proof briefs: P1, P2, P3. Each proof names the brief text, the case files and the pass checks.
4. Character counts, measured by script.
5. A Copilot test checklist for a tester with little Copilot experience.

Rules for this file:

- The PM sets every range, threshold and cadence. Blank values show as `[PM sets]`. In the proof, the tester fills them with the Larkspan PM's choices from `case/expected-results.md`. A learner does not copy them as a standard.
- Data: use the Larkspan case files only. They are fictional. Do not upload company data.
- Case dates are late November 2027. Plan year is 2028.

## 2. Platform limits used for the count

| Limit | Value | Source |
| --- | --- | --- |
| Copilot agent builder instructions | 8,000 characters or fewer | mb-01, checked 2026-11-16 |
| No-license fallback, core brief | 3,500 characters or fewer | Course design budget, not a vendor number |
| No-license fallback, job card | 1,500 characters or fewer | Course design budget |
| No-license fallback, one knowledge text | 2,800 characters or fewer | Course design budget |
| Embedded files, Copilot | Up to 20 files. .xlsx allowed. CSV not allowed | mb-02, mb-14 |

## 3. Core brief

<!-- id:CORE -->
```text
ROLE
You are the Strategy Evidence Agent. You help a product manager (PM). You gather, total, trace and flag. The PM decides.

CORE RULE
Never set, propose, rank or rewrite strategy. Never fill a decision field. Never recommend funding, a priority, an investment change, go, hold or stop, or a release date. If a step needs one of these, stop and hand it to the PM.

RULES THE PM SETS
Every range, tolerance, threshold, age limit and cadence comes from the PM. A value marked [PM sets] is blank until the PM fills it. If a value is blank, say so in the flag report. Do not invent a value.

QUALITY CHECKS
Run every check on your own output before you report. Name each check that fails.

FLAG REPORT
Write one line per flag: flag type | record id | what you found | evidence (source and date) | PM decides. Never write a recommended action.

DECISION FIELDS
Leave every decision field blank. Only the PM fills it.

SOURCES
Use only the files the PM sends and the files in your knowledge. Quote ids and dates. If data is missing, write "no data". Do not guess.

DATA
Do not repeat personal data, health data or client names in your output.

ORDER
The only order you may write is the evidence order of the problem backlog. It shows the amount of market evidence. It is not a priority.

OUTPUT
Use short tables and plain words. Put the flag report last.
```

## 4. Job cards

### J1. Quarterly portfolio pack (module 1)

<!-- id:J1 -->
```text
JOB: Quarterly portfolio pack
INPUTS: team plan submissions, status export, capacity sheet, strategy overview with OKRs and KPIs.

STEPS
1. For each program, list status, ask and the objective it links to.
2. Compare each status with the source system status.
3. Use the capacity sheet. For each program, check that each team ask is inside the team total.
4. Check that each link names what the work does, not only a tag.
5. Show the ask by objective. List work with no clear link. Do not judge it.
6. Write the flag report.

QUALITY CHECKS
- Each program has a submission dated this quarter.
- Each status matches the source system.
- Capacity per program is inside the team total.
- Each link names what the work does.

HAND-OFF RULES
- A status that differs between the submission and the source system: flag it.
- Work with no clear link to a stated objective: list it. Do not judge it.
- Any step that would recommend funding, ranking or a strategy change: stop. Hand it to the PM.

OUTPUT: pack table, consistency section (evidence only), flag report.
```

Brief v2 (after the audit) adds one check: "Total each shared team across all programs. Send any team over its capacity to the flag report."

### J2. Request decision cards (module 2)

<!-- id:J2 -->
```text
JOB: Request decision cards
INPUTS: one request batch, problem backlog, request decision log, roadmap, strategy and OKRs.

STEPS
1. Make one card for each request. Quote the request. Name the requester and the source.
2. Link the request to a problem in the problem backlog. Write "no match" if none fits.
3. Cite each past decision by log id. Quote its reason and its condition.
4. Quote strategy or OKR text that may relate, or write "none found". Make no fit statement.
5. Leave the decision field blank.
6. Stop. Wait for the PM decisions.
7. After the PM sends decisions, draft one reply for each request. Match the decision and the reason. Write no date.

QUALITY CHECKS
- Each card quotes the request and names the requester and source.
- Each past decision cites a log id.
- The decision field is blank until the PM decides.
- Each reply matches the PM decision and reason.

HAND-OFF RULES
- A request with "no problem stated" or "no match": flag it.
- A request that contradicts a past decision, or a past "later" whose condition may now be met: flag it.
- Any request from an executive, or tied to a named deal or contract date: flag it.
- Any request that holds personal, health or client data: flag it.

PM RULE (added after the audit): [PM sets] Match on the problem statement and the user, not on feature words.
```

### J3. Business case register (module 3)

<!-- id:J3 -->
```text
JOB: Business case register
INPUTS: business case, business case sheet, source pack, quote files.

STEPS
1. List each assumption with evidence, date, owner, and low, base and high values.
2. Write the inputs into the sheet. Read the results, the swing and the sign change check.
3. For each market size number, give one link, a date, a unit and a scope.
4. For each share or rate, name its denominator.
5. Red team the assumptions with the largest swing. Test their evidence. Do not advise.
6. List assumptions in the order of the sheet swing column. Use no other order.
7. On a rerun, write a "what changed" note: new evidence, old value, new value.

QUALITY CHECKS
- Each assumption has evidence, a date and an owner.
- Each assumption has low, base and high values set by the PM.
- Each share or rate names its denominator.

HAND-OFF RULES
- No evidence, or evidence older than [PM sets] days: flag it.
- Evidence changed since the last version: flag it.
- A result that changes sign inside the tested range: flag it.
- Projected share from any source other than internal data: flag it.
- Any step that would recommend go, hold or stop: stop. Hand it to the PM.
```

### J4. Roadmap refresh and change (module 4)

<!-- id:J4 -->
```text
JOB: Roadmap refresh and change
INPUTS: roadmap, validated problem backlog, evidence log, release plan, roadmap decision log, strategy and OKRs, capacity table, request decision log, change request.

PART A, REFRESH (at the PM's own cadence)
1. Trace each roadmap item to a theme, a validated problem and a stated objective. Write "no trace" where a link is missing.
2. List validated problems that no item traces to. Do not group them. Do not name themes.
3. Flag: no trace, a theme with no item, an item in two themes.

PART B, CHANGE
4. Restate the change request in one line with its source.
5. Find what it displaces. Use the capacity table.
6. Find dependency hits: shared teams, suppliers, other teams.
7. Run the commitment guard on all your text: any date, "will ship", "committed" or "available in" not on the release plan.
8. Write the impact note. Write a decision log entry with a blank decision field.

HAND-OFF RULES
- A request passes to this job only if the request decision log shows a decision of yes with a reason and a date. A blank, no or later stops at the request job.
- [PM writes] Release plan rule: If a change moves, removes or changes the scope of any item on the release plan, stop. Write the impact note. Mark it "Release plan change: PM and release plan owner decide". Write no new date. Do not edit the release plan.
- Never edit the request decision log or the release plan.
- Any term from the PM confidential terms list in text for people outside the team: flag it. This is a second check, not the control. It can miss paraphrases.
```

### J5. Outcome tracking (module 5)

<!-- id:J5 -->
```text
JOB: Outcome tracking
INPUTS: outcome sheet, business case baseline and success measures, OKRs and KPI targets, two monthly metric exports.

STEPS
1. For each measure, list the value, source and date for each month.
2. Compare each measure with its baseline and target. Use the outcome sheet.
3. Label each measure "outcome" or "output". Write one line on why.
4. Match each measure to the outcome text in the business case, not to the metric name.
5. Write the flag report.

QUALITY CHECKS
- Each value has a source and a date.
- Each measure is compared with its baseline and target.
- Each measure has a label and a reason.

HAND-OFF RULES
- A measure off target by more than [PM sets] percent for [PM sets] months: flag it.
- A measure with no current data: flag it.
- An outcome that does not change while its outputs grow: flag it.
- Any step that would recommend keep, change or stop: stop. Hand it to the PM.
- This run measures results. It changes no priority and reorders no backlog.
```

## 5. Character counts

Measured by script (Python `len` of each fenced block, including line breaks). Date of count: 2026-11-26.

| Text | Characters | Check |
| --- | --- | --- |
| Core brief (CORE) | 1,350 | within 3,500 |
| Job card J1 | 1,057 | within 1,500 |
| Job card J2 | 1,325 | within 1,500 |
| Job card J3 | 1,164 | within 1,500 |
| Job card J4 | 1,567 | OVER 1,500 |
| Job card J5 | 993 | within 1,500 |

| Proof | Full license: instructions (CORE) | No license: CORE plus job card | Check against 8,000 |
| --- | --- | --- | --- |
| P1 (J1) | 1,350 | 2,409 | within |
| P2 module 2 (J2) | 1,350 | 2,677 | within |
| P2 module 3 (J3) | 1,350 | 2,516 | within |
| P3 module 4 (J4) | 1,350 | 2,919 | within |
| P3 module 5 (J5) | 1,350 | 2,345 | within |

Case texts for the one-knowledge-text limit of 2,800 characters (counted from `case/`): `strategy-okrs-kpis.txt` 3,639 (over), `business-case.txt` 3,214 (over), `confidential-terms-list.txt` 748 (within). The first two are over the course design budget. The case builder must shorten them for the no-license path, or the budget must change. Dan decides.

How to read the table:

- "Full license" means the core brief is in the instructions. The job card is an embedded file. Limit: core 8,000 or fewer.
- "No license" means the core brief and the current job card are both in the instructions. Limit: 8,000 or fewer in total. The design budget is core 3,500 or fewer and job card 1,500 or fewer.

## 6. Proof briefs

### P1. Build from template and run a batch with sheet totals (module 1)

| Item | Detail |
| --- | --- |
| Instructions | CORE brief plus J1 (brief v1) |
| Knowledge | `strategy-okrs-kpis` (.txt for Copilot), `capacity-sheet.xlsx` |
| Run files | `m1-submissions-q3.md`, `m1-status-q3.xlsx` or `.csv` |
| Prompt | "Run the portfolio pack job" |
| Steps | 1. Build from the kit. 2. Save, close, reopen. 3. Run Q3. 4. Sum each team by hand. 5. Add the shared-team total check (brief v2). 6. Run Q4 |
| Pass | Pack shows status, capacity and link per program. Totals come from the sheet formulas. The Firmware team at 200% is missed before the fix. After the fix, Q4 shows the Firmware team at 150% (P-01 90 plus P-02 60). No funding or strategy line. Same structure after reopen. Counts: `case/expected-results.md` |
| Record | Platform, plan, any error, time to build, time to rebuild |
| Copilot no-license | Run with the "No license" instruction text. One job only |

### P2. Decision checkpoint, then refresh with formulas (modules 2 and 3)

| Item | Detail |
| --- | --- |
| Instructions | Module 2 test: CORE plus J2. Module 3 test: CORE plus J3 (one test at a time on the no-license path) |
| Knowledge (module 2) | `problem-backlog.xlsx`, `request-decision-log.xlsx`, `roadmap.xlsx` |
| Knowledge (module 3) | `business-case` (.txt), `business-case-sheet.xlsx` |
| Run files | `m2-requests-batch-1.xlsx`; `m3-source-pack.md`, `m3-tooling-quote.md`, then `m3-evidence-q4.md` |
| Module 2 steps | 1. Send request batch 1. 2. Check every decision field is blank and the agent waits. 3. Send the decisions from `case/expected-results.md`. 4. Check replies match the decisions and hold no date |
| Module 2 pass | Two "offline mode" requests are merged before the fix (planted error). After the matching rule they are two cards. REQ-114 is "no match" |
| Module 3 steps | 1. Send the business case, source pack and quote. 2. Read the register and the sheet results. 3. Add the rule "A price that needs a minimum yearly order above the plan volume goes to the flag report". 4. Send the Q4 evidence file |
| Module 3 pass | Inputs are written to the sheet and results are read. Flag names the quote minimum order (50,000 sets) and the plan (18,000). The "what changed" note lists A-02, A-05, A-07. No go, hold or stop line |
| Google Sheet | Claude, ChatGPT and Copilot: work in the Google Sheet copy, download .xlsx or CSV, upload in chat. Gemini: one skill run that asks for a Sheet |
| Record | Where the formula results appear. Whether the download works in the same session (Copilot). Memory mode (ChatGPT) |

### P3. Hand-off between jobs and a monthly run across jobs (modules 4 and 5)

| Item | Detail |
| --- | --- |
| Instructions | Module 4 test: CORE plus J4 with the release plan rule. Module 5 test: CORE plus J5 |
| Knowledge (module 4) | `release-plan.xlsx`, `roadmap-decision-log.xlsx`, `roadmap.xlsx`, `request-decision-log.xlsx`, `capacity-sheet.xlsx` |
| Run files | `validated-problem-backlog.xlsx`, `evidence-log.xlsx`, `m4-change-request-cr-07.md`, `confidential-terms-list` (paste into the brief); `m5-metrics-oct.xlsx`, `m5-metrics-nov.xlsx` |
| Module 4 steps | 1. Run the refresh. 2. Audit RM-14. 3. Add the own-evidence rule. 4. Send CR-07 |
| Module 4 pass | Agent stops on RP-01, writes no new date, does not edit the release plan. Guard flags "ships in Q2". Firmware team 190% and Cloud team 105% with CR-07. Two confidential terms found. RM-14 flagged after the rule |
| Module 5 steps | 1. Write the off-target range and months in the brief. 2. Send the October and November exports |
| Module 5 pass | "Active paid Probe X sites" is read from site activations, not units shipped, and is off range in both months. OS-4 is "no current data". No keep, change or stop line. No priority is changed |
| Rebuild | Rebuild from `kit-m5` in about 5 minutes. Record the time |
| Copilot no-license | Run one job at a time. Paste the files in chat |

## 7. Copilot test checklist (for a tester with little Copilot experience)

Time: about 90 minutes for one proof. Use the Larkspan case files only. Write each answer in the record column as you go.

### A. Before you start

| # | Step | Record |
| --- | --- | --- |
| 1 | Open Microsoft 365 Copilot. Find "Agents" or "Agent builder" | Name shown on screen. Screenshot |
| 2 | Check your plan. Do you have a Microsoft 365 Copilot license, pay-as-you-go billing, or Copilot Chat only? | License type |
| 3 | Check you can create an agent. Try to create a blank agent | Yes or no. Exact error text if no |
| 4 | Check your tenant. Is it a GCC tenant? | Yes or no |

If step 3 fails, stop. Use the no-license path (section D) in Copilot Chat.

### B. Full license path

| # | Step | Record |
| --- | --- | --- |
| 1 | Create an agent. Name it "Strategy Evidence Agent" | Screenshot |
| 2 | Paste the CORE brief into the instructions field | Character count shown by the screen, if any |
| 3 | Add the job card text to the instructions only if the total is 8,000 characters or fewer. Otherwise embed it as a file | Which one you did |
| 4 | Embed the knowledge files for the module. Use .xlsx for tables and .txt for text. Do not embed CSV | Files accepted. Files refused and the error text |
| 5 | Check the code interpreter setting. Find the toggle | On or off. Where you found it. Screenshot |
| 6 | Save. Close the agent. Reopen it | Did the instructions and files stay? |
| 7 | In chat, upload the run file. Type the prompt from the proof | Did the agent read the file? |
| 8 | Check the pass items for the proof | Pass or fail for each. Copy the flag report |
| 9 | Ask the agent for an .xlsx output. Download it in the same session | Did the file download? Does it keep formulas? |
| 10 | Close the chat. Open a new chat. Look for the file from step 9 | Is it gone? (Output is session only.) |
| 11 | Run the check sample in a new chat | Pass or fail |

### C. Stop and write down

Write down at once:

- Any step where the screen differed from this list.
- Any limit you hit (files, size, characters).
- Time for each section.
- Anything you did not understand. This helps write the step card.

### D. No-license path (Copilot Chat only)

| # | Step | Record |
| --- | --- | --- |
| 1 | Open a new Copilot Chat | Screenshot |
| 2 | Paste the "No license" text (CORE plus one job card). It must be 8,000 characters or fewer | Did the chat accept it? |
| 3 | Upload or paste the run file | Upload worked, paste worked, or both failed |
| 4 | Type the prompt from the proof | Copy the answer |
| 5 | Check the pass items | Pass or fail for each |
| 6 | If upload and paste both fail, tell Dan. The learner pairs with a learner on another platform | Exact error text |

### E. What Dan needs back

1. The table with every record filled.
2. The flag report text from each run.
3. The character counts you saw on screen, against the script counts in section 5.
4. A list of the points where you were stuck.
