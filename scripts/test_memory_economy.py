#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BROAD = ROOT / "experiments" / "m4-broad-manifest.txt"
GUIDED = ROOT / "experiments" / "m4-guided-manifest.txt"

CRITICAL = {
    "docs/go-memory-regression-01.md",
    "docs/principia-v2-04-representation-adequacy.md",
    "docs/principia-v2-07-exact-history-memory-adequacy.md",
    "docs/principia-v2-09-recursive-history-quotient-update.md",
}


def read_manifest(path: Path) -> list[str]:
    items: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        items.append(line)
    assert len(items) == len(set(items)), f"duplicate entries in {path}"
    return items


def stats(items: list[str]) -> tuple[int, int, int]:
    total_bytes = 0
    total_lines = 0
    for rel in items:
        path = ROOT / rel
        assert path.is_file(), f"missing manifest file: {rel}"
        data = path.read_bytes()
        total_bytes += len(data)
        total_lines += data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)
    return len(items), total_bytes, total_lines


def main() -> None:
    broad = read_manifest(BROAD)
    guided = read_manifest(GUIDED)

    assert CRITICAL <= set(broad), f"broad pack lost critical sources: {CRITICAL - set(broad)}"
    assert CRITICAL <= set(guided), f"guided pack lost critical sources: {CRITICAL - set(guided)}"

    broad_files, broad_bytes, broad_lines = stats(broad)
    guided_files, guided_bytes, guided_lines = stats(guided)

    assert broad_bytes > 0 and guided_bytes > 0
    ratio = guided_bytes / broad_bytes
    reduction = 1.0 - ratio

    # Frozen M4a success condition from PSI-MEMORY-M4-01.
    assert ratio <= 0.5, (
        f"M4a compression target missed: guided/broad={ratio:.3f} "
        f"({guided_bytes}/{broad_bytes} bytes)"
    )

    print("PSI-MEMORY M4a PASS")
    print(f"broad:  files={broad_files} bytes={broad_bytes} lines={broad_lines}")
    print(f"guided: files={guided_files} bytes={guided_bytes} lines={guided_lines}")
    print(f"guided/broad bytes={ratio:.4f}; reduction={reduction:.2%}")
    print("M4b NOT RUN: requires two independent model executions")


if __name__ == "__main__":
    main()
