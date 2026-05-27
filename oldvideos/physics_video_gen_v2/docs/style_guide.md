# Visual Style Guide

Every scene in this project follows the same visual recipe. **New scenes MUST
match this**, otherwise the series feels inconsistent when watched as a set.

## Why this matters

The pipeline produces a *series* of physics demo videos. Inconsistent skybox /
lighting / floor / wood tones between scenes breaks the look and makes them
feel like random clips rather than a curated collection. The recipe below was
tuned over the first ~5 scenes and every subsequent scene reuses it verbatim.

## The recipe — copy this verbatim

```xml
<option timestep="0.001 or 0.002" gravity="0 0 -9.81" integrator="implicitfast"
        impratio="3" cone="elliptic"/>   <!-- impratio/cone for contact scenes -->

<visual>
  <headlight diffuse="0 0 0" ambient="0.50 0.48 0.55" specular="0 0 0"/>
  <rgba haze="0.94 0.91 0.90 1"/>
  <global azimuth="120" elevation="-15" offwidth="1920" offheight="1080" fovy="35-42"/>
  <quality shadowsize="8192" offsamples="8"/>
  <map shadowclip="6" shadowscale="0.7"/>
</visual>

<asset>
  <!-- Flat purple skybox (NOT gradient — avoids the wavy seam at horizon) -->
  <texture type="skybox" builtin="flat"
           rgb1="0.74 0.68 0.86" rgb2="0.74 0.68 0.86"
           width="512" height="512" mark="none" markrgb="0 0 0"/>
  <material name="floor_mat" rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
  <!-- Warm wood palette for structural elements -->
  <material name="wood"      rgba="0.93 0.82 0.58 1" specular="0.1" shininess="0.1"/>
  <material name="wood_dark" rgba="0.78 0.65 0.40 1" specular="0.1" shininess="0.1"/>
</asset>

<worldbody>
  <!-- Two-light setup: key from upper-left-front + cool fill from opposite -->
  <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
         diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
  <light pos="0 0  8" dir=" 0.40 -0.30 -1" directional="true" castshadow="false"
         diffuse="0.28 0.28 0.34" specular="0 0 0"/>

  <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>
  ...
  <!-- 3/4 view camera with explicit xyaxes (not quat) for predictability -->
  <camera name="cam" pos="..." fovy="35-42" xyaxes="... ... 0   ... ... ..."/>
</worldbody>
```

## Accent material palette

Don't invent ad-hoc colors. Pick from these for moving objects:

| Material name        | rgba                       | specular / shininess | Use for                           |
|----------------------|----------------------------|----------------------|-----------------------------------|
| `ball_brass`         | 0.90 0.74 0.36 1           | 0.7 / 0.85           | Newton's cradle, Maxwell wheel disc |
| `bob_red` / `m_heavy`| 0.86 0.34 0.30 1           | 0.35-0.4 / 0.4       | Heavy mass, "hot" object          |
| `bob_blue` / `m_light`| 0.30 0.50 0.78 1          | 0.35-0.4 / 0.4       | Light mass, "cool" object         |
| `block_cream`        | 0.96 0.92 0.85 1           | -                    | Generic block                     |
| `block_blue`         | 0.34 0.52 0.80 1           | -                    | Accent block                      |
| `string_mat` / `rod` | 0.28-0.30 0.25-0.27 0.22-0.24 1 | 0                | Strings, ropes, thin rods         |

## Camera rules of thumb

- **Distance**: pos at distance ≈ 2× scene extent, at height ≈ 1× scene height
- **fovy**: 35-42°. Lower = more zoomed-in, less perspective distortion.
- **3/4 view**: cam_xy makes ~30-45° with the principal motion axis.
- **Frame the motion CENTER**, not the floor — common bug is camera looks too low,
  putting subject in upper third with empty floor below.
- **Verify the frame is wide enough**: if column is 1 m tall and motion deflects
  ~0.5 m sideways, you need ≥ 1.5 m of width × 1.2 m of height in frame at the
  scene's depth plane.

## Strings, springs, ropes

- Use `<tendon><spatial>` with sites, **NOT** a fixed capsule (a capsule can't
  stretch / change length and looks rigid).
- Place `<tendon>` as a **TOP-LEVEL element** under `<mujoco>`, NOT inside
  `<worldbody>`. (MuJoCo schema rule — see gotcha #2.)
- Sites that the tendon references can live anywhere — inside bodies, inside
  worldbody, doesn't matter.

## Render + verify workflow

```bash
python3 render.py    --scene scenes/X.xml --out out/scenes/X.mp4 \
                     --duration T [--init-qpos ...]
python3 make_grid.py --scene scenes/X.xml --out out/X_grid.png \
                     --duration T --cols 4 --rows 2 [--init-qpos ...]
```

**Output dir convention**: new scenes' mp4s go in `out/scenes/`. Only the
original 4 (bowling/marble/pendulum/projectile_jenga) live in `out/` directly.
Grid PNGs stay in `out/` (throwaway verification, not part of the deliverable).

**Always inspect the grid PNG before declaring done.** Videos hide framing /
physics issues that grids surface immediately. If a scene's motion period is
close to `duration / (cols × rows)`, the grid samples alias — use `--cols 6
--rows 2` (12 frames) or a different duration to break the aliasing.
