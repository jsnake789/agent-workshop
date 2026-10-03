#!/usr/bin/env python3
"""Check a Todoist import CSV against the format in the todoist-export skill."""
import csv
import sys

HEADER = ["TYPE", "CONTENT", "DESCRIPTION", "PRIORITY", "INDENT", "AUTHOR", "RESPONSIBLE",
          "DATE", "DATE_LANG", "TIMEZONE", "DURATION", "DURATION_UNIT", "DEADLINE", "DEADLINE_LANG"]


def main(path):
    errors, counts = [], {"section": 0, "task": 0}
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    if rows[0] != HEADER:
        errors.append("header does not match the Todoist template")
    for i, row in enumerate(rows[1:], start=2):
        if len(row) != len(HEADER):
            errors.append(f"line {i}: {len(row)} fields, expected {len(HEADER)}")
            continue
        r = dict(zip(HEADER, row))
        if r["TYPE"] not in counts:
            errors.append(f"line {i}: TYPE must be section or task")
            continue
        counts[r["TYPE"]] += 1
        if not r["CONTENT"].strip():
            errors.append(f"line {i}: empty CONTENT")
        if r["TYPE"] == "task":
            if r["PRIORITY"] not in ("1", "2", "3", "4"):
                errors.append(f"line {i}: PRIORITY must be 1-4")
            if r["INDENT"] not in ("1", "2", "3", "4"):
                errors.append(f"line {i}: INDENT must be 1-4")
    for e in errors:
        print("ERROR", e)
    print(f"{path}: {counts['section']} sections, {counts['task']} tasks, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(max(main(p) for p in sys.argv[1:]) if len(sys.argv) > 1 else 2)
