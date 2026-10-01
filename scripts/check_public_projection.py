#!/usr/bin/env python3
"""Bounded consistency check for the public PSI projection."""
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
errors = []

def require(ok, msg):
    if not ok:
        errors.append(msg)

state = json.loads((root / 'docs/control-state.json').read_text(encoding='utf-8'))
readme = (root / 'README.md').read_text(encoding='utf-8')
agents = (root / 'AGENTS.md').read_text(encoding='utf-8')
mem = (root / 'docs/memory/README.md').read_text(encoding='utf-8')

require('docs/publication-policy.md' in readme, 'README lacks publication-policy pointer')
require((root / 'docs/publication-policy.md').is_file(), 'publication policy missing')

f = state.get('registry_counts', {}).get('F')
if isinstance(f, int):
    require(f'F01–F{f}' in readme or f'F01-F{f}' in readme,
            f'README falsifier count differs from control state F={f}')

p9i = next((t for t in state.get('tasks', []) if t.get('id') == 'P9-I'), None)
if p9i and p9i.get('state') == 'DONE':
    require('No III.13 theorem is authorized yet' not in readme,
            'README retains stale III.13 authorization text')
    require('P9-I SOURCE GATE NEXT' not in readme.upper(),
            'README retains stale P9-I NEXT')

unit = next((u for u in state.get('units', []) if u.get('id') == 'III.13'), None)
if unit and unit.get('state') == 'PASS':
    require('III.13' in readme, 'README omits passed III.13')

for text, label in ((agents, 'AGENTS'), (mem, 'memory README')):
    require('Current next unit: R1' not in text, f'{label} retains stale R1 NEXT')
    require('Następna jednostka dla GPT-5: R1' not in text, f'{label} retains stale R1 NEXT')
    require('P9-I SOURCE GATE NEXT' not in text.upper(), f'{label} retains stale P9-I NEXT')

require('private research queue' in agents.lower(), 'AGENTS does not separate public and private work selection')
require('not a private work selector' in mem.lower(), 'memory README does not disclaim private NEXT authority')

if errors:
    for error in errors:
        print('FAIL:', error)
    sys.exit(1)
print('PASS: public PSI projection matches recorded F/III.13 status and disclosure boundary')
