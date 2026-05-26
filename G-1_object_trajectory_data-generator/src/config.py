"""Task configuration — G-1 object trajectory."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from pydantic import Field

from core.base_generator import GenerationConfig


# Shape vocabulary (must be in sync with declarative_spec + replay_metadata).
SHAPES = ("circle", "square", "triangle", "diamond")


class TaskConfig(GenerationConfig):
    """G-1 object-trajectory task.

    The scene shows a single coloured shape that must travel along the
    shortest straight-line path to a dashed target outline of the same
    shape. The video animates this motion at a configurable fps.
    """

    domain: str = "G-1_object_trajectory_data-generator"
    num_samples: int = Field(default=5)
    image_size: tuple[int, int] = Field(default=(1024, 1024))

    # CLI's `--render` flips this to True; default keeps meta-only fast.
    generate_videos: bool = Field(default=False)
    video_fps: int = Field(default=16)

    # ── Task parameters (matched to legacy G-1) ─────────────────────────────
    ball_radius: int = Field(default=70, description="Half-extent of the shape in pixels.")
    margin_extra: int = Field(default=10, description="Extra margin from the canvas edge.")
    min_separation_px: int = Field(
        default=120,
        description="Minimum centre-to-centre distance between start and target.",
    )
    min_separation_ratio: float = Field(
        default=0.35,
        description="Effective min separation is max(min_separation_px, ratio * min(width, height)).",
    )
    color_min: int = Field(default=50, description="Lower bound for per-channel RGB sampling.")
    color_max: int = Field(default=200, description="Upper bound for per-channel RGB sampling.")
    shape_pool: list[str] = Field(
        default=list(SHAPES),
        description="Allowed shape vocabulary.",
    )

    # ── Visual styling ──────────────────────────────────────────────────────
    background_rgb: tuple[int, int, int] = Field(default=(255, 255, 255))
    outline_rgb: tuple[int, int, int] = Field(default=(0, 0, 0), description="Outline of the solid shape.")
    dash_color_rgb: tuple[int, int, int] = Field(default=(0, 0, 0), description="Colour of dashed target outline.")
    outline_width_px: int = Field(default=1)
    dash_width_px: int = Field(default=3)
    dash_length_px: int = Field(default=5)

    # ── Video temporal layout (matches legacy G-1: 1s hold + 2s move + 1s hold) ─
    hold_duration_sec: float = Field(default=1.0)
    move_duration_sec: float = Field(default=2.0)

    # IO
    output_dir: Path = Field(default=Path("out_meta"))
