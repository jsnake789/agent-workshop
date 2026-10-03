---
name: recall
description: Pull just the relevant context from the memory graph before starting a task. Use at the start of any task about Willow, the land, the dogs, plans or past decisions, or when the user asks what we know about something.
---

# Recall

Load as little as possible, as precisely as possible.

1. Read `memory/INDEX.md` (one line per node).
2. Choose the 1 to 3 node ids the task is centred on. If nothing matches, try
   `python3 tools/memory.py search <keyword>`.
3. Run `python3 tools/memory.py context <id> [<id> ...] --depth 1`.
   - Use `--depth 2` only for broad questions ("everything about Willow's education").
   - Use `--full` only when neighbours' bodies matter, not just their summaries.
4. Work from that output. If something important is missing or stale, say so and offer
   to `remember` the correction afterwards.
5. When answering "what do we know about X", cite node ids so the user can open them.
