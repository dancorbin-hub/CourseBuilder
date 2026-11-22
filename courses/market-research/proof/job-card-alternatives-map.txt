# Job card: alternatives map

Use this job when the PM says "Run the alternatives map job".

Input: the evidence pack (driver log, CRM export, win/loss interviews and problem backlog) and the current alternatives map (knowledge file).

Steps:

1. For each lost deal, find the alternative the buyer chose.
2. Match it to an entry in the map: a named competitor, a substitute or do nothing.
3. Count lost deals per entry, per segment and per quarter. Keep deals with a buyer interview separate from CRM-only deals.
4. Compare the two quarters. Label each entry growing, fading or no change, with the counts for each quarter.
5. Link each entry to its evidence rows (deal ID and interview ID).
6. Write the updated map.

Quality checks:

- Each map entry links to 1 or more evidence rows with a deal ID or interview ID.
- Each entry shows its source type (buyer interview or CRM only).
- Each "growing" or "fading" label states the two periods compared and the counts in each.

Hand-off rules. Send these to the flag report:

- An alternative that is not in the map.
- A segment where "do nothing" or a workaround is the top alternative.
- The PM adds one hand-off rule here, from the win/loss job to the map job.

Output order: 1. updated map, 2. counts by segment, 3. flag report, 4. what changed.
