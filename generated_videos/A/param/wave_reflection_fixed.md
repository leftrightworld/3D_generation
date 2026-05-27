# wave_reflection_fixed

## Task description
A pulse propagating along a discretized string reflects off a fixed (clamped) end with inverted polarity. The string is a chain of 41 small bodies linked by hinge joints with rotational stiffness; the left end is rigidly attached to a wooden wall, the right end is free. An initial Gaussian pulse encoded as hinge angles propagates to the wall and returns inverted.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.0002 s
- **`gravity` = (0, 0, 0)** — turned off so the string doesn't sag
- `integrator` = implicitfast

### Chain (41 nodes n0..n40)
- Root body `n0` at world (0, 0, 1.0), rigidly attached (no joint) — this is the clamped/fixed end
- Each subsequent body n_k offset (0.05, 0, 0) from its parent
- Each hinge joint (h1..h40):
  - type = hinge, axis=(0,1,0)
  - **`stiffness` = 0.06 N·m/rad**
  - **`damping` = 0.0002** (very light damping for long-lived pulse)
- Each node geom: box size 0.0225×0.012×0.01, pos (0.0250, 0, 0), `mass` = 0.01 kg
- `contype` = 0, `conaffinity` = 0 (no contact — pure dynamics)
- Total chain length ≈ 41 × 0.05 = 2.05 m

### Initial state
- Pulse encoded as initial hinge angles via `--init-qpos` (typical: Gaussian centered on chain interior)

### Wall (static)
- Box geom: size 0.04×0.18×0.18 at (-0.04, 0, 1.0)

### Camera
- `cam` pos = (1.000, -1.900, 1.000), fovy 42, side view perpendicular to chain
