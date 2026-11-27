**Fictional data for training.** Larkspan Systems case. All companies, people, quotes and numbers are invented. No real personal data.

# Evidence pack for lab 4 (Larkspan Systems)

One file with four parts. Upload it, or paste it.

1. Driver log, Q2 and Q3 2027 (from the win/loss job)
2. CRM export, Q3 2027 decided deals (with the competitor field)
3. Win/loss interview excerpts, Q3 2027
4. Problem backlog, after lab 3

---

## Part 1. Driver log, Q2 and Q3 2027

Q2 rows are the checked rows from lab 2. Q3 rows were coded quickly before quarter close. Two Q3 rows have no alternative recorded.

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
| D-3102 | Q3 | Lost | Distribution | interview | D4 Compliance report fit | | "Their audit pack came out in our customer's format with no rework." | WL-3102 | Price | no |
| D-3103 | Q3 | Lost | Food service | interview | D1 Price and value | Paper logs (do nothing) | "For three cafes the paper log on the cooler door is free and the inspector accepts it." | WL-3103 | Price | yes |
| D-3104 | Q3 | Won | Distribution | interview | D3 Alert accuracy | n/a | "Your door delay setting meant my night lead finally trusted the alarms." | WL-3104 | Alert accuracy | yes |
| D-3105 | Q3 | Lost | Pharmacy and lab | interview | D6 Calibration and certificates | Rimecore | "Rimecore calibrates on site twice a year, so the probes never leave the pharmacy." | WL-3105 | Calibration | yes |
| D-3106 | Q3 | Lost | Food service | interview | D7 Timing and budget cycle | Spreadsheet (do nothing) | "We froze all new spend after the second quarter, so the spreadsheet stays for now." | WL-3106 | Timing | yes |
| D-3107 | Q3 | Lost | Pharmacy and lab | interview | D7 Timing and budget cycle | Budget freeze (do nothing) | "The grant that would have paid for it did not come through this cycle." | WL-3107 | Timing | yes |
| D-3108 | Q3 | Lost | Food service | interview | D3 Alert accuracy | | "Rimecore's demo had fewer alerts, I'll give them that." | WL-3108 | Price | no |
| D-3109 | Q3 | Lost | Distribution | CRM only | n/a | n/a (CRM competitor: Incumbent loggers) | none | none | Price | n/a |
| D-3110 | Q3 | Won | Food service | interview | D8 Reseller and install support | n/a | "The contractor set up all four sites in a week and showed every manager the app." | WL-3110 | Reseller support | yes |

---

## Part 2. CRM export, Q3 2027 decided deals

```csv
deal_id,account,segment,channel,sites,amount_usd,stage,close_date,crm_reason,crm_competitor,owner
D-3101,Granary Wharf Distribution,Distribution,Direct,2,58900,Closed Lost,2027-07-09,Price,Rimecore,REP-03
D-3102,Beckton Cold Chain,Distribution,Direct,3,64200,Closed Lost,2027-07-16,Price,Vantafrost,REP-09
D-3103,Tansy Row Kitchens,Food service,Reseller,3,10400,Closed Lost,2027-07-23,Price,None,REP-11
D-3104,Ashgrove Freight Cold,Distribution,Direct,2,51700,Closed Won,2027-07-30,Alert accuracy,Rimecore,REP-03
D-3105,Mallow Court Pharmacy,Pharmacy and lab,Direct,4,24800,Closed Lost,2027-08-06,Calibration,Rimecore,REP-05
D-3106,Fernhollow Cafes,Food service,Reseller,5,16900,Closed Lost,2027-08-13,Timing,None,REP-07
D-3107,Kittering Research Labs,Pharmacy and lab,Direct,1,18300,Closed Lost,2027-08-20,Timing,None,REP-05
D-3108,Hobnail Burger Co,Food service,Reseller,6,21600,Closed Lost,2027-08-27,Price,Rimecore,REP-07
D-3109,Duncairn Logistics,Distribution,Direct,3,47500,Closed Lost,2027-09-03,Price,Incumbent loggers,REP-09
D-3110,Quillon Street Eateries,Food service,Reseller,4,15200,Closed Won,2027-09-10,Reseller support,None,REP-11
```

---

## Part 3. Win/loss interview excerpts, Q3 2027

Run by the product team or an outside firm. Sales did not run any interview. Quotes are word for word.

**WL-3101 (D-3101, Granary Wharf Distribution, lost).** Interview 2027-07-28. Operations manager. "Rimecore let us set a delay per door, and that killed most of the false alarms." Price was about the same.

**WL-3102 (D-3102, Beckton Cold Chain, lost).** Interview 2027-08-04. Quality manager. We went with Vantafrost. "Their audit pack came out in our customer's format with no rework." Your price was fine.

**WL-3103 (D-3103, Tansy Row Kitchens, lost).** Interview 2027-08-11. Owner. "For three cafes the paper log on the cooler door is free and the inspector accepts it." We did not look at anyone else.

**WL-3104 (D-3104, Ashgrove Freight Cold, won).** Interview 2027-08-18. Operations manager. We also trialed Rimecore. "Your door delay setting meant my night lead finally trusted the alarms."

**WL-3105 (D-3105, Mallow Court Pharmacy, lost).** Interview 2027-08-25. Pharmacy manager. We chose Rimecore. "Rimecore calibrates on site twice a year, so the probes never leave the pharmacy."

**WL-3106 (D-3106, Fernhollow Cafes, lost).** Interview 2027-09-01. Director of operations. "We froze all new spend after the second quarter, so the spreadsheet stays for now." We will look again in spring.

**WL-3107 (D-3107, Kittering Research Labs, lost).** Interview 2027-09-08. Lab manager. "The grant that would have paid for it did not come through this cycle." We kept our current loggers.

**WL-3108 (D-3108, Hobnail Burger Co, lost).** Interview 2027-09-15. Director of operations. We looked at Rimecore twice and trialed you at two sites. "Your trial sent alerts every lunch rush, and my managers gave up on it." "Rimecore's demo had fewer alerts, I'll give them that." But we did not buy Rimecore either. "In the end we didn't buy anything; we kept the spreadsheet and the clipboard on the walk-in door." We may try again when the alert problem is fixed.

**WL-3110 (D-3110, Quillon Street Eateries, won).** Interview 2027-09-29. Facilities lead. "The contractor set up all four sites in a week and showed every manager the app."

---

## Part 4. Problem backlog, after lab 3

One row per market problem. Each row is the evidence profile. Interviews count interviews, not quotes. Feedback counts unique accounts in the week of 2027-11-09. The agent proposes a rank with a reason. The PM decides the order. The agent never writes "pattern" or "validated".

| Problem | Problem statement | Interviews (PM-held; AI-moderated) | Accounts (interviews) | Segments (interviews) | Personas | Feedback accounts, week 2, by segment | Urgency (quote) | Willingness to pay clues | Fact labels | Source dates | Agent proposed rank (reason) | PM decision | Last change |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | Alert noise makes staff ignore alerts | 7 (PM-held: I-101, I-109, I-113; AI-moderated: I-102, I-105, I-107, I-110) | 6 | Distribution 4, Pharmacy and lab 2, Food service 1 | Operations manager, quality manager, night operations lead, kitchen manager, pharmacy manager | 7 (Distribution: A-01, A-03, A-05, A-27; Food service: A-09, A-28; Pharmacy and lab: A-12) | "If it beeps forty times a night, it's not an alarm anymore, it's background noise." (I-101) | A failed door seal was found about an hour late (I-101). No buyer named a price | None | Interviews 2027-09-08 to 2027-10-13. Feedback 2027-11-09 to 2027-11-13 | 1. Most interviews and accounts. All 3 segments | PM rank 1. Top problem in Distribution | Week 2: +1 account |
| P02 | Building compliance reports takes hours to days | 6 (PM-held: I-103, I-106, I-109; AI-moderated: I-102, I-108, I-114) | 6 | Distribution 3, Food service 2, Pharmacy and lab 1 | Quality manager, facilities lead, VP operations, lab manager, store manager | 3 (Distribution: A-02; Pharmacy and lab: A-14, A-29) | "Pulling two years of reagent fridge records into the auditor's format took my team a week." (I-108) | Staff time: 2 days per audit (I-102), 3 hours per site per inspection (I-103), 1 day per month (I-106), 1 week (I-108). No price named | None | Interviews 2027-09-09 to 2027-10-14. Feedback 2027-11-09 to 2027-11-12 | 2. Same reach as P01. Staff time cost in every interview | PM rank 2. Top problem in Distribution | No change |
| P06 | Who owns night alarms. Buyers disagree | 4 (PM-held: I-101, I-106, I-112; AI-moderated: I-110) | 3 | Distribution 4 | Operations manager, VP operations, night operations lead | 1 (Distribution: A-16) | "We tried having supervisors own night alarms, and it failed; we want a service to take that call for us." (I-112) | "I'd pay for a monitoring service that takes the 2 a.m. call and only wakes me if it's real." (I-110) | One segment only. Buyers disagree: I-101 and I-106 want own managers, I-110 and I-112 want a service. I-106 and I-112 are the same account | Interviews 2027-09-08 to 2027-10-09. Feedback 2027-11-11 | 3. 4 interviews, 3 accounts. Buyers disagree on the answer | PM rank 5. Needs research before any direction | Week 2: -1 account |
| P08 | Auditors need calibration certificates with probe serials | 3 (PM-held: I-113; AI-moderated: I-107, I-108) | 3 | Pharmacy and lab 3 | Pharmacy manager, lab manager | 1 (Pharmacy and lab: A-23) | "Every inspection starts with the calibration certificates, and if one is missing we get a finding." (I-113) | A missing certificate causes an inspection finding (I-113). No price named | One segment only | Interviews 2027-09-16 to 2027-10-13. Feedback 2027-11-10 | 4. Every Pharmacy and lab interview raises it. 3 accounts | PM rank 3. Top problem in Pharmacy and lab | Week 2: -1 account |
| P03 | Hubs lose signal in steel walk-ins and freezers | 3 (PM-held: I-103, I-111; AI-moderated: I-105) | 2 | Food service 3 | Facilities lead, regional manager, kitchen manager | 2 (Food service: A-04, A-30) | "Two of our freezers lost signal every night until the contractor moved the hub." (I-103) | Repeat installer visits (I-105). No price named | One segment only | Interviews 2027-09-10 to 2027-10-08. Feedback 2027-11-09 to 2027-11-12 | 5. 3 interviews, 2 accounts, 1 segment | PM rank 4. Top problem in Food service | Week 2: -2 accounts |
| P05 | No single view across sites | 2 (PM-held: I-104, I-111) | 2 | Food service 2 | Director of operations, regional manager | 2 (Food service: A-13; Distribution: A-33) | "I have nine stores and nine logins, and I can't see one screen that tells me which store is in trouble right now." (I-104). I-111: "it's not my top problem" | Renewal threat from 1 account (I-104) | One segment only (interviews). 3 of its 4 quotes are from I-104 | Interviews 2027-09-11 and 2027-10-08. Feedback 2027-11-10 to 2027-11-12 | 6. 2 interviews. The second buyer ranks it low | PM rank 6. Keep, watch | Week 2: +1 account |
| P04 | Battery changes take staff time | 1 (PM-held: I-112) | 1 | Distribution 1 | Operations manager | 3 (Distribution: A-06, A-11, A-32) | "Changing batteries on 200 sensors is a part-time job for someone." (I-112) | 1 account asks about a battery swap service (A-11, feedback) | Single source. One segment only | Interview 2027-10-09. Feedback 2027-11-10 to 2027-11-13 | 7. 1 interview. Feedback from 3 accounts | PM rank 7. Keep, watch | Week 2: +1 account |
| P09 | Buyers want to show temperature proof to their own customers | 1 (AI-moderated: I-102) | 1 | Distribution 1 | Quality manager | 3 (Distribution: A-25; Pharmacy and lab: A-34, A-35) | "I'd love to send my grocery customer a link that proves the load stayed cold, without giving them our whole account." (I-102) | None. Today the buyer emails screenshots (I-102) | Single source. AI-moderated only. One segment only (interviews) | Interview 2027-09-09. Feedback 2027-11-09 to 2027-11-13 | 8. 1 interview. Feedback from 3 accounts in 2 segments | PM rank 8. Keep, watch | Week 2: +1 account |
| P07 | Spoiled stock costs thousands per event | 1 (AI-moderated: I-114) | 1 | Food service 1 | Store manager | 0 | "One bad night in the dairy cooler cost us about eleven thousand dollars in product." (I-114) | Cost of one event: about USD 11,000 (I-114) | Single source. AI-moderated only. One segment only | Interview 2027-10-14 | 9. 1 interview. No feedback this week | PM rank 9. Keep | Week 2: -1 account |
| P10 | Inspectors want read-only remote access to records | 0 | 0 | None | None yet | 4 (Food service: A-08, A-17, A-22, A-31) | "The county inspector wants to log in and see our cooler records herself before she visits." (F-1215) | None yet | One segment only (feedback) | Feedback 2027-11-10 to 2027-11-13 | Not ranked. 0 interviews | Sent to discovery | Week 2: new |
