# com_pair_track

## Task description
Two cubes on a frictionless track, masses 2:1. With initial velocities chosen so total momentum is exactly zero, the two masses fly apart in opposite directions but their center of mass stays fixed — exactly what a compressed spring between them at t=0 would produce. A thin vertical brass "COM" post marks the system center of mass and remains permanently aligned with the mass-weighted midpoint.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.001 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast

### Red cube
- Body `red_cube` pos = (-0.10, 0, 0.115) m
- Slide joint `slide_red`: axis=(1,0,0), `damping` = 0
- Geom: box size 0.06×0.06×0.06, `mass` = 0.40 kg
- `contype` = 0, `conaffinity` = 0 (no contacts — pure 1-D motion via slide joint)
- Initial velocity: v_red = -0.30 m/s (via `--init-qvel`)

### Blue cube
- Body `blue_cube` pos = (0.20, 0, 0.115) m
- Slide joint `slide_blue`: axis=(1,0,0), `damping` = 0
- Geom: box size 0.06×0.06×0.06, `mass` = 0.20 kg
- `contype` = 0, `conaffinity` = 0
- Initial velocity: v_blue = +0.60 m/s

### Momentum check
- p = 0.40·(−0.30) + 0.20·(+0.60) = 0 → COM stays still

### Visual elements
- Wood track (visual aid): box size 2.0×0.18×0.025 at (0.4, 0, 0.025)
- COM fiducial: brass cylinder pin at x=0 (system COM), z=0.18, size 0.0045×0.13, with sphere tip at z=0.33, size 0.020 (`contype`=0, `conaffinity`=0)

### Camera
- `cam` pos = (0.4, -2.6, 0.30), fovy 42, side view centered on COM
