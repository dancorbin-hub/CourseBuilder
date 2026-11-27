**Fictional data for training.** Larkspan Systems case. All companies, people and numbers are invented.

# Alternatives map (Larkspan Systems)

Knowledge file for the Market Evidence Agent, alternatives map job. Current map: end of Q3 2027. Built from the Q2 and Q3 driver log after the lab 4 fix.

## Alternative types

| Type | Meaning |
| --- | --- |
| Competitor | The buyer bought a named competitor |
| Substitute | The buyer bought something outside the category that covers part of the need |
| Workaround | The buyer built or changed a process to cover the need |
| Do nothing | The buyer bought nothing new and kept the current method (paper logs, spreadsheet, old loggers) or stopped the project |

## Map, end of Q3 2027

Counts are lost deals. Buyer interview counts and CRM-only counts are kept apart. Periods compared: Q2 2027 vs Q3 2027.

| Entry | Alternative | Type | Q2, buyer interview | Q3, buyer interview | Q3 segments (buyer interview) | Buyer reason it was chosen, Q3 | Q3 evidence rows | Change |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ALT-01 | Rimecore | Competitor | 2 | 2 | Distribution 1, Pharmacy and lab 1 | Door delay setting cut false alarms (D3). On-site calibration (D6) | D-3101 / WL-3101; D-3105 / WL-3105 | No change (2 to 2) |
| ALT-02 | Vantafrost | Competitor | 1 | 1 | Distribution 1 | Audit pack in the customer's format (D4) | D-3102 / WL-3102 | No change (1 to 1) |
| ALT-03 | Alarms in a new refrigeration controller | Substitute | 1 | 0 | none | none in Q3 | none | Fading (1 to 0). Low counts, the PM judges |
| ALT-04 | Kept current method (paper logs, spreadsheet, old loggers) | Do nothing | 2 | 4 | Food service 3, Pharmacy and lab 1 | Paper log is free for small sites (D1). Spend froze (D7). Grant did not come (D7). Trial alerts (D3) | D-3103 / WL-3103; D-3106 / WL-3106; D-3107 / WL-3107; D-3108 / WL-3108 | Growing (2 to 4) |

Q2 evidence rows (lab 2): ALT-01 D-2203, D-2207. ALT-02 D-2212. ALT-03 D-2209. ALT-04 D-2205, D-2211.

CRM only, kept apart: Q2 3 (D-2204 and D-2214 Rimecore, D-2210 Vantafrost). Q3 1 (D-3109, "Incumbent loggers", do nothing).

## By segment, Q3 2027 (buyer interview)

| Segment | Alternatives |
| --- | --- |
| Food service | Do nothing 3 (top) |
| Pharmacy and lab | Rimecore 1, do nothing 1 |
| Distribution | Rimecore 1, Vantafrost 1 |

## Flag decisions (PM)

| Flag | Deal or entry | PM decision |
| --- | --- | --- |
| CRM competitor (Rimecore) and the buyer's answer (kept the spreadsheet) differ | D-3108 | Accept the buyer's answer. Tell sales ops to fix the CRM field |
| Do nothing is the top alternative in Food service | ALT-04 | Do nothing is the alternative to beat in Food service. Next is the substitute, controller alarms (D-2209) |
| Pharmacy and lab: Rimecore and do nothing tie | ALT-01, ALT-04 | Your decision (the case gives none) |
| "Incumbent loggers" is not a map entry name | D-3109 | Your decision. Mapped to do nothing, CRM only |

## "What moved" summary format

| Entry | Previous period count | This period count | Periods compared | Change (new, growing, fading, no change) |
| --- | --- | --- | --- | --- |

## Flag report format

| Flag ID | Deal or entry | Why the agent stopped | Evidence rows | PM decision |
| --- | --- | --- | --- | --- |
