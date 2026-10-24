#!/usr/bin/env python3
"""Acceptance of the ordinary CLI, including fail-closed corrupted copies."""
from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from memory_map_navigation import EDGES, MAP_COMMIT, MEM, NODES, PINS
from test_memory_map import read_edges, stale_closure

ROOT = Path(__file__).resolve().parents[1]


def cli(root, *args):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    process = subprocess.run(
        [sys.executable, "-B", str(root / "scripts/memory_retrieval.py"), *args],
        cwd=root, capture_output=True, text=True, encoding="utf-8", env=env)
    assert not process.stderr, process.stderr
    result = json.loads(process.stdout)
    assert process.returncode == (2 if result["status"] == "HOLD" else 0), result
    return result


def edit_cell(root, name, field, value):
    path = root / name
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields, rows = reader.fieldnames, list(reader)
    rows[0][field] = value
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run():
    results = {}
    m57 = results["ordinary_MATH_57"] = cli(ROOT, "MATH-57")
    assert m57["status"] == "SOURCE_SEEN"
    nodes = {node["id"]: node for node in m57["nodes"]}
    for node_id, source_id in [
            ("MATH-57", "6351600087"), ("MATH-57-ERRATA", "6351774428"),
            ("MATH-61", "6351811767")]:
        assert nodes[node_id]["source"].endswith("issuecomment-" + source_id)
    assert nodes["MATH-57-ERRATA"]["status"] == "ACTIVE_SCOPE_CORRECTION"
    assert "(A,Used)" in nodes["MATH-57-ERRATA"]["label"]
    assert "(A,Used)" in nodes["MATH-61"]["label"]
    assert max(m57["distances"].values()) <= 2
    assert all("effect" not in e for e in m57["edges"])
    with (ROOT / EDGES[-1]).open(encoding="utf-8", newline="") as stream:
        original = list(csv.DictReader(stream, delimiter="\t"))
    assert all(edge in original for edge in m57["edges"])
    assert any(e["relation"] == "HAS_ERRATA" and e["from"] == "MATH-57"
               and e["to"] == "MATH-57-ERRATA" for e in m57["edges"])
    assert any(e["relation"] == "QUALIFIES_SCOPE_OF"
               and e["from"] == "MATH-57-ERRATA" for e in m57["edges"])
    assert any(e["from"] == "MATH-61" and e["to"] in {"MATH-57", "MATH-57-ERRATA"}
               for e in m57["edges"])

    m69 = results["ordinary_MATH_69"] = cli(ROOT, "MATH-69")
    assert m69["status"] == "SOURCE_SEEN"
    nodes69 = {n["id"]: n for n in m69["nodes"]}
    assert nodes69["MATH-69"]["source"].endswith("6352758335")
    assert nodes69["MATH-69"]["status"] == "E001_ACCEPTED_PROOF_SCOPED_ENUM_NOT_RERUN"
    review = [n for n in m69["nodes"] if n["source"].endswith("6353231221")]
    assert review and all(n["kind"] == "INDEPENDENT_REVIEW" for n in review)
    assert not m69["enumeration_rerun"] and not m69["source_bodies_fetched"]

    for root in ("MATH-57-ERRATA", "MATH-61"):
        result = results["revoke_" + root] = cli(ROOT, "--revoke", root)
        assert result["status"] == "SIMULATED" and result["stale"] == []

    legacy = results["revoke_C57"] = cli(ROOT, "--revoke", "C57")
    assert legacy["status"] == "SIMULATED"
    assert set(legacy["stale"]) == stale_closure({"C57"}, read_edges())
    required = {"C58", "II.7", "C42", "II.8", "C44", "II.9", "C45",
                "C59", "II.11.PSI-BRIDGE", "C18"}
    assert required <= set(legacy["stale"])
    assert not any(node.startswith("MATH-") for node in legacy["stale"])

    results["unknown_query"] = cli(ROOT, "MATH-UNKNOWN")
    assert results["unknown_query"]["status"] == "HOLD"
    for args in [("--revoke", "C57", "MATH-57"), ("--map-node", "MATH-57", "MATH-69")]:
        assert cli(ROOT, *args)["status"] == "HOLD"

    cases = [
        ("missing_field", NODES[-1], "label", "", "MISSING_FIELD"),
        ("invalid_node_type", NODES[-1], "kind", "INVALID", "INVALID_NODE_TYPE"),
        ("invalid_layer", EDGES[-1], "layer", "VALIDITY", "INVALID_LAYER"),
        ("unknown_endpoint", EDGES[-1], "to", "MATH-UNKNOWN", "UNKNOWN_ENDPOINT"),
        ("invalid_effect", EDGES[0], "effect", "SCOPE", "INVALID_EFFECT"),
        ("invalid_relation", EDGES[-1], "relation", "invalid", "INVALID_RELATION_TYPE"),
        ("bad_blob", NODES[-1], "label", "Modified valid label", "WORKTREE_BLOB_MISMATCH"),
        ("missing_header", None, None, None, "SCHEMA"),
        ("bad_commit", None, None, None, "COMMIT_OR_BLOB_UNAVAILABLE"),
        ("bad_declared_blob", None, None, None, "DECLARED_BLOB_MISMATCH"),
    ]
    for case, name, field, value, reason in cases:
        with tempfile.TemporaryDirectory(prefix="psi-map-acceptance-") as temp:
            fixture = Path(temp)
            for rel in [*NODES, *EDGES, MEM + "PSI-MEMORY-MAP-01.md"]:
                dst = fixture / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / rel, dst)
            (fixture / "scripts").mkdir()
            for script in ("memory_retrieval.py", "memory_map_navigation.py",
                           "build_edge_provenance.py", "test_memory_map.py"):
                shutil.copyfile(ROOT / "scripts" / script, fixture / "scripts" / script)
            git_dir = subprocess.check_output(
                ["git", "-C", str(ROOT), "rev-parse", "--absolute-git-dir"],
                text=True, encoding="utf-8").strip()
            # Read-only object access to the pinned original; never commit fixtures.
            (fixture / ".git").write_text("gitdir: " + git_dir + "\n", encoding="utf-8")
            if name:
                edit_cell(fixture, name, field, value)
            elif case == "missing_header":
                path = fixture / EDGES[-1]
                path.write_text(path.read_text(encoding="utf-8").replace(
                    "from\trelation\tto\tlayer\tsource\tnote",
                    "from\trelation\tto\tsource\tnote", 1), encoding="utf-8")
            else:
                path = fixture / "scripts/memory_map_navigation.py"
                text = path.read_text(encoding="utf-8")
                old = MAP_COMMIT if case == "bad_commit" else PINS[NODES[-1]]
                path.write_text(text.replace(old, "f" * 40), encoding="utf-8")
            result = results[case] = cli(fixture, "MATH-57")
            assert result["status"] == "HOLD", (case, result)
            assert reason in result["reason"], (case, result)
            assert "nodes" not in result and "edges" not in result

    for script in ("test_memory_map.py", "test_m13_task_to_contract.py"):
        process = subprocess.run([sys.executable, "-B", str(ROOT / "scripts" / script)],
                                 cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                                 env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        assert process.returncode == 0, (script, process.stdout, process.stderr)
        results[script] = {"exit_code": process.returncode, "stdout": process.stdout}
    return {"status": "PASS_SCOPED", "scope": "LOCAL_ORDINARY_CLI_ACCEPTANCE",
            "source_commit": MAP_COMMIT, "enumeration_rerun": False,
            "production_deployment_certified": False, "results": results}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    receipt = run()
    if args.receipt:
        args.receipt.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
                                encoding="utf-8", newline="\n")
    print(json.dumps({"status": receipt["status"], "checks": list(receipt["results"]),
                      "scope": receipt["scope"]}, ensure_ascii=False, indent=2))
