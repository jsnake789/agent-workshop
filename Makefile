.PHONY: check index graph

check:            ## lint agents/skills and validate memory
	python3 tools/lint.py
	python3 tools/memory.py validate

index:            ## rebuild memory/INDEX.md
	python3 tools/memory.py index

graph:            ## export the memory graph
	python3 tools/memory.py export --format json > graph.json
	python3 tools/memory.py export --format cypher > graph.cypher
