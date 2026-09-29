#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "experiments/chem-vision-real-images-01.tsv"


def rows():
    with DATA.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def fibre(items, key, value):
    return [r for r in items if r[key] == value]


def main():
    data = rows()
    by_id = {r["image_id"]: r for r in data}
    assert set(by_id) == {"METHYL_RED", "RED_CABBAGE", "FERROUS_CARBONATE"}

    # 1. Visual geometry groups two chemically distinct systems together.
    colour_series = fibre(data, "visual_class", "MULTI_SAMPLE_COLOR_SERIES")
    assert {r["image_id"] for r in colour_series} == {"METHYL_RED", "RED_CABBAGE"}
    assert len({r["chemical_system"] for r in colour_series}) == 2

    # 2. For a coarse reaction-motif task the same visual class is also a
    # single task quotient, despite distinct concrete chemical identities.
    assert {r["reaction_motif"] for r in colour_series} == {"PH_INDICATOR_CHROMATIC_RESPONSE"}

    # 3. Chemical identity is not determined by the visual class.
    assert len({r["chemical_system"] for r in colour_series}) > 1

    # 4. A visually different solid-formation witness belongs to a different
    # reaction motif; visual geometry and reaction language may agree here,
    # but this is an observed coincidence, not an identification rule.
    solid = fibre(data, "visual_class", "SOLID_FORMATION_COLOR_STATE")
    assert [r["image_id"] for r in solid] == ["FERROUS_CARBONATE"]
    assert solid[0]["reaction_motif"] == "PRECIPITATION_GAS_OXIDATION_COUPLED"

    # 5. Provenance is retained for every image rather than replacing images
    # by free-floating labels.
    assert all(r["source_page"].startswith("https://commons.wikimedia.org/wiki/File:") for r in data)
    assert all(r["provenance_level"] == "WEB_SOURCE_REVIEWED" for r in data)

    print("PSI-CHEM-VISION-REAL-01 PASS_WITH_BOUNDARY")
    print("visual MULTI_SAMPLE_COLOR_SERIES fibre=2 concrete chemical systems")
    print("task quotient PH_INDICATOR_CHROMATIC_RESPONSE=singleton")
    print("chemical identity from visual class=NOT_IDENTIFIED")
    print("FERROUS_CARBONATE separates as solid-formation/coupled motif")
    print("image provenance retained=PASS")
    print("BOUNDARY: visual classes are reviewed attestations, not output of an automated pixel classifier")


if __name__ == "__main__":
    main()
