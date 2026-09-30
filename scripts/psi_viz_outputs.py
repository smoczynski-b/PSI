#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math

from psi_viz_projection import VisualFrame, classify_transition


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _digest(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


def _clean_token(value: str, field: str) -> str:
    out = str(value).strip()
    if not out:
        raise ValueError(f"{field} is required")
    return out


@dataclass(frozen=True)
class OutputProfile:
    profile_id: str
    paper_width: float = 1600.0
    paper_height: float = 1000.0
    margin: float = 80.0
    node_radius: float = 24.0
    font_family: str = "serif"
    background: str = "ivory"
    foreground: str = "black"
    identity_palette: tuple[str, ...] = ("red", "blue", "gold", "black")

    def __post_init__(self):
        object.__setattr__(self, "profile_id", _clean_token(self.profile_id, "profile_id"))
        for field in ("paper_width", "paper_height", "margin", "node_radius"):
            value = getattr(self, field)
            if isinstance(value, bool):
                raise ValueError(f"{field} must be a finite positive number")
            out = float(value)
            if not math.isfinite(out) or out <= 0:
                raise ValueError(f"{field} must be a finite positive number")
            object.__setattr__(self, field, out)
        if self.margin * 2 >= min(self.paper_width, self.paper_height):
            raise ValueError("margin leaves no printable area")
        for field in ("font_family", "background", "foreground"):
            object.__setattr__(self, field, _clean_token(getattr(self, field), field))
        palette = tuple(_clean_token(x, "identity_palette token") for x in self.identity_palette)
        if not palette:
            raise ValueError("identity_palette must be non-empty")
        object.__setattr__(self, "identity_palette", palette)


@dataclass(frozen=True)
class PrintKeyframe:
    source_semantic_digest: str
    source_layout_digest: str
    profile_id: str
    payload: dict
    payload_digest: str

    def as_dict(self) -> dict:
        return {
            "source_semantic_digest": self.source_semantic_digest,
            "source_layout_digest": self.source_layout_digest,
            "profile_id": self.profile_id,
            "payload": self.payload,
            "payload_digest": self.payload_digest,
        }


@dataclass(frozen=True)
class AnimationTimeline:
    source_semantic_digest: str
    target_semantic_digest: str
    from_layout_digest: str
    to_layout_digest: str
    declared_motion: str
    duration_seconds: float
    payload: dict
    payload_digest: str

    def as_dict(self) -> dict:
        return {
            "source_semantic_digest": self.source_semantic_digest,
            "target_semantic_digest": self.target_semantic_digest,
            "from_layout_digest": self.from_layout_digest,
            "to_layout_digest": self.to_layout_digest,
            "declared_motion": self.declared_motion,
            "duration_seconds": self.duration_seconds,
            "payload": self.payload,
            "payload_digest": self.payload_digest,
        }


def _asset_id(prefix: str, *parts: str) -> str:
    seed = "|".join(parts)
    return f"{prefix}:{hashlib.sha256(seed.encode('utf-8')).hexdigest()[:16]}"


def _identity_color(node_id: str, profile: OutputProfile) -> str:
    idx = int(hashlib.sha256(node_id.encode("utf-8")).hexdigest()[:8], 16) % len(profile.identity_palette)
    return profile.identity_palette[idx]


def _edge_id(row: dict) -> str:
    return _asset_id("edge", str(row["from"]), str(row["relation"]), str(row["to"]))


def _node_id(node: str) -> str:
    return _asset_id("node", node)


def _scale_positions(frame: VisualFrame, profile: OutputProfile) -> dict[str, tuple[float, float]]:
    positions = frame.layout_payload["positions"]
    xs = [float(pair[0]) for pair in positions.values()]
    ys = [float(pair[1]) for pair in positions.values()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    span_x = max(max_x - min_x, 1.0)
    span_y = max(max_y - min_y, 1.0)
    usable_w = profile.paper_width - 2 * profile.margin
    usable_h = profile.paper_height - 2 * profile.margin
    return {
        node: (
            profile.margin + (float(pair[0]) - min_x) / span_x * usable_w,
            profile.margin + (float(pair[1]) - min_y) / span_y * usable_h,
        )
        for node, pair in positions.items()
    }


def compile_print_keyframe(frame: VisualFrame, profile: OutputProfile) -> PrintKeyframe:
    if not isinstance(frame, VisualFrame):
        raise TypeError("compile_print_keyframe requires VisualFrame")
    if not isinstance(profile, OutputProfile):
        raise TypeError("compile_print_keyframe requires OutputProfile")

    positions = _scale_positions(frame, profile)
    semantic = frame.semantic_payload
    nodes = []
    for node in semantic["nodes"]:
        x, y = positions[node]
        nodes.append({
            "asset_id": _node_id(node),
            "object_id": node,
            "primitive": "circle+text",
            "cx": x,
            "cy": y,
            "radius": profile.node_radius,
            "fill": _identity_color(node, profile),
            "stroke": profile.foreground,
            "label": node,
            "font_family": profile.font_family,
            "status": semantic.get("node_status", {}).get(node, ""),
        })

    edges = []
    pos = positions
    for row in semantic["edges"]:
        source = str(row["from"])
        target = str(row["to"])
        sx, sy = pos[source]
        tx, ty = pos[target]
        out = {
            "asset_id": _edge_id(row),
            "primitive": "line+text",
            "from_object_id": source,
            "to_object_id": target,
            "x1": sx,
            "y1": sy,
            "x2": tx,
            "y2": ty,
            "relation": row["relation"],
            "stroke": profile.foreground,
            "label": row["relation"],
        }
        # Only metadata already present in the redacted VisualFrame can survive.
        if "provenance" in row:
            out["provenance"] = row["provenance"]
        if "status" in row:
            out["status"] = row["status"]
        edges.append(out)

    payload = {
        "format": "PSI-VIZ-PRINT-SCENE-1",
        "vector_safe": True,
        "gradients": False,
        "canvas": {
            "width": profile.paper_width,
            "height": profile.paper_height,
            "margin": profile.margin,
            "background": profile.background,
        },
        "source": {
            "visual_contract_id": frame.visual_contract_id,
            "task_id": frame.task_id,
            "source_revision": frame.source_revision,
            "source_state_digest": frame.source_state_digest,
            "semantic_digest": frame.semantic_digest,
            "layout_digest": frame.layout_digest,
        },
        "nodes": nodes,
        "edges": edges,
    }
    return PrintKeyframe(
        source_semantic_digest=frame.semantic_digest,
        source_layout_digest=frame.layout_digest,
        profile_id=profile.profile_id,
        payload=payload,
        payload_digest=_digest(payload),
    )


def _assert_animation_contract_invariant(before: VisualFrame, after: VisualFrame) -> None:
    if before.task_id != after.task_id:
        raise ValueError("animation cannot change task_id")
    for field in ("visible_metadata", "channel_meanings"):
        if before.semantic_payload.get(field) != after.semantic_payload.get(field):
            raise ValueError(f"animation cannot change visual contract field: {field}")


def compile_animation_timeline(
    before: VisualFrame,
    after: VisualFrame,
    declared_motion: str,
    *,
    duration_seconds: float = 1.0,
) -> AnimationTimeline:
    if not isinstance(before, VisualFrame) or not isinstance(after, VisualFrame):
        raise TypeError("compile_animation_timeline requires VisualFrame inputs")
    if isinstance(duration_seconds, bool):
        raise ValueError("duration_seconds must be a finite positive number")
    duration = float(duration_seconds)
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("duration_seconds must be a finite positive number")

    _assert_animation_contract_invariant(before, after)
    verdict = classify_transition(before, after, declared_motion)
    if not verdict["legal"]:
        raise ValueError(f"illegal visual transition: {verdict['reason']}")

    before_nodes = set(before.semantic_payload["nodes"])
    after_nodes = set(after.semantic_payload["nodes"])
    motion = verdict["declared_motion"]
    commands: list[dict] = []

    if motion == "REPOSITION":
        if before.semantic_digest != after.semantic_digest:
            raise ValueError("REPOSITION requires identical semantic digest")
        if before_nodes != after_nodes:
            raise ValueError("REPOSITION cannot change visible node set")
        for node in sorted(before_nodes):
            p0 = before.layout_payload["positions"][node]
            p1 = after.layout_payload["positions"][node]
            if p0 != p1:
                commands.append({
                    "kind": "MOVE_NODE",
                    "asset_id": _node_id(node),
                    "object_id": node,
                    "from": list(p0),
                    "to": list(p1),
                    "t0": 0.0,
                    "t1": duration,
                })
    else:
        # Semantic transitions are not inferred from screen geometry. F4.1 only
        # emits the validated declared event and frame references; a later
        # adapter may animate it but may not invent additional semantics.
        commands.append({
            "kind": "SEMANTIC_EVENT",
            "declared_motion": motion,
            "from_semantic_digest": before.semantic_digest,
            "to_semantic_digest": after.semantic_digest,
            "t0": 0.0,
            "t1": duration,
        })

    payload = {
        "format": "PSI-VIZ-TIMELINE-1",
        "renderer_target": "MANIM_ADAPTER",
        "source": {
            "visual_contract_id": before.visual_contract_id,
            "task_id": before.task_id,
            "from_revision": before.source_revision,
            "to_revision": after.source_revision,
            "from_state_digest": before.source_state_digest,
            "to_state_digest": after.source_state_digest,
        },
        "transition": verdict,
        "duration_seconds": duration,
        "commands": commands,
    }
    return AnimationTimeline(
        source_semantic_digest=before.semantic_digest,
        target_semantic_digest=after.semantic_digest,
        from_layout_digest=before.layout_digest,
        to_layout_digest=after.layout_digest,
        declared_motion=motion,
        duration_seconds=duration,
        payload=payload,
        payload_digest=_digest(payload),
    )
