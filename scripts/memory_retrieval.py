#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
from collections import defaultdict, deque
from pathlib import Path
from build_edge_provenance import extract_fragment

ROOT = Path(__file__).resolve().parents[1]
ANCHOR = "II.9"
RADIUS = 2
EDGE_BUDGET = 12
CONTRACT = ROOT / "experiments/m12-task-contract.tsv"
TABLES = [
    ROOT / "docs/memory/psi-memory-edges-history-01.tsv",
    ROOT / "docs/memory/psi-memory-edges-relational-01.tsv",
    ROOT / "docs/memory/psi-memory-edges-bridges-01.tsv",
]
M9 = ROOT / "docs/memory/psi-memory-m9-verified-delta-01.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def git_blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def record_is_current(row, root=None):
    """Check the actual fragment and complete file bytes, not its stored label."""
    root = ROOT if root is None else Path(root)
    try:
        path = (root / row['path']).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            return False
        fragment = extract_fragment(path, row['selector_type'], row['selector'])
        return (hashlib.sha256(fragment).hexdigest() == row['fragment_sha256'] and
                git_blob(path) == row['verified_git_blob_sha'])
    except (OSError, KeyError, ValueError, AssertionError):
        return False


def certification_state():
    records = {}
    rejected = set()
    for evidence_name, provenance_name in [
        ('psi-memory-edge-evidence-01.tsv', 'psi-memory-edge-provenance-spec-01.tsv'),
        ('psi-memory-edge-evidence-m8-bridge-01.tsv', 'psi-memory-edge-provenance-m8-bridge-spec-01.tsv'),
    ]:
        evidence = ROOT / 'docs/memory' / evidence_name
        provenance = ROOT / 'docs/memory' / provenance_name
        if not evidence.is_file() or not provenance.is_file():
            continue
        valid = {row['evidence_id']: row for row in read_tsv(evidence)
                 if row.get('status') == 'VALID' and record_is_current(row)}
        for edge in read_tsv(provenance):
            triple = (edge['from'], edge['relation'], edge['to'])
            if edge['evidence_id'] in valid:
                records[triple] = valid[edge['evidence_id']]
            else:
                rejected.add(triple)
    for row in read_tsv(M9):
        if row['object_kind'] == 'EDGE':
            triple = (row['id_or_from'], row['relation_or_kind'], row['to_or_label'])
            if row['status'] == 'VERIFIED' and record_is_current(row):
                records[triple] = row
            else:
                rejected.add(triple)
    return records, rejected - records.keys()


def certified_records():
    return certification_state()[0]


def certified_triples():
    return set(certified_records())


def load_attested_edges():
    certificates, rejected = certification_state()
    by_triple = {}
    for table in TABLES:
        for row in read_tsv(table):
            source = row["source"]
            source_path = ROOT / source
            if not source.startswith("docs/") or not source_path.exists():
                continue
            triple = (row["from"], row["relation"], row["to"])
            if triple in rejected:
                continue
            payload = "\t".join([*triple, source, row.get("note", "")]).encode("utf-8")
            by_triple[triple] = {
                "from": row["from"],
                "relation": row["relation"],
                "to": row["to"],
                "source": source,
                "source_blob_sha": git_blob(source_path),
                "routing_attestation_sha256": hashlib.sha256(payload).hexdigest(),
                "attestation": "ROUTING_ATTESTED",
            }

    # A historical VERIFIED label does not survive a source edit automatically.
    for row in read_tsv(M9):
        if row["object_kind"] != "EDGE" or row["status"] != "VERIFIED" or not record_is_current(row):
            continue
        source = row["path"]
        source_path = ROOT / source
        assert source_path.exists()
        triple = (row["id_or_from"], row["relation_or_kind"], row["to_or_label"])
        by_triple[triple] = {
            "from": triple[0],
            "relation": triple[1],
            "to": triple[2],
            "source": source,
            "source_blob_sha": row["verified_git_blob_sha"],
            "routing_attestation_sha256": row["fragment_sha256"],
            "attestation": "VALID_FRAGMENT_CERT",
        }
    for triple, certificate in certificates.items():
        if triple in by_triple:
            by_triple[triple].update(
                attestation='VALID_FRAGMENT_CERT',
                source_blob_sha=certificate['verified_git_blob_sha'],
                routing_attestation_sha256=certificate['fragment_sha256'])
    return list(by_triple.values())


def local_pool(edges, anchor=ANCHOR, radius=RADIUS):
    undirected = defaultdict(set)
    for e in edges:
        undirected[e["from"]].add(e["to"])
        undirected[e["to"]].add(e["from"])
    dist = {anchor: 0}
    q = deque([anchor])
    while q:
        node = q.popleft()
        if dist[node] >= radius:
            continue
        for nxt in sorted(undirected[node]):
            if nxt not in dist:
                dist[nxt] = dist[node] + 1
                q.append(nxt)
    nodes = set(dist)
    pool = [e for e in edges if e["from"] in nodes and e["to"] in nodes]
    return nodes, pool, dist


def load_policy():
    rows = read_tsv(CONTRACT)
    return {
        r["relation"]: {
            "role": r["role"],
            "priority": int(r["priority"]),
            "expand": r["expand_target"] == "YES",
        }
        for r in rows
    }


def select(pool, policy, budget=EDGE_BUDGET, anchor=ANCHOR):
    outgoing = defaultdict(list)
    for e in pool:
        if e["relation"] in policy:
            outgoing[e["from"]].append(e)

    selected = []
    selected_triples = set()
    expanded = set()
    queued = {anchor}
    q = deque([anchor])

    while q and len(selected) < budget:
        node = q.popleft()
        queued.discard(node)
        if node in expanded:
            continue
        expanded.add(node)
        options = sorted(
            outgoing[node],
            key=lambda e: (-policy[e["relation"]]["priority"], e["relation"], e["to"], e["source"]),
        )
        for e in options:
            triple = (e["from"], e["relation"], e["to"])
            if triple in selected_triples:
                continue
            if len(selected) >= budget:
                break
            selected.append(e)
            selected_triples.add(triple)
            if policy[e["relation"]]["expand"] and e["to"] not in expanded and e["to"] not in queued:
                q.append(e["to"])
                queued.add(e["to"])
    return selected


def triples(edges):
    return {(e["from"], e["relation"], e["to"]) for e in edges}


def retrieve(contract):
    """Execute the declared anchor, policy, evidence mode and finite budget."""
    if contract.get('status') != 'COMPILED' or contract.get('stop_condition') == 'NO_RETRIEVAL':
        return {'status': 'NO_RETRIEVAL', 'reason': contract.get('status'), 'edges': []}
    anchor = contract.get('anchor')
    radius, budget = contract.get('local_radius'), contract.get('edge_budget')
    if (not isinstance(anchor, str) or not anchor or type(radius) is not int or radius < 0 or
            type(budget) is not int or budget < 0):
        raise ValueError('invalid anchor/radius/edge budget')
    mode = contract.get('attestation_mode')
    if mode not in {'VALID_FRAGMENT_CERT_ONLY', 'VALID_FRAGMENT_CERT_OR_ROUTING_ATTESTED'}:
        raise ValueError('unknown attestation mode')
    policy = {}
    for rule in contract['relation_policy']:
        if rule['relation'] in policy or type(rule['expand_target']) is not bool or type(rule['priority']) is not int:
            raise ValueError('invalid/duplicate relation policy')
        policy[rule['relation']] = {'role': rule['role'], 'priority': rule['priority'], 'expand': rule['expand_target']}
    edges = load_attested_edges()
    if mode == 'VALID_FRAGMENT_CERT_ONLY':
        edges = [edge for edge in edges if edge['attestation'] == 'VALID_FRAGMENT_CERT']
    _, pool, _ = local_pool(edges, anchor=anchor, radius=radius)
    # Probe one extra edge to distinguish exhausted frontier from budget truncation.
    probe = select(pool, policy, budget=budget + 1, anchor=anchor)
    return {'status': 'RETRIEVED', 'anchor': anchor, 'radius': radius,
            'edge_budget': budget, 'attestation_mode': mode,
            'budget_truncated': len(probe) > budget,
            'scope': 'DECLARED_LOCAL_VIEW', 'edges': probe[:budget]}


if __name__ == '__main__':
    import argparse
    import json
    from compile_multilingual_contract import compile_multilingual_task
    parser = argparse.ArgumentParser(description='Compile one bounded task and retrieve its declared memory view.')
    parser.add_argument('--language', choices=['PL', 'EN', 'DE'], default='PL')
    parser.add_argument('task')
    args = parser.parse_args()
    contract = compile_multilingual_task(args.task, args.language)
    print(json.dumps({'contract': contract, 'result': retrieve(contract)}, ensure_ascii=False, indent=2))
