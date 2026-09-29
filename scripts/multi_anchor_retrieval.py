#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict, deque
import json
import re
import sys

from compile_task_contract import detect_intents, unsupported_exclusion
from compose_task_contract import (
    build_policy,
    detect_anchors,
    intent_budget,
    strict_cert_mode,
)
import memory_retrieval as memory

COMPARE_MARKERS = ("porownaj", "porownanie")
INTERSECT_MARKERS = ("wspolne", "wspolna", "przeciecie", "czesc wspolna")
TRANSFER_MARKERS = ("przenies", "transfer")


def _fold(text: str) -> str:
    from compile_task_contract import ascii_fold
    return ascii_fold(text)


def detect_operator(task: str) -> str | None:
    folded = _fold(task)
    hits = []
    if any(marker in folded for marker in COMPARE_MARKERS):
        hits.append("COMPARE")
    if any(marker in folded for marker in INTERSECT_MARKERS):
        hits.append("INTERSECT")
    if any(marker in folded for marker in TRANSFER_MARKERS):
        hits.append("TRANSFER")
    return hits[0] if len(hits) == 1 else None


def compile_multi_anchor_task(task: str) -> dict:
    anchors = detect_anchors(task)
    intents = detect_intents(task)
    operator = detect_operator(task)
    strict = strict_cert_mode(task)
    base = {
        "task": task,
        "anchors": anchors,
        "operator": operator,
        "intents": intents,
        "relation_policy": [],
        "local_radius": None,
        "per_anchor_edge_budget": None,
        "route_budget": None,
        "stop_condition": "NO_RETRIEVAL",
        "attestation_mode": "VALID_FRAGMENT_CERT_ONLY" if strict else "VALID_FRAGMENT_CERT_OR_ROUTING_ATTESTED",
        "compiler": "MULTI-ANCHOR-01",
    }
    if unsupported_exclusion(task):
        return {**base, "status": "NEEDS_CONTRACT", "conflicts": ["UNSUPPORTED_EXCLUSION"]}
    if len(anchors) != 2:
        status = "NEEDS_ANCHOR_POLICY" if len(anchors) > 1 else "NEEDS_ANCHOR"
        return {**base, "status": status, "conflicts": ["EXACTLY_TWO_ANCHORS_REQUIRED"]}
    if operator is None:
        return {**base, "status": "NEEDS_ANCHOR_POLICY", "conflicts": ["MULTIPLE_ANCHORS_WITHOUT_OPERATOR"]}
    if not intents:
        return {**base, "status": "NEEDS_CONTRACT", "conflicts": ["MISSING_TASK_INTENT"]}
    budget = intent_budget(intents)
    return {
        **base,
        "status": "COMPILED",
        "relation_policy": build_policy(intents),
        "local_radius": 2,
        "per_anchor_edge_budget": budget,
        "route_budget": 2,
        "stop_condition": "OPERATOR_COMPLETE_OR_BUDGET_EXHAUSTED",
        "conflicts": [],
    }


def _single_contract(contract: dict, anchor: str) -> dict:
    return {
        "status": "COMPILED",
        "task": contract["task"],
        "anchor": anchor,
        "intents": contract["intents"],
        "relation_policy": contract["relation_policy"],
        "local_radius": contract["local_radius"],
        "edge_budget": contract["per_anchor_edge_budget"],
        "stop_condition": "EDGE_BUDGET_OR_FRONTIER_EXHAUSTED",
        "attestation_mode": contract["attestation_mode"],
        "compiler": contract["compiler"],
    }


def _edge_key(edge: dict) -> tuple[str, str, str]:
    return edge["from"], edge["relation"], edge["to"]


def _allowed_edges(contract: dict) -> list[dict]:
    relations = {rule["relation"] for rule in contract["relation_policy"]}
    edges = [e for e in memory.load_attested_edges() if e["relation"] in relations]
    if contract["attestation_mode"] == "VALID_FRAGMENT_CERT_ONLY":
        edges = [e for e in edges if e["attestation"] == "VALID_FRAGMENT_CERT"]
    return edges


def _direct_cross_edges(contract: dict, a: str, b: str) -> list[dict]:
    allowed = {a, b}
    return sorted(
        [e for e in _allowed_edges(contract) if e["from"] in allowed and e["to"] in allowed],
        key=_edge_key,
    )


def _directed_route(contract: dict, source: str, target: str) -> list[dict] | None:
    expandable = {rule["relation"] for rule in contract["relation_policy"] if rule["expand_target"]}
    edges = [e for e in _allowed_edges(contract) if e["relation"] in expandable]
    outgoing = defaultdict(list)
    for edge in edges:
        outgoing[edge["from"]].append(edge)
    for node in outgoing:
        outgoing[node].sort(key=_edge_key)

    budget = contract["route_budget"]
    queue = deque([(source, [])])
    visited_depth = {source: 0}
    while queue:
        node, path = queue.popleft()
        if len(path) >= budget:
            continue
        for edge in outgoing[node]:
            nxt = edge["to"]
            new_path = path + [edge]
            if nxt == target:
                return new_path
            depth = len(new_path)
            if depth < visited_depth.get(nxt, budget + 1):
                visited_depth[nxt] = depth
                queue.append((nxt, new_path))
    return None


def execute_multi_anchor(contract: dict) -> dict:
    if contract.get("status") != "COMPILED" or contract.get("stop_condition") == "NO_RETRIEVAL":
        return {"status": "NO_RETRIEVAL", "reason": contract.get("status"), "operator": contract.get("operator")}
    anchors = contract.get("anchors")
    if not isinstance(anchors, list) or len(anchors) != 2 or anchors[0] == anchors[1]:
        raise ValueError("multi-anchor execution requires two distinct anchors")
    if type(contract.get("per_anchor_edge_budget")) is not int or contract["per_anchor_edge_budget"] < 0:
        raise ValueError("invalid per-anchor budget")
    if type(contract.get("route_budget")) is not int or contract["route_budget"] < 1:
        raise ValueError("invalid route budget")

    a, b = anchors
    operator = contract["operator"]
    views = {
        a: memory.retrieve(_single_contract(contract, a)),
        b: memory.retrieve(_single_contract(contract, b)),
    }

    if operator == "COMPARE":
        return {
            "status": "RETRIEVED",
            "operator": operator,
            "anchors": anchors,
            "budget_mode": "EQUAL_PER_ANCHOR",
            "per_anchor_edge_budget": contract["per_anchor_edge_budget"],
            "views": views,
            "cross_edges": _direct_cross_edges(contract, a, b),
        }

    if operator == "INTERSECT":
        by_a = {_edge_key(e): e for e in views[a]["edges"]}
        by_b = {_edge_key(e): e for e in views[b]["edges"]}
        common = sorted(set(by_a) & set(by_b))
        common_nodes = sorted({n for t in common for n in (t[0], t[2])})
        return {
            "status": "RETRIEVED",
            "operator": operator,
            "anchors": anchors,
            "budget_mode": "EQUAL_PER_ANCHOR",
            "per_anchor_edge_budget": contract["per_anchor_edge_budget"],
            "views": views,
            "common_edges": [by_a[t] for t in common],
            "common_nodes": common_nodes,
        }

    if operator == "TRANSFER":
        route = _directed_route(contract, a, b)
        if route is None:
            return {
                "status": "NO_ROUTE",
                "operator": operator,
                "source": a,
                "target": b,
                "route_budget": contract["route_budget"],
                "transferred_view": None,
            }
        return {
            "status": "RETRIEVED",
            "operator": operator,
            "source": a,
            "target": b,
            "route_budget": contract["route_budget"],
            "route": route,
            "transferred_view": views[b],
        }

    raise ValueError("unknown multi-anchor operator")


def canonical_signature(result: dict) -> dict:
    """Order-insensitive signature for symmetric operators."""
    operator = result.get("operator")
    if operator == "COMPARE":
        view_sigs = {
            anchor: sorted(_edge_key(e) for e in view["edges"])
            for anchor, view in result["views"].items()
        }
        return {
            "operator": operator,
            "views": dict(sorted(view_sigs.items())),
            "cross": sorted(_edge_key(e) for e in result["cross_edges"]),
        }
    if operator == "INTERSECT":
        return {
            "operator": operator,
            "common": sorted(_edge_key(e) for e in result["common_edges"]),
            "nodes": sorted(result["common_nodes"]),
        }
    return result


def main(argv: list[str]) -> int:
    task = " ".join(argv[1:]).strip()
    if not task:
        print("usage: multi_anchor_retrieval.py <natural-language task>", file=sys.stderr)
        return 2
    contract = compile_multi_anchor_task(task)
    print(json.dumps({"contract": contract, "result": execute_multi_anchor(contract)}, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
