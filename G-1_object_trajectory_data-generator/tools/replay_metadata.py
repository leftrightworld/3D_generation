#!/usr/bin/env python3
"""Canonical replay tool — every project's tools/replay_metadata.py is a
1-line shim that re-exports this module. DO NOT re-implement per project.

Reads metadata.json, reconstructs first_frame.png, final_frame.png,
ground_truth.mp4 (if video frames present), prompt.txt — purely from
`metadata["generic_declarative_render"]`. Supports all 8 vbvr-meta canvas-v2
layer types via `core.declarative_renderer.render_frame`.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Discover the project root (parent of tools/) so we can import core.declarative_renderer
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.declarative_renderer import render_frame, write_video


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--json", type=Path, default=ROOT / "metadata.json")
    p.add_argument("--output-dir", type=Path, default=ROOT / "rendered")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    meta = json.loads(args.json.read_text(encoding="utf-8"))
    gdr = meta.get("generic_declarative_render") or {}
    if not gdr:
        print("No generic_declarative_render in metadata", file=sys.stderr)
        sys.exit(1)
    task_id = meta.get("task_id", "unknown_task")
    out = args.output_dir.resolve() / task_id
    out.mkdir(parents=True, exist_ok=True)
    canvas = gdr["canvas"]
    (out / "prompt.txt").write_text(gdr.get("prompt", ""), encoding="utf-8")
    first = render_frame(canvas, gdr["first_frame"])
    final = render_frame(canvas, gdr["final_frame"])
    first.save(out / "first_frame.png")
    final.save(out / "final_frame.png")
    vid = gdr.get("video") or {}
    fps = int(vid.get("fps", 8))
    frames = [render_frame(canvas, f) for f in vid.get("frames", [])]
    if frames:
        write_video(frames, fps, out / "ground_truth.mp4")
    print(f"OK: wrote under {out}")


if __name__ == "__main__":
    main()
