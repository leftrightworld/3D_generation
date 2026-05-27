# damped_pendulum_decay

## Task description
A simple pendulum with viscous damping at the hinge shows exponential decay of amplitude: θ(t) = θ₀·e^(-γt)·cos(ωt). Period is nearly unchanged for light damping; the envelope decay should be visible over roughly 8 swings before the pendulum settles to rest.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.002 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast

### Pendulum body
- Body pos = (0, -0.75, 2.005) m — hung from the end of the horizontal stand arm
- Joint `hinge`: type=hinge, axis=(0,1,0), pos=(0,0,0), **`damping` = 0.035** (the key parameter producing the decay envelope)
- String geom (visual capsule, no contact): fromto (0,0,0) → (0,0,-1.1), size 0.005
- Bob (sphere, no contact): pos (0,0,-1.1), size 0.115

### Stand (static)
- Vertical wood post: size 0.045×0.045×1.05 at (0, 0.55, 1.05)
- Horizontal wood arm: size 0.045×0.65×0.045 at (0, -0.10, 2.05)

### Camera
- `cam` pos = (3.0, -3.3, 1.9), 3/4 view from front-right
- fovy = 40°
