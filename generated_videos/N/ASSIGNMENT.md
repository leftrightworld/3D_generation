# Assignment for N

**Round:** 2026-05-25

## Your tasks this round

### Task 1 — `resonance_forced_oscillation`

#### `resonance_forced_oscillation` — Resonance / driven oscillator

**Physics:** A spring-mass oscillator driven at its natural frequency ω₀ = √(k/m) builds amplitude without bound (in the absence of damping). Off-resonance driving at 0.7·ω₀ produces only bounded, small-amplitude oscillation.
**Setup:** Two side-by-side spring-masses: M = 0.1 kg, k = 100 N/m, ω₀ ≈ 31.6 rad/s. Both masses on slide joints along z with stiffness=100. gen_resonance.py injects a periodic impulse (qvel += A·sin(ω_drive·t)·dt each step) at ω_drive = ω₀ for Mass A and ω_drive = 0.7·ω₀ for Mass B. Amplitude A = 0.02 m/s per step, timestep 0.001 s. No damping on either joint.
**Motion:** Render 15 s. Mass A amplitude grows steadily (resonance). Mass B oscillates at small bounded amplitude. Camera: side view, fovy = 45, showing both oscillators.
**Template:** `spring_mass.xml`. Two copies x-separated 0.3 m. gen_resonance.py drives each at its respective frequency.
**Hints:** MuJoCo has no built-in sinusoidal actuator. Implement via gen script that writes qpos/qvel into the model at each step using mujoco.mj_step. Alternatively, attach a driver mass to a long massless rod and give it circular initial conditions — the vertical component acts as a sinusoidal force. See gotchas.md §forced_oscillation.

---

### Task 2 — `resonance_damping_compare`

#### `resonance_damping_compare` — Q factor / damping regimes

**Physics:** Three oscillators with different damping coefficients γ driven at their natural frequency show vastly different steady-state amplitudes. High Q (low damping) → large amplitude; overdamped → barely moves.
**Setup:** Three spring-masses, identical k = 100 N/m, M = 0.1 kg. Joint damping: (a) γ = 0.01 (underdamped, Q ≈ 50), (b) γ = 0.63 (critically damped, Q = 1), (c) γ = 2.0 (overdamped). All three driven at ω₀ via gen_resonance.py as above.
**Motion:** Render 20 s. Oscillator (a) builds large amplitude. (b) barely responds. (c) no oscillation. Camera: side view showing all three.
**Template:** `spring_mass.xml` ×3. Adjust joint damping values.
**Hints:** Q = ω₀·M/γ. For clean demo, run at least 20 s so the high-Q oscillator has time to build up significant amplitude. x-separation 0.3 m between each pair.

---

### Task 3 — `wave_dispersion_chain`

#### `wave_dispersion_chain` — Dispersion relation / frequency-dependent speed

**Physics:** In a uniform spring chain (linear dispersion at low frequency, but nonlinear at high k), a Gaussian pulse travels without spreading. In a chain with alternating spring constants k₁/k₂, the dispersion relation has a bandgap — the pulse spreads and slows as high-frequency components travel at different speeds.
**Setup:** Two 40-body chains side by side (x-separation 0.3 m). Chain A: uniform k = 500 N/m between all links, damping = 0. Chain B: alternating k₁ = 200 N/m, k₂ = 800 N/m. All bodies M = 0.01 kg on slide joints z. Both chains receive the same initial Gaussian displacement pulse: z_i = 0.02·exp(-(i-5)²/2) for i = 0..39, others at z = 0.
**Motion:** Render 3 s. Chain A pulse travels cleanly. Chain B pulse spreads into multiple components that travel at different speeds. Side view, both chains visible.
**Template:** `wave_reflection_fixed.xml` (discretized chain). gen_dispersion_chain.py for alternating k setup.
**Hints:** Alternating masses also create dispersion (acoustic vs optical branches). Use alternating k (simpler) rather than alternating mass. Timestep 0.0005 for stability.

---

### Task 4 — `melde_harmonic_3modes`

#### `melde_harmonic_3modes` — String harmonics / standing wave modes

**Physics:** A discretized string (both ends fixed) initialized in the shape of its nth harmonic mode oscillates in a pure standing wave. The 1st mode has one antinode (λ = 2L), 2nd has two antinodes (λ = L), 3rd has three (λ = 2L/3). All at different frequencies.
**Setup:** Three discretized strings side by side (x-separation 0.25 m), each 40 nodes, total length L = 0.50 m, both ends fixed (world weld). Each node M = 0.005 kg on slide joint z, stiffness k = 200 N/m between neighbors. init-qpos: z_i = A·sin(n·π·i/39) for n = 1, 2, 3 respectively. A = 0.025 m. Damping = 0 on all joints.
**Motion:** Render 4 s. Each string oscillates cleanly in its mode shape. Camera: front view, fovy = 50, all three strings visible.
**Template:** `standing_wave_on_string.xml`. Three copies with different init-qpos.
**Hints:** Node spacing must be small enough to resolve the 3rd harmonic — 40 nodes easily resolves 3 antinodes. Period of mode n: T_n = 2L/(n·v) where v = √(k·L_seg/M). Ensure natural frequency matches actual MuJoCo frequency with chosen k.

---

### Task 5 — `coriolis_turntable_puck`

#### `coriolis_turntable_puck` — Rotating frame / Coriolis deflection

**Physics:** A puck launched radially on a frictionless rotating turntable travels in a straight line in the lab frame but traces a curved path in the rotating frame — demonstrating the Coriolis pseudoforce.
**Setup:** Rotating disc (R = 0.25 m, M = 2 kg, thickness 0.01 m) on a fixed vertical hinge with init-qvel ω = 2 rad/s. Puck (R = 0.015 m, M = 0.05 kg) placed on the disc surface at r = 0.05 m from center with init-qvel vr = 0.3 m/s radially outward (in the lab frame). Disc-puck contact: friction = 0. Disc hinge damping = 0.
**Motion:** Render 4 s. Puck slides outward and off the disc edge. Camera: directly top-down, fovy = 60. Marker on puck traces the curved path visible against disc markings (colored sectors painted on disc geom).
**Template:** `rotating_fluid.xml` (spinning disc base). Puck as a sphere with freejoint on the disc surface.
**Hints:** In the lab frame the puck moves in a straight line (no friction). Color the disc with wedge-shaped geoms at different angles to make the rotation visible. Puck traces a curve relative to disc markings. See gotchas.md §rotating_frames.

---

### Task 6 — `rotating_bucket_parabola`

#### `rotating_bucket_parabola` — Rotating frame / centrifugal parabola

**Physics:** In a rotating reference frame, the centrifugal pseudopotential adds to gravity to create an effective gravity pointing outward and downward. Small balls in a spinning cylinder settle on a paraboloid z = ω²r²/(2g), the same shape as a rotating liquid surface.
**Setup:** Cylinder (R = 0.12 m, H = 0.18 m) on a vertical hinge with init-qvel ω = 8 rad/s. Cylinder wall as curved geom or ring of box segments. ~60 balls (R = 0.006 m, M = 0.002 kg) with freejoints, initially piled near the center at z = 0.02 m.
**Motion:** Render 8 s. Balls are thrown outward by rotation, climb the cylinder walls, and settle in a paraboloid surface. Camera: 3/4 overhead, fovy = 50.
**Template:** `rotating_fluid.xml`. Replace fluid visualization with ball granular proxy.
**Hints:** Balls need contact with each other and the cylinder wall. friction = 0.3. At ω = 8 rad/s, parabola height at r = 0.10 m: z = 8²×0.1²/(2×9.81) ≈ 0.033 m — a modest but visible curve. See gotchas.md §granular_initial_conditions.

---

### Task 7 — `universal_joint_velocity_variation`

#### `universal_joint_velocity_variation` — Cardan joint / velocity ripple

**Physics:** A Hooke's (Cardan) universal joint connecting two shafts at angle θ = 30° transmits constant torque but produces sinusoidal output angular velocity variation: ω_out = ω_in·cos θ/(1 − sin²θ·cos²φ), oscillating ±15% per revolution.
**Setup:** Input shaft: cylinder (L = 0.15 m, R = 0.015 m) on a fixed hinge (axis y), init-qvel ω = 4 rad/s. Cross-piece: small plus-shaped body with two perpendicular hinges connecting input and output shafts. Output shaft: same cylinder, hinge axis rotated 30° from input. Bright colored marker disc on each shaft end to visualize speed.
**Motion:** Render 4 s (~2.5 revolutions). Input marker rotates uniformly. Output marker visibly speeds up and slows down twice per revolution. Side view, fovy = 40.
**Template:** `four_bar_linkage.xml` (crossed hinge concept). gen_universal_joint.py for the cross-piece geometry.
**Hints:** The cross-piece must have exactly two perpendicular hinges — one matching the input shaft axis, one perpendicular for the output. The 30° shaft angle is the key parameter for visible variation. Add a velocity-indicator (arm length proportional to current ω) if possible via colored sector geom.

---

### Task 8 — `snells_law_ball_refraction`

#### `snells_law_ball_refraction` — Snell's law analog / momentum at interface

**Physics:** A ball rolling from a low-friction region (fast) into a high-friction region (slow) has its path bent at the interface — analogous to Snell's law. The component of momentum parallel to the boundary is conserved (friction only acts perpendicular to motion), bending the trajectory toward the normal.
**Setup:** Flat frictionless floor divided into two half-planes by a sharp line along z-axis. Left half (x < 0): friction = 0 (fast region). Right half (x > 0): floor friction = 0.6 (slow region, approximated by floor geom segmentation). Ball (R = 0.02 m, M = 0.05 kg, freejoint) starts at (-0.3, 0, 0.02), init-qvel: vx = 1.5 m/s, vy = 0.8 m/s (oblique approach at ~28° to interface normal).
**Motion:** Render 2 s. Ball rolls straight in left region, then bends toward the normal upon entering the right region. Top-down camera, fovy = 50, xyaxes = "1 0 0  0 1 0".
**Template:** `incline_friction.xml`. Two floor geom patches with different friction values.
**Hints:** The analogy is clearest with a perfectly sharp interface and no rolling (use a sliding puck: zero rotational inertia). The "refraction" is approximate — real Snell's law requires wave optics. See gotchas.md §friction_zones.

---

### Task 9 — `suspension_cable_parabola`

#### `suspension_cable_parabola` — Distributed load / parabola vs catenary

**Physics:** A catenary (uniform load per arc length = cable self-weight) hangs as y = cosh(x/a). A suspension bridge cable carrying a uniform horizontal load (deck weight) hangs as a parabola y = x²/(2a). Side-by-side demonstration of both shapes.
**Setup:** Two chains of 40 links each (M = 0.01 kg, length 0.04 m per link), endpoints fixed at (±0.8 m, 0, 1.0 m). Chain A: no extra loads — pure catenary. Chain B: 20 evenly spaced vertical rods hanging from every other link, each rod carrying a hanging mass M_load = 0.03 kg at its bottom (uniform horizontal load distribution).
**Motion:** Render 6 s (settle time ~3 s, then static). Camera: side view, both chains overlaid in the same x-z plane (y-separated by 0.1 m), showing different sag shapes.
**Template:** `hanging_chain_catenary.xml`. Chain B: add sub-bodies with tendons every 2 links.
**Hints:** The parabola chain sags more at the center relative to the endpoints. Overlay a thin static arch (or colored geom) tracing the theoretical parabola for visual comparison. Render 6 s — first 3 s for settling, last 3 s static.

---

### Task 10 — `vibration_isolation_spring_mount`

#### `vibration_isolation_spring_mount` — Vibration isolation / transmissibility

**Physics:** A machine (heavy mass) on a spring mount is isolated from floor vibration at frequencies above √2·ω_n. Below resonance, vibration is transmitted fully; at resonance it amplifies; above, it is attenuated (transmissibility < 1).
**Setup:** Floor body (M = 5 kg, slide joint z) given sinusoidal motion via gen_isolation.py at ω_drive = 2·ω_n. Machine (M = 2 kg, box, slide joint z) connected to floor via spring (k = 500 N/m, damping = 0.5). ω_n = √(500/2) ≈ 15.8 rad/s; ω_drive ≈ 31.6 rad/s. Floor amplitude: ±0.02 m.
**Motion:** Render 6 s. Floor oscillates visibly ±2 cm. Machine barely moves (< ±3 mm). Camera: side view showing both floor and machine markers.
**Template:** `spring_mass.xml`. Floor body on a slide joint with gen-driven motion; machine body nested above with spring joint.
**Hints:** At ω_drive = 2·ω_n, transmissibility T = 1/|1 − (ω/ω_n)²| = 1/3 ≈ 0.33 (with light damping). Machine amplitude should be ~1/3 of floor amplitude. Mark the floor and machine with contrasting colored geoms.

---

### Task 11 — `brazil_nut_granular_effect`

#### `brazil_nut_granular_effect` — Granular segregation / size separation

**Physics:** When a mixture of small and large granular particles is vibrated vertically, the large particles rise to the top — the "Brazil nut effect." Caused by a combination of void-filling (small particles fall into gaps left by large particle) and convection cells.
**Setup:** Cylindrical container (R = 0.065 m, H = 0.18 m). 50 small balls (R = 0.007 m, M = 0.003 kg) and 1 large ball (R = 0.020 m, M = 0.07 kg) initially placed with large ball at the bottom. Container body on a slide joint z, gen_brazil_nut.py injects sinusoidal z-displacement (A = 0.012 m, f = 8 Hz). Friction between balls = 0.4.
**Motion:** Render 10 s. Large ball visibly rises through the small-ball bed, reaching the top by ~8 s. Camera: side view with transparent or cut-away container wall.
**Template:** `rotating_fluid.xml` (container geometry). gen_brazil_nut.py for vertical vibration.
**Hints:** Container wall needs to be thin box geoms (or a mesh cylinder) so the interior is visible. The vibration amplitude A must exceed the ball diameter for effective segregation. This is a computationally heavy scene (~50 contacts per step) — use timestep = 0.001 and nsubsteps accordingly.

---

### Task 12 — `arch_vs_beam_load_compare`

#### `arch_vs_beam_load_compare` — Arch vs beam / compression vs bending

**Physics:** An arch transfers vertical load to its foundations through compressive forces along the arch axis (no bending). A flat beam under the same load must resist bending moments that grow as span². The arch is vastly more efficient for wide spans.
**Setup:** Two side-by-side structures spanning 0.60 m: (a) Semi-circular arch of 10 wedge-shaped blocks (same as arch_compression.xml), with a 1 kg central load. (b) Flat beam of 10 rectangular blocks (each 0.06×0.04×0.04 m) connected by weak hinges (stiffness = 500 N/m), spanning the same width, with the same 1 kg central load.
**Motion:** Render 4 s. Arch holds the load — stable. Beam sags progressively and eventually collapses under the load. Camera: side view showing both structures, fovy = 45.
**Template:** `arch_compression.xml` (arch) + `cantilever_load_curve.xml` (beam). x-separate structures by 0.8 m.
**Hints:** Beam hinges must be weak enough to show deflection under 1 kg but stiff enough to not collapse instantly. stiffness = 500 N/m gives visible sag in ~1 s. The arch requires careful initial geometry so blocks interlock cleanly.


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
