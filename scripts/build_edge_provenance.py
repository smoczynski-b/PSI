#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_SPEC = ROOT / "docs/memory/psi-memory-edge-evidence-spec-01.tsv"
EDGE_SPEC = ROOT / "docs/memory/psi-memory-edge-provenance-spec-01.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def extract_fragment(path: Path, selector_type: str, selector: str) -> bytes:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if selector_type == "exact_line":
        matches = [line for line in lines if line.rstrip("\r\n") == selector]
        if len(matches) != 1:
            raise AssertionError(f"exact_line selector must match exactly once: {path}: {selector!r}; got {len(matches)}")
        fragment = matches[0]
        if not fragment.endswith(("\n", "\r")):
            fragment += "\n"
        return fragment.replace("\r\n", "\n").encode("utf-8")

    if selector_type == "heading":
        target_level = len(selector) - len(selector.lstrip("#"))
        starts = [i for i, line in enumerate(lines) if line.rstrip("\r\n") == selector]
        if len(starts) != 1:
            raise AssertionError(f"heading selector must match exactly once: {path}: {selector!r}; got {len(starts)}")
        start = starts[0]
        end = len(lines)
        for i in range(start + 1, len(lines)):
            stripped = lines[i].lstrip()
            if not stripped.startswith("#"):
                continue
            head = stripped.rstrip("\r\n")
            level = len(head) - len(head.lstrip("#"))
            if level <= target_level and len(head) > level and head[level] == " ":
                end = i
                break
        fragment = "".join(lines[start:end]).replace("\r\n", "\n")
        if not fragment.endswith("\n"):
            fragment += "\n"
        return fragment.encode("utf-8")

    raise AssertionError(f"unsupported selector_type: {selector_type}")


def git_blob_sha(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return subprocess.check_output(["git", "hash-object", str(rel)], cwd=ROOT, text=True).strip()


def load_declared_edges():
    edges = set()
    for path in sorted((ROOT / "docs/memory").glob("psi-memory-edges*.tsv")):
        for row in read_tsv(path):
            if {"from", "relation", "to"}.issubset(row):
                edges.add((row["from"], row["relation"], row["to"]))
    return edges


def build_records():
    evidence_rows = read_tsv(EVIDENCE_SPEC)
    edge_rows = read_tsv(EDGE_SPEC)
    declared_edges = load_declared_edges()

    evidence_ids = {row["evidence_id"] for row in evidence_rows}
    if len(evidence_ids) != len(evidence_rows):
        raise AssertionError("duplicate evidence_id")

    for edge in edge_rows:
        triple = (edge["from"], edge["relation"], edge["to"])
        if triple not in declared_edges:
            raise AssertionError(f"provenance spec references undeclared edge: {triple}")
        if edge["evidence_id"] not in evidence_ids:
            raise AssertionError(f"unknown evidence_id: {edge['evidence_id']}")

    out = []
    for row in evidence_rows:
        path = ROOT / row["path"]
        fragment = extract_fragment(path, row["selector_type"], row["selector"])
        out.append({
            "evidence_id": row["evidence_id"],
            "path": row["path"],
            "selector_type": row["selector_type"],
            "selector": row["selector"],
            "git_blob_sha": git_blob_sha(path),
            "fragment_sha256": hashlib.sha256(fragment).hexdigest(),
            "fragment_bytes": str(len(fragment)),
        })
    return out, edge_rows


def write_tsv(records, out_path: Path):
    fields = ["evidence_id", "path", "selector_type", "selector", "git_blob_sha", "fragment_sha256", "fragment_bytes"]
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(records)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--emit", action="store_true")
    args = ap.parse_args()

    records, edge_rows = build_records()
    if args.out:
        write_tsv(records, ROOT / args.out)
    if args.emit or not args.out:
        print("PSI-MEMORY M7 CANDIDATE EVIDENCE")
        for r in records:
            print("\t".join([r["evidence_id"], r["git_blob_sha"], r["fragment_sha256"], r["fragment_bytes"]]))
        print(f"edges={len(edge_rows)} evidence_fragments={len(records)}")


if __name__ == "__main__":
    main()
