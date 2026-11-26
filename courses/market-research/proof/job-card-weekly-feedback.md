# Job card: weekly feedback

Use this job when the PM says "Run the weekly feedback job".

Input: one week of feedback items (CSV), the tag list (knowledge file) and the current problem backlog. If the PM gave you last week's result, compare with it.

Steps:

1. Give each item one primary tag from the tag list, or "no fit".
2. Write a one-line reason for each tag. The reason quotes the item.
3. Count each tag by unique account, not by item.
4. Compare with last week. Report the change in accounts for every tag.
5. Update the problem backlog: add the feedback counts as "other sources" in each evidence profile.
6. Write a "what changed" summary. Report every change in accounts. Do not call a one-week change a trend.

Quality checks:

- Each tag has a one-line reason that quotes the item.
- Each item has exactly one primary tag or "no fit".
- Counts are by unique account.
- The "what changed" summary reports the change in accounts for every tag.

Hand-off rules. Send these to the flag report:

- Every "no fit" group, with its item IDs and accounts.
- Items that hold personal or health data. Do not copy that data into the backlog.

Output order: 1. tag table (tag, accounts this week, accounts last week, change, item IDs), 2. updated problem backlog, 3. flag report, 4. what changed.
