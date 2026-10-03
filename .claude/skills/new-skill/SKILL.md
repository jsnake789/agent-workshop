---
name: new-skill
description: Scaffold a new skill in this repo. Use when asked to create, add or turn a workflow into a skill.
---

# New skill

1. Pick a kebab-case name that says what it does (`seasonal-land-plan`, not `helper`).
   Check `.claude/skills/` and `.claude/agents/` for overlap; extend instead if one fits.
2. Copy the template: `cp -r templates/skill .claude/skills/<name>` and rename nothing else.
3. Fill in the frontmatter:
   - `name`: same as the folder.
   - `description`: one or two sentences, what it does **and** when to use it, using
     words Jake would actually say. This line decides whether the skill triggers.
4. Write the body as numbered steps with a concrete output format. Keep SKILL.md under
   ~150 lines; move reference material to sibling files (`reference.md`, `examples/`) and
   link to them by relative path.
5. If the skill needs facts about people, places or decisions, read them from memory
   (`python3 tools/memory.py context <id>`) rather than hard-coding them.
6. Run `python3 tools/lint.py` and fix anything it reports.
7. Add a line to the skills table in `README.md`.
