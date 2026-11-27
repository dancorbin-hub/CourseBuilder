**Fictional data for training.** Larkspan Systems case. All companies, people, quotes and numbers are invented. No real personal data.

# Driver log

Log file for the Market Evidence Agent, win/loss job. State after module 2: Q2 2026 decided deals (14 deals, 9 with a buyer interview, 5 CRM only). The format is in the driver code book. Facts and counts only. The agent never writes "pattern" or "validated".

Last updated: after the Q2 2026 batch (decisions 2026-04-08 to 2026-06-29).

## Driver log

| Deal ID | Period | Outcome | Segment | Deal source | Primary driver | Alternative chosen | Buyer quote (word for word) | Interview ID | CRM reason | CRM and buyer match |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D-2201 | Q2 | Won | Distribution | interview | D4 Compliance report fit | n/a | "Your audit report was the only one that matched what our customers' auditors ask for, line for line." | WL-2201 | Compliance reports | yes |
| D-2202 | Q2 | Won | Food service | interview | D8 Reseller and install support | n/a | "The contractor had all six sites live in one visit each, and Vantafrost wanted a separate installer." | WL-2202 | Price | no |
| D-2203 | Q2 | Lost | Distribution | interview | D2 Install and connectivity | Rimecore | "Your hub kept dropping the sensors in our two blast freezers, and Rimecore's didn't drop once in three weeks." | WL-2203 | Price | no |
| D-2204 | Q2 | Lost | Food service | CRM only | n/a | n/a (CRM competitor: Rimecore) | none | none | Price | n/a |
| D-2205 | Q2 | Lost | Food service | interview | D1 Price and value | Paper logs (do nothing) | "Four site subscriptions was more than we spend on the coolers' service contract, so we stayed with paper logs." | WL-2205 | Price | yes |
| D-2206 | Q2 | Won | Pharmacy and lab | interview | D6 Calibration and certificates | n/a | "You include the calibration certificates with the probe serial number on them, so my auditor stops asking." | WL-2206 | Calibration certificates | yes |
| D-2207 | Q2 | Lost | Distribution | interview | D3 Alert accuracy | Rimecore | "We got over forty alerts in the first week of the trial, and most were dock doors during loading." | WL-2207 | Feature gap: multi-site dashboard | no |
| D-2208 | Q2 | Won | Distribution | CRM only | n/a | n/a | none | none | Relationship | n/a |
| D-2209 | Q2 | Lost | Food service | interview | D10 Current equipment is good enough | Alarms in a new refrigeration controller | "The new controllers already text us when a walk-in goes warm, so it's good enough for now." | WL-2209 | Price | no |
| D-2210 | Q2 | Lost | Pharmacy and lab | CRM only | n/a | n/a (CRM competitor: Vantafrost) | none | none | Price | n/a |
| D-2211 | Q2 | Lost | Pharmacy and lab | interview | D7 Timing and budget cycle | Budget freeze (do nothing) | "Our capital review got pushed to 2027, so nothing new got bought this year." | WL-2211 | Timing | yes |
| D-2212 | Q2 | Lost | Distribution | interview | D4 Compliance report fit | Vantafrost | "Vantafrost's audit export matched our auditor's template exactly, and yours needed a day of rework every month." | WL-2212 | Price | no |
| D-2213 | Q2 | Won | Food service | CRM only | n/a | n/a | none | none | Price | n/a |
| D-2214 | Q2 | Lost | Distribution | CRM only | n/a | n/a (CRM competitor: Rimecore) | none | none (buyer did not attend) | Price | n/a |

## Match rate table (deals with an interview only)

| Outcome | Deals with an interview | CRM reason matches buyer primary driver | Match rate |
| --- | --- | --- | --- |
| Won | 3 | 2 (D-2201, D-2206) | 67% |
| Lost | 6 | 2 (D-2205, D-2211) | 33% |
| Total | 9 | 4 | 44% |

## Driver counts (interviewed deals only)

| Driver | Interviewed deals | Won | Lost | Accounts | Segments |
| --- | --- | --- | --- | --- | --- |
| D4 Compliance report fit | 2 (D-2201, D-2212) | 1 | 1 | 2 | Distribution 2 |
| D1 Price and value | 1 (D-2205) | 0 | 1 | 1 | Food service 1 |
| D2 Install and connectivity | 1 (D-2203) | 0 | 1 | 1 | Distribution 1 |
| D3 Alert accuracy | 1 (D-2207) | 0 | 1 | 1 | Distribution 1 |
| D6 Calibration and certificates | 1 (D-2206) | 1 | 0 | 1 | Pharmacy and lab 1 |
| D7 Timing and budget cycle | 1 (D-2211) | 0 | 1 | 1 | Pharmacy and lab 1 |
| D8 Reseller and install support | 1 (D-2202) | 1 | 0 | 1 | Food service 1 |
| D10 Current equipment is good enough | 1 (D-2209) | 0 | 1 | 1 | Food service 1 |

Interviewed deals by segment: Distribution 4, Food service 3, Pharmacy and lab 2. No driver repeats across the lost deals of any segment.

CRM says "Price" on 7 of 9 lost deals. Interviewed buyers name price on 1 of 6 lost deals.

## Flag report (Q2 batch)

| Flag | Deals | PM decision |
| --- | --- | --- |
| CRM reason and buyer reason differ | D-2202, D-2203, D-2207, D-2209, D-2212 | From your lab 2 record sheet |
| Alternative not in the code book | D-2209 (alarms in a new refrigeration controller) | From your lab 2 record sheet |
| No buyer interview (buyer did not attend). CRM only | D-2214 | From your lab 2 record sheet |
