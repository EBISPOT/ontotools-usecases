#!/usr/bin/env python3
"""Merge evaluation entries (JSON list on stdin) into evaluations.json, keyed by question number."""
import json, sys, os
new = json.load(sys.stdin)
path = 'evaluations.json'
ev = json.load(open(path)) if os.path.exists(path) else {}
for e in new:
    ev[str(e['n'])] = e
json.dump(ev, open(path, 'w'), indent=2, ensure_ascii=False)
print(f"{len(new)} added; {len(ev)} total")
