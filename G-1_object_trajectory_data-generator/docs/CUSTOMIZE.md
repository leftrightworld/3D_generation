# Customising this generator

## Knobs in `src/config.py`

| Field | Effect |
|---|---|
| `shape_pool` | Allowed shapes (`circle`, `square`, `triangle`, `diamond`). |
| `ball_radius` | Half-extent of both moving shape and dashed target outline. |
| `margin_extra` | Extra pixels added to the radius for edge margin. |
| `min_separation_px` / `min_separation_ratio` | Minimum centre-to-centre distance between start and target. The effective minimum is `max(px, ratio · min(W,H))`. |
| `color_min` / `color_max` | Per-channel RGB bounds for the moving shape's random colour. |
| `video_fps` | Frames per second of `ground_truth.mp4` (also recorded in metadata `video_temporal`). |
| `hold_duration_sec` / `move_duration_sec` | Phase durations (default 1s / 2s / 1s = legacy G-1 layout). |
| `image_size` | Canvas resolution. Affects layer `*_px` fields. |
| `background_rgb` / `outline_rgb` / `dash_color_rgb` | Pure cosmetic. |
| `outline_width_px` / `dash_width_px` / `dash_length_px` | Line styling. |

## Forking to a new sibling task

If your task is also a single-object-translation task you can keep
`dashed_shape_outline` + `filled_shape` and adapt `_sample_task` to your
needs. If you need additional layer primitives (e.g., trajectory arrows,
keypoint markers), extend:

1. `core/declarative_spec.py` to emit the new layer dicts.
2. `tools/replay_metadata.py::_draw_layer` to draw them.
3. `src/generator.py::_draw_layer` (shared helpers) to draw them in the src
   render path with **identical** math.
4. Register the new names in `provenance.layer_vocabulary_used`.

## Determinism notes

- Per-task RNG is seeded by `_stable_hash(task_id)` (SHA-256 prefix), so
  re-running with the same `--seed` and `--num-samples` reproduces identical
  metadata across processes. Python's built-in `hash()` is process-salted
  and must **not** be used here.
- Both meta-only and `--render` modes share `_ensure_specs()` to pre-compute
  the per-sample indices once; the parity check verifies that
  `parameters`, `param_hash`, and `generic_declarative_render` match across
  modes.
- The `--render` path renders by re-using the per-frame layers from
  `metadata["generic_declarative_render"]` (rather than from raw params)
  — this guarantees the src render and metadata replay paths are
  byte-identical by construction.
