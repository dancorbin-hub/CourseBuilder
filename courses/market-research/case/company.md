**Fictional data for training.** Larkspan Systems, its people, customers, competitors and all numbers are invented. Any match with a real company or person is chance.

# Case company: Larkspan Systems

Use this case only when you cannot use your own work. One company serves the whole course.

## The company

| Item | Detail |
| --- | --- |
| What it does | Makes wireless temperature sensors (hardware) and the cloud software that watches them (SaaS) |
| Size | About 420 employees. Revenue about USD 68 million |
| Business model | Hardware sold once per sensor and hub. Software sold as a subscription per site per year |
| Channels | Direct sales for distribution and pharmacy. Resellers (refrigeration contractors) for most food service sites |
| Product teams | 3 external product teams and 1 internal platform team (see below) |

## Products

| Product | Type | What it does |
| --- | --- | --- |
| Larkspan Probe | Hardware | Wireless sensor for walk-in coolers, freezers and medicine fridges. Battery life about 3 years |
| Larkspan Hub | Hardware | Gateway that sends sensor data to the cloud over Wi-Fi or cellular |
| Larkspan Tag | Hardware | Single-use logger that rides with a shipment |
| Larkspan Cloud | Software | Live alerts, dashboards and compliance reports (food safety logs, calibration records, audit trail) |
| Fleet Data Platform (FDP) | Internal software | Internal tool that shows device health, firmware status and install status. Used by Support, Install, Customer Success and Finance |

## External and internal product management

- **External PMs** own Probe, Hub, Tag and Cloud. They research buyers, run win/loss and keep the alternatives map.
- **Internal PM** owns the Fleet Data Platform. Internal teams are the customers. They send requests through an internal intake form. They also pass on customer feedback they hear. The internal PM uses the external problem backlog to rank internal requests.

## Segments

| Segment | Typical buyer | Typical user | Notes |
| --- | --- | --- | --- |
| Distribution | Operations or quality manager at a regional food distributor or cold storage warehouse | Warehouse shift lead | Large sites, many freezers, night shifts |
| Food service | Director of operations at a restaurant group or grocery chain | Kitchen or store manager | Many small sites. Bought through a refrigeration contractor (reseller) |
| Pharmacy and lab | Pharmacy manager or lab manager | Pharmacy or lab technician | Medicine fridges and reagent storage. Calibration records matter. No patient data in the product |

## Roles you meet in the case data

Roles only. The case uses no personal names.

- Head of Product (decides which problems go to the 2028 plan)
- PM, Larkspan Cloud
- PM, Fleet Data Platform (internal PM). Asks one question in lab 5
- VP Sales, Head of Hardware, Support lead (stakeholders who ask questions)
- Win/loss interviewer (product team or an outside firm, never sales)

## Alternatives buyers choose

| Alternative | Type |
| --- | --- |
| Rimecore | Named competitor (sensors and cloud) |
| Vantafrost | Named competitor (cloud reports, lower hardware price) |
| Alarms built into a new refrigeration controller | Substitute |
| Keep paper logs, a spreadsheet or old USB data loggers | Do nothing |

## Current market questions (November 2027)

1. Which market problems should go forward to the 2028 plan, and for which segment?
2. Why do we lose deals? Sales says price. Is that what buyers say?
3. Which new problems show up in weekly feedback?
4. Which alternative must we beat in each segment? Is Rimecore growing?
5. What can we tell stakeholders now, and what needs new research?

## Interview source labels

Each interview says who ran it.

- **PM-held**: a Larkspan PM ran the interview.
- **AI-moderated**: an AI interview tool ran the interview. A PM read the transcript.

## How Larkspan PMs set priority

There is no fixed bar. Priority is relative: the PM judges each problem against the other problems in the problem backlog.

1. The agent keeps a **problem backlog**. One row per market problem.
2. Each problem has an **evidence profile**. The agent reports facts only:
   - interviews (count interviews, not quotes), accounts, segments and personas
   - source type: PM-held, AI-moderated, win/loss, feedback item or past report
   - urgency (with one quote), pervasiveness (how many accounts and segments) and willingness to pay clues
   - source dates
3. The agent adds fact labels: **single source** (1 interview, however many quotes), **AI-moderated only** and **one segment only**. These are facts, not verdicts. A single-source problem stays in the backlog for trend tracking.
4. The agent **proposes a ranking with a reason for each rank**. The PM decides the order, what is a pattern and what goes to validation. The agent never writes "pattern" or "validated".
5. **Segment rule.** The agent ranks within a segment before it makes a claim about that segment. It never writes "food service buyers want" from 1 interview in that segment.

## The case PM's hand-off rules

These are the rules that the Larkspan Head of Product wrote for this study. They tell the agent when to stop and send an item to the PM. They are one PM's choices, shown as examples. On your own work, write your own.

1. **Old evidence.** Send any source older than 18 months to the flag report.
2. **PM contact.** Send any segment with no PM-held interview to the flag report.
3. **Win/loss.** Show the count of interviewed deals behind every driver statement. Send a deal to the flag report when the CRM reason and the buyer differ.
4. **Weekly feedback.** Report the change in accounts for every tag. Send every "no fit" group to the flag report, with its item IDs and accounts.
5. **Stakeholder answers.** Show the date and segment of every source. Add a "what we do not know" line.

## Files by module

Each lab adds 2 files to the agent: the job card (from the catch-up kit) and 1 case knowledge file. Then you upload or paste the run files and the check file in chat. You can paste a run file as text instead of an upload.

In Copilot, use the `.txt` copy of each knowledge file (see `README.md`).

| Module | Add to the agent | Run files (upload or paste in chat) | Check file (second sample) | Files this lab | Stretch (optional) |
| --- | --- | --- | --- | --- | --- |
| 1 | Problem backlog job card, empty problem backlog (kit), `m1-code-book.md` | `m1-interviews-batch-1.md`, `m1-interviews-batch-2.md` | `m1-check-sample.md` | 6 | `m1-stretch-applicants.md` |
| 2 | Win/loss job card, `m2-driver-code-book.md` | `m2-crm-export-q2.csv`, `m2-winloss-notes-q2.md` | `m2-check-sample.md` | 5 | none |
| 3 | Weekly feedback job card, `m3-tag-list.md` | `m3-feedback-week-1.csv`, `m3-feedback-week-2.csv` | `m3-check-sample.md` | 5 | `m3-stretch-survey-wave.csv` |
| 4 | Alternatives map job card, `m4-alternatives-map.md` | `m4-evidence-pack.md` (holds the driver log, CRM export, interviews and problem backlog) | `m4-check-sample.md` | 4 | none |
| 5 | Stakeholder answer job card, `m5-past-reports.md` | `m5-stakeholder-questions.md`: Q1, Q2 and Q5 core, Q3 optional (the backlog and logs are already in the agent) | Q4 in `m5-stakeholder-questions.md` | 3 | none |

"Files this lab" counts the agent files, run files and check file. It does not count the stretch file. The agent ends the course with 12 knowledge files: 5 job cards, 5 case knowledge files and 2 logs (problem backlog, driver log). The course budget is 13.

Instructor files (do not give to learners): `planted-errors.md`, `expected-results.md`.
