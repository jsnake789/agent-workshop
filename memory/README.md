# Memory

A small, file-based knowledge graph. Plain markdown today; a graph database later
without rewriting anything.

## Shape

```
memory/
  schema.yaml          node types + allowed relations (the contract)
  INDEX.md             generated: every node, one line each (read this first)
  nodes/<type>/<slug>.md
  inbox/               quick unstructured captures, triaged into nodes later
```

## A node

```markdown
---
id: decision/eyfs-framework        # = <type>/<slug>, must match the file path
type: decision
title: Use EYFS as Willow's framework
status: active                     # active | paused | done | archived | superseded
created: 2026-10-02
updated: 2026-10-03
tags: [education]
summary: One line. This is what shows in INDEX.md and in recall.
links:
  - {rel: decided_in, to: area/willow-education}
  - {rel: about, to: concept/eyfs}
---

Free markdown body. Mention other nodes inline like [[person/willow]];
those become `mentions` edges.
```

Rules that keep it graph-ready:

1. **One fact cluster per node.** If a note covers two things, split it.
2. **Ids are stable.** Rename the title freely; never the id. If you must, make
   a new node and `supersedes` the old one.
3. **Edges are typed** and live in `links`. Use a relation from `schema.yaml`;
   add a new one there first if nothing fits.
4. **Edges are stored once**, on the node where they read naturally
   (`willow child_of jake`). The tooling derives the inverse view.
5. **Keep bodies short** (under ~60 lines). Long reference material belongs in
   a `resource` node pointing at a file.

## Tooling

```bash
python3 tools/memory.py new decision "Use EYFS as framework"   # scaffold a node
python3 tools/memory.py validate     # ids, types, relations, dangling links
python3 tools/memory.py index        # rebuild INDEX.md
python3 tools/memory.py show person/willow      # node + in/out edges
python3 tools/memory.py context person/willow --depth 2   # subgraph as markdown, for prompts
python3 tools/memory.py search dogs
python3 tools/memory.py export --format json   > graph.json     # nodes + edges
python3 tools/memory.py export --format cypher > graph.cypher   # Neo4j/Memgraph import
```

## Managing context

Agents should not load the whole memory. The pattern is:

1. Read `memory/INDEX.md` (one line per node, cheap).
2. Pick the 1 to 3 nodes the task is about.
3. Run `memory.py context <id> --depth 1` (or 2) to pull just that neighbourhood.
4. After the work, write back new facts and decisions (the `remember` skill).

## Moving to a graph database later

`export --format cypher` already emits `MERGE` statements: one label per node
type, properties from frontmatter, the body as a `body` property, and one
relationship per link. When you outgrow files, either import once and switch,
or keep markdown as the source of truth and re-import on change. Adding
embeddings later just means a `vector` property per node; nothing here
needs to change shape.
