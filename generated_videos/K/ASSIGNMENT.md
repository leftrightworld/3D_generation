# Assignment for K

**Round:** 2026-05-25

## Your tasks this round

### Task 1 — `spring_gun_launch`

#### `spring_gun_launch` — Elastic PE → KE

**Physics:** A compressed spring stores elastic potential energy E = ½kx²; upon release, all stored energy converts to kinetic energy of a launched projectile (minus losses), and maximum height is h = E/(mg).
**Setup:** Spring mechanism: a hinge joint with stiffness k = 5000 N/m acts as the launch spring. Ball (M = 0.05 kg, R = 0.015 m) sits in a cup on the spring arm. init-qpos: spring compressed by x = 0.03 m (stored PE = ½ × 5000 × 0.03² = 2.25 J). At t = 0 the ball is released from the cup (unconstrained). Floor and walls absent to show clean ballistic arc.
**Motion:** render 1.5 s. Spring releases, flinging the ball upward. Ball follows a parabolic arc, reaching maximum height h = 2.25/(0.05×9.81) ≈ 4.6 m (adjust scale so this fits in frame — use k = 200 N/m for h ≈ 0.18 m with x = 0.03 m). Ball rises and falls.
**Template:** `spring_mass.xml`. Use a hinge joint (y-axis) with `stiffness="200"` as the launch mechanism. Ball body connected via an equality constraint (weld) that is disabled at t = 0, or simply use contact-based cup. Render with a moderately high camera.
**Hints:** Predicted max height h = kx²/(2mg) = 200×0.03²/(2×0.05×9.81) = 0.18 m — matches a clean 1.5 s scene. For a visually dramatic launch, use k = 2000 N/m and x = 0.04 m → h ≈ 3.3 m with appropriate camera. Weld equality constraint release: set `active="false"` in gen script at t = 0. See gotchas.md §equality_constraints.

---

### Task 2 — `toggle_clamp_overcenter`

#### `toggle_clamp_overcenter` — Mechanism / over-center locking

**Physics:** A toggle clamp passes through an over-center configuration where the three pivot points become collinear; at this singularity, the mechanical advantage is infinite and any output force cannot backdrive the mechanism — the basis for vice grips and industrial clamps.
**Setup:** Three-link planar mechanism: input arm (L = 0.10 m, M = 0.05 kg, hinge to world at origin, y-axis), coupler (L = 0.08 m, M = 0.03 kg, hinge between input arm tip and output stub base), output stub (L = 0.03 m, M = 0.02 kg, constrained to slide vertically via slide joint to world). init-qvel on input arm: ω = 1.5 rad/s (drives toward over-center). After over-center, apply a large downward force (F = 50 N) on the output platen via a `<actuator forcerange=...>` or body gravity.
**Motion:** render 4 s. Input arm rotates, passing over-center at ~t = 1 s. Output platen locks. Applied force after locking cannot move the mechanism — it remains locked. Camera: front view.
**Template:** `four_bar_linkage.xml`. Remove the fourth link; add a slide joint constraint for the output stub. Key: the over-center condition is when all three pivots (world hinge, coupler–input junction, coupler–output junction) are collinear.
**Hints:** Over-center condition: input arm angle + coupler angle = 180°. Detect in gen script and stop applying input velocity. For the lock test, add a downward external force as a body-level `<force>` after t = 1 s. Numerical stability near singularity: reduce timestep to 0.0005 around the over-center moment. See gotchas.md §mechanism_singularities.

---

### Task 3 — `maxwell_wheel_inertia_compare`

#### `maxwell_wheel_inertia_compare` — Rotational inertia / descent

**Physics:** For a Maxwell wheel (yo-yo descending on a string), angular acceleration α = g / (1 + I/(mR²)) — wheels with higher moment of inertia I descend slower. Three wheels with identical mass but different mass distributions illustrate the effect of I on acceleration.
**Setup:** Three Maxwell wheels side by side (x = −0.3, 0, +0.3 m), all M = 0.2 kg, axle R = 0.01 m, string length 0.4 m. (a) Hoop/rim-mass: I = mR_rim² with R_rim = 0.08 m → I ≈ 0.00128 kg·m². (b) Solid disc: I = ½mR² with R = 0.08 m → I ≈ 0.00064 kg·m². (c) Centre-mass (all mass at axle): I ≈ m·R_axle² → I ≈ 0.00002 kg·m². Strings attached to ceiling.
**Motion:** render 4 s. All three released simultaneously. Rim-mass wheel (a) descends slowest. Solid disc (b) intermediate. Centre-mass (c) descends fastest, almost in free fall.
**Template:** `maxwell_wheel.xml` (×3). Override `<inertial diaginertia="...">` for each wheel to set the desired I values. Ensure string (tendon) length and attachment points are identical for all three.
**Hints:** Use `<inertial mass="0.2" diaginertia="I I I">` override. Stagger x-positions. Predicted descent times: use energy conservation — (c) descends in t ≈ √(2h/g) ≈ 0.29 s, (a) in t ≈ √(2h(1 + I_a/(mR²))/g). Camera: front view. See gotchas.md §inertia_override.

---

### Task 4 — `flywheel_energy_storage`

#### `flywheel_energy_storage` — Rotational KE / energy transfer

**Physics:** A spinning flywheel stores rotational kinetic energy; when frictionally coupled to a second disc, angular momentum distributes between them according to conservation: ω_final = (I₁ω₁) / (I₁ + I₂).
**Setup:** Flywheel (M = 2 kg, R = 0.15 m, I₁ = ½ × 2 × 0.15² = 0.0225 kg·m², hinge joint y-axis) at x = −0.15 m, init-qvel ω₁ = 40 rad/s. Second disc (M = 0.5 kg, R = 0.10 m, I₂ = 0.0025 kg·m²) at x = +0.10 m, initially ω₂ = 0. At t = 2 s, a friction pad (separate body with high-friction contact) is pressed between the two discs' rim edges — real contact friction couples them.
**Motion:** render 5 s. For t < 2 s: flywheel spins fast, second disc stationary. After t = 2 s: friction coupling — flywheel slows, second disc accelerates. Final: both at ω_f = I₁ω₁/(I₁+I₂) ≈ 36 rad/s. Camera: side view.
**Template:** `maxwell_wheel.xml` (two-disc setup). Add a friction-pad body between the discs' rims, activated at t = 2 s via a slide joint (gen script pushes pad into contact). Pad geom: `friction="1.5 0.01 0.005"`.
**Hints:** The friction coupling is achieved by translating a rubber-pad body into contact with both disc rims simultaneously. Use gen script to set pad slide-joint qpos at t = 2 s. The energy lost to friction heat = ½(I₁I₂/(I₁+I₂)) × (ω₁−ω₂)² ≈ 6.8 J. See gotchas.md §friction_coupling.

---

### Task 5 — `bascule_bridge_opening`

#### `bascule_bridge_opening` — Mechanism / counterweight

**Physics:** A bascule bridge uses a counterweight to reduce the net torque required to lift the roadway; if the counterweight torque exceeds the roadway torque (counterweight side heavy), the bridge opens under gravity without external power.
**Setup:** Single plate (total mass distributed as: counterweight M_cw = 2 kg on the short arm L_cw = 0.2 m from pivot, roadway M_road = 0.5 kg uniformly over L_road = 0.6 m, COM at 0.3 m from pivot). Hinge joint at the pivot (y-axis). init-qpos: 5° from horizontal (nearly flat, counterweight side slightly heavy). No actuator.
**Motion:** render 3 s. The counterweight side falls, the roadway side rises. Bridge swings from near-horizontal to near-vertical. Camera: side view, fovy = 50.
**Template:** `pendulum.xml` (hinge) adapted for an asymmetric plate. Model as a single box body with `<inertial>` specifying the asymmetric COM position (mass = 2.5 kg, COM at x_COM = (M_cw × (−0.2) + M_road × 0.3) / 2.5 from pivot). Alternatively, use two box geoms on either side of the hinge.
**Hints:** The net torque at 5° tilt must be confirmed to cause opening (counterweight torque > roadway torque accounting for cosine factors). Torque_cw = 2 × 9.81 × 0.2 × cos(5°) ≈ 3.91 N·m. Torque_road = 0.5 × 9.81 × 0.3 × cos(5°) ≈ 1.47 N·m. Net torque opens bridge. See gotchas.md §asymmetric_inertia.

---

### Task 6 — `domino_energy_amplification`

#### `domino_energy_amplification` — Chain reaction / energy amplification

**Physics:** In a chain of geometrically scaled dominoes, each falling domino has more potential energy than the one before it; the small initial push is amplified exponentially through the chain, demonstrating multiplicative energy transfer in mechanical cascades.
**Setup:** 12 dominoes with geometric scaling factor 1.5: heights h_i = 0.02 × 1.5^(i−1) m, widths w_i = h_i/5, thicknesses t_i = h_i/10, masses m_i = ρ × h_i × w_i × t_i (density ρ = 1500 kg/m³). Domino 1: h = 0.02 m, m ≈ 0.000024 kg. Domino 12: h ≈ 0.39 m, m ≈ 0.0089 kg. Spacing: domino i placed so domino i (when falling) just reaches domino i+1 top edge.
**Motion:** render 6 s. First domino pushed (init-qvel ω = 2 rad/s). Each subsequent domino topples with more energy. Final domino fall is dramatically larger. Camera: side view, wide angle.
**Template:** `dominoes.xml`. gen_domino_amplify.py computes positions and dimensions for each domino. Each domino is a separate body with box geom, hinge joint to the floor, correct inertial properties.
**Hints:** Spacing formula: d_i = h_i × sin(θ_fall) + t_{i+1}/2 where θ_fall ≈ 60° for typical aspect ratio. Total energy amplification: PE₁₂/PE₁ ≈ (1.5^11)² × m₁₂/m₁ ≈ 83. Domino sizes grow, so camera needs to adjust — use a dolly-zoom effect or very wide fovy = 70. See gotchas.md §domino_spacing.

---

### Task 7 — `hourglass_granular_flow`

#### `hourglass_granular_flow` — Granular flow / constant rate

**Physics:** In an hourglass, granular flow rate through the neck is roughly constant (independent of fill height for h >> neck radius) due to arching dynamics — unlike liquid flow (Torricelli's law) where rate decreases with height.
**Setup:** Two glass chambers (top: box 0.08 × 0.08 × 0.10 m; bottom: box 0.08 × 0.08 × 0.08 m) connected by a narrow neck (cylinder R = 0.006 m, length 0.02 m). Static glass geometry (no joints). 80 balls: R = 0.005 m, M = 0.002 kg, initially packed in the top chamber. Floor of top chamber is a funnel converging to the neck.
**Motion:** render 8 s. Balls flow one by one through the neck at a nearly constant rate. Top chamber empties, bottom chamber fills. Camera: front view with a cross-section cut showing internal flow.
**Template:** `rotating_fluid.xml` (container structure) + `marble.xml` (spherical balls). gen_hourglass.py constructs the glass geometry using box + cylinder geoms. Balls initialized using a grid pattern in the top chamber via gen script.
**Hints:** Neck radius must be > 2.5× ball radius for reliable flow (R_neck = 0.006, R_ball = 0.005 → barely 1.2× — increase to R_neck = 0.015). Ball packing in top chamber: use a grid with slight random jitter to avoid crystalline packing that blocks flow. Enable `solimp` settings that allow slight overlap for high ball counts. See gotchas.md §granular_packing and §neck_flow.

---

### Task 8 — `tensegrity_prism`

#### `tensegrity_prism` — Tensegrity / tension/compression

**Physics:** Tensegrity structures separate tension members (cables) from compression members (struts), with no bending moments at nodes; the triangular tensegrity prism remains rigid under load through this purely axial force distribution.
**Setup:** Triangular tensegrity prism: 3 compression struts (capsule geoms, L = 0.20 m, R = 0.008 m, M = 0.05 kg each) oriented at ~60° from vertical. 9 cables (tendons, stiffness k = 2000 N/m, rest length set so structure is in equilibrium). Top triangle (3 top nodes) + bottom triangle (3 bottom nodes), rotated 60° relative to each other. A load plate (M = 0.5 kg) rests on the top 3 nodes.
**Motion:** render 4 s. Load applied at t = 0 via the 0.5 kg plate. Structure compresses slightly and reaches static equilibrium. Camera: 3/4 isometric view showing all 6 nodes and 3 struts clearly.
**Template:** `atwood.xml` (tendons) + `block_overhang.xml` (rigid bodies). 6 node bodies (small spheres), 3 strut bodies (capsules), 9 tendons connecting nodes. All bodies have ball joints at nodes for the struts.
**Hints:** Tensegrity equilibrium requires precise tendon rest lengths and stiffness. Pre-compute the equilibrium geometry analytically: for a triangular prism with h = 0.15 m and triangle side s = 0.10 m, derive rest lengths of the 9 cables. Enable tendon damping = 2 to suppress vibration. See gotchas.md §tendon_equilibrium.

---

### Task 9 — `cam_follower_simple`

#### `cam_follower_simple` — Cam/follower mechanism

**Physics:** A rotating cam converts continuous rotational motion into oscillating translational motion; the follower displacement profile is determined entirely by the cam geometry — an elliptical cam gives a sinusoidal-like stroke.
**Setup:** Elliptical cam (modelled as an ellipsoid geom: a = 0.05 m, b = 0.03 m, along x and z in the cam's local frame) mounted on a hinge joint (y-axis) with init-qvel ω = 3 rad/s. A follower rod (box 0.01 × 0.01 × 0.08 m, M = 0.02 kg) on a slide joint (z-axis) rests on the cam surface under gravity. Cam and follower share a common xz-plane.
**Motion:** render 4 s (= 2 cam revolutions at ω = 3 rad/s). Follower moves up when the long axis of the ellipse comes around, down when the short axis is aligned. Stroke amplitude = a − b = 0.02 m. Camera: front view, fovy = 30.
**Template:** `gear_train_2_gears.xml` (hinge for cam rotation) + `spring_mass.xml` (slide joint for follower). Cam body: ellipsoid geom. Follower body: box geom with slide joint to world (z-axis). Follower rests on cam by gravity (no spring needed).
**Hints:** The follower must stay in contact with the cam — ensure follower mass (0.02 kg) provides enough contact force vs. cam acceleration. If contact is lost at high speed, add a light spring (k = 5 N/m) between follower and ceiling to maintain contact. Cam axle at z = 0.02 m above the floor; follower slide joint centred on same z-axis as cam. See gotchas.md §cam_contact_stability.

---

### Task 10 — `marble_run_multistage`

#### `marble_run_multistage` — Energy / multi-stage track

**Physics:** A marble run converts gravitational PE to KE on ramps, briefly stores KE as rotational energy on the helix, then delivers a collision to a target — demonstrating energy bookkeeping across multiple conversion stages.
**Setup:** Three-stage track: (1) Straight launch ramp, L = 0.5 m at 30° slope (height drop = 0.25 m). (2) Helical descent, 3 turns, helix radius R = 0.06 m, pitch 0.04 m/turn (total descent = 0.12 m, track length ~1.2 m). (3) Flat exit rail 0.2 m long leading to stationary target ball (M = 0.05 kg, R = 0.012 m). Marble: R = 0.010 m, M = 0.020 kg. Released from top of ramp.
**Motion:** render 5 s. Marble rolls down ramp, enters helix, spirals down, exits onto flat rail, and collides with target ball — which flies off. Camera: 3/4 isometric view capturing all three stages.
**Template:** `bead_on_helix.xml` (helix geometry) + `marble.xml` (ball) + `elastic_collision.xml` (target). gen_marble_run.py assembles all three track sections. Helix from `bead_on_helix.xml` gen script. Ramp and rail from box geoms.
**Hints:** Helix inner diameter must be > 2.5 × marble diameter (0.025 m vs. 0.02 m marble diameter — use R_helix = 0.06 m, tube inner R = 0.013 m). Marble transitions from ramp to helix: ensure smooth joint (chamfer the entry). At target collision, use stiff contacts for clean elastic bounce. See gotchas.md §helix_track and §track_transitions.

---

### Task 11 — `angle_of_repose_comparison`

#### `angle_of_repose_comparison` — Granular / friction

**Physics:** The angle of repose of a granular pile equals arctan(μ_effective) — higher inter-particle friction gives steeper stable slopes. Two piles of identical balls with different friction coefficients settle at measurably different angles.
**Setup:** Two separate piles built on the same flat floor, separated by 0.4 m in x. Pile A: 40 balls (R = 0.010 m, M = 0.004 kg each), contact friction "0.2 0.005 0.001". Pile B: 40 balls, same geometry, contact friction "0.7 0.005 0.001". Balls dropped from z = 0.3 m directly above each pile centre, released one every 0.05 s via gen script.
**Motion:** render 5 s. Pile A settles into a low, flat mound (angle ~11°). Pile B forms a steep cone (angle ~35°). Side-by-side comparison clearly shows different repose angles. Camera: side view, wide (fovy = 50).
**Template:** `rotating_fluid.xml` (granular container idea, but here no container — open floor). gen_angle_of_repose.py drops 40 balls at specified intervals. Ball geoms with individual friction properties via `<geom friction="...">`.
**Hints:** Assign friction on the ball geom directly, not the floor. Contact friction between two surfaces uses the minimum of their individual friction values by default in MuJoCo — set both ball geom friction AND floor friction to the desired value for Pile A vs. B. Stagger the drop sequence so piles build naturally. Render long enough (5 s) for full settling. See gotchas.md §contact_friction_model.

---

### Task 12 — `ball_in_toroidal_track`

#### `ball_in_toroidal_track` — Constrained circular motion

**Physics:** A ball constrained to roll inside a toroidal track converts gravitational PE to KE on descending segments, slows on ascending segments, and maintains circulation as long as minimum speed at the top is sufficient — analogous to a vertical loop but in a torus geometry.
**Setup:** Toroidal track: major radius R_t = 0.15 m (horizontal circle centre-to-centre), minor radius r = 0.018 m (tube inner radius). Track built from ~60 short curved box-segment tiles arranged in a torus (generated by gen_toroidal_track.py). Ball: R = 0.012 m, M = 0.010 kg. init-qvel: tangential v = 1.5 m/s along the torus tangent at the top of the torus cross-section (θ_minor = 90°, highest point).
**Motion:** render 5 s (≥ 2 full laps). Ball circulates around the torus, speeding up at the bottom of each minor arc and slowing at the top. Camera: 3/4 isometric top view to see the full torus, fovy = 45.
**Template:** `bead_on_helix.xml` (tube track geometry technique). gen_toroidal_track.py computes 60 segment positions and orientations around the torus. Each segment is a short box geom with appropriate position and rotation to approximate the inner torus surface.
**Hints:** Minimum speed for not losing track contact at the top of the minor circle: v_min = √(g·r) = √(9.81 × 0.018) ≈ 0.42 m/s. Launch at v = 1.5 m/s ensures multiple complete laps before slowing too much. Tube segments need chamfered edges to avoid ball catching on segment joints. See gotchas.md §tube_track_segments.

---

### Task 13 — `elastic_longitudinal_wave_chain`

#### `elastic_longitudinal_wave_chain` — Longitudinal waves

**Physics:** A compressive impulse in a 1D mass-spring chain propagates as a longitudinal (P-wave) at speed v = √(k/m) × Δx — distinct from transverse waves in existing scenes; the compressions and rarefactions travel along the chain axis.
**Setup:** 30 masses (M = 0.01 kg each, box 0.010 × 0.010 × 0.010 m) spaced at Δx = 0.02 m along the x-axis. Each connected to its neighbours by a hinge joint with stiffness k = 1000 N/m along the x-direction (slide joints, not hinges). All slide joints constrained to x-axis only. Mass 0 (leftmost) given init-qvel vx = 1.5 m/s. All other masses stationary. No gravity (gravity = "0 0 0").
**Motion:** render 2 s. A compression wave propagates from left to right. Observe individual masses oscillating longitudinally (along x) as the wave passes. Wave speed v_theory = √(k·Δx²/m) = √(1000×0.0004/0.01) = √40 ≈ 6.3 m/s → wave traverses 30 × 0.02 = 0.6 m in ~0.1 s. Camera: top-down view (pos (0, 0, 0.5), fovy = 60), showing all 30 masses from above.
**Template:** `dominoes.xml` (chain of bodies) + `spring_mass.xml` (stiffness values). Bodies connected by slide joints (axis "1 0 0"), gravity disabled. gen_longitudinal_wave.py sets up all 30 bodies and joints.
**Hints:** Wave speed v = Δx × √(k/m) = 0.02 × √(1000/0.01) = 0.02 × 316 = 6.3 m/s. Render 2 s shows the wave traverse the chain ~20 times — use timestep = 0.0001 for accurate wave propagation. Distinguished from transverse wave scenes by motion direction (along chain axis, not perpendicular). See gotchas.md §longitudinal_waves.


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
