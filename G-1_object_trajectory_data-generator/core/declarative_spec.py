"""Build `generic_declarative_render` for the G-1 object-trajectory task.

Emits ONLY v2 canonical layer vocabulary (see重构_v2/LAYER_VOCAB_V2.md):

  - `stroked_shape` (with `dash_pattern_px`) : the static dashed target outline
    for the goal shape (circle / rect / triangle / polygon).
  - `filled_shape` : the moving solid coloured shape with a thin outline.

Shape geometry is materialised into the canonical per-kind fields here so
that downstream replay uses the shared `core.declarative_renderer` verbatim
— no project-specific shape vocabulary leaks into the metadata.
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple


# ───────────────────────────── per-shape geometry ─────────────────────────
# These mirror the legacy G-1 geometry (square/triangle/diamond use the same
# centre + radius semantics as the v1 layer carried — but emitted as canonical
# v2 kinds: rect / triangle / polygon).


def _triangle_points(cx: float, cy: float, radius: float) -> List[List[float]]:
    r = float(radius) * 1.2
    return [
        [cx, cy - r],
        [cx + r * 0.866, cy + r * 0.5],
        [cx - r * 0.866, cy + r * 0.5],
    ]


def _diamond_points(cx: float, cy: float, radius: float) -> List[List[float]]:
    r = float(radius) * 1.2
    return [
        [cx, cy - r],
        [cx + r, cy],
        [cx, cy + r],
        [cx - r, cy],
    ]


def _filled_layer(
    shape: str,
    cx: float,
    cy: float,
    radius: float,
    fill_rgb: List[int],
    outline_rgb: List[int],
    outline_width_px: int,
) -> Dict[str, Any]:
    """Emit a canonical v2 `filled_shape` layer for the G-1 shape vocabulary."""
    base: Dict[str, Any] = {
        "type": "filled_shape",
        "fill_rgb": fill_rgb,
        "outline_rgb": outline_rgb,
        "outline_width_px": int(outline_width_px),
    }
    if shape == "circle":
        base.update({
            "kind": "circle",
            "cx_px": cx,
            "cy_px": cy,
            "radius_px": float(radius),
        })
        return base
    if shape == "square":
        base.update({
            "kind": "rect",
            "x_px": cx - radius,
            "y_px": cy - radius,
            "w_px": 2.0 * radius,
            "h_px": 2.0 * radius,
        })
        return base
    if shape == "triangle":
        base.update({
            "kind": "triangle",
            "points_px": _triangle_points(cx, cy, radius),
        })
        return base
    if shape == "diamond":
        base.update({
            "kind": "polygon",
            "points_px": _diamond_points(cx, cy, radius),
        })
        return base
    raise ValueError(f"Unknown shape for filled_shape: {shape!r}")


def _stroked_dashed_layer(
    shape: str,
    cx: float,
    cy: float,
    radius: float,
    color_rgb: List[int],
    line_width_px: int,
    dash_length_px: int,
) -> Dict[str, Any]:
    """Emit a canonical v2 `stroked_shape` layer with a dash pattern."""
    base: Dict[str, Any] = {
        "type": "stroked_shape",
        "stroke_rgb": color_rgb,
        "stroke_width_px": int(line_width_px),
        "dash_pattern_px": [int(dash_length_px), int(dash_length_px)],
    }
    if shape == "circle":
        base.update({
            "kind": "circle",
            "cx_px": cx,
            "cy_px": cy,
            "radius_px": float(radius),
        })
        return base
    if shape == "square":
        base.update({
            "kind": "rect",
            "x_px": cx - radius,
            "y_px": cy - radius,
            "w_px": 2.0 * radius,
            "h_px": 2.0 * radius,
        })
        return base
    if shape == "triangle":
        base.update({
            "kind": "triangle",
            "points_px": _triangle_points(cx, cy, radius),
        })
        return base
    if shape == "diamond":
        base.update({
            "kind": "polygon",
            "points_px": _diamond_points(cx, cy, radius),
        })
        return base
    raise ValueError(f"Unknown shape for stroked_shape: {shape!r}")


def build_generic_declarative_render(
    parameters: Dict[str, Any], prompt: str, cfg: Any
) -> Dict[str, Any]:
    canvas_w, canvas_h = int(cfg.image_size[0]), int(cfg.image_size[1])
    bg_rgb = list(parameters["background_rgb"])

    shape = parameters["shape"]
    radius = float(parameters["ball_radius"])
    start_pos: Tuple[float, float] = (
        float(parameters["start_pos"][0]),
        float(parameters["start_pos"][1]),
    )
    end_pos: Tuple[float, float] = (
        float(parameters["end_pos"][0]),
        float(parameters["end_pos"][1]),
    )

    fill_rgb = list(parameters["ball_color_rgb"])
    outline_rgb = list(parameters["outline_rgb"])
    dash_rgb = list(parameters["dash_color_rgb"])
    outline_width = int(parameters["outline_width_px"])
    dash_width = int(parameters["dash_width_px"])
    dash_length = int(parameters["dash_length_px"])

    def dashed_target_layer() -> Dict[str, Any]:
        return _stroked_dashed_layer(
            shape, end_pos[0], end_pos[1], radius,
            dash_rgb, dash_width, dash_length,
        )

    def filled_shape_layer(center: Tuple[float, float]) -> Dict[str, Any]:
        return _filled_layer(
            shape, float(center[0]), float(center[1]), radius,
            fill_rgb, outline_rgb, outline_width,
        )

    # first frame: dashed target + ball at start
    first_layers = [dashed_target_layer(), filled_shape_layer(start_pos)]
    # final frame: dashed target + ball at end (full overlap)
    final_layers = [dashed_target_layer(), filled_shape_layer(end_pos)]

    # Video frame layout matches legacy G-1: hold(1s) + move(2s) + hold(1s).
    fps = int(parameters["video_fps"])
    hold_frames = int(parameters["hold_frames"])
    move_frames = int(parameters["move_frames"])

    video_frames: List[Dict[str, Any]] = []
    # Hold at start
    for _ in range(hold_frames):
        video_frames.append({"layers": [dashed_target_layer(), filled_shape_layer(start_pos)]})
    # Linear move: i = 1..move_frames, t = i / move_frames (matches legacy)
    for i in range(1, move_frames + 1):
        t = i / move_frames
        cx = start_pos[0] + (end_pos[0] - start_pos[0]) * t
        cy = start_pos[1] + (end_pos[1] - start_pos[1]) * t
        video_frames.append({"layers": [dashed_target_layer(), filled_shape_layer((cx, cy))]})
    # Hold at end
    for _ in range(hold_frames):
        video_frames.append({"layers": [dashed_target_layer(), filled_shape_layer(end_pos)]})

    return {
        "schema": "generic_declarative_canvas_v2",
        "version": 2,
        "prompt": prompt,
        "canvas": {"width": canvas_w, "height": canvas_h, "background_rgb": bg_rgb},
        "first_frame": {"layers": first_layers},
        "final_frame": {"layers": final_layers},
        "video": {"fps": fps, "frames": video_frames},
    }
