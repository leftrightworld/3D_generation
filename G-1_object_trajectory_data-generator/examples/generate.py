"""Default: meta-only. Optional `--render` writes media + metadata."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core import OutputWriter
from src import TaskConfig, TaskGenerator


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="vbvr-meta v0 — G-1 object-trajectory generator.")
    p.add_argument("--num-samples", type=int, default=1)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--output-dir", type=Path, default=Path("out_meta"))
    p.add_argument(
        "--render",
        action="store_true",
        help="Also write prompt.txt, PNGs, ground_truth.mp4 (requires opencv-python).",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    config = TaskConfig(
        num_samples=args.num_samples,
        random_seed=args.seed,
        output_dir=args.output_dir,
        generate_videos=bool(args.render),
    )
    gen = TaskGenerator(config)
    out = args.output_dir.resolve()
    domain = config.domain

    if args.render:
        pairs = gen.generate_dataset()
        writer = OutputWriter(config.output_dir)
        writer.write_dataset(pairs)
        print(f"Rendered {len(pairs)} samples to {config.output_dir}")
        return

    task_dir = out / f"{domain}_task"
    task_dir.mkdir(parents=True, exist_ok=True)
    for i in range(args.num_samples):
        task_id = f"{domain}_{i:08d}"
        meta = gen.generate_metadata_bundle(task_id)
        sample_dir = task_dir / task_id
        sample_dir.mkdir(parents=True, exist_ok=True)
        (sample_dir / "metadata.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(f"Wrote {args.num_samples} metadata.json under {task_dir}")


if __name__ == "__main__":
    main()
