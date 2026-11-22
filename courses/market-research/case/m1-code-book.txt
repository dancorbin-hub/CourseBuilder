**Fictional data for training.** Larkspan Systems case. All companies, people and numbers are invented.

# Code book: market problems (Larkspan Systems)

Knowledge file for the Market Evidence Agent, insight log job. Version 1, September 2026.

## Codes

| Code | Problem | Definition | Example signal |
| --- | --- | --- | --- |
| P01 | Alert fatigue | Too many alarms, or alarms that are not real problems, so staff stop reacting | "We mute it" |
| P02 | Compliance report effort | Time and work to turn temperature records into reports for inspections and audits | Hours spent on a binder before an inspection |
| P03 | Install and connectivity | Sensors or hubs that do not connect, or are hard to install, at the site | Signal lost inside a freezer |
| P04 | Sensor upkeep | Battery changes, replacements and other upkeep work on the sensors | Staff time to swap batteries |
| P05 | Multi-site visibility | No single view across many sites, so leaders cannot compare or act across sites | Calls to each store to ask for status |
| P06 | After-hours response | Who responds to an alarm at night or on a weekend, and how fast | A 2 a.m. alarm that no one answers |
| P07 | Product loss cost | Money lost when stock spoils because of a temperature problem | Value of a lost freezer load |
| P08 | Calibration records | Proof that sensors are calibrated, with certificates an auditor accepts | Certificate requests from a lab auditor |

## Segments

Distribution, Food service, Pharmacy and lab.

## Personas (roles)

Operations manager, quality manager, facilities lead, director of operations, kitchen or store manager, pharmacy manager, lab manager.

## Insight log format (empty)

The agent writes the log in this format. One row per insight.

| Insight ID | Code | Insight (one sentence) | Segment | Persona | Frequency | Intensity (quote) | Impact clues | Quotes and source interview IDs | Source labels (PM-held or AI-moderated) | Change (new, growing, fading, no change) | First seen | Last updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## "What changed" summary format

3 to 6 bullets. Each bullet names the insight ID and what changed since the last batch.

## Flag report format

| Flag ID | Item | Why the agent stopped | Source interview IDs | PM decision (keep, fix, send to discovery) |
| --- | --- | --- | --- | --- |
