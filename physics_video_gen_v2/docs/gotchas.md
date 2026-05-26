# MuJoCo Gotchas (Hit & Documented)

Real traps we've hit while building scenes in this project. **Read these before
debugging "why doesn't my scene do what I expect."** Each one cost us between
30 minutes and 2 hours to figure out the first time — re-reading this file
costs you 5.

---

### 1. Friction at a contact = element-wise MAX of the two geoms' friction vectors.

**Why:** documented MuJoCo behavior; easy to forget. Setting one geom to
μ=0.05 does NOT give you a low-friction contact if the OTHER geom has μ=0.6 —
you get 0.6.

**How to apply:** when you want a per-block friction comparison on a shared
surface (incline-friction scene), set the SHARED surface's μ to near-zero
(e.g. `friction="0.001 0.0001 0.00001"`) and let each block's own μ dominate.

### 2. `<tendon>` is a TOP-LEVEL element under `<mujoco>`, NOT a child of `<worldbody>`.

**Why:** MuJoCo schema rule. You'll see "Element 'tendon', line N: unrecognized
element" if you nest it wrong.

**How to apply:** spatial tendons (visual strings / springs for spring-mass,
Atwood, Maxwell wheel) live at the same level as `<worldbody>`, `<asset>`,
`<default>`, `<equality>`. The `<site>` elements that the tendon references
CAN live inside `<worldbody>` and inside bodies — that's fine.

### 3. Hinge axis direction matters for which way bodies fall.

**Why:** in the dominoes scene, the first domino was pre-tilted with a
quaternion built for rotation about **-y**, which tipped it BACKWARD (away
from the chain). The cascade never started.

**How to apply:** for a body whose top (+z) should move toward +x, rotate
about **+y** with positive angle: `qw=cos(α/2), qy=+sin(α/2)`. Visualize:
right-hand thumb along +y, fingers curl +z → +x. **Test on a single body
before generating a chain.**

### 4. Newton's cradle and other near-elastic chains need stiff contacts + small timestep.

**Why:** MuJoCo's default soft contacts smear momentum, so all balls oscillate
together instead of clean energy transfer.

**How to apply:** use `solref="0.001 1" solimp="0.99 0.999 0.0001"`,
`impratio=5+`, `cone="elliptic"`, `timestep=0.0005`. Even so, energy decays
faster than an ideal cradle — that's normal; qualitative behavior is correct
in the first ~1.5 s.

### 5. Grid sampling can alias the motion period.

**Why:** a `make_grid.py` 2×4 grid samples 8 evenly-spaced frames. If
`duration / 8 ≈ T` (the motion period), every frame catches the same phase
and the grid looks static.

**How to apply:** if a grid shows seemingly static motion that you know is
dynamic, re-grid with `--cols 6 --rows 2` (12 frames, different sample
interval) before assuming a physics bug.

### 6. Joint equality for inextensible strings and rolling-without-slip.

**Why:** there's no built-in "rope" or "string-wraps-around-axle" in MuJoCo;
the practical way to model a string-over-pulley is a joint-equality constraint
`<equality><joint joint1="A" joint2="B" polycoef="0 -1 0 0 0"/></equality>`
which enforces q_A = -q_B. The same trick works across MIXED joint types: for
the Maxwell wheel we couple a slide joint to a hinge joint with
`polycoef="0 r_axle 0 0 0"`, giving q_slide = r_axle · q_axle (rolling without
slip on the unwinding string). Effective gravitational acceleration becomes
a = g/(1 + I/(M·r_axle²)) as expected.

**How to apply:** also render the visible string with two spatial tendons
(one per side) for visual fidelity. The equality does the physics, the
tendons are pure decoration. Pick `r_axle` such that descent over the clip
duration stays inside the slider range (e.g. r_axle=0.008, R=0.08, M=0.5 →
a≈0.19 m/s², ~0.75 m descent in 2.8 s).

### 7. With high mass differential + low damping, an Atwood machine accelerates *fast*.

**Why:** a = (m1-m2)g/(m1+m2) can hit the joint range limit in under a second.

**How to apply:** either raise joint damping (we used 2.5 per joint) to make
motion sub-terminal, or widen joint ranges, or shorten duration. We chose
high damping so the clip shows steady-state motion across ~3 s.

### 8. Ball joint `qvel` frame is ambiguous in practice — use a 2-DOF gimbal instead.

**Why:** docs say ball-joint qvel is in the parent frame, but empirically
setting `qvel=(0,0,Ω)` for a tilted pendulum did NOT produce rotation about
world +z — the rod just spun about its own axis. Switching to body-frame
conversion `qvel = R^T · (0,0,Ω)` also failed in a different way.

**How to apply:** for the conical pendulum we replaced the ball joint with
two hinges in a gimbal (outer hinge axis `(0,0,1)` for yaw, inner hinge axis
`(0,1,0)` for tilt). Then `init-qpos="yaw, tilt"` and
`init-qvel="yaw_rate, 0"` work transparently. The outer body just needs a
tiny dummy geom for inertia. Use this whenever you need to launch a system
with a specific rotation about an external axis — gimbals are much easier to
reason about.

### 9. Loop-the-loop with smooth ramp-to-loop entry is fragile; a CLOSED loop with launch velocity is robust.

**Why:** making segmented track tangents match between an entry ramp and a
loop bottom requires careful sub-millimeter alignment of segment positions;
small mismatches cause the ball to slip through a seam or bump and lose
energy.

**How to apply:** place loop segments at radius `R + T/2` from the loop center
(so the segment top face is exactly on the ideal circle), make the loop
CLOSED (no gap), launch the ball from the bottom with
`init-qvel="v 0 0 0 -v/r 0"` (linear + matching rolling spin). Demonstrates
the same physics (energy conservation + centripetal force at top) without
the geometry headaches. The ball orbits until friction stops it.

### 10. Free-joint `qvel` angular components ARE in WORLD frame.

Confirmed empirically by the spinning top — `(0,0,0,0,0,ω)` interpreted as
body frame would have produced tumbling for any nonzero tilt, but it actually
DOES tumble, while `(sin θ · ω, 0, cos θ · ω)` does NOT tumble. So world
frame.

**How to apply:** to produce pure spin around body +z when the body starts
tilted by θ about +y, pass `init-qvel = "vx vy vz  ω·sin θ  0  ω·cos θ"`.

### 11. Spinning-top stability has a hard minimum spin rate; below it, the top falls instead of precessing.

**Why:** critical spin rate is `ω_min = sqrt(4·M·g·L_cm·I_xy / I_z²)` where
I_xy is about the contact tip (parallel-axis from the disc center, plus
disc's own perpendicular moment). For our top (M≈0.087, L_cm≈0.075,
I_xy≈5e-4, I_z≈1.2e-4), ω_min ≈ 95 rad/s. We use ω=120 for margin.

**How to apply:** when designing a top, compute ω_min first; pick
ω ≥ 1.3·ω_min. If the geometry changes (e.g. moving the disc up the stem for
floor clearance), recompute — it scales with I_xy / I_z² which grows fast
with L_cm.

### 12. Even with correct ω_min, you also need the precession velocity in the initial state, or nutation amplitude will blow up.

**Why:** setting ω = pure-spin-along-body+z leaves the body without its
steady precession velocity Ω·z_world. Gravity then redirects the spin via
gyroscopic action, but the transient is HUGE nutation (the top wobbles
between ~0° and ~90° tilt).

**How to apply:** at the body's known initial tilt θ, compute
Ω = M·g·L_cm / (I_z·ω) and add Ω to the z-component of the angular-velocity
qvel. For our top: `init-qvel = "0,0,0, 20.88, 0, 122.4"` (ω=120 along
body+z at 10°, plus Ω=4.23 around world +z).

### 13. Spinning-top tip needs HIGH sliding friction, LOW torsional friction.

**Why:** high sliding friction prevents the precessing tip from "walking"
the top across the floor (gyroscopic horizontal force at the contact); low
torsional friction lets the spin angular momentum survive
(μ_torsional · F_n · r_contact drains it otherwise).

**How to apply:** set tip `friction="1.5 0.003 0.0005"`. The first number
prevents lateral drift; the small second/third numbers keep spin alive.

### 14. To change I/MR² without changing geom shape, override inertia with `<inertial diaginertia=...>` and set the geom `mass="0"`.

**Why:** MuJoCo auto-computes inertia from each geom assuming uniform
density. For a "hollow sphere" or "thin ring" demo where the shape is the
same as solid-sphere / solid-disk but the I/MR² is different (2/3 vs 2/5
for hollow sphere, 1 vs 1/2 for thin ring), we need to override.

**How to apply:**
```xml
<body>
  <inertial pos="0 0 0" mass="0.10" diaginertia="Ix Iy Iz"/>
  <geom .. mass="0"/>
</body>
```
For a thin hoop in body frame with axle = body +z, use
`diaginertia="0.5·mr²  0.5·mr²  mr²"`.

### 15. Pendulum-wave init: all hinges at the same angle, but render at the FULL sync window for the pattern to read.

**Why:** lengths chosen as L_i = g·(W/(K+i))²/(4π²) make all pendulums
resync at t=W. The "traveling-wave" + "alternating" + "anti-sync" patterns
play out within one W window. Rendering < W/4 just shows everyone roughly
in phase.

**How to apply:** render for at least W (we used 15 s = W/2 with W=30, K=25,
N=14 — gives the full pattern up to alternating). Camera 3/4 top-down so
swing direction projects to screen — front view foreshortens the swing and
the pattern reads as static.

### 16. For elastic ball-on-ball collisions, use direct-stiffness contact AND freejoint-on-frictionless-track, NOT slide joints.

**Why:** slide joints are over-constrained (5 of 6 DOFs locked) and the
default solref/solimp produce inelastic restitution; the two balls end up
moving together after impact instead of exchanging velocity. Switching to
freejoints + zero geom friction + `solref="-200000 -20"`
`solimp="0.999 0.9999 0.0001"` gives ~95% elastic equal-mass collisions
(red stops, blue carries the momentum).

**How to apply:** keep balls on the track with gravity + side walls; set
ball friction to "0 0 0" so they slide rather than roll; use small timestep
(0.0002 s) to resolve the short stiff-contact impulse.

### 17. Euler beam buckling is delicate — margin must sit in the narrow band [1.10, 1.25] above critical, or the demo fails.

**Why:** discretize the column into N rigid segments with torsional hinge
springs (stiffness k → EI_eff ≈ k·L/N, P_cr ≈ π²EI/(4L²) for pin-free
cantilever). If margin = load/P_cr is too high (>1.5), the post-buckled
equilibrium angle is past horizontal and the column collapses flat to the
floor instead of holding a bow. If margin too low (<1.05), the unstable
eigenvalue is tiny and nothing visibly happens in a 5 s clip. Damping also
has a sweet spot: too low → oscillation about the buckled equilibrium; too
high → overdamped, growth phase invisible.

**How to apply:** target margin ≈ 1.20, per-hinge damping ≈ 0.30, seed
initial qpos ≈ 0.015 rad at every hinge (cumulative ~8° initial bow makes
early frames not look pathologically straight). Render 4 s. Working
parameters: N=10, L=1 m, k=26 N·m/rad, d=0.30, m_seg=0.025, m_top=0.55 —
column settles to ~55° tip angle without flopping over.

### 18. "Balls as fluid" only works visually from a top-down view, and contact count is the bottleneck.

**Why:** granular media doesn't flow like a continuum, so a SIDE view of N
rigid balls in a spinning bucket reads as "messy pile, not parabolic
surface" — they form discrete clumps and angles of repose, not a smooth
surface. The radial pile-up IS happening, but it's only legible from above.
Contact count is O(N²); 160 balls froze the renderer for 9+ minutes, 72
balls renders in ~90 s.

**How to apply:** cap ball count around 60-80, use straight TOP-DOWN camera
(`xyaxes="1 0 0   0 1 0"`, `pos="0 0 H"`) to show the ring distribution +
dry-center hole, and spin fast enough that Δh = Ω²R²/(2g) exceeds 2× the
average fill height — this puts you in the "dry annulus" regime where the
central hole is unmistakable. Initial qvel for every ball must be `ω × r`
so they start in sync with the bucket; spinning up from rest via friction
is too slow and unstable. Heavy bucket bottom (10+ kg) keeps Ω roughly
constant despite ball back-torque.

---

### 19. Negative CLI values (--init-qpos / --init-qvel) are parsed as flags by argparse and PowerShell.

**Why:** Any token starting with `-` looks like a CLI option to Python's `argparse`. On Windows PowerShell the problem is the same even inside quotes in some invocation patterns.

**How to apply:** Always use the equals form: `--init-qpos=-0.35,0,...` or `--init-qvel=-7,0,0`. Adding a bare `--` separator before the argument also works (`-- -0.35,...`). This applies to every numeric argument that can go negative.

---

### 20. Coin spiral (and any free-spinning freejoint body): angular velocity must be in the WORLD frame, not body frame.

**Why:** For a `freejoint`, `qvel[3:6]` is the angular velocity in the **world** frame. A coin standing nearly on edge (~88°) needs its spin axis along its symmetry axis (body +z), which is tilted relative to world +z. Passing `[0,0,ω]` gives the wrong spin direction.

**How to apply:** Compute `qvel[3:6] = quat_rotate(qpos[3:7], [0,0,1]) * spin_rate`. Also store full-precision `qpos`/`qvel` values — rounding to 3–4 decimals changes the chaotic outcome. For coin-spiral specifically: friction ≈ 0.65 sliding, spin ≈ 34 rad/s → ~7 s edge precession before flop.

---

### 21. Reuleaux triangle (and any rolling non-circular profile): the cross-section must be in the XZ plane, not XY.

**Why:** Rolling along +x with spin about +y requires the constant-width profile in the **xz vertical plane**. Building the arc capsules in the xy horizontal plane makes it look like it's sliding, and the centroid doesn't bob correctly.

**How to apply:** Generate arc capsules in xz; use a freejoint + floor friction. (A freejoint + slide/hinge combo froze after ~0.5 s in testing.)

---

### 22. Spherical pendulum: use a yaw+tilt gimbal (two perpendicular hinges), NOT two coplanar horizontal hinges.

**Why:** Two coplanar horizontal hinges over-constrain or collapse the motion space, producing flat or degenerate trajectories.

**How to apply:** Outer hinge `axis="0 0 1"` (yaw), inner hinge `axis="0 1 0"` (tilt). Pre-compute the floor trail in a gen script; render with a top-down camera.

---

### 23. Compound pendulum clusters: lower the pivot to avoid inter-pendulum clipping at large angles.

**Why:** Three pendulums sharing one crossbar support clip through each other and the post at large angles.

**How to apply:** Lower the pivot below the crossbar, remove the centre post, angle initial `qpos` inward (~0.42 rad each), and add thin suspension ropes between the crossbar and each pendulum.

---

### 24. Recursive chain XML: the leaf link needs its own full `<body>` tag.

**Why:** Recursive generators that build nested chains often produce mismatched XML — the leaf segment has `</body>` without an opening tag, or one extra closing tag.

**How to apply:** The base case of the recursion must emit a complete `<body>…<joint/>…<geom/>…</body>` block, not just a `<geom>` inside the parent body.

---

### 25. Catenary chain: total link arc-length must EXCEED the span between anchor posts.

**Why:** A chain whose total length equals the post span snaps into a straight diagonal under weld constraints; no visible sag forms.

**How to apply:** Either use excess link length (arc_length > span), or initialise link positions along a downward parabolic arc; weld the right endpoint to the post.

---

### 26. Catenary chain kinematic init: MuJoCo Y-hinge convention requires negating the angle, and joint range must be wide.

**Why:** Uniform-x catenary angles leave the right end disconnected; removing the sign negation makes the chain arch upward. The default hinge range `[-1.55, 0.05]` clamps the angles needed by a deeply sagging catenary.

**How to apply:** Use FABRIK + arc-length catenary in `render.py`; set `qpos = -q` for MuJoCo's Y-hinge convention; widen hinge range to `"-1.55 1.55"`.

---

### 27. Rattleback: strip debug visuals and centre the camera before final render.

**Why:** Red/blue masts, a yellow bow mark, deck strips, and floor cross/tick lines are useful during debugging but confuse the demo. An oblique FREE camera offset the stone from frame centre.

**How to apply:** Use hull-only visuals; set a fixed centred XML camera. The two-direction compare (`render_rattleback_compare`) handles the preferred vs. wrong-spin segments automatically.

---

### 28. Pyramid keystone removal: side blocks must be shorter than the keystone, or they form a stable arch after removal.

**Why:** Full-height side blocks formed a stable arch after the keystone was removed; soft contacts caused clipping between the upper tier and the arch.

**How to apply:** Use a 4-1-1-1 layout (only the bottom keystone, not side blocks). Use stiff contacts; let the structure settle, then apply a timed kick in `render.py` (do not hardcode a `qvel` index — use `mj_name2id` on the keystone body).

---

### 29. `freejoint` can only be used on top-level bodies (direct children of `<worldbody>`).

**Why:** MuJoCo schema restriction: `freejoint` on a nested body raises `free joint can only be used on top level` at load time.

**How to apply:** For a mass that moves inside a parent body (e.g. a ball inside a bucket), use a `ball` joint or a slide joint instead of `freejoint`.

---

### 30. Windows: use relative paths when invoking MuJoCo via subprocess — absolute paths with non-ASCII characters fail.

**Why:** Absolute paths containing non-ASCII directory names (e.g. Chinese characters) cause `ParseXML: Error opening file` in the MuJoCo child process due to encoding/path handling on Windows.

**How to apply:** `os.chdir()` to the project root first, then pass only relative paths like `scenes/foo.xml` to `render.py` and any subprocess call.

---

## Adding new gotchas

When you (or your AI) discover a new non-obvious MuJoCo behavior that costs
more than 30 minutes to debug, **add it here**. The next person joining the
project gets to learn from your time, not repeat it.

Format: short title, "Why" (one paragraph), "How to apply" (concrete code or
parameter values).
