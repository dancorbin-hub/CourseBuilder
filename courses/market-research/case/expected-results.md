**Fictional data for training.** Larkspan Systems case. Instructor only. Do not give this file to learners.

# Expected results, by lab

For each lab: the result the case records support, the second sample input and a concrete pass condition (PRD lab rule 7). Gate 2 locks these records and results.

## The case PM's bar (example only)

Learners see this bar in `company.md`, as the Larkspan Head of Product's bar for this study. It is that PM's choice, not a rule. There is no magic number.

- **Meets the PM's bar**: 3 or more interviews (not quotes), from 2 or more accounts, with 1 or more PM-held interview. Show the segment split.
- **Segment claims**: a claim about one segment needs the bar met inside that segment.
- **Emerging**: 2 interviews, or 3 or more with no PM-held interview.
- **Single source**: 1 interview, however many quotes. In this case, a single interview is labeled single source.
- **Win/loss**: a driver pattern needs 3 or more interviewed deals in a segment.
- **Weekly feedback**: a "what moved" flag needs a change of 3 or more accounts.
- **Stakeholder answers**: age limit 18 months.

**Who labels a pattern (Gate 1 PA-01).** The agent writes "Meets the PM's bar". It never writes "Pattern". Only the PM promotes an insight to "Pattern". In the tables below, "Status" is the agent's label.

A learner may set a different bar. The pass condition then uses the learner's bar.

**Debrief prompt (lab 1).** Use Dan's test for any bar: can you predict that the next buyer of this persona will raise it? If not, the evidence is not yet a pattern.

---

## Lab 1: insight log

### Batch 1 (`m1-interviews-batch-1.md`), after the fix

| Code | Interviews | IDs (PM-held in bold) | Segments | Status |
| --- | --- | --- | --- | --- |
| P01 Alert fatigue | 4 | **I-101**, I-102, I-105, I-107 | Distribution 2, Food service 1, Pharmacy and lab 1 | Meets the PM's bar. No segment meets it alone |
| P02 Compliance report effort | 4 | I-102, **I-103**, **I-106**, I-108 | Distribution 2, Food service 1, Pharmacy and lab 1 | Meets the PM's bar. No segment meets it alone |
| P03 Install and connectivity | 2 | **I-103**, I-105 | Food service 2 | Emerging |
| P05 Multi-site visibility | 1 (3 quotes) | **I-104** | Food service | Single source (planted error) |
| P06 After-hours response | 2 | **I-101**, **I-106** | Distribution 2. Both say own managers own night alarms | Emerging |
| P08 Calibration records | 2 | I-107, I-108 | Pharmacy and lab 2 | Emerging (2 interviews, no PM-held interview) |

Batch 1 flag report:

1. I-102 note fits no code: a distributor wants to send temperature proof to its own customers. PM decision: send to discovery. It becomes P09 in the tag list (lab 3).
2. Pharmacy and lab has no PM-held interview (I-107, I-108 are AI-moderated). PM decision: book a PM-held interview.
3. Below the bar: P05 (single source), P03, P06, P08 (emerging). Kept in the log.

Before the fix (template brief v1), expect P05 to look like a strong or top Food service insight. That is the planted error.

The PM then reviews P01 and P02. The PM may promote them to "Pattern" across segments. No single segment meets the bar yet, so the PM makes no segment claim. The agent promotes nothing.

### Batch 2 (`m1-interviews-batch-2.md`)

| Code | Interviews after batch 2 | New IDs | Status | What changed |
| --- | --- | --- | --- | --- |
| P01 | 7 (Distribution 4, Pharmacy and lab 2, Food service 1) | **I-109**, I-110, **I-113** | Meets the PM's bar. Inside a segment: Distribution | Growing |
| P02 | 6 (Distribution 3, Food service 2, Pharmacy and lab 1) | **I-109**, I-114 | Meets the PM's bar. Inside a segment: Distribution | Growing |
| P03 | 3 (Food service 3; 2 accounts: Saltgrass Kitchens, Bramblefield Bistro) | **I-111** | Meets the PM's bar (Food service) | Now meets the bar |
| P04 Sensor upkeep | 1 | **I-112** | Single source | New |
| P05 | 2 | **I-111** (low intensity: "not my top problem") | Emerging | Still below the bar |
| P06 | 4 | I-110, **I-112** | Contradiction | I-110 and I-112 want a service to take night calls. I-101 and I-106 want own managers. I-106 and I-112 are the same account (Pellham Distribution) |
| P07 Product loss cost | 1 | I-114 | Single source | New |
| P08 | 3 (Pharmacy and lab 3; 3 accounts) | **I-113** | Meets the PM's bar (Pharmacy and lab) | Now has a PM-held interview |

Batch 2 flag report: (1) P06 contradiction, (2) single source P04 and P07, (3) emerging P05. The Pharmacy and lab flag clears.

The PM decides which insights become "Pattern". The case PM promotes P01 and P02 for Distribution, P03 for Food service and P08 for Pharmacy and lab. This is the PM decision column in Part 4 of `m4-evidence-pack.md`.

**Success check (spec).** The log updates. The flag report lists the P06 contradiction. No insight below the bar is marked "Meets the PM's bar". The agent writes "Pattern" for no insight.

### Second sample: `m1-check-sample.md`

Run on an empty log.

| Code | Interviews | Expected label |
| --- | --- | --- |
| P07 Product loss cost | 1 (I-201, 3 quotes) | Single source |
| P01 Alert fatigue | 2 (I-202, I-203) | Emerging |
| P04 Sensor upkeep | 2 (I-203, I-204) | Emerging |

**Pass condition.**

1. P07 shows a frequency of 1 interview, not 3, and is labeled "single source".
2. No insight is marked "Meets the PM's bar", and the agent writes "Pattern" for none.
3. The flag report lists P07 and says Pharmacy and lab has no PM-held interview (I-204).
4. Every quote is word for word in the sample.

### Stretch: `m1-stretch-applicants.md`

Criteria are in `m1-stretch-applicants.md`. The study starts in December 2026.

| Result | Applicant | Reason |
| --- | --- | --- |
| Pass | AP-01, AP-04, AP-06 | Meet all 5 criteria |
| Pass | AP-11 | Meets all 5 criteria. Uses a competitor (Rimecore), which is allowed |
| Fail | AP-02 | Criterion 2 and 3: uses only, 1 site |
| Fail | AP-03 | Criterion 5: interviewed 2026-09, inside 6 months |
| Fail | AP-05 | Criterion 4: works for a reseller |
| Fail | AP-09 | Criterion 1: segment out of scope (hardware retail) |
| Edge case to the PM | AP-07 | Criterion 2: "Influences" only. Is that "strongly influences"? Criterion 3 passes (11 walk-ins) |
| Edge case to the PM | AP-08 | Criterion 3: 2 warehouses and no cold-room count. Criterion 5 passes (last interview 2026-05, 7 months before) |
| Edge case to the PM | AP-10 | Criterion 2: runs the purchase but does not choose |
| Edge case to the PM | AP-12 | Criterion 2: "Influences" only |

--- | --- | --- |
| Pass | AP-01, AP-04, AP-06, AP-11 | Meet all 5 criteria. AP-11 uses a competitor, which is allowed |
| Fail | AP-02, AP-03, AP-05, AP-09 | 1 site and user only; interviewed 2026-09; works for a reseller; segment out of scope |
| Edge case to the PM | AP-07, AP-08, AP-10, AP-12 | 2 sites but 11 walk-ins; last interview 2026-05 is close to the 6-month line; runs the purchase but does not choose; "influences" only |

---

## Lab 2: win/loss and the match rate

### Result on `m2-crm-export-q2.csv` and `m2-winloss-notes-q2.md`

14 decided deals: 9 with an interview, 5 CRM only (D-2204, D-2208, D-2210, D-2213, D-2214).

The correct driver log is Part 1 (Q2 rows) of `m4-evidence-pack.md`.

**Match rate table (interviewed deals only).**

| Outcome | Deals with an interview | CRM reason matches buyer primary driver | Match rate |
| --- | --- | --- | --- |
| Won | 3 | 2 (D-2201, D-2206) | 67% |
| Lost | 6 | 2 (D-2205, D-2211) | 33% |
| Total | 9 | 4 | 44% |

**Buyer drivers on lost deals (interviewed only).** D1 Price 1 (D-2205), D2 Install 1 (D-2203), D3 Alert accuracy 1 (D-2207), D4 Report fit 1 (D-2212), D7 Timing 1 (D-2211), D10 Current equipment 1 (D-2209). No driver repeats.

**The aha.** CRM says "Price" on 7 of 9 lost deals. Interviewed buyers name price on 1 of 6.

**Flag report.**

1. CRM and buyer reasons differ: D-2202, D-2203, D-2207, D-2209, D-2212.
2. Alternative not in the code book: D-2209 (alarms in a new refrigeration controller).
3. Segment with too few deals: Pharmacy and lab (2 interviewed deals: D-2206, D-2211).
4. D-2214 has no interview (buyer did not attend). CRM only.

**Planted error.** With the leak, price shows 2 to 4 buyer deals and looks like the top driver.

**Pass condition (spec success check).** The match rate table counts only the 9 interviewed deals. No CRM-only deal (including D-2214) is in the buyer driver findings. The flag report lists the 5 mismatched deals.

### Second sample: `m2-check-sample.md`

10 deals (program minimum met). Interviewed: D-1301, D-1302, D-1304, D-1306, D-1308, D-1309. CRM only: D-1303, D-1305, D-1307 (declined, sales note "Price"), D-1310.

| Outcome | Interviewed | Match | Match rate |
| --- | --- | --- | --- |
| Won | 2 | 2 | 100% |
| Lost | 4 | 1 (D-1306) | 25% |
| Total | 6 | 3 | 50% |

**Pass condition.**

1. D-1307 is labeled CRM only and is not in the buyer drivers or the match rate table.
2. The table counts 6 deals.
3. Price is the buyer driver on 1 lost deal (D-1306).
4. The flag report lists mismatches D-1302, D-1304, D-1309, and too few deals for Food service (1) and Pharmacy and lab (2).

---

## Lab 3: weekly feedback

### Week 1 (`m3-feedback-week-1.csv`), 24 items

| Tag | Accounts | Items |
| --- | --- | --- |
| P01 | 6 | 6 |
| P02 | 3 | 3 |
| P03 | 4 | 4 |
| P04 | 2 | 2 |
| P05 | 1 | 1 |
| P06 | 2 | 2 |
| P07 | 1 | 1 |
| P08 | 2 | 2 |
| P09 | 2 | 2 |
| No fit | 1 (A-26, invoice currency) | 1 |

### Week 2 (`m3-feedback-week-2.csv`), 32 items, after the fix

| Tag | Accounts week 1 | Accounts week 2 | Change | Items week 2 |
| --- | --- | --- | --- | --- |
| P01 | 6 | 7 | +1 | 11 (A-05 sent 5) |
| P02 | 3 | 3 | 0 | 3 |
| P03 | 4 | 2 | -2 | 2 |
| P04 | 2 | 3 | +1 | 3 |
| P05 | 1 | 2 | +1 | 2 |
| P06 | 2 | 1 | -1 | 1 |
| P07 | 1 | 0 | -1 | 0 |
| P08 | 2 | 1 | -1 | 1 |
| P09 | 2 | 3 | +1 | 3 |
| No fit | 1 | 5 | +4 | 6: F-1215 to F-1219 (4 accounts, remote inspector access) and F-1232 (A-10, Spanish app) |

**Flag report.**

1. "No fit" items across 3 or more accounts: F-1215, F-1216, F-1217, F-1218, F-1219 (A-08, A-17, A-22, A-31). New problem: inspectors want read-only remote access.
2. Personal data: F-1221 (name and phone number). Remove before the log keeps it.
3. No tag moves 3 or more accounts after the fix.

**Planted error.** With forced fit, P02 shows 7 accounts (+4) and gets a false "big move" flag. The "no fit" group holds 1 item or none. If counted by mentions, P01 shows +5.

**Pass condition (spec success check).** After the fix, the week 2 rerun shows the new problem in the "no fit" group with 4 accounts, and the flag report names it. P02 stays at 3 accounts. P01 shows 7 accounts, not 11. F-1221 is flagged.

### Second sample: `m3-check-sample.md` (week of 2026-11-16)

| Tag | Accounts | Items |
| --- | --- | --- |
| P01 | 2 (A-01, A-03) | 4 |
| P02, P04, P05, P08 | 1 each | 1 each |
| No fit | 4 | 4: F-1305, F-1306, F-1307 (A-04, A-09, A-15: send alarms to the refrigeration contractor's dispatch) and F-1312 (A-26, invoice email) |

**Pass condition.**

1. F-1305, F-1306 and F-1307 are "no fit", not P06. P06 covers who responds at night or on a weekend. These items ask for a repair job with the contractor, with no time of day.
2. The flag report names the contractor dispatch request across 3 accounts.
3. P01 counts 2 accounts, not 4.

### Stretch: `m3-stretch-survey-wave.csv` (remote inspector access)

| Segment | Respondents | Urgent (4 or 5) | Pervasive (most or all sites) | Would pay: yes, maybe, no |
| --- | --- | --- | --- | --- |
| Food service | 12 | 8 | 7 | 5, 4, 3 |
| Distribution | 4 | 0 | 0 | 0, 1, 3 |
| Pharmacy and lab | 4 | 0 | 0 | 0, 1, 3 |

Expected read: urgent and pervasive in Food service only. Willingness to pay is mixed. Next step is discovery interviews on price and packaging, not a build decision.

---

## Lab 4: alternatives map

### Result on `m4-evidence-pack.md` with `m4-alternatives-map.md`, after the fix

Counts are lost deals with a buyer interview. Periods compared: Q2 2026 vs Q3 2026.

| Entry | Q2 | Q3 | Q3 evidence | Change |
| --- | --- | --- | --- | --- |
| ALT-01 Rimecore | 2 | 2 | D-3101 / WL-3101 (Distribution), D-3105 / WL-3105 (Pharmacy and lab) | No change |
| ALT-02 Vantafrost | 1 | 1 | D-3102 / WL-3102 (Distribution) | No change |
| ALT-03 Controller alarms | 1 | 0 | none | Fading (low counts, PM judges) |
| ALT-04 Do nothing | 2 | 4 | D-3103, D-3106, D-3108 (Food service); D-3107 (Pharmacy and lab) | Growing |
| CRM only (separate) | 3 | 1 | D-3109 (Incumbent loggers, do nothing) | n/a |

**By segment, Q3.** Food service: do nothing 3, the top alternative. Pharmacy and lab: Rimecore 1, do nothing 1. Distribution: Rimecore 1, Vantafrost 1.

**Flag report.**

1. CRM competitor and buyer answer differ: D-3108 (CRM Rimecore, buyer kept the spreadsheet).
2. Do nothing is the top alternative in Food service. Pharmacy and lab is a tie (a flag here is fine).
3. Optional: "Incumbent loggers" (D-3109, CRM only) is not a map entry name. Mapping it to do nothing (CRM only) is correct.

**Planted error.** Before the fix, D-3108 counts for Rimecore. Rimecore shows Q2 2, Q3 3, "growing". Do nothing shows 3.

**Pass condition (spec success check).** D-3108 is under ALT-04 do nothing. Rimecore shows 2 in Q3 and "no change". The flag report lists the D-3108 mismatch. Every entry shows its source type. Each "growing" or "fading" label names Q2 2026 vs Q3 2026.

**Alternative to beat (debrief, Food service).** Do nothing: paper logs and spreadsheets (D-3103, D-3106, D-3108; Q2 D-2205). Next is the substitute, controller alarms (D-2209).

### Second sample: `m4-check-sample.md`

| Entry | October count | Deal |
| --- | --- | --- |
| Rimecore | 1 | D-4101 |
| Vantafrost | 1 | D-4105 |
| Controller alarms (substitute) | 1 | D-4102 |
| Do nothing | 1 | D-4103 |
| CRM only | 1 | D-4104 (Vantafrost) |

**Pass condition.**

1. D-4102 is under controller alarms, not Vantafrost.
2. The flag report lists D-4102 (CRM Vantafrost, buyer bought no sensor system).
3. D-4104 is shown as CRM only.

---

## Lab 5: stakeholder answers

Age limit: 18 months. R-2024-07 (2024-09-12) is over the limit. R-2026-03 (2026-05-20) is within it.

### Expected answers

| Question | What the answer says | Flags | Expected PM decision |
| --- | --- | --- | --- |
| Q1 VP Sales: pharmacy and lab losses on price? | Interviewed buyers do not name price. D-2211 and D-3107: budget or grant timing. D-3105: Rimecore's on-site calibration. Only D-2210 says price, and it is CRM only. What we do not know: price sensitivity in this segment. 3 interviewed losses in 2 quarters | Evidence below the bar | Change, then send. Soften to "the interviews we have do not point to price". Add the next pharmacy losses to the interview list |
| Q2 Head of Hardware: pharmacy and lab report pack? (planted) | Evidence points to calibration certificates with probe serial numbers (INS-08: I-107, I-108, I-113, Sep to Oct 2026; won D-2206; lost D-3105) and audit exports in the accreditor's or state board's format (I-108, Sep 2026). R-2024-07 is food service and over the age limit, so it is not used. What we do not know: which formats the boards and accreditors require, and whether a report pack changes deals | Old evidence, other segment. Report effort in Pharmacy and lab is below the bar (INS-02: 1 interview, I-108). Calibration certificates meet the bar (INS-08). Needs new research | Hold the roadmap commitment. Change the answer and start research |
| Q3 Support lead: night monitoring service for distribution? | Buyers disagree. INS-06: 2 interviews want own managers, 2 want a service (Sep to Oct 2026). R-2026-03 (May 2026, Distribution): 5 of 9 want a service option, 4 of 9 want own managers. No price tested | Sources disagree, needs new research | Change, then send as "split; test a priced offer before Support plans staff" |

**Status proposals.** Every status is labeled "proposal" until the PM decides.

Proposals are by segment, from the interview counts in Part 4 of `m4-evidence-pack.md`. A segment proposal needs the bar met inside that segment (same rule as Q4).

| Problem | Distribution | Food service | Pharmacy and lab |
| --- | --- | --- | --- |
| P01 Alert fatigue | Enough evidence to validate (4 interviews, 3 accounts, 2 PM-held) | Below the bar. Single source (I-105) | Below the bar. Emerging (I-107, I-113) |
| P02 Compliance report effort | Enough evidence to validate (3 interviews, 3 accounts, 2 PM-held) | Below the bar. Emerging (I-103, I-114) | Below the bar. Single source (I-108) |
| P03 Install and connectivity | No interviews | Enough evidence to validate (3 interviews, 2 accounts) | No interviews |
| P04 Sensor upkeep | Single source (I-112). Not enough | No interviews | No interviews |
| P05 Multi-site visibility | No interviews | Emerging (I-104, I-111). Not enough | No interviews |
| P06 After-hours response | Contradiction (2 against 2). Not enough | No interviews | No interviews |
| P07 Product loss cost | No interviews | Single source (I-114). Not enough | No interviews |
| P08 Calibration records | No interviews | No interviews | Enough evidence to validate (3 interviews, 3 accounts, 1 PM-held) |
| P09 Proof for the buyer's own customers | Single source (I-102). Not enough | No interviews | No interviews |
| P10 Inspector remote access | No interviews | No interviews. Discovery (feedback from 4 accounts) | No interviews |

Feedback counts do not change a proposal. They can add a "watch" note (for example P09: 3 accounts in week 2).

**Planted error.** The Q2 answer says "Buyers want a one-click inspection binder" and cites R-2024-07.

**Pass condition (spec success check).** The fixed Q2 answer names the study date and segment of every source. The flag report lists R-2024-07 as old evidence for another segment. The answer does not say "buyers want". Status proposals are given by segment and stay labeled as proposals until the PM decides.

### Second sample: Q4 in `m5-stakeholder-questions.md`

Q4 asks about alert noise in Food service and tempts "food service buyers want quiet hours".

Expected evidence: 1 interview (I-105, AI-moderated, Sep 2026). Feedback from 2 Food service accounts (A-09, A-28, Nov 2026); only A-09 asks for quiet hours (F-1207). Lost deal D-3108 (alerts every lunch rush, Sep 2026). R-2024-07 says alert noise was minor in 2024, but it is over the age limit.

**Pass condition.**

1. The answer does not say "food service buyers want quiet hours".
2. Each claim shows its date and segment.
3. The answer has a "what we do not know" line.
4. The flag report lists R-2024-07 as over the age limit, the evidence as below the bar, and the 2024 and 2026 sources as in disagreement.

---

## State files for the catch-up kits

| Kit | Case state to use |
| --- | --- |
| kit-m2 | Insight log after batch 2 (Lab 1 tables above) |
| kit-m3 | Adds the Q2 driver log (Part 1 Q2 rows of `m4-evidence-pack.md`) |
| kit-m4 | Adds P09 to the log. Insight log as in Part 4 of `m4-evidence-pack.md` |
| kit-m5 | Adds the map after lab 4 (Lab 4 table above) |
