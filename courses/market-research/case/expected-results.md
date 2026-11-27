**Fictional data for training.** Larkspan Systems case. Instructor only. Do not give this file to learners.

# Expected results, by lab

For each lab: the result the case records support, the second sample input and a concrete pass condition (PRD lab rule 7). Gate 2 locks these records and results.

## The model these results use (rework brief 2, decision 4)

There is no fixed bar. Priority is relative across the problem backlog.

1. The agent keeps a **problem backlog**. Each problem has an **evidence profile** of facts: interviews (count interviews, not quotes), accounts, segments, personas, source types, urgency with one quote, pervasiveness, willingness to pay clues and source dates.
2. Fact labels only: **single source** (1 interview, however many quotes), **AI-moderated only**, **one segment only**. Single-source problems stay in the backlog.
3. The agent **proposes a ranking with reasons**. The PM decides the order, what is a pattern and what goes to validation. The agent never writes "pattern" or "validated".
4. **Segment rule (decision 3, provisional A).** The agent ranks within a segment before it makes a claim about that segment. It never writes "<segment> buyers want" from 1 interview in that segment.
5. **The case PM's hand-off rules** (`company.md`): old evidence (over 18 months) to the flag report; a segment with no PM-held interview to the flag report; win/loss counts shown behind every driver statement; every "no fit" group to the flag report; date and segment on every source.

**How to read the pass conditions.** A ranking is a proposal, so the pass conditions do not ask for one exact order. They check the facts in each profile, the place of the planted item and the words the agent must not write. Where two problems have the same profile strength, any order with a stated reason passes. A learner who writes different hand-off rules is checked against their own rules.

**Debrief prompt (lab 1).** Use the Pragmatic test: can you predict that the next buyer of this persona will raise it? If the PM cannot, the PM may treat it as not yet a pattern. The PM, not the agent, makes that call.

---

## Lab 1: problem backlog

### Batch 1 (`m1-interviews-batch-1.md`), after the fix

8 interviews, 8 accounts. PM-held interviews are in bold.

| Problem | Interviews | Accounts | Segments (interviews) | Personas | Urgency (one quote) | Willingness to pay clues | Fact labels | Dates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01 Alert fatigue | 4: **I-101**, I-102, I-105, I-107 | 4 | Distribution 2, Food service 1, Pharmacy and lab 1 | Operations manager, quality manager, kitchen manager, pharmacy manager | "If it beeps forty times a night, it's not an alarm anymore, it's background noise." (I-101) | A failed door seal found about an hour late (I-101) | None | 2027-09-08 to 2027-09-16 |
| P02 Compliance report effort | 4: I-102, **I-103**, **I-106**, I-108 | 4 | Distribution 2, Food service 1, Pharmacy and lab 1 | Quality manager, facilities lead, VP operations, lab manager | "Pulling two years of reagent fridge records into the auditor's format took my team a week." (I-108) | Staff time in every interview: 2 days, 3 hours per site, 1 day, 1 week | None | 2027-09-09 to 2027-09-17 |
| P03 Install and connectivity | 2: **I-103**, I-105 | 2 | Food service 2 | Facilities lead, kitchen manager | "Two of our freezers lost signal every night until the contractor moved the hub." (I-103) | Two installer visits (I-105) | One segment only | 2027-09-10, 2027-09-14 |
| P06 After-hours response | 2: **I-101**, **I-106** | 2 | Distribution 2 | Operations manager, VP operations | "I want my own on-call manager to own the night alarms, not some outside call center that doesn't know our building." (I-101) | None. Both reject an outside service | One segment only | 2027-09-08, 2027-09-15 |
| P08 Calibration records | 2: I-107, I-108 | 2 | Pharmacy and lab 2 | Pharmacy manager, lab manager | "The auditor rejected one certificate because it didn't list the probe serial number." (I-108) | None | AI-moderated only. One segment only | 2027-09-16, 2027-09-17 |
| P05 Multi-site visibility (planted error) | 1: **I-104** (3 quotes) | 1 | Food service 1 | Director of operations | "If I can't compare all nine stores on one page by next spring, I'm not renewing, it's that simple." (I-104) | Renewal threat from 1 account | Single source. One segment only | 2027-09-11 |

**Expected proposed ranking, batch 1.**

| Proposed rank | Problem | Reason the agent should give |
| --- | --- | --- |
| 1 to 2 | P01, P02 (either order) | 4 interviews, 4 accounts, all 3 segments |
| 3 to 5 | P03, P06, P08 (any order) | 2 interviews, 2 accounts, 1 segment each. P08 is AI-moderated only |
| 6 | P05 | 1 interview, 1 account. High urgency, but no other buyer raised it |

**Why P05 (I-104) should not be near the top.**

1. Pervasiveness is the lowest in the backlog: 1 account of 8. No other batch 1 interview mentions P05.
2. The 3 quotes are one voice. Count interviews, not quotes.
3. Urgency is real but comes from one buyer. High urgency with no reach is the "noisy 20%" risk (workbook skill 1.1B).
4. The willingness to pay clue is one account's renewal threat. The PM may treat it as an account issue for Customer Success, not a market problem.
5. Inside Food service, 2 other interviews (I-103, I-105) do not raise P05. I-104 also says alerts and reports are "fine", so this buyer is an outlier on P01 and P02.
6. Batch 2 confirms it: I-111 says multi-site view is "not my top problem".

**By segment (segment rule).** If the agent says anything about Food service, it ranks within Food service first. P03 comes first (2 interviews). P01, P02 and P05 have 1 Food service interview each. The agent must not write "food service buyers want one view across stores".

**Batch 1 flag report.**

1. I-102 note fits no code: a distributor wants to send temperature proof to its own customers. PM decision: send to discovery. It becomes P09 in the tag list (lab 3).
2. Pharmacy and lab has no PM-held interview (I-107, I-108 are AI-moderated). Case PM's hand-off rule 2. PM decision: book a PM-held interview.
3. P05: all 3 quotes come from 1 interview (I-104). Proposed rank 6 of 6. This entry appears when the learner adds the lab 1 rule from `planted-errors.md`. PM decision: keep in the backlog, watch in batch 2.

**Before the fix (template brief v1).** Expect P05 in the top 3 of the proposed ranking, or first in Food service, with "3 quotes" and the renewal threat as the reason. That is the planted error.

### Batch 2 (`m1-interviews-batch-2.md`)

14 interviews, 11 accounts after batch 2.

| Problem | Interviews after batch 2 | New IDs | Accounts | Segments (interviews) | Fact labels | What changed |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | 7 (3 PM-held, 4 AI-moderated) | **I-109**, I-110, **I-113** | 6 | Distribution 4, Pharmacy and lab 2, Food service 1 | None | Growing |
| P02 | 6 (3 PM-held, 3 AI-moderated) | **I-109**, I-114 | 6 | Distribution 3, Food service 2, Pharmacy and lab 1 | None | Growing |
| P03 | 3 (2 PM-held) | **I-111** | 2 (Saltgrass Kitchens, Bramblefield Bistro) | Food service 3 | One segment only | Growing |
| P04 Sensor upkeep | 1 | **I-112** | 1 | Distribution 1 | Single source. One segment only | New |
| P05 | 2 (both PM-held) | **I-111** (low urgency: "not my top problem") | 2 | Food service 2 | One segment only | Second interview ranks it low |
| P06 | 4 (3 PM-held) | I-110, **I-112** | 3 | Distribution 4 | One segment only. Buyers disagree | I-110 and I-112 want a service to take night calls. I-101 and I-106 want own managers. I-106 and I-112 are the same account (Pellham Distribution). I-110 says "I'd pay" for a service |
| P07 Product loss cost | 1 | I-114 | 1 | Food service 1 | Single source. AI-moderated only. One segment only | New |
| P08 | 3 (1 PM-held) | **I-113** | 3 | Pharmacy and lab 3 | One segment only | AI-moderated only label clears |

**Expected proposed ranking, batch 2.**

| Proposed rank | Problem | Reason the agent should give |
| --- | --- | --- |
| 1 to 2 | P01, P02 (either order) | 6 or more interviews, 6 accounts, all 3 segments |
| 3 to 5 | P06, P08, P03 (any order) | 3 to 4 interviews, 2 to 3 accounts, 1 segment each. P06: buyers disagree |
| 6 to 8 | P05, P04, P07 (any order) | 1 to 2 interviews. P05: the second buyer ranks it low |

**By segment, after batch 2.**

| Segment | Problems by interviews (accounts) |
| --- | --- |
| Distribution (6 interviews, 4 accounts) | P01 4 (3), P06 4 (3, buyers disagree), P02 3 (3), P04 1 (1) |
| Food service (5 interviews, 4 accounts) | P03 3 (2), P02 2 (2), P05 2 (2), P01 1, P07 1 |
| Pharmacy and lab (3 interviews, 3 accounts) | P08 3 (3), P01 2 (2), P02 1 |

**Batch 2 flag report.** (1) P06: buyers disagree, including 2 people at the same account. (2) New single-source problems P04 and P07, kept in the backlog. (3) P05: the new interview gives low urgency. The Pharmacy and lab flag clears (I-113 is PM-held).

**Case PM decision after batch 2.** The PM orders the backlog: P01, P02, P08, P03, P06, P05, P04, P07. The PM moves P06 below P08 and P03 because the buyers disagree, so it is a research question first. The PM names P01 and P02 the top problems in Distribution, P03 in Food service and P08 in Pharmacy and lab. This is the PM decision column in Part 4 of `m4-evidence-pack.md`.

**Debrief check, instructor only.** The backlog updates. Every problem shows its evidence profile and fact labels. The flag report lists the P06 disagreement. The agent proposes a ranking with a reason for each rank. P05 ranks below P01, P02, P03, P06 and P08. The agent writes "pattern" or "validated" for no problem.

### Second sample: `m1-check-sample.md`

Run on an empty backlog. 4 interviews, 4 accounts.

| Problem | Interviews | Accounts | Segments | Fact labels |
| --- | --- | --- | --- | --- |
| P01 Alert fatigue | 2 (**I-202**, **I-203**) | 2 | Distribution 1, Food service 1 | None |
| P04 Sensor upkeep | 2 (**I-203**, I-204) | 2 | Food service 1, Pharmacy and lab 1 | None |
| P07 Product loss cost | 1 (**I-201**, 3 quotes) | 1 | Distribution 1 | Single source. One segment only |

**Pass condition.**

1. P07 shows 1 interview, not 3. It has the labels "single source" and "one segment only".
2. The proposed ranking puts P07 below P01 and P04. The reason names the interview count, not the quote count.
3. The agent writes "pattern" or "validated" for no problem.
4. The flag report says Pharmacy and lab has no PM-held interview (I-204). If the learner added the lab 1 rule, it also lists P07 (all 3 quotes from I-201).
5. Every quote is word for word in the sample.

### Stretch: `m1-stretch-applicants.md`

Criteria are in `m1-stretch-applicants.md`. The study starts in December 2027.

| Result | Applicant | Reason |
| --- | --- | --- |
| Pass | AP-01, AP-04, AP-06 | Meet all 5 criteria |
| Pass | AP-11 | Meets all 5 criteria. Uses a competitor (Rimecore), which is allowed |
| Fail | AP-02 | Criterion 2 and 3: uses only, 1 site |
| Fail | AP-03 | Criterion 5: interviewed 2027-09, inside 6 months |
| Fail | AP-05 | Criterion 4: works for a reseller |
| Fail | AP-09 | Criterion 1: segment out of scope (hardware retail) |
| Edge case to the PM | AP-07 | Criterion 2: "Influences" only. Is that "strongly influences"? Criterion 3 passes (11 walk-ins) |
| Edge case to the PM | AP-08 | Criterion 3: 2 warehouses and no cold-room count. Criterion 5 passes (last interview 2027-05, 7 months before) |
| Edge case to the PM | AP-10 | Criterion 2: runs the purchase but does not choose |
| Edge case to the PM | AP-12 | Criterion 2: "Influences" only |


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
3. Counts by segment (case PM's hand-off rule 3). Interviewed deals: Distribution 4, Food service 3, Pharmacy and lab 2. Interviewed lost deals: Distribution 3, Food service 2, Pharmacy and lab 1. No driver repeats across the lost deals of any segment, so the agent states no top loss driver for a segment.
4. D-2214 has no interview (buyer did not attend). CRM only.

**Planted error.** With the leak, price shows 2 to 4 buyer deals and looks like the top driver.

**Pass condition (debrief check, instructor only).** The match rate table counts only the 9 interviewed deals. No CRM-only deal (including D-2214) is in the buyer driver findings. The flag report lists the 5 mismatched deals.

### Second sample: `m2-check-sample.md`

10 deals. Interviewed: D-1301, D-1302, D-1304, D-1306, D-1308, D-1309. CRM only: D-1303, D-1305, D-1307 (declined, sales note "Price"), D-1310.

| Outcome | Interviewed | Match | Match rate |
| --- | --- | --- | --- |
| Won | 2 | 2 | 100% |
| Lost | 4 | 1 (D-1306) | 25% |
| Total | 6 | 3 | 50% |

**Pass condition.**

1. D-1307 is labeled CRM only and is not in the buyer drivers or the match rate table.
2. The table counts 6 deals.
3. Price is the buyer driver on 1 lost deal (D-1306).
4. The flag report lists mismatches D-1302, D-1304 and D-1309. Every driver statement shows its count of interviewed deals by segment: Distribution 3, Food service 1, Pharmacy and lab 2. The agent names no top driver for a segment.

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

1. "No fit" group (case PM's hand-off rule 4): F-1215, F-1216, F-1217, F-1218, F-1219, 5 items from 4 accounts (A-08, A-17, A-22, A-31). New problem: inspectors want read-only remote access.
2. "No fit" item F-1232 (A-10, Spanish app), 1 account.
3. Personal data: F-1221 (name and phone number). Remove before the backlog keeps it.

The agent reports every change in accounts. After the fix, changes run from -2 (P03) to +1. The agent does not call any one-week change a trend. The PM reads the changes.

**Planted error.** With forced fit, P02 shows 7 accounts (+4). It becomes the largest change of the week, and the summary calls it the top mover. The "no fit" group holds 1 item or none. If counted by mentions, P01 shows +5.

**Pass condition (debrief check, instructor only).** After the fix, the week 2 rerun shows the new problem in the "no fit" group with 4 accounts, and the flag report names it. P02 stays at 3 accounts. P01 shows 7 accounts, not 11. F-1221 is flagged.

### Second sample: `m3-check-sample.md` (week of 2027-11-16)

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

Counts are lost deals with a buyer interview. Periods compared: Q2 2027 vs Q3 2027.

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

**Pass condition (debrief check, instructor only).** D-3108 is under ALT-04 do nothing. Rimecore shows 2 in Q3 and "no change". The flag report lists the D-3108 mismatch. Every entry shows its source type. Each "growing" or "fading" label names Q2 2027 vs Q3 2027.

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

Case PM's hand-off rule 1: evidence older than 18 months goes to the flag report. R-2025-07 (2025-09-12) is over the limit. R-2027-03 (2027-05-20) is within it.

The agent reads the problem backlog (Part 4 of `m4-evidence-pack.md`), the driver log, the alternatives map after lab 4 and `m5-past-reports.md`.

### Expected answers

| Question | What the answer says | Flags | Expected PM decision |
| --- | --- | --- | --- |
| Q1 VP Sales: pharmacy and lab losses on price? | Interviewed buyers do not name price. D-2211 and D-3107: budget or grant timing. D-3105: Rimecore's on-site calibration. Only D-2210 says price, and it is CRM only. Count: 3 interviewed Pharmacy and lab losses in 2 quarters (Q2 and Q3 2027). What we do not know: price sensitivity in this segment | Small count, stated in the answer (hand-off rule 3). D-2210 is CRM only | Change, then send. Soften to "the 3 interviews we have do not point to price". Add the next pharmacy losses to the interview list |
| Q2 Head of Hardware: pharmacy and lab report pack? (planted) | Evidence points to 2 needs. (1) Calibration certificates with probe serial numbers: P08, 3 interviews, 3 accounts (I-107, I-108, I-113, Sep to Oct 2027); won D-2206; lost D-3105. (2) Audit exports in the accreditor's or state board's format: P02 in Pharmacy and lab, 1 interview (I-108, AI-moderated, Sep 2027) and feedback from 2 accounts (A-14, A-29, Nov 2027). R-2025-07 is Food service and over the age limit, so it is not used. What we do not know: which formats the boards and accreditors require, and whether a report pack changes deals | Old evidence for another segment (R-2025-07). Report effort in Pharmacy and lab is 1 interview: single source in this segment, AI-moderated only. Needs new research | Hold the roadmap commitment. Change the answer and start research |
| Q3 Support lead: night monitoring service for distribution? | Buyers disagree. P06: 4 interviews, 3 accounts, Distribution only (Sep to Oct 2027). 2 want own managers (I-101, I-106), 2 want a service (I-110, I-112). I-106 and I-112 are the same account. R-2027-03 (May 2027, Distribution): 5 of 9 want a service option, 4 of 9 want own managers. I-110 says "I'd pay"; no price was tested | Sources disagree. Needs new research | Change, then send as "split; test a priced offer before Support plans staff" |
| Q5 FDP PM (internal): hub signal history view? | Customer evidence for hub signal loss is P03. 3 interviews (I-103, I-111 PM-held; I-105 AI-moderated), 2 accounts (Saltgrass Kitchens, Bramblefield Bistro), all Food service, Sep to Oct 2027. Feedback from 2 Food service accounts in the week of 2027-11-09 (A-04, A-30), down 2 from the week before. 1 Distribution lost deal: D-2203 (Q2 2027), the hub dropped sensors in blast freezers and the buyer chose Rimecore. No Pharmacy and lab evidence. P03 is the agent's proposed rank 1 in Food service and the PM's rank 4 overall. What we do not know: how many sites in the whole fleet lose hub signal. FDP device-health data can answer this. The agent has no FDP data | One segment only. "Many customer sites" is not supported across segments. The FDP backlog order is the internal PM's decision | Send. Add one line: pull hub drop counts by segment from FDP before placing the request |

**Q5 is not a planted error** (decision 9). It gives the internal PM a real question and tests the segment rule a second time. It adds no case data and changes no lab 1 to 4 count.

**Q5 pass condition (debrief check, instructor only).**

1. The answer does not say "hubs lose signal at many customer sites" or name all segments.
2. It names Food service as the only segment with interviews, and shows D-2203 with its segment and quarter.
3. It has a "what we do not know" line that points to FDP fleet data.
4. It gives evidence and leaves the FDP backlog order to the FDP PM.

### Ranking and validation proposals by segment

The agent ranks within each segment first (segment rule). Then it proposes which problems go to validation. Every line is labeled "proposal". The PM decides. The agent never writes "validated" or "pattern".

Inside a segment, problems with the same evidence strength can come in any order if the agent gives a reason.

Each table lists every problem with evidence in that segment: interviews, feedback or deals. A problem with no interview in the segment shows "Not ranked".

**Distribution** (6 interviews, 4 accounts)

| Proposed rank | Problem | Evidence in this segment | Proposal |
| --- | --- | --- | --- |
| 1 | P01 Alert fatigue | 4 interviews, 3 accounts, 2 PM-held. Feedback 4 accounts. Lost D-2207, D-3101 on alert accuracy; won D-3104 | Propose for validation |
| 2 | P02 Compliance report effort | 3 interviews, 3 accounts, 2 PM-held. Feedback 1 account. Won D-2201; lost D-2212, D-3102 on report fit | Propose for validation |
| 3 | P06 After-hours response | 4 interviews, 3 accounts. Feedback 1 account. Buyers disagree 2 to 2. R-2027-03 split 5 to 4 | Propose research (priced offer test), not validation |
| 4 to 5 | P04 Sensor upkeep, P09 Proof for own customers | 1 interview each. Feedback: P04 3 accounts, P09 1 account. P09 is AI-moderated only | Keep in backlog, watch |
| Not ranked | P03 Install and connectivity | 0 interviews. No feedback. 1 lost deal (D-2203) | Note only. Ask about hubs in the next Distribution interviews |
| Not ranked | P05 Multi-site visibility | 0 interviews. Feedback 1 account (A-33) | Keep in backlog, watch |

**Food service** (5 interviews, 4 accounts)

| Proposed rank | Problem | Evidence in this segment | Proposal |
| --- | --- | --- | --- |
| 1 | P03 Install and connectivity | 3 interviews, 2 accounts, 2 PM-held. Feedback 2 accounts | Propose for validation |
| 2 to 4 | P02, P05, P01 (any order with reasons) | P02: 2 interviews, 2 accounts, no feedback. P05: 2 interviews, 2 accounts, the second buyer ranks it low, feedback 1 account. P01: 1 interview (AI-moderated), feedback 2 accounts, lost D-3108 on alert accuracy | Keep in backlog, watch. Add P01 and P02 to the next Food service interview guide |
| 5 | P07 Product loss cost | 1 interview, AI-moderated only. No feedback this week | Keep in backlog |
| Not ranked | P10 Inspector remote access | 0 interviews. Feedback 4 accounts | Discovery (PM decided in lab 3) |

**Pharmacy and lab** (3 interviews, 3 accounts)

| Proposed rank | Problem | Evidence in this segment | Proposal |
| --- | --- | --- | --- |
| 1 | P08 Calibration records | 3 interviews, 3 accounts, 1 PM-held. Feedback 1 account. Won D-2206; lost D-3105 | Propose for validation |
| 2 | P01 Alert fatigue | 2 interviews, 2 accounts, 1 PM-held. Feedback 1 account | Keep in backlog, watch |
| 3 | P02 Compliance report effort | 1 interview (AI-moderated). Feedback 2 accounts | Keep in backlog. Research question (see Q2) |
| Not ranked | P09 Proof for own customers | 0 interviews. Feedback 2 accounts (A-34, A-35) | Keep in backlog, watch |

**Expected PM decision.** Send to validation: P01 and P02 (Distribution), P03 (Food service), P08 (Pharmacy and lab). Research: P06. Discovery: P10. Keep and watch: the rest. The case PM chose not to send a problem to validation on feedback counts alone. The PM added a "watch" note instead (for example P04 and P09: 3 accounts each in week 2).

**Planted error.** The Q2 answer says "Buyers want a one-click inspection binder" and cites R-2025-07.

**Pass condition (debrief check, instructor only).** The fixed Q2 answer names the study date and segment of every source. The flag report lists R-2025-07 as old evidence for another segment. The answer does not say "buyers want". The agent ranks within each segment before any segment claim. Ranking and validation proposals stay labeled as proposals until the PM decides.

### Second sample: Q4 in `m5-stakeholder-questions.md`

Q4 asks about alert noise in Food service and tempts "food service buyers want quiet hours".

Expected evidence: P01 has 1 Food service interview (I-105, AI-moderated, 2027-09-14). Feedback from 2 Food service accounts (A-09, A-28, week of 2027-11-09). Lost deal D-3108 (alerts every lunch rush, interview 2027-09-15). Inside Food service, P01 is not in the top proposed rank (see the Food service table). No interview asks for quiet hours. R-2025-07 says alert noise was minor in 2025, but it is over the age limit.

If the learner also pasted the week 2 feedback, the agent may add that 1 account asks for quiet hours (A-09, F-1207). That is still 1 account.

**Pass condition.**

1. The answer does not say "food service buyers want quiet hours".
2. Each claim shows its date and segment.
3. The answer has a "what we do not know" line.
4. The flag report lists R-2025-07 as over the age limit, the Food service interview evidence as 1 interview (single source in this segment, AI-moderated only), and the 2025 and 2027 sources as in disagreement.

---

## State files for the catch-up kits

| Kit | Case state to use |
| --- | --- |
| kit-m2 | Problem backlog after batch 2 (lab 1 tables above), with the case PM's order |
| kit-m3 | Adds the Q2 driver log (Part 1 Q2 rows of `m4-evidence-pack.md`) |
| kit-m4 | Adds P09 and P10 and the week 2 feedback counts. Problem backlog as in Part 4 of `m4-evidence-pack.md` |
| kit-m5 | Adds the map after lab 4 (lab 4 table above) |
