---
name: weekly-review
description: Run a short weekly review of tasks, calendar and memory and set the week's priorities. Use when asked for a weekly review, "what's on this week", "what slipped", or on a Sunday or Monday check-in.
---

# Weekly review

1. **Collect** (read-only):
   - Todoist: overdue tasks, tasks due in the next 7 days, tasks completed in the last 7
     days (Todoist connector if available; otherwise ask Jake to paste or export).
   - Calendar: events in the next 7 days, if a calendar connector is available.
   - Memory: `python3 tools/memory.py context area/willow-education area/smallholding`
     and anything in `memory/inbox/`.
2. **Write the review** (under a page):
   - **This week's three:** the three things that matter most, one line each.
   - **Willow this week:** which plan activities are due; anything to adjust for her age
     or the weather.
   - **Land and dogs:** due jobs and routines.
   - **Slipped:** overdue items with a suggestion each: do, reschedule, delegate or drop.
   - **Decisions needed:** anything waiting on Jake.
3. **Propose changes, then wait.** List the reschedules or new tasks you'd make. Only
   apply them after an explicit yes.
4. **Remember.** Save decisions or changed routines with the `remember` skill and triage
   the inbox. Save the review itself as `reviews/<yyyy>-W<ww>.md`.
