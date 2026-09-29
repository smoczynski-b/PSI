#!/usr/bin/env python3
"""Check PSI control records. No mathematical or live-system certification."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BEGIN = '<!-- BEGIN CONTROL STATUS -->'
END = '<!-- END CONTROL STATUS -->'


def status_table(state, volume=None):
    rows = ['| Unit | Recorded status | Evidence |', '|---|---|---|']
    for unit in state['units']:
        if volume and not unit['id'].startswith(volume + '.'):
            continue
        rows.append(f"| {unit['id']} | {unit['state']} | "
                    f"[unit]({Path(unit['path']).name}) / "
                    f"[audit]({Path(unit['evidence']).name}) |")
    return '\n'.join(rows)


def work_map(state):
    out = ['# PSI — current work map', '', '**Control role:** `work-map`',
           f"**Record date:** {state['as_of']}", '',
           'Generated from [control-state.json](control-state.json); edit that source,',
           'then run `python scripts/check_control.py --write`.',
           'Mathematical statuses are inherited records, not fresh proof audits.', '',
           '## Selection', '', state['selection']['rule'], '',
           f"Default substantive unit: **{state['selection']['primary']}**, after the external delta/STOP check.",
           'One active primary unit. [Regular checks and effort budget](work-routine.md).', '',
           '## Operational tasks', '']
    for task in state['tasks']:
        out += [f"### {task['id']} — {task['state']}", '']
        for key in ('action', 'reason', 'release', 'next_check', 'allowed', 'evidence'):
            if key in task:
                out += [f"**{key.replace('_', ' ').capitalize()}:** {task[key]}", '']
        out += [f"**Source:** [{task['source']}](../{task['source']}).", '']
    out += ['## Recorded mathematical state', '', status_table(state), '',
            'CORE5 remains FROZEN. P2 general remains PARTIAL; P9 general remains OPEN/CENTRAL.',
            'III.13 requires a completed P9-I source/contract gate.', '',
            '## Interpretation', '',
            'Traffic: G0A/G0D instrumentation PASS is inherited from the protocol;',
            'G0B/G0C/G0E remain UNOBSERVED. No fresh live counts are asserted here.',
            'WWW visual grammar remains frozen; FB publication sequence is unchanged.',
            'PSI theory/control lives here; the experimental implementation lives in psi-model.',
            'Stable pointers supersede numbered control snapshots. Unchanged history is not reread',
            'at every session. No new status, ledger or commit is required without a meaningful delta.', '']
    return '\n'.join(out)


def write_views(root, state):
    (root / state['current']['work-map']).write_text(work_map(state), encoding='utf-8')
    for vol in (2, 3):
        path = root / state['current'][f'theorem-map-v{vol}']
        content = path.read_text(encoding='utf-8')
        block = BEGIN + '\n' + status_table(state, 'II' if vol == 2 else 'III') + '\n' + END
        if BEGIN in content:
            content = re.sub(re.escape(BEGIN) + r'.*?' + re.escape(END),
                             lambda _: block, content, flags=re.S)
        else:
            content += '\n\n## Recorded unit status (control view)\n\n' + block + '\n'
        path.write_text(content, encoding='utf-8')


def validate(root):
    errors = []
    state = json.loads((root / 'docs/control-state.json').read_text(encoding='utf-8'))

    def require(ok, message):
        if not ok:
            errors.append(message)

    def exists(path):
        return bool(path) and (root / path).is_file()

    current = state['current']
    require(len(set(current.values())) == len(current), 'duplicate current paths')
    for role, path in current.items():
        require(exists(path), f'missing current file: {path}')
        holders = [str(p.relative_to(root)) for p in (root / 'docs').glob('*.md')
                   if f'**Control role:** `{role}`' in p.read_text(encoding='utf-8')]
        require(holders == [path], f'current role is not unique: {role}: {holders}')
    readme = (root / 'README.md').read_text(encoding='utf-8')
    pointer_block = readme.split('## Current control pointers', 1)[-1].split('\n---', 1)[0]
    for path in current.values():
        require(f']({path})' in pointer_block, f'README pointer missing: {path}')
    require(not re.search(r'\]\(docs/(?:claim-registry|falsifier-registry|work-map|principia-v[23]-theorem-map)-\d+\.md\)', pointer_block),
            'README points to a historical current registry/map')

    files = [root / 'README.md', root / 'AGENTS.md'] + [root / p for p in current.values()]
    for path in files:
        if not path.is_file():
            continue
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]\n]+\]\(([^\s)]+)\)', text):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            require((path.parent / unquote(parts.path)).is_file(),
                    f'broken local link: {path.relative_to(root)} -> {target}')

    for prefix, role in [('C', 'claim-registry'), ('F', 'falsifier-registry')]:
        path = root / current[role]
        if not path.is_file():
            continue
        text = path.read_text(encoding='utf-8')
        ids = re.findall(r'^## (' + prefix + r'\d+(?:-v\d+)?) — ', text, re.M)
        numbers = [int(re.search(r'\d+', item)[0]) for item in ids]
        require(sorted(numbers) == list(range(1, state['registry_counts'][prefix] + 1)),
                f'{prefix} registry missing or duplicate entry')
        require(not re.search(r'^Retain [CF]\d', text, re.M), f'{prefix} registry is recursive')
        if prefix == 'C':
            require('C19-v3' in ids and 'C19-v2' not in ids, 'withdrawn C19 version is current')
            c21 = text.split('## C21 —', 1)[-1].split('\n## ', 1)[0]
            require('RESOLVED / SUPERSEDED BY C22' in c21 and '=OPEN' not in c21,
                    'C21 retains withdrawn OPEN status')
        else:
            f12 = text.split('## F12 —', 1)[-1].split('\n## ', 1)[0]
            require('C19-v3' in f12 and 'F62' in f12, 'F12 lacks adopted scope correction')

    task_ids = [t['id'] for t in state['tasks']]
    require(len(task_ids) == len(set(task_ids)), 'duplicate task ID')
    task_map = {t['id']: t for t in state['tasks']}
    require(task_map.get(state['selection']['primary'], {}).get('state') == 'READY',
            'primary task is not executable')
    for task in state['tasks']:
        require(exists(task['source']), f"missing task source: {task['id']}")
        if task['state'] in ('WAIT', 'BLOCKED'):
            for key in ('reason', 'source', 'release', 'next_check', 'allowed'):
                require(bool(task.get(key, '').strip()), f"{task['id']} lacks {key}")

    units = state['units']
    require(len({u['id'] for u in units}) == len(units), 'duplicate theorem unit')
    declared = {u['path'] for u in units}
    for unit in units:
        require(exists(unit['path']) and exists(unit['evidence']), f"unit/evidence missing: {unit['id']}")
        if unit['id'].startswith('III.') and int(unit['id'].split('.')[1]) > 12:
            gate = state['gates'].get(unit['id'], {})
            require(gate.get('state') == 'PASS' and exists(gate.get('path')), f"unpassed source gate: {unit['id']}")
    for path in (root / 'docs').glob('principia-v[23]-[0-9][0-9]-*.md'):
        require(str(path.relative_to(root)) in declared, f'unregistered theorem unit: {path.name}')
    require((root / current['work-map']).read_text(encoding='utf-8') == work_map(state),
            'work map differs from control state; regenerate views')
    for vol in (2, 3):
        path = root / current[f'theorem-map-v{vol}']
        if not path.is_file():
            continue
        text = path.read_text(encoding='utf-8')
        expected = BEGIN + '\n' + status_table(state, 'II' if vol == 2 else 'III') + '\n' + END
        require(expected in text and text.count(BEGIN) == 1, f'V{vol} status mismatch')

    graph = {k: list(v) for k, v in state['supersedes'].items()}
    for path in (root / 'docs').glob('*.md'):
        matches = re.findall(r'\*\*Supersedes(?:[^*]*):\*\*\s*`([^`]+\.md)`', path.read_text(encoding='utf-8'))
        if matches:
            graph.setdefault(str(path.relative_to(root)), []).extend('docs/' + p for p in matches)
    for newer, older in graph.items():
        require(exists(newer) and all(exists(p) for p in older), f'missing supersedes target: {newer}')
    visited, active = set(), set()

    def visit(node):
        if node in active:
            errors.append(f'supersedes cycle: {node}')
            return
        if node in visited:
            return
        active.add(node)
        for parent in graph.get(node, []):
            visit(parent)
        active.remove(node)
        visited.add(node)
    for node in graph:
        visit(node)
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='regenerate current work/status views')
    args = parser.parse_args()
    if args.write:
        write_views(ROOT, json.loads((ROOT / 'docs/control-state.json').read_text(encoding='utf-8')))
    try:
        failures = validate(ROOT)
    except (KeyError, ValueError, OSError, TypeError) as exc:
        failures = [f'invalid control record: {exc}']
    for failure in failures:
        print('FAIL:', failure)
    if not failures:
        print('PASS: pointers, materialized registries, task conditions, recorded statuses and source-gate records.')
        print('Scope: control consistency only; mathematical proofs and live operation were not tested.')
    sys.exit(bool(failures))
