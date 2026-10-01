#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from email import policy
from email.parser import BytesParser
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "docs/memory/arch-lang-fragment-cert-01.tsv"
RECOVERY = ROOT / "docs/memory/arch-lang-source-recovery-01.tsv"


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def html_payloads(path: Path) -> list[str]:
    msg = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
    payloads = []
    for part in msg.walk():
        if part.get_content_type() == "text/html":
            raw = part.get_payload(decode=True)
            if raw is None:
                continue
            payloads.append(raw.decode("utf-8", errors="strict"))
    if not payloads:
        raise ValueError(f"no text/html MIME part: {path}")
    return payloads


def validate_registry(rows, recovery):
    ids = [row["evidence_id"] for row in rows]
    assert len(ids) == len(set(ids)), "duplicate evidence id"
    recovered = {row["archive_id"]: row for row in recovery}
    for row in rows:
        assert row["archive_id"] in recovered, f"unknown archive id: {row['archive_id']}"
        assert row["selector_type"] == "exact_utf8_html_substring"
        fragment = row["selector"].encode("utf-8")
        assert sha256_bytes(fragment) == row["fragment_sha256"], row["evidence_id"]
        assert len(fragment) == int(row["fragment_bytes"]), row["evidence_id"]
        assert int(row["expected_occurrences"]) >= 1
        assert len(row["source_sha256"]) == 64
        assert row["source_sha256"] in recovered[row["archive_id"]]["content_sha256_or_note"], (
            "certificate source hash not bound in recovery registry: " + row["evidence_id"]
        )
        assert row["status"] == "FROZEN_SELECTOR"


def map_sources(source_dir: Path) -> dict[str, Path]:
    found = {}
    for path in source_dir.rglob("*.mhtml"):
        digest = sha256_bytes(path.read_bytes())
        if digest in found:
            raise ValueError(f"duplicate source digest {digest}: {found[digest]} and {path}")
        found[digest] = path
    return found


def revalidate_sources(rows, source_dir: Path):
    sources = map_sources(source_dir)
    used = {}
    for row in rows:
        digest = row["source_sha256"]
        if digest not in sources:
            raise FileNotFoundError(f"source hash not found under {source_dir}: {digest}")
        path = sources[digest]
        payloads = html_payloads(path)
        selector = row["selector"]
        count = sum(payload.count(selector) for payload in payloads)
        expected = int(row["expected_occurrences"])
        if count != expected:
            raise AssertionError(
                f"{row['evidence_id']}: selector occurrences {count}, expected {expected}, source={path}"
            )
        used[digest] = path
    return used


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=None,
                        help="directory containing raw MHTML archives; enables source revalidation")
    args = parser.parse_args()

    rows = read_tsv(CERTS)
    recovery = read_tsv(RECOVERY)
    validate_registry(rows, recovery)

    print("ARCH-LANG-CERT-01 CERT_REGISTRY_PASS")
    print(f"certified_selectors={len(rows)} source_hashes={len({r['source_sha256'] for r in rows})}")

    if args.source_dir is None:
        print("source_bytes=NOT_AVAILABLE; source revalidation not claimed")
        return

    used = revalidate_sources(rows, args.source_dir)
    print("ARCH-LANG-CERT-01 SOURCE_REVALIDATION_PASS")
    for digest, path in sorted(used.items()):
        print(f"SOURCE\t{digest}\t{path}")
    for row in rows:
        print(f"FRAGMENT\t{row['evidence_id']}\t{row['fragment_sha256']}\t{row['fragment_bytes']}")


if __name__ == "__main__":
    main()
