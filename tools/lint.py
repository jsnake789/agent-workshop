#!/usr/bin/env python3
"""Lint agents and skills: frontmatter, naming, descriptions, relative links."""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK = re.compile(r"\]\(([^)#:]+)\)")
KNOWN_TOOLS = {"Read", "Write", "Edit", "Glob", "Grep", "Bash", "WebSearch", "WebFetch",
               "NotebookEdit", "TodoWrite", "Task", "Agent"}


def frontmatter(path):
    text = path.read_text()
    if not text.startswith("---"):
        return None, text
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm) or {}, body


def check(path, expected_name, errors, is_agent):
    rel = path.relative_to(ROOT)
    fm, body = frontmatter(path)
    if fm is None:
        errors.append(f"{rel}: missing frontmatter")
        return
    name, desc = fm.get("name"), fm.get("description", "")
    if name != expected_name:
        errors.append(f"{rel}: name '{name}' should be '{expected_name}'")
    if not NAME.match(str(name)):
        errors.append(f"{rel}: name must be kebab-case")
    if len(desc) < 40:
        errors.append(f"{rel}: description too short to trigger reliably")
    if len(desc) > 1024:
        errors.append(f"{rel}: description over 1024 characters")
    if "use" not in desc.lower():
        errors.append(f"{rel}: description should say when to use it ('Use when ...')")
    if len(body.splitlines()) > 300:
        errors.append(f"{rel}: body over 300 lines, move reference material to files")
    if is_agent and fm.get("tools"):
        for t in [t.strip() for t in str(fm["tools"]).split(",")]:
            if t not in KNOWN_TOOLS and not t.startswith("mcp__"):
                errors.append(f"{rel}: unknown tool '{t}'")
    for target in LINK.findall(body):
        if not (path.parent / target).exists():
            errors.append(f"{rel}: broken link '{target}'")


def main():
    errors = []
    agents = sorted((ROOT / ".claude/agents").glob("*.md"))
    skills = sorted((ROOT / ".claude/skills").glob("*/SKILL.md"))
    for p in agents:
        check(p, p.stem, errors, True)
    for p in skills:
        check(p, p.parent.name, errors, False)
    for d in (ROOT / ".claude/skills").iterdir():
        if d.is_dir() and not (d / "SKILL.md").exists():
            errors.append(f"{d.relative_to(ROOT)}: missing SKILL.md")
    for e in errors:
        print("ERROR", e)
    print(f"{len(agents)} agents, {len(skills)} skills, {len(errors)} errors")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
