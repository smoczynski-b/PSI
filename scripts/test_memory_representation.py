#!/usr/bin/env python3
"""Finite, same-data representation witness; no image or LLM performance claim."""
from __future__ import annotations

import csv
from itertools import combinations
import json
import math

from prepare_memory_evaluation import digest, source_bytes

SOURCE_REF = '772bd92eb67f314bf99402462e9ec69392abcb5f'
SOURCE_PATH = 'docs/memory/psi-memory-edges-01.tsv'


def frozen_data():
    raw = source_bytes(SOURCE_REF, SOURCE_PATH)
    rows = list(csv.DictReader(raw.decode().splitlines(), delimiter='\t'))
    selected = [r for r in rows if r['from'] == 'II.9' and r['to'] in {'II.6', 'II.7', 'II.8'}]
    if len(selected) != 3 or len({r['to'] for r in selected}) != 3:
        raise ValueError('the frozen three-relation contract is not present')
    return sorted(selected, key=lambda r: r['to']), digest(raw)


def lost_distinctions(data, representation, task):
    """Exact finite check ker(representation) subset ker(task); return witnesses."""
    return [(a['to'], b['to']) for a, b in combinations(data, 2)
            if representation(a) == representation(b) and task(a) != task(b)]


def typed_graph(data, layout):
    return {'nodes': [{'id': n, 'xy': xy} for n, xy in layout.items()],
            'edges': [{'from': r['from'], 'to': r['to'], 'relation': r['relation'],
                       'source': r['source'], 'layer': r['layer'], 'note': r['note']} for r in data]}


def read_graph(view):
    ids = {n['id'] for n in view['nodes']}
    if len(ids) != len(view['nodes']) or any(e['from'] not in ids or e['to'] not in ids for e in view['edges']):
        raise ValueError('invalid graph view')
    return sorted(view['edges'], key=lambda r: r['to'])


def experiment():
    data, source_hash = frozen_data()
    task = lambda row: row['relation']
    # Identical data, different coordinates. Neither layout defines semantic edges.
    layouts = {
        'ALL_NEAR': {'II.9': [0, 0], 'II.6': [0, 1], 'II.7': [1, 0], 'II.8': [0, -1]},
        'PROOF_FAR': {'II.9': [0, 0], 'II.6': [1, 0], 'II.7': [3, 0], 'II.8': [0, 1]},
    }
    canonical = json.dumps(data, sort_keys=True, ensure_ascii=False).encode()
    result = {'status': 'FINITE_REPRESENTATION_CHECK', 'source_ref': SOURCE_REF,
              'source_path': SOURCE_PATH, 'source_sha256': source_hash,
              'data_sha256': digest(canonical), 'records': len(data),
              'task': 'EXACT_DECLARED_RELATION_KIND', 'radius': 1.5, 'layouts': {}}
    proof_targets = {r['to'] for r in data if r['relation'] == 'DEPENDS_ON'}
    assert proof_targets == {'II.7'}
    assert not lost_distinctions(data, lambda r: tuple(sorted(r.items())), task)
    for name, layout in layouts.items():
        view = json.loads(json.dumps(typed_graph(data, layout)))
        decoded = read_graph(view)
        assert decoded == data, 'typed representation changed the underlying records'
        assert {r['to'] for r in decoded if r['relation'] == 'DEPENDS_ON'} == proof_targets
        near = lambda row: math.dist(layout[row['from']], layout[row['to']]) <= 1.5
        collisions = lost_distinctions(data, near, task)
        assert collisions, 'negative control unexpectedly preserved all task distinctions'
        inferred = {r['to'] for r in data if near(r)}
        result['layouts'][name] = {
            'typed_roundtrip': 'EXACT', 'typed_task_answer': sorted(proof_targets),
            'nearness_only_adequate': False, 'lost_distinction_pairs': collisions,
            'nearness_as_proof_false_positives': sorted(inferred - proof_targets),
            'nearness_as_proof_false_negatives': sorted(proof_targets - inferred),
        }
    assert result['layouts']['PROOF_FAR']['nearness_as_proof_false_negatives'] == ['II.7']
    result['boundary'] = ('Checks a fixed finite dataset and explicit encodings. '
                          'Does not measure visual recognition, model memory, discovery, or graph superiority.')
    return result


if __name__ == '__main__':
    print(json.dumps(experiment(), ensure_ascii=False, indent=2))
