# coefficient_of_restitution

## Task description
A single ball is dropped onto a hard floor with contact tuned for ~85% coefficient of restitution. Successive bounce heights follow h_n = h₀·e^(2n) where e is the coefficient of restitution, giving a clean geometric decay envelope over roughly 5–8 visible bounces.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.0005 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast
- `impratio` = 3, `cone` = elliptic

### Floor
- Plane geom (default contact)

### Ball
- Body pos = (0, 0, 0.55) m (drop height)
- `<freejoint/>`
- Geom: sphere size 0.05, `mass` = 0.20 kg
- `friction` = "0.4 0.005 0.001"
- **`solref` = "-100000 -16"** — direct stiffness (k = 100000 N/m, c = 16 N·s/m)
- **`solimp` = "0.98 0.999 0.001"** — high impedance, near-elastic
- These give ≈ 85% restitution per bounce

### Camera
- `cam` pos = (0, -1.9, 0.42), fovy 38, side view framing from floor to drop height
