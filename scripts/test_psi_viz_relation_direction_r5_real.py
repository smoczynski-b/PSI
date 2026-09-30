#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
SOURCE_WITNESS = ROOT / "scripts" / "test_psi_viz_relation_direction_r5.py"
GENERATED = ROOT / "build" / "psi-viz-r5"
OUT = ROOT / "build" / "psi-viz-r5-real"

SCENES = (
    ("directed-ab", GENERATED / "directed-ab.py", "R5DirectedAB"),
    ("directed-ba", GENERATED / "directed-ba.py", "R5DirectedBA"),
    ("symmetric-ab", GENERATED / "symmetric-ab.py", "R5SymmetricAB"),
    ("symmetric-ba", GENERATED / "symmetric-ba.py", "R5SymmetricBA"),
)


def render_pixels(tag: str, scene_path: Path, class_name: str) -> tuple[tuple[int, int], bytes, str]:
    media_dir = OUT / "media" / tag
    if media_dir.exists():
        shutil.rmtree(media_dir)
    media_dir.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            sys.executable,
            "-m",
            "manim",
            "-ql",
            "-s",
            "--disable_caching",
            "--media_dir",
            str(media_dir),
            str(scene_path),
            class_name,
        ],
        cwd=ROOT,
        check=True,
    )

    candidates = sorted(p for p in media_dir.rglob("*.png") if class_name in p.name)
    assert len(candidates) == 1, (tag, class_name, [str(p) for p in candidates])
    rendered = candidates[0]

    with Image.open(rendered) as image:
        rgba = image.convert("RGBA")
        size = rgba.size
        pixels = rgba.tobytes()

    digest = hashlib.sha256(pixels).hexdigest()
    shutil.copyfile(rendered, OUT / f"{tag}.png")
    return size, pixels, digest


def main() -> None:
    # Regenerate the four fixtures through the production PSI-VIZ pipeline.
    subprocess.run([sys.executable, str(SOURCE_WITNESS)], cwd=ROOT, check=True)

    OUT.mkdir(parents=True, exist_ok=True)
    rendered = {
        tag: render_pixels(tag, scene_path, class_name)
        for tag, scene_path, class_name in SCENES
    }

    sizes = {tag: value[0] for tag, value in rendered.items()}
    assert len(set(sizes.values())) == 1, sizes

    directed_ab = rendered["directed-ab"][1]
    directed_ba = rendered["directed-ba"][1]
    symmetric_ab = rendered["symmetric-ab"][1]
    symmetric_ba = rendered["symmetric-ba"][1]

    # Acceptance boundary: compare decoded RGBA pixels, not source or PNG metadata.
    assert directed_ab != directed_ba, "directed reversal did not change rendered pixels"
    assert symmetric_ab == symmetric_ba, "symmetric reversal changed rendered pixels"

    digest_lines = []
    for tag, (size, _pixels, digest) in rendered.items():
        line = f"{tag} size={size[0]}x{size[1]} rgba_sha256={digest}"
        digest_lines.append(line)
        print(line)
    (OUT / "pixel-digests.txt").write_text("\n".join(digest_lines) + "\n", encoding="utf-8")

    print("PSI-VIZ-R5-REAL-MANIM PASS_WITH_BOUNDARY")
    print("directed_reversal_pixels_differ=PASS")
    print("symmetric_reversal_pixels_identical=PASS")


if __name__ == "__main__":
    main()
