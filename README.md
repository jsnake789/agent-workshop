# Agent workshop

A place to create and maintain Claude Code **agents** and **skills**, plus a small
**memory graph** that gives them shared, durable context. Plain files today, designed to
load into a graph database later.

## Quick start

```bash
make check                                   # lint agents/skills + validate memory
python3 tools/memory.py context person/willow   # see what an agent would load
```

Open the folder in Claude Code; the agents and skills are picked up from `.claude/`
automatically, and the memory index is loaded at session start.

## Agents (`.claude/agents/`)

| Agent | Use it for |
|---|---|
| `eyfs-lesson-planner` | Willow's quarterly and weekly EYFS activities |
| `todoist-sync` | Turning any plan into Todoist tasks (CSV, or the connector on request) |
| `smallholding-steward` | Seasonal jobs on the two acres and the dogs' care routines |
| `weekly-reviewer` | A short weekly review across Todoist, calendar and memory |
| `memory-librarian` | Triaging the inbox, linking and tidying the memory graph |
| `agent-smith` | Designing, writing and reviewing agents and skills here |

## Skills (`.claude/skills/`)

| Skill | What it does |
|---|---|
| `quarterly-lesson-plan` | Builds a 13-week EYFS grid + Todoist CSV + memory node |
| `todoist-export` | Writes the exact Todoist CSV import format |
| `seasonal-land-plan` | Monthly land and dog checklists for Shropshire |
| `weekly-review` | The weekly review procedure |
| `remember` | Saves a fact or decision into the memory graph |
| `recall` | Loads just the relevant slice of memory for a task |
| `new-skill` / `new-agent` | Scaffolds new ones from `templates/` |

## Memory (`memory/`)

Each node is a markdown file with typed frontmatter (`id`, `type`, `summary`, `links`).
Typed `links` are graph edges; `[[type/slug]]` in the body becomes a `mentions` edge.
`schema.yaml` defines the node types and relations. Full guide in
[memory/README.md](memory/README.md).

```
person/jake ──parent_of──▶ person/willow ──lives_at──▶ place/home-acres
area/willow-education ──follows──▶ decision/eyfs-framework ──about──▶ concept/eyfs
project/willow-plan-2026-q4 ──belongs_to──▶ area/willow-education
```

Graph export when you're ready for a database:

```bash
make graph     # graph.json (nodes + edges) and graph.cypher (Neo4j / Memgraph MERGE script)
```

## Adding your own

Ask Claude "make a skill for X" or "add an agent that does Y"; the `new-skill`,
`new-agent` and `agent-smith` pieces handle the scaffolding and `make check` keeps it
consistent.
