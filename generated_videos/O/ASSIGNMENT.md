# Assignment for O

**Round:** 2026-05-25

## Your tasks this round

### Task 1 — `worm_gear_nonbackdrivable`

#### `worm_gear_nonbackdrivable` — Worm gear / self-locking

**Physics:** A worm gear has a high reduction ratio (N:1) and is self-locking — the worm can drive the wheel but the wheel cannot backdrive the worm, because the friction angle exceeds the lead angle. Used in lifts and hoists where loads must not back-drive.
**Setup:** Worm shaft: cylinder (R = 0.015 m) on a hinge about x, init-qvel ω = 10 rad/s. Worm wheel: cylinder (R = 0.10 m) on a hinge about z. Joint equality coupling: wheel_angle = worm_angle / 20 (20:1 ratio). High rotational friction/damping on worm shaft hinge (damping = 5 N·m·s) acts as the self-locking mechanism. Render scene (a): normal drive (worm spins, wheel turns slowly). Scene (b): give wheel init-qvel, observe worm stays still.
**Motion:** Render 4 s each. (a) Worm rotates at 10 rad/s, wheel at 0.5 rad/s. (b) Wheel given 2 rad/s, worm stays near-stationary. Camera: 3/4 isometric.
**Template:** `gear_train_2_gears.xml` (joint equality coupling).
**Hints:** True self-locking requires friction between the worm thread and wheel tooth faces — approximated here by high damping on the worm hinge that resists reverse torque. Joint equality polycoef = "0 0.05 0 0 0" (ratio 1/20).

---

### Task 2 — `projectile_with_drag_compare`

#### `projectile_with_drag_compare` — Projectile / air resistance effect

**Physics:** Air drag (≈ quadratic in speed for real projectiles, linear approximation here) reduces range and shifts the optimal launch angle below 45°. A dragged ball traces a steeper, shorter arc than a vacuum projectile launched identically.
**Setup:** Two balls at (0, 0, 0.02): Ball A (freejoint, no damping — vacuum). Ball B (freejoint, linear damping d = 0.3 kg/s on x and z translational DOFs — drag proxy). Both launched at 45° with v = 5 m/s: init-qvel = (3.54, 0, 3.54) m/s.
**Motion:** Render 2 s. Ball A traces the longer parabola, lands at x ≈ 2.55 m. Ball B lands at x ≈ 1.9 m (shorter) with a steeper descent. Side view, fovy = 45, pos (1.2, -3, 0.8).
**Template:** `projectile_jenga.xml` (projectile + floor). Two freejoint balls, one with damping.
**Hints:** Linear damping on freejoint translational DOFs: add `<joint name="ball_b_tx" ... damping="0.3"/>` for x and z joints. The drag slows both rise and fall asymmetrically. Mark each ball differently (red/blue) for clear comparison.

---

### Task 3 — `double_pendulum_on_cart`

#### `double_pendulum_on_cart` — 3-DOF / coupled chaos on cart

**Physics:** A double pendulum on a freely sliding cart has three coupled degrees of freedom (cart x, θ₁, θ₂). The additional DOF creates richer dynamics than a fixed double pendulum — the cart recoils from pendulum swings, feeding energy back into the chain chaotically.
**Setup:** Cart (M = 0.5 kg, box 0.15×0.05×0.03 m) on a frictionless slide joint along x (damping = 0). Double pendulum mounted on cart: link 1 (L = 0.30 m, M = 0.10 kg) on hinge y at cart top; link 2 (L = 0.30 m, M = 0.10 kg) on hinge y at link 1 bottom. init-qvel: cart vx = 1.5 m/s, both pendulum angles = 0.
**Motion:** Render 8 s. Cart oscillates back and forth as pendulum swings generate reaction forces; pendulum enters chaotic motion within 3–4 s. Camera: wide side view, fovy = 50.
**Template:** `double_pendulum.xml` + `pendulum_pivot_on_cart.xml`. Cart body is parent of pivot body.
**Hints:** Keep cart damping = 0 (frictionless) to preserve total horizontal momentum. The scene is sensitive to initial conditions — cart vx = 1.5 m/s with both angles at 0 gives a clean initial coupled motion that turns chaotic. See gotchas.md §chained_joints.

---

### Task 4 — `elastic_rod_bounce_modes`

#### `elastic_rod_bounce_modes` — Flexible body / impact mode excitation

**Physics:** A flexible rod dropped horizontally onto the floor excites multiple bending modes simultaneously on impact. The rod bounces in complex S-curves and wavy shapes, unlike a rigid rod which bounces uniformly.
**Setup:** 20 rigid links (each L = 0.05 m, M = 0.01 kg, capsule R = 0.006 m) connected by hinge joints (axis y) with stiffness k = 2000 N/m and damping = 0.01. Initial configuration: all hinges at 0 (rod horizontal), centered at world (0, 0, 0.25). All links given init-qvel vz = −1.5 m/s (fall toward floor).
**Motion:** Render 2.5 s. Rod falls, center hits floor first, bends around the contact, bounces back with complex S-shape oscillations. Side view, fovy = 40.
**Template:** `dominoes.xml` (chain) + `hanging_slinky_drop.xml` (release). No gravity compensation — all links released simultaneously.
**Hints:** stiffness = 2000 N/m ensures the rod feels "stiff but not rigid" on impact. The center hits first (slightly due to contact geometry), exciting the odd bending modes (1st, 3rd). Timestep = 0.0005 for stability. nsubsteps = 4.

---

### Task 5 — `spinning_hoop_on_incline`

#### `spinning_hoop_on_incline` — Gyroscopic / lateral drift on slope

**Physics:** A hoop spinning rapidly about its own axis (gyroscopically stiff) placed on an inclined surface precesses sideways rather than rolling straight down the slope. The gravitational torque (trying to tip the hoop down the slope) is 90°-redirected by angular momentum into a sideways precession.
**Setup:** Hoop (thin cylinder R = 0.10 m, thickness 0.008 m, M = 0.20 kg) on a 15° inclined floor. Freejoint. init-qvel: spin ω_spin = 30 rad/s about the hoop's own axis (pointing along the slope), plus small downhill component vx = 0.05 m/s to keep contact.
**Motion:** Render 4 s. Hoop rolls slowly sideways across the slope (perpendicular to downhill direction) instead of rolling down. Camera: front view of incline, fovy = 40.
**Template:** `rolling_race.xml` (incline) + `spinning_top.xml` (spin init). Inclined floor at 15°.
**Hints:** Precession rate Ω = M·g·L/(I·ω_spin) where L is horizontal distance from contact point to COM. For the hoop, I ≈ MR². Use high spin ω_spin = 30 rad/s to keep precession slow and visible. Friction must be high enough to prevent slipping (friction = 0.5). See gotchas.md §world_frame_angular_qvel.

---

### Task 6 — `epicyclic_compound_reversal`

#### `epicyclic_compound_reversal` — Compound planetary / direction reversal

**Physics:** In a standard planetary gear train (ring fixed, sun input, carrier output), the carrier rotates in the same direction as the sun. By instead fixing the carrier and using the ring as input, the sun rotates in the OPPOSITE direction to the ring — compound epicyclic direction reversal.
**Setup:** Same geometry as `planetary_gear_train.xml` but with the carrier body fixed to the world and the ring gear body given init-qvel ω = 3 rad/s. Three joint equalities now couple ring-to-planet and planet-to-sun with reversed sign. Sun hinge is free to rotate; carrier hinge is locked (range = "0 0").
**Motion:** Render 3 s. Ring rotates clockwise (top-down). Sun rotates counter-clockwise at ratio ω_sun/ω_ring = −(R_ring/R_sun). Planets spin AND orbit backward. Colored markers on ring and sun show opposite directions clearly.
**Template:** `planetary_gear_train.xml`. Swap which hinge is fixed vs driven. Reverse polycoef signs.
**Hints:** Carrier fixed: add `<joint ... range="0 0"/>` to lock it. Ring input: init-qvel on ring hinge. Joint equality ratio changes sign because the power path reverses. Top-down camera, fovy = 40.

---

### Task 7 — `gyroscope_on_incline_precesses`

#### `gyroscope_on_incline_precesses` — Gyro on slope / non-vertical precession axis

**Physics:** A fast-spinning gyroscope placed on an inclined surface experiences gravity along the slope-normal direction. Its precession axis is the slope normal (not vertical), causing the spin axis to sweep a cone around a tilted axis — visually striking.
**Setup:** Inclined floor at 15° to horizontal. Gyroscope disc (R = 0.08 m, M = 0.30 kg, thin cylinder) with freejoint, placed on the slope. init-qvel: spin ω = 60 rad/s about the disc's own symmetry axis (initially pointing up the slope), no translational velocity.
**Motion:** Render 5 s. Gyroscope precesses around the slope-normal axis; the spin axis traces a tilted cone — not around vertical but around the slope's upward normal. Camera: 3/4 view from above the incline, fovy = 45.
**Template:** `spinning_top.xml` (spin init) + `incline_friction.xml` (tilted floor). Tilt world floor geom 15°.
**Hints:** The precession axis is normal to the slope, not to the world vertical. Precession rate Ω = M·g·cos(15°)·L / (I·ω). Floor friction = 0.4 to maintain contact without excessive sliding. init-qvel in world frame: see gotchas.md §world_frame_angular_qvel for converting body-frame ω to world-frame qvel.

---

### Task 8 — `chain_vs_rod_pendulum`

#### `chain_vs_rod_pendulum` — Rigid vs flexible pendulum / effective length

**Physics:** A rigid rod pendulum has a well-defined period T = 2π√(2L/3g). A chain pendulum of the same total length behaves differently: its COM is at the same height but its effective pendulum length (related to its I/Md) differs, and the chain's flexibility allows internal modes that shift the apparent period.
**Setup:** Side by side: (a) Rigid rod (single body, length L = 0.50 m, M = 0.20 kg, box 0.02×0.02×0.50 m), hinged at its top — pivot at (−0.3, 0, 1.0). (b) Chain (10 links, each 0.05 m, M = 0.02 kg, capsule), top link hinged at (0.3, 0, 1.0), remaining links via hinge joints (axis y, damping = 0.005). Both released from 30° tilt.
**Motion:** Render 6 s. Rod swings at its period T ≈ 1.16 s. Chain swings at a slightly different effective period; lower links lag behind the upper links visibly, creating a whipping motion. Side view, fovy = 45.
**Template:** `pendulum.xml` (rod) + `swinging_chain_pendulum.xml` (chain).
**Hints:** The chain's lower links lag the upper ones — a visual signature of flexibility. Keep chain hinge damping = 0.005 (very low) so the flexible modes don't die too quickly. Mark the bottom of each to compare oscillation phases.

---

### Task 9 — `pendulum_group_phase_velocity`

#### `pendulum_group_phase_velocity` — Wave packet / group vs phase velocity

**Physics:** In a dispersive wave medium, the phase velocity (speed of individual oscillation crests) differs from the group velocity (speed of the packet envelope). A Gaussian-modulated wave packet spreads as it travels because different frequency components move at different speeds.
**Setup:** 20 pendulums (lengths 0.28 to 0.42 m in small steps, creating a dispersive medium). init-qpos: q_i = A·exp(−(i−10)²/8)·cos(k₀·i) with A = 0.15 rad, k₀ = π/3 (a localized wave packet centered at pendulum 10). No damping.
**Motion:** Render 20 s. The packet envelope moves at the group velocity while the oscillation crests inside move at the phase velocity. The envelope broadens over time (dispersion). Camera: front view showing all 20 pendulums, fovy = 55.
**Template:** `pendulum_waves.xml`. Modify lengths to vary linearly; modify init-qpos to wave packet.
**Hints:** Group velocity v_g = dω/dk, phase velocity v_p = ω/k. For pendulums with varying length, ω_i = √(g/L_i) — each pendulum has a different natural frequency, creating dispersion. The packet spreading becomes clear by t = 10 s. Render at least 20 s.

---

### Task 10 — `superball_corner_retroreflection`

#### `superball_corner_retroreflection` — Elastic collision / retroreflection

**Physics:** A spinning superball thrown at a 90° corner undergoes two sequential surface bounces; each bounce reverses the spin component normal to that surface. The combined effect sends the ball approximately antiparallel to its initial direction.
**Setup:** 90° corner formed by two perpendicular floor/wall geoms. Ball (R = 0.025 m, M = 0.05 kg, freejoint). Contact: high CoR (solref = "−200000 −20", solimp = "0.99 0.999 0.001"), high friction (friction = "1.0 0.1 0.01"). init-qvel: translational (2.0, 0, −1.0) m/s (toward corner) + angular ω_y = −20 rad/s (backspin).
**Motion:** Render 1.5 s. Ball hits floor, bounces sideways into wall, bounces back approximately antiparallel to original direction. Camera: 3/4 view of corner, fovy = 50.
**Template:** `bowling.xml` (floor + walls) + `elastic_collision.xml` (stiff contact settings).
**Hints:** The retroreflection is only approximate — exact retroreflection requires a specific spin magnitude. The key is high friction (spin-to-velocity coupling) and high CoR. Two bounces in quick succession are the visual signature. See gotchas.md §high_restitution_contacts.

---

### Task 11 — `ball_in_v_groove_constraint`

#### `ball_in_v_groove_constraint` — Constrained rolling / groove guidance

**Physics:** A ball rolling in a V-groove track (two flat rails at 45° forming a V) is constrained to move only along the groove axis. The groove exerts normal forces from both sides simultaneously, providing lateral guidance without kinetic friction along the axis.
**Setup:** Two flat floor geoms angled at ±45° to form a V-groove, oriented along the x-axis, length 1.0 m. Ball (R = 0.025 m, M = 0.05 kg, freejoint). Ball placed in the groove at x = −0.4 m, init-qvel: vx = 0.8 m/s. Groove-ball friction = 0.3 (rolling without slip along x, constrained laterally).
**Motion:** Render 2.5 s. Ball rolls smoothly along the groove, decelerating slightly due to rolling resistance. No lateral drift. Camera: 3/4 front-side view, fovy = 40.
**Template:** `bead_on_helix.xml` (channel guidance concept). gen_v_groove.py places two angled geom strips.
**Hints:** V-groove geometry: two flat geoms each rotated ±45° around x-axis, meeting at the groove bottom. Ball radius 0.025 m, groove half-angle 45° — contact at ~0.018 m from groove centerline on each side. Groove width at ball contact ≈ 0.036 m. See gotchas.md §groove_contact_geometry.

---

### Task 12 — `spinning_top_on_incline`

#### `spinning_top_on_incline` — Gyroscope / precession around tilted axis

**Physics:** A spinning top on a tilted surface precesses around the local gravitational vertical (the surface normal), not the world vertical. The precession cone axis is tilted from vertical by the slope angle, creating visually distinct "slanted" precession circles.
**Setup:** Floor tilted 15° from horizontal (geom euler = "0 −15 0"). Spinning top (standard cone+stem body, M = 0.05 kg, cone R = 0.035 m) with freejoint, placed on the slope. init-qvel: spin ω_spin = 60 rad/s about top's symmetry axis (pointing approximately along slope-normal direction), no translational velocity. init-qpos: tip at contact point on slope.
**Motion:** Render 6 s. Top precesses around the slope-normal axis, tracing circles that are tilted from vertical — clearly different from the same top on a flat floor. Camera: oblique view showing the tilted precession cone, pos (0.5, −0.6, 0.4), fovy = 38.
**Template:** `spinning_top.xml`. Tilt the floor geom. Adjust init-qpos/qvel to match slope geometry.
**Hints:** On the slope, effective gravity = g·cos(15°) ≈ 9.48 m/s² perpendicular to slope. Precession rate Ω = M·g·cos(15°)·d/(I·ω_spin) where d is the distance from tip to COM. Floor friction = 0.4. See gotchas.md §world_frame_angular_qvel for setting spin in world frame.


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
