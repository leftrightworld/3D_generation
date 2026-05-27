# bifilar_pendulum

## Task description
Bifilar pendulum: a mass suspended by two parallel strings swings sideways but rotation about the vertical is geometrically blocked by the parallel-string constraint. A horizontal rod hangs from two vertical strings attached at its two ends; when pushed sideways the rod translates in pure swing without twisting about its own axis. Period depends on string length and lateral separation.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.002 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast
- `angle` = radian, `autolimits` = true

### Pendulum body (`rod`)
- Body pivot pos = (0, -0.10, 2.005) m (midpoint of ceiling anchors)
- Joint `hinge`: type=hinge, axis=(0,1,0), `damping` = 0.020
- Rod geom: capsule fromto (-0.30, 0, -0.85) → (0.30, 0, -0.85), `size` = 0.025, `mass` = 0.40 kg
- Rod length = 0.60 m, hangs 0.85 m below pivot

### Strings (visual)
- Two `<spatial>` tendons (ceiling_L↔rod_end_L, ceiling_R↔rod_end_R)
- Tendon width = 0.005, `limited` = false (no length constraint — hinge enforces kinematics)
- Ceiling anchor sites at (±0.30, -0.10, 2.005) — lateral separation 0.60 m

### Stand (static)
- Vertical wood post: size 0.045×0.045×1.05 at (0, 0.55, 1.05)
- Horizontal wood arm: size 0.045×0.65×0.045 at (0, -0.10, 2.05)

### Camera
- `cam` pos = (3.0, -3.3, 1.9), 3/4 view, xyaxes="0.74 0.67 0 / -0.20 0.22 0.95"
- fovy = 40°
