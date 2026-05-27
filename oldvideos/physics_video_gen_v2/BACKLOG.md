# Scene Backlog

**Status (2026-05-23):** 23 done, **~90 candidates** queued with full
descriptions, ~10 explicitly out-of-scope. Theoretical ceiling ≈ 88–92
genuinely-distinct mechanics scenes (no parameter sweeps); beyond that, the
next idea is just "the same with different numbers".

## How to use this file

1. **Pick an item** from your `ASSIGNMENT.md` (in handoff packages) or any
   unclaimed item here (master only).
2. **Read its full description** — `Physics`, `Setup`, `Expected motion`,
   `Template`, `Hints`. The Template line tells you which existing scene to
   copy from as a starting point. Don't write from scratch.
3. **Build it** following the 5-step recipe in `CLAUDE.md` / `README.md`.
4. **Mark done** in `DIARY.md` when finished, strike the line here.

## Conventions for each entry

```
### `scene_filename` — Topic tag

**Physics:** One sentence on the concept being demonstrated.
**Setup:** Physical arrangement, initial conditions, what bodies + joints exist.
**Motion:** What the rendered clip should show.
**Template:** Which existing scene to copy from as a starting point.
**Hints:** Key parameter values, common pitfalls, gotchas to watch (cross-ref `docs/gotchas.md` when relevant).
```

---

## ✅ Done (104 scenes)

See `DIARY.md` for the inventory and notes. mp4s in `out/` (original 4) and
`out/scenes/` (the rest). Showreel at
`out/scenes/all_scenes_grid.mp4`.

### Original 23 (maiwang)

| # | scene | topic |
|---|-------|-------|
| 1 | bowling | collision + friction |
| 2 | marble | gravity + rolling |
| 3 | pendulum | simple oscillation |
| 4 | projectile_jenga | projectile + stability |
| 5 | newton_cradle | elastic chain |
| 6 | double_pendulum | chaos |
| 7 | incline_friction | μ comparison |
| 8 | dominoes | chain reaction |
| 9 | spring_mass | SHM |
| 10 | atwood | inextensible string |
| 11 | spinning_top | precession + nutation |
| 12 | conical_pendulum | circular motion |
| 13 | loop_the_loop | centripetal force |
| 14 | rolling_race | I/MR² |
| 15 | pendulum_waves | multi-pendulum sync |
| 16 | coupled_pendulums | normal modes |
| 17 | block_overhang | ∑L/(2k) harmonic series |
| 18 | galileo_dropballs | equivalence of fall time |
| 19 | elastic_collision | momentum transfer |
| 20 | brachistochrone | cycloid vs straight |
| 21 | maxwell_wheel | rotational+translational KE |
| 22 | beam_buckling | Euler instability |
| 23 | rotating_fluid | centrifugal pile-up |

### Round 1 — Employee A (13/17 complete)

| # | scene | topic |
|---|-------|-------|
| 24 | bifilar_pendulum | torsional oscillation |
| 25 | wilberforce_pendulum | spring-torsion energy exchange |
| 26 | damped_pendulum_decay | viscous damping |
| 27 | yoyo_with_reversal | Maxwell yo-yo reversal |
| 28 | coin_spiral | precession then flop |
| 29 | inelastic_collision | perfectly inelastic impact |
| 30 | coefficient_of_restitution | bounce height decay |
| 31 | com_pair_track | COM conservation |
| 32 | beats | coupled oscillator envelope |
| 33 | wave_reflection_fixed | inverted reflection at fixed end |
| 34 | capstan_effect | rope wrap friction |
| 35 | falling_chain_classical | chain acceleration |
| 36 | bead_on_helix | helical rail gravity slide |

### Round 1 — Employee B (17/17 complete)

| # | scene | topic |
|---|-------|-------|
| 37 | trifilar_pendulum | disc torsional oscillation |
| 38 | pendulum_with_air_drag | quadratic drag decay |
| 39 | anharmonic_pendulum_large_swing | large-angle deviation from SHM |
| 40 | rolling_cone | cone circular path |
| 41 | gyroscope_on_string | gyroscope precession |
| 42 | falling_chimney | tipping rigid body |
| 43 | ballistic_pendulum | impulse + momentum |
| 44 | glancing_2d_collision | elastic glancing impact |
| 45 | cannon_recoil | Newton 3rd law |
| 46 | normal_modes_2mass | coupled spring modes |
| 47 | wave_reflection_free | same-polarity free-end reflection |
| 48 | stick_slip | kinetic/static friction oscillation |
| 49 | dzhanibekov_effect | intermediate-axis theorem |
| 50 | sliding_chain_off_table | chain over edge |
| 51 | bead_on_cycloid_track_isochrony | tautochrone |
| 52 | geneva_drive | intermittent mechanism |
| 53 | balance_beam_lever | torque equilibrium |

### Round 1 — Employee C (17/17 complete)

| # | scene | topic |
|---|-------|-------|
| 54 | compound_pendulum_shapes | period vs shape |
| 55 | triple_pendulum | chaos |
| 56 | spherical_pendulum_2d | rose-curve trajectory |
| 57 | spool_with_string | rolling + string direction |
| 58 | mass_through_hole | angular momentum conservation |
| 59 | reuleaux_triangle_rolling | constant-width rolling |
| 60 | basketball_tennis_drop | superball rebound |
| 61 | line_collision_chain | Newton's cradle no strings |
| 62 | two_pendulums_collide | elastic velocity exchange |
| 63 | vertical_spring_mass | vertical SHM |
| 64 | wave_on_heavy_rope | pulse speed vs tension |
| 65 | tipping_vs_sliding | friction determines outcome |
| 66 | rattleback | chirality-driven spin reversal |
| 67 | hanging_chain_catenary | catenary shape |
| 68 | bead_on_parabolic_wire | SHM vs amplitude on parabola |
| 69 | domino_branching | Y-branch cascade |
| 70 | pyramid_keystone_removal | arch collapse |

### Round 1 — Employee D (17/17 complete)

| # | scene | topic |
|---|-------|-------|
| 71 | cycloidal_pendulum_huygens | isochronous pendulum |
| 72 | rolling_chain | tank-tread chain |
| 73 | centrifugal_governor | Watt flyball |
| 74 | pulley_with_inertia | Atwood with massive pulley |
| 75 | n_body_1d_collisions | elastic chain of 7 balls |
| 76 | block_on_accelerating_wedge | non-inertial frame |
| 77 | pendulum_with_lateral_spring | spring-pendulum coupling |
| 78 | hanging_slinky_drop | bottom lags on release |
| 79 | standing_wave_on_string | fundamental mode |
| 80 | belt_friction | coupled pulleys |
| 81 | block_on_block_static_friction | stacked block launch |
| 82 | tumbling_book | intermediate-axis flip |
| 83 | swinging_chain_pendulum | flexible chain whip |
| 84 | bead_in_rotating_ring | centrifugal equilibrium |
| 85 | block_and_tackle | 2:1 mechanical advantage |
| 86 | cantilever_load_curve | beam tip deflection |
| 87 | symmetry_breaking_ball_on_dome | unstable equilibrium |

### Round 2 — Employee F (17/17 complete)

| # | scene | topic |
|---|-------|-------|
| 88 | galileo_pendulum_peg | energy conservation with peg |
| 89 | horizontal_vs_dropped_balls | independence of motion |
| 90 | chain_jet_classic | self-propelled chain |
| 91 | rolling_disc_inscribes_cycloid | cycloid trajectory |
| 92 | bucket_of_water_overhead_swing | vertical circular motion |
| 93 | two_marbles_curved_track_collision | elastic collision on track |
| 94 | planetary_gear_train | sun + planet gears |
| 95 | gear_train_2_gears | gear ratio |
| 96 | four_bar_linkage | Grashof crank |
| 97 | ratchet_pawl | one-way mechanism |
| 98 | chain_unspooling_from_pile | chain pile dynamics |
| 99 | triple_block_friction_chain | stacked friction chain |
| 100 | chain_on_scale_falling | impact on scale |
| 101 | two_bodies_on_incline_string | incline + tendon |
| 102 | double_atwood | nested Atwood |
| 103 | galileo_inclined_plane_squared | d ∝ t² |
| 104 | rolling_dumbbell | tumbling on floor |

---

## 🔵 Tier 1 — Quick wins (1–2 hr each, copy + tweak)

### Pendulum / oscillation (7)

#### ~~`bifilar_pendulum`~~ ✅ — Oscillation
**Physics:** Mass suspended by two parallel strings swings, but rotation about the vertical is geometrically blocked. Period depends on string length and lateral separation.
**Setup:** A horizontal rod (or thin plate) hangs from two vertical strings at its two ends. Push it sideways; it swings without rotating.
**Motion:** Rod translates sideways in pure swing; no twisting about its own axis.
**Template:** `pendulum.xml`. Use two tendons instead of one.
**Hints:** Use spatial tendons (`<tendon><spatial>`) for the two strings — see gotcha #2 for placement. Rod needs a freejoint or a slide+slide joint pair; constraints from the two tendons enforce no rotation. Render ~4 s.

#### ~~`trifilar_pendulum`~~ ✅ — Oscillation
**Physics:** Disc suspended by three equally spaced strings; angular oscillation period is sensitive to the disc's moment of inertia (this is how I is measured experimentally).
**Setup:** Horizontal disc hung from a ceiling triangle by three vertical strings (radius r, length L). Twist the disc slightly about the vertical axis; it oscillates torsionally.
**Motion:** Disc rotates back and forth about its vertical axis with period T = 2π·sqrt(I·L/(m·g·r²)).
**Template:** `pendulum.xml` + `atwood.xml` (for the tendon-as-string idea). Three tendons, one disc, init-qpos a small yaw.
**Hints:** Use a single hinge joint about z for the disc, with NO stiffness. The "restoring" comes purely from the three-string geometry — strings tilt as the disc rotates, giving a gravitational restoring torque. Disc body needs a freejoint or constrained body.

#### ~~`compound_pendulum_shapes`~~ ✅ — Oscillation
**Physics:** Period of a rigid-body pendulum depends on I_pivot, not just mass — three different shapes pivoted at one end swing at different periods even with the same mass.
**Setup:** Three pendulums side-by-side: a thin rod, a flat plate, and a thin triangular plate, all pivoted at their top with hinge joints. Same mass each.
**Motion:** Released from the same angle, the three swing at visibly different periods.
**Template:** `pendulum.xml`. Replicate 3× with different geom types.
**Hints:** Compute I_pivot for each shape (parallel-axis theorem). Use `<inertial>` to override if needed — gotcha #14. Side-view camera, fovy ~40.

#### ~~`wilberforce_pendulum`~~ ✅ — Oscillation / coupling
**Physics:** Mass hangs on a spring with both longitudinal and torsional stiffness. With matched periods, energy slowly trades between bobbing and twisting.
**Setup:** Cylindrical bob hangs from a long thin coiled "spring" (modelled by a tendon for visual + a custom stiff+damped joint pair). Bob has a slide joint (z) and a hinge joint (about z). Both joints have stiffness and similar periods.
**Motion:** Initially the bob bobs up-and-down; over 5–10 oscillations the bobbing dies and the bob is twisting; then it twists back to bobbing. Beats.
**Template:** `spring_mass.xml` + `spinning_top.xml`.
**Hints:** Tune k_slide and k_torsion so periods match within 5%. Add small initial qvel in slide only; the coupling (which we'd add via a constraint or pre-existing geometry) will transfer energy. If pure-MuJoCo coupling is hard, use a small `<equality>` linking the two joints with a tiny polycoef. Render 15+ s.

#### ~~`damped_pendulum_decay`~~ ✅ — Oscillation
**Physics:** A pendulum with viscous damping shows exponential decay of amplitude: θ(t) = θ₀·e^(-γt)·cos(ωt). Period is nearly unchanged for light damping.
**Setup:** Single pendulum with a moderate joint damping value.
**Motion:** ~8–10 visible swings, each successively smaller; eventually settles to rest.
**Template:** `pendulum.xml`. Add `damping="0.05"` to the hinge.
**Hints:** Pick damping so the envelope decay is visible within 8 s (try 0.04). Camera: same as `pendulum.xml`. Grid PNG should show monotonically decreasing amplitude.

#### ~~`pendulum_with_air_drag`~~ ✅ — Oscillation
**Physics:** Quadratic drag (∝ ω²) decays a pendulum faster at large amplitudes than viscous damping; the envelope curves rather than being a clean exponential.
**Setup:** Same as damped pendulum but with quadratic damping if MuJoCo supports it, otherwise high linear damping that mimics drag.
**Motion:** Initially fast amplitude decay, slowing as amplitude shrinks.
**Template:** `pendulum.xml`.
**Hints:** MuJoCo joint damping is linear in ω. To fake quadratic, use a large linear damping and accept the qualitative behavior. Side-by-side render with `damped_pendulum_decay` would be ideal but each scene is rendered alone.

#### ~~`triple_pendulum`~~ ✅ — Chaos
**Physics:** Adding a third link to the double pendulum increases chaotic sensitivity; the trajectory is wildly path-dependent on initial conditions.
**Setup:** Three rigid arms connected by hinges in series, top pivot fixed. Link lengths 0.30 / 0.25 / 0.20 m, masses 0.15 / 0.12 / 0.10 kg (decreasing as you go down — like double_pendulum). Each hinge has axis y, damping=0.005.
**Motion:** From `init-qpos="1.4, 0, 0"` (top link near horizontal, others vertical), the system rapidly transitions to chaotic flailing where all three links swing wildly.
**Template:** `double_pendulum.xml`. Add a third nested body with the same hinge axis.
**Hints:** Render 8 s — chaos takes a few seconds to fully develop. Camera same as double_pendulum (front view, fovy 38). Damping smaller than double_pendulum so motion lasts longer.

### Rolling / rotation (4)

#### ~~`yoyo_with_reversal`~~ ✅ — Rotation
**Physics:** Like Maxwell wheel but the wheel hits the lower string limit and re-ascends — the string catches and the rotation direction reverses with respect to descent.
**Setup:** Modified Maxwell wheel where the slider joint hits a "stop" at the bottom, causing the equality constraint to allow re-ascent.
**Motion:** Disc descends, rotates, hits bottom, climbs back up while spinning the same way.
**Template:** `maxwell_wheel.xml`. Add a slider range stop at the bottom.
**Hints:** The polycoef equality may bind oddly at the range limit — use stiff `solref` for the slider's range so the bounce is mostly elastic. Render 6–8 s to see one full cycle.

#### ~~`rolling_cone`~~ ✅ — Rotation
**Physics:** A cone rolling on its side traces a circular path centered on its apex (precession of the rolling axis).
**Setup:** A cone (apex on the floor) rolls in a circular path. Use a thin cone geom or build from segments.
**Motion:** Cone rolls around its apex, completing a circle in proportion to its half-angle.
**Template:** `rolling_race.xml`.
**Hints:** Body needs a freejoint + rolling-without-slip via friction. Initial spin matters: give it angular velocity so it starts rolling, not skidding. fovy ~38, top-down 3/4 camera. Render 4–6 s.

#### ~~`spool_with_string`~~ ✅ — Rotation / counter-intuitive
**Physics:** A spool with string wrapped underneath — pulling the string horizontally rolls the spool TOWARD you (not away). Surprising visual.
**Setup:** Spool (cylinder with a smaller axle) on the floor. String wraps under the axle and exits horizontally toward +x. Pull the string by ramping a tension.
**Motion:** Spool rolls in +x direction while string unwinds and the spool's axle moves toward you.
**Template:** `marble.xml` + `maxwell_wheel.xml`.
**Hints:** No actuator needed if you set the spool's initial qvel so it's already in motion. Alternatively, attach the string end to a stationary point and give the spool a small push so the tension acts. Camera: side view.

#### ~~`rolling_chain`~~ ✅ — Rotation
**Physics:** A flexible chain laid flat on the floor can be pulled like a tank tread — the chain "rolls" by having parts continuously transition between contact and free-fall.
**Setup:** Long chain of small linked bodies on the floor; one end is given a horizontal velocity.
**Motion:** The chain moves like a tractor tread, with the leading end being lifted by tension and falling at the rear.
**Template:** `dominoes.xml` (chain layout) + `atwood.xml` (linked bodies).
**Hints:** Probably needs ~30 small links with friction-enabled contact. Render 4–5 s. May need a programmatic generator (`gen_rolling_chain.py`).

### Collision / momentum (6)

#### ~~`inelastic_collision`~~ ✅ — Collision
**Physics:** Two bodies stick together after impact; kinetic energy is lost but momentum is conserved.
**Setup:** Two cubes on a frictionless track; one moving toward the other. On contact, they stick (via high-damping contact or an equality constraint that activates).
**Motion:** Moving block hits stationary block, both move off together at half the original velocity (for equal masses).
**Template:** `elastic_collision.xml`.
**Hints:** Disable elastic contact: set `solref` and `solimp` to soft values so the impact dissipates. Or use a tendon equality that snaps in on contact (advanced). Camera: same as elastic_collision.

#### ~~`coefficient_of_restitution`~~ ✅ — Collision
**Physics:** A ball bouncing on a floor loses a fixed fraction of energy per bounce. Successive bounce heights follow h_n = h_0 · e^(2n), giving geometric decay.
**Setup:** Single ball dropped from a height onto a hard floor, with contact `solref/solimp` tuned for partially elastic collision.
**Motion:** Ball bounces with decreasing height; the envelope shows geometric decay over 5–8 bounces.
**Template:** `bowling.xml` (for floor + ball pattern).
**Hints:** Use `solref="-100000 -8" solimp="0.98 0.999 0.001"` for ~85% restitution. Camera: side view, frame from 0 to drop height. Render 4–5 s.

#### ~~`ballistic_pendulum`~~ ✅ — Collision + oscillation
**Physics:** A "bullet" embeds in a pendulum bob; momentum conservation gives the bob's swing velocity; energy conservation gives the swing height. The combo lets you measure the bullet's speed.
**Setup:** Small fast cube (the bullet) flies horizontally into a heavier cube hanging on a string (the bob). On contact, the bullet sticks (inelastic).
**Motion:** Bullet → impact → bob+bullet swing as one pendulum to a measurable height.
**Template:** `pendulum.xml` + `projectile_jenga.xml`.
**Hints:** Inelastic contact (soft solref) on the bob-bullet pair. Mass ratio matters: bullet/bob ≈ 0.05 gives a visible but modest swing. Camera: side view.

#### ~~`basketball_tennis_drop`~~ ✅ — Collision / energy transfer
**Physics:** Stacked balls dropped together; the bottom one bounces off the floor and immediately collides with the top one, transferring kinetic energy upward. The small top ball can shoot up at ~3× the drop speed.
**Setup:** Two balls stacked vertically (small one on top of big one), released from a height.
**Motion:** Big ball hits floor and rebounds; immediately collides with small ball mid-air; small ball flies up far higher than its drop height.
**Template:** `bowling.xml` + `elastic_collision.xml`.
**Hints:** Use very high contact stiffness (`solref="-200000 -20"`) for both bottom-ball-to-floor AND ball-to-ball contacts. Initial separation between balls: 0.01 m (almost touching). Mass ratio ~10:1 (heavy:light) gives the cleanest effect.

#### ~~`glancing_2d_collision`~~ ✅ — Collision
**Physics:** Equal-mass elastic collision at an angle: the two balls fly off at 90° to each other. Their final velocity vectors form a right angle.
**Setup:** Two pucks on a frictionless table; one moving, the other stationary, with a small lateral offset so the impact is glancing (not head-on).
**Motion:** Moving puck strikes glancingly; both pucks scatter at angles that sum to 90°.
**Template:** `elastic_collision.xml`. Switch to 2D (top-down camera).
**Hints:** Pucks on a slide-x and slide-y joint pair (no rotation). High contact stiffness, zero friction between pucks and floor. Top-down camera. Render 2 s.

#### ~~`line_collision_chain`~~ ✅ — Collision
**Physics:** Newton's cradle without the strings — a row of touching balls. Striking the leftmost transmits momentum along the line; only the rightmost moves off.
**Setup:** 5 balls in a horizontal row on a frictionless track, just barely touching. Add 1 more ball arriving from the left with some velocity.
**Motion:** Incoming ball strikes, momentum "walks" down the line in an instant, the rightmost ball leaves at the incoming velocity.
**Template:** `newton_cradle.xml` (for contact tuning) + `elastic_collision.xml` (for track).
**Hints:** Use the same stiff contact + small timestep recipe as Newton's cradle (gotcha #4). Balls on freejoints, frictionless track. Energy still leaks (not perfectly elastic) but the qualitative effect is striking.

### Spring / oscillator (4)

#### ~~`beats`~~ ✅ — Oscillation
**Physics:** Two mass-spring oscillators with slightly different frequencies appear to slowly modulate each other's amplitude when started in phase. The envelope frequency is the difference frequency.
**Setup:** Two separate mass-spring systems side-by-side, with k values differing by ~5%. Both released with the same initial displacement.
**Motion:** Both bodies oscillate; their RELATIVE phase drifts. Watched together, the visual "beats" pattern is the slow envelope.
**Template:** `spring_mass.xml`. Replicate 2× with slightly different k.
**Hints:** Need to render long enough for the difference frequency to manifest — beat period = 2π/(ω₁-ω₂). If ω₁=2π, ω₂=2π·0.95, beat period = 2π/0.314 ≈ 20 s. Render 25 s or use larger Δk. Camera: front view showing both side by side.

#### ~~`normal_modes_2mass`~~ ✅ — Oscillation
**Physics:** Two masses with three springs (wall–m–m–wall) have two normal modes: symmetric (both move together) at lower frequency, antisymmetric (move oppositely) at higher frequency.
**Setup:** Two masses on a horizontal frictionless track, three springs in series. Initial conditions chosen to excite ONE mode only (e.g., symmetric: both same displacement; antisymmetric: equal but opposite).
**Motion:** Demonstrates pure mode: in symmetric mode the gap between masses stays constant; in antisymmetric mode the gap oscillates twice per cycle.
**Template:** `spring_mass.xml`.
**Hints:** Use tendons as visual springs + slide joints with stiffness for the dynamics. Render two versions (one for each mode) if desired, or just pick antisymmetric (more visually striking). Camera: side view.

#### ~~`vertical_spring_mass`~~ ✅ — Oscillation
**Physics:** Mass on a vertical spring oscillates about its STRETCHED equilibrium (where spring force = mg), not the unstretched length. Period is unchanged: T = 2π·sqrt(m/k).
**Setup:** Spring (tendon + stiffness) hanging from a ceiling point; mass attached at the bottom. Release from above the equilibrium (or below).
**Motion:** Mass oscillates vertically about the equilibrium height; equilibrium is BELOW the unstretched-spring height.
**Template:** `spring_mass.xml`.
**Hints:** k tuned so equilibrium stretch is visible (e.g., 5–10 cm). Mark the equilibrium with a thin horizontal line for clarity. Camera: side view.

#### ~~`pendulum_with_lateral_spring`~~ ✅ — Oscillation / coupling
**Physics:** A pendulum attached to a horizontal wall-spring shows mode coupling: pure swing and pure spring oscillation are eigenstates only when carefully tuned; otherwise energy sloshes between them.
**Setup:** Hinge-pivoted pendulum with a spring connecting its mass to a horizontal wall.
**Motion:** Initially energy goes into the pendulum swing; over time it transfers to the spring's vibration, then back.
**Template:** `pendulum.xml` + `spring_mass.xml`.
**Hints:** Tune string length and spring k so the periods are close — that gives the strongest beats-like transfer. Render 15 s.

### Constraint / mechanical advantage (3)

#### ~~`block_and_tackle`~~ ✅ — Mechanical advantage
**Physics:** A 2:1 pulley system halves the force needed to lift a mass (and doubles the distance). This is Atwood with an extra pulley.
**Setup:** Heavy mass on one end of a rope; rope goes over a fixed pulley, around a movable pulley attached to a lighter mass, and ends fixed to the ceiling.
**Motion:** Heavy mass descends slowly; the light load lifts up (also slowly) because the rope on the movable pulley side bears HALF the tension.
**Template:** `atwood.xml`. Add a second pulley + joint-equality coupling: q_heavy + 2·q_light = 0.
**Hints:** Polycoef "0 -0.5 0 0 0" enforces q_heavy = -0.5·q_light (i.e., 2:1 ratio). Mass ratio matters: heavy ≈ 1.0, light ≈ 0.45 to see clean lifting at moderate damping.

#### `mass_on_frictionless_incline` — Constraint
**Physics:** Block on a frictionless inclined plane has acceleration a = g·sin(θ) regardless of mass.
**Setup:** Inclined ramp + a block constrained to slide along its surface (slide joint along the ramp's surface direction).
**Motion:** Block accelerates down the ramp; with no friction, motion is pure linear acceleration along the slope.
**Template:** `incline_friction.xml`. Drop friction to 0.
**Hints:** Set ALL friction values to 0 (block AND ramp — gotcha #1!). Slide joint along the ramp surface gives clean physics without contact instability. Camera: side view. Render 2 s.

#### `incline_with_pulley` — Constraint / Atwood variant
**Physics:** Mass on an incline connected over a pulley to a hanging mass — system accelerates if hanging weight > sin(θ)·incline weight. Classic IPhO-style problem.
**Setup:** Inclined ramp + a block on it + a pulley at the top of the ramp + a string over the pulley + a hanging mass on the other side.
**Motion:** If hanging mass is heavy enough, it descends and pulls the incline block up the ramp; otherwise the reverse.
**Template:** `atwood.xml` + `incline_friction.xml`.
**Hints:** Use joint equality (Atwood-style) between the slide joint on incline and the slide joint of the hanging mass. Adjust masses so the dynamics are visible over 3–4 s. Damping in both joints.

### Friction (4)

#### ~~`capstan_effect`~~ ✅ — Friction / wrap
**Physics:** A rope wrapped around a fixed cylinder needs only a small holding force to resist a large pulling force; the ratio scales exponentially with wrap angle: F_pull/F_hold = e^(μθ).
**Setup:** Vertical post on the floor; rope wrapped 1.5 turns around it; one end has a heavy weight (10 kg); the other end has a light weight (0.5 kg, hanging just over the edge).
**Motion:** Despite the huge mass ratio, the rope holds — light weight doesn't get lifted because friction along the wrap absorbs the tension.
**Template:** `atwood.xml` (for tendons + hanging weights) + `dominoes.xml` (post setup).
**Hints:** Use a thin spatial tendon for the rope; friction interaction may be approximate. Could fake the effect with a 2:1 joint equality if direct wrap-friction is too hard. Render 5 s.

#### ~~`stick_slip`~~ ✅ — Friction
**Physics:** Block dragged by a spring shows alternating stick-and-slip: builds tension until static friction breaks, then slips forward, then sticks again. Generates characteristic sawtooth motion.
**Setup:** Block on floor with high static friction; attached by a spring to a slowly-moving driver. (Driver moves via init-qvel.)
**Motion:** Block sits still while spring stretches, then suddenly jumps forward; then sits still while spring stretches again; repeats.
**Template:** `incline_friction.xml` + `spring_mass.xml`.
**Hints:** μ_static must be > μ_kinetic — MuJoCo distinguishes these via `friction` and `solimp` settings. Driver needs a sustained low velocity, so give it big mass and high init-qvel so it barely slows over the render. Render 6 s.

#### ~~`tipping_vs_sliding`~~ ✅ — Friction / statics
**Physics:** A tall block on an inclined plane either tips over or slides, depending on the ratio of its height/width vs μ — the tipping angle is arctan(w/h), the sliding angle is arctan(μ).
**Setup:** Two side-by-side blocks on the same incline: one tall (high h/w), one short (low h/w). Same μ for both. Increase incline gradually.
**Motion:** As the incline tilts, the tall block tips first while the short one is still static; then the short block slides.
**Template:** `incline_friction.xml`. Two blocks with different aspect ratios.
**Hints:** Use a hinged or sliding incline (joint with init velocity to gradually tilt) or just set the incline at a critical angle showing both behaviors at once. Side view camera. Render 4 s.

#### ~~`belt_friction`~~ ✅ — Friction / coupled rotation
**Physics:** A belt connecting two pulleys couples their rotation — if pulley radii differ, the angular velocities differ inversely. With sufficient slip, the belt slides instead of driving.
**Setup:** Two pulleys (different radii) connected by a closed loop tendon "belt". One pulley is driven (initial spin); the other should follow.
**Motion:** Driven pulley spins; belt transfers motion; driven pulley spins at scaled velocity.
**Template:** `maxwell_wheel.xml` + `atwood.xml` (for tendon as belt).
**Hints:** Belt as a tendon-loop is approximate — true belt-pulley coupling needs friction simulation along the tendon, which MuJoCo doesn't do well. Workaround: use a joint equality coupling the two hinges directly (polycoef = -r₁/r₂). The tendon is purely visual. Render 4 s.

---

## 🟣 Tier 1 — Quick wins, brand new (~20 more)

### Kinematics / projectile (4)

#### `monkey_and_hunter` — Kinematics
**Physics:** Both projectiles fall the same Δh in the same time. A dart aimed at the monkey's initial position will hit it regardless of dart speed (within ballistic range), provided both are released at the same instant.
**Setup:** A "cannon" (small box) on the floor angled at ~30° toward a "monkey" ball suspended at height 0.8 m, 1 m away. The monkey is held by a "release point" that activates at t=0.
**Motion:** Cannon fires a small ball at angle; monkey simultaneously begins free-fall. They collide in mid-air regardless of initial dart velocity.
**Template:** `projectile_jenga.xml` (strip the tower).
**Hints:** Both are freejoint balls. The "monkey" has zero initial qvel; the dart has angled init-qvel pointing at monkey. Make 2-3 scenes' worth: vary dart speed, all still collide. Camera: x-z side view, fovy 38.

#### `projectile_max_range_45` — Kinematics
**Physics:** For projectiles launched at the same speed from ground level, the 45° angle maximizes range; angles equidistant from 45° (e.g. 30° and 60°) give equal but shorter ranges.
**Setup:** Three projectiles launched simultaneously at 30°, 45°, 60° from the same point, same initial speed.
**Motion:** All three follow parabolic arcs; the 45° lands furthest; the 30° and 60° land the same distance away but at different times.
**Template:** `projectile_jenga.xml`.
**Hints:** Three freejoint balls with carefully tuned init-qvel (each (v·cos θ, 0, v·sin θ)). Side view camera with wide fovy. Render 1.5 s.

#### ~~`com_pair_track`~~ ✅ — Momentum
**Physics:** Two masses on a frictionless track connected by a compressed spring — when released, they fly apart, but the center of mass stays still (momentum conservation).
**Setup:** Two cubes on a horizontal frictionless slider track, with a compressed (or stretched) spring between them. Spring releases at t=0.
**Motion:** The two masses fly apart in opposite directions; visibly, their midpoint never moves.
**Template:** `spring_mass.xml` + `elastic_collision.xml`.
**Hints:** Initialize the spring with stored energy (tendons may need init-qvel that gives them stored PE, or use a stiff hinge with init torsion). A pre-marked "COM" indicator (a thin vertical line at the midpoint) makes the demo visually obvious. Mass ratio 2:1 gives unequal velocities but same COM. Camera: side view.

#### ~~`cannon_recoil`~~ ✅ — Momentum
**Physics:** Cannon on wheels firing a projectile experiences recoil; final momenta sum to zero (cannon backward, ball forward).
**Setup:** Heavy cannon (box on wheels — slide joint horizontal) holding a smaller projectile. At t=0, the projectile is given a strong forward velocity; the cannon must accordingly receive backward momentum.
**Motion:** Projectile shoots forward; cannon visibly rolls backward.
**Template:** `marble.xml` (for cart on wheels) + `projectile_jenga.xml`.
**Hints:** Use a freejoint for both bodies but connect them with a "spring" or "rod" until t=0 (then somehow release). Simpler: just give both bodies opposite initial qvel, scaled by inverse mass. Render 2.5 s.

### Rotational / gyroscopic (5)

#### `bicycle_wheel_gyroscope` — Rotation / precession
**Physics:** A spinning wheel suspended by a string at one end of its axle precesses horizontally rather than falling — gyroscopic stabilization. Precession rate Ω = M·g·L / (I·ω) where L is distance from string to wheel center.
**Setup:** A heavy wheel: cylinder, R=0.10 m, thickness 0.015 m, M=0.5 kg. Mounted on a thin axle (length 0.18 m) sticking through its center. One axle end is connected by a 0.4 m vertical string (tendon) to the ceiling. Initial state: axle horizontal, wheel at world position (0.09, 0, 0.6), and `init-qvel` gives the wheel a spin of ω=60 rad/s about its axle axis.
**Motion:** Wheel doesn't fall; instead, its axle slowly rotates horizontally about the suspension point with Ω ≈ 2-3 rad/s. Render at least one half-revolution.
**Template:** `spinning_top.xml` (for spin physics) + `maxwell_wheel.xml` (for tendon as string).
**Hints:** Use a freejoint on the wheel body. Initial qvel: linear=(0,0,0), angular=(0,ω,0) — see gotcha #10 for world-frame angular qvel. Wheel inertia I_axle = ½MR² = 0.0025. Render 5 s. Camera: side view at the suspension point, pos (1.2, -0.5, 0.7), fovy 38.

#### ~~`gyroscope_on_string`~~ ✅ — Rotation
**Physics:** Same gyroscopic precession as the bicycle wheel demo, but with a thin disc (rather than wheel) emphasizing the rotor character. Different aspect ratio yields different I/I_perpendicular ratio.
**Setup:** Thin heavy disc: cylinder R=0.08 m, thickness 0.005 m, M=0.4 kg, on an axle (length 0.15 m). One axle end connected by a 0.4 m tendon to the ceiling. Disc starts at world (0.075, 0, 0.65), axle horizontal, spinning at ω=80 rad/s.
**Motion:** Disc precesses about the vertical through the suspension point.
**Template:** `bicycle_wheel_gyroscope` (copy after building that one first; this is its sibling).
**Hints:** Thinner disc + higher ω compared to bicycle_wheel scene. Precession rate Ω = Mg·L/(½MR²·ω). Render 5 s. Side view, pos (1.0, -0.4, 0.75), fovy 38.

#### ~~`mass_through_hole`~~ ✅ — Angular momentum
**Physics:** A mass on a string passing through a hole in a frictionless table is pulled inward; as the radius shrinks, the angular velocity grows (L = mvr conserved).
**Setup:** A puck on a frictionless table, attached to a string that passes through a central hole. Below the table, the string's lower end is given a downward velocity (or a hanging mass below pulling it).
**Motion:** Puck spirals inward while spinning faster and faster.
**Template:** `conical_pendulum.xml` + `atwood.xml`.
**Hints:** Tricky to set up — the string going through a hole needs to be modelled as a tendon with a fixed point in space (the hole). Alternative: use a slide joint to model the radius and a hinge joint for the angle. Camera: top-down or 3/4.

#### ~~`reuleaux_triangle_rolling`~~ ✅ — Rotation / geometry
**Physics:** A Reuleaux triangle (constant-width non-circular shape) rolls along a flat surface keeping the TOP face at a constant height — but the centroid of the shape bobs up and down by ~6.7% of the width as it rolls.
**Setup:** Reuleaux triangle of side L=0.10 m, thickness (z-extent) 0.05 m. Construct programmatically: for each of 3 vertices (at angles 0°, 120°, 240° on a circle of radius L/sqrt(3)), generate an arc of radius L centered on the OPPOSITE vertex. Approximate each arc with 8 small `<geom type="box">` segments. The triangle is given an initial linear velocity (vx=0.3 m/s) and matching rolling angular velocity (ω_y = vx / (centroid_height)).
**Motion:** Triangle rolls; the upper face holds a near-constant height (so a board on top wouldn't tilt). The centroid (and thus a marker glued to the centroid) bobs visibly up and down with 3× the rolling angular period.
**Template:** Programmatic gen (`gen_reuleaux.py`). Reuse rolling pattern from `marble.xml`.
**Hints:** ~24 box geoms total (3 arcs × 8). Friction tuned for rolling without slip: `friction="0.6 0.005 0.0001"`. Side view, camera pos (0, -1.5, 0.15), fovy 40. Render 4 s.

#### ~~`coin_spiral`~~ ✅ — Rotation / friction
**Physics:** A coin set on its edge and given a small wobble spins down in a spiral, transitioning from tall precession to flat rotation with characteristic increasing pitch. Energy lost to floor friction.
**Setup:** A thin cylinder ("coin") on the floor, given an initial vertical orientation with a small tilt and large initial spin about its vertical axis.
**Motion:** Coin spins on edge, gradually tilts more, and finally settles flat after a few seconds of accelerating-pitch oscillation.
**Template:** `spinning_top.xml`.
**Hints:** Use a freejoint with a carefully tuned initial state including a small tilt and large ω. Camera at 3/4 to capture the spiral motion. Render 6–8 s.

### Waves on strings (3)

#### ~~`wave_reflection_fixed`~~ ✅ — Waves
**Physics:** A pulse traveling along a string reflects off a fixed (clamped) end with an inverted polarity.
**Setup:** Long discretized horizontal string (chain of small bodies linked by spring-like hinges), one end pinned to a wall, other end free. Initial pulse generated by displacing the free end then releasing.
**Motion:** Pulse travels along the string toward the wall; upon hitting the wall, returns as an inverted pulse traveling back.
**Template:** `dominoes.xml` (chain) + `spring_mass.xml`.
**Hints:** Use ~40 nodes, hinge joints with stiffness, low damping. Initial qpos gives the pulse shape (e.g., one peak at the middle). Render 4 s. Side view.

#### ~~`wave_reflection_free`~~ ✅ — Waves
**Physics:** A pulse traveling along a string reflects off a free end with the same polarity (no inversion).
**Setup:** Same as above but with the second end completely free (no wall).
**Motion:** Pulse propagates → reflects from free end → returns SAME-SIDE.
**Template:** Same as `wave_reflection_fixed` but free-end boundary.
**Hints:** Discrete chain endpoint has a freejoint (no constraint). Render side-by-side with the fixed case for the educational contrast — but each is its own scene.

#### ~~`wave_on_heavy_rope`~~ ✅ — Waves
**Physics:** Wave speed in a vertical hanging rope varies with height: v(h) = sqrt(g·h). A pulse at the top moves faster than at the bottom (heavy lower portion has lower tension).
**Setup:** Vertical chain of small bodies hanging by gravity, top fixed, bottom free.
**Motion:** A pulse displaced at one end propagates downward and speeds up (or vice versa).
**Template:** `dominoes.xml` (chain) + `spring_mass.xml`.
**Hints:** Use ~30 nodes; gravity creates the tension gradient automatically. Initial qpos for the pulse. Render 3 s.

### Statics / structures (4)

#### `arch_compression` — Statics
**Physics:** A Roman arch supports a heavy load above by transferring the weight through compressive force along its curved spine. Remove the keystone and the arch collapses.
**Setup:** Roman semi-circular arch made of N wedge-shaped blocks; a heavy load on top. Compare with-keystone vs without-keystone.
**Motion:** With keystone in place, the arch holds the load indefinitely. Without (drop the keystone), the arch buckles inward.
**Template:** `block_overhang.xml`. Programmatic generator likely needed.
**Hints:** Use ~10-12 wedge-shaped blocks per arch. Block-block friction tuned moderately. Initial qpos placing each block precisely. Render 4 s. Side view.

#### ~~`balance_beam_lever`~~ ✅ — Statics / equilibrium
**Physics:** A lever in static equilibrium: F1·d1 = F2·d2 (torque balance about the fulcrum).
**Setup:** Horizontal rod pinned at center on a fulcrum. Two different weights hanging at different distances from the fulcrum, balanced.
**Motion:** Static initially. Add a small perturbation (a third mass briefly applied), then released — beam returns to equilibrium.
**Template:** `pendulum.xml`. The rod is essentially a pendulum but pinned at center.
**Hints:** The fulcrum is a hinge joint with no stiffness. Two weights attached as nested bodies at different x offsets. Render 3 s.

#### ~~`pyramid_keystone_removal`~~ ✅ — Statics
**Physics:** A pyramid of blocks held together by gravity and friction; remove a load-bearing block and the structure collapses.
**Setup:** ~10 blocks stacked in a pyramidal arrangement (4 on bottom, 3 on next, etc.). At some moment, one block is removed (via temporary support that disappears).
**Motion:** Pyramid initially static; after key block removal, it collapses progressively.
**Template:** `block_overhang.xml`.
**Hints:** Initially over-constrain so the stack is stable (high friction, soft contacts). To "remove" a block, just don't render it or use a slide joint with init-qvel to slide it out. Render 3 s.

#### `ladder_slipping_off_wall` — Friction / statics
**Physics:** A ladder leans against a wall, supported by friction at the floor and the wall. If μ is too low, the ladder slips outward (foot slides, top slides down).
**Setup:** A long thin rod leaning at ~60° against a vertical wall. Friction values at the floor and wall contact tuned.
**Motion:** With high μ: static. With low μ: ladder slips outward.
**Template:** `incline_friction.xml`.
**Hints:** Use a freejoint for the ladder body. Floor and wall geoms. Tune friction so the demo is at the edge of stability. Render 3–4 s.

### Mechanisms (3)

#### `slider_crank_mechanism` — Mechanism
**Physics:** Converts rotational motion to linear (reciprocating) motion via a crank arm and connecting rod. Used in every IC engine.
**Setup:** A spinning crank (hinge joint with init-qvel); connecting rod attached at one end of the crank; piston (slide joint) attached at the other end of the rod.
**Motion:** Crank spins continuously → piston reciprocates back and forth.
**Template:** `maxwell_wheel.xml`. Custom rod via hinge joints.
**Hints:** Initial qvel on the crank hinge to make it spin; geometric constraints (the rod's length) drive the piston. Render 3 s, several cycles. Side view.

#### ~~`geneva_drive`~~ ✅ — Mechanism
**Physics:** Converts continuous rotation into intermittent indexed rotation — a driver wheel with a single pin engages a slotted driven wheel, causing the driven wheel to step by 360°/N per pin engagement.
**Setup:** Driving wheel: cylinder R=0.08 m, thickness 0.02 m, with a small box pin of half-extent (0.005, 0.005, 0.015) at offset 0.04 m from center. Driven wheel: cylinder R=0.10 m, thickness 0.02 m, with 4 radial slots cut at 90° spacing. Each slot is a 0.012 m wide × 0.04 m deep rectangular channel approximated by box geoms forming the slot walls. The two wheel centers are 0.13 m apart on the same y-line so the pin clears the driven wheel's body but enters the slots. Driver gets init-qvel ω=2 rad/s on its hinge.
**Motion:** Driver rotates continuously; driven wheel sits still for ~270° of driver rotation, then jumps forward by 90° in ~90° of driver rotation, then sits still again. Render shows 2-3 indexing steps.
**Template:** Programmatic gen `gen_geneva_drive.py`. Closest existing: `dominoes.xml` (for chain reaction style).
**Hints:** Slot width must be slightly larger than pin width (1.5x for clean engagement). Damping on driven wheel hinge (0.05) to prevent oscillation. Friction off between pin and slot walls. Render 5 s. Top-down camera, pos (0.06, 0, 0.7), looking straight down, xyaxes="1 0 0  0 1 0".

#### ~~`domino_branching`~~ ✅ — Chain reaction
**Physics:** A multi-branch domino chain where one tip can trigger multiple branches simultaneously.
**Setup:** A Y-shaped or fractal layout of dominoes. The first domino is pushed.
**Motion:** Wave propagates from the start, branches at the Y, then both branches cascade simultaneously.
**Template:** `dominoes.xml`. Use a custom programmatic generator.
**Hints:** Spacing and angle at the branch point matters — too far apart and the trigger doesn't reach both. Render 5 s. Camera angled to see both branches.

### Multi-body, exotica (4)

#### ~~`hanging_slinky_drop`~~ ✅ — Oscillation / dispersion
**Physics:** A slinky hanging from one end has a tension gradient (tight at top, slack at bottom). When released, the top falls but the bottom STAYS in place for about 0.3 s due to wave propagation along the spring — counter-intuitive.
**Setup:** Long discretized slinky (chain of bodies with stiff springs between them) hanging from one end. Release the support at t=0.
**Motion:** Top of slinky falls immediately; bottom remains stationary for several frames; then everything falls together.
**Template:** `dominoes.xml` + `spring_mass.xml`.
**Hints:** Many small bodies (~20+), spring-joints with high stiffness. Initial qpos = gravity-equilibrium positions (heavy upward bias). Render 1.5 s. Side view, fovy small.

#### ~~`anharmonic_pendulum_large_swing`~~ ✅ — Oscillation
**Physics:** A pendulum with very large amplitude (~150°) shows period dependence on amplitude — the small-angle approximation breaks. Period at 90° is ~1.18× longer than at 5°.
**Setup:** Single pendulum, init-qpos = 150° (almost vertical-up).
**Motion:** Pendulum oscillates with very large amplitude; period visibly longer than what small-angle predicts.
**Template:** `pendulum.xml`. Just init-qpos = large angle.
**Hints:** Reference: place a second small-amplitude pendulum (5°) side-by-side for visual contrast — but that may be parameter variation in disguise; alternatively, just render one with a long duration to show the period.

#### ~~`centrifugal_governor`~~ ✅ — Rotation / equilibrium
**Physics:** Watt's flyball governor: two heavy balls on arms rotate about a vertical axis; at higher RPM, centrifugal effects lift them outward, which (in a real engine) would close a steam valve. Here we just show the equilibrium angle.
**Setup:** Two heavy balls on arms attached to a central spindle by hinge joints (so they can swing outward). Spindle spins about its vertical axis with initial qvel.
**Motion:** Balls swing outward as the system spins; at steady ω, they reach an equilibrium angle determined by ω.
**Template:** `conical_pendulum.xml` (two of them, mirrored).
**Hints:** Damping on the swing hinges so the balls settle. Camera: 3/4 front. Render 4 s.

#### ~~`n_body_1d_collisions`~~ ✅ — Multi-body
**Physics:** A line of N balls with elastic collisions and a small initial perturbation evolves to interesting patterns. Edge cases (light vs heavy ratios) show momentum transfer phenomena.
**Setup:** 6–8 balls on a frictionless track, just barely separated. Strike one end with a fast-moving ball.
**Motion:** Series of elastic collisions propagating; with equal masses, the leftmost ball stops and the rightmost moves off. With varying masses, complex transfer patterns.
**Template:** `elastic_collision.xml` + `newton_cradle.xml`.
**Hints:** Stiff contacts, small timestep. Use freejoints on frictionless track. Camera: side view, wide enough for all N balls.

---

## 🟠 Tier 2 — New patterns (3–5 hr each)

### Free rigid body / inertia tensor (4)

#### `tippe_top` — Free rigid body
**Physics:** An asymmetric "top" (rounded bottom + protruding stem) spun fast inverts itself: the stem (initially at the top) ends up touching the floor while the body spins on it. Driven by the contact friction torque combined with the asymmetric inertia tensor.
**Setup:** Two-part body via a single freejoint:
- Lower hemisphere: capsule from (0,0,0) to (0,0,0.04), radius 0.04 m, M=0.06 kg (heavy half-sphere bottom).
- Upper stem: thin capsule from (0,0,0.04) to (0,0,0.08), radius 0.005 m, M=0.002 kg.
Initial position: center of mass at z = 0.035 (hemisphere bottom near floor). Initial qvel = (0,0,0, 0,0, 80) — 80 rad/s about world +z. Floor contact uses `friction="0.4 0.005 0.01"` (high sliding friction, moderate torsional to drive the flip).
**Motion:** First 1-2 s: top spins upright. Then it gradually tilts; eventually inverts and ends up balancing on the stem. Total time to flip: ~4-5 s.
**Template:** `spinning_top.xml` for the rotation setup + `bowling.xml` for floor friction.
**Hints:** This is HARD to tune. Margins: see gotcha #11 for the floor-friction subtlety. Mass distribution between hemisphere and stem is critical — hemisphere too light → no flip; too heavy → never tilts. Render 6 s, may need 5-8 iterations to dial in. Camera: 3/4 low-angle, pos (0.3, -0.3, 0.1), fovy 36.

#### ~~`dzhanibekov_effect`~~ ✅ — Free rigid body / intermediate axis
**Physics:** A free rigid body with three distinct principal moments of inertia, spun about its intermediate axis, periodically flips by 180°. The other two axes are stable; only the intermediate is unstable.
**Setup:** A T-handle or similar asymmetric body in zero gravity, with init-qvel about the intermediate principal axis (with a small perturbation to make the instability manifest).
**Motion:** Body spins about one axis for ~1 s, then suddenly flips by 180°, then spins for another ~1 s, then flips again. Periodic.
**Template:** `spinning_top.xml`. Set `gravity="0 0 0"`.
**Hints:** Use `<option gravity="0 0 0"/>`. Freejoint body. Mass distribution: T-handle (long arm + short cross-piece). Initial qvel slightly off the intermediate axis to seed the instability. Render 4–5 s.

#### ~~`rattleback`~~ ✅ — Free rigid body / chirality
**Physics:** A "rattleback" (Celt stone) — boat-shaped, with the long axis of its inertia ellipsoid slightly offset from the long axis of its underside curvature — prefers one spin direction; spun the wrong way it rattles vertically and reverses direction.
**Setup:** Approximate the rattleback with an ellipsoid body. Use a freejoint at world (0, 0, 0.015). Inertia tensor must be asymmetric AND its principal axes must be rotated ~5° relative to the geometric long axis (this is what creates the chirality). Achieve this by setting `<inertial pos="0 0 0" mass="0.05" fullinertia="Ixx Iyy Izz Ixy Ixz Iyz"/>` with non-zero Ixy. Concretely: Ixx=2e-5, Iyy=8e-5, Izz=8.5e-5, Ixy=1.5e-5, Ixz=Iyz=0. Geom: ellipsoid via `<geom type="ellipsoid" size="0.06 0.025 0.015"/>` (long axis x, narrow y, flat z). Floor friction `friction="0.4 0.005 0.001"`. Initial qvel about +z: in our model ωz≈-7 is preferred (smooth spin); ωz≈+7.5 is wrong (pitch bob → slows → reverses). See `render.py` compare segments.
**Motion:** Wrong-direction spin: rocks up-and-down (visible bobbing of the long axis), spin slows to a stop, then reverses to the preferred direction.
**Template:** `spinning_top.xml` (rotation handling).
**Hints:** Ellipsoid geom is convex in MuJoCo (works). The skewed-inertia trick (off-diagonal Ixy) is the entire physics. Render 6-8 s for the full reversal. Side view, pos (0, -0.5, 0.08), fovy 38.

#### ~~`tumbling_book`~~ ✅ — Free rigid body / intermediate axis
**Physics:** Same physics as Dzhanibekov, demonstrated with a book/rectangular slab. Spinning about the medium-length axis is unstable.
**Setup:** Rectangular slab in zero gravity, init-qvel about its intermediate axis (with small perturbation).
**Motion:** Spins ~1 s about intermediate axis, then suddenly flips, then again.
**Template:** Same as `dzhanibekov_effect` but with a rectangular slab geom.
**Hints:** Different shape but same physics. Render 5 s.

### Chains and ropes (4)

#### ~~`falling_chain_classical`~~ ✅ — Chain dynamics
**Physics:** A chain falling off the edge of a table accelerates faster than g once moving — falling links pull the still-on-table links into motion.
**Setup:** A chain (~30 discretized bodies linked by short hinges) initially resting on a table with half hanging off the edge.
**Motion:** Hanging portion descends, pulling the on-table portion off — chain accelerates progressively until fully airborne.
**Template:** `dominoes.xml` (chain layout).
**Hints:** Friction on the table tuned so the resting portion doesn't slide too easily. Render 2–3 s. Side view.

#### ~~`sliding_chain_off_table`~~ ✅ — Chain dynamics
**Physics:** A chain half on a frictionless table, half hanging — the hanging weight pulls the table portion off; in the limit of no friction, motion is purely gravity-driven.
**Setup:** Same as `falling_chain_classical` but with zero friction on the table.
**Motion:** Hanging portion descends; table portion slides off rapidly.
**Template:** `dominoes.xml`. Adjust friction.
**Hints:** Same caveats but with friction off. Render 1.5 s.

#### ~~`hanging_chain_catenary`~~ ✅ — Statics / chain
**Physics:** A chain hanging from two pinned endpoints at the same height settles into a CATENARY (cosh) curve, not a parabola — though they look similar for shallow sags.
**Setup:** 40 chain links, each a small capsule (length 0.04 m, radius 0.005 m, M=0.01 kg per link). Links connected by hinge joints with axis y (sag in x-z plane), damping=0.05. Endpoints (link 0 and link 39) are attached to fixed posts via weld constraints at world (-0.5, 0, 1.0) and (+0.5, 0, 1.0). Initial qpos: all hinges = 0 (chain starts as a straight horizontal line stretching between the posts; gravity pulls it down to settle).
**Motion:** Chain dynamically settles under gravity into the catenary shape over ~2-3 s, then stays stable.
**Template:** Programmatic gen (`gen_hanging_catenary.py`). Reuse pattern from `gen_dominoes.py` for chain layout.
**Hints:** Endpoint weld constraints can be done by making link 0 and 39 child bodies of the world post (no joint). Friction off. Render 5 s — first 2 s settle, last 3 s show the catenary shape. Side view, pos (0, -1.8, 0.85), fovy 40.

#### ~~`swinging_chain_pendulum`~~ ✅ — Chain dynamics
**Physics:** A chain hanging from one fixed end behaves like a continuous pendulum but with internal flexibility — modes are non-trivial; it whips.
**Setup:** Chain fixed at one end, pulled to ~30° tilt, released.
**Motion:** Swings like a pendulum but with the lower end whipping noticeably.
**Template:** `dominoes.xml`. Adjust pivot.
**Hints:** ~25 links, low damping. Render 5 s.

### Bead on wire / constrained particle (4)

#### ~~`bead_on_helix`~~ ✅ — Constraint
**Physics:** A bead on a frictionless helical wire descends with combined translation+rotation; ratio of vertical drop to spiral length determines acceleration: a = g·sin(α) where α is the helix pitch angle.
**Setup:** Helix axis vertical (along +z). Generator parameters: radius R=0.06 m, pitch p=0.04 m per turn, 5 turns (total height 0.20 m). Approximate the helix with ~80 short tubular box-segments: at each parameter t ∈ [0, 5·2π], position is `(R·cos(t), R·sin(t), -p·t/(2π))`, segment is a thin box oriented along the local tangent. Bead: sphere R=0.012 m, freejoint, placed just above the top of the helix at world (R, 0, 0.01).
**Motion:** Bead falls onto the helix, slides down spiraling, exits at the bottom after ~3-4 s.
**Template:** Programmatic gen `gen_bead_on_helix.py`. Reuse curve-generation pattern from `gen_brachistochrone.py`.
**Hints:** Make the helix wire from boxes that form a thin "channel" (two parallel walls) so the bead is trapped. Friction off on both bead and helix. Bead radius 0.012 should be much smaller than helix radius 0.06 to fit. Render 4 s. 3/4 view from front-above, pos (0.3, -0.3, 0.15), fovy 38.

#### ~~`bead_on_cycloid_track_isochrony`~~ ✅ — Constraint
**Physics:** A bead on a cycloid track has the same period regardless of release point — the cycloid is the tautochrone.
**Setup:** A cycloid-shaped track (programmatic generation from cycloid equation); a bead placed at different starting positions reaches the bottom in the same time.
**Motion:** Three beads released from different positions on the cycloid; they all reach the bottom (or center) simultaneously.
**Template:** `brachistochrone.xml`. Reuse cycloid generator.
**Hints:** Multiple beads released from different heights but on the same track. Render 1.5 s (cycloid is fast). Side view.

#### ~~`bead_on_parabolic_wire`~~ ✅ — Constraint
**Physics:** A bead on a parabolic wire (z = x²) has period dependent on amplitude — contrast with cycloid's amplitude-independent period.
**Setup:** A parabolic wire (programmatic), one bead.
**Motion:** Bead oscillates back and forth; period varies with amplitude.
**Template:** `brachistochrone.xml`. Use parabolic curve instead of cycloid.
**Hints:** Render 4 s.

#### ~~`bead_in_rotating_ring`~~ ✅ — Constraint
**Physics:** A bead inside a ring that's spinning about its diameter — bead sits at an angle determined by ω, the centrifugal "potential" creating a non-trivial equilibrium.
**Setup:** A ring on a horizontal axis spinning about its diameter; a bead inside it (constrained to the ring's circular path).
**Motion:** Bead settles at an equilibrium angle on the inside of the ring. Higher ω → more horizontal position.
**Template:** `conical_pendulum.xml` + `marble.xml`.
**Hints:** Ring spins via init-qvel on its hinge. Bead's motion is constrained to the ring (geometric setup). Render 4 s. Side view.

### Curves and bowls (3)

#### `ball_in_spherical_bowl` — Oscillation
**Physics:** A ball in a spherical bowl oscillates with period independent of amplitude for small amplitudes (like a pendulum on short string).
**Setup:** A spherical bowl (a hemisphere) with a ball inside, released from one side.
**Motion:** Ball rolls back and forth in the bowl.
**Template:** `loop_the_loop.xml` (closed curved surface).
**Hints:** Build the bowl as a triangle-mesh hemisphere or as many curved segments. Or use a partial spherical capsule. Camera: 3/4 front. Render 4 s.

#### ~~`cycloidal_pendulum_huygens`~~ ✅ — Constraint / tautochrone
**Physics:** A pendulum's string wrapping around two cycloid-shaped "cheeks" forces the bob to trace a cycloid path. The resulting motion is exactly isochronous: period is independent of amplitude (unlike a normal pendulum).
**Setup:** Pivot at world (0, 0, 1.0). Two cycloid arcs (the "cheeks") flank the pivot, one on each side. Each cheek is the EVOLUTE of the path-cycloid (per Huygens). Use the parametric form `x = ±R·(θ - sin θ), z = 1.0 - R·(1 - cos θ)` for θ ∈ [0, π/2]; with R=0.20 m. Approximate each cheek with 12 short box-segments. The pendulum: massless string (tendon) of length π·R from the pivot to a bob (sphere R=0.015 m, M=0.05 kg). As the bob swings, the string wraps around the cheeks, effectively shortening — this forces the bob's path to be a cycloid.
**Motion:** Bob swings back and forth tracing a cycloid arc (visibly different from a circular pendulum arc). Period ≈ 4π·sqrt(R/g) ≈ 0.9 s, INDEPENDENT of swing amplitude.
**Template:** `pendulum.xml` (pivot + bob) + `gen_brachistochrone.py` (cycloid generator).
**Hints:** Use a tendon for the string — tendons wrap around obstacles naturally. The cheeks need contact with the tendon. Programmatic generator. Render 4 s (~4 cycles). Side view, pos (0, -1.6, 0.8), fovy 40.

#### `ball_on_saddle` — Constraint / instability
**Physics:** A saddle point (z = x² - y²) is stable in one direction, unstable in the other. A ball placed at the saddle rolls off in the unstable direction.
**Setup:** Saddle-shaped surface (z = a·x² - b·y²) with a ball placed exactly at the center.
**Motion:** Ball is stationary briefly, then with a tiny perturbation rolls off in the unstable y-direction while remaining centered in x.
**Template:** `loop_the_loop.xml` (curved geometry).
**Hints:** Approximate the saddle with many small geoms. Slight initial offset in y to seed the instability. Side view.

### Angular momentum / energy (2)

#### `skater_pulling_arms_in` — Angular momentum
**Physics:** Conservation of angular momentum — a rotating body retracting mass closer to the axis spins faster (I·ω = const).
**Setup:** A central spinning hub (vertical axis) with two arms extending horizontally. Masses are attached to the arms via slide joints; initially extended. At some point the masses are retracted (via init qpos + spring-loaded sliders) — system spins faster.
**Motion:** System spins at ω₁; arms retract; system now spins at ω₂ > ω₁.
**Template:** `conical_pendulum.xml`.
**Hints:** Tricky to model "retracting" without an actuator. Easiest: start with arms in the extended position, use slide joints with stiffness pulling them toward retracted equilibrium; release and watch them retract under their own spring tension. The conservation effect manifests automatically. Render 4 s.

#### `cradle_drop_demo` — Energy / momentum
**Physics:** A small object placed on a pendulum bob is propelled upward when the bob reaches the bottom of its swing — energy transfer demonstration.
**Setup:** A pendulum with a small block balanced on top of its bob. Release the pendulum from height.
**Motion:** Bob swings down; at the bottom of the swing, momentum transfer flicks the small block upward.
**Template:** `pendulum.xml`.
**Hints:** Carefully tuned mass ratio (~10:1 bob:block). Render 3 s.

### Resonance and waves (3)

#### ~~`standing_wave_on_string`~~ ✅ — Waves
**Physics:** Wave on a fixed-end string forms standing waves at resonance frequencies. The nodes and antinodes are visible.
**Setup:** Long discretized string with one end fixed. The other end is given a small periodic motion via init-qpos (a sinusoidal initial condition matching the lowest mode).
**Motion:** String oscillates with the visible standing-wave pattern.
**Template:** `dominoes.xml` (chain) + `spring_mass.xml`.
**Hints:** Initial qpos = sin(πx/L) gives the fundamental. Run for several periods. Render 3 s. Without actuator, only the freely-oscillating modes are visible.

#### `wave_on_chain_pulse` — Waves
**Physics:** A pulse propagates along a 1D chain of masses connected by springs. Speed depends on tension and mass density.
**Setup:** Long chain of bodies on a frictionless surface, connected by stiff hinge-springs. Initial pulse at one end (displaced upward).
**Motion:** Pulse propagates along the chain.
**Template:** `dominoes.xml` + `spring_mass.xml`.
**Hints:** Initial qpos has one peak at the start. Render 3 s.

#### `mexican_hat_drum_modes` — Waves / modes
**Physics:** A 2D mass-spring lattice (drum head analog) has discrete vibration modes — the (1,1) "Mexican hat", the (2,1), (1,2), etc. Each mode oscillates at its eigenfrequency. Here we excite the (1,1) fundamental.
**Setup:** 10×10 grid of small bodies on a square 0.20×0.20 m. Each body: sphere R=0.005 m, M=0.005 kg. Body (i,j) at world (-0.10 + i·0.022, -0.10 + j·0.022, 0.20). Each body connected to its 4 nearest neighbors via hinge-joint spring approximation. Use slide joints in z (only out-of-plane vertical motion) with `<equality>` constraints between adjacent bodies acting as springs: `<equality><joint joint1="zij" joint2="z(i+1)j" polycoef="..."/></equality>` — actually for simplicity, just use linked bodies with hinges or tendons. Edges (i=0, i=9, j=0, j=9) are fixed (no slide joint, attached to the world).
**Motion:** Initial qpos sets all bodies to `z_offset = A · sin(π·i/9) · sin(π·j/9)` with A=0.02 — the (1,1) mode shape (one big up-bump in the middle). System oscillates in pure (1,1) mode.
**Template:** Programmatic gen `gen_drum_modes.py`. Reuse from `gen_pendulum_waves.py`.
**Hints:** 10×10 = 100 bodies, manageable. Use slide joints (1 DOF each) with stiffness, not freejoints. Stiffness tuned so visible oscillation period ≈ 1 s. Render 3 s. Top-down 3/4 camera (pos 0.2, -0.2, 0.4) showing the wave shape.

### Structures (4)

#### ~~`cantilever_load_curve`~~ ✅ — Structures
**Physics:** A cantilever beam under a tip load deflects in proportion to the load (Hooke's law for the beam): δ = FL³/(3EI). Heavier load = more deflection.
**Setup:** A horizontal beam clamped at one end (like beam_buckling but horizontal). A movable load at the free end progressively gets heavier.
**Motion:** Static or quasi-static: at low load, beam barely deflects; at high load, beam visibly bends.
**Template:** `beam_buckling.xml`. Re-use the discretized beam.
**Hints:** Beam horizontal, one end pinned to a wall. Mass at tip varies (could just render 3 separate scenes or one with progressive mass via tendons). Render 2 s.

#### `truss_collapse` — Structures
**Physics:** A 2D truss is statically determinate; removing one member shifts the load through alternate paths or, if the truss becomes a mechanism, collapses entirely.
**Setup:** Triangulated 2D truss (Pratt or Warren style, ~5-7 members) holding a load. One member is "removed" (or always missing) — truss collapses.
**Motion:** Truss with all members: holds load. Without: collapses.
**Template:** `dominoes.xml` + `block_overhang.xml`.
**Hints:** Members as rigid rods connected by hinges. Programmatic generator. Render 3 s.

#### `inverted_pendulum_tower` — Stability
**Physics:** A tower of inverted pendulums (each hinged on the one below) is unstable — any small perturbation grows.
**Setup:** Stack of N inverted pendulums (link-on-link, each a hinge with stiffness but high amplitude). Small initial tilt.
**Motion:** Tower wobbles initially, then collapses in some direction.
**Template:** `beam_buckling.xml`.
**Hints:** Set hinge stiffness so it's below the buckling-stability threshold. Render 3–4 s.

#### `crane_lifting_simple` — Structures / mechanism
**Physics:** A simple crane (arm + cable + load) demonstrates torque on the base; tipping happens if load·arm-extension > base-weight·base-half-width.
**Setup:** A pivoting vertical pole with a horizontal arm extending out; a cable hanging from the arm tip; a load on the cable.
**Motion:** Without enough base mass, the crane tips forward when the load is hung. With enough, it stays.
**Template:** Custom; use `block_overhang.xml` ideas.
**Hints:** Visualize the load's weight and the crane's stability margin. Render 3 s.

---

## 🟢 Tier 1 — Final additions (10 more, brainstormed in round 2)

### Equilibrium / instability (4)

#### `cone_balanced_on_tip` — Statics / instability
**Physics:** A cone balanced perfectly on its apex is in unstable equilibrium; any infinitesimal perturbation causes it to fall.
**Setup:** Cone shape (build from cylinder + capsule cap or use a cone-shaped geom). Cone height 0.20 m, base radius 0.06 m. M=0.10 kg. Place upside-down with apex on floor at world (0, 0, 0.20). Initial qpos: tiny tilt (~0.5° about y-axis, i.e. quaternion (1, 0, 0.004, 0)). Floor friction `friction="0.8 0.01 0.001"`.
**Motion:** Cone holds steady for ~0.3 s, then starts tilting visibly, falls completely by 1.5-2 s.
**Template:** `spinning_top.xml` (free body + floor) + `dominoes.xml` (tilt seed).
**Hints:** This is just unstable equilibrium — gravity does the rest. Camera: side view, pos (0, -0.6, 0.15), fovy 38. Render 2.5 s.

#### ~~`symmetry_breaking_ball_on_dome`~~ ✅ — Statics / instability
**Physics:** A ball at the very top of a smooth dome is in unstable equilibrium; tiny perturbations make it slide off, eventually flying through air.
**Setup:** A semi-spherical dome of radius R=0.20 m, half-sphere shape built from many small triangular boxes or a single half-ellipsoid geom positioned at world (0, 0, 0.20). Ball: sphere R=0.015 m, M=0.05 kg, placed on top at (0, 0, 0.215). Initial qpos: tiny horizontal offset (Δx=0.001). Friction zero.
**Motion:** Ball stays nearly still for ~0.5 s, then slides off the dome accelerating to the side, then flies through the air after losing dome contact.
**Template:** `loop_the_loop.xml` (for curved surface).
**Hints:** Dome can be approximated by half of a high-poly sphere or by stacked rings. Render 2 s. Camera: side view, pos (0.5, -0.5, 0.15), fovy 40.

#### `marble_in_funnel` — Gravity / circular motion
**Physics:** A marble released inside a funnel (cone with vertical axis) spirals down, accelerating as the radius decreases — angular momentum NOT conserved (gravity does work) but visually striking.
**Setup:** Funnel: inverted cone shape, top radius 0.15 m, bottom hole radius 0.01 m, height 0.20 m. Built programmatically from ~24 box segments forming the conical wall. Marble: sphere R=0.008 m, M=0.005 kg, placed at the top edge (R=0.14, z=0.20) with initial tangential velocity vt=0.5 m/s.
**Motion:** Marble spirals down the funnel wall, speeding up as the radius decreases; exits the bottom or oscillates at the throat.
**Template:** Programmatic gen (`gen_funnel.py`). Reuse pattern from `gen_rotating_fluid.py` for ring-of-walls.
**Hints:** Marble friction tuned for low slip on the funnel wall (`friction="0.05 0.005 0.001"`). Camera 3/4 from above, pos (0.25, -0.25, 0.30), fovy 38. Render 4 s.

#### ~~`falling_chimney`~~ ✅ — Rotational / rigid body
**Physics:** A tall vertical rod pinned at the base falls over by rotating about the base. The TIP accelerates faster than g during part of the fall — counter-intuitive demonstration of how internal stresses redistribute (real chimneys often break mid-fall because of this).
**Setup:** Single rigid rod: a thin box of length 1.0 m, half-extents (0.025, 0.025, 0.5), M=2 kg. Bottom end pinned at world (0, 0, 0) via a hinge joint with axis y, no stiffness. Initial qpos: 2° tilt about y to seed the fall. No damping.
**Motion:** Rod falls over rotating about its base. Tip's vertical velocity exceeds free-fall during the second half of the trajectory (~30° to 60° from vertical).
**Template:** `pendulum.xml` (single rod on hinge).
**Hints:** Compare the tip's z-velocity to g·t to verify the >g effect. Render 1.5 s. Side view, pos (1.5, -1.0, 0.5), fovy 40.

### Coupling & action-reaction (3)

#### ~~`block_on_accelerating_wedge`~~ ✅ — Action-reaction
**Physics:** A block on a frictionless wedge that can itself slide on a frictionless floor — when released, both bodies accelerate. The wedge slides one way as the block slides down it; momentum in x conserved.
**Setup:** Wedge: triangular prism, 30° incline, base 0.40 m × 0.10 m, height 0.20 m at the high end. M_wedge=1.0 kg. Wedge sits on a slide joint along world x. Block: cube 0.05 m, M_block=0.3 kg, sits on the slope of the wedge, constrained to slide on it via slide joint along the slope direction.
**Motion:** Block accelerates down the slope; wedge accelerates in the opposite direction. The combined center of mass stays fixed in x.
**Template:** `incline_friction.xml` (block-on-wedge) + add a slide joint for the wedge.
**Hints:** Set ALL friction to 0 (gotcha #1). Render 1.5 s. Add a vertical marker line at the initial x of the combined COM to make conservation visually obvious. Side view, fovy 38.

#### ~~`two_pendulums_collide`~~ ✅ — Collision + oscillation
**Physics:** Two pendulums released from opposite sides meet at the bottom and collide elastically; momentum transfer depends on mass ratio.
**Setup:** Two single pendulums side-by-side (small lateral offset so they meet at the bottom). Left: length 0.40 m, mass 0.10 kg, released from 30° (positive angle). Right: length 0.40 m, mass 0.10 kg, released from -30° (negative angle), with a tiny y-offset (0.001) so geoms don't tangle.
**Motion:** Both pendulums swing toward each other; collide at the bottom with equal-mass elastic collision (essentially swap velocities); each bounces back to near-original height.
**Template:** `pendulum.xml` (duplicate) + `elastic_collision.xml` (stiff contact tuning).
**Hints:** Use stiff contact (`solref="-150000 -15"` `solimp="0.99 0.999 0.001"`) for clean elastic transfer (gotcha #4). Render 3 s (two full swings). Side view.

#### ~~`pulley_with_inertia`~~ ✅ — Constraint / rotational
**Physics:** Atwood machine where the pulley has significant moment of inertia — the pulley's I REDUCES the acceleration: a = (m1-m2)·g / (m1 + m2 + I/r²). Pulley I shows up as effective mass.
**Setup:** Same as Atwood but the pulley is a heavy disc (R=0.10 m, thickness 0.02 m, M=0.5 kg) — NOT massless. Pulley rotates via a hinge joint with no damping. The rope is two tendons (one each side) attached to the pulley via sites at radius R; the rope coupling to the pulley rotation enforces no-slip via joint-equality (combination of slide joints + hinge equality).
**Motion:** Heavier mass descends, lighter ascends — but more slowly than ideal Atwood predicts because of the pulley's I.
**Template:** `atwood.xml` (Atwood structure) + `maxwell_wheel.xml` (rolling-without-slip equality).
**Hints:** Connection: two equalities, one per side, each coupling rope-slide to pulley-hinge. Or simpler: ONE equality between (heavy_slide - light_slide) and (pulley_hinge · R). Mass ratio: 0.6 / 0.4 kg gives clean visible acceleration. Render 3 s. Side view.

### Friction & contact (3)

#### ~~`block_on_block_static_friction`~~ ✅ — Friction
**Physics:** Two stacked blocks on a frictionless floor; pull the bottom block. If μ_static between blocks is high enough, the top block moves WITH the bottom (no slip). If μ exceeded, top stays while bottom slides out.
**Setup:** Bottom block: 0.20 × 0.10 × 0.05 m, M=1 kg, sitting on a frictionless floor, with slide joint along x. Top block: 0.10 × 0.10 × 0.05 m, M=0.2 kg, placed centered on top, also with a slide joint along x. Inter-block contact has μ_static = 0.4. Apply a horizontal initial velocity to the bottom block (vx=1.0 m/s, large enough to slip).
**Motion:** Bottom block slides; top block stays nearly still for a moment, then accelerates due to friction; eventually they share velocity (or stay apart depending on initial velocity).
**Template:** `incline_friction.xml` (stacked geoms) + `elastic_collision.xml` (sliders).
**Hints:** Set floor friction to 0 (gotcha #1). Top block's slide joint allows it to be left behind. Render 2 s. Side view, pos (0, -1.0, 0.15), fovy 40.

#### `vertical_loop_insufficient_speed` — Energy / centripetal
**Physics:** A ball on a vertical loop track needs minimum speed `v_min = sqrt(g·R)` at the top to maintain contact. With less, it falls off the track partway up.
**Setup:** Closed vertical loop track (radius 0.20 m) — same geometry as `loop_the_loop.xml`. Ball: sphere R=0.025 m, M=0.05 kg. Initial position at the bottom of the loop; initial qvel = small (vx=1.5 m/s — too slow to make it around).
**Motion:** Ball ascends the loop on the inside surface; somewhere past 90° (when gravity component exceeds centripetal requirement), the ball loses contact with the track and falls inward.
**Template:** `loop_the_loop.xml`. Reduce initial speed.
**Hints:** Compare to `loop_the_loop` which uses enough speed. Render 1.5 s. Same camera as loop_the_loop.

#### ~~`spherical_pendulum_2d`~~ ✅ — Oscillation
**Physics:** A pendulum with 2D bob motion (instead of constrained to a plane) traces complex Lissajous-like patterns. Period not necessarily commensurate, so trajectory can be quasi-periodic.
**Setup:** Single bob hung from a pivot at world (0, 0, 1.2) via a 2-DOF gimbal: outer hinge axis y (pitch), inner hinge axis x (roll) — see gotcha #8 for why this is better than a ball joint. Bob: sphere R=0.025 m, M=0.10 kg, at the end of a 0.6 m rod from pivot. Initial qpos: pitch=0.5 rad, roll=0; init-qvel: roll_rate=0.8 rad/s.
**Motion:** Bob traces a rosette pattern in the xy plane (as projected) — not a circle, not a flat line.
**Template:** `conical_pendulum.xml` (gimbal pattern).
**Hints:** Use a long render (10 s) so the pattern becomes visible. Top-down camera, pos (0, 0, 0.4), xyaxes="1 0 0  0 1 0", fovy 42.

---

## 🟡 Tier 1/2 — Round 2 additions (F and G packages, 34 more)

### Classic energy / motion demos (5)

#### ~~`galileo_pendulum_peg`~~ ✅ — Energy conservation
**Physics:** A pendulum swung from a height rises to the SAME height on the other side, even if a peg in the path shortens the effective length mid-swing.
**Setup:** Pivot at world (0, 0, 1.0); rigid string (length 0.6 m, modelled as a tendon) to a bob (sphere R=0.025 m, M=0.05 kg). Fixed peg at world (0, 0, 0.7). Initial pose: bob pulled back to angle 60° from vertical on the left side.
**Motion:** Bob swings down, string contacts the peg, effective swing length shortens to 0.30 m, bob now swings about the peg, rises to the same height as it started.
**Template:** `pendulum.xml` (basic pendulum) + `cradle_drop_demo.xml`.
**Hints:** Tendon wraps naturally around the peg. Mark the original height with a thin horizontal line for visual proof. Side view, pos (0, -1.5, 0.7), fovy 38. Render 3 s.

#### ~~`horizontal_vs_dropped_balls`~~ ✅ — Independence of motion
**Physics:** Horizontal motion is independent of vertical free fall: two balls dropped from the same height — one pushed horizontally, one not — hit the ground simultaneously.
**Setup:** Two balls at world (0, 0, 1.0), each sphere R=0.025 m, M=0.05 kg, with freejoints. Ball A: init-qvel zero. Ball B: init-qvel "1.5 0 0 0 0 0" (horizontal kick).
**Motion:** Ball A falls straight down; Ball B traces a parabola landing 1m+ to the side. Both touch the floor at the same instant (t = √(2·1.0/9.81) ≈ 0.45 s).
**Template:** `galileo_dropballs.xml`.
**Hints:** Side view, pos (0.7, -1.5, 0.5), fovy 38 — frame both initial position AND ball B's landing point. Render 0.6 s.

#### ~~`rolling_disc_inscribes_cycloid`~~ ✅ — Trajectory geometry
**Physics:** A point on the rim of a rolling disc traces a cycloid in space — the curve that originally motivated cycloid mathematics.
**Setup:** Disc R=0.10 m, thickness 0.02 m, M=0.5 kg, rolling on the floor (init-qvel: vx=0.6, ω_y=-6 for rolling-without-slip). A small bright marker (sphere R=0.005 m) welded to the disc at one point on the rim.
**Motion:** Disc rolls; marker traces high arches (cycloid), touching the ground at intervals.
**Template:** `rolling_race.xml` + `maxwell_wheel.xml`.
**Hints:** Side view, pos (1.5, -2.0, 0.3), fovy 38. Render 4 s — 2-3 cycloid arches.

#### ~~`bucket_of_water_overhead_swing`~~ ✅ — Vertical circular motion
**Physics:** A bucket swung in a vertical circle keeps its contents inside even at the top (upside-down moment) as long as centripetal acceleration > g.
**Setup:** Pivot at world (0, 0, 1.0). Rigid rod (length 0.5 m, NOT a tendon — tendon would go slack at top) ending in a "bucket" (an open-top 5-sided box, 0.10 × 0.10 × 0.10 m). Inside the bucket: a free ball (R=0.025 m, M=0.05 kg). Arm initial qvel: ω=4 rad/s.
**Motion:** Bucket sweeps a full vertical circle (or two). Ball stays inside even when upside-down at the top.
**Template:** `pendulum.xml` + `conical_pendulum.xml`.
**Hints:** Arm must be RIGID (use a rigid hinge-connected body, not tendon). Ball free inside the cup. Render 3 s (1 full circle).

#### ~~`two_marbles_curved_track_collision`~~ ✅ — Energy + collision
**Physics:** Two marbles in a frictionless U-shaped track oscillate, meet at the bottom with equal speeds, elastically collide (swap velocities), and oscillate again — perpetual motion (ideally).
**Setup:** U-shaped parabolic track (`z = 0.4·x²` for x ∈ [-0.4, 0.4]), built from ~20 box segments via programmatic gen. Two marbles (R=0.02 m, M=0.04 kg) placed at the rim on opposite sides; both released from rest.
**Motion:** Slide down → meet at bottom → elastic collision → scatter back to original heights → repeat.
**Template:** `brachistochrone.xml` (curved track) + `elastic_collision.xml` (stiff contact).
**Hints:** Marble friction zero. Stiff contact (solref="-200000 -20"). Render 4 s — multiple oscillations. Side view, pos (0, -1.5, 0.4), fovy 40.

### Mechanisms (4)

#### ~~`planetary_gear_train`~~ ✅ — Mechanism
**Physics:** Planetary gear system: sun + 3 planets + ring. Driving the sun makes planets rotate AND orbit; ring stays still. Demonstrates how complex gear ratios arise.
**Setup:** Sun gear: cylinder R=0.04 m at world (0, 0, 0.1) on a hinge. 3 planet gears: cylinders R=0.025 m at world (0.065, 0, 0.1) and 120° rotations, each on a hinge attached to a "planet carrier" body. Ring gear: hollow cylinder, inner R=0.115 m, outer R=0.13 m, fixed to world. Joint-equalities couple sun-to-planet and planet-to-ring as `ω_sun · R_sun = -ω_planet · R_planet` (and similar for ring).
**Motion:** Sun spins (init-qvel ω=4 rad/s); planets rotate AND orbit; ring stays still.
**Template:** `maxwell_wheel.xml` (rolling-without-slip equality).
**Hints:** Use joint equalities, not real gear teeth. Top-down view, pos (0, 0, 0.5), xyaxes="1 0 0  0 1 0", fovy 38. Render 3 s.

#### ~~`gear_train_2_gears`~~ ✅ — Mechanism
**Physics:** Two meshed gears: angular velocities related by gear ratio (ω_a · R_a = -ω_b · R_b), opposite directions.
**Setup:** Two cylinder gears: A (R=0.06 m) at world (-0.07, 0, 0.1), B (R=0.10 m) at world (0.09, 0, 0.1), each on a hinge about z. Joint equality: `<equality><joint joint1="gear_a" joint2="gear_b" polycoef="0 -0.6 0 0 0"/></equality>` (ratio R_a/R_b=0.6). Gear A initial qvel ω=5 rad/s.
**Motion:** A spins; B counter-rotates at 0.6× A's speed.
**Template:** `maxwell_wheel.xml`.
**Hints:** Top-down, fovy 40. Mark a colored dot on each gear so the speed ratio is visible. Render 3 s.

#### ~~`four_bar_linkage`~~ ✅ — Mechanism
**Physics:** Four bars in a closed loop (ground + crank + coupler + rocker) — driving the crank in continuous rotation makes the rocker oscillate. Classic mechanism (e.g., oil pump jacks, windshield wipers).
**Setup:** 4 rigid bar bodies joined by 4 hinge joints in a closed quadrilateral. Lengths: ground 0.20, crank 0.05, coupler 0.20, rocker 0.15 (satisfies Grashof condition for full rotation). Ground bar fixed to world; crank driven by init-qvel ω=4 rad/s.
**Motion:** Crank rotates uniformly; rocker swings back and forth; coupler bar's midpoint traces a "coupler curve" (complex closed shape).
**Template:** `slider_crank_mechanism.xml` (similar mechanism with crank).
**Hints:** Use four hinge joints forming a loop — MuJoCo handles closed loops via constraint. Side view. Render 4 s.

#### ~~`ratchet_pawl`~~ ✅ — Mechanism
**Physics:** A toothed wheel + spring-loaded pawl that locks rotation in one direction only. Forward: pawl clicks over teeth. Backward: pawl catches a tooth and locks.
**Setup:** Wheel R=0.10 m with 12 saw-tooth teeth (each tooth: angled box on the rim). Pawl: small lever hinged to a fixed frame, spring-loaded (joint stiffness) so it presses on the rim. Wheel given init-qvel ω in the "allowed" direction (ratchets freely) — for the "blocked" version, give ω in the other direction (immediately locks).
**Motion:** Allowed direction: wheel rotates freely, pawl clicks over teeth. Blocked: wheel rotates ~5° then locks.
**Template:** Programmatic gen `gen_ratchet.py`. Reuse from `gen_dominoes.py` for tooth layout.
**Hints:** Render two variants if desired, or one render that reverses direction at t=1.5 s. Top-down camera. Render 3 s.

### Chain / pile dynamics (3)

#### ~~`chain_jet_classic`~~ ✅ — Self-propelled chain
**Physics:** A chain in a container, with one end pulled up, develops a self-propelled "fountain" — the falling chain pulls more chain out, accelerating. The chain arches above the container.
**Setup:** Cylindrical "beaker" (R=0.05 m, H=0.10 m) on a table. ~50 small chain links piled inside. Topmost link given small upward initial velocity (vz=2 m/s).
**Motion:** Chain begins falling out; arch forms above the beaker; chain continuously feeds itself.
**Template:** `dominoes.xml` (chain) + `rotating_fluid.xml` (container).
**Hints:** Hard — pile geometry is finicky. Programmatic gen. Render 3-4 s. Side view, pos (0.5, -1.0, 0.2), fovy 40.

#### ~~`chain_unspooling_from_pile`~~ ✅ — Self-feeding chain
**Physics:** A chain piled on the floor, with one end pulled up — the chain accelerates as more length is lifted (less mass remains stationary). Tension at the pile-junction pulls more chain out.
**Setup:** ~40 chain links initially piled at world (0, 0, 0.05). Topmost link given a small lift (initial qpos at z=0.15, with downward velocity zero).
**Motion:** Pile feeds chain upward and out, accelerating over time.
**Template:** `dominoes.xml`.
**Hints:** Programmatic gen for the initial loose stack. Side view. Render 3-4 s.

#### ~~`chain_on_scale_falling`~~ ✅ — Impact dynamics
**Physics:** A chain falling onto a scale — the scale reading is HIGHER than the static weight of the deposited chain during the fall, because falling links transfer impact momentum.
**Setup:** Chain (~30 links, each M=0.01 kg) initially suspended just above a fixed plate ("the scale"). Release.
**Motion:** Chain falls onto the scale segment by segment; visible impact dynamics; total deposited weight grows linearly while impact force adds extra peak force.
**Template:** `dominoes.xml` + `bowling.xml`.
**Hints:** Programmatic gen. Render 2 s. Side view.

### Friction / mechanical (3)

#### ~~`triple_block_friction_chain`~~ ✅ — Friction
**Physics:** Three stacked blocks on a frictionless floor — push the bottom block. Depending on inter-block μ, all three move together, or top blocks slip behind.
**Setup:** 3 boxes stacked vertically, each on a slide joint along x. Bottom block (M=2 kg) given init-qvel vx=2 m/s. Inter-block friction: μ=0.3 between bottom-middle, μ=0.5 between middle-top.
**Motion:** Bottom accelerates fast; top and middle blocks lag (limited by friction); over a short time they catch up.
**Template:** `incline_friction.xml` + `block_on_block_static_friction.xml`.
**Hints:** Floor friction zero (gotcha #1). Render 2.5 s. Side view, pos (0, -1.0, 0.15), fovy 40.

#### ~~`two_bodies_on_incline_string`~~ ✅ — Friction + constraint
**Physics:** Two blocks on an incline connected by a string. If they have different μ, internal string tension develops; they slide as a unit at an intermediate speed.
**Setup:** Inclined ramp at 25°. Two blocks on it (separated 0.15 m along the slope), connected by a tendon. Block A (uphill): μ=0.1 (low). Block B (downhill): μ=0.4 (high).
**Motion:** Both blocks slide down at the same speed (locked by the string); intermediate between their solo speeds.
**Template:** `incline_friction.xml` + `atwood.xml` (tendon).
**Hints:** Tendon visible. Side view, pos (1.0, -1.5, 0.3), fovy 40. Render 3 s.

#### `pulled_block_string_around_peg` — Redirect force
**Physics:** A string going around a fixed peg redirects the pulling direction without changing magnitude (if frictionless). A vertical pull lifts a horizontal block.
**Setup:** Heavy block (M=1 kg) on a frictionless floor with a slide joint along x. Tendon from the block goes UP around a fixed peg at world (0.5, 0, 0.5), then HORIZONTAL to a downward-falling counterweight (M=0.5 kg) on a slide joint along z.
**Motion:** Counterweight falls; string pulls block; block slides horizontally as counterweight descends.
**Template:** `atwood.xml` + `capstan_effect.xml`.
**Hints:** Tendon wraps naturally. Side view. Render 3 s.

### Constraint / coupled motion (4)

#### ~~`double_atwood`~~ ✅ — Constraint
**Physics:** Atwood machine where one of the two masses is itself an Atwood machine. Three masses, complex coupled dynamics.
**Setup:** Top pulley at world (0, 0, 1.5). Left side: heavy mass M_h = 0.8 kg on a slide joint. Right side: a second pulley at world (0.3, 0, 0.9) (hanging on the right rope), with two masses m1=0.3 kg, m2=0.2 kg on slide joints below it. Joint equalities couple slides.
**Motion:** All 3 masses move; left mass goes down or up depending on net imbalance; right side masses also move relative to each other.
**Template:** `atwood.xml`.
**Hints:** Two joint equalities chained. Render 3-4 s.

#### `wheel_with_pendulum_inside` — Coupled rotation/pendulum
**Physics:** A wheel rolling on the floor with a pendulum mounted at its center — wheel acceleration drives pendulum swing; coupled dynamics.
**Setup:** Hollow cylinder (wheel) R=0.15 m rolling on the floor. Inside the wheel: a thin rod (pendulum, length 0.10 m, mass 0.05 kg) pivoted at the wheel's axle, free to swing. Wheel given initial rolling velocity.
**Motion:** Wheel rolls; pendulum swings due to wheel's transient acceleration; over time, pendulum's swing decays.
**Template:** `rolling_race.xml` + `conical_pendulum.xml`.
**Hints:** Hollow wheel via thin ring of geoms. Render 3 s. Side view.

#### `catenary_with_central_load` — Statics
**Physics:** A catenary chain with a heavy weight at the midpoint — the chain forms a V-shape (two straight segments) instead of a smooth cosh.
**Setup:** Same as `hanging_chain_catenary` but a heavy mass (M=0.5 kg) attached to the central link.
**Motion:** Chain settles to V-shape; midpoint hangs much lower than usual.
**Template:** `hanging_chain_catenary.xml`.
**Hints:** Render 5 s — last 3 s show the V. Side view.

#### `pulley_chain_loop` — Mechanism
**Physics:** Closed chain loop around two pulleys (like a tank tread laid flat). Drive one pulley → loop circulates continuously.
**Setup:** Two pulleys (R=0.05 m) at fixed positions 0.3 m apart. Closed chain (~30 links) wrapped around both. One pulley has initial qvel ω=3 rad/s.
**Motion:** Loop circulates around the two pulleys continuously.
**Template:** `belt_friction.xml` + `dominoes.xml`.
**Hints:** Programmatic gen for the loop. Render 3 s.

### Mass / drag / various (4)

#### `two_balls_drop_with_different_drag` — Drag
**Physics:** Two balls of the same mass dropped from the same height — one with low air drag, one with high — fall at different rates.
**Setup:** Two balls (each M=0.05 kg) at world (0, 0, 1.0). Ball A: sphere R=0.02 m. Ball B: larger sphere R=0.06 m (more drag). Both freejoints. Use joint damping (linear) as drag proxy. Drop both.
**Motion:** A reaches the floor first; B reaches later (a couple frames behind).
**Template:** `galileo_dropballs.xml`.
**Hints:** MuJoCo has no native air drag — use linear joint damping on each freejoint to mimic. Side view. Render 1.2 s.

#### `block_rolls_off_curved_hill` — Energy → projectile
**Physics:** Block at the top of a smooth curved hill slides down by gravity, then becomes a projectile when the hill ends.
**Setup:** Curved hill: a "ramp-then-cliff" shape (smooth slope going down, then a sharp drop to flat ground). Block placed at the top, friction zero.
**Motion:** Block slides down the slope, reaches the cliff edge, flies off as a projectile, lands somewhere ahead on the ground.
**Template:** `brachistochrone.xml` + `bowling.xml`.
**Hints:** Programmatic gen for the hill shape. Render 1.5 s.

#### ~~`rolling_dumbbell`~~ ✅ — Rolling / inertia
**Physics:** A dumbbell (two balls on a rod) on a flat floor doesn't roll uniformly — it tumbles end-over-end, alternating between resting on each ball.
**Setup:** Two spheres (R=0.04 m, M=0.1 kg each) connected by a thin rod (length 0.15 m, M=0.02 kg). Free body on the floor; initial qvel includes both translation (vx=0.3) and rotation.
**Motion:** Dumbbell rolls partially, then tumbles end-over-end, then rolls, then tumbles — characteristic gait.
**Template:** `rolling_race.xml`.
**Hints:** Floor friction tuned for rolling. Side view. Render 4 s.

#### ~~`galileo_inclined_plane_squared`~~ ✅ — Distance ~ t²
**Physics:** Ball rolling down a frictionless incline travels distances proportional to t² — passes the d=1,4,9,16 marks at t=1,2,3,4 (in any units).
**Setup:** Long inclined ramp (length 1.0 m, angle 10°). Ball at top. Place 4 visible colored markers at positions corresponding to 1, 4, 9, 16 (scaled) along the ramp.
**Motion:** Ball accelerates down; passes the 4 markers at predicted time intervals (1, 2, 3, 4 in some unit).
**Template:** `marble.xml`.
**Hints:** Friction near zero. Side view. Render 4 s.

### Rotating frame / dynamics (4)

#### `ball_in_rotating_dish_equilibrium` — Rotating frame
**Physics:** A ball in a parabolic dish spinning at constant ω settles at a radius where centrifugal "gravity" balances the dish's slope (a stable orbit).
**Setup:** Parabolic dish (`z = 4·r²` for r ∈ [0, 0.15]) rotating about its vertical axis at ω=6 rad/s. Ball (R=0.012, M=0.01 kg) inside, initial position near the rim with tangential velocity matching the dish.
**Motion:** Ball orbits with the dish at an equilibrium radius.
**Template:** `rotating_fluid.xml` (rotating container).
**Hints:** Dish via programmatic gen. Heavy dish bottom. Render 5 s. 3/4 camera from above.

#### `dropping_ball_on_rotating_disc` — Friction + centrifugal
**Physics:** Ball dropped onto a fast-spinning disc — friction briefly imparts angular velocity, then centrifugal force throws the ball off tangentially.
**Setup:** Spinning disc (R=0.20 m, ω=15 rad/s on a fixed hinge). Ball (R=0.025, M=0.05 kg) dropped from 0.5 m above the disc center.
**Motion:** Ball hits disc, briefly co-rotates, then slides off radially.
**Template:** `rotating_fluid.xml` + `bowling.xml`.
**Hints:** High disc-ball friction. Side view. Render 1.5 s.

#### `bead_on_rotating_horizontal_rod` — Centrifugal
**Physics:** A bead on a horizontal rod that's spinning — without anything to provide centripetal force along the rod, the bead slides outward and flies off the end.
**Setup:** Horizontal rod hinged at its center (axis z), spinning at ω=3 rad/s. Bead on a slide joint along the rod (initial offset 0.02 m from center).
**Motion:** Bead slides outward along the rod, accelerating; eventually flies off the end.
**Template:** `bead_on_helix.xml` + `conical_pendulum.xml`.
**Hints:** Rod must be horizontal (gravity normal to it). Render 2.5 s. Top-down camera.

#### `rotor_wheel_off_axis_wobble` — Imbalance
**Physics:** A wheel with its center of mass offset from its rotation axis wobbles as it spins. Whole system vibrates.
**Setup:** Wheel (R=0.10 m) with its axle going through a point offset 0.025 m from the wheel's true center. Axle on a hinge with init-qvel ω=10 rad/s.
**Motion:** Wheel spins, but visibly wobbles up-and-down (the offset center swings around the axle).
**Template:** `maxwell_wheel.xml` + `spinning_top.xml`.
**Hints:** Use `<inertial>` to position the COM off-center. Side view. Render 3 s.

### Multi-body / structures (4)

#### `three_pendulums_synced_via_support` — Synchronization (Huygens)
**Physics:** Three pendulums on a flexible support (the support itself can move) synchronize in phase over time — Huygens-style coupling through the support's small motion.
**Setup:** Horizontal bar (M=0.5 kg) hanging on two strings (the support, which can swing). Three pendulums (each length 0.30 m, M=0.10 kg) hanging from the bar at evenly spaced points. Initial pendulum angles: 30°, 0°, -30° (out of phase).
**Motion:** Bar's small motion couples the pendulums; over many oscillations, they synchronize to all swing in phase.
**Template:** `pendulum_waves.xml` + `coupled_pendulums.xml`.
**Hints:** Bar needs nonzero mass but small relative to pendulums. Render 20 s (sync takes time). Side view.

#### `chain_swing_collision_target` — Flexibility + collision
**Physics:** A flexible chain pendulum swung into a target hits with the bottom link's whip-effect velocity — higher than a rigid pendulum of the same length.
**Setup:** Chain (~15 links) pivoted at the top, hanging vertically. Bottom link is a heavier "tip". Pulled to 60° and released. A stationary target block at the chain's lowest point.
**Motion:** Chain whips down, bottom link strikes target with whip velocity, target moves off.
**Template:** `dominoes.xml` + `projectile_jenga.xml`.
**Hints:** Render 2.5 s. Side view.

#### `billiard_break_setup` — 2D multi-body collision
**Physics:** A cue ball striking a triangular rack of 10 balls — classic 2D elastic scatter. Energy and momentum redistribute over many bodies.
**Setup:** 10 balls in a triangular pack (4-3-2-1 rows) on a frictionless table. Cue ball positioned 0.3 m away, init-qvel toward the front ball at 2 m/s.
**Motion:** Cue ball strikes; 10-ball rack scatters in a characteristic pattern.
**Template:** `elastic_collision.xml` + `n_body_1d_collisions.xml`.
**Hints:** Top-down camera. Stiff contacts. Render 3 s.

#### `walking_robot_passive_slope` — Passive walking
**Physics:** A 2-legged "biped" with no actuators on a gentle slope — gravity drives walking; swing leg falls forward, plants, switch sides.
**Setup:** Two rigid legs (length 0.4 m, M=0.3 kg each) hinged at a common hip joint. Place on a 5° slope. Initial pose: one leg planted, other leg swung back.
**Motion:** Walker takes 3-5 passive steps down the slope before falling.
**Template:** `triple_pendulum.xml` (link chain).
**Hints:** Slope angle critical (4-7° works); too steep → falls; too shallow → no walk. Render 4 s. Side view.

### Door / dispersion (3)

#### `swinging_door` — Compound pendulum
**Physics:** A door (rectangular plate) hinged on one edge — its swing period depends on moment of inertia, larger than a point-mass pendulum of equivalent length.
**Setup:** Plate dims 0.8 m × 0.6 m × 0.02 m, M=2 kg. Hinged on one vertical edge (axis z). Initial pose: door open 90°. Damping low.
**Motion:** Door swings closed under gravity, oscillates back-and-forth (large period due to extended I).
**Template:** `pendulum.xml` + `compound_pendulum_shapes.xml`.
**Hints:** Top-down camera (door swings in horizontal plane). Render 5 s.

#### `dripping_chain_through_bottleneck` — Chain through hole
**Physics:** A chain piled on a horizontal plate falls through a small hole; the falling portion accelerates as more chain joins it.
**Setup:** Horizontal plate at world (0, 0, 0.3) with a small hole at the center. Chain (~40 links) piled on top of the plate, with the bottom of the chain through the hole.
**Motion:** Chain falls through the hole; accelerating downward as more falls in.
**Template:** `dominoes.xml`.
**Hints:** Programmatic gen for the chain pile + hole geometry. Render 2 s.

#### `chain_around_corner_table_edge` — Static friction
**Physics:** A chain laid over a table edge — part on table, part hanging — stays static if friction is high enough; slides otherwise. Critical fraction is determined by chain-table μ.
**Setup:** Chain (~30 links, each M=0.01 kg) laid flat on a tabletop with the last few links hanging off the edge. Chain-edge friction μ=0.4.
**Motion:** Chain stays static (or, with longer overhang, starts sliding).
**Template:** `falling_chain_classical.xml`.
**Hints:** Tune the overhang fraction to balance friction. Render 3 s.

---

## 🔵 Tier 1/2 — Round 3 additions (H and I packages, 34 more)

### Rotation / gimbal / gyroscope (4)

#### `gimbal_rings_3axes` — Rotational DOF
**Physics:** Three nested gimbals provide three independent rotational DOFs; when two axes align, "gimbal lock" reduces effective DOF to 2.
**Setup:** Outer ring (R=0.20 m) hinged to a fixed stand, axis z. Inner ring (R=0.15 m) hinged to outer, axis y. Innermost ring (R=0.10 m) hinged to inner, axis x. Small rotor inside the innermost ring. Initial qvel: each ring 1-2 rad/s on its own axis.
**Motion:** All three rings rotate independently. If you tune initial conditions, you can show gimbal lock (when two axes coincide).
**Template:** `spinning_top.xml` + `conical_pendulum.xml` (gimbal pattern).
**Hints:** Programmatic gen for the rings. Side view. Render 5 s.

#### `torsion_pendulum` — Rotational oscillation
**Physics:** A disc suspended by a wire that resists twisting oscillates torsionally; period T = 2π·sqrt(I/κ) where κ is the torsion constant.
**Setup:** Disc R=0.08 m, M=0.15 kg, hung from a single hinge axis pointing up. Hinge has stiffness κ=0.02 N·m/rad, damping=0.005. Initial qpos: disc twisted to 60°.
**Motion:** Disc rotates back-and-forth about the vertical axis, period ~2 s, slowly decaying.
**Template:** `pendulum.xml` (oscillation pattern).
**Hints:** Render 8 s — multiple periods. Top-down camera, fovy 40.

#### `l_handle_rotation_inertia` — Inertia tensor
**Physics:** An L-shaped rigid body has different moments of inertia about its three principal axes. Spinning about different axes shows visibly different dynamics.
**Setup:** L-shape made of two perpendicular rods (each 0.20 m × 0.02 m × 0.02 m). Freejoint, gravity off. Apply init-qvel: angular velocity along (a) the long arm axis, (b) the short arm axis, (c) the perpendicular axis. Render 3 versions OR one with the intermediate-axis instability.
**Motion:** Spinning about extreme axes: stable rotation. Spinning about intermediate axis: tumbles (similar to Dzhanibekov).
**Template:** `dzhanibekov_effect.xml`.
**Hints:** Use `<option gravity="0 0 0"/>`. Render 4 s.

#### `gyroscope_pendulum_3d_motion` — Coupled gyro + pendulum
**Physics:** A spinning gyroscope attached to a pendulum-like hanging rod — combined motion has both gyroscopic precession and pendulum swing.
**Setup:** Vertical rod (length 0.4 m) hung from a pivot via a hinge with axis y; at its bottom, a fast-spinning disc (R=0.10 m, ω=30 rad/s about disc's own axis). Pull pendulum to 30° angle and release.
**Motion:** Bob swings as a pendulum AND the gyro precesses — combined 3D motion.
**Template:** `pendulum.xml` + `spinning_top.xml`.
**Hints:** Render 6 s. 3/4 camera, fovy 40.

### Energy / projectile / kinematics (4)

#### `slingshot_elastic_release` — Energy storage/release
**Physics:** A pre-stretched elastic band (spring) releases stored elastic PE into a ball's kinetic energy — slingshot effect.
**Setup:** Two posts with a horizontal "rubber band" (tendon with stiffness, modelled as a spring). Ball placed against the band, band stretched back by initial qpos. At t=0, the ball is unconstrained; band snaps forward, launching the ball.
**Motion:** Ball flies forward at high velocity; arcs through the air.
**Template:** `spring_mass.xml` + `projectile_jenga.xml`.
**Hints:** Tune spring stiffness for visible launch. Side view. Render 1.5 s.

#### `trampoline_bounce_membrane` — Multi-bounce on elastic surface
**Physics:** A ball bouncing on an elastic membrane — surface flexes, ball bounces multiple times with progressive energy loss.
**Setup:** Membrane: 8×8 grid of small masses with springs between (similar to mexican_hat_drum but smaller, with damping). Edges fixed. Ball dropped from above.
**Motion:** Ball strikes membrane, bounces back up, falls again, bounces several times with decaying amplitude.
**Template:** `mexican_hat_drum_modes.xml` (grid + springs) + `bowling.xml` (ball).
**Hints:** Membrane damping for energy loss. Render 4 s. 3/4 camera.

#### `multi_link_chain_vertical_collapse` — Free fall / chain
**Physics:** A vertical chain standing straight up topples over progressively under gravity; the top accelerates while the base remains in place initially.
**Setup:** Chain of 20 links stacked vertically at world (0, 0, z=0.05 to z=1.05), hinged together. Bottom link pinned to the floor. Initial perturbation: top link tilted 2°.
**Motion:** Top tips and falls, pulling lower links along; full collapse to the floor.
**Template:** `dominoes.xml` + `beam_buckling.xml`.
**Hints:** Hinge damping 0.005 per joint. Render 2.5 s. Side view.

#### `galileo_chord_isochrony` — Energy / kinematics
**Physics:** Galileo's chord isochrony: balls released from rest sliding down chords of a vertical circle all reach the bottom (the circle's lowest point) at the same time, regardless of chord angle.
**Setup:** A vertical circle (R=0.5 m) drawn with thin marker geoms; 3-4 frictionless chord-shaped slides starting from different points on the circle, all ending at the bottom. One ball on each slide, released simultaneously.
**Motion:** All balls reach the bottom simultaneously despite different distances and angles.
**Template:** `brachistochrone.xml` (multi-track ball racing).
**Hints:** Programmatic gen for the chord geometry. Render 1 s — close finish. Side view, pos (1.0, -1.5, 0.3), fovy 40.

### Mechanisms (4)

#### `rack_and_pinion` — Mechanism
**Physics:** A gear (pinion) meshed with a flat toothed bar (rack) converts rotation to linear translation.
**Setup:** Pinion: small cylinder R=0.05 m on a hinge. Rack: long box with a slide joint (along x). Joint equality couples pinion rotation to rack translation: rack_x = -R_pinion · pinion_angle.
**Motion:** Pinion driven by init-qvel; rack translates uniformly.
**Template:** `gear_train_2_gears.xml` + `slider_crank_mechanism.xml`.
**Hints:** Top-down camera. Render 3 s.

#### `scotch_yoke` — Mechanism
**Physics:** Converts rotation to sinusoidal (NOT polygonal) linear motion. Different from slider-crank, which gives non-sinusoidal motion.
**Setup:** Rotating crank with a pin (small post offset from center); the pin engages a vertical slot in a "yoke" (a box with a slide joint along x). As the crank rotates, the pin slides along the slot, pushing the yoke horizontally.
**Motion:** Crank rotates uniformly; yoke moves sinusoidally x(t) = R·cos(ωt).
**Template:** `slider_crank_mechanism.xml`.
**Hints:** Slot is a long groove in the yoke; pin slides along it (slide joint between pin and yoke). Render 3 s.

#### `lazy_tongs_extending` — Mechanism
**Physics:** Lazy tongs (accordion / pantograph) — a linkage of crossed rods extends linearly when actuated at one end.
**Setup:** 4-5 X-shaped pairs of rods, each pair pinned at the middle and at the ends to adjacent pairs. One end has a slide joint (push it inward to extend the mechanism).
**Motion:** End pushed → tongs extend; opposite end moves with mechanical advantage.
**Template:** `slider_crank_mechanism.xml` (linkage idea).
**Hints:** Programmatic gen. Initial impulse rather than actuator. Render 2.5 s.

#### `caliper_scissor_mechanism` — Mechanism
**Physics:** Scissor mechanism (two crossed arms pinned at center) — closing one end opens the other proportionally.
**Setup:** Two long bars crossed at their center on a hinge. Pull the bars at one end together; their other ends spread apart.
**Motion:** One end closes → other end opens, by the lever ratio.
**Template:** `four_bar_linkage.xml`.
**Hints:** Side view. Render 3 s.

### Constrained motion / sliding (4)

#### `bead_on_inverted_cycloid` — Tautochrone (upside-down)
**Physics:** A bead released from various heights on an INVERTED cycloid all reach the bottom in the same time — the cycloid's tautochrone property holds for the inverted shape too.
**Setup:** An inverted-cycloid wire (programmatic, opens downward). 3 beads placed at different heights on the wire, all released simultaneously.
**Motion:** All beads reach the bottom of the cycloid at the same time.
**Template:** `bead_on_cycloid_track_isochrony.xml` (cycloid generator) — inverted.
**Hints:** Render 1.5 s.

#### `two_objects_on_conveyor_belt` — Friction / belt
**Physics:** Two objects placed on a moving conveyor belt — friction accelerates them up to belt speed; afterwards they move with the belt.
**Setup:** A horizontal belt (rectangular surface) given a constant velocity vx=0.5 m/s. Two boxes placed on the belt with zero initial velocity.
**Motion:** Boxes accelerate due to friction with the belt; reach belt speed; then move with it.
**Template:** `belt_friction.xml` + `incline_friction.xml`.
**Hints:** Belt as a moving plane — give it `init-qvel` and high mass so it doesn't slow. Render 3 s.

#### `block_slipping_threshold_on_incline` — Friction transition
**Physics:** A block on an incline is static if angle θ < arctan(μ); above that angle, it slides. The transition is abrupt.
**Setup:** Incline angle slowly increases over time (init-qvel slowly tilts the ramp). Block on the incline with μ=0.4 (so critical angle ~22°).
**Motion:** Block stays static while ramp tilts; at critical angle it suddenly starts sliding and accelerates down.
**Template:** `incline_friction.xml` + `tipping_vs_sliding.xml`.
**Hints:** Initial ramp tilt 0°, init-qvel small rotation rate. Render 4 s.

#### `pendulum_string_breaks_at_peak` — Energy + projectile
**Physics:** A pendulum at the peak of its swing has zero KE (all PE). If the string breaks at that instant, the bob falls straight down. Compare with breaking at the bottom (max KE, flies horizontally).
**Setup:** Pendulum pulled to 60° and released. At a specific time (when the bob reaches peak), the string "breaks" — modelled by setting a tendon limit that fails. The bob becomes a free body.
**Motion:** Bob swings up, string breaks at peak, bob falls straight down from peak (vs would fly horizontally if string broke at bottom).
**Template:** `pendulum.xml`. Add a tendon that fails by setting `range` and `solref`.
**Hints:** "Breaking" is implemented by removing the constraint at the right time. Could use two separate scenes: one with string still intact (for comparison) — but render one with the break. Render 2 s.

### Multi-body / collision (5)

#### `two_balls_on_rotating_string` — Rotating frame
**Physics:** Two equal-mass balls connected by a rigid string, rotating about their common COM, demonstrate circular motion (centripetal force = tension).
**Setup:** Two equal balls (M=0.05 kg each) connected by a thin string (length 0.4 m). System at rest with initial angular velocity 4 rad/s about COM. No gravity (or gravity perpendicular to rotation plane).
**Motion:** Balls orbit each other in a circle, string taut, period T = 2π/ω.
**Template:** `binary_pendulum` style or new — like a rotating dumbbell.
**Hints:** Set gravity to 0 or perpendicular plane. Top-down camera. Render 4 s.

#### `pendulum_hits_spring_target` — Energy transfer
**Physics:** A pendulum swung into a spring-loaded target compresses the spring; spring then bounces target away, transferring energy.
**Setup:** Pendulum at 45°. A target block (M=0.1 kg) on a frictionless surface, with a spring attached behind it. Pendulum bob (M=0.2 kg) hits the target.
**Motion:** Bob hits target, compresses spring, spring bounces target away, pendulum recoils.
**Template:** `pendulum.xml` + `spring_mass.xml` + `elastic_collision.xml`.
**Hints:** Render 3 s.

#### `n_marbles_funnel_clog` — Granular jam
**Physics:** Many marbles fed through a narrowing funnel can jam at the throat — granular media jamming, where arches of force-chains support the load.
**Setup:** Funnel (R=0.10 top → R=0.012 throat), ~40 small balls (R=0.005) placed above the throat. Gravity acts.
**Motion:** Balls accumulate above the throat; some flow through; eventually jam forms and flow stops.
**Template:** `rotating_fluid.xml` (granular hack) + `marble_in_funnel.xml`.
**Hints:** Throat just slightly bigger than ball diameter. Render 4 s.

#### `double_chain_fall_compare` — Chain dynamics comparison
**Physics:** Two chains: one with both ends free, one with one end held — both released. The freely-falling one falls at g; the held one has tension dynamics, falls faster than g (like falling_chain_classical).
**Setup:** Two parallel chains. Left chain: free, dropped horizontally. Right chain: half on a table, half hanging.
**Motion:** Right chain accelerates faster than left (after the same time, right reaches the ground first).
**Template:** `falling_chain_classical.xml`.
**Hints:** Render 1.5 s. Side view, wide.

#### `ball_inside_closed_box_bounces` — Multi-bounce containment
**Physics:** A ball inside a closed 5-sided box (open top) bounces off the walls and floor many times; CoR < 1 makes eventually settle.
**Setup:** Cube box (open top), 0.30 m side. Ball (R=0.02, M=0.05 kg) inside, initial qvel (0.5, 0.7, -0.3).
**Motion:** Ball ricochets around the box, eventually losing energy and settling.
**Template:** `bowling.xml` + `elastic_collision.xml`.
**Hints:** Render 4 s. 3/4 camera.

### Structures / statics (4)

#### `leaning_tower_critical_angle` — Equilibrium / tipping
**Physics:** A tower is stable as long as the projection of its COM onto the floor stays inside the base. Tilt it beyond, and it tips.
**Setup:** A tall thin tower (rectangular box, dims 0.10 × 0.10 × 0.6 m) on a slowly-tilting platform. Platform tilts via init-qvel angular rotation.
**Motion:** Tower stays upright while platform tilts; at critical angle (~10° for this geometry), tower tips and falls.
**Template:** `cone_balanced_on_tip.xml` + `tipping_vs_sliding.xml`.
**Hints:** Render 5 s.

#### `arch_stability_increasing_load` — Statics / failure
**Physics:** An arch can hold up to its critical load; beyond that, individual stones slip and the structure fails.
**Setup:** Arch (like `arch_compression.xml`) with a movable load on top that grows over time (or step-increments).
**Motion:** Arch holds small load → grows → eventually buckles when load exceeds critical.
**Template:** `arch_compression.xml`.
**Hints:** Programmatic gen for the arch. Load can be a heavy mass that descends onto the arch. Render 4 s.

#### `granular_arch_self_support` — Granular statics
**Physics:** Granular media (small balls) can form a self-supporting arch over a gap — force chains transfer load to the supports.
**Setup:** Two supports with a gap between them (10 cm). Many small balls (R=0.01) piled on top. After release, some balls fall through; the rest form a self-supporting arch over the gap.
**Motion:** Initial pile collapses; settling state shows a stable arch with balls bridging the gap.
**Template:** `rotating_fluid.xml` (granular).
**Hints:** Render 3 s. Side view.

#### `waterwheel_with_balls` — Granular flow / mechanism
**Physics:** A water wheel driven by cascading "water" (granular balls) — gravity pulls balls into cups on the wheel rim, wheel rotates.
**Setup:** A wheel (R=0.15 m) with 8 small cups on its rim, on a horizontal axle. A stream of small balls falling from above onto one side of the wheel.
**Motion:** Balls land in cups, weight unbalances the wheel, wheel rotates; new cups receive balls; continuous rotation.
**Template:** `rotating_fluid.xml` + `marble.xml`.
**Hints:** Hard — granular cascade. Programmatic. Render 4-5 s.

### Other (5)

#### `inverted_pendulum_on_hinge_falls` — Instability
**Physics:** An inverted rigid rod pinned at the base, with no support, falls due to instability. Different from `falling_chimney` (which has more pinning detail) and `cone_balanced_on_tip` (which is a free body, not pinned).
**Setup:** Rod (length 0.5 m, M=0.5 kg) pinned at base with a hinge (axis y, no stiffness). Initial pose: vertical (no perturbation), with init-qvel tiny angular velocity (0.05 rad/s) to seed the fall.
**Motion:** Rod falls over, pivot at base.
**Template:** `falling_chimney.xml`.
**Hints:** Render 2 s. Side view.

#### `chain_in_freefall_no_tension` — Free fall demonstration
**Physics:** A chain in free-fall has zero internal tension — every link accelerates at g, so they all "float" relative to each other. The chain maintains its initial shape during fall.
**Setup:** Chain shaped in a recognizable curve (e.g., a U or a horizontal line) at world height z=2.0 m. Released from rest.
**Motion:** Entire chain falls together, maintaining its initial shape (no relative motion between links).
**Template:** `dominoes.xml`.
**Hints:** Verify by visual: chain shape doesn't change as it falls. Render 0.6 s (fall time from 2 m ≈ 0.64 s).

#### `chain_pulled_through_pipe` — Constrained chain
**Physics:** A chain pulled through a curved tube — the constraint of the tube redirects the chain's motion; the pulling force changes direction at every bend.
**Setup:** Curved tube (gen): like an S-shape. Chain inside the tube. One end of the chain pulled out at constant force.
**Motion:** Chain slides through the tube; visible direction changes at each bend.
**Template:** `bead_on_helix.xml` + `dominoes.xml`.
**Hints:** Programmatic. Render 4 s.

#### `brake_drum_friction` — Friction / energy dissipation
**Physics:** A spinning drum is slowed by a friction brake pressing on its rim. Kinetic energy dissipated as heat (or in this case, just observed as slowing rotation).
**Setup:** A heavy disc (drum) R=0.15 m, M=1 kg, on a vertical axle, spinning at ω=20 rad/s. A "brake pad" (block on a slide joint) pressed against the rim with some normal force.
**Motion:** Drum spins; friction torque slows it down; eventually stops.
**Template:** `maxwell_wheel.xml` + `incline_friction.xml`.
**Hints:** Brake pad against the rim has friction coefficient. Render 4 s.

#### `two_disks_friction_coupling` — Friction-driven rotation
**Physics:** Two discs in contact at their rims, one spinning — friction between rims drives the other disc to spin (opposite direction). No teeth, just friction.
**Setup:** Disc A (R=0.08 m, M=0.5 kg) on a vertical hinge, spinning at ω=10 rad/s. Disc B (R=0.12 m) on a vertical hinge, initially at rest. The two rims pressed together with some normal force.
**Motion:** A spins; friction transfers torque to B; B starts rotating in opposite direction at scaled speed (R_a/R_b ratio).
**Template:** `gear_train_2_gears.xml` (but without equality — let friction couple them).
**Hints:** Tune normal force and friction to get clean coupling. Render 4 s.

#### `galton_board_classic` — Statistics / multi-body
**Physics:** Many balls dropped through a grid of pegs end up distributed in a binomial (approximate normal) distribution at the bottom.
**Setup:** Grid of small pegs (5-7 rows, triangular layout). Funnel above releases balls one at a time (or many at once). Catchment bins below collect them.
**Motion:** Each ball bounces left/right at each peg level; net path leads to a bell-curve distribution in the bins.
**Template:** `dominoes.xml` (peg layout) + `bowling.xml` (balls).
**Hints:** Pegs as small cylinders. ~20 balls in the funnel. Render 5-6 s.

#### `plate_balancing_on_stick` — Balance + rotation
**Physics:** A plate spinning on a vertical stick — its angular momentum gyroscopically stabilizes the plate against tipping over.
**Setup:** Vertical thin stick on the floor. A horizontal plate (M=0.2 kg, R=0.15 m) balanced on the stick's top, initially spinning at ω=20 rad/s about the stick's axis.
**Motion:** Plate spins; gradually slows due to friction; while spinning fast, stays balanced; eventually wobbles and falls when spin too slow.
**Template:** `spinning_top.xml`.
**Hints:** Stick tip-plate friction needs tuning. Render 5-6 s.

#### `ball_bouncing_corner_2d` — Collision geometry
**Physics:** A ball bouncing into a 90° corner (two perpendicular walls) reflects twice and exits in a direction opposite to incoming (parallel reverse).
**Setup:** Two perpendicular walls forming a corner. A ball with init-qvel into the corner at some angle.
**Motion:** Ball hits one wall, reflects; immediately hits the other wall, reflects again; exits in a direction antiparallel to original.
**Template:** `elastic_collision.xml` + `bowling.xml`.
**Hints:** Stiff contacts. Top-down camera. Render 1 s.

#### `swinging_bell_with_clapper` — Multi-body coupling
**Physics:** A bell swinging on a pivot has a clapper inside (a sub-pendulum hung from the bell's interior); the two pendulums have different effective lengths, so the clapper strikes the bell's walls at characteristic intervals.
**Setup:** Bell: outer hollow cup (4 thin walls + closed top, opening down), M=0.5 kg, pivoted at the top with hinge axis y. Inside the bell: a small clapper (sphere R=0.015, M=0.05 kg) on a short string (length 0.10 m) hung from the bell's interior ceiling. Bell pulled to 60° and released.
**Motion:** Bell swings back and forth as a pendulum; clapper swings inside but with its own (shorter) period; clapper periodically strikes the inner bell wall.
**Template:** `pendulum.xml` (basic pendulum) + `double_pendulum.xml` (nested swings).
**Hints:** Bell wall is a few thin box geoms making the hollow cup. Stiff contact between clapper and walls (gotcha #4). Render 5 s. Side view, pos (0, -1.2, 0.5), fovy 40.

---

## 🔴 Tier 3 — Harder, multi-part scenes (5–10 hr each)

These are bigger projects that warrant their own day each. Don't include in
the 18-scenes-per-day plan; allocate them as one-off projects.

- **trebuchet** — counterweight + arm + sling + projectile; classic mechanical advantage
- **crane_hoist_articulated** — multi-link crane arm + cable + hook + load
- **roller_coaster_simple** — track with loops, hills, and a launch
- **cam_follower_mechanism** — rotating cam drives a reciprocating follower
- **differential_gear_visual** — visual demo of how a car differential splits torque
- **articulated_arm_5dof** — 5-DOF robotic arm reaching for an object
- **domino_fibonacci_spiral** — programmatic Fibonacci or logarithmic spiral of dominoes
- **pendulum_clock_escapement** — escapement wheel + pendulum drives a clock
- **perpetual_motion_demos** — show 3 famous "perpetual motion" designs failing
- **kinetic_sculpture_mobile** — multi-pendulum mobile, balanced and swinging

---

## ❌ Tier 4 — Out of scope (need a different simulator)

These need fluid / EM / optics / thermo and cannot be done with MuJoCo as-is.

- ❌ `hydrostatic_buoyancy` — needs continuous fluid; granular hack is poor
- ❌ `surface_tension`, `capillary_action` — needs SPH/MPM
- ❌ `wave_tank`, `dam_break` — needs SPH
- ❌ `vortex_shedding`, `karman_street` — needs Navier-Stokes
- ❌ `charged_particle_in_field` — needs EM force solver
- ❌ `electromagnetic_induction` — Faraday's law
- ❌ `motor_generator` — coil + magnet rotation, needs EM
- ❌ `light_refraction_lens` — needs ray tracing
- ❌ `double_slit_interference` — needs wave optics
- ❌ `gas_in_piston` — needs thermodynamics

For any of these, suggest a different toolkit (Genesis, Taichi+MPM, Manim,
or pre-animated Blender) — they are deliberately off-roadmap for this repo.

## 🟤 Round 3 — Packages J / K / L / M (50 scenes)

### Package J — Chaos, Nonlinear & Coupled Oscillators (13)

#### `double_pendulum_chaos_compare` — Chaos / butterfly effect

**Physics:** Two double pendulums with initial conditions differing by only ε = 0.01° exhibit exponential divergence of trajectories — a hallmark of deterministic chaos and sensitive dependence on initial conditions.
**Setup:** Two identical double pendulums (each link L = 0.3 m, M = 0.1 kg) placed side by side in the xz-plane, x-separated by 0.4 m. Both start from θ₁ = 60°, θ₂ = 0°; the second pendulum's θ₁ is offset by +0.01° = 0.000175 rad. No damping.
**Motion:** render 8 s. For the first 2–3 s the two pendulums swing nearly identically. Around t ≈ 3–5 s the trajectories visibly diverge; by t = 8 s the two bobs are completely out of phase. Camera: front view, fovy = 45, pos (0, -1.2, 0.0).
**Template:** `double_pendulum.xml`. Duplicate the entire double-pendulum body tree, offset by x = 0.4 m. Adjust init-qpos for the second copy's first joint by +0.000175 rad.
**Hints:** Use `integrator="RK4"` and `timestep="0.001"` for accurate long-horizon integration. Keep gravity at default (9.81). Both pendulums must share the same world body but have completely independent joint trees. See gotchas.md §chaos — do NOT use `euler` integrator here; RK4 is required or divergence will be numerical artefact not physical chaos.

---

#### `pendulum_full_rotation` — Separatrix / rotation

**Physics:** A pendulum released with kinetic energy just above the separatrix energy E = 2mgL transitions from oscillation to continuous rotation; the separatrix is the unstable fixed point at θ = π (inverted position).
**Setup:** Single pendulum, L = 0.5 m, M = 0.1 kg, pivot fixed. init-qpos: θ = 0 (hanging). init-qvel: ω = 6.3 rad/s (just above ω_sep = √(4gL/L²·L) = √(4 × 9.81 / 0.5) ≈ 8.86 rad/s — recalculate: ω_sep = √(4g/L) = √(4×9.81/0.5) ≈ 8.86 rad/s. For L=0.5, ω_sep ≈ 8.86 rad/s; use ω = 9.0 rad/s to be safely above). No damping.
**Motion:** render 6 s. The pendulum sweeps through the bottom, continues past horizontal, passes through the top (θ = 180°) with non-zero speed, and completes full rotations. Camera: side view capturing the full circle.
**Template:** `pendulum.xml`. Set init-qvel on the hinge joint to 9.0. Ensure joint `range` is not clamped (remove range or set range = "-1e9 1e9"). Set `limited="false"` on the hinge.
**Hints:** Critical: remove joint angle limits or MuJoCo will clamp the rotation. ω_sep = √(4g/L); use ω = 1.015 × ω_sep for a clean rotation with a little headroom. If the pendulum just barely passes the top it will look like it "floats" — which is fine for separatrix illustration. See gotchas.md §joint_limits.

---

#### `lissajous_2d_spring_mass` — Parametric curves

**Physics:** A mass on two perpendicular springs with incommensurable natural frequencies traces closed Lissajous figures in 2D. For ω_x : ω_z = 1 : 2 (achieved by k_z = 4 k_x), the trajectory is a figure-8 in the xz-plane.
**Setup:** Single bob (M = 0.1 kg) with two independent slide joints: one along x (stiffness k_x = 100 N/m, equilibrium x = 0) and one along z (stiffness k_z = 400 N/m, equilibrium z = 0). init-qpos: x = 0.05 m, z = 0. init-qvel: ẋ = 0, ż = 0 (starts from x-displaced rest). No damping.
**Motion:** render 10 s. The bob traces a clean figure-8 Lissajous pattern in the xz-plane. Camera: front view, orthographic recommended, fovy = 30, pos (0, -0.5, 0).
**Template:** `spring_mass.xml`. Replace the single slide joint with two orthogonal slide joints (axes "1 0 0" and "0 0 1"). Add spring stiffness via `<joint ... stiffness="100">` (x) and `<joint ... stiffness="400">` (z).
**Hints:** Use zero damping (`damping="0"`) for persistent Lissajous pattern. For k₁ : k₂ = 1 : 4 and starting from x-displacement only, the pattern is 1:2 (figure-8). Add a tracer geom (small sphere) or use the ball itself. The scene should run long enough (≥ 10 s) to show the closed curve traced multiple times. See gotchas.md §spring_stiffness.

---

#### `duffing_double_well` — Nonlinear oscillator / chaos

**Physics:** A Duffing oscillator with two potential wells (W-shaped track) shows qualitatively different behaviour depending on total energy: low-energy trajectories are trapped in one well (quasi-linear), while high-energy trajectories hop between wells (nonlinear chaos territory).
**Setup:** W-shaped curved track: z(x) = a·x⁴ − b·x² with a = 10 m⁻³, b = 1 m⁻¹ (minima at x = ±0.22 m, z_min ≈ −0.025 m, barrier at x = 0, z = 0). Built from ~30 thin box segments approximating the curve, static. Two balls: Ball A (M = 0.1 kg) placed at x = 0.22 m with low init-qvel v = 0.2 m/s (stays in right well); Ball B at x = 0.22 m with v = 1.4 m/s (clears barrier and transitions).
**Motion:** render 6 s. Ball A oscillates back and forth in the right valley. Ball B has enough energy to cross the central barrier and hop between wells, showing the nonlinear dynamics.
**Template:** `brachistochrone.xml` (for curved track segment technique). gen_duffing_track.py generates ~30 box geoms approximating z = 10x⁴ − x² over x ∈ [−0.35, 0.35].
**Hints:** Track segments must be tangentially placed (each segment rotated to match the local slope angle = arctan(dz/dx)). Segment width ~0.015 m. Balls start at x = ±0.22 m. Both balls same y-position but separated in x so they don't collide. See gotchas.md §curved_track_segments.

---

#### `pendulum_pivot_on_cart` — Coupled translational/rotational

**Physics:** A pendulum mounted on a freely sliding cart couples rotational and translational degrees of freedom. When the cart is given an impulse, kinetic energy transfers between cart translation and pendulum rotation — the system's COM moves at constant velocity.
**Setup:** Cart (M = 0.5 kg, box 0.15 × 0.05 × 0.03 m) on a frictionless slide joint along x. Pendulum (L = 0.5 m, M = 0.1 kg) hung from the cart's top via a hinge joint (y-axis). init-qvel: cart ẋ = 1.5 m/s, pendulum ω = 0. No friction on slide joint (frictionloss = 0, damping = 0).
**Motion:** render 8 s. Cart slides right, pendulum swings behind it (reaction). Energy oscillates between cart KE and pendulum KE+PE; the cart accelerates and decelerates as the pendulum swings. COM of the whole system drifts at constant vx.
**Template:** `pendulum.xml`. Add a slide joint (axis "1 0 0") to the world-to-cart connection, replacing the fixed mount. Cart body defined as parent of the pivot body.
**Hints:** The cart slide joint must have `frictionloss="0"` and `damping="0"` or energy will not be conserved. The system has 2 DOF: cart x and pendulum angle θ. Total linear momentum is conserved. Camera: wide side view (fovy = 50) to capture cart travel. See gotchas.md §chained_joints.

---

#### `foucault_pendulum_turntable` — Rotating frame / Coriolis

**Physics:** A pendulum mounted on a slowly rotating horizontal platform precesses its swing plane in the lab frame due to the Coriolis effect — analogous to Earth's rotation causing real Foucault pendulum precession.
**Setup:** Platform disk (M = 1 kg, R = 0.15 m, thickness 0.01 m) connected to the world via a hinge joint about z with init-qvel ω_plat = 0.3 rad/s. Pendulum pivot attached to the platform surface; pendulum L = 0.4 m, M = 0.1 kg, hanging from platform. init-qvel: pendulum ω = 2 rad/s about the platform-frame x-axis.
**Motion:** render 15 s. In the lab frame, the pendulum swing plane slowly rotates as the platform turns. Observe at least 1–2 full platform rotations and the corresponding swing-plane rotation. Camera: top-down, pos (0, 0, 0.8), fovy = 50.
**Template:** `conical_pendulum.xml`. Replace the fixed pivot with a platform body having a z-hinge joint. Pendulum body parented to platform.
**Hints:** Platform rotation must be frictionless (damping = 0 on z-hinge) to sustain steady rotation. The pendulum swing damps naturally in MuJoCo due to joint damping — set damping = 0.001 (minimal). Use 15 s render to see clear precession. The turntable angular velocity ω_plat = 0.3 rad/s means one full rotation in ~21 s, so 15 s shows about 3/4 of a rotation. See gotchas.md §rotating_frames.

---

#### `variable_length_pendulum` — Energy pumping / parametric

**Physics:** Parametric resonance: shortening a pendulum's effective length at the bottom of each swing (when the bob's KE is maximum) injects energy into the oscillation, causing amplitude to grow each cycle — the classic "pumping a swing" mechanism.
**Setup:** Single pendulum, base pivot fixed. A slide joint at the pivot allows the string length to vary between L_min = 0.3 m and L_max = 0.6 m. String shortens by Δ = 0.15 m each time the bob passes through θ = 0 (bottom), then re-extends at the top. Start: L = 0.6 m, θ = 30°, ω = 0.
**Motion:** render 10 s. Amplitude grows visibly over ~5–7 cycles. The bob swings with increasing arc. After 8–10 cycles the amplitude saturates near the joint limit.
**Template:** `pendulum.xml`. Add a slide joint at the pivot with range [−0.3, 0] (controls Δ-length). gen_variable_length_pendulum.py injects qpos commands for the slide joint each timestep based on sign of angular velocity (bottom of swing detection).
**Hints:** Parametric pumping requires precise timing: shorten at θ ≈ 0, extend at θ ≈ ±θ_max. Implement via `mj_step` callback in gen script. Slide joint stiffness = 0, damping = 0. The mass of the "string" should be negligible. See gotchas.md §programmatic_control.

---

#### `euler_disk_spindown` — Precession / singularity

**Physics:** As a spinning coin loses energy to rolling friction, it paradoxically spins faster while tilting lower — a finite-time singularity where precession frequency diverges just before the coin abruptly stops, explained by Moffatt's rolling-friction theory.
**Setup:** Thin disc (cylinder, R = 0.05 m, thickness = 0.004 m, M = 0.05 kg) on a flat floor. Freejoint. init-qpos: tilt 3° from vertical (Euler angles). init-qvel: spin ω_z = 20 rad/s (about the disc's symmetry axis). Floor friction: `friction="0.3 0.005 0.001"` (rolling friction nonzero).
**Motion:** render 6 s. Disc initially spins steadily with mild precession. Over time, tilt angle increases and precession rate increases dramatically. Near t ≈ 5–6 s, the disc rattles with very fast precession and abruptly stops flat on the floor.
**Template:** `spinning_top.xml` (freejoint body + floor). Replace sphere/cone tip with a flat cylinder. Set freejoint initial conditions via `qpos` (position + quaternion) and `qvel` (linear + angular velocities).
**Hints:** The freejoint qvel order in MuJoCo is [vx, vy, vz, ωx, ωy, ωz]. The disc's spin axis is its local z (symmetry axis). init-qvel should be [0, 0, 0, 0, 0, 20]. Rolling friction `solimp` must allow realistic energy dissipation — use `solref="0.02 1"` and `solimp="0.9 0.95 0.001"`. See gotchas.md §freejoint_init and §rolling_friction.

---

#### `kapitza_pendulum` — Parametric stabilization

**Physics:** An inverted pendulum becomes dynamically stable when its pivot is oscillated vertically at high frequency and sufficient amplitude — the Kapitza pendulum effect, where rapid oscillation creates an effective stabilizing potential.
**Setup:** Two side-by-side pendulums (L = 0.5 m, M = 0.1 kg), both inverted (hinge at bottom, rod pointing up). Pendulum A: pivot fixed, initial tilt 3° — falls. Pendulum B: pivot has a slide joint along z driven sinusoidally at A = 0.01 m, f = 20 Hz (ω_drive = 125.7 rad/s >> ω_0 = √(g/L) ≈ 4.4 rad/s) — stands stable. Both start at 3° tilt from vertical.
**Motion:** render 5 s. Pendulum A falls in ~0.5 s. Pendulum B oscillates about the inverted position, stabilized by the rapid pivot motion. Camera: front view.
**Template:** `pendulum.xml` (with gravity flipped for inverted mount, or simply start with rod pointing up from hinge). gen_kapitza.py provides the sinusoidal z-displacement by setting the slide joint qpos each step.
**Hints:** Kapitza stability condition: A·ω_drive > √2 · g·L (approximately). With A = 0.01, ω = 125.7: A·ω = 1.257 m/s. √2·g·L = √2·9.81·0.5 = 6.94 m/s — need to increase A or ω. Use A = 0.02 m, f = 50 Hz: A·ω ≈ 6.28 m/s (closer). Fine-tune in simulation. See gotchas.md §parametric_drive.

---

#### `precession_nutation_full` — Euler angles / gyroscope

**Physics:** A spinning top at a large nutation angle (40°) exhibits both slow precession (spin axis orbits the vertical) and superimposed nutation (wobbling of the spin axis up and down), demonstrating the full complexity of Euler angle dynamics beyond the small-angle limit.
**Setup:** Top (M = 0.3 kg, principal moments I_axial = 5×10⁻⁴ kg·m², I_transverse = 3×10⁻⁴ kg·m²) with a ball tip touching the floor. init-qpos: Euler angles giving θ = 40° nutation (tilt from vertical). init-qvel: spin ω_spin = 50 rad/s about the top's symmetry axis; precession and nutation rates initially zero (giving maximum nutation wobble).
**Motion:** render 6 s at least 2 full precession cycles. Observe: the spin axis sweeps a cone (precession) and simultaneously oscillates between two nutation angles (wobble). Camera: 3/4 view, pos (0.5, −0.5, 0.3), fovy = 40.
**Template:** `spinning_top.xml`. Adjust inertia tensor components via `<inertial diaginertia="...">`. Set nutation angle via quaternion in init-qpos: quat = [cos(θ/2), sin(θ/2), 0, 0] gives tilt θ about x.
**Hints:** With zero initial precession rate and θ = 40°, the top will nutate between 40° and a second nutation angle determined by energy/angular momentum conservation. Render long enough (6 s) to see ≥ 2 precession cycles. MuJoCo's freejoint or ball joint work; if using freejoint, set full 6-DOF initial conditions carefully. See gotchas.md §spinning_top_init.

---

#### `coupled_gyroscopes_reaction` — Gyroscopic coupling

**Physics:** Two co-spinning gyroscopes on parallel axles exert reaction torques that oppose frame tilting: tilting the shared frame causes both gyros to precess in opposite directions (or the same, depending on spin direction), creating a net reaction moment that resists the tilt.
**Setup:** Rigid frame body (L = 0.3 m bar) connected to world via hinge about x-axis. Gyro disc A (R = 0.05 m, M = 0.2 kg) on a hinge about y at position x = +0.10 m on the frame, init-qvel ω_A = +60 rad/s. Gyro disc B identical, at x = −0.10 m, init-qvel ω_B = +60 rad/s (same spin direction). Frame init-qpos: 20° tilt about x.
**Motion:** render 5 s. From the initial tilted position, both gyros precess and the frame exhibits a characteristic rocking/precessing motion driven by gyroscopic coupling. Camera: 3/4 view showing both discs and frame.
**Template:** `spinning_top.xml` (×2 disc bodies). Frame body with hinge (axis "1 0 0") to world. Each disc body parented to frame with hinge (axis "0 1 0"). High spin-rate init-qvel on each disc's y-hinge.
**Hints:** Both discs spinning in the same direction about y gives net angular momentum along y; tilting the frame about x will cause precession about z (perpendicular). The frame hinge about x must have low damping (0.001) to allow gyroscopic effects to dominate. With opposite spin directions, angular momenta cancel and no gyroscopic effect appears — use same direction for visible effect. See gotchas.md §gyroscopic_coupling.

---

#### `newton_cradle_mass_gradient` — Momentum / mass mismatch

**Physics:** In a Newton's cradle with non-uniform ball masses, the simple one-in/one-out rule breaks down: the momentum and energy cannot be simultaneously conserved with a clean transfer, resulting in multiple balls moving after impact.
**Setup:** Five balls on strings (string length 0.3 m from pivot) at regulation spacing. Masses left to right: 0.05, 0.08, 0.12, 0.18, 0.25 kg. All same radius R = 0.02 m. Leftmost ball pulled to θ = 40° and released. Contact parameters: stiff (solref = "0.005 1", solimp = "0.99 0.999 0.001").
**Motion:** render 4 s. Leftmost ball strikes the row. Unlike the uniform cradle, the rightmost ball does NOT simply fly off alone — multiple balls on the right end move, with decreasing velocities. On return collisions the pattern continues to break classical expectations.
**Template:** `newton_cradle.xml`. Assign individual `<body ... mass="...">` or `<inertial mass="...">` values to each ball body. Keep geometry (R, string length, pivot spacing) uniform.
**Hints:** The mass gradient makes elastic collision analysis non-trivial. Use very stiff contacts to approximate ideal elastic collisions. Five balls means five equations but only two conservation laws — under-determined, so MuJoCo's contact model determines the actual outcome. Validate: leftmost ball (lightest) should bounce back slightly. See gotchas.md §newton_cradle_contacts.

---

#### `pendulum_near_separatrix` — Phase space / critical energy

**Physics:** A pendulum given initial speed just below the separatrix energy asymptotes toward the inverted position (θ = π), slowing to near-zero speed at the top — a trajectory that theoretically takes infinite time to reach the unstable equilibrium point.
**Setup:** Single pendulum L = 0.5 m, M = 0.1 kg. init-qpos: θ = 0 (hanging). init-qvel: ω = 4.40 rad/s (99% of separatrix speed ω_sep = √(4g/L) = √(4×9.81/0.5) ≈ 8.86 rad/s — wait, recheck: ω_sep from energy: ½Iω² = 2mgL → ω² = 4mgL/I = 4mg·L/(mL²) = 4g/L → ω_sep = 2√(g/L) = 2√(9.81/0.5) ≈ 8.86 rad/s. Use ω = 0.99 × 8.86 = 8.77 rad/s). No damping.
**Motion:** render 12 s. Pendulum swings up quickly, then decelerates dramatically near θ = 180°, hanging near the top for several seconds before slowly swinging back down. Camera: side view, wide enough to show full arc.
**Template:** `pendulum.xml`. Set init-qvel = 8.77 on the hinge. Remove joint limits. Use `integrator="RK4"` for accurate near-separatrix integration.
**Hints:** At 99% separatrix energy the bob reaches θ ≈ 178° and hangs there for ~8–10 s (numerical precision determines exact hover time). Use RK4 with timestep = 0.0005 for accuracy. The scene illustrates phase-space concepts: the separatrix separates libration from rotation orbits. See gotchas.md §separatrix_integration.

---

### Package K — Mechanisms & Machines 2.0 (13)

#### `spring_gun_launch` — Elastic PE → KE

**Physics:** A compressed spring stores elastic potential energy E = ½kx²; upon release, all stored energy converts to kinetic energy of a launched projectile (minus losses), and maximum height is h = E/(mg).
**Setup:** Spring mechanism: a hinge joint with stiffness k = 5000 N/m acts as the launch spring. Ball (M = 0.05 kg, R = 0.015 m) sits in a cup on the spring arm. init-qpos: spring compressed by x = 0.03 m (stored PE = ½ × 5000 × 0.03² = 2.25 J). At t = 0 the ball is released from the cup (unconstrained). Floor and walls absent to show clean ballistic arc.
**Motion:** render 1.5 s. Spring releases, flinging the ball upward. Ball follows a parabolic arc, reaching maximum height h = 2.25/(0.05×9.81) ≈ 4.6 m (adjust scale so this fits in frame — use k = 200 N/m for h ≈ 0.18 m with x = 0.03 m). Ball rises and falls.
**Template:** `spring_mass.xml`. Use a hinge joint (y-axis) with `stiffness="200"` as the launch mechanism. Ball body connected via an equality constraint (weld) that is disabled at t = 0, or simply use contact-based cup. Render with a moderately high camera.
**Hints:** Predicted max height h = kx²/(2mg) = 200×0.03²/(2×0.05×9.81) = 0.18 m — matches a clean 1.5 s scene. For a visually dramatic launch, use k = 2000 N/m and x = 0.04 m → h ≈ 3.3 m with appropriate camera. Weld equality constraint release: set `active="false"` in gen script at t = 0. See gotchas.md §equality_constraints.

---

#### `toggle_clamp_overcenter` — Mechanism / over-center locking

**Physics:** A toggle clamp passes through an over-center configuration where the three pivot points become collinear; at this singularity, the mechanical advantage is infinite and any output force cannot backdrive the mechanism — the basis for vice grips and industrial clamps.
**Setup:** Three-link planar mechanism: input arm (L = 0.10 m, M = 0.05 kg, hinge to world at origin, y-axis), coupler (L = 0.08 m, M = 0.03 kg, hinge between input arm tip and output stub base), output stub (L = 0.03 m, M = 0.02 kg, constrained to slide vertically via slide joint to world). init-qvel on input arm: ω = 1.5 rad/s (drives toward over-center). After over-center, apply a large downward force (F = 50 N) on the output platen via a `<actuator forcerange=...>` or body gravity.
**Motion:** render 4 s. Input arm rotates, passing over-center at ~t = 1 s. Output platen locks. Applied force after locking cannot move the mechanism — it remains locked. Camera: front view.
**Template:** `four_bar_linkage.xml`. Remove the fourth link; add a slide joint constraint for the output stub. Key: the over-center condition is when all three pivots (world hinge, coupler–input junction, coupler–output junction) are collinear.
**Hints:** Over-center condition: input arm angle + coupler angle = 180°. Detect in gen script and stop applying input velocity. For the lock test, add a downward external force as a body-level `<force>` after t = 1 s. Numerical stability near singularity: reduce timestep to 0.0005 around the over-center moment. See gotchas.md §mechanism_singularities.

---

#### `maxwell_wheel_inertia_compare` — Rotational inertia / descent

**Physics:** For a Maxwell wheel (yo-yo descending on a string), angular acceleration α = g / (1 + I/(mR²)) — wheels with higher moment of inertia I descend slower. Three wheels with identical mass but different mass distributions illustrate the effect of I on acceleration.
**Setup:** Three Maxwell wheels side by side (x = −0.3, 0, +0.3 m), all M = 0.2 kg, axle R = 0.01 m, string length 0.4 m. (a) Hoop/rim-mass: I = mR_rim² with R_rim = 0.08 m → I ≈ 0.00128 kg·m². (b) Solid disc: I = ½mR² with R = 0.08 m → I ≈ 0.00064 kg·m². (c) Centre-mass (all mass at axle): I ≈ m·R_axle² → I ≈ 0.00002 kg·m². Strings attached to ceiling.
**Motion:** render 4 s. All three released simultaneously. Rim-mass wheel (a) descends slowest. Solid disc (b) intermediate. Centre-mass (c) descends fastest, almost in free fall.
**Template:** `maxwell_wheel.xml` (×3). Override `<inertial diaginertia="...">` for each wheel to set the desired I values. Ensure string (tendon) length and attachment points are identical for all three.
**Hints:** Use `<inertial mass="0.2" diaginertia="I I I">` override. Stagger x-positions. Predicted descent times: use energy conservation — (c) descends in t ≈ √(2h/g) ≈ 0.29 s, (a) in t ≈ √(2h(1 + I_a/(mR²))/g). Camera: front view. See gotchas.md §inertia_override.

---

#### `flywheel_energy_storage` — Rotational KE / energy transfer

**Physics:** A spinning flywheel stores rotational kinetic energy; when frictionally coupled to a second disc, angular momentum distributes between them according to conservation: ω_final = (I₁ω₁) / (I₁ + I₂).
**Setup:** Flywheel (M = 2 kg, R = 0.15 m, I₁ = ½ × 2 × 0.15² = 0.0225 kg·m², hinge joint y-axis) at x = −0.15 m, init-qvel ω₁ = 40 rad/s. Second disc (M = 0.5 kg, R = 0.10 m, I₂ = 0.0025 kg·m²) at x = +0.10 m, initially ω₂ = 0. At t = 2 s, a friction pad (separate body with high-friction contact) is pressed between the two discs' rim edges — real contact friction couples them.
**Motion:** render 5 s. For t < 2 s: flywheel spins fast, second disc stationary. After t = 2 s: friction coupling — flywheel slows, second disc accelerates. Final: both at ω_f = I₁ω₁/(I₁+I₂) ≈ 36 rad/s. Camera: side view.
**Template:** `maxwell_wheel.xml` (two-disc setup). Add a friction-pad body between the discs' rims, activated at t = 2 s via a slide joint (gen script pushes pad into contact). Pad geom: `friction="1.5 0.01 0.005"`.
**Hints:** The friction coupling is achieved by translating a rubber-pad body into contact with both disc rims simultaneously. Use gen script to set pad slide-joint qpos at t = 2 s. The energy lost to friction heat = ½(I₁I₂/(I₁+I₂)) × (ω₁−ω₂)² ≈ 6.8 J. See gotchas.md §friction_coupling.

---

#### `bascule_bridge_opening` — Mechanism / counterweight

**Physics:** A bascule bridge uses a counterweight to reduce the net torque required to lift the roadway; if the counterweight torque exceeds the roadway torque (counterweight side heavy), the bridge opens under gravity without external power.
**Setup:** Single plate (total mass distributed as: counterweight M_cw = 2 kg on the short arm L_cw = 0.2 m from pivot, roadway M_road = 0.5 kg uniformly over L_road = 0.6 m, COM at 0.3 m from pivot). Hinge joint at the pivot (y-axis). init-qpos: 5° from horizontal (nearly flat, counterweight side slightly heavy). No actuator.
**Motion:** render 3 s. The counterweight side falls, the roadway side rises. Bridge swings from near-horizontal to near-vertical. Camera: side view, fovy = 50.
**Template:** `pendulum.xml` (hinge) adapted for an asymmetric plate. Model as a single box body with `<inertial>` specifying the asymmetric COM position (mass = 2.5 kg, COM at x_COM = (M_cw × (−0.2) + M_road × 0.3) / 2.5 from pivot). Alternatively, use two box geoms on either side of the hinge.
**Hints:** The net torque at 5° tilt must be confirmed to cause opening (counterweight torque > roadway torque accounting for cosine factors). Torque_cw = 2 × 9.81 × 0.2 × cos(5°) ≈ 3.91 N·m. Torque_road = 0.5 × 9.81 × 0.3 × cos(5°) ≈ 1.47 N·m. Net torque opens bridge. See gotchas.md §asymmetric_inertia.

---

#### `domino_energy_amplification` — Chain reaction / energy amplification

**Physics:** In a chain of geometrically scaled dominoes, each falling domino has more potential energy than the one before it; the small initial push is amplified exponentially through the chain, demonstrating multiplicative energy transfer in mechanical cascades.
**Setup:** 12 dominoes with geometric scaling factor 1.5: heights h_i = 0.02 × 1.5^(i−1) m, widths w_i = h_i/5, thicknesses t_i = h_i/10, masses m_i = ρ × h_i × w_i × t_i (density ρ = 1500 kg/m³). Domino 1: h = 0.02 m, m ≈ 0.000024 kg. Domino 12: h ≈ 0.39 m, m ≈ 0.0089 kg. Spacing: domino i placed so domino i (when falling) just reaches domino i+1 top edge.
**Motion:** render 6 s. First domino pushed (init-qvel ω = 2 rad/s). Each subsequent domino topples with more energy. Final domino fall is dramatically larger. Camera: side view, wide angle.
**Template:** `dominoes.xml`. gen_domino_amplify.py computes positions and dimensions for each domino. Each domino is a separate body with box geom, hinge joint to the floor, correct inertial properties.
**Hints:** Spacing formula: d_i = h_i × sin(θ_fall) + t_{i+1}/2 where θ_fall ≈ 60° for typical aspect ratio. Total energy amplification: PE₁₂/PE₁ ≈ (1.5^11)² × m₁₂/m₁ ≈ 83. Domino sizes grow, so camera needs to adjust — use a dolly-zoom effect or very wide fovy = 70. See gotchas.md §domino_spacing.

---

#### `hourglass_granular_flow` — Granular flow / constant rate

**Physics:** In an hourglass, granular flow rate through the neck is roughly constant (independent of fill height for h >> neck radius) due to arching dynamics — unlike liquid flow (Torricelli's law) where rate decreases with height.
**Setup:** Two glass chambers (top: box 0.08 × 0.08 × 0.10 m; bottom: box 0.08 × 0.08 × 0.08 m) connected by a narrow neck (cylinder R = 0.006 m, length 0.02 m). Static glass geometry (no joints). 80 balls: R = 0.005 m, M = 0.002 kg, initially packed in the top chamber. Floor of top chamber is a funnel converging to the neck.
**Motion:** render 8 s. Balls flow one by one through the neck at a nearly constant rate. Top chamber empties, bottom chamber fills. Camera: front view with a cross-section cut showing internal flow.
**Template:** `rotating_fluid.xml` (container structure) + `marble.xml` (spherical balls). gen_hourglass.py constructs the glass geometry using box + cylinder geoms. Balls initialized using a grid pattern in the top chamber via gen script.
**Hints:** Neck radius must be > 2.5× ball radius for reliable flow (R_neck = 0.006, R_ball = 0.005 → barely 1.2× — increase to R_neck = 0.015). Ball packing in top chamber: use a grid with slight random jitter to avoid crystalline packing that blocks flow. Enable `solimp` settings that allow slight overlap for high ball counts. See gotchas.md §granular_packing and §neck_flow.

---

#### `tensegrity_prism` — Tensegrity / tension/compression

**Physics:** Tensegrity structures separate tension members (cables) from compression members (struts), with no bending moments at nodes; the triangular tensegrity prism remains rigid under load through this purely axial force distribution.
**Setup:** Triangular tensegrity prism: 3 compression struts (capsule geoms, L = 0.20 m, R = 0.008 m, M = 0.05 kg each) oriented at ~60° from vertical. 9 cables (tendons, stiffness k = 2000 N/m, rest length set so structure is in equilibrium). Top triangle (3 top nodes) + bottom triangle (3 bottom nodes), rotated 60° relative to each other. A load plate (M = 0.5 kg) rests on the top 3 nodes.
**Motion:** render 4 s. Load applied at t = 0 via the 0.5 kg plate. Structure compresses slightly and reaches static equilibrium. Camera: 3/4 isometric view showing all 6 nodes and 3 struts clearly.
**Template:** `atwood.xml` (tendons) + `block_overhang.xml` (rigid bodies). 6 node bodies (small spheres), 3 strut bodies (capsules), 9 tendons connecting nodes. All bodies have ball joints at nodes for the struts.
**Hints:** Tensegrity equilibrium requires precise tendon rest lengths and stiffness. Pre-compute the equilibrium geometry analytically: for a triangular prism with h = 0.15 m and triangle side s = 0.10 m, derive rest lengths of the 9 cables. Enable tendon damping = 2 to suppress vibration. See gotchas.md §tendon_equilibrium.

---

#### `cam_follower_simple` — Cam/follower mechanism

**Physics:** A rotating cam converts continuous rotational motion into oscillating translational motion; the follower displacement profile is determined entirely by the cam geometry — an elliptical cam gives a sinusoidal-like stroke.
**Setup:** Elliptical cam (modelled as an ellipsoid geom: a = 0.05 m, b = 0.03 m, along x and z in the cam's local frame) mounted on a hinge joint (y-axis) with init-qvel ω = 3 rad/s. A follower rod (box 0.01 × 0.01 × 0.08 m, M = 0.02 kg) on a slide joint (z-axis) rests on the cam surface under gravity. Cam and follower share a common xz-plane.
**Motion:** render 4 s (= 2 cam revolutions at ω = 3 rad/s). Follower moves up when the long axis of the ellipse comes around, down when the short axis is aligned. Stroke amplitude = a − b = 0.02 m. Camera: front view, fovy = 30.
**Template:** `gear_train_2_gears.xml` (hinge for cam rotation) + `spring_mass.xml` (slide joint for follower). Cam body: ellipsoid geom. Follower body: box geom with slide joint to world (z-axis). Follower rests on cam by gravity (no spring needed).
**Hints:** The follower must stay in contact with the cam — ensure follower mass (0.02 kg) provides enough contact force vs. cam acceleration. If contact is lost at high speed, add a light spring (k = 5 N/m) between follower and ceiling to maintain contact. Cam axle at z = 0.02 m above the floor; follower slide joint centred on same z-axis as cam. See gotchas.md §cam_contact_stability.

---

#### `marble_run_multistage` — Energy / multi-stage track

**Physics:** A marble run converts gravitational PE to KE on ramps, briefly stores KE as rotational energy on the helix, then delivers a collision to a target — demonstrating energy bookkeeping across multiple conversion stages.
**Setup:** Three-stage track: (1) Straight launch ramp, L = 0.5 m at 30° slope (height drop = 0.25 m). (2) Helical descent, 3 turns, helix radius R = 0.06 m, pitch 0.04 m/turn (total descent = 0.12 m, track length ~1.2 m). (3) Flat exit rail 0.2 m long leading to stationary target ball (M = 0.05 kg, R = 0.012 m). Marble: R = 0.010 m, M = 0.020 kg. Released from top of ramp.
**Motion:** render 5 s. Marble rolls down ramp, enters helix, spirals down, exits onto flat rail, and collides with target ball — which flies off. Camera: 3/4 isometric view capturing all three stages.
**Template:** `bead_on_helix.xml` (helix geometry) + `marble.xml` (ball) + `elastic_collision.xml` (target). gen_marble_run.py assembles all three track sections. Helix from `bead_on_helix.xml` gen script. Ramp and rail from box geoms.
**Hints:** Helix inner diameter must be > 2.5 × marble diameter (0.025 m vs. 0.02 m marble diameter — use R_helix = 0.06 m, tube inner R = 0.013 m). Marble transitions from ramp to helix: ensure smooth joint (chamfer the entry). At target collision, use stiff contacts for clean elastic bounce. See gotchas.md §helix_track and §track_transitions.

---

#### `angle_of_repose_comparison` — Granular / friction

**Physics:** The angle of repose of a granular pile equals arctan(μ_effective) — higher inter-particle friction gives steeper stable slopes. Two piles of identical balls with different friction coefficients settle at measurably different angles.
**Setup:** Two separate piles built on the same flat floor, separated by 0.4 m in x. Pile A: 40 balls (R = 0.010 m, M = 0.004 kg each), contact friction "0.2 0.005 0.001". Pile B: 40 balls, same geometry, contact friction "0.7 0.005 0.001". Balls dropped from z = 0.3 m directly above each pile centre, released one every 0.05 s via gen script.
**Motion:** render 5 s. Pile A settles into a low, flat mound (angle ~11°). Pile B forms a steep cone (angle ~35°). Side-by-side comparison clearly shows different repose angles. Camera: side view, wide (fovy = 50).
**Template:** `rotating_fluid.xml` (granular container idea, but here no container — open floor). gen_angle_of_repose.py drops 40 balls at specified intervals. Ball geoms with individual friction properties via `<geom friction="...">`.
**Hints:** Assign friction on the ball geom directly, not the floor. Contact friction between two surfaces uses the minimum of their individual friction values by default in MuJoCo — set both ball geom friction AND floor friction to the desired value for Pile A vs. B. Stagger the drop sequence so piles build naturally. Render long enough (5 s) for full settling. See gotchas.md §contact_friction_model.

---

#### `ball_in_toroidal_track` — Constrained circular motion

**Physics:** A ball constrained to roll inside a toroidal track converts gravitational PE to KE on descending segments, slows on ascending segments, and maintains circulation as long as minimum speed at the top is sufficient — analogous to a vertical loop but in a torus geometry.
**Setup:** Toroidal track: major radius R_t = 0.15 m (horizontal circle centre-to-centre), minor radius r = 0.018 m (tube inner radius). Track built from ~60 short curved box-segment tiles arranged in a torus (generated by gen_toroidal_track.py). Ball: R = 0.012 m, M = 0.010 kg. init-qvel: tangential v = 1.5 m/s along the torus tangent at the top of the torus cross-section (θ_minor = 90°, highest point).
**Motion:** render 5 s (≥ 2 full laps). Ball circulates around the torus, speeding up at the bottom of each minor arc and slowing at the top. Camera: 3/4 isometric top view to see the full torus, fovy = 45.
**Template:** `bead_on_helix.xml` (tube track geometry technique). gen_toroidal_track.py computes 60 segment positions and orientations around the torus. Each segment is a short box geom with appropriate position and rotation to approximate the inner torus surface.
**Hints:** Minimum speed for not losing track contact at the top of the minor circle: v_min = √(g·r) = √(9.81 × 0.018) ≈ 0.42 m/s. Launch at v = 1.5 m/s ensures multiple complete laps before slowing too much. Tube segments need chamfered edges to avoid ball catching on segment joints. See gotchas.md §tube_track_segments.

---

#### `elastic_longitudinal_wave_chain` — Longitudinal waves

**Physics:** A compressive impulse in a 1D mass-spring chain propagates as a longitudinal (P-wave) at speed v = √(k/m) × Δx — distinct from transverse waves in existing scenes; the compressions and rarefactions travel along the chain axis.
**Setup:** 30 masses (M = 0.01 kg each, box 0.010 × 0.010 × 0.010 m) spaced at Δx = 0.02 m along the x-axis. Each connected to its neighbours by a hinge joint with stiffness k = 1000 N/m along the x-direction (slide joints, not hinges). All slide joints constrained to x-axis only. Mass 0 (leftmost) given init-qvel vx = 1.5 m/s. All other masses stationary. No gravity (gravity = "0 0 0").
**Motion:** render 2 s. A compression wave propagates from left to right. Observe individual masses oscillating longitudinally (along x) as the wave passes. Wave speed v_theory = √(k·Δx²/m) = √(1000×0.0004/0.01) = √40 ≈ 6.3 m/s → wave traverses 30 × 0.02 = 0.6 m in ~0.1 s. Camera: top-down view (pos (0, 0, 0.5), fovy = 60), showing all 30 masses from above.
**Template:** `dominoes.xml` (chain of bodies) + `spring_mass.xml` (stiffness values). Bodies connected by slide joints (axis "1 0 0"), gravity disabled. gen_longitudinal_wave.py sets up all 30 bodies and joints.
**Hints:** Wave speed v = Δx × √(k/m) = 0.02 × √(1000/0.01) = 0.02 × 316 = 6.3 m/s. Render 2 s shows the wave traverse the chain ~20 times — use timestep = 0.0001 for accurate wave propagation. Distinguished from transverse wave scenes by motion direction (along chain axis, not perpendicular). See gotchas.md §longitudinal_waves.

---

### Package L — Granular, Multi-Body & Energy Transport (12)

#### `bowling_10pin_full` — Multi-body collision

**Physics:** A bowling ball strike initiates a cascade of rigid-body collisions among 10 pins; the exact outcome depends sensitively on ball entry point and angle — perfect centre strike often leaves corner pins standing due to deflection geometry.
**Setup:** Standard 10-pin triangle: pins in 4-3-2-1 formation, spacing 0.305 m (pin centre to centre). Each pin: capsule R = 0.028 m, half-height 0.077 m, M = 1.5 kg. Ball: sphere R = 0.108 m, M = 7.0 kg. Ball positioned 2.0 m in front of the head pin, init-qvel: vx = 5 m/s (along alley axis), vy = 0, vz = 0. Floor static friction 0.3. Pin bases ~0 m from floor (pins stand on the lane).
**Motion:** render 4 s. Ball strikes the head pin, cascade collision ensues. All 10 pins scatter. Camera: front view, pos (0, −3, 0.5), fovy = 38, looking down the alley.
**Template:** `bowling.xml`. gen_bowling_10pin.py places all 10 pins at regulation triangle positions. Each pin is an independent body with freejoint (falls over when hit). Ball has freejoint. High contact stiffness for authentic pin action.
**Hints:** Regulation pin spacing: 0.305 m. Triangle row positions: row 1 at y=0 (1 pin), row 2 at y=0.305 (2 pins, x=±0.1525), row 3 at y=0.61 (3 pins, x=0,±0.305), row 4 at y=0.915 (4 pins, x=±0.1525, ±0.4575). Ball launch 2 m in front of head pin. See gotchas.md §bowling_pin_contacts.

---

#### `bouncing_ball_cor_compare` — Coefficient of restitution comparison

**Physics:** The coefficient of restitution (CoR) determines what fraction of pre-collision normal velocity is retained after each bounce: h_n = CoR^(2n) × h_0. Different materials exhibit CoR from ~0.3 (clay) to ~0.95 (super ball).
**Setup:** Three identical balls (R = 0.03 m, M = 0.1 kg) dropped from z = 1.0 m, side by side at x = −0.3, 0, +0.3 m. Ball A (CoR ≈ 0.9): solref = "0.02 1", solimp = "0.99 0.999 0.001". Ball B (CoR ≈ 0.6): solref = "0.02 1", solimp = "0.80 0.90 0.001". Ball C (CoR ≈ 0.3): solref = "0.02 1", solimp = "0.50 0.60 0.001". Flat static floor.
**Motion:** render 5 s. All three balls dropped simultaneously. Ball A bounces high (h₁ ≈ 0.81 m), Ball B medium (h₁ ≈ 0.36 m), Ball C barely bounces (h₁ ≈ 0.09 m). After 5 s, A is still bouncing, C is nearly stationary.
**Template:** `coefficient_of_restitution.xml` (if present) or `bowling.xml`. Three ball bodies with individual geom-level solimp/solref. Verify CoR by measuring bounce heights in sim.
**Hints:** MuJoCo's `solimp` controls the effective CoR indirectly through the contact impedance model. Calibrate: drop a test ball and measure v_after/v_before from consecutive bounce heights. Typical tuning: solimp `d0` parameter near 0.99 gives near-elastic; near 0.5 gives highly inelastic. Stagger x by 0.3 m to prevent inter-ball interaction. See gotchas.md §coefficient_of_restitution_tuning.

---

#### `sand_pile_avalanche` — Granular / self-organized criticality

**Physics:** A sandpile at the angle of repose is in a state of self-organised criticality — adding a single grain can trigger an avalanche of any size. This scene demonstrates the threshold instability: a pile near repose + one perturbation = avalanche.
**Setup:** Initial conical pile: ~60 balls (R = 0.008 m, M = 0.001 kg each) arranged in a stable cone with slope angle ≈ 30° (just below repose for μ = 0.6). Cone height ≈ 0.06 m, base radius ≈ 0.10 m. Balls settled at t = 0 (via pre-simulation or direct placement). One extra ball (same specs) placed at the apex, z = z_top + 0.02 m, vx = 0.
**Motion:** render 3 s. Initial pile is stable. Extra ball lands on apex and triggers a cascade — several balls slide off one side, reorganising the pile into a lower-angle stable configuration.
**Template:** `rotating_fluid.xml` (granular pile technique). gen_sand_pile.py first builds the initial pile via simulation, then saves qpos as initial state. Extra ball added as a separate body. Friction: "0.6 0.005 0.001" for all balls and floor.
**Hints:** Building the initial pile at exactly the angle of repose requires careful friction tuning. Alternative: set friction lower (μ = 0.5), drop 60 balls, let settle, then add the extra ball — the existing slope will be below repose but the extra ball will still trigger local rearrangement. Add a reference line (thin static box) to mark the initial slope angle for visual comparison. See gotchas.md §pile_initialisation.

---

#### `spinning_disc_floor_wobble` — Precessing coin / Euler disk

**Physics:** A coin spinning on a flat surface exhibits a characteristic wobble where both the tilt angle and the precession rate increase as energy is dissipated by rolling friction — the precession frequency scales as f ∝ 1/√ε where ε is the tilt angle, diverging in the limit.
**Setup:** Flat disc (cylinder R = 0.05 m, thickness = 0.004 m, M = 0.05 kg, freejoint) on flat floor. init-qpos: disc tilted 20° from vertical (quaternion computed for 20° tilt about x-axis). init-qvel: freejoint velocity [0, 0, 0, 0, 0, 30] (vx=vy=vz=0, ωx=ωy=0, ωz=30 rad/s — spin about disc symmetry axis). Floor friction: `friction="0.25 0.005 0.001"`.
**Motion:** render 6 s. Disc initially wobbles and precesses with a stable cycle. Over time, tilt angle increases and precession rate increases dramatically. Near the end, very fast rattling precession followed by abrupt stop (disc flat on floor).
**Template:** `spinning_top.xml`. Replace the conical/spherical tip with a flat cylinder. Use freejoint. This is distinct from `euler_disk_spindown` (Package J) — here the initial tilt is larger (20° vs 3°) so the early wobble phase is clearly visible and more visually prominent.
**Hints:** The tilt of 20° makes the initial wobble large enough to photograph clearly. Rolling friction coefficient `solref="0.02 1"` with small rolling component (`solimp` third parameter = 0.001) provides realistic energy dissipation timescale. Total simulation time 6 s is sufficient to show the full lifecycle. See gotchas.md §euler_disk.

---

#### `rigid_body_3axis_stability` — Intermediate-axis theorem / all three axes

**Physics:** Euler's intermediate-axis theorem (Dzhanibekov effect): rotation about the major (longest) and minor (shortest) principal axes is stable; rotation about the intermediate axis is unstable — any perturbation causes the body to flip periodically.
**Setup:** Zero gravity (gravity = "0 0 0"). Three identical box bodies (0.30 × 0.15 × 0.05 m, M = 0.3 kg) at x = −0.4, 0, +0.4 m. Box (a) at x = −0.4: init-qvel ωx = 5 rad/s (longest axis — stable). Box (b) at x = 0: init-qvel ωy = 5 rad/s (intermediate axis — UNSTABLE, will flip). Box (c) at x = +0.4: init-qvel ωz = 5 rad/s (shortest axis — stable). All bodies with freejoint.
**Motion:** render 5 s. Box (a) and (c) spin cleanly about their respective axes. Box (b) initially spins, then begins to flip (~t = 1–2 s), and flips repeatedly. Camera: 3/4 isometric view showing all three boxes simultaneously.
**Template:** `dzhanibekov_effect.xml`. This extends the existing scene by showing all three axes simultaneously. Three bodies with freejoint, gravity off. Principal moments: I_x = m(y²+z²)/12 = 0.3×(0.0225+0.0025)/12 = 0.000625, I_y = m(x²+z²)/12 = 0.3×(0.09+0.0025)/12 = 0.002313, I_z = m(x²+y²)/12 = 0.3×(0.09+0.0225)/12 = 0.002813 kg·m².
**Hints:** Intermediate axis is y (intermediate I_y). Box (b) must be given a tiny perturbation off the pure y-axis (e.g., ωx = 0.01 rad/s) to seed the instability and trigger the flip within the 5 s render. Without perturbation, numerical noise will eventually trigger it but timing is unpredictable. See gotchas.md §dzhanibekov.

---

#### `billiard_trick_shot_curve` — Spin / friction-induced curve

**Physics:** A ball rolling with sidespin curves due to friction: the contact friction force has a component perpendicular to the direction of motion, equal to μ_k × N × (ω_z × R / v) — the "Magnus-like" friction curve experienced in billiards as the cue ball develops English.
**Setup:** Cue ball (R = 0.028 m, M = 0.17 kg, freejoint) on a flat table (z = 0). init-qpos: z = R (resting on table). init-qvel: vx = 2.0 m/s (forward), vy = 0, vz = 0, ωx = 0, ωy = 0, ωz = 15 rad/s (sidespin — top view clockwise). Table friction: `friction="0.4 0.01 0.005"`.
**Motion:** render 3 s. Ball rolls forward, gradually curving to the right (for positive ωz). The path is a visibly curved arc, not a straight line. Camera: top-down view, pos (0, 0, 0.8), fovy = 45.
**Template:** `marble.xml` + `incline_friction.xml` (friction model). Freejoint ball on flat floor (extend floor to 2 m × 2 m). The table surface is a static box, no slope.
**Hints:** The curve radius depends on friction: R_curve = v²/(μ × g × ω_z × R / v) ≈ v³/(μ × g × R × ω_z). With the given values: R_curve ≈ 8/0.4/9.81/0.028/15 ≈ 0.49 m — a tight curve. Use `solref="0.02 1"` for the contact. The ball will also experience rolling-without-slip transition (initially sliding, then rolling), which adds complexity. Top-down camera essential for visibility. See gotchas.md §spin_friction_curve.

---

#### `projectile_range_angle_sweep` — Projectile / optimal angle

**Physics:** For a projectile launched at speed v, range R(θ) = v²sin(2θ)/g — maximum at 45°, with complementary pairs (30° and 60°, 15° and 75°) giving equal range. This scene visualises the full angular sweep simultaneously.
**Setup:** Five balls (R = 0.015 m, M = 0.05 kg each, freejoint) launched from the same point (x = 0, z = 0.015). Launch speed v = 4 m/s. Launch angles: θ = 15°, 30°, 45°, 60°, 75° from horizontal. init-qvel for each: vx = 4cos(θ), vz = 4sin(θ), vy = 0. Floor is a long flat surface (5 m × 0.5 m). No air resistance.
**Motion:** render 2 s. Five balls fan out simultaneously, tracing five parabolic arcs. The 45° ball goes furthest (R = 1.63 m). The 30° and 60° balls land at equal range (R = 1.41 m). The 15° and 75° balls land closer (R = 0.82 m). Camera: side view, fovy = 50, wide enough to show all landing points.
**Template:** `projectile_jenga.xml`. Five freejoint ball bodies with individual init-qvel. Long static floor box (5 × 0.02 × 0.5 m). Side-view camera.
**Hints:** Predicted ranges: R(θ) = v²sin(2θ)/g = 16sin(2θ)/9.81. Confirm numerical results match theory. Separate balls in y by 0.05 m to avoid inter-ball collisions. Use thin markers (small static boxes) at predicted landing spots for educational value. Render time 2 s = slightly more than the longest flight time (t_45 = v sin(45°)/g × 2 = 0.58 s). See gotchas.md §projectile_setup.

---

#### `chain_whip_crack_tip` — Whip / velocity amplification

**Physics:** In a whip, momentum is conserved as wave energy travels from a heavy base to a lighter tip — with decreasing mass per unit length, the wave speed increases and tip velocity can exceed the initial handle velocity by a factor of ~10.
**Setup:** 20-link chain with decreasing link masses. Link i (i = 1 to 20) has mass m_i = 0.02 × (21 − i) / 20 kg (linear gradient: link 1 = 0.020 kg, link 20 = 0.001 kg). All links: box 0.015 × 0.015 × 0.03 m (length scales with mass for constant density). Links connected by hinge joints (y-axis). Link 1 (base) given init-qvel vx = 3 m/s. All other links initially at rest. No gravity (or include gravity for a more realistic droop effect — include it for realism).
**Motion:** render 1.5 s. The velocity impulse propagates from the heavy base toward the light tip. The tip's speed at impact can be estimated as v_tip ≈ v_base × (m_base/m_tip)^(1/2) ≈ 3 × √20 ≈ 13 m/s. Camera: side view capturing the full chain length.
**Template:** `dominoes.xml` (chain of bodies). gen_whip_chain.py constructs the 20 links with decreasing masses. Hinge joints with low damping. init-qvel on link 0 body only.
**Hints:** Use low joint damping (0.001) to preserve the wave amplification. The velocity amplification formula (impedance mismatch model) gives v_tip/v_base ≈ √(m_1/m_N) for ideal chain — numerical result will be lower due to damping and bending losses. If gravity is included, orient the chain horizontally (along x) with init-qpos so all links start in-line. See gotchas.md §chain_wave_propagation.

---

#### `elastic_wave_2d_grid_pulse` — 2D wave propagation

**Physics:** A 2D mass-spring grid with fixed boundaries supports circular wave fronts after a central impulse; the wave speed is isotropic in the limit of small spacing and the circular ripple expands at v = Δx × √(k/m).
**Setup:** 7×7 grid of masses (M = 0.005 kg each) on slide joints (z-axis only) with spacing 0.03 m in x and y. Adjacent masses connected by stiff springs (k = 500 N/m, implemented as hinge stiffness or actuator springs). Edge masses (border of the 7×7 grid) have their slide joint fixed to world (range = "0 0"). Central mass (position [3,3]) given init-qvel vz = 0.5 m/s. No gravity (gravity = "0 0 0" to isolate wave from sag).
**Motion:** render 3 s. A circular ripple radiates outward from the central mass, reflects off the fixed boundaries, and creates interference patterns. Camera: top-down, pos (0, 0, 0.5), fovy = 45 (looking straight down), showing all 49 masses.
**Template:** `gen_pendulum_waves.py` (adapted for 2D grid). gen_elastic_grid.py creates 49 bodies, 2×(7×6) spring connections (horizontal and vertical), fixed edge joints. Slide joints along z only. Springs between adjacent bodies use actuator (position spring) or joint stiffness.
**Hints:** Wave speed v = 0.03 × √(500/0.005) = 0.03 × 316 = 9.5 m/s → wave crosses 7×0.03 = 0.21 m in 0.022 s. The wave will traverse the grid many times in 3 s, creating complex standing-wave patterns. This is the main visual payoff: concentric ripples + reflection interference. See gotchas.md §2d_spring_grid.

---

#### `multi_ball_chain_different_mass` — Momentum / mass gradient collision

**Physics:** Newton's cradle with non-uniform masses violates the simple elastic transfer rule; the momentum wave couples into multiple outgoing velocities determined by the full N-body elastic collision equations, showing mass mismatch effects on momentum transport.
**Setup:** Five hanging balls with masses 0.05, 0.10, 0.15, 0.20, 0.25 kg left to right (all R = 0.020 m, uniform geometry). A 6th ball (M = 0.05 kg, same geometry) swings in from the left at v = 2 m/s (init-qvel on its hinge). All balls suspended on strings (length 0.25 m) from a common ceiling bar, spacing 0.042 m (just touching at rest).
**Motion:** render 3 s. Incoming light ball (6th) strikes the left end of the chain. Unlike a uniform cradle, the momentum wave does not cleanly transfer to the rightmost ball — multiple balls on the right end move with different velocities. Observe which ball(s) emerge fastest.
**Template:** `newton_cradle.xml` + `elastic_collision.xml`. Six ball bodies on hinge-joint strings. Individual mass values. Stiff contact parameters. Side view.
**Hints:** Theoretical prediction for elastic collision of mass m₁ striking stationary m₂: v₂' = 2m₁v₁/(m₁+m₂) — but in a chain it's more complex. The lightest incoming ball (0.05 kg) hitting the 0.05 kg ball should initially have near-elastic transfer to that ball. Increasing masses to the right will show progressive slowing of the momentum wave. See gotchas.md §mass_gradient_cradle.

---

#### `tipping_block_thin_wide_compare` — Statics / tipping criterion

**Physics:** A block tips if its centre of mass projects outside its base before the block slides; tip-vs-slide depends on aspect ratio: wide blocks slide (low COM projection overhang needed), tall blocks tip (high torque, easy COM overhang). Critical angle for tipping: θ_tip = arctan(w/(2h)).
**Setup:** Three blocks of equal mass M = 0.5 kg on a ramp, static friction μ = 0.3 for all. Block A (wide): 0.20 × 0.04 × 0.08 m (w × d × h), θ_tip = arctan(0.10/0.04) = 68° — much more than θ_slide = arctan(0.3) = 17°: slides. Block B (square base): 0.08 × 0.04 × 0.08 m, θ_tip = arctan(0.04/0.04) = 45° > 17°: marginal but slides first. Block C (tall): 0.04 × 0.04 × 0.20 m, θ_tip = arctan(0.02/0.10) = 11° < 17°: tips before sliding.
**Motion:** render 3 s. Ramp init-qvel tilts at 3 rad/s. Block C tips first (~t ≈ 0.7 s). Block A slides from the start. Camera: side view showing all three blocks.
**Template:** `incline_friction.xml` + `tipping_vs_sliding.xml`. Three block bodies on a hinge-joint ramp. Individual block dimensions and inertial properties. Same μ = 0.3 floor friction.
**Hints:** Recalculate θ_tip for each block: arctan(half-base-width / half-height). Ensure block dimensions give clearly distinct outcomes. The ramp tilt rate 3 rad/s = reaching 17° in ~0.1 s (very fast) — reduce to 0.5 rad/s for a clearer visual. Check: a ramp hinge joint with init-qvel OR use a motor actuator ramping angle. See gotchas.md §tipping_vs_sliding.

---

#### `pendulum_wave_decay_pattern` — Coupled waves / damping asymmetry

**Physics:** A pendulum wave machine with heterogeneous damping exhibits asymmetric pattern decay: heavily-damped pendulums on one side lose their oscillations quickly, while lightly-damped ones persist, creating a travelling degradation of the wave pattern.
**Setup:** 15 pendulums (L from 0.28 to 0.42 m tuned for 10 oscillations per pattern period on the right end). Each pendulum on a hinge joint. Damping gradient: pendulums 1–5 (left): `damping="0.5"`, pendulums 6–10 (middle): `damping="0.1"`, pendulums 11–15 (right): `damping="0.01"`. All released simultaneously from 15° amplitude.
**Motion:** render 15 s. Initial wave pattern forms as in `pendulum_waves.xml`. After ~5 s, the left side (heavy damping) pendulums lose amplitude; the pattern degrades from the left, creating an asymmetric visual — the right side still waves while the left side is nearly still.
**Template:** `pendulum_waves.xml`. Apply a damping gradient over the 15 hinge joints. No other changes. Side view or slight 3/4 view to see the wave pattern.
**Hints:** 15 pendulums with lengths tuned for the wave pattern: L_i = g/(2π × f_i)² where f_i varies from f_1 to f_15 to give 9 to 10 oscillations per 15 s pattern period. Heavy damping γ = 0.5 means amplitude halves in ~2 s (e-folding time = 1/γ = 2 s). Light damping γ = 0.01 means amplitude barely changes over 15 s. See gotchas.md §pendulum_wave_tuning.

---

### Package M — Structures, Stability & Special Motion (12)

#### `spinning_top_sleep_to_fall` — Top lifecycle

**Physics:** A spinning top's "sleeping" state (upright spin axis) is stable only above a critical spin rate ω_crit = 2√(MgℓI_transverse)/I_axial; as friction dissipates the spin, the sleeping state destabilises, nutation grows, and the top eventually falls.
**Setup:** Standard top (M = 0.3 kg, tip at origin, COM at ℓ = 0.03 m above tip, I_axial = 5×10⁻⁴ kg·m², I_transverse = 3×10⁻⁴ kg·m²). Freejoint with ball tip contacting floor. init-qpos: perfectly vertical (no tilt). init-qvel: spin ω = 80 rad/s about symmetry axis. Floor friction: `friction="0.15 0.002 0.001"` (low rolling friction to dissipate spin slowly over 8 s).
**Motion:** render 8 s. Phase 1 (t = 0–4 s): top spins stably upright (sleeping state). Phase 2 (t ≈ 4 s): nutation slowly appears as spin drops below ω_crit. Phase 3 (t = 4–7 s): precession and growing nutation. Phase 4 (t ≈ 7–8 s): rapid tumbling and fall.
**Template:** `spinning_top.xml`. Tune floor friction to give the desired spin-down timescale. ω_crit = 2√(MgℓI_t)/I_a = 2√(0.3×9.81×0.03×3×10⁻⁴)/(5×10⁻⁴) ≈ 25 rad/s.
**Hints:** The key challenge is getting the right friction coefficient so the spin decays from 80 to 25 rad/s in about 4 s. Rolling friction is the main dissipation mechanism for a top (sliding friction at the tip is zero for a perfectly upright top). Start with `friction="0.1 0.003 0.001"` and adjust third parameter (rolling). See gotchas.md §spinning_top_lifecycle.

---

#### `gyroscope_resists_tipping` — Gyroscopic stabilization

**Physics:** A fast-spinning gyroscope resists applied torques by precessing perpendicular to the applied force — a torque about the x-axis causes precession about the z-axis rather than tipping about x; this gyroscopic rigidity is the basis for gyro stabilizers and navigation instruments.
**Setup:** Gimbal frame (box 0.20 × 0.01 × 0.10 m, M = 0.1 kg) connected to world via hinge (x-axis). Gyro disc (R = 0.07 m, M = 0.3 kg, thickness 0.01 m) inside frame on a second hinge (y-axis). init-qvel: disc spin ω = 80 rad/s about y-axis. init-qpos: frame horizontal (0°). At t = 0.5 s, an impulsive force F = 5 N for 0.1 s applied to frame in z-direction (pushing it sideways).
**Motion:** render 5 s. Without spin: frame would simply tip and swing about the x-axis hinge. With spin (ω = 80): instead, frame precesses about z (rotates in the horizontal plane) — the gyro resists the tipping. Camera: 3/4 view, pos (0.4, −0.4, 0.3).
**Template:** `spinning_top.xml` + `conical_pendulum.xml` (gimbal structure). Frame body with hinge (x-axis) to world. Gyro disc body with hinge (y-axis) to frame. Apply the impulse force in the gen script using `mj_applyFT` at the specified time.
**Hints:** Precession rate Ω_p = τ/(I·ω) = F·r/(I·ω) = 5×0.1/(½×0.3×0.07²×80) ≈ 5×0.1/0.0588 ≈ 8.5 rad/s. This means the frame rotates ~4.25 rad in 0.5 s — clearly visible. The gyro effectively "stores" the applied torque as precession momentum. See gotchas.md §gyroscope_precession.

---

#### `spinning_football_stabilized` — Gyrostabilization / prolate body

**Physics:** A prolate body thrown without spin tumbles chaotically (Dzhanibekov instability about the intermediate axis); the same body thrown with a fast spin about its long axis becomes gyroscopically stable and maintains its orientation throughout the flight.
**Setup:** Two prolate ellipsoids (a = 0.11 m semi-major, b = c = 0.035 m semi-minor, M = 0.4 kg, freejoint) in free flight. Same translational launch: vx = 2.0 m/s, vz = 1.0 m/s (giving a parabolic arc over ~0.4 s). Ellipsoid A (no-spin): no rotational init-qvel. Ellipsoid B (spinning): init-qvel includes ωx = 30 rad/s (spin about symmetry axis). Both launched from z = 0.5 m, separated by y = 0.3 m.
**Motion:** render 2 s. Ellipsoid A tumbles chaotically. Ellipsoid B maintains its orientation with the nose pointing consistently along the velocity direction (or at a slight angle). Camera: side view, fovy = 45.
**Template:** `dzhanibekov_effect.xml` (freejoint + gravity). Replace box with ellipsoid geom (`type="ellipsoid" size="0.11 0.035 0.035"`). Include gravity (default). Two separate freejoint bodies.
**Hints:** For the spinning case, the gyroscopic stability condition: ω_spin > ω_tumble × √(I_transverse/I_axial). With ω_spin = 30 rad/s and typical tumble rate ~5 rad/s, this is well satisfied. The Dzhanibekov flip period for the non-spinning case (just translating, no spin) will be purely random/chaotic — add tiny initial angular velocity (ωy = 0.5 rad/s) to seed tumbling for ellipsoid A. See gotchas.md §gyrostabilization.

---

#### `coin_edge_rolling_curve` — Rolling / banking

**Physics:** A coin rolling along a curved track leans into the curve at a banking angle φ = arctan(v²/(gR_curve)) — the same angle a bicycle leans when cornering. Higher speed or tighter curve requires more lean.
**Setup:** Curved track: a 90° arc of radius R_curve = 0.5 m, track width 0.02 m, generated by gen_curved_track.py as ~20 box segments. Coin: cylinder R = 0.030 m, thickness = 0.003 m, M = 0.010 kg, freejoint. init-qpos: coin at the start of the curve, upright (zero tilt). init-qvel: tangential v = 1.0 m/s. Rolling-without-slip condition: ωy = v/R_coin = 33.3 rad/s. Contact friction: "0.5 0.01 0.005".
**Motion:** render 4 s. Coin enters the curved track, leans inward, and rolls through the curve maintaining upright balance (if v is sufficient). For v = 1.0 m/s: φ_theory = arctan(1²/(9.81×0.5)) = 11.5°. The coin exhibits this lean visibly. After the curve, coin rolls straight again.
**Template:** `marble.xml` + `bead_on_helix.xml`. gen_curved_track.py creates the curved track as ~20 short box segments in a 90° arc, each rotated appropriately. Coin has freejoint, initial spin set for rolling-without-slip.
**Hints:** The coin will likely wobble and possibly fall without the track providing lateral support — build the track as a narrow channel (two parallel rail strips) 0.025 m apart so the coin is guided. Initial spin must match rolling-without-slip or the coin will skid. See gotchas.md §coin_rolling_setup.

---

#### `leaning_tower_mass_distribution` — Stability / COM height

**Physics:** A tower tips when its centre of mass projects outside its base; towers with higher COMs require less tilt to reach the tipping threshold. For a uniform tower, tipping angle θ_tip = arctan(w/(2h)); lowering the COM raises the tipping angle (more stable).
**Setup:** Three towers (each 0.10 × 0.10 × 0.5 m total, M = 0.5 kg) on a slow-tilting ramp. Tower A: uniform density, COM at h/2 = 0.25 m, θ_tip = arctan(0.05/0.25) = 11.3°. Tower B: heavy-bottom (COM at 0.10 m height, composite of 0.4 kg at bottom 0.1 m + 0.1 kg at top 0.4 m), θ_tip ≈ 27°. Tower C: heavy-top (COM at 0.40 m), θ_tip ≈ 7.1°. Ramp tilts at ω = 0.3 rad/s.
**Motion:** render 5 s. Ramp tilts gradually. Tower C tips first at ~7.1° (~t = 0.4 s). Tower A tips at ~11.3° (~t = 0.75 s). Tower B tips last at ~27° (~t = 1.5 s). Camera: side view showing all three towers and the ramp.
**Template:** `dominoes.xml` + `tipping_vs_sliding.xml`. Three tower bodies modelled as composite bodies (two box geoms with different densities) to achieve different COM heights. Ramp body with a hinge joint to world and init-qvel or motor.
**Hints:** Ensure tower bases have enough friction to prevent sliding before tipping: μ > tan(θ_tip) for tipping to occur before sliding. For Tower B: μ > tan(27°) = 0.51 — use μ = 0.7 for all. For Tower C: μ > tan(7.1°) = 0.12 — easily satisfied. Set ramp friction accordingly. See gotchas.md §composite_body_com.

---

#### `trebuchet_simple` — Projectile / mechanical advantage

**Physics:** A trebuchet converts the gravitational PE of a heavy counterweight into projectile KE via mechanical advantage from an unequal-arm lever; ideal efficiency gives projectile speed v_proj = v_cw × √(M_cw/m_proj) × (L_long/L_short).
**Setup:** Trebuchet arm (total length 0.75 m) pivoted at 0.15 m from the counterweight end. Counterweight: M_cw = 2 kg hanging at the short arm (L_short = 0.15 m). Sling: tendon length L_sling = 0.25 m connecting long arm tip to projectile. Projectile: M_proj = 0.05 kg, R = 0.015 m. init-qpos: counterweight up (arm horizontal, counterweight side high), sling hanging down with projectile resting in a cup.
**Motion:** render 2 s. Counterweight falls, arm rotates, sling whips the projectile upward and releases it (~t = 0.3 s). Projectile follows a high-speed ballistic arc. Camera: side view, wide fovy = 60 to capture full arc.
**Template:** `pendulum.xml` (arm pivot) + `atwood.xml` (counterweight and sling tendon). gen_trebuchet.py assembles the arm body (box geom), counterweight body on a tendon, and sling tendon with projectile. Arm hinge joint (y-axis) to world support frame.
**Hints:** Predicted projectile speed: v ≈ √(2 × M_cw × g × L_short) × L_long/L_short / √m_proj = √(2×2×9.81×0.15) × 0.60/0.15 / √0.05 ≈ √5.886 × 4/0.224 ≈ 105 m/s (unrealistically high for this scale — reduce M_cw to 0.3 kg for v ≈ 13 m/s). The sling release is implemented when the sling attachment angle triggers automatic detach (sling tip exceeds a threshold angle). See gotchas.md §sling_release.

---

#### `ball_in_rotating_bowl_spiral` — Rotating frame / equilibrium radius

**Physics:** In a parabolic bowl rotating at angular velocity ω, a ball finds a stable circular orbit at radius r_eq where the centrifugal "force" mω²r balances the bowl's restoring slope force mg × dz/dr = mg × 2ar; equilibrium at r_eq = √(g/(2aω²)).
**Setup:** Parabolic bowl z = 5r² (a = 5 m⁻¹) rotating at ω = 6 rad/s about its vertical axis. Bowl built from ~40 box segments arranged in a paraboloid pattern (gen_rotating_bowl.py). Ball: R = 0.015 m, M = 0.050 kg, freejoint. init-qpos: ball at r = 0.12 m from bowl axis, z = 5×0.12² = 0.072 m on the bowl surface. init-qvel: bowl-frame tangential velocity for co-rotation at r = 0.12 m.
**Motion:** render 6 s. Ball starts at r = 0.12 m (above equilibrium) and spirals inward (or outward if friction > centrifugal). Equilibrium r_eq = √(9.81/(2×5×36)) = √(9.81/360) ≈ 0.165 m → ball is at r = 0.12 < r_eq, so it should spiral outward toward equilibrium. Camera: 3/4 isometric top view.
**Template:** `rotating_fluid.xml`. Replace fluid content with a single ball. Bowl geom from gen_rotating_bowl.py. Bowl body has a hinge joint (z-axis) with `velocity="6"` motor or init-qvel.
**Hints:** r_eq = √(g/(2aω²)) = √(9.81/(2×5×36)) = 0.165 m. Start ball at r = 0.12 m (inside r_eq) — it should spiral outward. Start at r = 0.20 m — it spirals inward. Use a motorised bowl hinge with velocity control to maintain constant ω despite ball reaction forces. See gotchas.md §rotating_bowl_equilibrium.

---

#### `double_pendulum_mode_shapes` — Normal modes / eigenfrequencies

**Physics:** A linearised double pendulum has two normal modes: symmetric (both links swing in phase at ω₋ — lower frequency) and antisymmetric (links out of phase at ω₊ — higher frequency); pure mode initial conditions give periodic (non-chaotic) motion.
**Setup:** Double pendulum: L₁ = L₂ = 0.3 m, M₁ = M₂ = 0.1 kg. Normal mode frequencies (equal masses and lengths): ω₋ = √(g(2−√2)/L) = √(9.81×0.586/0.3) ≈ 4.38 rad/s; ω₊ = √(g(2+√2)/L) ≈ 11.55 rad/s. Two side-by-side renderings: (a) Symmetric: θ₁ = θ₂ = 20°, angular velocities from eigenmode. (b) Antisymmetric: θ₁ = 20°, θ₂ = −20°. Both small-angle to validate linear modes.
**Motion:** render 5 s. (a) both links swing together at ω₋ — slower, synchronized. (b) links swing against each other at ω₊ — faster, opposing. Camera: front view, wide enough to see both pendulums side by side.
**Template:** `double_pendulum.xml`. Two copies side by side (x-offset 0.4 m). Set init-qpos for each copy to the respective mode shape (θ₁, θ₂ pairs). Use small angles (20°) to stay in linear regime.
**Hints:** Symmetric mode period T₋ = 2π/ω₋ ≈ 1.43 s. Antisymmetric mode period T₊ = 2π/ω₊ ≈ 0.54 s. In a 5 s render: symmetric completes ~3.5 cycles, antisymmetric ~9 cycles. The ratio of periods (2.6:1) is visually striking. Keep angles small (≤ 20°) to maintain pure mode shape. Use `integrator="RK4"` for accuracy. See gotchas.md §normal_modes.

---

#### `inverted_pendulum_cart_balance` — Instability / coupled motion

**Physics:** An inverted pendulum on a free cart is unstable but the cart's reactive motion creates a brief delay in the fall — the cart accelerates in the direction of the falling rod, reducing the effective gravitational torque momentarily before the pendulum inevitably falls.
**Setup:** Cart (M = 1 kg, box 0.20 × 0.05 × 0.05 m) on a slide joint (x-axis, frictionless). Inverted rod (L = 0.5 m, M = 0.3 kg) pinned at the cart top by a hinge (y-axis), pointing upward. init-qpos: rod tilted 3° from vertical (toward +x). init-qvel: zero for both cart and rod. No friction on cart slide joint.
**Motion:** render 2 s. Rod falls toward +x. Cart slides to +x (reaction). Rod falls faster than it would without the free cart — but the reactive cart motion is visible. Compare mentally with a fixed-pivot inverted pendulum: the cart provides a temporary but ultimately futile reactive force. Camera: side view, fovy = 40.
**Template:** `pendulum.xml` (inverted configuration) + `block_on_accelerating_wedge.xml` (sliding cart). The rod hinge at the top of the cart body. Cart body connected to world via slide joint (x-axis). Hinge joint at cart top: rod points up (init-qpos = π for inverted), gravity will pull it to fall.
**Hints:** Inverted pendulum init-qpos: set hinge joint angle = π − 0.0524 rad (≈ 177° from downward vertical = 3° from inverted vertical). Alternatively, use qpos = 0.0524 and flip pendulum geometry (attach point at bottom, rod upward). The fall time from 3° is approximately t_fall ≈ 1/ω × ln(2θ/θ₀) ≈ 0.9 s (where ω = √(g/L)). See gotchas.md §inverted_pendulum.

---

#### `chain_lasso_circular` — Rotating chain / steady state

**Physics:** A chain rotating at constant ω forms a circular shape in the horizontal plane — each link is in centripetal force balance where the tension in the inner links provides centripetal acceleration for all the mass further out.
**Setup:** 20-link chain, M = 0.01 kg per link, link length 0.025 m. Link 0 (innermost) connected to a fixed pivot via a hinge joint (z-axis) with motor velocity = 8 rad/s. Links connected by hinge joints with y-axis (allowing in-plane spreading). All joints in the horizontal plane (gravity = "0 0 0" or arrange so chain lies in xy-plane). init-qpos: chain initially straight along x.
**Motion:** render 4 s. From the initial straight configuration, the chain rotates and gradually settles into a circular loop (each link at equal radius from pivot). At steady state, the outer links are at maximum radial displacement due to centripetal tension. Camera: top-down, pos (0, 0, 0.6), fovy = 50.
**Template:** `conical_pendulum.xml` + `dominoes.xml` (chain of bodies). 20 bodies with hinge joints. Innermost hinge to world with velocity motor ω = 8 rad/s. Chain in horizontal plane.
**Hints:** Equilibrium radius: each link at radius r_i is in balance when tension T_i = m × ω² × (sum of r_j for j ≥ i). For uniform chain, the equilibrium shape is approximately circular with total radius R_total = chain_total_length × 2/(π) for half-circle, or chain_length/2π for a full circle. With 20 links × 0.025 m = 0.5 m total, circle circumference ≈ 0.5 m → R ≈ 0.08 m. Use `gravity="0 0 0"` to keep chain in horizontal plane. See gotchas.md §rotating_chain.

---

#### `pendulum_clock_escapement_simple` — Mechanism / feedback

**Physics:** The escapement converts continuous rotational energy (from the falling weight) into discrete angular impulses, regulated by the pendulum — each pendulum half-swing allows the ratchet wheel to advance exactly one tooth, creating the characteristic tick-tock rhythm.
**Setup:** Ratchet wheel (12 teeth, R = 0.06 m, M = 0.1 kg, hinge y-axis). Anchor escapement (two-arm lever, hinge y-axis on the same shaft as pendulum, but offset). Pendulum (L = 0.25 m, M = 0.05 kg, hinge y-axis). Driving weight (M = 0.5 kg) on a string (tendon) wrapped around the wheel axle (R_axle = 0.008 m). All in the xz-plane. The anchor alternately locks and unlocks the ratchet wheel with each pendulum swing.
**Motion:** render 5 s (≥ 4 pendulum ticks). Each pendulum half-swing: anchor releases one ratchet tooth, wheel advances 30°, anchor re-engages. Driving weight descends ~3 mm per tick. Camera: front view, fovy = 35.
**Template:** `geneva_drive.xml` (intermittent rotation concept) + `ratchet_pawl.xml` (if exists) + `pendulum.xml`. gen_escapement.py assembles geometry. Key: the anchor-to-wheel contact is the critical interaction — use stiff contacts between anchor pallet faces and ratchet teeth.
**Hints:** Escapement geometry is intricate — the anchor pallet faces must contact the ratchet tooth flanks at the correct angles to deliver an impulse AND lock. Alternatively, implement the escapement using equality constraints that are conditionally activated based on pendulum angle (programmatic approach in gen script). The pendulum period T = 2π√(L/g) = 2π√(0.25/9.81) ≈ 1.0 s. See gotchas.md §escapement_contacts.

---

#### `roller_coaster_loop_minimal` — Centripetal / critical speed

**Physics:** Minimum speed to complete a circular loop: v_min at the top = √(gR), where R is the loop radius. A ball released from height h_min = 5R/2 just barely makes it; from h < h_min it falls off before the top.
**Setup:** Two side-by-side tracks: (a) Launch ramp at 30° slope, height H_a = 5R/2 + ramp_start = 0.375 m + small clearance. (b) Same geometry but H_b = 0.25 m (below critical). Both tracks: straight ramp (1.0 m long) → circular loop (R = 0.15 m). Ball: R = 0.020 m, M = 0.050 kg, freejoint. Tracks as box-geom rails (channel tracks).
**Motion:** render 3 s. Ball (a) released from H_a: rolls down ramp, enters loop, completes the full 360° loop, exits. Ball (b) from H_b: enters the loop, slows, and detaches from the track before reaching the top — falls into the interior. Camera: side view, fovy = 45, showing both tracks.
**Template:** `loop_the_loop.xml` + `brachistochrone.xml` (ramp). Two complete track setups side by side (y-offset 0.25 m). Ball freejoint for each. Channel track (two rails) guides balls.
**Hints:** h_min = 5R/2 = 5×0.15/2 = 0.375 m for a point mass. With a rolling ball (solid sphere), the actual h_min = 5R/2 + 2R/5 × R/(R_ball) (rolling correction) ≈ 0.377 m. Ball (b) set to H = 0.25 m gives v_top < 0 (doesn't make it). Track must be a closed channel (not just a flat ramp) for the ball to stay on past the inverted section. See gotchas.md §loop_track_closure.

---

## 🟤 Round 4 — Packages N / O (24 scenes)

### Package N — Resonance, Rotating Frames & Wave Phenomena (12)

#### `resonance_forced_oscillation` — Resonance / driven oscillator

**Physics:** A spring-mass oscillator driven at its natural frequency ω₀ = √(k/m) builds amplitude without bound (in the absence of damping). Off-resonance driving at 0.7·ω₀ produces only bounded, small-amplitude oscillation.
**Setup:** Two side-by-side spring-masses: M = 0.1 kg, k = 100 N/m, ω₀ ≈ 31.6 rad/s. Both masses on slide joints along z with stiffness=100. gen_resonance.py injects a periodic impulse (qvel += A·sin(ω_drive·t)·dt each step) at ω_drive = ω₀ for Mass A and ω_drive = 0.7·ω₀ for Mass B. Amplitude A = 0.02 m/s per step, timestep 0.001 s. No damping on either joint.
**Motion:** Render 15 s. Mass A amplitude grows steadily (resonance). Mass B oscillates at small bounded amplitude. Camera: side view, fovy = 45, showing both oscillators.
**Template:** `spring_mass.xml`. Two copies x-separated 0.3 m. gen_resonance.py drives each at its respective frequency.
**Hints:** MuJoCo has no built-in sinusoidal actuator. Implement via gen script that writes qpos/qvel into the model at each step using mujoco.mj_step. Alternatively, attach a driver mass to a long massless rod and give it circular initial conditions — the vertical component acts as a sinusoidal force. See gotchas.md §forced_oscillation.

---

#### `resonance_damping_compare` — Q factor / damping regimes

**Physics:** Three oscillators with different damping coefficients γ driven at their natural frequency show vastly different steady-state amplitudes. High Q (low damping) → large amplitude; overdamped → barely moves.
**Setup:** Three spring-masses, identical k = 100 N/m, M = 0.1 kg. Joint damping: (a) γ = 0.01 (underdamped, Q ≈ 50), (b) γ = 0.63 (critically damped, Q = 1), (c) γ = 2.0 (overdamped). All three driven at ω₀ via gen_resonance.py as above.
**Motion:** Render 20 s. Oscillator (a) builds large amplitude. (b) barely responds. (c) no oscillation. Camera: side view showing all three.
**Template:** `spring_mass.xml` ×3. Adjust joint damping values.
**Hints:** Q = ω₀·M/γ. For clean demo, run at least 20 s so the high-Q oscillator has time to build up significant amplitude. x-separation 0.3 m between each pair.

---

#### `wave_dispersion_chain` — Dispersion relation / frequency-dependent speed

**Physics:** In a uniform spring chain (linear dispersion at low frequency, but nonlinear at high k), a Gaussian pulse travels without spreading. In a chain with alternating spring constants k₁/k₂, the dispersion relation has a bandgap — the pulse spreads and slows as high-frequency components travel at different speeds.
**Setup:** Two 40-body chains side by side (x-separation 0.3 m). Chain A: uniform k = 500 N/m between all links, damping = 0. Chain B: alternating k₁ = 200 N/m, k₂ = 800 N/m. All bodies M = 0.01 kg on slide joints z. Both chains receive the same initial Gaussian displacement pulse: z_i = 0.02·exp(-(i-5)²/2) for i = 0..39, others at z = 0.
**Motion:** Render 3 s. Chain A pulse travels cleanly. Chain B pulse spreads into multiple components that travel at different speeds. Side view, both chains visible.
**Template:** `wave_reflection_fixed.xml` (discretized chain). gen_dispersion_chain.py for alternating k setup.
**Hints:** Alternating masses also create dispersion (acoustic vs optical branches). Use alternating k (simpler) rather than alternating mass. Timestep 0.0005 for stability.

---

#### `melde_harmonic_3modes` — String harmonics / standing wave modes

**Physics:** A discretized string (both ends fixed) initialized in the shape of its nth harmonic mode oscillates in a pure standing wave. The 1st mode has one antinode (λ = 2L), 2nd has two antinodes (λ = L), 3rd has three (λ = 2L/3). All at different frequencies.
**Setup:** Three discretized strings side by side (x-separation 0.25 m), each 40 nodes, total length L = 0.50 m, both ends fixed (world weld). Each node M = 0.005 kg on slide joint z, stiffness k = 200 N/m between neighbors. init-qpos: z_i = A·sin(n·π·i/39) for n = 1, 2, 3 respectively. A = 0.025 m. Damping = 0 on all joints.
**Motion:** Render 4 s. Each string oscillates cleanly in its mode shape. Camera: front view, fovy = 50, all three strings visible.
**Template:** `standing_wave_on_string.xml`. Three copies with different init-qpos.
**Hints:** Node spacing must be small enough to resolve the 3rd harmonic — 40 nodes easily resolves 3 antinodes. Period of mode n: T_n = 2L/(n·v) where v = √(k·L_seg/M). Ensure natural frequency matches actual MuJoCo frequency with chosen k.

---

#### `coriolis_turntable_puck` — Rotating frame / Coriolis deflection

**Physics:** A puck launched radially on a frictionless rotating turntable travels in a straight line in the lab frame but traces a curved path in the rotating frame — demonstrating the Coriolis pseudoforce.
**Setup:** Rotating disc (R = 0.25 m, M = 2 kg, thickness 0.01 m) on a fixed vertical hinge with init-qvel ω = 2 rad/s. Puck (R = 0.015 m, M = 0.05 kg) placed on the disc surface at r = 0.05 m from center with init-qvel vr = 0.3 m/s radially outward (in the lab frame). Disc-puck contact: friction = 0. Disc hinge damping = 0.
**Motion:** Render 4 s. Puck slides outward and off the disc edge. Camera: directly top-down, fovy = 60. Marker on puck traces the curved path visible against disc markings (colored sectors painted on disc geom).
**Template:** `rotating_fluid.xml` (spinning disc base). Puck as a sphere with freejoint on the disc surface.
**Hints:** In the lab frame the puck moves in a straight line (no friction). Color the disc with wedge-shaped geoms at different angles to make the rotation visible. Puck traces a curve relative to disc markings. See gotchas.md §rotating_frames.

---

#### `rotating_bucket_parabola` — Rotating frame / centrifugal parabola

**Physics:** In a rotating reference frame, the centrifugal pseudopotential adds to gravity to create an effective gravity pointing outward and downward. Small balls in a spinning cylinder settle on a paraboloid z = ω²r²/(2g), the same shape as a rotating liquid surface.
**Setup:** Cylinder (R = 0.12 m, H = 0.18 m) on a vertical hinge with init-qvel ω = 8 rad/s. Cylinder wall as curved geom or ring of box segments. ~60 balls (R = 0.006 m, M = 0.002 kg) with freejoints, initially piled near the center at z = 0.02 m.
**Motion:** Render 8 s. Balls are thrown outward by rotation, climb the cylinder walls, and settle in a paraboloid surface. Camera: 3/4 overhead, fovy = 50.
**Template:** `rotating_fluid.xml`. Replace fluid visualization with ball granular proxy.
**Hints:** Balls need contact with each other and the cylinder wall. friction = 0.3. At ω = 8 rad/s, parabola height at r = 0.10 m: z = 8²×0.1²/(2×9.81) ≈ 0.033 m — a modest but visible curve. See gotchas.md §granular_initial_conditions.

---

#### `universal_joint_velocity_variation` — Cardan joint / velocity ripple

**Physics:** A Hooke's (Cardan) universal joint connecting two shafts at angle θ = 30° transmits constant torque but produces sinusoidal output angular velocity variation: ω_out = ω_in·cos θ/(1 − sin²θ·cos²φ), oscillating ±15% per revolution.
**Setup:** Input shaft: cylinder (L = 0.15 m, R = 0.015 m) on a fixed hinge (axis y), init-qvel ω = 4 rad/s. Cross-piece: small plus-shaped body with two perpendicular hinges connecting input and output shafts. Output shaft: same cylinder, hinge axis rotated 30° from input. Bright colored marker disc on each shaft end to visualize speed.
**Motion:** Render 4 s (~2.5 revolutions). Input marker rotates uniformly. Output marker visibly speeds up and slows down twice per revolution. Side view, fovy = 40.
**Template:** `four_bar_linkage.xml` (crossed hinge concept). gen_universal_joint.py for the cross-piece geometry.
**Hints:** The cross-piece must have exactly two perpendicular hinges — one matching the input shaft axis, one perpendicular for the output. The 30° shaft angle is the key parameter for visible variation. Add a velocity-indicator (arm length proportional to current ω) if possible via colored sector geom.

---

#### `snells_law_ball_refraction` — Snell's law analog / momentum at interface

**Physics:** A ball rolling from a low-friction region (fast) into a high-friction region (slow) has its path bent at the interface — analogous to Snell's law. The component of momentum parallel to the boundary is conserved (friction only acts perpendicular to motion), bending the trajectory toward the normal.
**Setup:** Flat frictionless floor divided into two half-planes by a sharp line along z-axis. Left half (x < 0): friction = 0 (fast region). Right half (x > 0): floor friction = 0.6 (slow region, approximated by floor geom segmentation). Ball (R = 0.02 m, M = 0.05 kg, freejoint) starts at (-0.3, 0, 0.02), init-qvel: vx = 1.5 m/s, vy = 0.8 m/s (oblique approach at ~28° to interface normal).
**Motion:** Render 2 s. Ball rolls straight in left region, then bends toward the normal upon entering the right region. Top-down camera, fovy = 50, xyaxes = "1 0 0  0 1 0".
**Template:** `incline_friction.xml`. Two floor geom patches with different friction values.
**Hints:** The analogy is clearest with a perfectly sharp interface and no rolling (use a sliding puck: zero rotational inertia). The "refraction" is approximate — real Snell's law requires wave optics. See gotchas.md §friction_zones.

---

#### `suspension_cable_parabola` — Distributed load / parabola vs catenary

**Physics:** A catenary (uniform load per arc length = cable self-weight) hangs as y = cosh(x/a). A suspension bridge cable carrying a uniform horizontal load (deck weight) hangs as a parabola y = x²/(2a). Side-by-side demonstration of both shapes.
**Setup:** Two chains of 40 links each (M = 0.01 kg, length 0.04 m per link), endpoints fixed at (±0.8 m, 0, 1.0 m). Chain A: no extra loads — pure catenary. Chain B: 20 evenly spaced vertical rods hanging from every other link, each rod carrying a hanging mass M_load = 0.03 kg at its bottom (uniform horizontal load distribution).
**Motion:** Render 6 s (settle time ~3 s, then static). Camera: side view, both chains overlaid in the same x-z plane (y-separated by 0.1 m), showing different sag shapes.
**Template:** `hanging_chain_catenary.xml`. Chain B: add sub-bodies with tendons every 2 links.
**Hints:** The parabola chain sags more at the center relative to the endpoints. Overlay a thin static arch (or colored geom) tracing the theoretical parabola for visual comparison. Render 6 s — first 3 s for settling, last 3 s static.

---

#### `vibration_isolation_spring_mount` — Vibration isolation / transmissibility

**Physics:** A machine (heavy mass) on a spring mount is isolated from floor vibration at frequencies above √2·ω_n. Below resonance, vibration is transmitted fully; at resonance it amplifies; above, it is attenuated (transmissibility < 1).
**Setup:** Floor body (M = 5 kg, slide joint z) given sinusoidal motion via gen_isolation.py at ω_drive = 2·ω_n. Machine (M = 2 kg, box, slide joint z) connected to floor via spring (k = 500 N/m, damping = 0.5). ω_n = √(500/2) ≈ 15.8 rad/s; ω_drive ≈ 31.6 rad/s. Floor amplitude: ±0.02 m.
**Motion:** Render 6 s. Floor oscillates visibly ±2 cm. Machine barely moves (< ±3 mm). Camera: side view showing both floor and machine markers.
**Template:** `spring_mass.xml`. Floor body on a slide joint with gen-driven motion; machine body nested above with spring joint.
**Hints:** At ω_drive = 2·ω_n, transmissibility T = 1/|1 − (ω/ω_n)²| = 1/3 ≈ 0.33 (with light damping). Machine amplitude should be ~1/3 of floor amplitude. Mark the floor and machine with contrasting colored geoms.

---

#### `brazil_nut_granular_effect` — Granular segregation / size separation

**Physics:** When a mixture of small and large granular particles is vibrated vertically, the large particles rise to the top — the "Brazil nut effect." Caused by a combination of void-filling (small particles fall into gaps left by large particle) and convection cells.
**Setup:** Cylindrical container (R = 0.065 m, H = 0.18 m). 50 small balls (R = 0.007 m, M = 0.003 kg) and 1 large ball (R = 0.020 m, M = 0.07 kg) initially placed with large ball at the bottom. Container body on a slide joint z, gen_brazil_nut.py injects sinusoidal z-displacement (A = 0.012 m, f = 8 Hz). Friction between balls = 0.4.
**Motion:** Render 10 s. Large ball visibly rises through the small-ball bed, reaching the top by ~8 s. Camera: side view with transparent or cut-away container wall.
**Template:** `rotating_fluid.xml` (container geometry). gen_brazil_nut.py for vertical vibration.
**Hints:** Container wall needs to be thin box geoms (or a mesh cylinder) so the interior is visible. The vibration amplitude A must exceed the ball diameter for effective segregation. This is a computationally heavy scene (~50 contacts per step) — use timestep = 0.001 and nsubsteps accordingly.

---

#### `arch_vs_beam_load_compare` — Arch vs beam / compression vs bending

**Physics:** An arch transfers vertical load to its foundations through compressive forces along the arch axis (no bending). A flat beam under the same load must resist bending moments that grow as span². The arch is vastly more efficient for wide spans.
**Setup:** Two side-by-side structures spanning 0.60 m: (a) Semi-circular arch of 10 wedge-shaped blocks (same as arch_compression.xml), with a 1 kg central load. (b) Flat beam of 10 rectangular blocks (each 0.06×0.04×0.04 m) connected by weak hinges (stiffness = 500 N/m), spanning the same width, with the same 1 kg central load.
**Motion:** Render 4 s. Arch holds the load — stable. Beam sags progressively and eventually collapses under the load. Camera: side view showing both structures, fovy = 45.
**Template:** `arch_compression.xml` (arch) + `cantilever_load_curve.xml` (beam). x-separate structures by 0.8 m.
**Hints:** Beam hinges must be weak enough to show deflection under 1 kg but stiff enough to not collapse instantly. stiffness = 500 N/m gives visible sag in ~1 s. The arch requires careful initial geometry so blocks interlock cleanly.

---

### Package O — Kinematics, Mechanisms & Coupled Dynamics (12)

#### `worm_gear_nonbackdrivable` — Worm gear / self-locking

**Physics:** A worm gear has a high reduction ratio (N:1) and is self-locking — the worm can drive the wheel but the wheel cannot backdrive the worm, because the friction angle exceeds the lead angle. Used in lifts and hoists where loads must not back-drive.
**Setup:** Worm shaft: cylinder (R = 0.015 m) on a hinge about x, init-qvel ω = 10 rad/s. Worm wheel: cylinder (R = 0.10 m) on a hinge about z. Joint equality coupling: wheel_angle = worm_angle / 20 (20:1 ratio). High rotational friction/damping on worm shaft hinge (damping = 5 N·m·s) acts as the self-locking mechanism. Render scene (a): normal drive (worm spins, wheel turns slowly). Scene (b): give wheel init-qvel, observe worm stays still.
**Motion:** Render 4 s each. (a) Worm rotates at 10 rad/s, wheel at 0.5 rad/s. (b) Wheel given 2 rad/s, worm stays near-stationary. Camera: 3/4 isometric.
**Template:** `gear_train_2_gears.xml` (joint equality coupling).
**Hints:** True self-locking requires friction between the worm thread and wheel tooth faces — approximated here by high damping on the worm hinge that resists reverse torque. Joint equality polycoef = "0 0.05 0 0 0" (ratio 1/20).

---

#### `projectile_with_drag_compare` — Projectile / air resistance effect

**Physics:** Air drag (≈ quadratic in speed for real projectiles, linear approximation here) reduces range and shifts the optimal launch angle below 45°. A dragged ball traces a steeper, shorter arc than a vacuum projectile launched identically.
**Setup:** Two balls at (0, 0, 0.02): Ball A (freejoint, no damping — vacuum). Ball B (freejoint, linear damping d = 0.3 kg/s on x and z translational DOFs — drag proxy). Both launched at 45° with v = 5 m/s: init-qvel = (3.54, 0, 3.54) m/s.
**Motion:** Render 2 s. Ball A traces the longer parabola, lands at x ≈ 2.55 m. Ball B lands at x ≈ 1.9 m (shorter) with a steeper descent. Side view, fovy = 45, pos (1.2, -3, 0.8).
**Template:** `projectile_jenga.xml` (projectile + floor). Two freejoint balls, one with damping.
**Hints:** Linear damping on freejoint translational DOFs: add `<joint name="ball_b_tx" ... damping="0.3"/>` for x and z joints. The drag slows both rise and fall asymmetrically. Mark each ball differently (red/blue) for clear comparison.

---

#### `double_pendulum_on_cart` — 3-DOF / coupled chaos on cart

**Physics:** A double pendulum on a freely sliding cart has three coupled degrees of freedom (cart x, θ₁, θ₂). The additional DOF creates richer dynamics than a fixed double pendulum — the cart recoils from pendulum swings, feeding energy back into the chain chaotically.
**Setup:** Cart (M = 0.5 kg, box 0.15×0.05×0.03 m) on a frictionless slide joint along x (damping = 0). Double pendulum mounted on cart: link 1 (L = 0.30 m, M = 0.10 kg) on hinge y at cart top; link 2 (L = 0.30 m, M = 0.10 kg) on hinge y at link 1 bottom. init-qvel: cart vx = 1.5 m/s, both pendulum angles = 0.
**Motion:** Render 8 s. Cart oscillates back and forth as pendulum swings generate reaction forces; pendulum enters chaotic motion within 3–4 s. Camera: wide side view, fovy = 50.
**Template:** `double_pendulum.xml` + `pendulum_pivot_on_cart.xml`. Cart body is parent of pivot body.
**Hints:** Keep cart damping = 0 (frictionless) to preserve total horizontal momentum. The scene is sensitive to initial conditions — cart vx = 1.5 m/s with both angles at 0 gives a clean initial coupled motion that turns chaotic. See gotchas.md §chained_joints.

---

#### `elastic_rod_bounce_modes` — Flexible body / impact mode excitation

**Physics:** A flexible rod dropped horizontally onto the floor excites multiple bending modes simultaneously on impact. The rod bounces in complex S-curves and wavy shapes, unlike a rigid rod which bounces uniformly.
**Setup:** 20 rigid links (each L = 0.05 m, M = 0.01 kg, capsule R = 0.006 m) connected by hinge joints (axis y) with stiffness k = 2000 N/m and damping = 0.01. Initial configuration: all hinges at 0 (rod horizontal), centered at world (0, 0, 0.25). All links given init-qvel vz = −1.5 m/s (fall toward floor).
**Motion:** Render 2.5 s. Rod falls, center hits floor first, bends around the contact, bounces back with complex S-shape oscillations. Side view, fovy = 40.
**Template:** `dominoes.xml` (chain) + `hanging_slinky_drop.xml` (release). No gravity compensation — all links released simultaneously.
**Hints:** stiffness = 2000 N/m ensures the rod feels "stiff but not rigid" on impact. The center hits first (slightly due to contact geometry), exciting the odd bending modes (1st, 3rd). Timestep = 0.0005 for stability. nsubsteps = 4.

---

#### `spinning_hoop_on_incline` — Gyroscopic / lateral drift on slope

**Physics:** A hoop spinning rapidly about its own axis (gyroscopically stiff) placed on an inclined surface precesses sideways rather than rolling straight down the slope. The gravitational torque (trying to tip the hoop down the slope) is 90°-redirected by angular momentum into a sideways precession.
**Setup:** Hoop (thin cylinder R = 0.10 m, thickness 0.008 m, M = 0.20 kg) on a 15° inclined floor. Freejoint. init-qvel: spin ω_spin = 30 rad/s about the hoop's own axis (pointing along the slope), plus small downhill component vx = 0.05 m/s to keep contact.
**Motion:** Render 4 s. Hoop rolls slowly sideways across the slope (perpendicular to downhill direction) instead of rolling down. Camera: front view of incline, fovy = 40.
**Template:** `rolling_race.xml` (incline) + `spinning_top.xml` (spin init). Inclined floor at 15°.
**Hints:** Precession rate Ω = M·g·L/(I·ω_spin) where L is horizontal distance from contact point to COM. For the hoop, I ≈ MR². Use high spin ω_spin = 30 rad/s to keep precession slow and visible. Friction must be high enough to prevent slipping (friction = 0.5). See gotchas.md §world_frame_angular_qvel.

---

#### `epicyclic_compound_reversal` — Compound planetary / direction reversal

**Physics:** In a standard planetary gear train (ring fixed, sun input, carrier output), the carrier rotates in the same direction as the sun. By instead fixing the carrier and using the ring as input, the sun rotates in the OPPOSITE direction to the ring — compound epicyclic direction reversal.
**Setup:** Same geometry as `planetary_gear_train.xml` but with the carrier body fixed to the world and the ring gear body given init-qvel ω = 3 rad/s. Three joint equalities now couple ring-to-planet and planet-to-sun with reversed sign. Sun hinge is free to rotate; carrier hinge is locked (range = "0 0").
**Motion:** Render 3 s. Ring rotates clockwise (top-down). Sun rotates counter-clockwise at ratio ω_sun/ω_ring = −(R_ring/R_sun). Planets spin AND orbit backward. Colored markers on ring and sun show opposite directions clearly.
**Template:** `planetary_gear_train.xml`. Swap which hinge is fixed vs driven. Reverse polycoef signs.
**Hints:** Carrier fixed: add `<joint ... range="0 0"/>` to lock it. Ring input: init-qvel on ring hinge. Joint equality ratio changes sign because the power path reverses. Top-down camera, fovy = 40.

---

#### `gyroscope_on_incline_precesses` — Gyro on slope / non-vertical precession axis

**Physics:** A fast-spinning gyroscope placed on an inclined surface experiences gravity along the slope-normal direction. Its precession axis is the slope normal (not vertical), causing the spin axis to sweep a cone around a tilted axis — visually striking.
**Setup:** Inclined floor at 15° to horizontal. Gyroscope disc (R = 0.08 m, M = 0.30 kg, thin cylinder) with freejoint, placed on the slope. init-qvel: spin ω = 60 rad/s about the disc's own symmetry axis (initially pointing up the slope), no translational velocity.
**Motion:** Render 5 s. Gyroscope precesses around the slope-normal axis; the spin axis traces a tilted cone — not around vertical but around the slope's upward normal. Camera: 3/4 view from above the incline, fovy = 45.
**Template:** `spinning_top.xml` (spin init) + `incline_friction.xml` (tilted floor). Tilt world floor geom 15°.
**Hints:** The precession axis is normal to the slope, not to the world vertical. Precession rate Ω = M·g·cos(15°)·L / (I·ω). Floor friction = 0.4 to maintain contact without excessive sliding. init-qvel in world frame: see gotchas.md §world_frame_angular_qvel for converting body-frame ω to world-frame qvel.

---

#### `chain_vs_rod_pendulum` — Rigid vs flexible pendulum / effective length

**Physics:** A rigid rod pendulum has a well-defined period T = 2π√(2L/3g). A chain pendulum of the same total length behaves differently: its COM is at the same height but its effective pendulum length (related to its I/Md) differs, and the chain's flexibility allows internal modes that shift the apparent period.
**Setup:** Side by side: (a) Rigid rod (single body, length L = 0.50 m, M = 0.20 kg, box 0.02×0.02×0.50 m), hinged at its top — pivot at (−0.3, 0, 1.0). (b) Chain (10 links, each 0.05 m, M = 0.02 kg, capsule), top link hinged at (0.3, 0, 1.0), remaining links via hinge joints (axis y, damping = 0.005). Both released from 30° tilt.
**Motion:** Render 6 s. Rod swings at its period T ≈ 1.16 s. Chain swings at a slightly different effective period; lower links lag behind the upper links visibly, creating a whipping motion. Side view, fovy = 45.
**Template:** `pendulum.xml` (rod) + `swinging_chain_pendulum.xml` (chain).
**Hints:** The chain's lower links lag the upper ones — a visual signature of flexibility. Keep chain hinge damping = 0.005 (very low) so the flexible modes don't die too quickly. Mark the bottom of each to compare oscillation phases.

---

#### `pendulum_group_phase_velocity` — Wave packet / group vs phase velocity

**Physics:** In a dispersive wave medium, the phase velocity (speed of individual oscillation crests) differs from the group velocity (speed of the packet envelope). A Gaussian-modulated wave packet spreads as it travels because different frequency components move at different speeds.
**Setup:** 20 pendulums (lengths 0.28 to 0.42 m in small steps, creating a dispersive medium). init-qpos: q_i = A·exp(−(i−10)²/8)·cos(k₀·i) with A = 0.15 rad, k₀ = π/3 (a localized wave packet centered at pendulum 10). No damping.
**Motion:** Render 20 s. The packet envelope moves at the group velocity while the oscillation crests inside move at the phase velocity. The envelope broadens over time (dispersion). Camera: front view showing all 20 pendulums, fovy = 55.
**Template:** `pendulum_waves.xml`. Modify lengths to vary linearly; modify init-qpos to wave packet.
**Hints:** Group velocity v_g = dω/dk, phase velocity v_p = ω/k. For pendulums with varying length, ω_i = √(g/L_i) — each pendulum has a different natural frequency, creating dispersion. The packet spreading becomes clear by t = 10 s. Render at least 20 s.

---

#### `superball_corner_retroreflection` — Elastic collision / retroreflection

**Physics:** A spinning superball thrown at a 90° corner undergoes two sequential surface bounces; each bounce reverses the spin component normal to that surface. The combined effect sends the ball approximately antiparallel to its initial direction.
**Setup:** 90° corner formed by two perpendicular floor/wall geoms. Ball (R = 0.025 m, M = 0.05 kg, freejoint). Contact: high CoR (solref = "−200000 −20", solimp = "0.99 0.999 0.001"), high friction (friction = "1.0 0.1 0.01"). init-qvel: translational (2.0, 0, −1.0) m/s (toward corner) + angular ω_y = −20 rad/s (backspin).
**Motion:** Render 1.5 s. Ball hits floor, bounces sideways into wall, bounces back approximately antiparallel to original direction. Camera: 3/4 view of corner, fovy = 50.
**Template:** `bowling.xml` (floor + walls) + `elastic_collision.xml` (stiff contact settings).
**Hints:** The retroreflection is only approximate — exact retroreflection requires a specific spin magnitude. The key is high friction (spin-to-velocity coupling) and high CoR. Two bounces in quick succession are the visual signature. See gotchas.md §high_restitution_contacts.

---

#### `ball_in_v_groove_constraint` — Constrained rolling / groove guidance

**Physics:** A ball rolling in a V-groove track (two flat rails at 45° forming a V) is constrained to move only along the groove axis. The groove exerts normal forces from both sides simultaneously, providing lateral guidance without kinetic friction along the axis.
**Setup:** Two flat floor geoms angled at ±45° to form a V-groove, oriented along the x-axis, length 1.0 m. Ball (R = 0.025 m, M = 0.05 kg, freejoint). Ball placed in the groove at x = −0.4 m, init-qvel: vx = 0.8 m/s. Groove-ball friction = 0.3 (rolling without slip along x, constrained laterally).
**Motion:** Render 2.5 s. Ball rolls smoothly along the groove, decelerating slightly due to rolling resistance. No lateral drift. Camera: 3/4 front-side view, fovy = 40.
**Template:** `bead_on_helix.xml` (channel guidance concept). gen_v_groove.py places two angled geom strips.
**Hints:** V-groove geometry: two flat geoms each rotated ±45° around x-axis, meeting at the groove bottom. Ball radius 0.025 m, groove half-angle 45° — contact at ~0.018 m from groove centerline on each side. Groove width at ball contact ≈ 0.036 m. See gotchas.md §groove_contact_geometry.

---

#### `spinning_top_on_incline` — Gyroscope / precession around tilted axis

**Physics:** A spinning top on a tilted surface precesses around the local gravitational vertical (the surface normal), not the world vertical. The precession cone axis is tilted from vertical by the slope angle, creating visually distinct "slanted" precession circles.
**Setup:** Floor tilted 15° from horizontal (geom euler = "0 −15 0"). Spinning top (standard cone+stem body, M = 0.05 kg, cone R = 0.035 m) with freejoint, placed on the slope. init-qvel: spin ω_spin = 60 rad/s about top's symmetry axis (pointing approximately along slope-normal direction), no translational velocity. init-qpos: tip at contact point on slope.
**Motion:** Render 6 s. Top precesses around the slope-normal axis, tracing circles that are tilted from vertical — clearly different from the same top on a flat floor. Camera: oblique view showing the tilted precession cone, pos (0.5, −0.6, 0.4), fovy = 38.
**Template:** `spinning_top.xml`. Tilt the floor geom. Adjust init-qpos/qvel to match slope geometry.
**Hints:** On the slope, effective gravity = g·cos(15°) ≈ 9.48 m/s² perpendicular to slope. Precession rate Ω = M·g·cos(15°)·d/(I·ω_spin) where d is the distance from tip to COM. Floor friction = 0.4. See gotchas.md §world_frame_angular_qvel for setting spin in world frame.

---

## Unsorted ideas (to triage)

New scene ideas land here. The master keeper triages and slots them into the
right tier when reviewing RETURNS_LOG.md.

- ...

---

## Distribution math

| Tier | Count |
|------|------:|
| ✅ Done | 23 |
| 🔵 Tier 1 (kept) | 28 |
| 🟣 Tier 1 (new) | 23 |
| 🟢 Tier 1 (final additions, round 2) | 10 |
| 🟡 Tier 1/2 (F + G additions, round 2) | 34 |
| 🔵 Tier 1/2 (H + I additions, round 3) | 34 |
| 🟠 Tier 2 | 24 |
| 🔴 Tier 3 (reserved as special projects) | 10 |
| **Total available for assignment** | **129 Tier 1 + 24 Tier 2 = 153** |

Plan: 9 employees × 17 each = 153, exhausting the assignable pool (Tier 3 is
reserved for special projects). Per-person mix: 12 Tier 1 + 5 Tier 2, spread
across topic categories (pendulum / rolling / collision / spring-or-wave /
chain-or-curve / free-body-or-structure / friction-or-mechanism / energy /
mechanism / equilibrium) so nobody gets a one-topic day. Round-1 packages
A–E used the first 85; round-2 packages F and G use the next 34; round-3
packages H and I use the latest 34.
