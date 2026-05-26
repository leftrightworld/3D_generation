# Returns log

Raw returns appended by `merge_return.py`. Skim this and manually promote items into `DIARY.md`, `BACKLOG.md`, or `docs/gotchas.md` as appropriate, then leave them here as historical record.


---

## Return: `A_return_2026-05-23.tar.gz` merged at 2026-05-25T00:36

# Return from A

**Your name:** A
**Round date (received):** 2026-05-23
**Return date:** 2026-05-23

---

## Tasks completed

- [x] **bifilar_pendulum** — two-string horizontal rod, different string lengths, 6s
- [x] **wilberforce_pendulum** — spring–torsional energy exchange on helical spring, 18s
- [x] **damped_pendulum_decay** — viscous damping, exponential amplitude decay, 8s
- [x] **yoyo_with_reversal** — Maxwell yo-yo descent, bottom bounce, spin reversal, 9s
- [x] **coin_spiral** — coin on edge precesses ~7 s then flops flat, 10s
- [x] **inelastic_collision** — two blocks stick together after impact, 3.5s
- [x] **coefficient_of_restitution** — ball bounce height decays geometrically (e≈0.7), 14s
- [x] **com_pair_track** — equal masses fly apart from compressed spring, COM fixed, 5s
- [x] **beats** — two spring oscillators, beating envelope, 18s
- [x] **wave_reflection_fixed** — pulse on string reflects inverted from clamped end, 5s
- [x] **capstan_effect** — rope wrap holds lighter load against heavier, 7s
- [x] **falling_chain_classical** — chain sags then accelerates downward, 3.5s
- [x] **bead_on_helix** — bead slides down helical rail under gravity, 7.5s

Showreel: `out/new_scenes/a_scenes_grid.mp4` (4×4 grid of the 13 clips above).

## Tasks incomplete or blocked

- [ ] **tippe_top** — not started this round
- [ ] **slider_crank_mechanism** — not started this round
- [ ] **arch_compression** — not started this round
- [ ] **cone_balanced_on_tip** — not started this round

## New gotchas hit (worth adding to docs/gotchas.md)

### Coin spiral: spin must be about body z, not world z; quaternion precision matters

**What happened:** Rendering with `--init-qvel=0,0,0,0,0,10` made the coin lie flat in ~0.5 s. Even with the correct spin axis, rounding qpos/qvel to 3–4 decimals caused early collapse to ~22° without ever going flat.

**Why:** For a freejoint, qvel angular part is in the world frame. A coin ~88° on edge needs ω along its symmetry axis (body +z), not world +z. This stiff contact problem is chaotic; small quaternion errors change the outcome.

**Fix / how to apply:** Compute world-frame angular velocity as `qvel[3:6] = quat_rotate(qpos[3:7], [0,0,1]) * spin_rate`. Store full-precision init values in XML comments / render batch. Tune friction (~0.65 sliding) and spin (~34 rad/s) for ~7 s edge precession before flop.

## New scene ideas worth adding to BACKLOG

(none this round)

## Anything else (questions, comments, blockers)

Added `scenes/gen_render_batch.py` and `scenes/gen_a_showreel.py` for batch render / A-package grid showreel. Left `_coin_trace*.py` in repo root from-template tuning scripts (optional to delete on merge).


---

## Return: `my_return_b_2026-05-24.tar.gz` merged at 2026-05-25T00:36

# Return from B

(Fill this in before sending the package back. Keep the headings — the master
keeper greps for them.)

**Your name:** B
**Round date (received):** 2026-05-23
**Return date:** 2026-05-23

---

## Tasks completed

List each scene you finished. For each, give a 1-line description and the
duration you rendered.

- [x] trifilar_pendulum — disc torsional oscillation on three strings, 4s
- [x] pendulum_with_air_drag — high-damping pendulum amplitude decay, 8s
- [x] anharmonic_pendulum_large_swing — large-angle pendulum (150°), 8s
- [x] rolling_cone — cone rolling in circular path, 5s
- [x] gyroscope_on_string — disc gyroscope precession on string, 5s
- [x] falling_chimney — tall rod tipping about base pivot, 1.5s
- [x] ballistic_pendulum — bullet embeds in pendulum bob, 3s
- [x] glancing_2d_collision — equal-mass glancing elastic collision, 2s
- [x] cannon_recoil — projectile forward, cannon rolls backward, 2.5s
- [x] normal_modes_2mass — antisymmetric two-mass spring mode, 4s
- [x] wave_reflection_free — pulse reflects at free end (same polarity), 4s
- [x] stick_slip — spring-driven block stick-and-slip on floor, 6s
- [x] dzhanibekov_effect — T-handle intermediate-axis flip in zero-g, 5s
- [x] sliding_chain_off_table — frictionless chain slides off table edge, 1.5s
- [x] bead_on_cycloid_track_isochrony — three beads on cycloid arrive together, 1.8s
- [x] geneva_drive — driver wheel rotates, driven wheel indexes, 5s
- [x] balance_beam_lever — lever returns to torque equilibrium, 3s

## Tasks incomplete or blocked

All 17 assigned scenes completed.

## New gotchas hit (worth adding to docs/gotchas.md)

### Negative init-qvel values break argparse

**What happened:** `--init-qvel -0.4,4,0,0,0,0` caused `render.py` to fail with "expected one argument" because argparse interprets `-0.4` as a new flag.

**Why:** Any `--init-qvel` value starting with `-` looks like a CLI option.

**Fix / how to apply:** Use the equals form: `--init-qvel=-0.4,4,0,0,0,0`.

## New scene ideas worth adding to BACKLOG

(none this round)

## Anything else (questions, comments, blockers)

- Used `E:\python\python3.12.6\python.exe` with mujoco 3.8.1 for rendering.
- Chain scenes (`wave_reflection_free`, `sliding_chain_off_table`) use nested body hierarchies with hinge joints.
- `geneva_drive` uses contact-based pin-slot engagement; indexing is qualitative rather than precision mechanical.


---

## Return: `c_return_2026-05-24.tar.gz` merged at 2026-05-25T00:36

# Return from C

(Fill this in before sending the package back. Keep the headings — the master
keeper greps for them.)

**Your name:** C (continued)
**Round date (received):** 2026-05-23
**Return date:** 2026-05-24

---

## Tasks completed

List each scene you finished. For each, give a 1-line description and the
duration you rendered.

- [x] **compound_pendulum_shapes** — 三根等质量复摆（杆/板/三角）周期对比，6s
- [x] **triple_pendulum** — 三重摆混沌甩动，8s（init-qpos 1.4,0,0）
- [x] **spherical_pendulum_2d** — 万向节球面摆玫瑰线轨迹，14s（俯视 cam_top，init-qpos 0,0.58 init-qvel 0.52,0.44）
- [x] **spool_with_string** — 线轴滚转+绳层切换，4s（init-qvel 0.28,0,0,0,-4.5,0）
- [x] **mass_through_hole** — 质点穿圆孔轨道，5s（init-qpos 0.85,0.40,0.08 init-qvel 2.2,0,0）
- [x] **reuleaux_triangle_rolling** — 鲁洛三角形等宽滚动+质心上下，4s（init-qvel 0.38,0,0,0,12,0）
- [x] **rattleback** — 凯尔特石 ~8s@60fps：顺向 ωz=-7 平稳 2.5s → 错向 ωz=+7.5 颠动反转 5s；居中相机、纯船形 hull（无调试色条/地面刻度）
- [x] **basketball_tennis_drop** — 大小球叠放落地能量传递，网球弹至数倍高度，4s
- [x] **line_collision_chain** — 无绳牛顿摆动量传递，2.5s（init-qvel 2,0,0,0,0,0）
- [x] **two_pendulums_collide** — 两等长摆底部弹性碰撞换速，3s（init-qpos 0.524,-0.524）
- [x] **vertical_spring_mass** — 竖直弹簧-质量块在拉伸平衡位置附近 SHM，5s（init-qpos -0.08）
- [x] **wave_on_heavy_rope** — 重绳顶部脉冲向下传播，3s（init-qvel 0,6,0）
- [x] **tipping_vs_sliding** — 24° 斜面高窄块倾覆 vs 低宽块滑动，4s
- [x] **hanging_chain_catenary** — 双端固定悬链线水平初态→下沉成悬链线，6s（render.py 运动学 sag 0→1，FABRIK 两端对齐）
- [x] **bead_on_parabolic_wire** — 抛物线导轨上滑块往复（周期随振幅变），4s
- [x] **domino_branching** — Y 形多米诺骨牌双分支级联，5s
- [x] **pyramid_keystone_removal** — 4-1-1-1 金字塔，0.55s 沉降后楔块 +y 滑出、上层坍塌，4s（render.py 自动 kick）

Also rendered **c_all_scenes_grid.mp4** — 17 场景 4×5 合集（见 scenes/gen_c_showreel.py）。

## Tasks incomplete or blocked

If you couldn't finish a task, say which one and why. If the physics was
harder than expected, what blocked you?

- (none — all 17 assigned scenes complete)

## New gotchas hit (worth adding to docs/gotchas.md)

If you (or your AI) hit a non-obvious MuJoCo behavior that cost more than
30 min to debug, describe it here. Use this format so the master keeper can
move it into `docs/gotchas.md` cleanly:

### Reuleaux triangle profile must live in the xz plane

**What happened:** Triangle built in the xy horizontal plane looked like it was sliding, not rolling; centroid didn't bob correctly.

**Why:** Rolling along +x with spin about +y requires the constant-width profile in the xz vertical plane.

**Fix / how to apply:** Generate arc capsules in xz; use freejoint + floor friction (slide+hinge froze ~0.5 s in).

### Spherical pendulum: use yaw+tilt gimbal, not two horizontal hinges

**What happened:** Early two-hinge setups gave flat or degenerate trajectories.

**Why:** Two coplanar horizontal hinges over-constrain or collapse the motion space.

**Fix / how to apply:** Outer hinge axis 0 0 1 (yaw), inner 0 1 0 (tilt); precompute floor trail in gen script; render with cam_top.

### Compound pendulum cluster: watch inter-pendulum clearance

**What happened:** Three pendulums clipped through each other and the support post at large angles.

**Fix / how to apply:** Lower pivot below crossbar, remove center post, angle initial qpos inward (~0.42 rad each), add thin suspension ropes.

### Nested chain XML: leaf link needs its own `<body>` tag

**What happened:** Recursive chain generators produced mismatched XML — leaf segment had `</body>` without an opening tag, or one extra closing tag.

**Fix / how to apply:** Base case of the recursion must emit a full `<body>…<joint/>…<geom/>…</body>` block, not just a geom inside the parent.

### Catenary chain: span must be shorter than total link length

**What happened:** Chain with total length equal to post span snapped into a straight diagonal under weld constraints; no visible sag.

**Fix / how to apply:** Either use excess length (L > span) or initialise link positions along a downward parabolic arc; weld right endpoint to post.

### Catenary chain: kinematic sag needs hinge sign flip + arc-length IK

**What happened:** Uniform-x catenary angles left the right end disconnected; removing q negation made the chain arch upward; joint range `-1.55 0.05` clamped needed angles.

**Fix / how to apply:** FABRIK + arc-length catenary in `render.py`; `qpos = -q` for MuJoCo Y-hinge convention; widen hinge range to `-1.55 1.55`.

### Rattleback: debug visuals and off-centre camera confuse the demo

**What happened:** Red/blue masts, yellow bow mark, deck strips, and floor cross/tick lines were for debugging spin/bob; oblique FREE camera offset the stone from frame centre.

**Fix / how to apply:** Hull-only visual; fixed centred XML camera; segment crossfade in `render_rattleback_compare()`.

### Pyramid keystone: side blocks catch the upper tier

**What happened:** Row-1 side blocks at full height formed a stable arch after keystone removal; soft contacts caused clipping.

**Fix / how to apply:** Row-1 keystone only (4-1-1-1 layout); stiff contacts; settle then timed kick in `render.py` (no brittle qvel index).

## New scene ideas worth adding to BACKLOG

Found a physics topic that would make a good scene but isn't in `BACKLOG.md`
yet? Suggest it here. Just a 1-line description per idea is fine.

- (none this round)

## Anything else (questions, comments, blockers)

Free-form. Anything you want the master keeper to know.

- All 17/17 assignment scenes done; mp4s in `out/new_scenes/`.
- **Master keeper note:** this return also modifies `render.py`, `make_grid.py`, and `scenes/gen_c_showreel.py` (catenary/rattleback/pyramid/showreel fixes). Please merge intentionally.
- Programmatic scenes: `gen_wave_on_heavy_rope.py`, `gen_hanging_chain_catenary.py`, `gen_bead_on_parabolic_wire.py`, `gen_domino_branching.py`, `gen_pyramid_keystone_removal.py`, `gen_rattleback.py`, `gen_c_showreel.py`.


---

## Return: `D_return_2026-05-24.tar.gz` merged at 2026-05-25T00:36

# Return from D

**Your name:** D
**Round date (received):** 2026-05-23
**Return date:** 2026-05-24

---

## Tasks completed

- [x] **cycloidal_pendulum_huygens** — Huygens cycloidal pendulum with guide cheeks, 4s
- [x] **rolling_chain** — tank-tread chain on floor, 4.5s
- [x] **centrifugal_governor** — Watt flyball governor at ω≈8 rad/s, 4s
- [x] **pulley_with_inertia** — Atwood with heavy pulley disc, 3s
- [x] **n_body_1d_collisions** — 7-ball elastic chain on frictionless floor, 2s
- [x] **block_on_accelerating_wedge** — frictionless wedge + sliding block, COM fixed, 1.5s
- [x] **pendulum_with_lateral_spring** — swing/spring energy exchange, 12s
- [x] **hanging_slinky_drop** — slinky bottom lags on release, 1.5s
- [x] **standing_wave_on_string** — fundamental-mode standing wave, 4s
- [x] **belt_friction** — coupled pulleys with visual belt, 4s
- [x] **block_on_block_static_friction** — stacked blocks, bottom launched at 1 m/s, 2s
- [x] **tumbling_book** — intermediate-axis flip in zero-g, 5s
- [x] **swinging_chain_pendulum** — flexible chain pendulum with whip, 5s
- [x] **bead_in_rotating_ring** — bead equilibrium in spinning ring, 4s
- [x] **block_and_tackle** — 2:1 pulley mechanical advantage, 3s
- [x] **cantilever_load_curve** — horizontal beam tip deflection under load, 3s
- [x] **symmetry_breaking_ball_on_dome** — unstable apex ball slides off dome, 2s

All mp4s in `out/new_scenes/`. **Showreel:** `out/new_scenes/all_d_scenes_grid.mp4` (5×4 grid, 5 s per cell — regenerate with `python make_showreel_d.py`).

Generators: `gen_hanging_slinky_drop.py`, `gen_rolling_chain.py`, `gen_standing_wave_on_string.py`, `gen_swinging_chain_pendulum.py`, `gen_cantilever_load_curve.py`, `gen_cycloidal_pendulum_huygens.py`, `gen_block_on_block_static_friction.py`, `gen_symmetry_breaking_ball_on_dome.py`.

## Tasks incomplete or blocked

(none)

## New gotchas hit (worth adding to docs/gotchas.md)

### PowerShell splits negative `--init-qpos` values

**What happened:** `render.py --init-qpos "-0.35,0,..."` failed with "expected one argument" because PowerShell treats `-0.35` as a separate flag.

**Why:** argparse on Windows PowerShell interprets tokens starting with `-` as flags even inside quotes in some invocation patterns.

**Fix / how to apply:** Use equals form: `--init-qpos=-0.35,0,...` or `--init-qpos "-0.35,0,..."` with explicit `--` separator before args.

## New scene ideas worth adding to BACKLOG

(none this round)

## Anything else (questions, comments, blockers)

- Re-rendered 2026-05-24: fixed `rolling_chain` physics (slide driver + idler roller + sustained pull) and auto-framed all 17 cameras via `gen_render_all_d.py` (motion-bounds centering + fovy widen).
- `cycloidal_pendulum_huygens` uses visual cycloid cheeks + standard hinge pendulum; full tendon-wrap isochrony would need cheek wrap geoms in the spatial tendon path.
- `standing_wave_on_string` may emit a brief QACC warning early in sim but produces a readable standing-wave clip.
- Renders at 1280×720; re-run `python scenes/gen_render_all_d.py` from repo root to regenerate all mp4s with updated cameras.


---

## Return: `my_return_f_2026-05-24.tar.gz` merged at 2026-05-25T00:36

# Return from F

(Fill this in before sending the package back. Keep the headings — the master
keeper greps for them.)

**Your name:** F
**Round date (received):** 2026-05-24
**Return date:** 2026-05-24

---

## Tasks completed

List each scene you finished. For each, give a 1-line description and the
duration you rendered.

- [x] galileo_pendulum_peg — Pendulum with peg wrap via stiff spatial tendon, 3s
- [x] horizontal_vs_dropped_balls — Two balls same height, one kicked horizontally, land together, 0.6s
- [x] chain_jet_classic — Chain pile in beaker, top link kicked upward (vz=2), 3.5s
- [x] rolling_disc_inscribes_cycloid — Rolling disc, rim marker traces cycloid, 4s
- [x] bucket_of_water_overhead_swing — Rigid arm + bucket, ball inside vertical circle ω=4, 3s
- [x] two_marbles_curved_track_collision — U-parabolic track, two marbles elastic collision, 4s
- [x] planetary_gear_train — Sun + 3 planets on carrier, joint equalities, 3s
- [x] gear_train_2_gears — Two gears coupled 0.6 ratio, sun ω=5, 3s
- [x] four_bar_linkage — Grashof four-bar, crank driven ω=4, 4s
- [x] ratchet_pawl — Toothed wheel + spring pawl, forward ω=3, 3s
- [x] chain_unspooling_from_pile — Loose chain pile, top link elevated, 3.5s
- [x] triple_block_friction_chain — Three stacked blocks, bottom vx=2, 2.5s
- [x] chain_on_scale_falling — Vertical chain drops onto scale plate, 2s
- [x] two_bodies_on_incline_string — Incline blocks different μ, tendon + equality, 3s
- [x] double_atwood — Nested Atwood (3 masses), 3.5s
- [x] galileo_inclined_plane_squared — Ball on low-friction ramp, d∝t² markers, 4s
- [x] rolling_dumbbell — Two spheres on rod tumble on floor, 4s

## Tasks incomplete or blocked

None — all 17 assigned scenes have XML + mp4 in `out/new_scenes/`.

Note: chain_jet_classic / chain_unspooling_from_pile are simplified pile models;
physics is qualitative (many free links).

**2026-05-24 optimization pass:** Re-tuned all 17 scenes for in-frame cameras
(side-view: camera on +y axis looking at xz motion; top-down: gears/ratchet),
fixed physics outliers (hinge pendulum for galileo_pendulum_peg, stacked free
bodies for triple_block, compact chain stack for chain_on_scale, +x downhill
ramp for galileo_inclined, sphere rolling for cycloid disc). All mp4/grid
re-rendered.

## New gotchas hit (worth adding to docs/gotchas.md)

### freejoint only on top-level bodies

**What happened:** `bucket_of_water_overhead_swing` failed to load with
`free joint can only be used on top level` when the ball was nested inside
the bucket body.

**Why:** MuJoCo schema restriction for free joints.

**Fix / how to apply:** Use a `ball` joint (or slide) for a mass moving inside
a parent body, not `freejoint`.

### Windows: pass relative XML paths to MuJoCo from subprocess

**What happened:** Batch rendering via subprocess with absolute paths containing
Chinese directory names (`3D场景开发`) caused `ParseXML: Error opening file`.

**Why:** Encoding / path handling in child processes on Windows.

**Fix / how to apply:** `os.chdir` to the project root and pass paths like
`scenes/foo.xml` only.

## New scene ideas worth adding to BACKLOG

(Delete the section entirely if you hit none.)

## Anything else (questions, comments, blockers)

- Render environment: Python 3.12.6 + mujoco 3.8.1 (`E:\python\python3.12.6\python.exe`).
- Generator scripts: `gen_two_marbles_curved_track_collision.py`, `gen_chain_on_scale_falling.py`,
  `gen_ratchet_pawl.py`, `gen_chain_unspooling_from_pile.py`, `gen_chain_jet_classic.py`.
- Grid PNGs in `out/*_grid.png` for verification (not in return tarball requirement but present locally).
