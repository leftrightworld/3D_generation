# coin_spiral

## Task description
Euler's disk / coin spiral: a thin disc set on its edge with a small tilt and large spin loses energy to floor friction, gradually tilting more and rolling on a smaller effective contact radius. Pitch of the precession audibly rises in the real demo; visually the precession speeds up and the coin finally lies flat after a few seconds.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.0005 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast
- `impratio` = 3, `cone` = elliptic

### Default contact
- `solref` = "0.002 1"
- `solimp` = "0.98 0.995 0.0001"

### Floor
- Plane geom; **`friction` = "1.2 0.020 0.008"** — high sliding friction so contact point doesn't drift; small torsional/rolling friction so spin angular momentum survives long enough to show the spiral.

### Coin body
- Body pos = (0, 0, 0.027) m (lowest rim ≈ 3 mm above floor at 75° tilt)
- `<freejoint/>`
- Geom `coin_face`: cylinder size 0.025 × 0.0015 (R = 25 mm, half-thickness 1.5 mm)
- `mass` = 0.008 kg
- `friction` = "0.6 0.002 0.0005"
- Decorative mark on top (box 0.012×0.0035×0.0006, mass 0, no contact) — makes spin orientation legible
- Initial orientation: ~75° tilt from vertical (disc plane nearly vertical)

### Camera
- `cam` pos = (0.16, -0.22, 0.11), fovy 34, 3/4 view from front-right
