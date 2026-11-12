#!/usr/bin/env python3
"""Save one DocBot capture. Usage: save_answer.py <n> < capture.json
stdin: the JSON string returned by the in-page capture script (a JSON-encoded string of a JSON object)."""
import json, sys, os, re
n = int(sys.argv[1])
raw = sys.stdin.read().strip()
try:
    cap = json.loads(raw)
    if isinstance(cap, str):
        cap = json.loads(cap)
except json.JSONDecodeError as e:
    sys.exit(f"bad json: {e}")
qs = {q['n']: q for q in json.load(open('questions.json'))}
q = qs[n]
users = [m for m in cap['msgs'] if m['role'] == 'user']
bots = [m for m in cap['msgs'] if m['role'] == 'assistant']
problems = []
if len(users) != 1 or len(bots) != 1:
    problems.append(f"expected 1 user + 1 assistant message, got {len(users)} + {len(bots)}")
if users and users[0]['md'].strip() != q['question'].strip():
    problems.append("typed question differs from questions.json")
if not cap.get('done'):
    problems.append("answer not marked complete")
bot = bots[-1] if bots else {'id': None, 'md': '', 'links': [], 'sources': []}
suffix = '' if q['variant'] == 'full' else '-wts'
fname = f"answers/{n:02d}-{q['id']}{suffix}.md"
with open(fname, 'w', encoding='utf-8') as f:
    f.write(f"# {n:02d} {q['id']} ({q['variant']})\n\n")
    f.write(f"- Captured: {cap['at']}\n- DocBot message id: {bot['id']}\n- Complete: {cap.get('done')}\n")
    f.write(f"- Reference: {q['source']}\n\n")
    f.write("## Question\n\n" + q['question'] + "\n\n")
    f.write("## Answer\n\n" + (bot['md'] or '') + "\n\n")
    f.write("## Links in answer\n\n" + ("\n".join('- ' + l for l in bot['links']) or '- none') + "\n\n")
    f.write("## Sources shown\n\n" + ("\n".join('- ' + s for s in bot['sources']) or '- none') + "\n")
log_path = 'captures.json'
log = json.load(open(log_path)) if os.path.exists(log_path) else {}
log[str(n)] = {'n': n, 'id': q['id'], 'variant': q['variant'], 'question': q['question'], 'capturedAt': cap['at'],
               'messageId': bot['id'], 'complete': cap.get('done'), 'answerFile': fname,
               'answer': bot['md'], 'links': bot['links'], 'sources': bot['sources'], 'problems': problems}
json.dump(log, open(log_path, 'w'), indent=2, ensure_ascii=False)
print(f"saved {fname}" + (f"  PROBLEMS: {problems}" if problems else "  ok"))
