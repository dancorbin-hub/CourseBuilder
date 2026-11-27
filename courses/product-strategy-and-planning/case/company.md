**Fictional data for training.** Larkspan Systems, its people, customers, suppliers and all numbers are invented. Any match with a real company or person is chance. No real personal data and no health data.

# Case company: Larkspan Systems (strategy and planning case)

Use this case only when you cannot use your own work. One company serves the whole course. It is the same company as the Market Research course case. This version adds strategy, OKRs, KPIs, programs and teams.

## The company

| Item | Detail |
| --- | --- |
| What it does | Makes wireless temperature sensors (hardware) and the cloud software that watches them (SaaS) |
| Size | About 420 employees. Revenue about USD 68 million |
| Business model | Hardware sold once per sensor and hub. Software sold as a subscription per site per year |
| Active paid sites | 9,840 (30 September 2027) |
| Channels | Direct sales for distribution and pharmacy. Resellers (refrigeration contractors) for most food service sites |
| Product teams | 3 external product teams and 1 internal platform team |
| Case date | Late November 2027. Planning for 2028 |

## Products

| Product | Type | What it does |
| --- | --- | --- |
| Larkspan Probe | Hardware | Wireless sensor for walk-in coolers, freezers and medicine fridges |
| Larkspan Hub | Hardware | Gateway that sends sensor data to the cloud over Wi-Fi or cellular. Runs firmware |
| Larkspan Probe X | Hardware | New Probe with a built-in cellular radio. No hub needed. Limited release since June 2027 on bridge tooling. The hard tooling commit decision is due 15 December 2027 |
| Larkspan Tag | Hardware | Single-use logger that rides with a shipment. Tag 2 is in development |
| Larkspan Cloud | Software | Live alerts, dashboards and compliance reports (food safety logs, calibration records, audit trail) |
| Fleet Data Platform (FDP) | Internal software | Shows device health, firmware status and install status. Used by Support, Install, Customer Success and Finance |

## External and internal product management

- **External PMs** own Probe, Hub, Probe X, Tag and Cloud. Roles: PM, Probe and Hub. PM, Larkspan Cloud.
- **Internal PM** (PM, Fleet Data Platform) owns the Fleet Data Platform. Internal teams are the customers. They send requests through an internal intake form.
- The Head of Product decides the quarterly plan. A Delivery lead owns the release plan.

## Teams that several programs share

| Team | Size (FTE) | Notes |
| --- | --- | --- |
| Firmware team | 12 | Writes firmware for Hub, Probe X and Tag. Shared by hardware programs |
| Cloud team | 18 | Builds Larkspan Cloud and the interfaces other programs need |
| Hardware design team | 8 | Probe X and Tag hardware |
| Test lab | 6 | Environmental and radio tests for every hardware program |
| Data platform team | 5 | Builds the Fleet Data Platform |

## The five programs in the quarterly pack

| Id | Program | Type |
| --- | --- | --- |
| P-01 | Probe X cellular | Hardware |
| P-02 | Hub firmware | Hardware and software |
| P-03 | Cloud compliance reports | Software |
| P-04 | Tag 2 | Hardware |
| P-05 | Fleet Data Platform | Internal platform |

## Segments

| Segment | Typical buyer | Typical user | Notes |
| --- | --- | --- | --- |
| Distribution | Operations or quality manager at a regional food distributor or cold storage warehouse | Warehouse shift lead | Large sites, many freezers, night shifts |
| Food service | Director of operations at a restaurant group or grocery chain | Kitchen or store manager | Many small sites. Bought through a reseller |
| Pharmacy and lab | Pharmacy manager or lab manager | Pharmacy or lab technician | Medicine fridges and reagent storage. Calibration records matter. No patient data in the product |

## Roles in the case data

Roles only. The case uses no personal names.

- Head of Product (decides the 2028 plan)
- PM, Probe and Hub. PM, Larkspan Cloud. PM, Fleet Data Platform (internal PM)
- Delivery lead (owns the release plan)
- Head of Hardware, VP Sales, Support lead, Install lead, Finance lead

## Alternatives buyers choose

| Alternative | Type |
| --- | --- |
| Rimecore | Named competitor (sensors and cloud) |
| Vantafrost | Named competitor (cloud reports, lower hardware price) |
| Alarms built into a new refrigeration controller | Substitute |
| Paper logs, a spreadsheet or old USB data loggers | Do nothing |

## Strategy, OKRs and KPIs

The file `strategy-okrs-kpis.md` holds the 2028 strategy overview, the 2028 H1 OKRs and the KPIs with targets. The agent reads that file. It never writes or changes strategy.

## Terms used in this case

| Term | Meaning |
| --- | --- |
| Problem backlog | Where a team tracks unsolved market problems and the evidence for each. It feeds the product backlog |
| Evidence order | A rank in the problem backlog by amount of market evidence (records, then accounts). Equal evidence shares a rank. It is one input. It is not a priority. The PM also weighs strategy, capacity and dependencies |
| Validated problem backlog | The problems the PM has validated by the PM's own rule, with evidence |
| Market | All buyers who have the problem the product solves |
| Market segment | A group inside the market with shared needs that the team can reach |
| Evaluator adoption | The share of the segment expected to evaluate a solution of this kind |
| Projected share | The share of evaluators the team expects to win. It comes only from Larkspan internal data |
| Roadmap | Direction: outcome themes and timeframes. Not a promise |
| Release plan | The promise: dated commitments the Delivery lead owns |

## Current planning questions (November 2027)

1. Is the planned work for next quarter consistent with the 2028 strategy and OKRs?
2. Which requests in this batch do we answer yes, no or later, and why?
3. Does the Probe X business case still hold before the hard tooling commit?
4. Does every roadmap item have its own evidence? What does a change to the roadmap displace?
5. Are the outcomes the business case promised on track, or only the outputs?

## The case PM's choices

These are the choices one Larkspan PM made for this case. They are examples. They are not a standard. On your own work, write your own.

| Lab | Choice | The case PM's setting |
| --- | --- | --- |
| 1 | What "over capacity" means | More than 100 percent of a team's capacity, summed across all programs in the quarter |
| 1 | What a good link looks like | The link names what the work does and a key result id, not only a tag |
| 2 | How to match a request to a problem | Match on the problem statement and the user, not on feature words |
| 3 | Age of evidence | Older than 180 days at the run date goes to the flag report |
| 3 | Low, base and high values | Set by the PM in the business case sheet |
| 4 | Validated rule for a roadmap item | The item's own evidence shows 3 or more accounts and 2 or more source types in the last 12 months |
| 4 | Confidential terms | The list in `confidential-terms-list.md` |
| 5 | Outcome or output | An outcome is a customer or business result named in the business case or a key result. An output counts work done or product moved |
| 5 | Off-target range | More than 15 percent below target, in 2 months in a row |
| 5 | No change | Less than 1 point of change in 2 months |

## Files by module

Each lab adds files to the agent. Knowledge files stay in the agent. Run files go into chat. The agent ends the course with 16 knowledge files: 1 core instruction file, 5 job cards and 10 case files. Details are in `README.md`.
