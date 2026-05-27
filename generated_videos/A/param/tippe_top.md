# tippe_top

## Task description
A tippe top is an asymmetric top (rounded heavy hemisphere bottom + thin stem on top) that, when spun fast about its symmetry axis, inverts itself — the stem flips down and the top ends up balancing on the stem. The flip is driven by contact friction torque combined with the asymmetric inertia tensor. Initial state: hemisphere upright on the floor, spinning about world +z at ω ≈ 80 rad/s.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.0005 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast
- `impratio` = 3, `cone` = elliptic

### Default contact
- `solref` = "0.001 1"
- `solimp` = "0.99 0.999 0.0001"

### Floor
- Plane geom
- **`friction` = "0.6 0.02 0.005"** — moderate sliding + sizable torsional component. The torsional friction is what generates the inversion torque under sustained spin; sliding stays below 0.5 so the contact can slip (slip-induced asymmetric torque is the heart of the effect).

### Top body
- Body `top` pos = (0, 0, 0.040) m
- `<freejoint name="top_free"/>`
- Bulb geom: sphere `size` = 0.040, pos (0,0,0), `mass` = 0.060 kg, `friction` = "0.6 0.02 0.005"
- Stem geom: capsule fromto (0,0,0.040) → (0,0,0.085), `size` = 0.0055, `mass` = 0.002 kg, `friction` = "0.6 0.02 0.005"
- Visual equator band (mass=0, no contact): cylinder size 0.0405×0.0035

### Initial state (via `--init-qvel`)
- Linear velocity = 0
- Angular velocity about world +z: ω = 80 rad/s (i.e. qvel last 3 components = (0, 0, 80))

### Camera
- `cam` pos = (0.30, -0.40, 0.13), fovy 36, mode="targetbody" target="top" (tracks the top)
