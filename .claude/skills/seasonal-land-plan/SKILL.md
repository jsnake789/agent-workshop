---
name: seasonal-land-plan
description: Plan the month's or quarter's jobs for the two acres and the dogs in Shropshire, England. Use for "what needs doing on the land", seasonal checklists, dog care schedules, or outdoor ideas to share with Willow.
---

# Seasonal land plan

1. Recall: `python3 tools/memory.py context area/smallholding place/home-acres animal/the-dogs`.
2. Start from [uk-seasonal-calendar.md](uk-seasonal-calendar.md) for the months in scope,
   then adjust to what memory says is actually on the land.
3. Add dog routines from memory (worming, flea and tick, boosters, insurance). If dates
   are missing, list them as questions and don't guess.
4. Mark any job that doubles as a Willow activity with `(Willow)` and a one-line idea.
5. Output a short checklist per month, then a CSV via `todoist-export` with sections
   `Land` and `Dogs` and labels `@land`, `@dogs`, `@outdoors`.
6. Save new facts (what's planted, dog details) with `remember`.
