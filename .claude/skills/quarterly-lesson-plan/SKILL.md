---
name: quarterly-lesson-plan
description: Build Willow's EYFS activity grid for a quarter (13 weeks) and its Todoist import. Use when asked for next quarter's plan, a lesson grid, or to refresh or extend an existing quarter.
---

# Quarterly lesson plan

## 1. Gather

- `python3 tools/memory.py context person/willow area/willow-education --depth 1`
- Previous quarter: find its `project/willow-plan-*` node and CSV, list what to progress.
- Willow's age in months at the start and end of the quarter (born about early March 2026).
- The season and what the land and weather will offer (see `seasonal-land-plan`).

## 2. Choose goals

For each EYFS area pick 1 or 2 observable goals for this age band. See
[eyfs-reference.md](eyfs-reference.md). Weighting until about age 3:

| Area | Activities per quarter |
|---|---|
| Communication and language | 4 to 6 |
| Physical development | 4 to 6 |
| Personal, social and emotional | 3 to 5 |
| Each specific area | 1 to 3 |

## 3. Write activities

Each activity: a verb-first title, the goal it serves, setting (indoors, garden, field,
with dogs), duration (10 to 20 min), what to notice, and a fortnightly or monthly date.
Repeat core activities across the quarter with a small twist rather than inventing new
ones weekly. Dog activities always say "supervised, dog free to walk away".

## 4. Deliver

1. A readable grid: `plans/willow-<yyyy>-q<n>.md`, a table per month with
   Area | Activity | Goal | When.
2. The Todoist CSV via the `todoist-export` skill: one section per EYFS area, label per
   area (`@communication`, `@physical`, `@psed`, `@literacy`, `@maths`, `@world`, `@arts`).
3. A memory node `project/willow-plan-<yyyy>-q<n>` (`belongs_to: area/willow-education`)
   with the age band, chosen goals and file paths.

## 5. Review the previous quarter (if one exists)

Ask Jake which goals were seen, which weren't, and what Willow loved. Record a short
`event/` or update the previous quarter's node, then carry unmet goals forward.
