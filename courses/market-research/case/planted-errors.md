**Fictional data for training.** Larkspan Systems case. Instructor only. Do not give this file to learners.

# Planted AI errors, by lab

Each lab has one planted error in the case data (house rule 13). The warning fades: told in lab 1, a hint in labs 2 to 4, no hint in lab 5.

Important: the data makes each error likely and findable. It cannot force a model to make it. Gate 2 proof patterns P1 to P3 must confirm that each error shows up on all four platforms. If a platform does not make the error, the debrief shows the error from the instructor's demo run.

## Summary

| Lab | Warning | Error | Where it is | Check that passes anyway | What finds it |
| --- | --- | --- | --- | --- | --- |
| 1 | Told | One vocal buyer counted as a pattern | `m1-interviews-batch-1.md`, interview I-104 | Quote check (all 3 quotes are word for word) | Audit of 3 insights: all 3 quotes trace to I-104 |
| 2 | Hint | CRM-only "price" leaks into buyer findings | `m2-winloss-notes-q2.md`, entry WL-2214 (no-show). Also CRM-only deals D-2204, D-2210 in `m2-crm-export-q2.csv` | Quote check (passes on deals with interviews) | Audit of the deal source column |
| 3 | Hint | Forced fit hides a new problem | `m3-feedback-week-2.csv`, items F-1215 to F-1219 | Reason check (items share words with tag P02) | Audit of 10 random items and the "no fit" group |
| 4 | Hint | CRM competitor trusted where the buyer did nothing | `m4-evidence-pack.md`, deal D-3108 (Parts 1, 2 and 3) | Link check (entry has a deal ID and interview ID) | Audit of map entries against the interview |
| 5 | None | Old research for another segment presented as current | `m5-past-reports.md`, report R-2024-07, asked by Q2 in `m5-stakeholder-questions.md` | Citation check (the report is in scope and cited) | Opening each citation in the answer |

---

## Lab 1: one vocal buyer counted as a pattern

**Where.** Interview I-104 (Marrowby Grocers, Food service, PM-held, 52 minutes). It has 3 strong quotes on P05 Multi-site visibility, including a renewal threat. No other batch 1 interview mentions P05. I-104 is the longest interview, and the buyer says alerts and reports are "fine". This makes P05 stand out.

**What the agent does with the template brief (v1).** The template has no "count interviews, not quotes" rule. The agent is likely to show P05 as a strong or top insight for Food service, with 3 quotes and high intensity. It may mark it as meeting the bar, or call it a pattern. Both are wrong: the agent never writes "Pattern" (Gate 1 PA-01), and P05 has 1 interview.

**Why the quote check passes.** All 3 quotes are word for word in I-104.

The case bar is in `company.md` (the Larkspan Head of Product's bar). Learners on the case path use it.

**How the audit finds it.** The learner picks 3 insights and opens the source interviews. For P05, all 3 quotes come from I-104. Frequency is 1 interview, not 3.

**Expected flag report entry (after the fix, brief v2).**

| Flag ID | Item | Why the agent stopped | Source interview IDs | PM decision |
| --- | --- | --- | --- | --- |
| example | P05 Multi-site visibility | Below the PM's bar. 1 interview (3 quotes). Labeled "single source". Kept in the log for trend tracking | I-104 | Keep in log. Watch in batch 2 |

**Fix the learner adds.** "Count interviews, not quotes, by persona and segment. Mark an insight 'Meets the PM's bar' only when it meets my bar. Label an insight below my bar emerging or single source, and keep it in the log. Never write 'Pattern'. I decide what is a pattern."

**Batch 2 follow-up.** I-111 mentions P05 once, with low intensity ("it's not my top problem"). P05 becomes 2 interviews: still below the case bar, labeled "emerging".

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

**What the agent does.** It tags these items to P02 Compliance report effort, the nearest tag. The "no fit" group stays empty or holds only F-1232 (Spanish app). P02 jumps from 3 to 7 accounts and may be flagged as a big move. The real new problem is hidden.

**Why the reason check passes.** Each tag reason quotes the item, and the quote contains "inspection report" or "audit". The words match the tag.

**Check sample note.** In `m3-check-sample.md`, F-1305 to F-1307 ask for a contractor repair job. None names a night or weekend, so none fits P06.

**How the audit finds it.** The learner reads 10 random items and the "no fit" group. Any of F-1215 to F-1219 in the sample shows that the buyer does not want a report. They want live, read-only access for the inspector. An empty "no fit" group in a week with new channel content is also a clue.

**Expected flag report entry (after the fix).**

| Flag ID | Item IDs | Why the agent stopped | Accounts | PM decision |
| --- | --- | --- | --- | --- |
| example | F-1215, F-1216, F-1217, F-1218, F-1219 | "No fit" items that repeat across 3 or more accounts: inspectors want read-only remote access to records | 4 (A-08, A-17, A-22, A-31) | Send to discovery. Add P10 to the tag list after interviews |

**Fix the learner adds.** "Tag an item only if it matches the tag definition, not only its words. If the item asks for something the definition does not cover, mark it no fit."

**Secondary checks in the same data.**

- Account A-05 sends 5 alert items in week 2. Counted by mentions, P01 jumps from 6 to 11. Counted by account, it moves from 6 to 7.
- F-1221 holds a fictional name and phone number (J. Doe, 555-0147). The hand-off rule for personal data must flag it.

---

## Lab 4: CRM competitor trusted where the buyer did nothing

**Where.** Deal D-3108 (Hobnail Burger Co, Food service, lost Q3 2026) in `m4-evidence-pack.md`.

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

**Where.** Report R-2024-07 in `m5-past-reports.md`. Dated 2024-09-12 (about 26 months old in November 2026). Food service only. The date and segment are in a small-print header line. Finding 1 is in bold: "Buyers want a one-click inspection binder that follows the county template." Question Q2 asks about pharmacy and lab buyers.

**What the agent does.** It answers Q2 with "Buyers want a one-click inspection binder" and cites R-2024-07. It may show the date in the citation but the answer text still says "buyers want".

**Why the citation check passes.** The report is in scope, and the citation is real.

**How the audit finds it.** The learner opens the citation. The report is food service only, and it is older than the 18-month age limit. The 2026 pharmacy and lab evidence points somewhere else: calibration certificates with probe serial numbers, and audit exports in the accreditor's or state board's format.

**Expected flag report entry (after the fix).**

| Flag ID | Question | Why the agent stopped | Evidence | PM decision |
| --- | --- | --- | --- | --- |
| example | Q2 | Only evidence for a "report pack" is older than the age limit and covers another segment. Report effort in Pharmacy and lab is 1 interview (INS-02, I-108), below the PM's bar. Calibration certificates (INS-08) meet the bar, but they are not a report pack. Question needs new research | R-2024-07 (2024-09-12, Food service); INS-08; INS-02 (I-108); D-2206; D-3105 | Hold the roadmap commitment. Start 4 to 6 PM-held pharmacy and lab interviews on report needs |

**Fix the learner adds (hand-off rules).** "Do not use a source for a segment it did not study. Flag any source older than the age limit. If the evidence is below my bar, do not write 'buyers want'. Write what we know, with dates and segments, and what we do not know."
