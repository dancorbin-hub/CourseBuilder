**Fictional data for training.** Larkspan Systems case. All companies, people and numbers are invented.

# Driver code book: win/loss (Larkspan Systems)

Knowledge file for the Market Evidence Agent, win/loss job. Version 1, July 2026.

## Decision drivers

| Code | Driver | Definition |
| --- | --- | --- |
| D1 | Price and value | Total cost, or cost per site, compared with the value the buyer expects |
| D2 | Install and connectivity | Whether the sensors and hub connect and install well at the buyer's sites, in the trial or pilot |
| D3 | Alert accuracy | How many alerts are real. Alert noise in a trial |
| D4 | Compliance report fit | Whether reports match what the buyer's inspector or auditor wants |
| D5 | Multi-site visibility | One view across many sites |
| D6 | Calibration and certificates | Calibration service and certificates an auditor accepts |
| D7 | Timing and budget cycle | Budget freeze, budget moved, or the project was delayed |
| D8 | Reseller and install support | How well the reseller or installer supported the buyer |
| D9 | Relationship and trust | Trust in the vendor or the sales team |
| D10 | Current equipment is good enough | The buyer's current equipment already covers the need |

## Alternatives (what the buyer chose instead)

| Alternative | Type |
| --- | --- |
| Rimecore | Competitor |
| Vantafrost | Competitor |
| Paper logs or spreadsheet (no purchase) | Do nothing |
| Budget freeze, no purchase | Do nothing |

## Deal source labels

- **interview**: a buyer win/loss interview exists for the deal.
- **CRM only**: no buyer interview. Only the CRM record exists.

## Program rules

- Add each win/loss interview to the driver log as soon as it is coded. Do not wait for a minimum number of deals.
- Someone outside sales runs the interviews.
- Interview 2 to 4 weeks after the decision.

## Driver log format

| Deal ID | Outcome | Segment | Deal source | Primary driver | Secondary drivers | Alternative chosen | Buyer quote (word for word) | Interview ID | CRM reason | CRM and buyer match (yes, no, n/a) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Match rate table format

| Outcome | Deals with an interview | CRM reason matches buyer primary driver | Match rate |
| --- | --- | --- | --- |
