#!/usr/bin/env python3
"""Estimate Dan's active hours in Claude Code from local session transcripts.

How it works:
- Claude Code saves each session as a .jsonl file in ~/.claude/projects/<folder>/.
- The script reads the times of the messages that a person typed (not tool results).
- Two typed messages close together mean Dan was active between them.
- A gap longer than the idle limit counts as the idle limit only (Dan was away).
- Each session also gets a short tail after the last message (time to read the answer).

This is an estimate. It does not see time spent reading a Claude Doc or testing
on a platform. Log that time by hand in logs/hours-log.csv.

Usage:
  python3 scripts/estimate_hours.py                     # all sessions for this repo
  python3 scripts/estimate_hours.py --since 2026-11-19  # from a date
  python3 scripts/estimate_hours.py --match coursebuilder --idle 10 --tail 5
"""
import argparse
import json
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path


def typed_by_person(entry):
    """True when the entry is a message a person typed, not a tool result."""
    if entry.get("type") != "user":
        return False
    if entry.get("isMeta") or entry.get("isSidechain"):
        return False
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        return bool(content.strip())
    if isinstance(content, list):
        return any(isinstance(c, dict) and c.get("type") == "text" for c in content)
    return False


def parse_time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def session_times(path):
    times = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if typed_by_person(entry) and entry.get("timestamp"):
                times.append(parse_time(entry["timestamp"]))
    return sorted(times)


def active_time(times, idle, tail):
    if not times:
        return timedelta(0)
    total = tail
    for earlier, later in zip(times, times[1:]):
        total += min(later - earlier, idle)
    return total


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default=str(Path.home() / ".claude" / "projects"))
    parser.add_argument("--match", default="coursebuilder", help="text in the project folder name (case is ignored)")
    parser.add_argument("--since", help="YYYY-MM-DD, local date of the first message")
    parser.add_argument("--idle", type=float, default=10, help="idle limit in minutes")
    parser.add_argument("--tail", type=float, default=5, help="minutes added after the last message")
    args = parser.parse_args()

    idle = timedelta(minutes=args.idle)
    tail = timedelta(minutes=args.tail)
    since = datetime.fromisoformat(args.since).date() if args.since else None

    by_day = defaultdict(timedelta)
    sessions = 0
    for folder in Path(args.root).glob("*"):
        if args.match.lower() not in folder.name.lower():
            continue
        for path in folder.glob("*.jsonl"):
            times = [t.astimezone() for t in session_times(path)]
            if since:
                times = [t for t in times if t.date() >= since]
            if not times:
                continue
            sessions += 1
            by_day[times[0].date()] += active_time(times, idle, tail)

    if not by_day:
        print("No sessions found. Check --root and --match.")
        return
    print("date,estimated_hours")
    for day in sorted(by_day):
        print(f"{day},{by_day[day].total_seconds() / 3600:.2f}")
    total = sum(by_day.values(), timedelta(0)).total_seconds() / 3600
    print(f"# {sessions} sessions, {total:.2f} hours in total (idle limit {args.idle:g} min)")


if __name__ == "__main__":
    main()
