# inelastic_collision

## Task description
One-dimensional collision between two equal-mass spheres on a frictionless floor. Ball A is launched toward stationary ball B with initial v₀ = 1.5 m/s (set via `--init-qvel`). Contact is tuned soft enough to be partially inelastic — the collision dissipates kinetic energy and momentum is shared between the two balls afterwards.

Note: although the scene XML header comment references the "elastic" limit (equal-mass swap), the actual contact tuning here is purposely soft (`solref="-2000 -800"`, `solimp="0.6 0.85 0.001"`) so this scene reads as the **inelastic** collision case, not the elastic one. The two-ball geometry is identical to `elastic_collision.xml`; only the contact stiffness/damping/impedance differ.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.0002 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast
- `impratio` = 10, `cone` = elliptic

### Default contact (inelastic tuning)
- `solref` = "-2000 -800" (k = 2000 N/m, c = 800 N·s/m → highly overdamped contact)
- `solimp` = "0.6 0.85 0.001" (low impedance → soft, energy-absorbing contact)

### Floor
- Plane, `friction` = "0 0 0" (frictionless)

### Ball A (`ballA`)
- Body pos = (-0.60, 0, 0.05) m
- `<freejoint/>`
- Geom: sphere size 0.05, `mass` = 0.20 kg, `friction` = "0 0 0"
- Initial velocity v₀ = +1.5 m/s along +x (via `--init-qvel`)

### Ball B (`ballB`)
- Body pos = (0.10, 0, 0.05) m
- `<freejoint/>`
- Geom: sphere size 0.05, `mass` = 0.20 kg, `friction` = "0 0 0"
- Initial velocity = 0

### Camera
- `cam` pos = (0.4, -2.80, 0.35), fovy 36, side view
