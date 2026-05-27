# arch_compression

## Task description
A Roman semicircular arch made of 15 voussoir (wedge) blocks plus a distinct keystone, supported by two piers, with a heavy block dropping onto the apex. The arch transmits the load through purely compressive forces along its curved spine and out to the piers. To make the demo numerically robust, the voussoirs are static worldbody geoms (effectively infinite mass) so the arch is guaranteed stable; the dynamic story is the falling load landing on the keystone.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.001 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast
- `impratio` = 3, `cone` = elliptic

### Default geom (contact)
- `friction` = "0.85 0.04 0.005" (high friction for rigid stack behavior)
- `solref` = "0.003 1"
- `solimp` = "0.97 0.99 0.001"

### Arch geometry (from `gen_arch_compression.py`)
- Inner radius R_IN = 0.40 m
- Outer radius R_OUT = 0.55 m
- Mid radius R_MID = 0.475 m
- N voussoirs = 15 (each spans π/15 ≈ 12°)
- Block depth (y half-extent) = 0.14 m
- Tangent half-length per block ≈ R_MID · sin(Δ/2) · 1.03 (≈3% overlap)
- Radial half-extent = (R_OUT − R_IN)/2 = 0.075 m
- All voussoirs are static worldbody geoms (no body, no joint)
- Voussoir mass parameter VOUS_MASS = 0.40 kg (unused while static)
- Keystone = middle block (index 7), distinct material

### Piers (static)
- Two pier blocks, one each side at x = ±0.475 m
- Top face at z = Z_BASE = 0.20 m
- Half-sizes (0.10, 0.145, 0.10)

### Load (dynamic)
- Body `load` at (0, 0, R_OUT + Z_BASE + 0.04 + 0.25) ≈ (0, 0, 1.04) m
- `<freejoint/>`
- Geom: box size 0.12×0.08×0.04, `mass` = 0.25 kg
- Drops ~25 cm onto the keystone

### Camera
- `cam` pos = (0, -2.20, 0.4750), fovy 36, pure side profile (xyaxes = "1 0 0 / 0 0 1")
