---
name: gate-docs-test
description: Phase 0 test. Proves that Claude Code on this computer can make a Claude Doc, read Dan's comments and edits, and reply in a thread. Run once before Phase 1, and again if gate reviews stop working.
---

# Gate docs test

Purpose: prove the gate review loop in `docs/gate-reviews.md` works from this computer. Explain each step to Dan in one or two plain sentences as you do it. Dan is learning Claude Code.

## Steps

1. Check for the Claude Docs tools (names that contain `Claude_Docs`). If they are not available, stop. Tell Dan to run `/login` with his claude.ai account and `/mcp`, then try again. Record step 1 as fail.
2. Make a Claude Doc named "Gate test <today's date>". Put in it:
   - One line: "This is a test gate packet. Add 2 comments and change one word in the table."
   - A table with 3 rows: Workflow, Bottleneck, Proposed lab. Use placeholder text.
3. Give Dan the doc link. Ask Dan to add 2 comments, change one word in the table, then say "done".
4. Wait for "done". Read the doc again and list its comment threads. Quote each comment and the changed word back to Dan. Ask Dan to confirm they are correct.
5. Reply in the first comment thread: "Read by Claude Code on <machine name> at <time>."
6. Ask Dan to confirm he sees the reply in the doc.
7. Write `logs/gate-test-result.md`:

   | Step | Result |
   | --- | --- |
   | Make doc | pass or fail |
   | Read comments and edit | pass or fail |
   | Reply in thread | pass or fail |

   Add the date, the machine (from `hostname`), and the doc link.
8. Update the "Result so far" table in `docs/gate-reviews.md`.
9. If any step failed, tell Dan the fallback: Word files per gate. Do not try to fix the connector by editing settings without Dan's yes.

## Rules

- Do not delete the test doc. Dan can delete it.
- ASD-STE100 style. No em dashes or en dashes.
