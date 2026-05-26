# QA Report — G-1 Object Trajectory (vbvr-meta v0 pilot)

**Pilot date:** 2026-05-17
**Source legacy:** `重构_待办/G-1_object_trajectory_data-generator/` (GitHub: `VBVR-DataFactory/G-1_object_trajectory_data-generator`)
**Canonical core baseline:** `重构/G-13_grid_number_sequence_data-generator/core/`
**Kin reference (not copied):** `重构/G-8_track_object_movement_data-generator/`, `重构/O-13_shape_outline_then_move_data-generator/`
**Pilot template:** `重构_v2/Multi-08_sliding_puzzle_data-generator/` (read-only reference)

---

## All gates passed

| Gate | Command | Result |
|---|---|---|
| Meta-only generation | `examples/generate.py --num-samples 5 --seed 42 --output-dir ./qa_out` | **PASS** — 5/5 `metadata.json` written |
| Render generation | `examples/generate.py --num-samples 5 --seed 42 --output-dir ./qa_full --render` | **PASS** — 5/5 metadata + first/final PNG + ground_truth.mp4 written |
| Meta/render parity | `tools/check_meta_render_parity.py --qa-out ./qa_out --qa-full ./qa_full --num-samples 5 --semantic-keys task_type,shape,start_pos_px,end_pos_px,path_length_px` | **PASS** — `parameters`, `param_hash`, `generic_declarative_render`, and all 5 semantic keys match |
| Schema contract | `eval/verify_meta_contract.py` | **PASS** — all 11 top-level keys present, declarative replay produces all 4 artefacts (`first_frame.png`, `final_frame.png`, `ground_truth.mp4`, `prompt.txt`) |
| Pixel-level replay parity | metadata-replay vs src-render, `PIL.ImageChops.difference(...).getbbox()` | **PASS** — first_frame + final_frame across all 5 samples: **10 / 10 frames byte-identical** (bbox `None`) |

---

## Sample distribution (seed=42, default config)

| # | Shape | Color (hex) | Start (x, y) | End (x, y) | Path length (px) | Heading (deg) | param_hash |
|--:|---|---|---|---|---:|---:|---|
| 0 | triangle | `#6e9b42` | (537, 745) | (190, 85) | 745.7 | -117.7 | `388cb9e9d9f70c46` |
| 1 | square   | `#7e3b9b` | (713, 479) | (697, 842) | 363.4 |  92.5 | `b4de2508b62473cd` |
| 2 | circle   | `#afa9b2` | (521, 733) | (802, 161) | 637.3 | -63.8 | `af94afffa3bd3132` |
| 3 | square   | `#61677a` | (321, 864) | (768, 819) | 449.3 |  -5.7 | `295fa43a4b733b90` |
| 4 | diamond  | `#78785f` | (752, 735) | (100, 299) | 784.3 | -146.2 | `7dddc41ad4242499` |

- **Shape distribution:** 4 distinct shapes seen out of 4 in the pool (`triangle ×1`, `square ×2`, `circle ×1`, `diamond ×1`).
- **Colour:** five distinct RGB triples, all in the legacy `[50, 200]` per-channel range.
- **Path length:** 363 – 784 px, all above the `min_separation_px = 120` floor (and above the `0.35 * min(W,H) = 358` floor for 1024×1024).
- **Heading:** four quadrants represented (NE, NW, SE; only SW absent from 5 samples — expected variance).

→ Random sampling is healthy on this small 5-sample slice. Param hashes are all distinct (no collisions, so `_seen` dedupe path was never triggered for `--seed 42 / num-samples 5`).

---

## Pixel parity numbers

| Sample | first_frame diff bbox | final_frame diff bbox |
|---|---|---|
| `..._00000000` | `None` | `None` |
| `..._00000001` | `None` | `None` |
| `..._00000002` | `None` | `None` |
| `..._00000003` | `None` | `None` |
| `..._00000004` | `None` | `None` |

All 10 image pairs are byte-identical. `tools/replay_metadata.py` reproduces the same image data as `src/generator.py`'s render path because both use the **exact same drawing primitives** and the `--render` path **re-uses the per-frame layer list from `metadata["generic_declarative_render"]`** instead of recomputing from raw params (see `_render_layers` in `src/generator.py`).

---

## Layer vocabulary used

| Layer type | Where it appears | Fields |
|---|---|---|
| `dashed_shape_outline` | First / final / every video frame (target outline is static) | `shape`, `center_px`, `radius_px`, `color_rgb`, `line_width_px`, `dash_length_px` |
| `filled_shape` | First / final / every video frame (one moving shape per frame) | `shape`, `center_px`, `radius_px`, `fill_rgb`, `outline_rgb`, `outline_width_px` |

Both are **new primitives** added to the `generic_declarative_canvas_v1` schema for this generator. `tools/replay_metadata.py` keeps backward-compatible support for the four pilot-#1 primitives (`grid_lines`, `labeled_tile`, `floating_tile`, `filled_rectangle`).

**Why two task-specific primitives instead of one monolithic layer:** a future sibling task with multiple shapes (e.g., G-1 variant with two simultaneously moving shapes, or G-8-style multi-object tracking) can compose the same two primitives without schema churn. The shape kernel (`circle / square / triangle / diamond`) is parameterised, not enumerated.

---

## "Found kin, didn't copy" — code overlap analysis

| File | vs G-8 (track object) | vs O-13 (outline-then-move) | Notes |
|---|---|---|---|
| `src/generator.py` | DIFFERENT | DIFFERENT | Re-derived from legacy G-1; legacy was 230 LoC, refactored is 473 LoC (added meta-bundle path, `_ensure_specs`, declarative layer rendering). |
| `src/config.py` | DIFFERENT | DIFFERENT | Lifted hyperparams (`ball_radius=70`, `color_min/max=50/200`, fps=16, 1s+2s+1s phases) directly from legacy values, but wrapped in pydantic + plain `domain: str = ...` syntax. |
| `src/prompts.py` | DIFFERENT | DIFFERENT | EN prompt preserved verbatim from legacy; added EN/ZH summaries + rules list. |
| `core/declarative_spec.py` | **DIFFERENT** (different layer vocab) | **DIFFERENT** (G-1 chose generic primitives; O-13 uses task-private `o13_shape` / `o13_arrow` / `o13_question`). | Generic-primitives route consistent with pilot #1 (Multi-08). |
| `tools/replay_metadata.py` | DIFFERENT | DIFFERENT | Task-specific drawing helpers in this generator are a verbatim mirror of `src/generator.py`'s helpers (so replay path is byte-identical). |
| `core/base_generator.py` | SAME | SAME | Canonical (intentional — copied from G-13). |
| `core/image_utils.py` | SAME | SAME | Canonical. |
| `core/video_utils.py` | SAME | SAME | Canonical. |
| `core/schemas.py` | SAME | SAME | Canonical. |
| `core/metadata_builder.py` | SAME | SAME | Canonical (from G-13). |
| `core/output_writer.py` | SAME | SAME | Canonical (from G-13). |

**Verdict:** Task logic was re-derived from the legacy G-1 codebase. Visual modelling intentionally followed the **pilot-#1 generic-primitives** route rather than the O-13-style monolithic-layer route. Shared `core/` infrastructure is byte-identical to the G-13 canonical baseline. No code was copied from any other refactored generator.

---

## Design decisions beyond the legacy

| Decision | Rationale |
|---|---|
| Default `generate_videos=False`; opt in with `--render` | vbvr-meta v0 convention: metadata is the primary artefact; media is on-demand. Legacy G-1 defaulted to videos on. |
| Two task-specific layer primitives (`dashed_shape_outline`, `filled_shape`) | Reusable for any single-object-translation task with a target-outline visual signal (multi-object variants compose multiple `filled_shape` layers). |
| `--render` path renders from `metadata["generic_declarative_render"]["…_frame"]["layers"]`, NOT from raw params | Guarantees byte parity between src-render and metadata-replay paths by construction — verified at `PIL.ImageChops` level. |
| `_stable_hash(task_id)` via SHA-256 prefix, not Python's built-in `hash()` | Python's `hash()` is per-process-salted; would silently break determinism across runs. (Pilot-#1 gotcha, pre-empted here.) |
| `_ensure_specs()` shared by both CLI modes | Without this, meta-only and `--render` paths could pull from different RNG positions and produce divergent parameters. The parity gate would fail. (Pilot-#1 gotcha, pre-empted here.) |
| `domain: str = "G-1_object_trajectory_data-generator"` plain assignment | The parity tool's regex (`r'domain:\s*str\s*=\s*"([^"]+)"'`) only matches plain syntax; `Field(default=...)` syntax would silently break domain detection. (Pilot-#1 gotcha, pre-empted here.) |
| `evaluator_class: "ObjectTrajectoryEvaluator"` with `evalkit_pending_confirmation: true` | EvalKit source not yet read; placeholder is honest. |
| Drop `setup.py`, `LICENSE`, `.gitmodules` | New repo is in-tree; deferred to a future packaging pass. |
| `min_separation_px = 120`, `min_separation_ratio = 0.35` | Preserves legacy `min_dist = max(120, int(min(W,H) * 0.35))` exactly. |
| Phases `1s + 2s + 1s` at fps=16 → 16+32+16 = 64 frames | Verified against generated `gdr["video"]["frames"]` length = 64. |

---

## Known follow-ups (not blocking pilot)

1. **EvalKit confirmation:** validate `evaluator_class` name (`ObjectTrajectoryEvaluator`) and the four dimension keys (`final_overlap_accuracy`, `trajectory_linearity`, `shape_color_preservation`, `target_static_preservation`) against the actual evaluator. Flip `evalkit_pending_confirmation` to `false` once verified.
2. **Video-frame-level parity:** current parity check covers `first_frame` + `final_frame` only. A frame-by-frame video diff (or hash of every interpolated frame) would strengthen the guarantee — the architecture already supports it because both src-render and replay paths consume identical layer lists.
3. **Layer vocabulary registration:** `dashed_shape_outline` + `filled_shape` should be added to a project-level layer-vocabulary doc (alongside pilot #1's `grid_lines` / `labeled_tile` / `floating_tile`) so future trajectory-style tasks (G-25 spinning, G-24 separate-no-spin, G-8 track-object) can reuse them.
4. **Auto-replay video parity:** extend `eval/verify_meta_contract.py` to additionally compare a replay-produced `ground_truth.mp4` against the src-produced one (frame-by-frame, since mp4 byte equality is codec-dependent).

---

## Pilot-level conclusions

- **Workflow validated, second time:** same "find kin → don't copy → strict parity" recipe used in pilot #1 (Multi-08) produced byte-identical replay on the first try for G-1. All four pilot-#1 gotchas (SHA-256 hash, `_ensure_specs`, plain `domain:` syntax, dir-clean idiom) were known up-front and avoided.
- **Generic-primitives schema is paying off:** the `generic_declarative_canvas_v1` schema absorbed two new primitives (`dashed_shape_outline`, `filled_shape`) cleanly. `tools/replay_metadata.py` now supports both pilot-#1 (grid-based) and G-1 (free-form-shape) tasks under one tool.
- **Wall-time:** G-1 took roughly **20 – 25 minutes of agent wall-time** end-to-end (read legacy + design metadata schema + write all files + run gates + write report). About half of pilot #1's 45 minutes, mostly because the workflow and the file scaffolding template were already in place.
- **Deviations from pilot #1:** none structural. The only differences are task-specific:
  - New layer vocabulary (`dashed_shape_outline`, `filled_shape` instead of `grid_lines` / `labeled_tile` / `floating_tile`).
  - Task params (radius / colour bounds / phase durations) ported from G-1 legacy.
  - Scoring dimensions named for trajectory tasks (`final_overlap_accuracy`, `trajectory_linearity`, `shape_color_preservation`, `target_static_preservation`) instead of sliding-puzzle dimensions.
  - `_seen` dedupe uses a `(shape, rgb, start, end)` signature (G-1 has only one task instance per signature, unlike multi-state puzzles).
