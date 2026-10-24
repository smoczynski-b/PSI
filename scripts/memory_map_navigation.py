#!/usr/bin/env python3
"""Pinned navigation overlay; never a source of validity effects."""
from __future__ import annotations

import csv
import hashlib
import re
import subprocess
from pathlib import Path

MAP_COMMIT = "38adb94c7f1f99374621017c33fbe4048602d922"
MEM = "docs/memory/"
NODES = [MEM + name for name in (
    "psi-memory-nodes-01.tsv", "psi-memory-nodes-history-01.tsv",
    "psi-memory-nodes-bridges-01.tsv",
    "psi-memory-nodes-math-migration-20261024.tsv")]
EDGES = [MEM + name for name in (
    "psi-memory-edges-history-01.tsv", "psi-memory-edges-bridges-01.tsv",
    "psi-memory-edges-math-migration-20261024.tsv")]
PINS = {
    NODES[-1]: "398a42112b2a2737df8fcb080957c78f23bc7378",
    EDGES[-1]: "b52f40072d52deacc5accef22c23566c9f2d46e3",
    MEM + "PSI-MEMORY-MAP-01.md": "d876f85b814d09b68e39f09c1b8311a0ca2d4c02",
}
LAYERS = {"INDEX", "EDITORIAL", "SCOPE", "EVIDENCE", "CANDIDATE"}
KINDS = {"EDITORIAL_MAP", "ERRATA", "INDEPENDENT_REVIEW", "RESEARCH_BLOCK",
         "RESEARCH_CLAIM", "RESEARCH_RANGE", "SOURCE_INDEX"}
STATUSES = {
    "ACTIVE_SCOPE_CORRECTION", "ACTIVE_SOURCE_CORRECTION", "CANDIDATE_NON_CORE",
    "E001_ACCEPTED_PROOF_SCOPED", "E001_ACCEPTED_PROOF_SCOPED_ENUM_NOT_RERUN",
    "LOGICAL_SCOPE_REVIEW_RECORDED", "PASS_SCOPED_ACCEPTED_PROOF_ONLY",
    "SCOPE_PENDING", "SELF_CHECKED_CANDIDATE_SECTION_COMPLETE",
    "SELF_CHECKED_REVIEW_PENDING", "SELF_CHECKED_SCOPE_CORRECTED_REVIEW_PENDING",
    "VERSIONED_EDITORIAL",
}


class MapHold(ValueError):
    """Unusable input; no partial answer may be promoted."""


def strict_rows(path, fields):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if reader.fieldnames != fields:
            raise MapHold(f"SCHEMA: {path.name}")
        rows = list(reader)
    for row in rows:
        if set(row) != set(fields) or any(
                not isinstance(v, str) or not v.strip() for v in row.values()):
            raise MapHold(f"MISSING_FIELD: {path.name}")
    if not rows:
        raise MapHold(f"EMPTY_TABLE: {path.name}")
    return rows


def git_value(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args],
                            capture_output=True, text=True, encoding="utf-8")
    if result.returncode:
        raise MapHold("COMMIT_OR_BLOB_UNAVAILABLE")
    return result.stdout.strip()


def verify_pins(root):
    if git_value(root, "rev-parse", "--verify", MAP_COMMIT + "^{commit}") != MAP_COMMIT:
        raise MapHold("COMMIT_MISMATCH")
    pins = {}
    for name in [*NODES, *EDGES, MEM + "PSI-MEMORY-MAP-01.md"]:
        expected = git_value(root, "rev-parse", "--verify", MAP_COMMIT + ":" + name)
        if name in PINS and expected != PINS[name]:
            raise MapHold("DECLARED_BLOB_MISMATCH: " + name)
        data = (root / name).read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if actual != expected:
            raise MapHold("WORKTREE_BLOB_MISMATCH: " + name)
        pins[name] = actual
    return pins


def load_map(root):
    root = Path(root)
    nodes, overlay_ids = {}, set()
    for name in NODES:
        for row in strict_rows(root / name, ["id", "kind", "status", "source", "label"]):
            if row["id"] in nodes:
                raise MapHold("DUPLICATE_NODE: " + row["id"])
            if name == NODES[-1]:
                if row["kind"] not in KINDS or row["status"] not in STATUSES:
                    raise MapHold("INVALID_NODE_TYPE_OR_STATUS")
                overlay_ids.add(row["id"])
            nodes[row["id"]] = row
    validity, navigation = [], []
    for name in EDGES:
        overlay = name == EDGES[-1]
        discriminator = "layer" if overlay else "effect"
        rows = strict_rows(root / name,
                           ["from", "relation", "to", discriminator, "source", "note"])
        for row in rows:
            if row["from"] not in nodes or row["to"] not in nodes:
                raise MapHold("UNKNOWN_ENDPOINT")
            if not re.fullmatch(r"[A-Z][A-Z0-9_]*", row["relation"]):
                raise MapHold("INVALID_RELATION_TYPE")
            if overlay:
                if row["layer"] not in LAYERS:
                    raise MapHold("INVALID_LAYER")
                navigation.append(row)
            else:
                if row["effect"] not in {"NONE", "VALIDITY", "BRIDGE_VALIDITY"}:
                    raise MapHold("INVALID_EFFECT")
                # Even an edited legacy table cannot grant overlay nodes validity.
                if row["from"] in overlay_ids or row["to"] in overlay_ids:
                    raise MapHold("OVERLAY_IN_VALIDITY_GRAPH")
                validity.append(row)
    pins = verify_pins(root)
    return nodes, navigation, validity, pins


def query_map(root, anchor=None, revoked=None):
    """Read locators/metadata, or simulate revocation. Never fetch or execute source text."""
    from memory_retrieval import local_pool
    from test_memory_map import stale_closure

    try:
        nodes, navigation, validity, pins = load_map(root)
        selected = revoked if revoked is not None else anchor
        if selected not in nodes:
            raise MapHold("UNKNOWN_NODE")
        provenance = {"source_commit": MAP_COMMIT, "input_blobs": pins}
        if revoked is not None:
            return {
                "status": "SIMULATED", "scope": "LEGACY_VALIDITY_ONLY",
                "revoked": [revoked], "stale": sorted(stale_closure({revoked}, validity)),
                "overlay_participates_in_validity": False, **provenance,
            }
        visible, edges, distances = local_pool(navigation, anchor=anchor, radius=2)
        return {
            "status": "SOURCE_SEEN", "scope": "PINNED_NAVIGATION_METADATA_ONLY",
            "anchor": anchor, "radius": 2, "traversal": "INCIDENCE",
            "edge_direction": "ORIGINAL_FROM_TO",
            "nodes": [nodes[key] for key in sorted(visible)],
            "edges": edges, "distances": distances,
            "source_bodies_fetched": False, "enumeration_rerun": False,
            "validity_effects_inferred": False, **provenance,
        }
    except (MapHold, OSError, UnicodeError, csv.Error) as exc:
        return {"status": "HOLD", "reason": str(exc), "scope": "NO_PARTIAL_RESULT"}


def cli_result(args, root):
    if args.revoke is not None:
        if args.task is not None or args.map_node is not None:
            return {"status": "HOLD", "reason": "CONFLICTING_QUERY_MODES"}
        return query_map(root, revoked=args.revoke)
    if args.map_node is not None:
        if args.task is not None:
            return {"status": "HOLD", "reason": "CONFLICTING_QUERY_MODES"}
        return query_map(root, anchor=args.map_node)
    if args.task and args.task.startswith("MATH-") and not any(c.isspace() for c in args.task):
        return query_map(root, anchor=args.task)
    return None
