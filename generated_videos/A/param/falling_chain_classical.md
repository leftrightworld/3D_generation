# falling_chain_classical

## Task description
A 24-segment chain initially L-shaped: half on a table, half hanging off the edge. Released from rest under gravity; the hanging portion's weight progressively drags the on-table portion off, and chain acceleration exceeds g once most of it is airborne.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.0005 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast
- `impratio` = 3, `cone` = elliptic

### Chain (25 bodies ch0..ch24)
- Root body `ch0` pos = (0.020, 0, 0.831), `<freejoint/>` (whole chain free to fall)
- Each subsequent body offset (0.04, 0, 0) from its parent — total 25 links
- Each link hinge (`hc1`..`hc24`):
  - type = hinge, axis=(0,1,0)
  - **`stiffness` = 0.0008 N·m/rad** (very low — chain hangs flexibly)
  - **`damping` = 0.0005**
- Each link geom: box size 0.0180×0.012×0.011 at pos (0.0200, 0, 0)
  - `mass` = 0.012 kg per link
  - `friction` = "0.30 0.005 0.001"

### Table (static)
- Tabletop `ttop`: box size 0.5×0.18×0.025 at (0, 0, 0.775), `friction` = "0.30 0.005 0.001"
- Four legs (size 0.03×0.03×0.375), all material `table_leg`
- Right edge of table at x = +0.5 — chain initially crosses this edge

### Camera
- `cam` pos = (0.30, -1.50, 0.70), fovy 42, side view looking at table edge
