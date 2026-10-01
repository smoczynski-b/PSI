#!/usr/bin/env python3
from __future__ import annotations

from statistics import median
from time import perf_counter_ns

from active_memory import compile_workspace, consolidate_workspace
from dependency_invalidation import DependencyIndex, full_scan_invalidated

CONTRACT = {
    "status": "COMPILED",
    "contract_id": "ACTIVE-MEMORY-INVALIDATION-01",
    "anchor": "ROOT",
    "task": "selectively invalidate derived memory after dependency change",
}
RETRIEVAL = {
    "status": "RETRIEVED",
    "anchor": "ROOT",
    "edges": [
        {"from": "ROOT", "relation": "DEPENDS_ON", "to": "A", "source": "doc:changing"},
        {"from": "A", "relation": "SUPPORT", "to": "B", "source": "forum:OID-REL"},
        {"from": "ROOT", "relation": "ANALOGY_TO", "to": "C", "source": "doc:stable"},
    ],
}
SIZES = (128, 1024, 8192, 32768)
REPEATS = 5


def core_records():
    ws = compile_workspace(CONTRACT, RETRIEVAL)
    snap = consolidate_workspace(ws, status="VALID")
    sid = snap["id"]
    records = {
        sid: tuple(snap["dependencies"]),
        "analysis:A": (f"record:{sid}",),
        "decision:B": ("record:analysis:A",),
        "independent:C": ("source:independent",),
    }
    return snap, sid, records


def make_index(records):
    idx = DependencyIndex()
    for rid, deps in records.items():
        idx.register(rid, deps)
    return idx


def main():
    snap, sid, base_records = core_records()
    expected = tuple(sorted((sid, "analysis:A", "decision:B")))

    assert "source:doc:changing" in snap["dependencies"]
    assert "source:forum:OID-REL" in snap["dependencies"]
    assert "edge:ROOT|DEPENDS_ON|A" in snap["dependencies"]

    direct = make_index(base_records)
    result = direct.invalidate({"source:doc:changing"})
    assert result.stale_records == expected
    assert result.examined_links == 3
    assert direct.status("independent:C") == "VALID"
    assert full_scan_invalidated(base_records, {"source:doc:changing"}) == expected

    forum = make_index(base_records)
    forum_result = forum.invalidate({"source:forum:OID-REL"})
    assert forum_result.stale_records == expected
    assert forum_result.examined_links == 3

    edge = make_index(base_records)
    edge_result = edge.invalidate({"edge:ROOT|DEPENDS_ON|A"})
    assert edge_result.stale_records == expected

    unknown = make_index(base_records)
    unknown_result = unknown.invalidate({"source:not-present"})
    assert unknown_result.stale_records == ()
    assert unknown_result.examined_links == 0

    rows = []
    for n in SIZES:
        records = dict(base_records)
        for i in range(n):
            records[f"noise:{i:06d}"] = (f"source:noise:{i:06d}",)

        indexed_times = []
        full_times = []
        for _ in range(REPEATS):
            idx = make_index(records)
            t0 = perf_counter_ns()
            indexed = idx.invalidate({"source:doc:changing"})
            t1 = perf_counter_ns()
            indexed_times.append(t1 - t0)
            assert indexed.stale_records == expected
            assert indexed.examined_links == 3

            t2 = perf_counter_ns()
            oracle = full_scan_invalidated(records, {"source:doc:changing"})
            t3 = perf_counter_ns()
            full_times.append(t3 - t2)
            assert oracle == indexed.stale_records

        it = int(median(indexed_times))
        ft = int(median(full_times))
        rows.append((n, it, ft))
        print(
            f"noise_records={n} total_records={len(records)} affected_records=3 "
            f"examined_links=3 indexed_median_ns={it} full_scan_median_ns={ft} "
            f"observed_ratio={ft / max(it, 1):.2f}"
        )

    assert rows[-1][0] / rows[0][0] == 256
    print("PSI-ACTIVE-MEMORY-INVALIDATION-01 PASS_WITH_BOUNDARY")
    print("transitive_selective_invalidation=PASS")
    print("full_scan_equivalence=PASS")
    print("forum_source_token_propagation=PASS")
    print("unrelated_records_untouched=PASS")
    print("indexed_work_accounting=3_dependency_links")
    print("timing_claim=MEASURED_NOT_PROOF")
    print("BOUNDARY: single-process deterministic dependency tokens; no concurrent writers, rollback, or live FORUM mutation")


if __name__ == "__main__":
    main()
