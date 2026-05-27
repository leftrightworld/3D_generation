# CLAUDE.md — Project Context for AI Agents

You're joining a MuJoCo-based physics scene renderer. Your job is to add new
scenes that match the established style and pass the verification workflow.

> **If you see `HANDOFF_RULES.md` and `ASSIGNMENT.md` at the repo root**, this
> is a generated employee handoff package (not the master repo). Read
> `HANDOFF_RULES.md` for additional restrictions (only-add files, don't edit
> shared docs, etc.) on top of everything below.

## What this repo is

A small pipeline that produces a *series* of physics demonstration videos for
classical mechanics topics. Each scene is a single `.xml` MuJoCo model + a
rendered `.mp4` clip showing the physics in motion. 23 scenes already exist
(see [DIARY.md](DIARY.md) for the inventory).

Long-term goal: front-end of a Sim2Reason / P1-style pipeline (physics sim →
QA generation → RL training). Right now this repo's scope is **scenes +
render only** — don't add QA / training / LLM code here.

## ⚠️ Before you write anything

Read in this order, top-down:

1. **This file** (you are here)
2. [docs/style_guide.md](docs/style_guide.md) — the visual recipe every scene must match
3. [docs/gotchas.md](docs/gotchas.md) — 18 traps already hit; re-reading them costs 5 min, re-discovering them costs hours
4. [BACKLOG.md](BACKLOG.md) — list of candidate scenes; pick one that isn't taken
5. [DIARY.md](DIARY.md) — what's already done, recent decisions

## Workflow for a new scene

```
1. Pick a topic from BACKLOG.md (or get one assigned).
2. Write scenes/<name>.xml — start by copying an existing scene close to
   what you want, then adapt.  Match the style guide verbatim (colors,
   lighting, camera framing).
3. Render an mp4 + a grid PNG:
     python3 render.py    --scene scenes/<name>.xml --out out/scenes/<name>.mp4 --duration T
     python3 make_grid.py --scene scenes/<name>.xml --out out/<name>_grid.png      --duration T --cols 4 --rows 2
4. OPEN THE GRID PNG.  Verify physics, camera framing, and that the motion
   is visible.  Mp4s hide problems; grids surface them immediately.
5. Iterate parameters (stiffness, damping, init-qpos, init-qvel, camera) until
   the grid looks right.  This usually takes 2-5 iterations.
6. If you hit a non-obvious MuJoCo behavior that cost > 30 min to debug,
   ADD IT TO docs/gotchas.md before moving on.
7. Update DIARY.md: add the scene to the inventory table and the "recently
   completed" list.
8. Move the BACKLOG item to "Done" or strike it through.
```

## Critical conventions — do not deviate

- **Output dir**: new mp4s go to `out/scenes/<scene>.mp4`. **Not** `out/`
  root — that's reserved for the 4 original scenes
  (bowling/marble/pendulum/projectile_jenga). Grid PNGs stay in `out/`
  (throwaway verification).
- **Scene file naming**: `scenes/<name>.xml`. For scenes with repetitive
  structure (chains, ramps, lots of identical objects), generate from
  `scenes/gen_<name>.py` — see `gen_dominoes.py`, `gen_brachistochrone.py`,
  `gen_beam_buckling.py`, `gen_rotating_fluid.py` for examples.
- **Visual style is non-negotiable**: purple flat skybox + cream floor +
  warm wood + brass/red/blue accents. See `docs/style_guide.md`. If you want
  a new accent color, get it approved before shipping.
- **Grid PNG is the truth**: render the mp4 too, but the grid is what you
  inspect to declare done. Many physics bugs are invisible at video frame
  rate but obvious in a sparse grid.
- **Duration**: pick the shortest duration that shows the full physics
  story. Most scenes are 3-5 s; pendulum_waves is 15 s; brachistochrone is
  1.2 s. Don't pad with empty motion.

## Anti-patterns — don't do these

- ❌ Inventing new colors / lighting setups per scene
- ❌ Skipping the grid PNG verification
- ❌ Putting new mp4s in `out/` root instead of `out/scenes/`
- ❌ Using `cat`/`echo`/`sed` for file edits — use the Edit/Write tools
- ❌ Starting a scene from scratch — always copy an existing similar scene
- ❌ Hardcoding the same numeric parameter 10 times — use a Python generator
- ❌ Adding scenes outside mechanics scope (no EM, no fluid beyond granular,
  no optics, no thermo) — those need a different tool

## Tools you'll use

- `render.py` — produces an mp4 from an XML scene. Args: `--scene`, `--out`,
  `--duration`, `--fps` (default 30), `--init-qpos`, `--init-qvel`, `--camera`
  (default "cam"). Resolution defaults to 1920×1080.
- `make_grid.py` — produces a 2×4 (or N×M) grid PNG showing N×M evenly
  spaced frames. Same args + `--cols`, `--rows`.
- `make_showreel.py` — composes all scene mp4s into a single 5×5 grid video.
  Run after adding scenes so the showreel includes them.

## Memory hygiene

When you finish a scene, also:
- Update [DIARY.md](DIARY.md) inventory table
- Strike off the BACKLOG entry
- If you discovered a gotcha, append to `docs/gotchas.md`
- If you added a new visual element worth reusing (a new material color,
  a useful camera framing trick), add it to `docs/style_guide.md`

The next agent that joins reads exactly these files. **Keep them current.**

## Quick sanity checks before declaring done

- [ ] mp4 exists in `out/scenes/<name>.mp4`
- [ ] Grid PNG looked physically correct (you actually opened it)
- [ ] Visual style matches existing scenes (skybox, floor, lighting unchanged)
- [ ] DIARY.md updated
- [ ] BACKLOG.md entry struck through
- [ ] Any new gotcha is in `docs/gotchas.md`
