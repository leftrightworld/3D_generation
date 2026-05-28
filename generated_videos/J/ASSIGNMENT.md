# Assignment for J

**Round:** 2026-05-25

## Your tasks this round

### Task 1 — `double_pendulum_chaos_compare`

#### `double_pendulum_chaos_compare` — Chaos / butterfly effect

**Physics:** Two double pendulums with initial conditions differing by only ε = 0.01° exhibit exponential divergence of trajectories — a hallmark of deterministic chaos and sensitive dependence on initial conditions.
**Setup:** Two identical double pendulums (each link L = 0.3 m, M = 0.1 kg) placed side by side in the xz-plane, x-separated by 0.4 m. Both start from θ₁ = 60°, θ₂ = 0°; the second pendulum's θ₁ is offset by +0.01° = 0.000175 rad. No damping.
**Motion:** render 8 s. For the first 2–3 s the two pendulums swing nearly identically. Around t ≈ 3–5 s the trajectories visibly diverge; by t = 8 s the two bobs are completely out of phase. Camera: front view, fovy = 45, pos (0, -1.2, 0.0).
**Template:** `double_pendulum.xml`. Duplicate the entire double-pendulum body tree, offset by x = 0.4 m. Adjust init-qpos for the second copy's first joint by +0.000175 rad.
**Hints:** Use `integrator="RK4"` and `timestep="0.001"` for accurate long-horizon integration. Keep gravity at default (9.81). Both pendulums must share the same world body but have completely independent joint trees. See gotchas.md §chaos — do NOT use `euler` integrator here; RK4 is required or divergence will be numerical artefact not physical chaos.

---

### Task 2 — `pendulum_full_rotation`

#### `pendulum_full_rotation` — Separatrix / rotation

**Physics:** A pendulum released with kinetic energy just above the separatrix energy E = 2mgL transitions from oscillation to continuous rotation; the separatrix is the unstable fixed point at θ = π (inverted position).
**Setup:** Single pendulum, L = 0.5 m, M = 0.1 kg, pivot fixed. init-qpos: θ = 0 (hanging). init-qvel: ω = 6.3 rad/s (just above ω_sep = √(4gL/L²·L) = √(4 × 9.81 / 0.5) ≈ 8.86 rad/s — recalculate: ω_sep = √(4g/L) = √(4×9.81/0.5) ≈ 8.86 rad/s. For L=0.5, ω_sep ≈ 8.86 rad/s; use ω = 9.0 rad/s to be safely above). No damping.
**Motion:** render 6 s. The pendulum sweeps through the bottom, continues past horizontal, passes through the top (θ = 180°) with non-zero speed, and completes full rotations. Camera: side view capturing the full circle.
**Template:** `pendulum.xml`. Set init-qvel on the hinge joint to 9.0. Ensure joint `range` is not clamped (remove range or set range = "-1e9 1e9"). Set `limited="false"` on the hinge.
**Hints:** Critical: remove joint angle limits or MuJoCo will clamp the rotation. ω_sep = √(4g/L); use ω = 1.015 × ω_sep for a clean rotation with a little headroom. If the pendulum just barely passes the top it will look like it "floats" — which is fine for separatrix illustration. See gotchas.md §joint_limits.

---

### Task 3 — `lissajous_2d_spring_mass`

#### `lissajous_2d_spring_mass` — Parametric curves

**Physics:** A mass on two perpendicular springs with incommensurable natural frequencies traces closed Lissajous figures in 2D. For ω_x : ω_z = 1 : 2 (achieved by k_z = 4 k_x), the trajectory is a figure-8 in the xz-plane.
**Setup:** Single bob (M = 0.1 kg) with two independent slide joints: one along x (stiffness k_x = 100 N/m, equilibrium x = 0) and one along z (stiffness k_z = 400 N/m, equilibrium z = 0). init-qpos: x = 0.05 m, z = 0. init-qvel: ẋ = 0, ż = 0 (starts from x-displaced rest). No damping.
**Motion:** render 10 s. The bob traces a clean figure-8 Lissajous pattern in the xz-plane. Camera: front view, orthographic recommended, fovy = 30, pos (0, -0.5, 0).
**Template:** `spring_mass.xml`. Replace the single slide joint with two orthogonal slide joints (axes "1 0 0" and "0 0 1"). Add spring stiffness via `<joint ... stiffness="100">` (x) and `<joint ... stiffness="400">` (z).
**Hints:** Use zero damping (`damping="0"`) for persistent Lissajous pattern. For k₁ : k₂ = 1 : 4 and starting from x-displacement only, the pattern is 1:2 (figure-8). Add a tracer geom (small sphere) or use the ball itself. The scene should run long enough (≥ 10 s) to show the closed curve traced multiple times. See gotchas.md §spring_stiffness.

---

### Task 4 — `duffing_double_well`

#### `duffing_double_well` — Nonlinear oscillator / chaos

**Physics:** A Duffing oscillator with two potential wells (W-shaped track) shows qualitatively different behaviour depending on total energy: low-energy trajectories are trapped in one well (quasi-linear), while high-energy trajectories hop between wells (nonlinear chaos territory).
**Setup:** W-shaped curved track: z(x) = a·x⁴ − b·x² with a = 10 m⁻³, b = 1 m⁻¹ (minima at x = ±0.22 m, z_min ≈ −0.025 m, barrier at x = 0, z = 0). Built from ~30 thin box segments approximating the curve, static. Two balls: Ball A (M = 0.1 kg) placed at x = 0.22 m with low init-qvel v = 0.2 m/s (stays in right well); Ball B at x = 0.22 m with v = 1.4 m/s (clears barrier and transitions).
**Motion:** render 6 s. Ball A oscillates back and forth in the right valley. Ball B has enough energy to cross the central barrier and hop between wells, showing the nonlinear dynamics.
**Template:** `brachistochrone.xml` (for curved track segment technique). gen_duffing_track.py generates ~30 box geoms approximating z = 10x⁴ − x² over x ∈ [−0.35, 0.35].
**Hints:** Track segments must be tangentially placed (each segment rotated to match the local slope angle = arctan(dz/dx)). Segment width ~0.015 m. Balls start at x = ±0.22 m. Both balls same y-position but separated in x so they don't collide. See gotchas.md §curved_track_segments.

---

### Task 5 — `pendulum_pivot_on_cart`

#### `pendulum_pivot_on_cart` — Coupled translational/rotational

**Physics:** A pendulum mounted on a freely sliding cart couples rotational and translational degrees of freedom. When the cart is given an impulse, kinetic energy transfers between cart translation and pendulum rotation — the system's COM moves at constant velocity.
**Setup:** Cart (M = 0.5 kg, box 0.15 × 0.05 × 0.03 m) on a frictionless slide joint along x. Pendulum (L = 0.5 m, M = 0.1 kg) hung from the cart's top via a hinge joint (y-axis). init-qvel: cart ẋ = 1.5 m/s, pendulum ω = 0. No friction on slide joint (frictionloss = 0, damping = 0).
**Motion:** render 8 s. Cart slides right, pendulum swings behind it (reaction). Energy oscillates between cart KE and pendulum KE+PE; the cart accelerates and decelerates as the pendulum swings. COM of the whole system drifts at constant vx.
**Template:** `pendulum.xml`. Add a slide joint (axis "1 0 0") to the world-to-cart connection, replacing the fixed mount. Cart body defined as parent of the pivot body.
**Hints:** The cart slide joint must have `frictionloss="0"` and `damping="0"` or energy will not be conserved. The system has 2 DOF: cart x and pendulum angle θ. Total linear momentum is conserved. Camera: wide side view (fovy = 50) to capture cart travel. See gotchas.md §chained_joints.

---

### Task 6 — `foucault_pendulum_turntable`

#### `foucault_pendulum_turntable` — Rotating frame / Coriolis

**Physics:** A pendulum mounted on a slowly rotating horizontal platform precesses its swing plane in the lab frame due to the Coriolis effect — analogous to Earth's rotation causing real Foucault pendulum precession.
**Setup:** Platform disk (M = 1 kg, R = 0.15 m, thickness 0.01 m) connected to the world via a hinge joint about z with init-qvel ω_plat = 0.3 rad/s. Pendulum pivot attached to the platform surface; pendulum L = 0.4 m, M = 0.1 kg, hanging from platform. init-qvel: pendulum ω = 2 rad/s about the platform-frame x-axis.
**Motion:** render 15 s. In the lab frame, the pendulum swing plane slowly rotates as the platform turns. Observe at least 1–2 full platform rotations and the corresponding swing-plane rotation. Camera: top-down, pos (0, 0, 0.8), fovy = 50.
**Template:** `conical_pendulum.xml`. Replace the fixed pivot with a platform body having a z-hinge joint. Pendulum body parented to platform.
**Hints:** Platform rotation must be frictionless (damping = 0 on z-hinge) to sustain steady rotation. The pendulum swing damps naturally in MuJoCo due to joint damping — set damping = 0.001 (minimal). Use 15 s render to see clear precession. The turntable angular velocity ω_plat = 0.3 rad/s means one full rotation in ~21 s, so 15 s shows about 3/4 of a rotation. See gotchas.md §rotating_frames.

---

### Task 7 — `variable_length_pendulum`

#### `variable_length_pendulum` — Energy pumping / parametric

**Physics:** Parametric resonance: shortening a pendulum's effective length at the bottom of each swing (when the bob's KE is maximum) injects energy into the oscillation, causing amplitude to grow each cycle — the classic "pumping a swing" mechanism.
**Setup:** Single pendulum, base pivot fixed. A slide joint at the pivot allows the string length to vary between L_min = 0.3 m and L_max = 0.6 m. String shortens by Δ = 0.15 m each time the bob passes through θ = 0 (bottom), then re-extends at the top. Start: L = 0.6 m, θ = 30°, ω = 0.
**Motion:** render 10 s. Amplitude grows visibly over ~5–7 cycles. The bob swings with increasing arc. After 8–10 cycles the amplitude saturates near the joint limit.
**Template:** `pendulum.xml`. Add a slide joint at the pivot with range [−0.3, 0] (controls Δ-length). gen_variable_length_pendulum.py injects qpos commands for the slide joint each timestep based on sign of angular velocity (bottom of swing detection).
**Hints:** Parametric pumping requires precise timing: shorten at θ ≈ 0, extend at θ ≈ ±θ_max. Implement via `mj_step` callback in gen script. Slide joint stiffness = 0, damping = 0. The mass of the "string" should be negligible. See gotchas.md §programmatic_control.

---

### Task 8 — `euler_disk_spindown`

#### `euler_disk_spindown` — Precession / singularity

**Physics:** As a spinning coin loses energy to rolling friction, it paradoxically spins faster while tilting lower — a finite-time singularity where precession frequency diverges just before the coin abruptly stops, explained by Moffatt's rolling-friction theory.
**Setup:** Thin disc (cylinder, R = 0.05 m, thickness = 0.004 m, M = 0.05 kg) on a flat floor. Freejoint. init-qpos: tilt 3° from vertical (Euler angles). init-qvel: spin ω_z = 20 rad/s (about the disc's symmetry axis). Floor friction: `friction="0.3 0.005 0.001"` (rolling friction nonzero).
**Motion:** render 6 s. Disc initially spins steadily with mild precession. Over time, tilt angle increases and precession rate increases dramatically. Near t ≈ 5–6 s, the disc rattles with very fast precession and abruptly stops flat on the floor.
**Template:** `spinning_top.xml` (freejoint body + floor). Replace sphere/cone tip with a flat cylinder. Set freejoint initial conditions via `qpos` (position + quaternion) and `qvel` (linear + angular velocities).
**Hints:** The freejoint qvel order in MuJoCo is [vx, vy, vz, ωx, ωy, ωz]. The disc's spin axis is its local z (symmetry axis). init-qvel should be [0, 0, 0, 0, 0, 20]. Rolling friction `solimp` must allow realistic energy dissipation — use `solref="0.02 1"` and `solimp="0.9 0.95 0.001"`. See gotchas.md §freejoint_init and §rolling_friction.

---

### Task 9 — `kapitza_pendulum`

#### `kapitza_pendulum` — Parametric stabilization

**Physics:** An inverted pendulum becomes dynamically stable when its pivot is oscillated vertically at high frequency and sufficient amplitude — the Kapitza pendulum effect, where rapid oscillation creates an effective stabilizing potential.
**Setup:** Two side-by-side pendulums (L = 0.5 m, M = 0.1 kg), both inverted (hinge at bottom, rod pointing up). Pendulum A: pivot fixed, initial tilt 3° — falls. Pendulum B: pivot has a slide joint along z driven sinusoidally at A = 0.01 m, f = 20 Hz (ω_drive = 125.7 rad/s >> ω_0 = √(g/L) ≈ 4.4 rad/s) — stands stable. Both start at 3° tilt from vertical.
**Motion:** render 5 s. Pendulum A falls in ~0.5 s. Pendulum B oscillates about the inverted position, stabilized by the rapid pivot motion. Camera: front view.
**Template:** `pendulum.xml` (with gravity flipped for inverted mount, or simply start with rod pointing up from hinge). gen_kapitza.py provides the sinusoidal z-displacement by setting the slide joint qpos each step.
**Hints:** Kapitza stability condition: A·ω_drive > √2 · g·L (approximately). With A = 0.01, ω = 125.7: A·ω = 1.257 m/s. √2·g·L = √2·9.81·0.5 = 6.94 m/s — need to increase A or ω. Use A = 0.02 m, f = 50 Hz: A·ω ≈ 6.28 m/s (closer). Fine-tune in simulation. See gotchas.md §parametric_drive.

---

### Task 10 — `precession_nutation_full`

#### `precession_nutation_full` — Euler angles / gyroscope

**Physics:** A spinning top at a large nutation angle (40°) exhibits both slow precession (spin axis orbits the vertical) and superimposed nutation (wobbling of the spin axis up and down), demonstrating the full complexity of Euler angle dynamics beyond the small-angle limit.
**Setup:** Top (M = 0.3 kg, principal moments I_axial = 5×10⁻⁴ kg·m², I_transverse = 3×10⁻⁴ kg·m²) with a ball tip touching the floor. init-qpos: Euler angles giving θ = 40° nutation (tilt from vertical). init-qvel: spin ω_spin = 50 rad/s about the top's symmetry axis; precession and nutation rates initially zero (giving maximum nutation wobble).
**Motion:** render 6 s at least 2 full precession cycles. Observe: the spin axis sweeps a cone (precession) and simultaneously oscillates between two nutation angles (wobble). Camera: 3/4 view, pos (0.5, −0.5, 0.3), fovy = 40.
**Template:** `spinning_top.xml`. Adjust inertia tensor components via `<inertial diaginertia="...">`. Set nutation angle via quaternion in init-qpos: quat = [cos(θ/2), sin(θ/2), 0, 0] gives tilt θ about x.
**Hints:** With zero initial precession rate and θ = 40°, the top will nutate between 40° and a second nutation angle determined by energy/angular momentum conservation. Render long enough (6 s) to see ≥ 2 precession cycles. MuJoCo's freejoint or ball joint work; if using freejoint, set full 6-DOF initial conditions carefully. See gotchas.md §spinning_top_init.

---

### Task 11 — `coupled_gyroscopes_reaction`

#### `coupled_gyroscopes_reaction` — Gyroscopic coupling

**Physics:** Two co-spinning gyroscopes on parallel axles exert reaction torques that oppose frame tilting: tilting the shared frame causes both gyros to precess in opposite directions (or the same, depending on spin direction), creating a net reaction moment that resists the tilt.
**Setup:** Rigid frame body (L = 0.3 m bar) connected to world via hinge about x-axis. Gyro disc A (R = 0.05 m, M = 0.2 kg) on a hinge about y at position x = +0.10 m on the frame, init-qvel ω_A = +60 rad/s. Gyro disc B identical, at x = −0.10 m, init-qvel ω_B = +60 rad/s (same spin direction). Frame init-qpos: 20° tilt about x.
**Motion:** render 5 s. From the initial tilted position, both gyros precess and the frame exhibits a characteristic rocking/precessing motion driven by gyroscopic coupling. Camera: 3/4 view showing both discs and frame.
**Template:** `spinning_top.xml` (×2 disc bodies). Frame body with hinge (axis "1 0 0") to world. Each disc body parented to frame with hinge (axis "0 1 0"). High spin-rate init-qvel on each disc's y-hinge.
**Hints:** Both discs spinning in the same direction about y gives net angular momentum along y; tilting the frame about x will cause precession about z (perpendicular). The frame hinge about x must have low damping (0.001) to allow gyroscopic effects to dominate. With opposite spin directions, angular momenta cancel and no gyroscopic effect appears — use same direction for visible effect. See gotchas.md §gyroscopic_coupling.

---

### Task 12 — `newton_cradle_mass_gradient`

#### `newton_cradle_mass_gradient` — Momentum / mass mismatch

**Physics:** In a Newton's cradle with non-uniform ball masses, the simple one-in/one-out rule breaks down: the momentum and energy cannot be simultaneously conserved with a clean transfer, resulting in multiple balls moving after impact.
**Setup:** Five balls on strings (string length 0.3 m from pivot) at regulation spacing. Masses left to right: 0.05, 0.08, 0.12, 0.18, 0.25 kg. All same radius R = 0.02 m. Leftmost ball pulled to θ = 40° and released. Contact parameters: stiff (solref = "0.005 1", solimp = "0.99 0.999 0.001").
**Motion:** render 4 s. Leftmost ball strikes the row. Unlike the uniform cradle, the rightmost ball does NOT simply fly off alone — multiple balls on the right end move, with decreasing velocities. On return collisions the pattern continues to break classical expectations.
**Template:** `newton_cradle.xml`. Assign individual `<body ... mass="...">` or `<inertial mass="...">` values to each ball body. Keep geometry (R, string length, pivot spacing) uniform.
**Hints:** The mass gradient makes elastic collision analysis non-trivial. Use very stiff contacts to approximate ideal elastic collisions. Five balls means five equations but only two conservation laws — under-determined, so MuJoCo's contact model determines the actual outcome. Validate: leftmost ball (lightest) should bounce back slightly. See gotchas.md §newton_cradle_contacts.

---

### Task 13 — `pendulum_near_separatrix`

#### `pendulum_near_separatrix` — Phase space / critical energy

**Physics:** A pendulum given initial speed just below the separatrix energy asymptotes toward the inverted position (θ = π), slowing to near-zero speed at the top — a trajectory that theoretically takes infinite time to reach the unstable equilibrium point.
**Setup:** Single pendulum L = 0.5 m, M = 0.1 kg. init-qpos: θ = 0 (hanging). init-qvel: ω = 4.40 rad/s (99% of separatrix speed ω_sep = √(4g/L) = √(4×9.81/0.5) ≈ 8.86 rad/s — wait, recheck: ω_sep from energy: ½Iω² = 2mgL → ω² = 4mgL/I = 4mg·L/(mL²) = 4g/L → ω_sep = 2√(g/L) = 2√(9.81/0.5) ≈ 8.86 rad/s. Use ω = 0.99 × 8.86 = 8.77 rad/s). No damping.
**Motion:** render 12 s. Pendulum swings up quickly, then decelerates dramatically near θ = 180°, hanging near the top for several seconds before slowly swinging back down. Camera: side view, wide enough to show full arc.
**Template:** `pendulum.xml`. Set init-qvel = 8.77 on the hinge. Remove joint limits. Use `integrator="RK4"` for accurate near-separatrix integration.
**Hints:** At 99% separatrix energy the bob reaches θ ≈ 178° and hangs there for ~8–10 s (numerical precision determines exact hover time). Use RK4 with timestep = 0.0005 for accuracy. The scene illustrates phase-space concepts: the separatrix separates libration from rotation orbits. See gotchas.md §separatrix_integration.


## How to do this (5-step recipe)

1. Read **`CLAUDE.md`** end-to-end. It's short and tells you the workflow and
   conventions. If you're letting an AI agent do the heavy lifting, point it at
   `CLAUDE.md` first — that's what it's designed for.

2. For each task above:
   - Find a similar existing scene under `scenes/` and copy it as your
     starting point. **Never write from scratch.**
   - Adapt it to your physics. Match the visual style in
     `docs/style_guide.md` **verbatim** — same purple skybox, same cream
     floor, same warm wood, same camera framing rules.
   - Render + verify:
     ```
     python3 render.py    --scene scenes/<name>.xml --out out/scenes/<name>.mp4 --duration T
     python3 make_grid.py --scene scenes/<name>.xml --out out/dev/<name>_grid.png --duration T --cols 4 --rows 2
     ```
   - **OPEN the grid PNG** and confirm the physics looks right. Iterate
     parameters until it does (usually 2–5 iterations).

3. Fill in `RETURN.md` at the root of this folder — what you finished, what
   got stuck, any new gotchas you hit.

4. Tar up the entire folder and send it back:
   ```
   tar czf my_return_2026-05-25.tar.gz physics_video_gen/
   ```

## Hard rules — do not break these

- **Only ADD files in these locations:**
  - `scenes/*.xml`
  - `scenes/gen_*.py`
  - `out/scenes/*.mp4`
- **Do NOT modify** any other file. If you need to suggest changes to
  `BACKLOG.md`, `DIARY.md`, `docs/gotchas.md`, etc., write your suggestion
  in `RETURN.md` and the master keeper will merge it.
- **Do NOT swap your assigned scenes** for different ones. If a task is
  impossible, mark it incomplete in `RETURN.md` and explain why.
- **Visual style is non-negotiable.** Same skybox, floor, lights, wood
  tones, accent palette as existing scenes. If you're tempted to invent a
  new color, don't.

## Common pitfalls already documented

See `docs/gotchas.md` — 18 traps your predecessors hit. Reading it takes
5 minutes and will save you hours of debugging.
