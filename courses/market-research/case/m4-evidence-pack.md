**Fictional data for training.** Larkspan Systems case. All companies, people, quotes and numbers are invented. No real personal data.

# Evidence pack for lab 4 (Larkspan Systems)

One file with four parts. Upload it, or paste it.

1. Driver log, Q2 and Q3 2026 (from the win/loss job)
2. CRM export, Q3 2026 decided deals (with the competitor field)
3. Win/loss interview excerpts, Q3 2026
4. Insight log, after lab 3

---

## Part 1. Driver log, Q2 and Q3 2026

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
| D-2211 | Q2 | Lost | Pharmacy and lab | interview | D7 Timing and budget cycle | Budget freeze (do nothing) | "Our capital review got pushed to 2027, so nothing new got bought this year." | WL-2211 | Timing | yes |
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

## Part 2. CRM export, Q3 2026 decided deals

```csv
deal_id,account,segment,channel,sites,amount_usd,stage,close_date,crm_reason,crm_competitor,owner
D-3101,Granary Wharf Distribution,Distribution,Direct,2,58900,Closed Lost,2026-07-09,Price,Rimecore,REP-03
D-3102,Beckton Cold Chain,Distribution,Direct,3,64200,Closed Lost,2026-07-16,Price,Vantafrost,REP-09
D-3103,Tansy Row Kitchens,Food service,Reseller,3,10400,Closed Lost,2026-07-23,Price,None,REP-11
D-3104,Ashgrove Freight Cold,Distribution,Direct,2,51700,Closed Won,2026-07-30,Alert accuracy,Rimecore,REP-03
D-3105,Mallow Court Pharmacy,Pharmacy and lab,Direct,4,24800,Closed Lost,2026-08-06,Calibration,Rimecore,REP-05
D-3106,Fernhollow Cafes,Food service,Reseller,5,16900,Closed Lost,2026-08-13,Timing,None,REP-07
D-3107,Kittering Research Labs,Pharmacy and lab,Direct,1,18300,Closed Lost,2026-08-20,Timing,None,REP-05
D-3108,Hobnail Burger Co,Food service,Reseller,6,21600,Closed Lost,2026-08-27,Price,Rimecore,REP-07
D-3109,Duncairn Logistics,Distribution,Direct,3,47500,Closed Lost,2026-09-03,Price,Incumbent loggers,REP-09
D-3110,Quillon Street Eateries,Food service,Reseller,4,15200,Closed Won,2026-09-10,Reseller support,None,REP-11
```

---

## Part 3. Win/loss interview excerpts, Q3 2026

Run by the product team or an outside firm. Sales did not run any interview. Quotes are word for word.

**WL-3101 (D-3101, Granary Wharf Distribution, lost).** Interview 2026-07-28. Operations manager. "Rimecore let us set a delay per door, and that killed most of the false alarms." Price was about the same.

**WL-3102 (D-3102, Beckton Cold Chain, lost).** Interview 2026-08-04. Quality manager. We went with Vantafrost. "Their audit pack came out in our customer's format with no rework." Your price was fine.

**WL-3103 (D-3103, Tansy Row Kitchens, lost).** Interview 2026-08-11. Owner. "For three cafes the paper log on the cooler door is free and the inspector accepts it." We did not look at anyone else.

**WL-3104 (D-3104, Ashgrove Freight Cold, won).** Interview 2026-08-18. Operations manager. We also trialed Rimecore. "Your door delay setting meant my night lead finally trusted the alarms."

**WL-3105 (D-3105, Mallow Court Pharmacy, lost).** Interview 2026-08-25. Pharmacy manager. We chose Rimecore. "Rimecore calibrates on site twice a year, so the probes never leave the pharmacy."

**WL-3106 (D-3106, Fernhollow Cafes, lost).** Interview 2026-09-01. Director of operations. "We froze all new spend after the second quarter, so the spreadsheet stays for now." We will look again in spring.

**WL-3107 (D-3107, Kittering Research Labs, lost).** Interview 2026-09-08. Lab manager. "The grant that would have paid for it did not come through this cycle." We kept our current loggers.

**WL-3108 (D-3108, Hobnail Burger Co, lost).** Interview 2026-09-15. Director of operations. We looked at Rimecore twice and trialed you at two sites. "Your trial sent alerts every lunch rush, and my managers gave up on it." "Rimecore's demo had fewer alerts, I'll give them that." But we did not buy Rimecore either. "In the end we didn't buy anything; we kept the spreadsheet and the clipboard on the walk-in door." We may try again when the alert problem is fixed.

**WL-3110 (D-3110, Quillon Street Eateries, won).** Interview 2026-09-29. Facilities lead. "The contractor set up all four sites in a week and showed every manager the app."

---

## Part 4. Insight log, after lab 3

Frequency counts interviews, not quotes. Feedback counts unique accounts. Status uses the case PM's bar.

| Insight ID | Code | Insight | Segments | Interviews (PM-held, AI-moderated) | Feedback accounts, week 2 | Intensity (quote) | Status | Last change |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INS-01 | P01 | Alert noise makes staff ignore alerts | All three | 7 (I-101, I-109, I-113 PM-held; I-102, I-105, I-107, I-110 AI-moderated) | 7 | "If it beeps forty times a night, it's not an alarm anymore, it's background noise." (I-101) | Pattern | Week 2: +1 account |
| INS-02 | P02 | Building compliance reports takes hours to days | All three | 6 (I-103, I-106, I-109 PM-held; I-102, I-108, I-114 AI-moderated) | 3 | "Pulling two years of reagent fridge records into the auditor's format took my team a week." (I-108) | Pattern | No change |
| INS-03 | P03 | Hubs lose signal in steel walk-ins and freezers | Food service | 3 (I-103, I-111 PM-held; I-105 AI-moderated), 2 accounts | 2 | "Two of our freezers lost signal every night until the contractor moved the hub." (I-103) | Pattern (Food service) | Week 2: -2 accounts |
| INS-04 | P04 | Battery changes take staff time | Distribution | 1 (I-112 PM-held) | 3 | "Changing batteries on 200 sensors is a part-time job for someone." (I-112) | Single source | Week 2: +1 account |
| INS-05 | P05 | No single view across sites | Food service | 2 (I-104, I-111 PM-held) | 2 | "I have nine stores and nine logins, and I can't see one screen that tells me which store is in trouble right now." (I-104) | Emerging | Week 2: +1 account |
| INS-06 | P06 | Who owns night alarms. Buyers disagree | Distribution | 4 (I-101, I-106, I-112 PM-held; I-110 AI-moderated). 2 want own managers, 2 want a service | 1 | "We tried having supervisors own night alarms, and it failed; we want a service to take that call for us." (I-112) | Contradiction open | Batch 2 contradiction |
| INS-07 | P07 | Spoiled stock costs thousands per event | Food service | 1 (I-114 AI-moderated) | 0 | "One bad night in the dairy cooler cost us about eleven thousand dollars in product." (I-114) | Single source | No change |
| INS-08 | P08 | Auditors need calibration certificates with probe serials | Pharmacy and lab | 3 (I-113 PM-held; I-107, I-108 AI-moderated) | 1 | "Every inspection starts with the calibration certificates, and if one is missing we get a finding." (I-113) | Pattern (Pharmacy and lab) | No change |
| INS-09 | P09 | Buyers want to show temperature proof to their own customers | Distribution, Pharmacy and lab | 1 (I-102 AI-moderated) | 3 | "I'd love to send my grocery customer a link that proves the load stayed cold, without giving them our whole account." (I-102) | Single source | Week 2: +1 account |
| INS-10 | P10 | Inspectors want read-only remote access to records | Food service | 0 | 4 | "The county inspector wants to log in and see our cooler records herself before she visits." (F-1215) | New. Sent to discovery | Week 2: new |
