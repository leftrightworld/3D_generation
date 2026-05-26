#!/usr/bin/env python3
"""
Smoke: one meta sample + metadata_builder.verify_metadata + vbvr-meta keys + replay_metadata.
No Evalkit (demo task has no evaluator). See eval/EVAL.md.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_TOP_LEVEL = (
    "task_id",
    "generator",
    "schema_version",
    "timestamp",
    "parameters",
    "param_hash",
    "generation",
    "semantic_ground_truth",
    "scoring_contract",
    "generic_declarative_render",
    "provenance",
)


def main() -> None:
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from core.metadata_builder import verify_metadata

    with tempfile.TemporaryDirectory() as td_s:
        td = Path(td_s)
        gen = subprocess.run(
            [
                sys.executable,
                str(ROOT / "examples" / "generate.py"),
                "--num-samples",
                "1",
                "--seed",
                "0",
                "--output-dir",
                str(td),
            ],
            cwd=str(ROOT),
        )
        if gen.returncode != 0:
            print("FAIL: generate.py", file=sys.stderr)
            sys.exit(1)

        cfg_txt = (ROOT / "src" / "config.py").read_text(encoding="utf-8")
        mdom = re.search(r'domain:\s*str\s*=\s*"([^"]+)"', cfg_txt)
        dom = mdom.group(1) if mdom else "template_demo"
        meta_path = td / f"{dom}_task" / f"{dom}_00000000" / "metadata.json"
        if not meta_path.is_file():
            print(f"FAIL: missing {meta_path}", file=sys.stderr)
            sys.exit(2)

        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if not verify_metadata(meta):
            print("FAIL: verify_metadata(base fields)", file=sys.stderr)
            sys.exit(3)

        missing = [k for k in REQUIRED_TOP_LEVEL if k not in meta]
        if missing:
            print(f"FAIL: missing keys: {missing}", file=sys.stderr)
            sys.exit(4)

        gdr = meta.get("generic_declarative_render") or {}
        if gdr.get("schema") != "generic_declarative_canvas_v2":
            print("FAIL: generic_declarative_render.schema", file=sys.stderr)
            sys.exit(5)

        out_render = td / "replay_out"
        rp = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "replay_metadata.py"),
                "--json",
                str(meta_path),
                "--output-dir",
                str(out_render),
            ],
            cwd=str(ROOT),
        )
        if rp.returncode != 0:
            print("FAIL: replay_metadata.py", file=sys.stderr)
            sys.exit(6)

        tid = meta["task_id"]
        sample_out = out_render / tid
        for name in ("prompt.txt", "first_frame.png", "final_frame.png", "ground_truth.mp4"):
            if not (sample_out / name).is_file():
                print(f"FAIL: replay missing {name} under {sample_out}", file=sys.stderr)
                sys.exit(7)

    print("OK: meta contract + declarative replay smoke passed.")


if __name__ == "__main__":
    main()
