#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORLD = ROOT / "experiments/m17-world-objects.tsv"
LEXICON = ROOT / "experiments/m17-lexical-partitions.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def world_rows():
    return read_tsv(WORLD)


def lexical_fibre(language: str, token: str) -> set[str] | None:
    for row in read_tsv(LEXICON):
        if row["language"] == language and row["token"] == token:
            return {x for x in row["candidate_world_ids"].split(",") if x}
    return None


def support(relation: str, allowed_values: set[str]) -> set[str]:
    rows = world_rows()
    if not rows or relation not in rows[0] or relation == "object_id":
        return set()
    return {
        row["object_id"]
        for row in rows
        if row[relation] in allowed_values
    }


def resolve_uncertain(
    language: str,
    token: str,
    observations: list[dict],
    max_conflicts: int = 0,
) -> dict:
    if max_conflicts < 0:
        raise ValueError("max_conflicts must be >= 0")

    initial = lexical_fibre(language, token)
    if initial is None:
        return {
            "status": "NO_LEXICAL_FIBRE",
            "language": language,
            "token": token,
            "max_conflicts": max_conflicts,
            "initial_fibre": None,
            "final_fibre": None,
            "trace": [],
            "violations": {},
        }

    seen_ids = set()
    normalized = []
    for obs in observations:
        obs_id = obs["observation_id"]
        if obs_id in seen_ids:
            raise ValueError(f"duplicate observation_id: {obs_id}")
        seen_ids.add(obs_id)
        allowed = set(obs["allowed_values"])
        if not allowed:
            raise ValueError(f"empty allowed_values: {obs_id}")
        normalized.append({
            "observation_id": obs_id,
            "relation": obs["relation"],
            "allowed_values": allowed,
            "support": support(obs["relation"], allowed),
        })

    violations = {x: [] for x in initial}
    active = set(initial)
    trace = [{"step": 0, "size": len(active), "fibre": sorted(active)}]

    for i, obs in enumerate(normalized, start=1):
        for x in initial:
            if x not in obs["support"]:
                violations[x].append(obs["observation_id"])
        before = set(active)
        active = {x for x in initial if len(violations[x]) <= max_conflicts}
        assert active <= before, "fixed-tolerance refinement must not resurrect candidates"
        trace.append({
            "step": i,
            "observation_id": obs["observation_id"],
            "relation": obs["relation"],
            "allowed_values": sorted(obs["allowed_values"]),
            "size": len(active),
            "fibre": sorted(active),
        })

    if not active:
        status = "INCONSISTENT"
    elif len(active) > 1:
        status = "UNRESOLVED"
    else:
        x = next(iter(active))
        status = "IDENTIFIED_EXACT" if not violations[x] else "IDENTIFIED_WITH_TOLERANCE"

    return {
        "status": status,
        "language": language,
        "token": token,
        "max_conflicts": max_conflicts,
        "initial_fibre": sorted(initial),
        "final_fibre": sorted(active),
        "trace": trace,
        "violations": {x: list(violations[x]) for x in sorted(active)},
    }
