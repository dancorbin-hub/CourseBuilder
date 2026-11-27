# Job card: win/loss

Use this job when the PM says "Run the win/loss job".

Input: a CRM export of decided deals and win/loss interview notes (in chat). The driver code book and the driver log (knowledge). At the start, there is no driver log.

This job writes the driver log. It does not change the problem backlog. It gives no ranking. It reports counts. The PM decides what to act on.

Steps:

1. Match each deal in the CRM export to its interview notes by deal ID.
2. Code the primary driver, secondary drivers and alternative chosen for each deal, with the driver code book.
3. Write the driver log, in the format in the driver code book.
4. Compare each CRM reason with the buyer's primary driver. Fill the match rate table.
5. For each driver, give its count of interviewed deals, accounts and segments, and the change since the last driver log.
6. Write the flag report and the "what changed" summary.

Quality checks. Run them on your output before you answer:

- Each driver has a buyer quote found word for word in the interview.
- Each driver shows its count of interviewed deals, its accounts and its segments.
- Each deal is marked "interview" or "CRM only".

Hand-off rules. Send these to the flag report:

- A deal where the CRM reason and the buyer reason differ.
- A lost deal that names an alternative not in the code book.

Output order (it replaces the order in the brief): 1. Driver log. 2. Match rate table. 3. Driver counts. 4. Flag report. 5. What changed.
