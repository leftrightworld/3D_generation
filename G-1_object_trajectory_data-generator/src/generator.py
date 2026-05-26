"""G-1 object-trajectory generator (vbvr-meta v0, canvas v2 vocabulary).

Produces tasks of the form: a single coloured shape must translate along the
shortest straight-line path to a dashed target outline of the same shape.

The metadata's `generic_declarative_render` section emits ONLY the v2
canonical layer vocabulary (`filled_shape`, `stroked_shape`) so that the
shared `core/declarative_renderer.py` can reproduce every frame
byte-identically. Both the meta-only path (via the canonical renderer) and
the `--render` path (also via the canonical renderer) draw through the same
function, guaranteeing pixel parity.
"""

from __future__ import annotations

import hashlib
import math
import random
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from core import BaseGenerator, TaskPair, VideoGenerator
from core.declarative_renderer import render_frame
from core.declarative_spec import build_generic_declarative_render

from .config import SHAPES, TaskConfig
from .prompts import (
    get_prompt,
    get_rules_en,
    get_task_summary_en,
    get_task_summary_zh,
)


EVALKIT_GENERATOR_KEY = "G-1_object_trajectory_data-generator"


def _stable_hash(s: str) -> int:
    """Process-independent hash: 8 bytes of sha256 -> unsigned int.

    NOTE: Python's built-in hash() is per-process-salted and breaks
    reproducibility across runs; never use it for task seeding.
    """
    return int.from_bytes(hashlib.sha256(s.encode("utf-8")).digest()[:8], "big")


class TaskGenerator(BaseGenerator):
    """G-1 object-trajectory task generator."""

    def __init__(self, config: TaskConfig):
        super().__init__(config)
        self.config: TaskConfig = config

        # Independent RNG so seeding stays deterministic per run.
        self.rng = random.Random()
        if config.random_seed is not None:
            self.rng.seed(config.random_seed)

        self._seen: set = set()
        self._specs: Optional[List[Dict[str, Any]]] = None

        self.video_generator: Optional[VideoGenerator] = None
        if config.generate_videos and VideoGenerator.is_available():
            self.video_generator = VideoGenerator(fps=config.video_fps, output_format="mp4")

    # ───────────────────────────── public entry points ─────────────────────

    def generate_metadata_bundle(self, task_id: str) -> dict:
        """Meta-only path used by examples/generate.py without --render."""
        params, prompt = self._sample_task(task_id)
        metadata = self._build_metadata(task_id, params)
        self._attach_meta_extensions(metadata, params, prompt)
        return metadata

    def generate_task_pair(self, task_id: str) -> TaskPair:  # type: ignore[override]
        """Full path used by examples/generate.py with --render."""
        params, prompt = self._sample_task(task_id)
        metadata = self._build_metadata(task_id, params)
        self._attach_meta_extensions(metadata, params, prompt)

        gdr = metadata["generic_declarative_render"]
        canvas = gdr["canvas"]
        first_image = render_frame(canvas, gdr["first_frame"])
        final_image = render_frame(canvas, gdr["final_frame"])

        video_path: Optional[str] = None
        if self.video_generator is not None:
            frames = [render_frame(canvas, f) for f in gdr["video"]["frames"]]
            if frames:
                tmp = Path(tempfile.gettempdir()) / f"{self.config.domain}_videos"
                tmp.mkdir(parents=True, exist_ok=True)
                out = tmp / f"{task_id}_ground_truth.mp4"
                video_path = str(self.video_generator.create_video_from_frames(frames, out))

        return TaskPair(
            task_id=task_id,
            domain=self.config.domain,
            prompt=prompt,
            first_image=first_image,
            final_image=final_image,
            ground_truth_video=video_path,
            metadata=metadata,
        )

    def generate_dataset(self) -> List[TaskPair]:  # type: ignore[override]
        """Dataset generator. Specs are pre-computed once + shared with meta-only."""
        self._ensure_specs()
        pairs: List[TaskPair] = []
        for i in range(self.config.num_samples):
            task_id = f"{self.config.domain}_{i:08d}"
            pair = self.generate_task_pair(task_id)
            pairs.append(pair)
            print(f"  Generated: {task_id}")
        return pairs

    # ───────────────────────────── spec pre-computation ────────────────────

    def _ensure_specs(self) -> None:
        """Pre-compute per-sample specs once. Both CLI modes call this."""
        if self._specs is not None:
            return
        self._seen.clear()
        if self.config.random_seed is not None:
            self.rng.seed(self.config.random_seed)
        # G-1 has no difficulty bins; spec is just an index marker. The
        # interesting randomness happens inside _sample_task using a stable
        # per-task seed.
        self._specs = [{"index": i} for i in range(self.config.num_samples)]

    # ───────────────────────────── core task logic ─────────────────────────

    def _sample_task(self, task_id: str) -> Tuple[Dict[str, Any], str]:
        """Sample a unique trajectory task; returns (parameters_dict, prompt)."""
        self._ensure_specs()
        idx_str = task_id.rsplit("_", 1)[-1]
        try:
            idx = int(idx_str)
        except ValueError as exc:
            raise ValueError(f"task_id must end with an 8-digit index, got {task_id!r}") from exc
        if not 0 <= idx < len(self._specs):  # type: ignore[arg-type]
            raise IndexError(f"task index {idx} out of range for num_samples={len(self._specs)}")  # type: ignore[arg-type]

        # Per-task RNG keyed off a stable hash → reproducible across processes.
        task_hash = _stable_hash(task_id)
        base_seed = task_hash
        if self.config.random_seed is not None:
            base_seed += self.config.random_seed
        local = random.Random(base_seed)

        w, h = int(self.config.image_size[0]), int(self.config.image_size[1])
        radius = int(self.config.ball_radius)
        margin = radius + int(self.config.margin_extra)
        min_dist = max(int(self.config.min_separation_px), int(min(w, h) * self.config.min_separation_ratio))

        # Sample start/end with min separation. Bound the attempts so we never
        # loop forever; reseed deterministically on failure.
        start_pos: Tuple[int, int] = (0, 0)
        end_pos: Tuple[int, int] = (0, 0)
        for attempt in range(1000):
            x1 = local.randint(margin, w - margin)
            y1 = local.randint(margin, h - margin)
            x2 = local.randint(margin, w - margin)
            y2 = local.randint(margin, h - margin)
            if math.hypot(x2 - x1, y2 - y1) > min_dist:
                start_pos = (x1, y1)
                end_pos = (x2, y2)
                break
        else:
            raise RuntimeError(f"Could not sample positions for {task_id}")

        r = local.randint(int(self.config.color_min), int(self.config.color_max))
        g = local.randint(int(self.config.color_min), int(self.config.color_max))
        b = local.randint(int(self.config.color_min), int(self.config.color_max))
        ball_color_rgb = (r, g, b)
        ball_color_hex = f"#{r:02x}{g:02x}{b:02x}"

        shape = local.choice(list(self.config.shape_pool))

        # Deduplicate on a coarse signature.
        signature = (shape, ball_color_rgb, start_pos, end_pos)
        if signature in self._seen:
            # If we collide, perturb the seed and try once more.
            local = random.Random(base_seed + 7919)
            for attempt in range(1000):
                x1 = local.randint(margin, w - margin)
                y1 = local.randint(margin, h - margin)
                x2 = local.randint(margin, w - margin)
                y2 = local.randint(margin, h - margin)
                if math.hypot(x2 - x1, y2 - y1) > min_dist:
                    start_pos = (x1, y1)
                    end_pos = (x2, y2)
                    break
            r = local.randint(int(self.config.color_min), int(self.config.color_max))
            g = local.randint(int(self.config.color_min), int(self.config.color_max))
            b = local.randint(int(self.config.color_min), int(self.config.color_max))
            ball_color_rgb = (r, g, b)
            ball_color_hex = f"#{r:02x}{g:02x}{b:02x}"
            shape = local.choice(list(self.config.shape_pool))
            signature = (shape, ball_color_rgb, start_pos, end_pos)
        self._seen.add(signature)

        # Temporal layout
        fps = int(self.config.video_fps)
        hold_frames = int(fps * float(self.config.hold_duration_sec))
        move_frames = int(fps * float(self.config.move_duration_sec))
        total_frames = 2 * hold_frames + move_frames

        # Trajectory description for semantic_ground_truth.
        path_length_px = math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        # Image coordinates: x grows right, y grows DOWN — describe direction in that frame.
        heading_rad = math.atan2(dy, dx)
        heading_deg = math.degrees(heading_rad)

        params: Dict[str, Any] = {
            "shape": shape,
            "ball_color_rgb": list(ball_color_rgb),
            "ball_color_hex": ball_color_hex,
            "start_pos": list(start_pos),
            "end_pos": list(end_pos),
            "ball_radius": radius,
            "background_rgb": list(self.config.background_rgb),
            "outline_rgb": list(self.config.outline_rgb),
            "dash_color_rgb": list(self.config.dash_color_rgb),
            "outline_width_px": int(self.config.outline_width_px),
            "dash_width_px": int(self.config.dash_width_px),
            "dash_length_px": int(self.config.dash_length_px),
            "canvas_size": [w, h],
            "video_fps": fps,
            "hold_frames": hold_frames,
            "move_frames": move_frames,
            "total_frames": total_frames,
            "path_length_px": round(path_length_px, 6),
            "heading_rad": round(heading_rad, 6),
            "heading_deg": round(heading_deg, 6),
        }

        prompt = get_prompt("default", shape=shape)
        return params, prompt

    # ───────────────────────────── vbvr-meta v0 extensions ─────────────────

    def _attach_meta_extensions(
        self, metadata: dict, params: Dict[str, Any], prompt: str
    ) -> None:
        metadata["generator"] = EVALKIT_GENERATOR_KEY
        metadata["schema_version"] = "vbvr-meta-v0"

        shape = params["shape"]
        objects = [
            {
                "symbol": "moving_shape",
                "shape": shape,
                "role": "agent",
                "color_rgb": params["ball_color_rgb"],
                "color_hex": params["ball_color_hex"],
                "radius_px": params["ball_radius"],
                "initial_position_px": params["start_pos"],
                "final_position_px": params["end_pos"],
            },
            {
                "symbol": "dashed_target",
                "shape": shape,
                "role": "target_outline",
                "color_rgb": params["dash_color_rgb"],
                "radius_px": params["ball_radius"],
                "initial_position_px": params["end_pos"],
                "final_position_px": params["end_pos"],
            },
        ]

        metadata["semantic_ground_truth"] = {
            "task_type": "object_trajectory",
            "motion_model": "linear_translation_shortest_path",
            "shape": shape,
            "start_pos_px": params["start_pos"],
            "end_pos_px": params["end_pos"],
            "path_length_px": params["path_length_px"],
            "heading_deg": params["heading_deg"],
            "objects": objects,
            "rules_en": get_rules_en(),
            "task_summary_en": get_task_summary_en(),
            "task_summary_zh": get_task_summary_zh(),
            "video_temporal": {
                "fps": params["video_fps"],
                "hold_frames": params["hold_frames"],
                "move_frames": params["move_frames"],
                "total_frames": params["total_frames"],
                "phase_order": ["hold_initial", "linear_translate", "hold_final"],
            },
            "interpretation": {
                "first_frame_is_initial_state": True,
                "final_frame_is_goal_state": True,
                "video_animates_solution": True,
                "dashed_target_is_static": True,
            },
        }

        metadata["scoring_contract"] = {
            "evaluator_class": "ObjectTrajectoryEvaluator",
            "evalkit_pending_confirmation": True,
            "evalkit_map_key": EVALKIT_GENERATOR_KEY,
            "task_specific_dimension_weights": {
                "final_overlap_accuracy":   0.40,
                "trajectory_linearity":     0.25,
                "shape_color_preservation": 0.20,
                "target_static_preservation": 0.15,
            },
            "required_semantic_fields": [
                "task_type", "shape", "start_pos_px", "end_pos_px",
                "path_length_px", "heading_deg",
            ],
            "pixel_tolerance_notes": {
                "final_overlap_mean_abs_diff_lt": 15,
                "trajectory_endpoint_radius_px_lt": 8,
            },
            "notes": (
                "Evaluator compares the model's final video frame to the goal "
                "(solid shape fully overlapping dashed target); trajectory "
                "linearity penalises detours from the straight-line path; "
                "target_static_preservation checks the dashed outline is "
                "unchanged across frames."
            ),
        }

        metadata["generic_declarative_render"] = build_generic_declarative_render(
            params, prompt, self.config
        )

        metadata["provenance"] = {
            "created_at": metadata["timestamp"],
            "random_seed": metadata["generation"]["seed"],
            "package": "vbvr-meta-generator-g1",
            "declarative_render_schema": "generic_declarative_canvas_v2",
            "metadata_schema_version": "vbvr-meta-v0",
            "layer_vocabulary_used": [
                "filled_shape", "stroked_shape",
            ],
        }
