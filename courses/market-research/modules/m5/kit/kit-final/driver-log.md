**Fictional data for training.** Larkspan Systems case. All companies, people, quotes and numbers are invented. No real personal data.

# Driver log

Log file for the Market Evidence Agent, win/loss job. State after module 4: Q2 2027 decided deals (14 deals, 9 with a buyer interview, 5 CRM only) and Q3 2027 decided deals (10 deals, 9 with a buyer interview, 1 CRM only). The format is in the driver code book. Facts and counts only. The agent never writes "pattern" or "validated".

Last updated: after lab 4. Q3 rows come from the lab 4 evidence pack. The alternative chosen for D-3102 and D-3108 is read from the buyer interview (WL-3102, WL-3108), not the CRM field.

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
| D-2211 | Q2 | Lost | Pharmacy and lab | interview | D7 Timing and budget cycle | Budget freeze (do nothing) | "Our capital review got pushed to 2028, so nothing new got bought this year." | WL-2211 | Timing | yes |
| D-2212 | Q2 | Lost | Distribution | interview | D4 Compliance report fit | Vantafrost | "Vantafrost's audit export matched our auditor's template exactly, and yours needed a day of rework every month." | WL-2212 | Price | no |
| D-2213 | Q2 | Won | Food service | CRM only | n/a | n/a | none | none | Price | n/a |
| D-2214 | Q2 | Lost | Distribution | CRM only | n/a | n/a (CRM competitor: Rimecore) | none | none (buyer did not attend) | Price | n/a |
| D-3101 | Q3 | Lost | Distribution | interview | D3 Alert accuracy | Rimecore | "Rimecore let us set a delay per door, and that killed most of the false alarms." | WL-3101 | Price | no |
| D-3102 | Q3 | Lost | Distribution | interview | D4 Compliance report fit | Vantafrost | "Their audit pack came out in our customer's format with no rework." | WL-3102 | Price | no |
| D-3103 | Q3 | Lost | Food service | interview | D1 Price and value | Paper logs (do nothing) | "For three cafes the paper log on the cooler door is free and the inspector accepts it." | WL-3103 | Price | yes |
| D-3104 | Q3 | Won | Distribution | interview | D3 Alert accuracy | n/a | "Your door delay setting meant my night lead finally trusted the alarms." | WL-3104 | Alert accuracy | yes |
| D-3105 | Q3 | Lost | Pharmacy and lab | interview | D6 Calibration and certificates | Rimecore | "Rimecore calibrates on site twice a year, so the probes never leave the pharmacy." | WL-3105 | Calibration | yes |
| D-3106 | Q3 | Lost | Food service | interview | D7 Timing and budget cycle | Spreadsheet (do nothing) | "We froze all new spend after the second quarter, so the spreadsheet stays for now." | WL-3106 | Timing | yes |
| D-3107 | Q3 | Lost | Pharmacy and lab | interview | D7 Timing and budget cycle | Budget freeze (do nothing) | "The grant that would have paid for it did not come through this cycle." | WL-3107 | Timing | yes |
| D-3108 | Q3 | Lost | Food service | interview | D3 Alert accuracy | Spreadsheet and clipboard (do nothing) | "Rimecore's demo had fewer alerts, I'll give them that." | WL-3108 | Price | no |
| D-3109 | Q3 | Lost | Distribution | CRM only | n/a | n/a (CRM competitor: Incumbent loggers) | none | none | Price | n/a |
| D-3110 | Q3 | Won | Food service | interview | D8 Reseller and install support | n/a | "The contractor set up all four sites in a week and showed every manager the app." | WL-3110 | Reseller support | yes |

## Match rate table, Q2 2027 (deals with an interview only)

| Outcome | Deals with an interview | CRM reason matches buyer primary driver | Match rate |
| --- | --- | --- | --- |
| Won | 3 | 2 (D-2201, D-2206) | 67% |
| Lost | 6 | 2 (D-2205, D-2211) | 33% |
| Total | 9 | 4 | 44% |

## Driver counts, Q2 2027 (interviewed deals only)

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

The match rate table and the driver counts cover Q2 only. Lab 4 added the Q3 rows and did not recount them.

## Flag report (Q3 rows, lab 4)

| Flag | Deals | PM decision |
| --- | --- | --- |
| CRM competitor (Rimecore) and the buyer's answer (kept the spreadsheet) differ. Counted as do nothing | D-3108 | Accept the buyer's answer. Tell sales ops to fix the CRM field |
