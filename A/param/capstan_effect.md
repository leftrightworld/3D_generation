# capstan_effect

## Task description
Capstan effect: a rope wrapped 1.5 turns around a vertical wooden post connects a heavy load on one side to a light load on the other. Friction along the wrap multiplies tension exponentially (F_pull/F_hold = e^(μθ)), so the tiny light weight is enough to "hold" the much heavier weight. Here the rope is decoration (sequence of capsule segments on a helical wrap + Bezier tails), and the physics is captured by stiff slide joints on the two masses — the demo communicates the force-ratio idea visually rather than simulating rope friction directly.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.001 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast

### Heavy mass (red)
- Body `heavy` pos = (-0.45, 0, 0.2) m
- Slide joint `j_heavy`: axis=(0,0,1)
  - **`stiffness` = 20000 N/m**
  - **`damping` = 800 N·s/m** (overdamped — settles in <0.5 s after perturbation)
  - `range` = [-0.10, 0.10]
- Geom: box size 0.08×0.08×0.08, `mass` = 5.0 kg

### Light mass (blue)
- Body `light` pos = (+0.45, 0, 0.3) m
- Slide joint `j_light`: axis=(0,0,1)
  - **`stiffness` = 100 N/m**
  - **`damping` = 0.8 N·s/m** (lightly damped — jiggles a few cycles)
  - `range` = [-0.10, 0.10]
- Geom: box size 0.03×0.03×0.03, `mass` = 0.25 kg

### Post (static)
- Wood base: box size 0.20×0.20×0.025 at (0,0,0.025)
- Vertical post: cylinder size 0.05 × 0.6000 at (0, 0, 0.6400)

### Rope (visual only, 110+ capsule segments)
- Helical wrap: 64 capsules along 1.5 turns at radius ≈ 0.056 m
- Two Bezier tails: 22 capsules each
- All capsules size 0.006, `contype` = 0, `conaffinity` = 0

### Camera
- `cam` pos = (0.45, -1.70, 0.85), fovy 36, 3/4 perspective
