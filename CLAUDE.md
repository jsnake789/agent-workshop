# Agent workshop

Jake's repository of Claude Code agents, skills and a file-based memory graph.

## Layout

- `.claude/agents/*.md` subagents (one role each, minimal tools)
- `.claude/skills/<name>/SKILL.md` skills, with reference files beside them
- `memory/` the knowledge graph; read `memory/README.md` before editing it
- `tools/` `memory.py` (graph CLI), `lint.py` (agents/skills), `check_todoist_csv.py`
- `templates/` starting points for new agents and skills
- `plans/`, `reviews/` outputs from the planning and review skills

## Working rules

- **Context:** the SessionStart hook prints `memory/INDEX.md`. Pull detail with
  `python3 tools/memory.py context <id> --depth 1`; never read the whole `memory/` tree.
- **Write back:** when you learn a lasting fact or a decision is made, use the `remember`
  skill before finishing.
- **New agents/skills:** use the `new-agent` / `new-skill` skills; facts belong in memory,
  not hard-coded in prompts.
- **Before committing:** `make check` must pass.
- **External changes** (Todoist, calendar, email, GitHub) need an explicit yes first.
  CSV files are the default delivery for Todoist.
- No secrets in this repo or in memory.
