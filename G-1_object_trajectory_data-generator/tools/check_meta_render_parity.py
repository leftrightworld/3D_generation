#!/usr/bin/env python3
"""
Cross-platform check: meta-only vs --render outputs share the same task for each index.

Compares per sample:
  generator, parameters, param_hash, generic_declarative_render
and optional semantic_ground_truth keys (--semantic-keys).

Usage (from 04_NEW_GENERATOR_WORK, after generating qa_out + qa_full with the same --seed):
  python3 tools/check_meta_render_parity.py --qa-out ./qa_out --qa-full ./qa_full --num-samples 3
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def _domain_from_config(repo_root: Path) -> str:
    txt = (repo_root / "src" / "config.py").read_text(encoding="utf-8")
    m = re.search(r'domain:\s*str\s*=\s*"([^"]+)"', txt)
    if not m:
        raise SystemExit("Could not parse domain from src/config.py")
    return m.group(1)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--qa-out", type=Path, required=True)
    p.add_argument("--qa-full", type=Path, required=True)
    p.add_argument("--num-samples", type=int, default=3)
    p.add_argument(
        "--semantic-keys",
        default="task_type,correct_option_index,correct_shape,sequence,candidates,rule",
        help="Comma-separated semantic_ground_truth keys to compare",
    )
    args = p.parse_args()

    root = Path(__file__).resolve().parents[1]
    domain = _domain_from_config(root)
    keys = [k.strip() for k in args.semantic_keys.split(",") if k.strip()]

    for i in range(args.num_samples):
        tid = f"{domain}_{i:08d}"
        pa = args.qa_out.resolve() / f"{domain}_task" / tid / "metadata.json"
        pb = args.qa_full.resolve() / f"{domain}_task" / tid / "metadata.json"
        if not pa.is_file():
            print(f"FAIL: missing {pa}", file=sys.stderr)
            sys.exit(1)
        if not pb.is_file():
            print(f"FAIL: missing {pb}", file=sys.stderr)
            sys.exit(2)
        a = json.loads(pa.read_text(encoding="utf-8"))
        b = json.loads(pb.read_text(encoding="utf-8"))

        if a.get("generator") != b.get("generator"):
            print(f"FAIL: generator mismatch {tid}", file=sys.stderr)
            sys.exit(3)
        if a.get("parameters") != b.get("parameters"):
            print(f"FAIL: parameters mismatch {tid}", file=sys.stderr)
            sys.exit(4)
        if a.get("param_hash") != b.get("param_hash"):
            print(f"FAIL: param_hash mismatch {tid}", file=sys.stderr)
            sys.exit(5)
        if a.get("generic_declarative_render") != b.get("generic_declarative_render"):
            print(f"FAIL: generic_declarative_render mismatch {tid}", file=sys.stderr)
            sys.exit(6)
        sa = a.get("semantic_ground_truth") or {}
        sb = b.get("semantic_ground_truth") or {}
        for k in keys:
            if sa.get(k) != sb.get(k):
                print(f"FAIL: semantic_ground_truth[{k}] mismatch {tid}", file=sys.stderr)
                sys.exit(7)

    print(
        f"OK: meta/render parity for {args.num_samples} samples "
        f"({domain}); parameters, param_hash, declarative, semantic keys checked."
    )


if __name__ == "__main__":
    main()
