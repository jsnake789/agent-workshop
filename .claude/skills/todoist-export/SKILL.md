---
name: todoist-export
description: Write tasks as a Todoist CSV import file in the exact format Jake uses. Use whenever a plan, checklist or routine should become Todoist tasks.
---

# Todoist CSV export

## Format

Header row, exactly:

```
TYPE,CONTENT,DESCRIPTION,PRIORITY,INDENT,AUTHOR,RESPONSIBLE,DATE,DATE_LANG,TIMEZONE,DURATION,DURATION_UNIT,DEADLINE,DEADLINE_LANG
```

Row types:
- `section,<Section name>,,,,,,,,,,,,` starts a section.
- `task,<content @label>,<description>,<priority>,<indent>,,,<date>,en,,<duration>,minute,,`

Rules:
- `PRIORITY`: Todoist CSV uses 1 = urgent (p1) to 4 = normal (p4). Default 4.
- `INDENT`: 1 for a task, 2 for a subtask of the task above.
- `DATE`: ISO `YYYY-MM-DD`, or natural language like `every 2 weeks starting 2026-10-05`.
- Labels go in CONTENT as `@label`, no spaces in the label.
- Quote any field containing a comma. Use Python's `csv` module, never hand-join.
- One CSV per Todoist project. Keep under ~150 rows.

## Steps

1. Build rows as a list of dicts in a short Python script and write with `csv.DictWriter`.
2. Name the file `<project-slug>-<period>.csv` (e.g. `todoist-willow-Q1-2027.csv`).
3. Validate with `python3 tools/check_todoist_csv.py <file>`.
4. Tell Jake: in Todoist, open the target project, then the project menu, then
   "Import from CSV".

## Example

See [example.csv](example.csv).
