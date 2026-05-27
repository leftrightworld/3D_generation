# physics_video_gen

A MuJoCo-based pipeline for producing a coherent *series* of physics
demonstration videos. Optimized for IPhO-style classical mechanics topics.

23 scenes done as of 2026-05-23 — see [DIARY.md](DIARY.md) for the inventory
and [out/scenes/all_scenes_grid.mp4](out/scenes/all_scenes_grid.mp4)
for a 5×5 showreel of everything.

## What this is, in one paragraph

You write a MuJoCo scene as an `.xml` file (or generate it from a Python
script for repetitive structures). You run `render.py` to produce a 1920×1080
mp4 clip of the physics playing out, and `make_grid.py` to produce a sparse
PNG that lets you verify the motion at a glance. Every scene shares the same
visual recipe (purple flat skybox + cream floor + warm wood + brass/red/blue
accents) so the whole series looks like one coherent set rather than random
clips.

## Quick start

```bash
# 1. Install deps (one-time)
pip install mujoco imageio numpy pillow

# 2. Render one of the existing scenes to see the output style
python3 render.py    --scene scenes/atwood.xml --out /tmp/atwood.mp4 --duration 3
python3 make_grid.py --scene scenes/atwood.xml --out /tmp/atwood_grid.png --duration 3

# 3. Open both and look — that's the standard quality bar.
```

## Adding a new scene (5-step recipe)

1. **Pick a topic** from [BACKLOG.md](BACKLOG.md). Mark it claimed.
2. **Copy a similar existing scene** as a starting point. For example, if you
   want to do a new pendulum variant, start from `scenes/pendulum.xml` or
   `scenes/double_pendulum.xml`. Don't write from scratch.
3. **Adapt the physics + camera**. Match the style guide
   ([docs/style_guide.md](docs/style_guide.md)) for skybox, floor, lighting,
   wood tones, accent colors.
4. **Render + verify**:
   ```bash
   python3 render.py    --scene scenes/X.xml --out out/scenes/X.mp4 \
                        --duration T [--init-qpos ...] [--init-qvel ...]
   python3 make_grid.py --scene scenes/X.xml --out out/X_grid.png \
                        --duration T --cols 4 --rows 2 [--init-qpos ...]
   ```
   **Open the grid PNG.** Grids surface framing / physics issues that videos
   hide. Iterate parameters until the grid looks right (usually 2-5
   iterations).
5. **Document**: update [DIARY.md](DIARY.md) inventory, strike the BACKLOG
   entry. If you hit a non-obvious MuJoCo behavior, append it to
   [docs/gotchas.md](docs/gotchas.md).

## Repository layout

```
physics_video_gen/
├── CLAUDE.md            # AI-agent entry doc (read first if you're Claude / an LLM)
├── README.md            # ← you are here
├── BACKLOG.md           # candidate scenes (claim before starting)
├── DIARY.md             # what's been done + recent decisions
├── docs/
│   ├── style_guide.md   # visual recipe (colors, lighting, camera rules)
│   └── gotchas.md       # 18 MuJoCo traps already hit + their fixes
├── render.py            # XML scene → mp4 clip
├── make_grid.py         # XML scene → grid PNG (verification artifact)
├── make_showreel.py     # all scene mp4s → one 5×5 grid showreel
├── scenes/
│   ├── *.xml            # MuJoCo scene definitions
│   └── gen_*.py         # programmatic XML generators (run them to regenerate .xml)
└── out/
    ├── *.png            # grid verification artifacts (throwaway)
    ├── bowling.mp4 etc. # the original 4 scenes
    └── scenes/       # all scene mp4s scenes' mp4s live here
        ├── *.mp4
        └── all_scenes_grid.mp4   # 5×5 showreel of everything
```

## How the work scales

The pipeline is intentionally simple — XML → mp4. There's no shared state
between scenes, so multiple people (or multiple AI agents) can work in
parallel on different scenes without merge conflicts. The only coordination
needed is:

- **Claim a BACKLOG entry before starting** — so two people don't make two
  Atwood machines.
- **Match the visual style** — see `docs/style_guide.md`.
- **Add to DIARY when done** — so the next person sees what already exists.

A realistic single-person throughput is **3-6 scenes per day** once the
workflow is familiar (each scene is 30 min - 2 h depending on physics
complexity). Five people in parallel ≈ 20-30 scenes per day.

## What's in scope, what isn't

✅ **In scope (MuJoCo is great at):**
- Rigid body dynamics — collisions, rolling, rotation, friction
- Pendulums of all kinds (single, double, coupled, conical, gimbal)
- Springs, oscillators, tendons, ropes (via spatial tendons)
- Constrained motion (joints, equalities)
- Discretized continuum (segmented beams, chains)

❌ **Out of scope (MuJoCo can't do well or at all):**
- Fluid dynamics — granular (balls-as-fluid) is a partial workaround for
  centrifugal/sloshing demos only, see `gen_rotating_fluid.py`
- Electromagnetism (no native EM force)
- Optics / ray tracing (no native)
- Thermodynamics / gases / phase transitions
- Relativity, quantum mechanics

If a candidate scene needs anything in the ❌ column, leave it out or flag
it for a different tool.

## Why we do it this way

- **Why MuJoCo over Blender?** MuJoCo simulates the physics; Blender just
  animates pre-computed transforms. For an educational series where the
  physics is the point, simulation is more authentic and you can change
  initial conditions without re-animating.
- **Why MuJoCo over Bullet / Isaac / Genesis?** MuJoCo has the cleanest XML
  scene format and the best default contact / constraint behavior for
  short-timescale rigid-body demos. We don't need GPU throughput or
  differentiable physics here.
- **Why a consistent skybox/floor?** The series is meant to be watched as a
  set. Inconsistent lighting between scenes breaks the "one coherent series"
  feel.
- **Why grid PNG before mp4 inspection?** A 30 fps video plays the buggy
  frame for 33 ms and you miss it. A grid shows 8 evenly-sampled phases
  side-by-side; bugs jump out.
