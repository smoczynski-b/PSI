#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from collections import defaultdict, deque
from pathlib import Path

from build_edge_provenance import extract_fragment

ROOT = Path(__file__).resolve().parents[1]
BASE_EVIDENCE = ROOT / "docs/memory/psi-memory-edge-evidence-01.tsv"
BASE_PROV = ROOT / "docs/memory/psi-memory-edge-provenance-spec-01.tsv"
BRIDGE_SPEC = ROOT / "docs/memory/psi-memory-edge-evidence-m8-bridge-spec-01.tsv"
BRIDGE_CERT = ROOT / "docs/memory/psi-memory-edge-evidence-m8-bridge-01.tsv"
BRIDGE_PROV = ROOT / "docs/memory/psi-memory-edge-provenance-m8-bridge-spec-01.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def blob_sha(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return subprocess.check_output(["git", "hash-object", str(rel)], cwd=ROOT, text=True).strip()


def current_record(row):
    path = ROOT / row["path"]
    fragment = extract_fragment(path, row["selector_type"], row["selector"])
    return {
        "evidence_id": row["evidence_id"],
        "path": row["path"],
        "selector_type": row["selector_type"],
        "selector": row["selector"],
        "git_blob_sha": blob_sha(path),
        "fragment_sha256": hashlib.sha256(fragment).hexdigest(),
        "fragment_bytes": len(fragment),
        "fragment": fragment.decode("utf-8"),
    }


def emit_bridge():
    print("PSI-MEMORY M8 BRIDGE CANDIDATE EVIDENCE")
    total = 0
    for row in read_tsv(BRIDGE_SPEC):
        r = current_record(row)
        total += r["fragment_bytes"]
        print("\t".join([r["evidence_id"], r["git_blob_sha"], r["fragment_sha256"], str(r["fragment_bytes"])]))
    print(f"bridge_fragments={len(read_tsv(BRIDGE_SPEC))} bytes={total}")


def validated_evidence():
    cert_rows = read_tsv(BASE_EVIDENCE) + read_tsv(BRIDGE_CERT)
    out = {}
    for row in cert_rows:
        cur = current_record(row)
        if cur["fragment_sha256"] != row["fragment_sha256"]:
            status = "STALE"
        elif cur["git_blob_sha"] != row["verified_git_blob_sha"]:
            status = "SOURCE_DRIFT"
        else:
            status = "VALID"
        cur["status"] = status
        out[row["evidence_id"]] = cur
    return out


def build_context(start: str, radius: int):
    evidence = validated_evidence()
    prov = read_tsv(BASE_PROV) + read_tsv(BRIDGE_PROV)
    adjacency = defaultdict(list)
    for edge in prov:
        ev = evidence.get(edge["evidence_id"])
        if ev and ev["status"] == "VALID":
            adjacency[edge["from"]].append(edge)

    dist = {start: 0}
    q = deque([start])
    selected_edges = []
    seen_edge_ids = set()
    while q:
        node = q.popleft()
        if dist[node] >= radius:
            continue
        for edge in sorted(adjacency[node], key=lambda x: x["edge_id"]):
            if edge["edge_id"] not in seen_edge_ids:
                selected_edges.append(edge)
                seen_edge_ids.add(edge["edge_id"])
            target = edge["to"]
            if target not in dist:
                dist[target] = dist[node] + 1
                q.append(target)

    ev_ids = sorted({e["evidence_id"] for e in selected_edges})
    fragments = [evidence[eid] for eid in ev_ids]
    nodes = sorted(dist, key=lambda n: (dist[n], n))
    return {
        "schema": "PSI-MEMORY-M8-CONTEXT-01",
        "anchor": start,
        "radius": radius,
        "nodes": [{"id": n, "distance": dist[n]} for n in nodes],
        "edges": [{k: e[k] for k in ("edge_id", "from", "relation", "to", "evidence_id")} for e in selected_edges],
        "evidence": [{
            "evidence_id": f["evidence_id"],
            "path": f["path"],
            "fragment_sha256": f["fragment_sha256"],
            "fragment_bytes": f["fragment_bytes"],
            "fragment": f["fragment"],
        } for f in fragments],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit-bridge-hashes", action="store_true")
    ap.add_argument("--start", default="GO-G4")
    ap.add_argument("--radius", type=int, default=3)
    ap.add_argument("--out")
    args = ap.parse_args()
    if args.emit_bridge_hashes:
        emit_bridge()
        return
    if not BRIDGE_CERT.exists():
        raise SystemExit("M8 bridge certificates not frozen yet")
    ctx = build_context(args.start, args.radius)
    text = json.dumps(ctx, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
    if args.out:
        (ROOT / args.out).write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
