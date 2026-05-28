# Assignment for M

**Round:** 2026-05-25

## Your tasks this round

### Task 1 — `spinning_top_sleep_to_fall`

#### `spinning_top_sleep_to_fall` — Top lifecycle

**Physics:** A spinning top's "sleeping" state (upright spin axis) is stable only above a critical spin rate ω_crit = 2√(MgℓI_transverse)/I_axial; as friction dissipates the spin, the sleeping state destabilises, nutation grows, and the top eventually falls.
**Setup:** Standard top (M = 0.3 kg, tip at origin, COM at ℓ = 0.03 m above tip, I_axial = 5×10⁻⁴ kg·m², I_transverse = 3×10⁻⁴ kg·m²). Freejoint with ball tip contacting floor. init-qpos: perfectly vertical (no tilt). init-qvel: spin ω = 80 rad/s about symmetry axis. Floor friction: `friction="0.15 0.002 0.001"` (low rolling friction to dissipate spin slowly over 8 s).
**Motion:** render 8 s. Phase 1 (t = 0–4 s): top spins stably upright (sleeping state). Phase 2 (t ≈ 4 s): nutation slowly appears as spin drops below ω_crit. Phase 3 (t = 4–7 s): precession and growing nutation. Phase 4 (t ≈ 7–8 s): rapid tumbling and fall.
**Template:** `spinning_top.xml`. Tune floor friction to give the desired spin-down timescale. ω_crit = 2√(MgℓI_t)/I_a = 2√(0.3×9.81×0.03×3×10⁻⁴)/(5×10⁻⁴) ≈ 25 rad/s.
**Hints:** The key challenge is getting the right friction coefficient so the spin decays from 80 to 25 rad/s in about 4 s. Rolling friction is the main dissipation mechanism for a top (sliding friction at the tip is zero for a perfectly upright top). Start with `friction="0.1 0.003 0.001"` and adjust third parameter (rolling). See gotchas.md §spinning_top_lifecycle.

---

### Task 2 — `gyroscope_resists_tipping`

#### `gyroscope_resists_tipping` — Gyroscopic stabilization

**Physics:** A fast-spinning gyroscope resists applied torques by precessing perpendicular to the applied force — a torque about the x-axis causes precession about the z-axis rather than tipping about x; this gyroscopic rigidity is the basis for gyro stabilizers and navigation instruments.
**Setup:** Gimbal frame (box 0.20 × 0.01 × 0.10 m, M = 0.1 kg) connected to world via hinge (x-axis). Gyro disc (R = 0.07 m, M = 0.3 kg, thickness 0.01 m) inside frame on a second hinge (y-axis). init-qvel: disc spin ω = 80 rad/s about y-axis. init-qpos: frame horizontal (0°). At t = 0.5 s, an impulsive force F = 5 N for 0.1 s applied to frame in z-direction (pushing it sideways).
**Motion:** render 5 s. Without spin: frame would simply tip and swing about the x-axis hinge. With spin (ω = 80): instead, frame precesses about z (rotates in the horizontal plane) — the gyro resists the tipping. Camera: 3/4 view, pos (0.4, −0.4, 0.3).
**Template:** `spinning_top.xml` + `conical_pendulum.xml` (gimbal structure). Frame body with hinge (x-axis) to world. Gyro disc body with hinge (y-axis) to frame. Apply the impulse force in the gen script using `mj_applyFT` at the specified time.
**Hints:** Precession rate Ω_p = τ/(I·ω) = F·r/(I·ω) = 5×0.1/(½×0.3×0.07²×80) ≈ 5×0.1/0.0588 ≈ 8.5 rad/s. This means the frame rotates ~4.25 rad in 0.5 s — clearly visible. The gyro effectively "stores" the applied torque as precession momentum. See gotchas.md §gyroscope_precession.

---

### Task 3 — `spinning_football_stabilized`

#### `spinning_football_stabilized` — Gyrostabilization / prolate body

**Physics:** A prolate body thrown without spin tumbles chaotically (Dzhanibekov instability about the intermediate axis); the same body thrown with a fast spin about its long axis becomes gyroscopically stable and maintains its orientation throughout the flight.
**Setup:** Two prolate ellipsoids (a = 0.11 m semi-major, b = c = 0.035 m semi-minor, M = 0.4 kg, freejoint) in free flight. Same translational launch: vx = 2.0 m/s, vz = 1.0 m/s (giving a parabolic arc over ~0.4 s). Ellipsoid A (no-spin): no rotational init-qvel. Ellipsoid B (spinning): init-qvel includes ωx = 30 rad/s (spin about symmetry axis). Both launched from z = 0.5 m, separated by y = 0.3 m.
**Motion:** render 2 s. Ellipsoid A tumbles chaotically. Ellipsoid B maintains its orientation with the nose pointing consistently along the velocity direction (or at a slight angle). Camera: side view, fovy = 45.
**Template:** `dzhanibekov_effect.xml` (freejoint + gravity). Replace box with ellipsoid geom (`type="ellipsoid" size="0.11 0.035 0.035"`). Include gravity (default). Two separate freejoint bodies.
**Hints:** For the spinning case, the gyroscopic stability condition: ω_spin > ω_tumble × √(I_transverse/I_axial). With ω_spin = 30 rad/s and typical tumble rate ~5 rad/s, this is well satisfied. The Dzhanibekov flip period for the non-spinning case (just translating, no spin) will be purely random/chaotic — add tiny initial angular velocity (ωy = 0.5 rad/s) to seed tumbling for ellipsoid A. See gotchas.md §gyrostabilization.

---

### Task 4 — `coin_edge_rolling_curve`

#### `coin_edge_rolling_curve` — Rolling / banking

**Physics:** A coin rolling along a curved track leans into the curve at a banking angle φ = arctan(v²/(gR_curve)) — the same angle a bicycle leans when cornering. Higher speed or tighter curve requires more lean.
**Setup:** Curved track: a 90° arc of radius R_curve = 0.5 m, track width 0.02 m, generated by gen_curved_track.py as ~20 box segments. Coin: cylinder R = 0.030 m, thickness = 0.003 m, M = 0.010 kg, freejoint. init-qpos: coin at the start of the curve, upright (zero tilt). init-qvel: tangential v = 1.0 m/s. Rolling-without-slip condition: ωy = v/R_coin = 33.3 rad/s. Contact friction: "0.5 0.01 0.005".
**Motion:** render 4 s. Coin enters the curved track, leans inward, and rolls through the curve maintaining upright balance (if v is sufficient). For v = 1.0 m/s: φ_theory = arctan(1²/(9.81×0.5)) = 11.5°. The coin exhibits this lean visibly. After the curve, coin rolls straight again.
**Template:** `marble.xml` + `bead_on_helix.xml`. gen_curved_track.py creates the curved track as ~20 short box segments in a 90° arc, each rotated appropriately. Coin has freejoint, initial spin set for rolling-without-slip.
**Hints:** The coin will likely wobble and possibly fall without the track providing lateral support — build the track as a narrow channel (two parallel rail strips) 0.025 m apart so the coin is guided. Initial spin must match rolling-without-slip or the coin will skid. See gotchas.md §coin_rolling_setup.

---

### Task 5 — `leaning_tower_mass_distribution`

#### `leaning_tower_mass_distribution` — Stability / COM height

**Physics:** A tower tips when its centre of mass projects outside its base; towers with higher COMs require less tilt to reach the tipping threshold. For a uniform tower, tipping angle θ_tip = arctan(w/(2h)); lowering the COM raises the tipping angle (more stable).
**Setup:** Three towers (each 0.10 × 0.10 × 0.5 m total, M = 0.5 kg) on a slow-tilting ramp. Tower A: uniform density, COM at h/2 = 0.25 m, θ_tip = arctan(0.05/0.25) = 11.3°. Tower B: heavy-bottom (COM at 0.10 m height, composite of 0.4 kg at bottom 0.1 m + 0.1 kg at top 0.4 m), θ_tip ≈ 27°. Tower C: heavy-top (COM at 0.40 m), θ_tip ≈ 7.1°. Ramp tilts at ω = 0.3 rad/s.
**Motion:** render 5 s. Ramp tilts gradually. Tower C tips first at ~7.1° (~t = 0.4 s). Tower A tips at ~11.3° (~t = 0.75 s). Tower B tips last at ~27° (~t = 1.5 s). Camera: side view showing all three towers and the ramp.
**Template:** `dominoes.xml` + `tipping_vs_sliding.xml`. Three tower bodies modelled as composite bodies (two box geoms with different densities) to achieve different COM heights. Ramp body with a hinge joint to world and init-qvel or motor.
**Hints:** Ensure tower bases have enough friction to prevent sliding before tipping: μ > tan(θ_tip) for tipping to occur before sliding. For Tower B: μ > tan(27°) = 0.51 — use μ = 0.7 for all. For Tower C: μ > tan(7.1°) = 0.12 — easily satisfied. Set ramp friction accordingly. See gotchas.md §composite_body_com.

---

### Task 6 — `trebuchet_simple`

#### `trebuchet_simple` — Projectile / mechanical advantage

**Physics:** A trebuchet converts the gravitational PE of a heavy counterweight into projectile KE via mechanical advantage from an unequal-arm lever; ideal efficiency gives projectile speed v_proj = v_cw × √(M_cw/m_proj) × (L_long/L_short).
**Setup:** Trebuchet arm (total length 0.75 m) pivoted at 0.15 m from the counterweight end. Counterweight: M_cw = 2 kg hanging at the short arm (L_short = 0.15 m). Sling: tendon length L_sling = 0.25 m connecting long arm tip to projectile. Projectile: M_proj = 0.05 kg, R = 0.015 m. init-qpos: counterweight up (arm horizontal, counterweight side high), sling hanging down with projectile resting in a cup.
**Motion:** render 2 s. Counterweight falls, arm rotates, sling whips the projectile upward and releases it (~t = 0.3 s). Projectile follows a high-speed ballistic arc. Camera: side view, wide fovy = 60 to capture full arc.
**Template:** `pendulum.xml` (arm pivot) + `atwood.xml` (counterweight and sling tendon). gen_trebuchet.py assembles the arm body (box geom), counterweight body on a tendon, and sling tendon with projectile. Arm hinge joint (y-axis) to world support frame.
**Hints:** Predicted projectile speed: v ≈ √(2 × M_cw × g × L_short) × L_long/L_short / √m_proj = √(2×2×9.81×0.15) × 0.60/0.15 / √0.05 ≈ √5.886 × 4/0.224 ≈ 105 m/s (unrealistically high for this scale — reduce M_cw to 0.3 kg for v ≈ 13 m/s). The sling release is implemented when the sling attachment angle triggers automatic detach (sling tip exceeds a threshold angle). See gotchas.md §sling_release.

---

### Task 7 — `ball_in_rotating_bowl_spiral`

#### `ball_in_rotating_bowl_spiral` — Rotating frame / equilibrium radius

**Physics:** In a parabolic bowl rotating at angular velocity ω, a ball finds a stable circular orbit at radius r_eq where the centrifugal "force" mω²r balances the bowl's restoring slope force mg × dz/dr = mg × 2ar; equilibrium at r_eq = √(g/(2aω²)).
**Setup:** Parabolic bowl z = 5r² (a = 5 m⁻¹) rotating at ω = 6 rad/s about its vertical axis. Bowl built from ~40 box segments arranged in a paraboloid pattern (gen_rotating_bowl.py). Ball: R = 0.015 m, M = 0.050 kg, freejoint. init-qpos: ball at r = 0.12 m from bowl axis, z = 5×0.12² = 0.072 m on the bowl surface. init-qvel: bowl-frame tangential velocity for co-rotation at r = 0.12 m.
**Motion:** render 6 s. Ball starts at r = 0.12 m (above equilibrium) and spirals inward (or outward if friction > centrifugal). Equilibrium r_eq = √(9.81/(2×5×36)) = √(9.81/360) ≈ 0.165 m → ball is at r = 0.12 < r_eq, so it should spiral outward toward equilibrium. Camera: 3/4 isometric top view.
**Template:** `rotating_fluid.xml`. Replace fluid content with a single ball. Bowl geom from gen_rotating_bowl.py. Bowl body has a hinge joint (z-axis) with `velocity="6"` motor or init-qvel.
**Hints:** r_eq = √(g/(2aω²)) = √(9.81/(2×5×36)) = 0.165 m. Start ball at r = 0.12 m (inside r_eq) — it should spiral outward. Start at r = 0.20 m — it spirals inward. Use a motorised bowl hinge with velocity control to maintain constant ω despite ball reaction forces. See gotchas.md §rotating_bowl_equilibrium.

---

### Task 8 — `double_pendulum_mode_shapes`

#### `double_pendulum_mode_shapes` — Normal modes / eigenfrequencies

**Physics:** A linearised double pendulum has two normal modes: symmetric (both links swing in phase at ω₋ — lower frequency) and antisymmetric (links out of phase at ω₊ — higher frequency); pure mode initial conditions give periodic (non-chaotic) motion.
**Setup:** Double pendulum: L₁ = L₂ = 0.3 m, M₁ = M₂ = 0.1 kg. Normal mode frequencies (equal masses and lengths): ω₋ = √(g(2−√2)/L) = √(9.81×0.586/0.3) ≈ 4.38 rad/s; ω₊ = √(g(2+√2)/L) ≈ 11.55 rad/s. Two side-by-side renderings: (a) Symmetric: θ₁ = θ₂ = 20°, angular velocities from eigenmode. (b) Antisymmetric: θ₁ = 20°, θ₂ = −20°. Both small-angle to validate linear modes.
**Motion:** render 5 s. (a) both links swing together at ω₋ — slower, synchronized. (b) links swing against each other at ω₊ — faster, opposing. Camera: front view, wide enough to see both pendulums side by side.
**Template:** `double_pendulum.xml`. Two copies side by side (x-offset 0.4 m). Set init-qpos for each copy to the respective mode shape (θ₁, θ₂ pairs). Use small angles (20°) to stay in linear regime.
**Hints:** Symmetric mode period T₋ = 2π/ω₋ ≈ 1.43 s. Antisymmetric mode period T₊ = 2π/ω₊ ≈ 0.54 s. In a 5 s render: symmetric completes ~3.5 cycles, antisymmetric ~9 cycles. The ratio of periods (2.6:1) is visually striking. Keep angles small (≤ 20°) to maintain pure mode shape. Use `integrator="RK4"` for accuracy. See gotchas.md §normal_modes.

---

### Task 9 — `inverted_pendulum_cart_balance`

#### `inverted_pendulum_cart_balance` — Instability / coupled motion

**Physics:** An inverted pendulum on a free cart is unstable but the cart's reactive motion creates a brief delay in the fall — the cart accelerates in the direction of the falling rod, reducing the effective gravitational torque momentarily before the pendulum inevitably falls.
**Setup:** Cart (M = 1 kg, box 0.20 × 0.05 × 0.05 m) on a slide joint (x-axis, frictionless). Inverted rod (L = 0.5 m, M = 0.3 kg) pinned at the cart top by a hinge (y-axis), pointing upward. init-qpos: rod tilted 3° from vertical (toward +x). init-qvel: zero for both cart and rod. No friction on cart slide joint.
**Motion:** render 2 s. Rod falls toward +x. Cart slides to +x (reaction). Rod falls faster than it would without the free cart — but the reactive cart motion is visible. Compare mentally with a fixed-pivot inverted pendulum: the cart provides a temporary but ultimately futile reactive force. Camera: side view, fovy = 40.
**Template:** `pendulum.xml` (inverted configuration) + `block_on_accelerating_wedge.xml` (sliding cart). The rod hinge at the top of the cart body. Cart body connected to world via slide joint (x-axis). Hinge joint at cart top: rod points up (init-qpos = π for inverted), gravity will pull it to fall.
**Hints:** Inverted pendulum init-qpos: set hinge joint angle = π − 0.0524 rad (≈ 177° from downward vertical = 3° from inverted vertical). Alternatively, use qpos = 0.0524 and flip pendulum geometry (attach point at bottom, rod upward). The fall time from 3° is approximately t_fall ≈ 1/ω × ln(2θ/θ₀) ≈ 0.9 s (where ω = √(g/L)). See gotchas.md §inverted_pendulum.

---

### Task 10 — `chain_lasso_circular`

#### `chain_lasso_circular` — Rotating chain / steady state

**Physics:** A chain rotating at constant ω forms a circular shape in the horizontal plane — each link is in centripetal force balance where the tension in the inner links provides centripetal acceleration for all the mass further out.
**Setup:** 20-link chain, M = 0.01 kg per link, link length 0.025 m. Link 0 (innermost) connected to a fixed pivot via a hinge joint (z-axis) with motor velocity = 8 rad/s. Links connected by hinge joints with y-axis (allowing in-plane spreading). All joints in the horizontal plane (gravity = "0 0 0" or arrange so chain lies in xy-plane). init-qpos: chain initially straight along x.
**Motion:** render 4 s. From the initial straight configuration, the chain rotates and gradually settles into a circular loop (each link at equal radius from pivot). At steady state, the outer links are at maximum radial displacement due to centripetal tension. Camera: top-down, pos (0, 0, 0.6), fovy = 50.
**Template:** `conical_pendulum.xml` + `dominoes.xml` (chain of bodies). 20 bodies with hinge joints. Innermost hinge to world with velocity motor ω = 8 rad/s. Chain in horizontal plane.
**Hints:** Equilibrium radius: each link at radius r_i is in balance when tension T_i = m × ω² × (sum of r_j for j ≥ i). For uniform chain, the equilibrium shape is approximately circular with total radius R_total = chain_total_length × 2/(π) for half-circle, or chain_length/2π for a full circle. With 20 links × 0.025 m = 0.5 m total, circle circumference ≈ 0.5 m → R ≈ 0.08 m. Use `gravity="0 0 0"` to keep chain in horizontal plane. See gotchas.md §rotating_chain.

---

### Task 11 — `pendulum_clock_escapement_simple`

#### `pendulum_clock_escapement_simple` — Mechanism / feedback

**Physics:** The escapement converts continuous rotational energy (from the falling weight) into discrete angular impulses, regulated by the pendulum — each pendulum half-swing allows the ratchet wheel to advance exactly one tooth, creating the characteristic tick-tock rhythm.
**Setup:** Ratchet wheel (12 teeth, R = 0.06 m, M = 0.1 kg, hinge y-axis). Anchor escapement (two-arm lever, hinge y-axis on the same shaft as pendulum, but offset). Pendulum (L = 0.25 m, M = 0.05 kg, hinge y-axis). Driving weight (M = 0.5 kg) on a string (tendon) wrapped around the wheel axle (R_axle = 0.008 m). All in the xz-plane. The anchor alternately locks and unlocks the ratchet wheel with each pendulum swing.
**Motion:** render 5 s (≥ 4 pendulum ticks). Each pendulum half-swing: anchor releases one ratchet tooth, wheel advances 30°, anchor re-engages. Driving weight descends ~3 mm per tick. Camera: front view, fovy = 35.
**Template:** `geneva_drive.xml` (intermittent rotation concept) + `ratchet_pawl.xml` (if exists) + `pendulum.xml`. gen_escapement.py assembles geometry. Key: the anchor-to-wheel contact is the critical interaction — use stiff contacts between anchor pallet faces and ratchet teeth.
**Hints:** Escapement geometry is intricate — the anchor pallet faces must contact the ratchet tooth flanks at the correct angles to deliver an impulse AND lock. Alternatively, implement the escapement using equality constraints that are conditionally activated based on pendulum angle (programmatic approach in gen script). The pendulum period T = 2π√(L/g) = 2π√(0.25/9.81) ≈ 1.0 s. See gotchas.md §escapement_contacts.

---

### Task 12 — `roller_coaster_loop_minimal`

#### `roller_coaster_loop_minimal` — Centripetal / critical speed

**Physics:** Minimum speed to complete a circular loop: v_min at the top = √(gR), where R is the loop radius. A ball released from height h_min = 5R/2 just barely makes it; from h < h_min it falls off before the top.
**Setup:** Two side-by-side tracks: (a) Launch ramp at 30° slope, height H_a = 5R/2 + ramp_start = 0.375 m + small clearance. (b) Same geometry but H_b = 0.25 m (below critical). Both tracks: straight ramp (1.0 m long) → circular loop (R = 0.15 m). Ball: R = 0.020 m, M = 0.050 kg, freejoint. Tracks as box-geom rails (channel tracks).
**Motion:** render 3 s. Ball (a) released from H_a: rolls down ramp, enters loop, completes the full 360° loop, exits. Ball (b) from H_b: enters the loop, slows, and detaches from the track before reaching the top — falls into the interior. Camera: side view, fovy = 45, showing both tracks.
**Template:** `loop_the_loop.xml` + `brachistochrone.xml` (ramp). Two complete track setups side by side (y-offset 0.25 m). Ball freejoint for each. Channel track (two rails) guides balls.
**Hints:** h_min = 5R/2 = 5×0.15/2 = 0.375 m for a point mass. With a rolling ball (solid sphere), the actual h_min = 5R/2 + 2R/5 × R/(R_ball) (rolling correction) ≈ 0.377 m. Ball (b) set to H = 0.25 m gives v_top < 0 (doesn't make it). Track must be a closed channel (not just a flat ramp) for the ball to stay on past the inverted section. See gotchas.md §loop_track_closure.


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
