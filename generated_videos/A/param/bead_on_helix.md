# bead_on_helix

## Task description
A small bead descends a helical track of 5 turns. Gravity drives the bead along the spiral path; the helical constraint converts vertical fall into combined translation + rotation about the central post. The bead's motion is modelled by a 1-DOF kinematic mechanism: a carrier (hinge about world +z) plus a bead body offset to the helix radius with a slide-z joint, coupled by a joint-equality that enforces q_slide = K·q_rot (K = −pitch/2π).

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.0005 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast
- `impratio` = 2, `cone` = elliptic

### Default contact
- `solref` = "0.002 1"
- `solimp` = "0.95 0.99 0.001"

### Helix geometry (from `gen_bead_on_helix.py`)
- Track radius R = 0.06 m
- Pitch = 0.04 m per turn
- Turns = 5 → total drop = 0.20 m
- Discretization: 28 segments per turn → 140 ramp planks
- Each plank: box size 0.0069×0.030×0.010, bank angle 0.18 rad inward, friction "0.05 0.002 0.0002", `solref` = "0.015 1", `solimp` = "0.92 0.97 0.001"
- Outer fence wall: 140 translucent box pillars at radius R+0.045, half-extents (chord/2)×0.003×0.020

### Bead carrier mechanism
- Carrier body at world origin
  - Inertial: mass = 1e-5 kg, diagonal inertia 1e-9 each (negligible — bead translation dominates)
  - Hinge joint `rot`: axis=(0,0,1), `damping` ≈ DRIVE/ω_terminal where DRIVE = |K|·m·g and ω_terminal = 3.0 rad/s
- Bead body at (R, 0, 0.20)
  - Slide joint `slide`: axis=(0,0,1), `range` = [-0.205, 0.005], `damping` = 0.0001
  - Geom: sphere `size` = 0.012 m, `mass` = 0.003 kg, `contype` = 0, `conaffinity` = 0 (no contacts — equality drives motion)

### Helical coupling equality
- `<joint joint1="slide" joint2="rot" polycoef="0 K 0 0 0"`
- K = −PITCH/(2π) ≈ −0.00637
- After full TURNS·2π rotation, slide reaches −TOTAL_DROP (bottom of spiral)

### Central post (static)
- Cylinder size 0.022 × 0.10 at (0, 0, 0.10), semi-transparent wood

### Camera
- `cam` pos = (0.30, -0.40, 0.13), fovy 34, 3/4 view aimed at helix center (z = 0.10)
