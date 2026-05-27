# slider_crank_mechanism

## Task description
Slider-crank linkage — the basic mechanism used in every internal-combustion engine. A continuously rotating crank disc drives a reciprocating piston via a connecting rod. Because MuJoCo's body tree is a tree, the closed kinematic loop (crank → rod → piston → ground) is closed by a `<connect>` equality constraint that locks the rod's far end to the piston pin.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.001 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast

### Default
- All joints: `damping` = 0.01 (set via `<default><joint damping="0.01"/></default>`)

### Crank body
- Body `crank` pos = (0, 0, 0.30) m
- Hinge `crank_h`: axis=(0,1,0), `damping` = 0.001
- Crank disc geom: cylinder size 0.10×0.014, pos (0, 0.07, 0), `mass` = 0.05 kg
- Crank pin (visual, no contact): cylinder size 0.012×0.030 at (0.08, 0.10, 0), mass 0.005
- Crank radius R = 0.08 m (pin offset)
- Initial angular velocity: provided via `--init-qvel` on `crank_h` to spin the crank

### Connecting rod body (nested inside crank)
- Body `rod` pos = (0.080, 0.10, 0) relative to crank
- Hinge `rod_h`: axis=(0,1,0), `damping` = 0.001
- Rod geom: box size 0.150×0.010×0.008 at pos (0.150, 0, 0), `mass` = 0.04 kg
- Rod length L = 0.30 m
- End cylinder geom (visual, no contact): size 0.010×0.018 at (0.300, 0, 0), mass 0.005

### Piston body
- Body `piston` pos = (0.380, 0.10, 0.30) m
- Slide `piston_s`: axis=(1,0,0), `damping` = 0.005
- Piston geom: box size 0.04×0.04×0.03, `mass` = 0.06 kg, `contype` = 0, `conaffinity` = 0

### Closure equality
- `<connect site1="pin_rod_end" site2="pin_piston"/>`
- 3-DOF constraint forcing the rod's far end and the piston pin to share world position

### Static frame
- Wood base: box 0.55×0.15×0.02 at (0.25, 0, 0.02)
- Bearing block: box 0.05×0.07×0.16 at (0, -0.03, 0.20)
- Two rails: box 0.18×0.06×0.010 at (0.300, 0.10, 0.345) and (0.300, 0.10, 0.255)

### Camera
- `cam` pos = (0.35, -1.25, 0.42), fovy 34, 3/4 from front-right
