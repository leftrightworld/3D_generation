"""Canonical declarative renderer for vbvr-meta v0 / canvas v2.

Single source of truth for layer drawing. Project's `tools/replay_metadata.py`
must re-export `render_frame` from here — do NOT re-implement per project.

Spec: see `重构_v2/LAYER_VOCAB_V2.md`.
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple

from PIL import Image, ImageDraw, ImageFont


_FONT_CANDIDATES_DEFAULT = [
    "/opt/fonts/DejaVuSans-Bold.ttf",
    "/opt/fonts/DejaVuSans.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial.ttf",
    "arial.ttf",
]

_FONT_FAMILY_MAP = {
    "DejaVuSans": ["/opt/fonts/DejaVuSans.ttf",
                   "/usr/share/fonts/dejavu/DejaVuSans.ttf",
                   "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"],
    "DejaVuSans-Bold": ["/opt/fonts/DejaVuSans-Bold.ttf",
                        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
                        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
    "Helvetica": ["/System/Library/Fonts/Helvetica.ttc"],
    "Arial": ["/Library/Fonts/Arial.ttf", "arial.ttf"],
    # ── CJK font families (project-local extension; same fallback semantics) ──
    "NotoSansCJK": [
        "/opt/fonts/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJKsc-Regular.otf",
        "/usr/share/fonts/google-noto-cjk/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
    ],
    "PingFang": [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
    ],
}


def _rgb(t: List[int]) -> Tuple[int, int, int]:
    return int(t[0]), int(t[1]), int(t[2])


def _load_font(size_px: int, family: Optional[str] = None):
    candidates: List[str] = []
    if family and family in _FONT_FAMILY_MAP:
        candidates.extend(_FONT_FAMILY_MAP[family])
    candidates.extend(_FONT_CANDIDATES_DEFAULT)
    for fp in candidates:
        try:
            return ImageFont.truetype(fp, int(size_px))
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


# ───────────────────────────── Per-kind geometry helpers ───────────────────

def _rect_bbox(layer: Dict[str, Any]) -> Tuple[float, float, float, float]:
    x = float(layer["x_px"]); y = float(layer["y_px"])
    w = float(layer["w_px"]); h = float(layer["h_px"])
    return (x, y, x + w, y + h)


def _circle_bbox(layer: Dict[str, Any]) -> Tuple[float, float, float, float]:
    cx = float(layer["cx_px"]); cy = float(layer["cy_px"])
    r = float(layer["radius_px"])
    return (cx - r, cy - r, cx + r, cy + r)


def _ellipse_bbox(layer: Dict[str, Any]) -> Tuple[float, float, float, float]:
    cx = float(layer["cx_px"]); cy = float(layer["cy_px"])
    rx = float(layer["rx_px"]); ry = float(layer["ry_px"])
    return (cx - rx, cy - ry, cx + rx, cy + ry)


def _polygon_points(layer: Dict[str, Any]) -> List[Tuple[float, float]]:
    return [(float(p[0]), float(p[1])) for p in layer["points_px"]]


def _star_points(layer: Dict[str, Any]) -> List[Tuple[float, float]]:
    cx = float(layer["cx_px"]); cy = float(layer["cy_px"])
    outer = float(layer["outer_radius_px"])
    inner = float(layer["inner_radius_px"])
    n = int(layer["num_points"])
    rot = float(layer.get("rotation_deg", 0.0)) * math.pi / 180.0
    pts: List[Tuple[float, float]] = []
    for i in range(2 * n):
        r = outer if i % 2 == 0 else inner
        ang = rot + math.pi * i / n - math.pi / 2  # start point up
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts


def _rounded_rect_polygon(layer: Dict[str, Any], steps_per_corner: int = 8) -> List[Tuple[float, float]]:
    """Approximate a rounded rectangle as a polygon (so we can fill/stroke
    consistently across kinds)."""
    x = float(layer["x_px"]); y = float(layer["y_px"])
    w = float(layer["w_px"]); h = float(layer["h_px"])
    r = float(layer["corner_radius_px"])
    r = min(r, w / 2, h / 2)
    pts: List[Tuple[float, float]] = []
    # corners (cx, cy, start_angle in radians)
    corners = [
        (x + w - r, y + r, -math.pi / 2),  # TR
        (x + w - r, y + h - r, 0.0),        # BR
        (x + r,     y + h - r, math.pi / 2),# BL
        (x + r,     y + r,     math.pi),    # TL
    ]
    for cx, cy, start in corners:
        for k in range(steps_per_corner + 1):
            ang = start + (math.pi / 2) * (k / steps_per_corner)
            pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts


# ───────────────────────────── Dashed-stroke helpers ───────────────────────

def _dash_path(points: List[Tuple[float, float]], dash_pattern: List[float], closed: bool) -> List[List[Tuple[float, float]]]:
    """Convert a polyline to a sequence of solid dashes."""
    if not points or len(points) < 2:
        return []
    if closed:
        points = points + [points[0]]
    segs: List[List[Tuple[float, float]]] = []
    current: List[Tuple[float, float]] = [points[0]]
    pat_idx = 0
    dash_on = True
    dist_left = float(dash_pattern[0])
    x0, y0 = points[0]
    for i in range(1, len(points)):
        x1, y1 = points[i]
        while True:
            seg_len = math.hypot(x1 - x0, y1 - y0)
            if seg_len <= dist_left + 1e-9:
                if dash_on:
                    current.append((x1, y1))
                else:
                    pass
                dist_left -= seg_len
                x0, y0 = x1, y1
                break
            else:
                t = dist_left / seg_len
                xm, ym = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
                if dash_on:
                    current.append((xm, ym))
                    if len(current) >= 2:
                        segs.append(current)
                    current = []
                else:
                    current = [(xm, ym)]
                dash_on = not dash_on
                pat_idx = (pat_idx + 1) % len(dash_pattern)
                dist_left = float(dash_pattern[pat_idx])
                x0, y0 = xm, ym
    if dash_on and len(current) >= 2:
        segs.append(current)
    return segs


# ───────────────────────────── Layer dispatch ──────────────────────────────

def _draw_filled_shape(draw: ImageDraw.ImageDraw, layer: Dict[str, Any]) -> None:
    kind = layer["kind"]
    fill = _rgb(layer["fill_rgb"])
    outline = _rgb(layer["outline_rgb"]) if "outline_rgb" in layer else None
    ow = int(layer.get("outline_width_px", 0)) if outline is not None else 0

    if kind == "rect":
        bbox = _rect_bbox(layer)
        if outline is not None and ow > 0:
            draw.rectangle(bbox, fill=fill, outline=outline, width=ow)
        else:
            draw.rectangle(bbox, fill=fill)
        return

    if kind == "circle":
        bbox = _circle_bbox(layer)
        if outline is not None and ow > 0:
            draw.ellipse(bbox, fill=fill, outline=outline, width=ow)
        else:
            draw.ellipse(bbox, fill=fill)
        return

    if kind == "ellipse":
        bbox = _ellipse_bbox(layer)
        if outline is not None and ow > 0:
            draw.ellipse(bbox, fill=fill, outline=outline, width=ow)
        else:
            draw.ellipse(bbox, fill=fill)
        return

    if kind == "polygon" or kind == "triangle":
        pts = _polygon_points(layer)
        if outline is not None:
            draw.polygon(pts, fill=fill, outline=outline)
        else:
            draw.polygon(pts, fill=fill)
        return

    if kind == "star":
        pts = _star_points(layer)
        if outline is not None:
            draw.polygon(pts, fill=fill, outline=outline)
        else:
            draw.polygon(pts, fill=fill)
        return

    if kind == "rounded_rect":
        bbox = _rect_bbox(layer)
        radius = int(layer["corner_radius_px"])
        if outline is not None and ow > 0:
            draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=ow)
        else:
            draw.rounded_rectangle(bbox, radius=radius, fill=fill)
        return

    raise ValueError(f"Unknown filled_shape kind: {kind!r}")


def _draw_stroked_shape(draw: ImageDraw.ImageDraw, layer: Dict[str, Any]) -> None:
    kind = layer["kind"]
    stroke = _rgb(layer["stroke_rgb"])
    sw = int(layer["stroke_width_px"])
    dash = layer.get("dash_pattern_px")

    def _stroke_polyline(pts: List[Tuple[float, float]], closed: bool) -> None:
        if dash:
            segs = _dash_path(pts, [float(x) for x in dash], closed)
            for seg in segs:
                draw.line(seg, fill=stroke, width=sw)
        else:
            if closed:
                draw.polygon(pts, outline=stroke)
                if sw > 1:
                    # PIL polygon outline ignores width; emit lines explicitly
                    looped = pts + [pts[0]]
                    draw.line(looped, fill=stroke, width=sw)
            else:
                draw.line(pts, fill=stroke, width=sw)

    if kind == "rect":
        x0, y0, x1, y1 = _rect_bbox(layer)
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        _stroke_polyline(pts, closed=True)
        return

    if kind == "circle":
        bbox = _circle_bbox(layer)
        if dash:
            # Approximate circle as polygon for dashed
            cx = (bbox[0] + bbox[2]) / 2; cy = (bbox[1] + bbox[3]) / 2
            r = (bbox[2] - bbox[0]) / 2
            pts = [(cx + r * math.cos(2 * math.pi * k / 64),
                    cy + r * math.sin(2 * math.pi * k / 64)) for k in range(64)]
            _stroke_polyline(pts, closed=True)
        else:
            draw.ellipse(bbox, outline=stroke, width=sw)
        return

    if kind == "ellipse":
        bbox = _ellipse_bbox(layer)
        if dash:
            cx = (bbox[0] + bbox[2]) / 2; cy = (bbox[1] + bbox[3]) / 2
            rx = (bbox[2] - bbox[0]) / 2; ry = (bbox[3] - bbox[1]) / 2
            pts = [(cx + rx * math.cos(2 * math.pi * k / 64),
                    cy + ry * math.sin(2 * math.pi * k / 64)) for k in range(64)]
            _stroke_polyline(pts, closed=True)
        else:
            draw.ellipse(bbox, outline=stroke, width=sw)
        return

    if kind == "polygon" or kind == "triangle":
        pts = _polygon_points(layer)
        _stroke_polyline(pts, closed=True)
        return

    if kind == "rounded_rect":
        bbox = _rect_bbox(layer)
        radius = int(layer["corner_radius_px"])
        if dash:
            # Dashed rounded rect is rare; fall back to polygon approximation.
            pts = _rounded_rect_polygon(layer)
            _stroke_polyline(pts, closed=True)
        else:
            draw.rounded_rectangle(bbox, radius=radius, outline=stroke, width=sw)
        return

    raise ValueError(f"Unknown stroked_shape kind: {kind!r}")


def _draw_line(draw: ImageDraw.ImageDraw, layer: Dict[str, Any]) -> None:
    pts = [(float(p[0]), float(p[1])) for p in layer["points_px"]]
    stroke = _rgb(layer["stroke_rgb"])
    sw = int(layer["stroke_width_px"])
    closed = bool(layer.get("closed", False))
    dash = layer.get("dash_pattern_px")
    if dash:
        segs = _dash_path(pts, [float(x) for x in dash], closed)
        for seg in segs:
            draw.line(seg, fill=stroke, width=sw)
    else:
        if closed:
            pts = pts + [pts[0]]
        draw.line(pts, fill=stroke, width=sw)


_ANCHOR_OFFSETS = {
    "l": 0.0, "m": 0.5, "r": 1.0,
    "t": 0.0, "b": 1.0,
}


def _draw_text(draw: ImageDraw.ImageDraw, layer: Dict[str, Any]) -> None:
    x = float(layer["x_px"]); y = float(layer["y_px"])
    content = str(layer["content"])
    color = _rgb(layer["color_rgb"])
    size_px = int(layer["font_size_px"])
    anchor = str(layer.get("anchor", "lt"))
    family = layer.get("font_family")
    font = _load_font(size_px, family)
    if len(anchor) != 2 or anchor[0] not in "lmr" or anchor[1] not in "tmb":
        anchor = "lt"
    bbox = draw.textbbox((0, 0), content, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    fx = _ANCHOR_OFFSETS[anchor[0]]
    fy = _ANCHOR_OFFSETS[anchor[1]]
    tx = x - text_w * fx - bbox[0]
    ty = y - text_h * fy - bbox[1]
    draw.text((tx, ty), content, fill=color, font=font)


def _draw_grid_lines(draw: ImageDraw.ImageDraw, layer: Dict[str, Any]) -> None:
    ox = float(layer["origin_x_px"]); oy = float(layer["origin_y_px"])
    rows = int(layer["rows"]); cols = int(layer["cols"])
    cs = float(layer["cell_size_px"])
    color = _rgb(layer["line_color_rgb"])
    lw = int(layer["line_width_px"])
    grid_w = cols * cs
    grid_h = rows * cs
    for i in range(cols + 1):
        x = ox + i * cs
        draw.line([(x, oy), (x, oy + grid_h)], fill=color, width=lw)
    for j in range(rows + 1):
        y = oy + j * cs
        draw.line([(ox, y), (ox + grid_w, y)], fill=color, width=lw)


def _draw_cell_fill(draw: ImageDraw.ImageDraw, layer: Dict[str, Any]) -> None:
    ox = float(layer["origin_x_px"]); oy = float(layer["origin_y_px"])
    cs = float(layer["cell_size_px"])
    row = int(layer["row"]); col = int(layer["col"])
    pad = float(layer.get("padding_px", 0))
    fill = _rgb(layer["fill_rgb"])
    x0 = ox + col * cs + pad
    y0 = oy + row * cs + pad
    x1 = ox + (col + 1) * cs - pad
    y1 = oy + (row + 1) * cs - pad
    draw.rectangle([(x0, y0), (x1, y1)], fill=fill)


def _draw_labeled_tile(draw: ImageDraw.ImageDraw, layer: Dict[str, Any]) -> None:
    ox = float(layer["origin_x_px"]); oy = float(layer["origin_y_px"])
    cs = float(layer["cell_size_px"])
    row = int(layer["row"]); col = int(layer["col"])
    ratio = float(layer.get("tile_size_ratio", 1.0))
    ts = cs * ratio
    margin = (cs - ts) / 2
    x = ox + col * cs + margin
    y = oy + row * cs + margin
    fill = _rgb(layer["fill_rgb"])
    text_color = _rgb(layer["text_color_rgb"])
    outline = _rgb(layer["outline_rgb"]) if "outline_rgb" in layer else None
    ow = int(layer.get("outline_width_px", 0)) if outline is not None else 0
    if outline is not None and ow > 0:
        draw.rectangle([(x, y), (x + ts, y + ts)], fill=fill, outline=outline, width=ow)
    else:
        draw.rectangle([(x, y), (x + ts, y + ts)], fill=fill)
    label = str(layer.get("label", ""))
    if label:
        size_px = int(layer["font_size_px"])
        font = _load_font(size_px, layer.get("font_family"))
        bbox = draw.textbbox((0, 0), label, font=font)
        text_w = bbox[2] - bbox[0]; text_h = bbox[3] - bbox[1]
        tx = x + (ts - text_w) / 2 - bbox[0]
        ty = y + (ts - text_h) / 2 - bbox[1]
        draw.text((tx, ty), label, fill=text_color, font=font)


def _draw_cell_grid(draw: ImageDraw.ImageDraw, layer: Dict[str, Any]) -> None:
    ox = float(layer["origin_x_px"]); oy = float(layer["origin_y_px"])
    cs = float(layer["cell_size_px"])
    rows = int(layer["rows"]); cols = int(layer["cols"])
    state = layer["state"]
    palette = layer["palette"]
    for i in range(rows):
        for j in range(cols):
            v = int(state[i][j])
            if v < 0 or v >= len(palette):
                continue
            color = _rgb(palette[v])
            x0 = ox + j * cs
            y0 = oy + i * cs
            x1 = ox + (j + 1) * cs
            y1 = oy + (i + 1) * cs
            draw.rectangle([(x0, y0), (x1, y1)], fill=color)


_DISPATCH = {
    "filled_shape":   _draw_filled_shape,
    "stroked_shape":  _draw_stroked_shape,
    "line":           _draw_line,
    "text":           _draw_text,
    "grid_lines":     _draw_grid_lines,
    "cell_fill":      _draw_cell_fill,
    "labeled_tile":   _draw_labeled_tile,
    "cell_grid":      _draw_cell_grid,
}


def render_frame(canvas: Dict[str, Any], frame: Dict[str, Any]) -> Image.Image:
    """Render a single frame (canvas + frame.layers) to PIL.Image.

    `canvas` must contain `width`, `height`, `background_rgb`.
    `frame` must contain `layers` (list of layer dicts).
    """
    w = int(canvas["width"]); h = int(canvas["height"])
    bg = _rgb(canvas["background_rgb"])
    image = Image.new("RGB", (w, h), bg)
    draw = ImageDraw.Draw(image)
    for layer in frame.get("layers", []):
        if not isinstance(layer, dict):
            continue
        t = layer.get("type")
        fn = _DISPATCH.get(t)
        if fn is None:
            raise ValueError(
                f"Unknown v2 layer type: {t!r}. "
                f"Allowed types: {sorted(_DISPATCH.keys())}. "
                f"See 重构_v2/LAYER_VOCAB_V2.md."
            )
        fn(draw, layer)
    return image


def write_video(frames: List[Image.Image], fps: int, path) -> None:
    """Encode frames to MP4 via opencv."""
    import cv2  # type: ignore
    import numpy as np  # type: ignore
    from pathlib import Path

    path = Path(path).with_suffix(".mp4")
    path.parent.mkdir(parents=True, exist_ok=True)
    w, h = frames[0].size
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(path), fourcc, float(fps), (w, h))
    for frame in frames:
        arr = np.array(frame.convert("RGB"))
        writer.write(cv2.cvtColor(arr, cv2.COLOR_RGB2BGR))
    writer.release()
