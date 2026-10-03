---
name: remember
description: Save a fact, decision, preference or event to the memory graph. Use when the user says remember, note that, we decided, from now on, or when a task produced something a future session would otherwise have to ask again.
---

# Remember

1. **Decide whether it's worth keeping.** Keep: facts about people, animals, places;
   decisions and why; preferences about how to work; recurring routines; pointers to
   files. Skip: anything already in git history or a file, or only relevant right now.
   Never store secrets, passwords or account numbers.
2. **Find the home.** `python3 tools/memory.py search <keyword>` and scan `memory/INDEX.md`.
   If a node already covers it, edit that node and bump `updated`.
3. **Otherwise create one:** `python3 tools/memory.py new <type> "<Title>"`, then fill in
   `summary` (one line) and the body. Types are in `memory/schema.yaml`. For decisions use
   **Decided:** date, **Why:**, **Consequence:**.
4. **Link it.** Add at least one typed edge to `links` (e.g.
   `{rel: belongs_to, to: area/willow-education}`). Mention related nodes inline as
   `[[type/slug]]`.
5. **If unsure where it goes,** write it to `memory/inbox/<yyyy-mm-dd>-<slug>.md` instead
   and let the `memory-librarian` triage it later.
6. Run `python3 tools/memory.py validate && python3 tools/memory.py index`.
7. Tell the user in one line what was saved and under which id.
