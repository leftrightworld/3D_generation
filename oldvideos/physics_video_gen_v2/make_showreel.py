"""Compose all scene mp4s into a single grid showreel video.

Auto-discovers every mp4 in out/ and out/scenes/, sorts alphabetically,
lays them out in a COLS-wide grid.  No ffmpeg installation needed — falls back
to the static binary bundled with imageio-ffmpeg if ffmpeg is not in PATH.

   * Each cell: 384×216 (16:9), 30 fps, 5 s per clip (loops / trims)
   * Output:    out/showreels/all_scenes_grid.mp4
   * Blank cells filled with the project's purple skybox colour (#bdaddb)
"""

import glob
import math
import os
import shutil
import subprocess
import sys


def _ffmpeg_exe() -> str:
    """Find ffmpeg: PATH first, then imageio-ffmpeg bundled binary."""
    p = shutil.which("ffmpeg")
    if p:
        return p
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        pass
    sys.exit(
        "ffmpeg not found.\n"
        "Install ffmpeg (https://ffmpeg.org) or run:  pip install imageio-ffmpeg"
    )


# ── Discover mp4s ──────────────────────────────────────────────────────────────
# Original 4 scenes live directly in out/; everything else in out/scenes/.
# Exclude the showreel output itself and per-employee grid files.
_EXCLUDE = {"all_scenes_grid.mp4", "a_scenes_grid.mp4",
            "c_all_scenes_grid.mp4", "all_d_scenes_grid.mp4"}

root_mp4s = sorted(
    p for p in glob.glob("out/*.mp4")
    if os.path.basename(p) not in _EXCLUDE
)
new_mp4s = sorted(
    p for p in glob.glob("out/scenes/*.mp4")
    if os.path.basename(p) not in _EXCLUDE
)
mp4s = root_mp4s + new_mp4s

if not mp4s:
    sys.exit("No mp4s found under out/. Run from the project root.")

missing = [p for p in mp4s if not os.path.isfile(p)]
if missing:
    print("WARNING: missing files (skipping):")
    for m in missing:
        print(f"  {m}")
    mp4s = [p for p in mp4s if p not in missing]

# ── Layout ─────────────────────────────────────────────────────────────────────
CELL_W      = 384
CELL_H      = 216
DURATION    = 5.0
FPS         = 30
BLANK_COLOR = "0xbdaddb"   # project's purple skybox
OUT_PATH    = "out/showreels/all_scenes_grid.mp4"

n_scenes = len(mp4s)
COLS     = min(10, math.ceil(math.sqrt(n_scenes)))
ROWS     = math.ceil(n_scenes / COLS)
n_total  = COLS * ROWS
n_blanks = n_total - n_scenes

print(f"{n_scenes} scenes → {COLS}×{ROWS} grid "
      f"({COLS*CELL_W}×{ROWS*CELL_H} px, {n_blanks} blank cells)")

# ── Build ffmpeg command ───────────────────────────────────────────────────────
ffmpeg = _ffmpeg_exe()
cmd = [ffmpeg, "-y", "-hide_banner", "-loglevel", "warning"]

for mp4 in mp4s:
    cmd += ["-stream_loop", "-1", "-i", mp4]
for _ in range(n_blanks):
    cmd += ["-f", "lavfi",
            "-i", f"color=c={BLANK_COLOR}:s={CELL_W}x{CELL_H}:d={DURATION}:r={FPS}"]

filter_parts = []
for i in range(n_scenes):
    filter_parts.append(
        f"[{i}:v]trim=0:{DURATION},setpts=PTS-STARTPTS,"
        f"scale={CELL_W}:{CELL_H},setsar=1[v{i}]"
    )
for j in range(n_blanks):
    idx = n_scenes + j
    filter_parts.append(f"[{idx}:v]setsar=1[v{idx}]")

layout = "|".join(
    f"{c*CELL_W}_{r*CELL_H}"
    for r in range(ROWS) for c in range(COLS)
)
inputs_chain = "".join(f"[v{i}]" for i in range(n_total))
filter_parts.append(
    f"{inputs_chain}xstack=inputs={n_total}:layout={layout}[out]"
)

cmd += ["-filter_complex", ";".join(filter_parts)]
cmd += ["-map", "[out]"]
cmd += ["-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-preset", "medium", "-crf", "20",
        "-r", str(FPS), "-t", str(DURATION)]
cmd += [OUT_PATH]

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
print("Running ffmpeg…")
subprocess.run(cmd, check=True)

size_mb = os.path.getsize(OUT_PATH) / 1e6
print(f"Wrote {OUT_PATH}  ({size_mb:.1f} MB, "
      f"{COLS*CELL_W}×{ROWS*CELL_H} @ {FPS} fps, {DURATION:.0f} s/cell)")
