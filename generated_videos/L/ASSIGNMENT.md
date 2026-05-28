# Assignment for L

**Round:** 2026-05-25

## Your tasks this round

### Task 1 — `bowling_10pin_full`

#### `bowling_10pin_full` — Multi-body collision

**Physics:** A bowling ball strike initiates a cascade of rigid-body collisions among 10 pins; the exact outcome depends sensitively on ball entry point and angle — perfect centre strike often leaves corner pins standing due to deflection geometry.
**Setup:** Standard 10-pin triangle: pins in 4-3-2-1 formation, spacing 0.305 m (pin centre to centre). Each pin: capsule R = 0.028 m, half-height 0.077 m, M = 1.5 kg. Ball: sphere R = 0.108 m, M = 7.0 kg. Ball positioned 2.0 m in front of the head pin, init-qvel: vx = 5 m/s (along alley axis), vy = 0, vz = 0. Floor static friction 0.3. Pin bases ~0 m from floor (pins stand on the lane).
**Motion:** render 4 s. Ball strikes the head pin, cascade collision ensues. All 10 pins scatter. Camera: front view, pos (0, −3, 0.5), fovy = 38, looking down the alley.
**Template:** `bowling.xml`. gen_bowling_10pin.py places all 10 pins at regulation triangle positions. Each pin is an independent body with freejoint (falls over when hit). Ball has freejoint. High contact stiffness for authentic pin action.
**Hints:** Regulation pin spacing: 0.305 m. Triangle row positions: row 1 at y=0 (1 pin), row 2 at y=0.305 (2 pins, x=±0.1525), row 3 at y=0.61 (3 pins, x=0,±0.305), row 4 at y=0.915 (4 pins, x=±0.1525, ±0.4575). Ball launch 2 m in front of head pin. See gotchas.md §bowling_pin_contacts.

---

### Task 2 — `bouncing_ball_cor_compare`

#### `bouncing_ball_cor_compare` — Coefficient of restitution comparison

**Physics:** The coefficient of restitution (CoR) determines what fraction of pre-collision normal velocity is retained after each bounce: h_n = CoR^(2n) × h_0. Different materials exhibit CoR from ~0.3 (clay) to ~0.95 (super ball).
**Setup:** Three identical balls (R = 0.03 m, M = 0.1 kg) dropped from z = 1.0 m, side by side at x = −0.3, 0, +0.3 m. Ball A (CoR ≈ 0.9): solref = "0.02 1", solimp = "0.99 0.999 0.001". Ball B (CoR ≈ 0.6): solref = "0.02 1", solimp = "0.80 0.90 0.001". Ball C (CoR ≈ 0.3): solref = "0.02 1", solimp = "0.50 0.60 0.001". Flat static floor.
**Motion:** render 5 s. All three balls dropped simultaneously. Ball A bounces high (h₁ ≈ 0.81 m), Ball B medium (h₁ ≈ 0.36 m), Ball C barely bounces (h₁ ≈ 0.09 m). After 5 s, A is still bouncing, C is nearly stationary.
**Template:** `coefficient_of_restitution.xml` (if present) or `bowling.xml`. Three ball bodies with individual geom-level solimp/solref. Verify CoR by measuring bounce heights in sim.
**Hints:** MuJoCo's `solimp` controls the effective CoR indirectly through the contact impedance model. Calibrate: drop a test ball and measure v_after/v_before from consecutive bounce heights. Typical tuning: solimp `d0` parameter near 0.99 gives near-elastic; near 0.5 gives highly inelastic. Stagger x by 0.3 m to prevent inter-ball interaction. See gotchas.md §coefficient_of_restitution_tuning.

---

### Task 3 — `sand_pile_avalanche`

#### `sand_pile_avalanche` — Granular / self-organized criticality

**Physics:** A sandpile at the angle of repose is in a state of self-organised criticality — adding a single grain can trigger an avalanche of any size. This scene demonstrates the threshold instability: a pile near repose + one perturbation = avalanche.
**Setup:** Initial conical pile: ~60 balls (R = 0.008 m, M = 0.001 kg each) arranged in a stable cone with slope angle ≈ 30° (just below repose for μ = 0.6). Cone height ≈ 0.06 m, base radius ≈ 0.10 m. Balls settled at t = 0 (via pre-simulation or direct placement). One extra ball (same specs) placed at the apex, z = z_top + 0.02 m, vx = 0.
**Motion:** render 3 s. Initial pile is stable. Extra ball lands on apex and triggers a cascade — several balls slide off one side, reorganising the pile into a lower-angle stable configuration.
**Template:** `rotating_fluid.xml` (granular pile technique). gen_sand_pile.py first builds the initial pile via simulation, then saves qpos as initial state. Extra ball added as a separate body. Friction: "0.6 0.005 0.001" for all balls and floor.
**Hints:** Building the initial pile at exactly the angle of repose requires careful friction tuning. Alternative: set friction lower (μ = 0.5), drop 60 balls, let settle, then add the extra ball — the existing slope will be below repose but the extra ball will still trigger local rearrangement. Add a reference line (thin static box) to mark the initial slope angle for visual comparison. See gotchas.md §pile_initialisation.

---

### Task 4 — `spinning_disc_floor_wobble`

#### `spinning_disc_floor_wobble` — Precessing coin / Euler disk

**Physics:** A coin spinning on a flat surface exhibits a characteristic wobble where both the tilt angle and the precession rate increase as energy is dissipated by rolling friction — the precession frequency scales as f ∝ 1/√ε where ε is the tilt angle, diverging in the limit.
**Setup:** Flat disc (cylinder R = 0.05 m, thickness = 0.004 m, M = 0.05 kg, freejoint) on flat floor. init-qpos: disc tilted 20° from vertical (quaternion computed for 20° tilt about x-axis). init-qvel: freejoint velocity [0, 0, 0, 0, 0, 30] (vx=vy=vz=0, ωx=ωy=0, ωz=30 rad/s — spin about disc symmetry axis). Floor friction: `friction="0.25 0.005 0.001"`.
**Motion:** render 6 s. Disc initially wobbles and precesses with a stable cycle. Over time, tilt angle increases and precession rate increases dramatically. Near the end, very fast rattling precession followed by abrupt stop (disc flat on floor).
**Template:** `spinning_top.xml`. Replace the conical/spherical tip with a flat cylinder. Use freejoint. This is distinct from `euler_disk_spindown` (Package J) — here the initial tilt is larger (20° vs 3°) so the early wobble phase is clearly visible and more visually prominent.
**Hints:** The tilt of 20° makes the initial wobble large enough to photograph clearly. Rolling friction coefficient `solref="0.02 1"` with small rolling component (`solimp` third parameter = 0.001) provides realistic energy dissipation timescale. Total simulation time 6 s is sufficient to show the full lifecycle. See gotchas.md §euler_disk.

---

### Task 5 — `rigid_body_3axis_stability`

#### `rigid_body_3axis_stability` — Intermediate-axis theorem / all three axes

**Physics:** Euler's intermediate-axis theorem (Dzhanibekov effect): rotation about the major (longest) and minor (shortest) principal axes is stable; rotation about the intermediate axis is unstable — any perturbation causes the body to flip periodically.
**Setup:** Zero gravity (gravity = "0 0 0"). Three identical box bodies (0.30 × 0.15 × 0.05 m, M = 0.3 kg) at x = −0.4, 0, +0.4 m. Box (a) at x = −0.4: init-qvel ωx = 5 rad/s (longest axis — stable). Box (b) at x = 0: init-qvel ωy = 5 rad/s (intermediate axis — UNSTABLE, will flip). Box (c) at x = +0.4: init-qvel ωz = 5 rad/s (shortest axis — stable). All bodies with freejoint.
**Motion:** render 5 s. Box (a) and (c) spin cleanly about their respective axes. Box (b) initially spins, then begins to flip (~t = 1–2 s), and flips repeatedly. Camera: 3/4 isometric view showing all three boxes simultaneously.
**Template:** `dzhanibekov_effect.xml`. This extends the existing scene by showing all three axes simultaneously. Three bodies with freejoint, gravity off. Principal moments: I_x = m(y²+z²)/12 = 0.3×(0.0225+0.0025)/12 = 0.000625, I_y = m(x²+z²)/12 = 0.3×(0.09+0.0025)/12 = 0.002313, I_z = m(x²+y²)/12 = 0.3×(0.09+0.0225)/12 = 0.002813 kg·m².
**Hints:** Intermediate axis is y (intermediate I_y). Box (b) must be given a tiny perturbation off the pure y-axis (e.g., ωx = 0.01 rad/s) to seed the instability and trigger the flip within the 5 s render. Without perturbation, numerical noise will eventually trigger it but timing is unpredictable. See gotchas.md §dzhanibekov.

---

### Task 6 — `billiard_trick_shot_curve`

#### `billiard_trick_shot_curve` — Spin / friction-induced curve

**Physics:** A ball rolling with sidespin curves due to friction: the contact friction force has a component perpendicular to the direction of motion, equal to μ_k × N × (ω_z × R / v) — the "Magnus-like" friction curve experienced in billiards as the cue ball develops English.
**Setup:** Cue ball (R = 0.028 m, M = 0.17 kg, freejoint) on a flat table (z = 0). init-qpos: z = R (resting on table). init-qvel: vx = 2.0 m/s (forward), vy = 0, vz = 0, ωx = 0, ωy = 0, ωz = 15 rad/s (sidespin — top view clockwise). Table friction: `friction="0.4 0.01 0.005"`.
**Motion:** render 3 s. Ball rolls forward, gradually curving to the right (for positive ωz). The path is a visibly curved arc, not a straight line. Camera: top-down view, pos (0, 0, 0.8), fovy = 45.
**Template:** `marble.xml` + `incline_friction.xml` (friction model). Freejoint ball on flat floor (extend floor to 2 m × 2 m). The table surface is a static box, no slope.
**Hints:** The curve radius depends on friction: R_curve = v²/(μ × g × ω_z × R / v) ≈ v³/(μ × g × R × ω_z). With the given values: R_curve ≈ 8/0.4/9.81/0.028/15 ≈ 0.49 m — a tight curve. Use `solref="0.02 1"` for the contact. The ball will also experience rolling-without-slip transition (initially sliding, then rolling), which adds complexity. Top-down camera essential for visibility. See gotchas.md §spin_friction_curve.

---

### Task 7 — `projectile_range_angle_sweep`

#### `projectile_range_angle_sweep` — Projectile / optimal angle

**Physics:** For a projectile launched at speed v, range R(θ) = v²sin(2θ)/g — maximum at 45°, with complementary pairs (30° and 60°, 15° and 75°) giving equal range. This scene visualises the full angular sweep simultaneously.
**Setup:** Five balls (R = 0.015 m, M = 0.05 kg each, freejoint) launched from the same point (x = 0, z = 0.015). Launch speed v = 4 m/s. Launch angles: θ = 15°, 30°, 45°, 60°, 75° from horizontal. init-qvel for each: vx = 4cos(θ), vz = 4sin(θ), vy = 0. Floor is a long flat surface (5 m × 0.5 m). No air resistance.
**Motion:** render 2 s. Five balls fan out simultaneously, tracing five parabolic arcs. The 45° ball goes furthest (R = 1.63 m). The 30° and 60° balls land at equal range (R = 1.41 m). The 15° and 75° balls land closer (R = 0.82 m). Camera: side view, fovy = 50, wide enough to show all landing points.
**Template:** `projectile_jenga.xml`. Five freejoint ball bodies with individual init-qvel. Long static floor box (5 × 0.02 × 0.5 m). Side-view camera.
**Hints:** Predicted ranges: R(θ) = v²sin(2θ)/g = 16sin(2θ)/9.81. Confirm numerical results match theory. Separate balls in y by 0.05 m to avoid inter-ball collisions. Use thin markers (small static boxes) at predicted landing spots for educational value. Render time 2 s = slightly more than the longest flight time (t_45 = v sin(45°)/g × 2 = 0.58 s). See gotchas.md §projectile_setup.

---

### Task 8 — `chain_whip_crack_tip`

#### `chain_whip_crack_tip` — Whip / velocity amplification

**Physics:** In a whip, momentum is conserved as wave energy travels from a heavy base to a lighter tip — with decreasing mass per unit length, the wave speed increases and tip velocity can exceed the initial handle velocity by a factor of ~10.
**Setup:** 20-link chain with decreasing link masses. Link i (i = 1 to 20) has mass m_i = 0.02 × (21 − i) / 20 kg (linear gradient: link 1 = 0.020 kg, link 20 = 0.001 kg). All links: box 0.015 × 0.015 × 0.03 m (length scales with mass for constant density). Links connected by hinge joints (y-axis). Link 1 (base) given init-qvel vx = 3 m/s. All other links initially at rest. No gravity (or include gravity for a more realistic droop effect — include it for realism).
**Motion:** render 1.5 s. The velocity impulse propagates from the heavy base toward the light tip. The tip's speed at impact can be estimated as v_tip ≈ v_base × (m_base/m_tip)^(1/2) ≈ 3 × √20 ≈ 13 m/s. Camera: side view capturing the full chain length.
**Template:** `dominoes.xml` (chain of bodies). gen_whip_chain.py constructs the 20 links with decreasing masses. Hinge joints with low damping. init-qvel on link 0 body only.
**Hints:** Use low joint damping (0.001) to preserve the wave amplification. The velocity amplification formula (impedance mismatch model) gives v_tip/v_base ≈ √(m_1/m_N) for ideal chain — numerical result will be lower due to damping and bending losses. If gravity is included, orient the chain horizontally (along x) with init-qpos so all links start in-line. See gotchas.md §chain_wave_propagation.

---

### Task 9 — `elastic_wave_2d_grid_pulse`

#### `elastic_wave_2d_grid_pulse` — 2D wave propagation

**Physics:** A 2D mass-spring grid with fixed boundaries supports circular wave fronts after a central impulse; the wave speed is isotropic in the limit of small spacing and the circular ripple expands at v = Δx × √(k/m).
**Setup:** 7×7 grid of masses (M = 0.005 kg each) on slide joints (z-axis only) with spacing 0.03 m in x and y. Adjacent masses connected by stiff springs (k = 500 N/m, implemented as hinge stiffness or actuator springs). Edge masses (border of the 7×7 grid) have their slide joint fixed to world (range = "0 0"). Central mass (position [3,3]) given init-qvel vz = 0.5 m/s. No gravity (gravity = "0 0 0" to isolate wave from sag).
**Motion:** render 3 s. A circular ripple radiates outward from the central mass, reflects off the fixed boundaries, and creates interference patterns. Camera: top-down, pos (0, 0, 0.5), fovy = 45 (looking straight down), showing all 49 masses.
**Template:** `gen_pendulum_waves.py` (adapted for 2D grid). gen_elastic_grid.py creates 49 bodies, 2×(7×6) spring connections (horizontal and vertical), fixed edge joints. Slide joints along z only. Springs between adjacent bodies use actuator (position spring) or joint stiffness.
**Hints:** Wave speed v = 0.03 × √(500/0.005) = 0.03 × 316 = 9.5 m/s → wave crosses 7×0.03 = 0.21 m in 0.022 s. The wave will traverse the grid many times in 3 s, creating complex standing-wave patterns. This is the main visual payoff: concentric ripples + reflection interference. See gotchas.md §2d_spring_grid.

---

### Task 10 — `multi_ball_chain_different_mass`

#### `multi_ball_chain_different_mass` — Momentum / mass gradient collision

**Physics:** Newton's cradle with non-uniform masses violates the simple elastic transfer rule; the momentum wave couples into multiple outgoing velocities determined by the full N-body elastic collision equations, showing mass mismatch effects on momentum transport.
**Setup:** Five hanging balls with masses 0.05, 0.10, 0.15, 0.20, 0.25 kg left to right (all R = 0.020 m, uniform geometry). A 6th ball (M = 0.05 kg, same geometry) swings in from the left at v = 2 m/s (init-qvel on its hinge). All balls suspended on strings (length 0.25 m) from a common ceiling bar, spacing 0.042 m (just touching at rest).
**Motion:** render 3 s. Incoming light ball (6th) strikes the left end of the chain. Unlike a uniform cradle, the momentum wave does not cleanly transfer to the rightmost ball — multiple balls on the right end move with different velocities. Observe which ball(s) emerge fastest.
**Template:** `newton_cradle.xml` + `elastic_collision.xml`. Six ball bodies on hinge-joint strings. Individual mass values. Stiff contact parameters. Side view.
**Hints:** Theoretical prediction for elastic collision of mass m₁ striking stationary m₂: v₂' = 2m₁v₁/(m₁+m₂) — but in a chain it's more complex. The lightest incoming ball (0.05 kg) hitting the 0.05 kg ball should initially have near-elastic transfer to that ball. Increasing masses to the right will show progressive slowing of the momentum wave. See gotchas.md §mass_gradient_cradle.

---

### Task 11 — `tipping_block_thin_wide_compare`

#### `tipping_block_thin_wide_compare` — Statics / tipping criterion

**Physics:** A block tips if its centre of mass projects outside its base before the block slides; tip-vs-slide depends on aspect ratio: wide blocks slide (low COM projection overhang needed), tall blocks tip (high torque, easy COM overhang). Critical angle for tipping: θ_tip = arctan(w/(2h)).
**Setup:** Three blocks of equal mass M = 0.5 kg on a ramp, static friction μ = 0.3 for all. Block A (wide): 0.20 × 0.04 × 0.08 m (w × d × h), θ_tip = arctan(0.10/0.04) = 68° — much more than θ_slide = arctan(0.3) = 17°: slides. Block B (square base): 0.08 × 0.04 × 0.08 m, θ_tip = arctan(0.04/0.04) = 45° > 17°: marginal but slides first. Block C (tall): 0.04 × 0.04 × 0.20 m, θ_tip = arctan(0.02/0.10) = 11° < 17°: tips before sliding.
**Motion:** render 3 s. Ramp init-qvel tilts at 3 rad/s. Block C tips first (~t ≈ 0.7 s). Block A slides from the start. Camera: side view showing all three blocks.
**Template:** `incline_friction.xml` + `tipping_vs_sliding.xml`. Three block bodies on a hinge-joint ramp. Individual block dimensions and inertial properties. Same μ = 0.3 floor friction.
**Hints:** Recalculate θ_tip for each block: arctan(half-base-width / half-height). Ensure block dimensions give clearly distinct outcomes. The ramp tilt rate 3 rad/s = reaching 17° in ~0.1 s (very fast) — reduce to 0.5 rad/s for a clearer visual. Check: a ramp hinge joint with init-qvel OR use a motor actuator ramping angle. See gotchas.md §tipping_vs_sliding.

---

### Task 12 — `pendulum_wave_decay_pattern`

#### `pendulum_wave_decay_pattern` — Coupled waves / damping asymmetry

**Physics:** A pendulum wave machine with heterogeneous damping exhibits asymmetric pattern decay: heavily-damped pendulums on one side lose their oscillations quickly, while lightly-damped ones persist, creating a travelling degradation of the wave pattern.
**Setup:** 15 pendulums (L from 0.28 to 0.42 m tuned for 10 oscillations per pattern period on the right end). Each pendulum on a hinge joint. Damping gradient: pendulums 1–5 (left): `damping="0.5"`, pendulums 6–10 (middle): `damping="0.1"`, pendulums 11–15 (right): `damping="0.01"`. All released simultaneously from 15° amplitude.
**Motion:** render 15 s. Initial wave pattern forms as in `pendulum_waves.xml`. After ~5 s, the left side (heavy damping) pendulums lose amplitude; the pattern degrades from the left, creating an asymmetric visual — the right side still waves while the left side is nearly still.
**Template:** `pendulum_waves.xml`. Apply a damping gradient over the 15 hinge joints. No other changes. Side view or slight 3/4 view to see the wave pattern.
**Hints:** 15 pendulums with lengths tuned for the wave pattern: L_i = g/(2π × f_i)² where f_i varies from f_1 to f_15 to give 9 to 10 oscillations per 15 s pattern period. Heavy damping γ = 0.5 means amplitude halves in ~2 s (e-folding time = 1/γ = 2 s). Light damping γ = 0.01 means amplitude barely changes over 15 s. See gotchas.md §pendulum_wave_tuning.


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
