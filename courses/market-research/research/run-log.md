# Stage 1 run log

- 2026-11-20 02:45 UTC: Stage 1 run 1 started in the cloud. Step 1, 4 researchers in parallel.
- Track 2 done (34 features, 12 gaps).
- Track 4 done (30 ledger entries, 26 sources, 10 gaps).
- Track 1 done (9 rows). Note: worked-example-row.yaml does not parse as YAML (2 unquoted values). Left unchanged; ask Dan before a quote-only fix.
- Track 3 done (12 tasks, 25 sources). Web fetch budget ran out; 4 primary pages unopened (listed in needs.md).
- 02:41 UTC: Step 2 started, 3 checkers in parallel.
- Critic done: 4 rerun asks (one per track).
- Alignment done: 9 conflicts (2 high). PA-01 touches the approved row; needs Dan.
- Verifier done: 54 verified, 11 partly, 22 not verified, 2 wrong (E8 Gemini date, E13 figure). Rows 07, 08 fail 2-source rule.
- 02:51 UTC: Step 3 started, one rerun per track on critic asks.
- Rerun done: track 1 partly (mr-wf-10), track 2 partly, track 3 partly, track 4 open. Fetch budget ran out.
- Rerun items verified. 02:58 UTC: Step 4, Synthesizer.
- Synthesizer done. 03:03 UTC: Step 5, trace check.
- Trace check done: ~110 claims, 17 fixes, 3 flags for Dan.
