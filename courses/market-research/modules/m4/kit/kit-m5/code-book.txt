**Fictional data for training.** Larkspan Systems case. All companies, people and numbers are invented.

# Code book: market problems (Larkspan Systems)

Knowledge file for the Market Evidence Agent, problem backlog job. Version 1, September 2027.

## Codes

| Code | Problem | Definition | Example signal |
| --- | --- | --- | --- |
| P01 | Alert fatigue | Too many alarms, or false alarms, so staff stop reacting | "We mute it" |
| P02 | Compliance report effort | Work to turn temperature records into inspection and audit reports | Hours on a binder before an inspection |
| P03 | Install and connectivity | Sensors or hubs that do not connect or are hard to install on site | Signal lost inside a freezer |
| P04 | Sensor upkeep | Battery changes, replacements and other sensor upkeep | Staff time to swap batteries |
| P05 | Multi-site visibility | No single view across sites, so leaders cannot compare or act | Calls to each store for status |
| P06 | After-hours response | Who responds to a night or weekend alarm, and how fast | A 2 a.m. alarm that no one answers |
| P07 | Product loss cost | Money lost when stock spoils after a temperature problem | Value of a lost freezer load |
| P08 | Calibration records | Proof of sensor calibration, with certificates an auditor accepts | Certificate requests from a lab auditor |

## Segments

Distribution, Food service, Pharmacy and lab.

## Personas (roles)

Operations manager, quality manager, facilities lead, director of operations, kitchen or store manager, pharmacy manager, lab manager.

## Problem backlog format (empty)

The agent writes the backlog in this format. One row per market problem. The row is the evidence profile. Facts only.

| Problem (code) | Problem (one sentence) | Interviews (IDs, PM-held or AI-moderated) | Accounts | Segments (interviews per segment) | Personas | Quotes (word for word, interview ID) | Other sources (win/loss, feedback, past report) | Urgency (one quote, interview ID) | Pervasiveness (accounts and segments) | Willingness to pay clues | Fact labels (single source, AI-moderated only, one segment only) | Source dates | Change (new, growing, fading, no change) | First seen | Last updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Proposed ranking format

The agent proposes. The PM decides the order.

| Proposed rank | Problem (code) | Scope (all segments or one segment) | Reason (from the evidence profile) |
| --- | --- | --- | --- |

## "What changed" summary format

3 to 6 bullets. Each names a problem code and what changed since the last batch.

## Flag report format

| Flag ID | Item | Why the agent stopped | Source interview IDs | PM decision (keep, fix, send to discovery) |
| --- | --- | --- | --- | --- |
