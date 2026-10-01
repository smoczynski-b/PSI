#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from build_memory_pack import ROOT, build_pack, render

BROAD_MANIFEST = ROOT / "experiments" / "m4-broad-manifest.txt"
SNAPSHOT = ROOT / "experiments" / "m5-generated-manifest.txt"
CRITICAL = {
    "docs/go-memory-regression-01.md",
    "docs/principia-v2-04-representation-adequacy.md",
    "docs/principia-v2-07-exact-history-memory-adequacy.md",
    "docs/principia-v2-09-recursive-history-quotient-update.md",
}
EXPECTED_VIEW = {"C57", "C58", "GO-G4", "GO-MEMORY-REGRESSION", "II.4", "II.7", "II.9"}


def read_manifest(path: Path) -> list[str]:
    result: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            result.append(line)
    return result


def total_bytes(paths: list[str]) -> int:
    return sum((ROOT / p).stat().st_size for p in paths)


def main() -> None:
    view, generated, external = build_pack("GO-G4", 3)
    text = render("GO-G4", 3)

    assert set(view) == EXPECTED_VIEW, f"unexpected generated view: {view}"
    assert not external, f"unexpected unresolved/external sources: {external}"
    assert CRITICAL <= set(generated), f"generated pack lost critical sources: {CRITICAL - set(generated)}"
    assert text == SNAPSHOT.read_text(encoding="utf-8"), "M5 generated manifest drifted"

    broad = read_manifest(BROAD_MANIFEST)
    broad_bytes = total_bytes(broad)
    generated_source_bytes = total_bytes(generated)
    generated_total_bytes = generated_source_bytes + len(text.encode("utf-8"))
    ratio = generated_total_bytes / broad_bytes

    # Same engineering gate as M4a: automatic selection must still cut raw input by >=50%.
    assert ratio <= 0.5, (
        f"automatic pack missed 50% gate: {generated_total_bytes}/{broad_bytes}={ratio:.3f}"
    )

    print("PSI-MEMORY M5 PASS")
    print(f"view nodes={len(view)} source_files={len(generated)}")
    print(f"broad bytes={broad_bytes}")
    print(f"generated source bytes={generated_source_bytes}")
    print(f"generated manifest bytes={len(text.encode('utf-8'))}")
    print(f"generated/broad={ratio:.4f}; reduction={1-ratio:.2%}")
    if "docs/claim-registry.md" in generated:
        print("M5 granularity witness: C57/C58 pull full docs/claim-registry.md")


if __name__ == "__main__":
    main()
