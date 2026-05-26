# cone_balanced_on_tip

## Task description
An inverted smooth cone is in unstable equilibrium standing on its apex. Any small perturbation breaks the symmetry; the restoring torque about the apex is negative (gravity amplifies the tilt) so the motion accelerates from imperceptible to a full topple in roughly 1.5 s. A tiny initial tilt (~0.2°) about the y-axis seeds the instability.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.0005 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast
- `impratio` = 3, `cone` = elliptic

### Floor
- Plane geom; **`friction` = "0.8 0.01 0.001"**

### Cone body
- Body `cone` pos = (0, 0, 0.001) m (apex barely above floor)
- Initial quaternion: (0.999998, 0, 0.001750, 0) — ~0.2° tilt about +y (seeds instability)
- `<freejoint/>`
- Mesh geom (`cone_mesh`):
  - Apex at (0,0,0), base centered at (0,0,0.20)
  - Base radius 0.06 m, height 0.20 m
  - 64 vertices around the base + 1 apex + 1 base-center (66 verts total)
  - `mass` = 0.1 kg
  - `friction` = "0.8 0.01 0.001"
  - `condim` = 3
  - `solref` = "0.005 1"
  - `solimp` = "0.95 0.99 0.001"

### Camera
- `cam` pos = (0.05, -0.90, 0.08), fovy 30, side view framing both upright and toppled states
