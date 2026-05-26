# G-1: Object Trajectory Data Generator (vbvr-meta v0)

**Task:** A single coloured shape (circle / square / triangle / diamond) must
travel along the shortest straight-line path to a dashed target outline of
the same shape, so that at the final frame the moving shape fully overlaps
the static dashed target.

**Generator Key:** `G-1_object_trajectory_data-generator`
**Evaluator (pending EvalKit confirmation):** `ObjectTrajectoryEvaluator`
**Schema:** `vbvr-meta-v0` · **Declarative render schema:** `generic_declarative_canvas_v2`

This generator emits **`metadata.json` first** (the source of truth) and
produces images / video on demand via `--render`. The metadata's
`generic_declarative_render` section reproduces every frame
**byte-identically** without importing `src/` — the pilot verifies this for
`first_frame.png` and `final_frame.png`.

---

## Quick Start

```bash
pip install -r requirements.txt

# Default: metadata.json only (fast; no opencv needed if you skip --render)
python3 examples/generate.py --num-samples 5 --seed 42 --output-dir ./qa_out

# Also write first_frame.png, final_frame.png, ground_truth.mp4
python3 examples/generate.py --num-samples 5 --seed 42 --output-dir ./qa_full --render
```

Output layout:
```
qa_out/G-1_object_trajectory_data-generator_task/
└── G-1_object_trajectory_data-generator_00000000/
    └── metadata.json
```

With `--render`:
```
qa_full/G-1_object_trajectory_data-generator_task/
└── G-1_object_trajectory_data-generator_00000000/
    ├── metadata.json
    ├── first_frame.png        # ball at start + dashed target outline
    ├── final_frame.png        # ball at target (full overlap)
    ├── prompt.txt             # task instruction
    └── ground_truth.mp4       # hold(1s) + linear translate(2s) + hold(1s)
```

---

## Replay the visual from metadata alone

`tools/replay_metadata.py` reconstructs all frames from
`generic_declarative_render`:

```bash
python3 tools/replay_metadata.py \
  --json qa_out/G-1_object_trajectory_data-generator_task/G-1_object_trajectory_data-generator_00000000/metadata.json \
  --output-dir ./replay_out
```

`tools/replay_metadata.py` is a thin re-export of the canonical shared
`core.declarative_renderer.render_frame` — it supports all 8 canvas-v2
layer types (see `重构_v2/LAYER_VOCAB_V2.md`). This generator only emits
two of them: `filled_shape` and `stroked_shape` (dashed).

Verify pixel parity (src render vs metadata replay):
```bash
python3 tools/check_meta_render_parity.py \
  --qa-out ./qa_out --qa-full ./qa_full --num-samples 5 \
  --semantic-keys task_type,shape,start_pos_px,end_pos_px,path_length_px
```

---

## Task description

- **Scene:** A single coloured shape (circle / square / triangle / diamond)
  plus a dashed outline of the same shape at the goal position.
- **Goal:** Translate the solid shape so that its centre reaches the goal
  centre — at the final frame the two shapes completely overlap.
- **Motion model:** linear translation along the straight line from start
  centre to goal centre (no rotation / scale / colour change).
- **Constraints:**
  - Both shapes have a fixed radius (default 70 px).
  - Start and goal centres are at least `min_separation_px` apart.
  - The dashed target outline is static throughout the animation.
- **Video temporal layout:** `hold_initial` (1s) → `linear_translate` (2s)
  → `hold_final` (1s) at 16 fps (default).

---

## vbvr-meta-v0 fields produced

| Top-level | What it contains |
|---|---|
| `task_id` | Stable per-sample ID. |
| `generator` | `G-1_object_trajectory_data-generator` |
| `schema_version` | `vbvr-meta-v0` |
| `timestamp` | ISO-8601 generation time |
| `parameters` | Shape, colour, start/end positions, radius, video timing, render knobs (deterministic from seed). |
| `param_hash` | SHA-256 prefix used for de-duplication. |
| `generation` | `{seed, git: {commit, branch, repo, is_dirty}}` |
| `semantic_ground_truth` | shape, start/end positions, path length, heading, per-object descriptors, en/zh task summaries, rules, video_temporal hints. |
| `scoring_contract` | evaluator class + four-dimension weights (see below). |
| `generic_declarative_render` | canvas + first/final frame layers + per-frame video layers (replayable). |
| `provenance` | layer vocabulary used, schema version, seed. |

### Scoring dimensions (and why they're named this way)

| Dimension | Weight | What it measures |
|---|---|---|
| `final_overlap_accuracy` | 0.40 | Does the model's final frame have the solid shape fully overlapping the dashed target? |
| `trajectory_linearity` | 0.25 | Is each intermediate centre near the straight-line interpolation between start and goal? |
| `shape_color_preservation` | 0.20 | Does the moving shape keep the same shape type and colour from start to finish? |
| `target_static_preservation` | 0.15 | Is the dashed target outline unchanged across all frames? |

> **NB:** `evaluator_class` is set to `ObjectTrajectoryEvaluator` with
> `evalkit_pending_confirmation: true`. Confirm against the actual EvalKit
> evaluator class name and dimension keys before shipping.

---

## Layer vocabulary (canvas v2, canonical)

This generator emits ONLY canonical canvas-v2 layer types
(see `重构_v2/LAYER_VOCAB_V2.md`):

| Layer | Kinds used | Notes |
|---|---|---|
| `filled_shape` | `circle`, `rect`, `triangle`, `polygon` | Solid coloured shape with a thin outline. Square → `rect` (x_px, y_px, w_px, h_px); diamond → `polygon` (4 points). |
| `stroked_shape` (with `dash_pattern_px`) | `circle`, `rect`, `triangle`, `polygon` | Static dashed outline of the goal shape. Dash pattern is `[dash_length, dash_length]`. |

Drawing is delegated to the shared `core/declarative_renderer.py` (copied
verbatim from `_canonical/`). Both `src/generator.py` and
`tools/replay_metadata.py` call `render_frame` — guaranteeing byte-identical
PNGs between the meta-only replay path and the `--render` path.

---

## Layout

| Path | Role |
|------|------|
| `core/` | Framework code (canonical, copied from G-13 baseline). |
| `core/declarative_renderer.py` | **Canonical:** shared renderer for all 8 canvas-v2 layer types (copied verbatim from `_canonical/`). |
| `core/declarative_spec.py` | **Task-specific:** params → v2 layer list translator. |
| `src/` | **Task-specific:** `config.py`, `prompts.py`, `generator.py`. |
| `examples/generate.py` | CLI entry. Default: meta-only. `--render` for media. |
| `schemas/metadata.example.json` | Compact, real example metadata (video frames truncated). |
| `eval/EVAL.md` + `eval/verify_meta_contract.py` | Schema-contract + replay smoke check. |
| `tools/replay_metadata.py` | Replay video/images from metadata alone. |
| `tools/check_meta_render_parity.py` | Cross-check meta-only vs `--render` outputs (parameters/hash/declarative/semantic). |
| `docs/CUSTOMIZE.md` | Forking checklist. |
| `docs/QA_REPORT.md` | Pilot QA results (parity status, sample counts, deltas). |
| `qa_out/` / `qa_full/` | QA artefacts produced by the smoke runs. |

---

## Origin

Refactored from
[`VBVR-DataFactory/G-1_object_trajectory_data-generator`](https://github.com/VBVR-DataFactory/G-1_object_trajectory_data-generator)
to the in-house **vbvr-meta v0** spec used by the in-tree sibling
generators. Task logic is preserved end-to-end (random shape, random
colour in `[50, 200]` per channel, 70-px radius, linear translation, 1s+2s+1s
phases at 16 fps) and metadata is enriched with `semantic_ground_truth`,
`scoring_contract`, and a replayable `generic_declarative_render`.
