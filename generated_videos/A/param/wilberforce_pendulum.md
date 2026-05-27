# wilberforce_pendulum

## Task description
A mass hangs on a spring that has both longitudinal and torsional stiffness. With the two periods (bobbing vs. twisting) matched within a few percent and a weak coupling between them, energy slowly trades between bobbing and twisting modes — the classic Wilberforce beat pattern. Implementation: one body with a slide-z joint and a hinge-z joint, each with its own spring stiffness, plus a soft equality constraint providing the off-diagonal coupling that real spring helices have.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.001 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast

### Bob body
- Body pos = (0, 0.20, 1.25) m
- Slide joint `slide_z`: axis=(0,0,1), `stiffness` = 50 N/m, `damping` = 0.04, `range` = [-0.5, 0.5], `springref` = 0
- Hinge joint `hinge_z`: axis=(0,0,1), `stiffness` = 0.16 N·m/rad, `damping` = 0.0006, `range` = [-6.28, 6.28], `springref` = 0
- Cylinder bob `bob_core`: size 0.08×0.08, `mass` = 0.5 kg
- Visual crossarms (mass=0, no contact): two perpendicular capsules length 0.44 m, radius 0.012
- Marker beads (mass=0): 4 spheres at arm tips, radius 0.024 (brass on x axis, blue on y axis)

### Period tuning
- T_slide = 2π·√(m/k_slide) = 2π·√(0.5/50) ≈ 0.628 s
- T_torsion = 2π·√(I_z/k_tors) = 2π·√(0.0016/0.16) ≈ 0.628 s
- I_z = ½·m·R² = 0.5·0.5·(0.08)² = 0.0016 kg·m²

### Coupling equality
- `<joint joint1="slide_z" joint2="hinge_z" polycoef="0 0.025 0 0 0"`
- `solref` = "0.6 1", `solimp` = "0.012 0.040 0.001" (soft → weak spring coupling)
- Enforces q_slide ≈ 0.025·q_hinge weakly; coupling time scale ~3 s

### Spring visual
- `<spatial>` tendon "spring_vis", width 0.014, anchor (0, 0.20, 1.99) ↔ hook (0,0,0.08)

### Camera
- `cam` pos = (0, -1.45, 1.18), fovy 30, front-facing tight on bob
