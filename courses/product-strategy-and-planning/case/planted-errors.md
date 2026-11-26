**Fictional data for training.** Larkspan Systems, its people, customers, suppliers and all numbers are invented. Any match with a real company or person is chance. No real personal data and no health data.

# Planted AI errors, by lab

Instructor only. Do not give this file to learners.

Each lab has one planted error in the case data (house rule 13). The warning fades: told in lab 1, a hint in labs 2 to 4, no hint in lab 5. Each error sits in the data and passes the agent's own quality checks and hand-off rules. Only the audit finds it.

**Important.** The data makes each error likely and findable. It cannot force a model to make it. Gate 2 proof patterns P1 to P3 must confirm that each error shows up on all four platforms. If a platform does not make the error, the debrief shows the error from the instructor's demo run.

## Summary

| Lab | Warning | Error | Where it is | Check that passes anyway | What finds it |
| --- | --- | --- | --- | --- | --- |
| 1 | Told | Shared firmware team planned at 100% in two programs | `m1-submissions-q3.md`, team asks for P-01 and P-02 (also `m1-submissions-q4.md`) | Per-program capacity check. Each ask is 100 percent or less | Sum by team: Firmware team 200 percent |
| 2 | Hint | False duplicate: two "offline mode" requests with different problems | `m2-requests-week-47.csv`, REQ-113 and REQ-114. Past "no" in `request-decision-log.csv`, DL-2025-11 | Quote check and log id check. The card quotes the request and cites DL-2025-11 | Opening the merge and reading the user and problem of each request |
| 3 | Hint | Tooling quote price is for 50,000 units a year. Plan is 18,000 | `business-case.md` and `business-case-sheet.xlsx` row A-03. Terms in `m3-tooling-quote.md` | Evidence check (source and date) and sheet recompute | Reading the quote tiers against the plan volume |
| 4 | Hint | Validation by association: RM-14 has one sales request in a strong theme | `roadmap.csv`, row RM-14. Evidence in `evidence-log.csv`, REQ-079 | Trace check (RM-14 links to PB-02, which is validated) | Reading RM-14's own evidence ids |
| 5 | None | Output counted as outcome: units shipped reported as active paid sites | `m5-metrics-oct.csv` and `m5-metrics-nov.csv`, metric PX-1 against OS-1 | Source and label check on every value | Reading the metric definition against the business case outcome text |

---

## Lab 1: shared team counted twice

**Where.** `m1-submissions-q3.md`, "Team asks" table: P-01 Probe X cellular asks the Firmware team for 100 percent. P-02 Hub firmware asks the same team for 100 percent. The Firmware team has 12 FTE. The error also exists in Q4 (90 and 60, total 150 percent) so the fix shows in run 2.

**What the agent does with the template brief (v1).** It checks capacity per program row. Each row is inside the team total, so every row passes. The capacity sheet shows 0 rows "over". The pack shows "capacity OK".

**Why the checks pass.** The template check is "Capacity per program is inside the team's total". Each ask is 100 percent or less. The template has no check that adds a team across programs.

**How the audit finds it.** The learner picks the Firmware team and adds P-01 and P-02: 200 percent, or 24 FTE against 12. The other shared teams (Cloud team 90 percent, Hardware design team 90, Test lab 90) are inside capacity. This is the aha: every per-program check passed, and the team total is double.

**Expected flag report entry (after the fix, Q4).**

| Flag type | Record | What the agent found | Evidence | PM decides |
| --- | --- | --- | --- | --- |
| Capacity over | Firmware team | P-01 90 + P-02 60 = 150 percent of capacity | `m1-submissions-q4.md` | Yes |

**Fix the learner adds.** "Total each shared team across all programs. Send any team over its capacity to the flag report."

**Other flags in the same run (not errors).** Q3: P-03 status differs from the tracker. P-04 has no stated link. Q4: P-02 status differs. P-04 link names only a tag. The Test lab is at exactly 100 percent in Q4 and is not over.

---

## Lab 2: a false duplicate

**Where.** `m2-requests-week-47.csv`:

- REQ-113 (Install lead, internal): "Add offline mode to the install checklist." Problem: installers at remote cold storage sites have no signal.
- REQ-114 (Pharmacy manager, customer A-5207): "Add offline mode." Problem: policy does not let readings leave the site.

`request-decision-log.csv`, DL-2025-11: last year's "no" on offline mode for field installers, with its reason (remote sites about 6 percent of installs, 48 hour cache, 14 weeks of work).

**What the agent does with the template brief.** It sees the same words. It merges both requests into one card and cites DL-2025-11 with its reason. The card quotes both requests and names a log id.

**Why the checks pass.** Every card quotes the request. Every past decision cites a log id. The decision field is blank. The reply (when drafted) matches the PM's decision.

**How the audit finds it.** The learner opens the merged card and reads both source requests. The users differ (installer, pharmacy customer). The segments differ (Distribution, Pharmacy and lab). The problems differ. The DL-2025-11 reason does not apply to the pharmacy request.

**Expected flag report entry (after the fix).** REQ-114, "no match", PM decides (also whether it goes to discovery). REQ-113 keeps its link to DL-2025-11.

**Fix the learner adds.** "Match on the problem statement and the user, not on feature words. Send any merge across segments to the flag report."

**Contrast cases in the same file.** REQ-111 and REQ-115 are true duplicates of past "yes" decisions (same problem, same user). They should link to DL-2026-07 and DL-2026-10. This shows a good merge.

---

## Lab 3: quote terms do not match the plan

**Where.** `m3-tooling-quote.md`, price table: USD 38.40 per set at 10,000 to 24,999 units, USD 31.60 at 50,000 and above. `business-case.md` and `business-case-sheet.xlsx`, assumption A-03: base USD 31.60, source "Corvane Tooling quote Q-2026-0417", dated 2026-09-30. Plan volume (A-01) is 18,000.

**What the agent does with the template brief.** It registers A-03 with its source and date. The sheet recomputes the same unit cost (USD 52.30). A-03 is the second assumption by swing, so the red team note covers it, but it tests the High value (USD 36.00), not the quote terms.

**Why the checks pass.** The register row has evidence, a date, an owner and a range. The sheet formula returns the same unit cost. The evidence is not stale (33 days at the run date).

**How the audit finds it.** The learner reads the quote for A-03, one of the two assumptions with the largest effect. The price table is by annual volume. The plan is 18,000 units. The matching tier is USD 38.40. The true price is above the High value of the tested range.

**Effect (recomputed).** Unit cost rises from USD 52.30 to USD 59.10. Hardware margin falls from 45.5% to 38.4%. Year 1 gross profit falls by USD 122,400.

**Expected flag report entry (after the fix).** Quote terms do not match plan volume. A-03. Price applies at 50,000 units a year or more. Plan is 18,000. Source: quote Q-2026-0417, 2026-09-30. PM decides. No go, hold or stop line.

**Fix the learner adds.** "A price or cost whose quote terms do not match the plan volume goes to the flag report."

**Other flags in the same run (not errors).** Run 1: A-02 evidence older than 180 days. A-07 has no evidence. Run 2: A-02, A-05 and A-07 evidence changed. A-05 is below its Low value.

---

## Lab 4: validation by association

**Where.** `roadmap.csv`, row RM-14 "Branded cover page on audit reports". Theme T-02. Linked problem PB-02. Own evidence: REQ-079 only (`evidence-log.csv`, a sales request from account A-5108, dated 2026-08-18, no problem stated).

**What the agent does with the template brief.** It traces RM-14 to T-02, PB-02 and KR1.2. PB-02 is in the validated problem backlog. The trace table shows RM-14 as linked.

**Why the checks pass.** The trace check asks for a theme, a validated problem and a stated objective. RM-14 has all three. The theme and PB-02 are strong (8 evidence records, 7 accounts, 4 source types).

**How the audit finds it.** The learner opens RM-14's own evidence ids. It has 1 account and 1 source type. The case PM's validated rule needs 3 accounts and 2 source types. Sibling items RM-04, RM-05 and RM-06 each pass.

**Expected flag report entry (after the fix, rerun).** Own evidence below the validated rule. RM-14. Own evidence REQ-079 (1 request, 1 account). PM decides.

**Fix the learner adds.** "Judge each item by its own evidence, not its theme's. Send any item below the validated rule to the flag report."

**Other flags in the same run (not errors).** RM-16 has no trace. RM-08 sits in two themes. T-05 has no item. CR-07 raises a release plan change (RP-01), a commitment guard flag, a dependency and a confidential term flag.

---

## Lab 5: output counted as outcome

**Where.** `m5-metrics-oct.csv` and `m5-metrics-nov.csv`.

- PX-1 "Probe X paid sites shipped". Definition: units invoiced to resellers, cumulative, one unit per site. Values 2,080 (October) and 2,690 (November).
- PX-2 "Probe X site activations". Definition: sites with Probe X activated and a paid Cloud plan, at month end. Values 1,490 and 1,780.

The business case outcome is "active paid Probe X sites" (`business-case.md`). The target in `outcome-sheet.xlsx` is 2,000 (October) and 2,600 (November).

**What the agent does.** It matches "active paid Probe X sites" to PX-1 because the words "paid", "sites" and "Probe X" match. PX-1 is 4% and 3.5% above target. The agent reports the measure on track.

**Why the checks pass.** Each value has a source and a date. Each measure has a label and a baseline and target. The agent labels PX-1 "outcome".

**How the audit finds it.** The learner reads the definition of PX-1 and the business case outcome text. Shipped units are an output. PX-2 is the outcome. Gap is -25.5% in October and -31.5% in November, both outside the case PM's range of 15 percent.

**Expected flag report entry (after the fix).** Off range, 2 months. OS-1. Source PX-2. PM decides. No investment line.

**Fix the learner adds.** "Match each measure to the outcome text in the business case, not to the metric name. Units shipped is an output."
