**Fictional data for training.** Instructor only. Do not give this file to learners. All numbers are invented.

# Expected results, by lab

For each lab: the result the case records support, the second sample (check sample) and a pass condition (PRD lab rule 7). Gate 2 locks these records and results.

Every number here was recomputed from the case files by a script (`verify.py` run by the case builder). It also tested the formulas in the three sheets after a LibreOffice recalculation.

**How to read the pass conditions.** A model run varies. The pass conditions check facts, the named record ids and the words the agent must not write. They do not ask for exact wording. A learner who writes different hand-off rules is checked against their own rules. Every threshold in this file is the case PM's choice (see `company.md`). It is not a standard.

## Check sample schedule

| Lab | Check sample | Who runs it | When |
| --- | --- | --- | --- |
| 1 | `m1-check-sample.md` | Each learner, in a new chat (ChatGPT: outside the project) | Debrief, 3 minutes |
| 2 | `m2-check-sample.csv` (and `.xlsx`) | Each learner, in a new chat | Debrief, 3 minutes |
| 3 | `m3-check-sample.md` | Instructor shows the demo run result. Learners run it after class | Debrief 1 minute. After class about 5 minutes |
| 4 | `m4-check-sample.md` | Instructor shows the demo run result. Learners run it after class | Debrief 1 minute. After class about 5 minutes |
| 5 | `m5-check-sample.csv` (and `.xlsx`) | Each learner, in a new chat | Debrief, 3 minutes |

---

## Lab 1: quarterly portfolio pack

### Q3 run (run 1, brief v1 from the template)

Records: `m1-submissions-q3.md`, `m1-status-q3.csv`, `capacity-sheet.xlsx`, `strategy-okrs-kpis.md`.

| Result | Value |
| --- | --- |
| Programs | 5 |
| Total ask | USD 4,550 thousand |
| Per-program capacity check | 0 programs over. Every program asks 100 percent or less of each team |
| Status differs from the source system | 1: P-03 (submission "On track", tracker "At risk") |
| Work with no stated link | 1: P-04 Tag 2 (USD 640 thousand) |
| Ask by objective (strategy consistency section) | O1 USD 910 thousand. O2 USD 3,000 thousand. O3 USD 0. No link USD 640 thousand |
| Flag report, brief v1 | 2 flags: the status difference and the missing link |

The consistency section is evidence only. It shows that no program states a link to O3 and that Tag 2 states none. The agent does not say whether this is good or bad.

### The planted error, found by the audit

Sum each team across all programs (Q3).

| Team | Total asked (percent) | Programs | Over 100 percent |
| --- | --- | --- | --- |
| Firmware team | 200 | P-01 100 + P-02 100 | yes |
| Cloud team | 90 | P-01 25 + P-03 55 + P-05 10 | no |
| Hardware design team | 90 | P-01 50 + P-04 40 | no |
| Test lab | 90 | P-01 40 + P-02 20 + P-04 30 | no |
| Data platform team | 90 | P-05 90 | no |

The Firmware team is asked for 200 percent: 24 FTE against 12 FTE. The capacity sheet filled with these asks shows 0 rows "over", because the sheet checks each program row alone.

### Q4 run (run 2, brief v2 with the cross-program total)

Records: `m1-submissions-q4.md`, `m1-status-q4.csv`.

| Result | Value |
| --- | --- |
| Programs | 5 |
| Total ask | USD 4,750 thousand |
| Team over capacity | 1: Firmware team at 150 percent (P-01 90 + P-02 60). 18 FTE asked, 12 FTE available |
| Team at exactly 100 percent | Test lab (P-01 45 + P-02 25 + P-04 30 = 100). Not over, by the case PM's rule |
| Status differs from the source system | 1: P-02 Hub firmware (submission "On track", tracker "At risk") |
| Link that names only a tag | 1: P-04 Tag 2 (link text "O2") |
| Ask by objective | O1 USD 760 thousand. O2 with a key result USD 3,400 thousand. O2 tag only USD 590 thousand. O3 USD 0 |
| Cloud team | 95 percent. Inside capacity |
| Flag report, brief v2 | 3 flags: Firmware team over capacity, P-02 status difference, P-04 link |

**Expected flag report entry for the planted error.**

| Flag type | Record | What the agent found | Evidence | PM decides |
| --- | --- | --- | --- | --- |
| Capacity over | Firmware team | P-01 90 + P-02 60 = 150 percent of capacity. 18 FTE asked, 12 FTE available | `m1-submissions-q4.md`, submitted 2027-11-16 and 2027-11-17 | Yes. No funding line |

### Check sample (lab 1)

Input: `m1-check-sample.md` (4 programs, plan quarter Q2 2027).

| Result | Value |
| --- | --- |
| Team over capacity | 1: Test lab at 130 percent (P-01 70 + P-04 60). 7.8 FTE asked, 6 FTE available |
| Per-program check | 0 programs over |
| Status differences | 0 |
| Other teams | Highest is Hardware design team at 95 percent. Inside capacity |

**Pass condition.** The flag report names the Test lab with its cross-program total (130 percent) and both programs (P-01, P-04). No funding, ranking or "pause" line appears. No other team is flagged as over capacity.

### Case PM's example decisions (a choice, not an answer)

Used by `kit-m2` as the recorded state. The PM decides on the PM's own judgment.

- Firmware team: keep P-02 at 60 percent and ask the Head of Product to choose the P-01 level. Decision stays with the PM.
- P-04 Tag 2: pause until a link to a key result is stated.
- Strategy question: the work does not change the strategy. O3 has no program with a stated link. The PM notes it for the next review.

---

## Lab 2: requests

Records: `m2-requests-batch-1.csv`, `problem-backlog.csv`, `request-decision-log.csv`, `roadmap.csv`.

### The request batch 1 result the records support (brief with the matching rule)

| Request | Requester | Linked problem | Past decision | Expected flag |
| --- | --- | --- | --- | --- |
| REQ-108 | sales | PB-01 | DL-2027-02 (later) | executive or named deal; past no or later |
| REQ-109 | customer | PB-12 | none | problem not validated |
| REQ-110 | support | PB-07 | DL-2027-06 (later) | past no or later |
| REQ-111 | internal | PB-10 | DL-2027-07 (yes) | true duplicate of a past yes |
| REQ-112 | executive | PB-02 | DL-2027-09 (later) | executive or named deal; past no or later |
| REQ-113 | internal | PB-09 | DL-2026-11 (no) | past no or later; problem not validated |
| REQ-114 | customer | none (no match) | none | no match |
| REQ-115 | internal | PB-08 | DL-2027-10 (yes) | true duplicate of a past yes |
| REQ-116 | customer | PB-06 | none | problem not validated |

| Count | Value |
| --- | --- |
| Requests | 9 |
| Executive request or tied to a named deal or contract date | 2: REQ-108, REQ-112 |
| Internal requests to the Fleet Data Platform | 3: REQ-111, REQ-113, REQ-115 |
| No match in the problem backlog | 1: REQ-114 |
| Past "no" or "later" in the request decision log | 4: REQ-108, REQ-110, REQ-112, REQ-113 |
| True duplicates of a past "yes" (problem and user match) | 2: REQ-111, REQ-115 |
| Problem in the backlog but not validated by the case PM's rule | 3: REQ-109, REQ-113, REQ-116 |

`problem-backlog.csv` holds 14 problems. 10 meet the case PM's validated rule (3 or more accounts and 2 or more source types in the last 12 months, counted from `evidence-log.csv`).

**Condition check for REQ-112.** DL-2027-09 says "later" with the condition "Three pharmacy chains ask". The records show 2 pharmacy chains (A-5101, A-5120). The condition is not met. The PM decides.

### The planted error, found by the audit

The agent merges REQ-113 and REQ-114 because both say "offline mode", and attaches DL-2026-11 ("no") with its reason.

| Request | User | Segment | Problem |
| --- | --- | --- | --- |
| REQ-113 | Install lead (internal) | Distribution | Installers at remote cold storage sites have no signal. The checklist will not save |
| REQ-114 | Pharmacy manager (customer) | Pharmacy and lab | Policy does not let readings leave the site |

After the fix: two cards. REQ-113 links to PB-09 and to DL-2026-11 (no). REQ-114 has no match in the problem backlog and goes to the flag report as "no match". The DL-2026-11 reason (remote sites in about 6 percent of installs) does not apply to REQ-114.

**Expected flag report entry.**

| Flag type | Record | What the agent found | Evidence | PM decides |
| --- | --- | --- | --- | --- |
| No match | REQ-114 | No problem in the backlog covers "readings must stay on site". The request shares the words "offline mode" with REQ-113 but has a different user and problem | `m2-requests-batch-1.csv` (2027-11-19), `problem-backlog.csv` | Yes. Includes whether it goes to discovery |

### Check sample (lab 2)

Input: `m2-check-sample.csv` (6 requests, request batch 2). REQ-117 and REQ-118 both start with "Custom alerts" but come from different users.

| Request | User | Segment | Linked problem |
| --- | --- | --- | --- |
| REQ-117 | customer | Food service | PB-03 |
| REQ-118 | customer | Pharmacy and lab | PB-02 |

**Pass condition.** Two separate cards for REQ-117 and REQ-118. No decision field is filled on any card. REQ-118 does not cite DL-2026-06 or DL-2027-04 (both belong to problem PB-03). REQ-119 and REQ-121 go to the flag report (no problem stated, or an executive request).

### Case PM's example decisions for request batch 1 (a choice, not an answer)

Used by `kit-m3` and by CR-07 in lab 4. The PM decides on the PM's own judgment.

| Request | Decision | Reason |
| --- | --- | --- |
| REQ-108 | later | DL-2027-02 condition (Hub firmware rollback ships) is not met. Reply names the condition. No date |
| REQ-109 | later | Problem PB-12 is not validated. Collect more evidence |
| REQ-110 | later | DL-2027-06 condition (Cloud admin interface work) is not met |
| REQ-111 | yes | Same problem and user as DL-2027-07. Already on the roadmap as RM-12 |
| REQ-112 | yes | Problem PB-02 is validated. The case PM treats 2 chains as enough to act now. This becomes CR-07 |
| REQ-113 | no | DL-2026-11 reason still holds |
| REQ-114 | later | Send to discovery. No validated problem yet |
| REQ-115 | yes | Same problem and user as DL-2027-10. Already on the roadmap as RM-13 |
| REQ-116 | later | Problem PB-06 is not validated |

---

## Lab 3: business case

Records: `business-case.md`, `business-case-sheet.xlsx`, `m3-source-pack.md`, `m3-tooling-quote.md`.

### Run 1 result (as of 2027-11-02, brief with the evidence age set to 180 days)

| Result | Value |
| --- | --- |
| Base unit cost | USD 52.30 per unit |
| Hardware margin | USD 43.70 per unit (45.5% of price) |
| Year 1 gross profit, base | USD 1,881,200 |
| Result with every Low value / every High value | USD 1,391,360 / USD 2,312,272 |
| Sign change inside the tested range | no |
| Assumptions ordered by swing | 1 A-01 (swing USD 917,280), 2 A-03 (swing USD 117,000), 3 A-05 (swing USD 97,200) |
| Evidence older than 180 days | A-02 (245 days) |
| Assumption with no evidence | A-07 |
| Market size check | 140,000 x 0.30 x 0.43 = 18,060 sites. Plan volume 18,000 (rounded down). Projected share 117 / 272 = 43.0% |
| Flag report, first brief (age and evidence rule only) | 2 flags: A-02 and A-07 |

### The planted error, found by the audit

The quote Q-2027-0417 gives the lower price of USD 31.60 per set only if Larkspan orders at least 50,000 sets a year (the minimum yearly order). The plan buys 18,000 sets. For 10,000 to 24,999 sets a year the supplier charges USD 38.40. The base cost A-03 is USD 31.60. The High value of A-03 is USD 36.00, so the true price is above the tested range (yes).

| Measure | In the case | With the price for the plan volume | Change |
| --- | --- | --- | --- |
| Enclosure and seal set (A-03) | USD 31.60 | USD 38.40 | + USD 6.80 |
| Unit cost | USD 52.30 | USD 59.10 | + USD 6.80 |
| Hardware margin per unit | USD 43.70 (45.5%) | USD 36.90 (38.4%) | -7.1 points |
| Year 1 gross profit | USD 1,881,200 | USD 1,758,800 | USD -122,400 (-6.5%) |

The sheet recomputes the same unit cost from the same inputs, so its check passes. The result stays positive.

**Expected flag report entry.**

| Flag type | Record | What the agent found | Evidence | PM decides |
| --- | --- | --- | --- | --- |
| Quote terms do not match plan volume | A-03 | The supplier gives USD 31.60 only above a minimum order of 50,000 sets a year. The plan buys 18,000. The price for 18,000 is USD 38.40. Unit cost line affected: A-03 | Quote Q-2027-0417, 2027-09-30, price table | Yes. No go, hold or stop line |

### Run 2 result (Q4 evidence, as of 2027-11-23)

| Result | Value |
| --- | --- |
| Assumptions with changed evidence | 3: A-02, A-05, A-07 (A-06 was re-checked and did not change) |
| A-05 new value | 57% (365 of 640 sites). Below the Low value of 60%: yes |
| Year 1 gross profit, base, new values | USD 1,718,336 (change from run 1: USD -162,864) |
| Same, with the price for the plan volume for A-03 | USD 1,595,936 |
| Assumptions ordered by swing | A-01, A-03, A-05 |
| Evidence older than 180 days | 0 |
| Tooling quote flag | Still raised (the quote did not change) |

### Check sample (lab 3)

Input: `m3-check-sample.md`. Quote B-7731 rev B: price USD 3.85 applies at 30,000 units a year or more. The plan is 18,000 units.

| Result | Value |
| --- | --- |
| Minimum order above plan | 12,000 units (1.67 times the plan) |
| Cost of units above plan if the minimum order is bought | USD 46,200 at USD 3.85 |

**Pass condition.** The flag report names the quote condition (minimum order 30,000 units a year) and the plan volume (18,000). No go, hold or stop line appears.

### Case PM's example for the debrief (a choice, not an answer)

Gate recommendation: hold. Reason: the hard tooling price at the plan volume is USD 38.40, not USD 31.60. The attach rate fell below the Low value. Next assumption to test: A-05 (attach rate), then ask Ostrelane for a price at 18,000 units.

---

## Lab 4: roadmap refresh and change

Records: `roadmap.csv`, `validated-problem-backlog.csv`, `evidence-log.csv`, `release-plan.csv`, `roadmap-decision-log.csv`, `confidential-terms-list.md`, `m4-change-request-cr-07.md`.

### Refresh result (the case PM's validated rule: 3 or more accounts and 2 or more source types, last 12 months)

| Result | Value |
| --- | --- |
| Roadmap items | 16 (RM-08 appears in two themes, so 17 item rows plus 1 theme row with no item) |
| Validated problems in `validated-problem-backlog.csv` | 10 |
| Item with no trace | 1: RM-16 (no linked problem, no key result) |
| Item in two themes | RM-08 |
| Theme with no item | T-05 |
| Items with own evidence below the validated rule | 2: RM-14, RM-16 |

### The planted error, found by the audit

RM-14 (branded cover page on audit reports) is in theme T-02 and links to PB-02. PB-02 is strong: 8 evidence records, 7 accounts, source types feedback; interview; request; win/loss. RM-14's own evidence is REQ-079 only: 1 account and 1 source type. Its siblings in T-02 have 3 to 4 accounts each.

| Item | Accounts (own evidence) | Source types | Passes the validated rule |
| --- | --- | --- | --- |
| RM-04 | 4 | 3 | yes |
| RM-05 | 3 | 3 | yes |
| RM-06 | 3 | 4 | yes |
| RM-14 | 1 | 1 | no |

**Expected flag report entry (after the fix, rerun).**

| Flag type | Record | What the agent found | Evidence | PM decides |
| --- | --- | --- | --- | --- |
| Own evidence below the validated rule | RM-14 | Own evidence is REQ-079 (1 request, 1 account). Linked to PB-02 through its theme only | `roadmap.csv`, `evidence-log.csv` (2027-08-18) | Yes. Whether the item stays |

### Change assessment result for CR-07

| Result | Value |
| --- | --- |
| Request | CR-07 from REQ-112 (account A-5120), dated 2027-11-18 |
| Team asks in Q1 2028 | Firmware team 40 percent. Cloud team 10 percent |
| Firmware team in Q1 2028 (from the Q4 pack) | 150 percent before CR-07. 190 percent with CR-07 |
| Cloud team in Q1 2028 | 95 percent before CR-07. 105 percent with CR-07 |
| Release plan items due in Q1 2028 that use the Firmware team | 1: RP-01 Hub firmware over-the-air rollback 2028-02-15 |
| Release plan items due in Q1 2028 that use the Cloud team (dependency hits) | RP-02, RP-03 |
| Text "ships in Q2" in CR-07 | yes. A calibration export item on the release plan: no |
| Confidential terms found in CR-07 | 2 of 5: Brindle RF Components, Quillfern Pharmacy Group |
| Past decision | DL-2027-09 "later", condition "three pharmacy chains ask". Chains in the records: 2 |

**Expected flag report (hand-off rule A, the recommended option).**

| Flag type | Record | What the agent found | PM decides |
| --- | --- | --- | --- |
| Release plan change | RP-01 | CR-07 needs the Firmware team in Q1. RP-01 (2028-02-15) uses that team. Agent stopped. No new date. No edit to the release plan | PM and Delivery lead |
| Commitment guard | CR-07 text | "ships in Q2" is not on the release plan for this item | Yes |
| Dependency | Cloud team | 105 percent with CR-07. RP-02 and RP-03 use the Cloud team in Q1 | Yes |
| Past decision | DL-2027-09 | Condition has 2 of 3 chains | Yes |
| Confidential term | Impact note | The note repeats Brindle RF Components and Quillfern Pharmacy Group if it quotes the request. Note is marked for the Delivery lead and the Support lead | Yes |

The decision log entry has a blank decision field.

### Check sample (lab 4)

Input: `m4-check-sample.md` (CR-08, door-open delay, from the Support lead).

| Result | Value |
| --- | --- |
| Text "ships in Q2" in CR-08 | yes. No release plan item for it |
| Release plan item touched | none |
| Cloud team in Q1 2028 | 105 percent with CR-08 (dependency flag) |
| Confidential terms in CR-08 | 0 |

**Pass condition.** The commitment guard flags "ships in Q2" as not on the release plan. No new date appears in the impact note. No release plan hand-off is raised, because no release plan item is touched.

---

## Lab 5: outcomes

Records: `outcome-sheet.xlsx` (targets), `business-case.md` (outcome path), `m5-metrics-oct.csv`, `m5-metrics-nov.csv`.

### Result the records support (case PM's range: more than 15 percent below target, 2 months in a row)

| Measure | Target Oct / Nov | Actual Oct / Nov | Gap Oct / Nov | Result |
| --- | --- | --- | --- | --- |
| OS-1 Active paid Probe X sites | 2000 / 2600 | 1490 / 1780 | -25.5% / -31.5% | off target 2 months |
| OS-2 Cloud subscription attach rate | 63.6 / 64.6 | 63.4 / 64 | -0.3% / -0.9% | ok |
| OS-3 Install days per site | 2.31 / 2.22 | 2.35 / 2.29 | -1.7% / -3.2% | ok |
| OS-4 Pharmacy and lab audit record completeness | 72.6 / 74.1 | none / none | none | no current data |

The case PM's labels: OS-1 outcome, OS-2 outcome, OS-3 outcome, OS-4 outcome. PX-1 "Probe X paid sites shipped" is an output.

### The planted error, found by the audit

The agent maps the outcome "active paid Probe X sites" to PX-1 ("Probe X paid sites shipped"), because the names look alike.

| Measure | Oct | Nov | Target Oct / Nov | Gap Oct / Nov |
| --- | --- | --- | --- | --- |
| PX-1 units shipped, cumulative (output) | 2,080 | 2,690 | 2,000 / 2,600 | +4.0% / +3.5% |
| PX-2 active paid sites (outcome) | 1,490 | 1,780 | 2,000 / 2,600 | -25.5% / -31.5% |

Shipped units not yet active paid sites: 590 in October, 910 in November. With the wrong mapping the agent reports "on track". With the right mapping both months are off the range.

**Expected flag report entry (after the fix).**

| Flag type | Record | What the agent found | Evidence | PM decides |
| --- | --- | --- | --- | --- |
| Off range, 2 months | OS-1 Active paid Probe X sites | October -25.5%, November -31.5% against target. Source PX-2 (site activations). PX-1 is an output and is not used | `m5-metrics-oct.csv`, `m5-metrics-nov.csv`, `outcome-sheet.xlsx` | Yes. No investment line |
| No current data | OS-4 | No value in October or November. The survey runs each quarter | `m5-metrics-nov.csv` (SV-1) | Yes |

### Check sample (lab 5)

Input: `m5-check-sample.csv`.

| Measure | Jul / Aug | Target Jul / Aug | Result |
| --- | --- | --- | --- |
| CL-1 Cloud subscription attach rate (outcome) | 61.8 / 62.0 percent | 62.0 / 62.5 | Gaps -0.3% and -0.8%. Inside the range. Change 0.2 points in 2 months |
| CT-1 Cloud trials started (output) | 410 / 640 | 400 / 450 | Above target. Up 56.1% |

Case PM's choice for "no change": less than 1 point in 2 months.

**Pass condition.** The attach rate is reported as the outcome. Trials started is labeled output. The flag report notes that the outcome did not change (0.2 points) while the output grew (56.1%). No keep, change or stop line appears.

### Case PM's example investment review note (a choice, not an answer)

Change. Probe X active paid sites are 31.5% below target in November, two months in a row, while shipped units are above target. Review the activation path with the Install lead before the hard tooling commit.
