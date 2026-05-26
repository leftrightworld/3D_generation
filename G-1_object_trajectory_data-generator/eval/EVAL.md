# Local eval (G-1 object trajectory)

## What this is

This folder runs **contract + replay smoke** — it does **not** invoke a real
VBVR-Evalkit `ObjectTrajectoryEvaluator`. The pending real-evaluator wiring
is flagged in `metadata.scoring_contract.evalkit_pending_confirmation: true`.

| Script | Purpose |
|--------|---------|
| `verify_meta_contract.py` | Generate 1 meta sample → `verify_metadata` base fields → all `vbvr-meta-v0` top-level keys present → `tools/replay_metadata.py` reproduces `first_frame.png`, `final_frame.png`, `ground_truth.mp4`, `prompt.txt`. |

## Run

```bash
pip install -r requirements.txt   # replay step requires opencv for mp4
python3 eval/verify_meta_contract.py
```

Exit code **0** = the generator's metadata is well-formed and self-replayable.

## When wiring a real evaluator

1. Confirm `evaluator_class` name in EvalKit (currently flagged as pending).
2. Confirm the four scoring-dimension keys match what the evaluator expects
   (currently: `final_overlap_accuracy`, `trajectory_linearity`,
   `shape_color_preservation`, `target_static_preservation`).
3. Add a second script that runs the evaluator on a small self-score batch
   and checks the result is a perfect score.
4. Flip `evalkit_pending_confirmation` to `false` in
   `src/generator.py::_attach_meta_extensions`.
