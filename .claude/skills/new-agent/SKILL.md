---
name: new-agent
description: Scaffold a new subagent in this repo. Use when asked to create or add an agent, assistant or specialist role.
---

# New agent

1. Confirm it should be an agent, not a skill: it needs its own context window because
   the work is long, noisy or needs a focused role. Otherwise use `new-skill`.
2. `cp templates/agent.md .claude/agents/<name>.md`.
3. Frontmatter:
   - `name`: kebab-case, same as the file name.
   - `description`: what the role does and when to delegate to it.
   - `tools`: the fewest that work, comma-separated (omit the line only if it truly needs
     everything). Common sets:
     - read-only research: `Read, Glob, Grep, WebSearch, WebFetch`
     - writes files: add `Write, Edit`
     - runs tools/scripts: add `Bash`
   - `model`: omit to inherit; use `haiku` for cheap, mechanical agents.
4. Body: role in one paragraph, a "Before" section saying which memory context to pull,
   principles, and an exact output format. Say what it must never do.
5. Run `python3 tools/lint.py`, then add it to the agents table in `README.md`.
