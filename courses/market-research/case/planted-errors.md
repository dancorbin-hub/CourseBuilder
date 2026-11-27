**Fictional data for training.** Larkspan Systems case. Instructor only. Do not give this file to learners.

# Planted AI errors, by lab

Each lab has one planted error in the case data (house rule 13). The warning fades: told in lab 1, a hint in labs 2 to 4, no hint in lab 5.

Important: the data makes each error likely and findable. It cannot force a model to make it. Gate 2 proof patterns P1 to P3 must confirm that each error shows up on all four platforms. If a platform does not make the error, the debrief shows the error from the instructor's demo run.

## Summary

| Lab | Warning | Error | Where it is | Check that passes anyway | What finds it |
| --- | --- | --- | --- | --- | --- |
| 1 | Told | One vocal buyer ranked near the top of the problem backlog | `m1-interviews-batch-1.md`, interview I-104 (P05) | Quote check (all 3 quotes are word for word) | Reading the evidence profile of the top-ranked problems: P05 has 1 interview, 1 account. All 3 quotes trace to I-104 |
| 2 | Hint | CRM-only "price" leaks into buyer findings | `m2-winloss-notes-q2.md`, entry WL-2214 (no-show). Also CRM-only deals D-2204, D-2210 in `m2-crm-export-q2.csv` | Quote check (passes on deals with interviews) | Audit of the deal source column |
| 3 | Hint | Forced fit hides a new problem | `m3-feedback-week-2.csv`, items F-1215 to F-1219 | Reason check (items share words with tag P02) | Audit of 10 random items and the "no fit" group |
| 4 | Hint | CRM competitor trusted where the buyer did nothing | `m4-evidence-pack.md`, deal D-3108 (Parts 1, 2 and 3) | Link check (entry has a deal ID and interview ID) | Audit of map entries against the interview |
| 5 | None | Old research for another segment presented as current | `m5-past-reports.md`, report R-2025-07, asked by Q2 in `m5-stakeholder-questions.md` | Citation check (the report is in scope and cited) | Opening each citation in the answer |

---

## Lab 1: one vocal buyer ranked near the top

**Where.** Interview I-104 (Marrowby Grocers, Food service, PM-held, 52 minutes). It has 3 strong quotes on P05 Multi-site visibility, including a renewal threat. No other batch 1 interview mentions P05. I-104 is the longest interview, and the buyer says alerts and reports are "fine". This makes P05 stand out.

**Template rule (decision 2, provisional C).** The template keeps "count interviews, not quotes". Proof P1 tests whether this error still shows with that rule. If P1 fails on 2 or more platforms, bring option B back to the course owner with the results. If a platform does not make the error, the debrief uses the instructor's demo run. Update this section after P1.

**What the agent does with the template brief (v1).** It proposes P05 in the top 3 of the backlog, or first in Food service. The reason it gives is the 3 quotes, the renewal threat or "high urgency". It may also write "food service buyers want one view across stores". That breaks the segment rule: P05 has 1 Food service interview.

**Why the quote check passes.** All 3 quotes are word for word in I-104.

**How the audit finds it.** The learner reads the evidence profile of the top-ranked problems, then opens the source interviews. P05 shows 1 interview, 1 account, 1 persona and 1 segment. All 3 quotes come from I-104. P01 and P02 each have 4 interviews, 4 accounts and 3 segments. This is the noisy 20% (workbook skill 1.1B).

**Why I-104 should not be near the top.**

| Evidence profile item | P05 (I-104) | Compare |
| --- | --- | --- |
| Interviews | 1 (3 quotes) | P01 and P02: 4 each. P03, P06, P08: 2 each |
| Accounts | 1 of 8 | P01 and P02: 4 each |
| Segments | Food service only. The other 2 Food service interviews do not raise it | P01 and P02: all 3 segments |
| Urgency | High, from 1 buyer | Urgency without pervasiveness is one voice |
| Willingness to pay clue | Renewal threat from 1 account | The PM may route it to Customer Success as an account issue |
| Next batch | I-111: "it's not my top problem" | P01 and P02 grow to 7 and 6 interviews |

**Expected flag report entry (after the fix, brief v2).**

| Flag ID | Item | Why the agent stopped | Source interview IDs | PM decision |
| --- | --- | --- | --- | --- |
| example | P05 Multi-site visibility | All 3 quotes come from 1 interview. Single source, one segment only. Urgency is high in that interview. Proposed rank 6 of 6 | I-104 | Keep in the backlog. Rank low. Watch in batch 2 |

**Fix the learner adds.** "Count interviews, not quotes, by account, persona and segment. Report each problem's evidence profile as facts. Propose a ranking with a reason for each rank. If all quotes for a problem come from 1 interview, send it to the flag report. Keep single-source problems in the backlog. Never write 'pattern' or 'validated'. I decide the order."

**Batch 2 follow-up.** I-111 mentions P05 once, with low urgency ("it's not my top problem"). P05 becomes 2 interviews, 2 accounts, Food service only. It stays in the bottom group of the proposed ranking, with P04 and P07.

---

## Lab 2: a CRM-only deal leaks into the buyer findings

**Where.**

- `m2-winloss-notes-q2.md`, entry WL-2214 (deal D-2214). The buyer did not attend. The entry holds only a sales note copied from CRM: "Lost on price."
- `m2-crm-export-q2.csv`. CRM-only lost deals D-2204 and D-2210 have the CRM reason "Price" and no interview.

**What the agent does.** It treats WL-2214 as interview evidence, or it fills the missing interviews from the CRM reason. Price then counts 2 to 4 deals and looks like the top buyer driver. The match rate table may count 10 or more deals.

**Why the quote check passes.** The check runs only on deals with a buyer quote. D-2214, D-2204 and D-2210 have no quote, so nothing fails.

**How the audit finds it.** The learner audits 2 random deals and reads the deal source column. D-2214 is labeled "interview" (or has a driver) but there is no buyer interview. Only 1 interviewed buyer (WL-2205) names price.

**Expected flag report entry (after the fix).**

| Flag ID | Deal | Why the agent stopped | Evidence | PM decision |
| --- | --- | --- | --- | --- |
| example | D-2214 | No buyer interview (no-show). Labeled CRM only. Kept out of buyer findings | WL-2214 entry, CRM row | Add to the next interview list, or leave as CRM only |

**Fix the learner adds.** "A deal with no buyer interview is CRM only. Never use the CRM reason or a sales note as a buyer driver. Count only deals with an interview in the match rate table."

---

## Lab 3: forced fit hides a new problem

**Where.** `m3-feedback-week-2.csv`, items F-1215, F-1216, F-1217, F-1218 and F-1219. 5 items from 4 accounts (A-17, A-22, A-31, A-08). Each asks for inspector or auditor read-only, remote access to records. Each item uses the words "inspector", "inspection", "audit" or "report".

**What the agent does.** It tags these items to P02 Compliance report effort, the nearest tag. The "no fit" group stays empty or holds only F-1232 (Spanish app). P02 jumps from 3 to 7 accounts, the largest change of the week, and the summary may call it the top mover. The real new problem is hidden.

**Why the reason check passes.** Each tag reason quotes the item, and the quote contains "inspection report" or "audit". The words match the tag.

**Check sample note.** In `m3-check-sample.md`, F-1305 to F-1307 ask for a contractor repair job. None names a night or weekend, so none fits P06.

**How the audit finds it.** The learner reads 10 random items and the "no fit" group. Any of F-1215 to F-1219 in the sample shows that the buyer does not want a report. They want live, read-only access for the inspector. An empty "no fit" group in a week with new channel content is also a clue.

**Expected flag report entry (after the fix).**

| Flag ID | Item IDs | Why the agent stopped | Accounts | PM decision |
| --- | --- | --- | --- | --- |
| example | F-1215, F-1216, F-1217, F-1218, F-1219 | "No fit" group: 5 items from 4 accounts ask for one thing. Inspectors want read-only remote access to records | 4 (A-08, A-17, A-22, A-31) | Send to discovery. Add P10 to the backlog and the tag list |

**Fix the learner adds.** "Tag an item only if it matches the tag definition, not only its words. If the item asks for something the definition does not cover, mark it no fit."

**Secondary checks in the same data.**

- Account A-05 sends 5 alert items in week 2. Counted by mentions, P01 jumps from 6 to 11. Counted by account, it moves from 6 to 7.
- F-1221 holds a fictional name and phone number (J. Doe, 555-0147). The hand-off rule for personal data must flag it.

---

## Lab 4: CRM competitor trusted where the buyer did nothing

**Where.** Deal D-3108 (Hobnail Burger Co, Food service, lost Q3 2027) in `m4-evidence-pack.md`.

- Part 1, driver log: "Alternative chosen" is blank. The buyer quote is "Rimecore's demo had fewer alerts, I'll give them that."
- Part 2, CRM export: crm_competitor is "Rimecore".
- Part 3, interview WL-3108: "In the end we didn't buy anything; we kept the spreadsheet and the clipboard on the walk-in door."

D-3102 is a decoy. Its alternative is also blank, but the CRM and the interview agree (Vantafrost). So a blank cell alone is not the clue.

**What the agent does.** It fills the blank from the CRM field. Rimecore counts 3 buyer-interview deals in Q3 against 2 in Q2, so Rimecore looks "growing".

**Why the link check passes.** The Rimecore entry links D-3108 and WL-3108. The source type shows "buyer interview", because the deal has an interview.

**How the audit finds it.** The learner traces 3 map entries back to the interviews. WL-3108 says the buyer bought nothing.

**Expected flag report entry (after the fix).**

| Flag ID | Deal or entry | Why the agent stopped | Evidence rows | PM decision |
| --- | --- | --- | --- | --- |
| example | D-3108 | CRM competitor (Rimecore) and the buyer's answer (kept the spreadsheet) differ. Counted as do nothing | D-3108 CRM row, WL-3108 | Accept the buyer's answer. Tell sales ops to fix the CRM field |

**Fix the learner adds (hand-off rule).** "The alternative chosen comes from the buyer's interview. If the driver log cell is blank, read the interview. Never fill it from the CRM competitor field. If the CRM field and the buyer differ, send the deal to the flag report."

---

## Lab 5: old research for another segment presented as current

**Where.** Report R-2025-07 in `m5-past-reports.md`. Dated 2025-09-12 (about 26 months old in November 2027). Food service only. The date and segment are in a small-print header line. Finding 1 is in bold: "Buyers want a one-click inspection binder that follows the county template." Question Q2 asks about pharmacy and lab buyers.

**What the agent does.** It answers Q2 with "Buyers want a one-click inspection binder" and cites R-2025-07. It may show the date in the citation but the answer text still says "buyers want".

**Why the citation check passes.** The report is in scope, and the citation is real.

**How the audit finds it.** The learner opens the citation. The report is food service only, and it is older than 18 months (the case PM's hand-off rule 1). The 2027 pharmacy and lab evidence points somewhere else: calibration certificates with probe serial numbers, and audit exports in the accreditor's or state board's format.

**Expected flag report entry (after the fix).**

| Flag ID | Question | Why the agent stopped | Evidence | PM decision |
| --- | --- | --- | --- | --- |
| example | Q2 | Only evidence for a "report pack" is older than 18 months and covers another segment. Report effort in Pharmacy and lab is 1 interview (P02, I-108): single source in this segment, AI-moderated only, plus feedback from 2 accounts. Calibration certificates (P08: 3 interviews, 3 accounts) are a different need, not a report pack. Question needs new research | R-2025-07 (2025-09-12, Food service); P08; P02 (I-108; A-14, A-29); D-2206; D-3105 | Hold the roadmap commitment. Start 4 to 6 PM-held pharmacy and lab interviews on report needs |

**Fix the learner adds (hand-off rules).** "Do not use a source for a segment it did not study. Flag any source older than my age limit. Rank within a segment before any claim about it. Never write '<segment> buyers want' from 1 interview in that segment. Write what we know, with counts, dates and segments, and what we do not know."

**Not a planted error: Q5 (FDP PM).** Q5 from the Fleet Data Platform PM (decision 9) uses only data already in the agent. It changes no planted error and no lab 1 to 4 count. It tests the segment rule a second time: P03 evidence is Food service interviews plus 1 Distribution lost deal, so "many customer sites" is not supported across segments. See `expected-results.md`.
