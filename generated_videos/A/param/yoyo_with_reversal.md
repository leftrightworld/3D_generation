# yoyo_with_reversal

## Task description
Maxwell wheel / yo-yo: a heavy disc with a thin axle is suspended by two strings wound around the axle. As the wheel descends it must rotate to unspool the strings; rolling-without-slip is enforced by a joint equality constraint between the vertical slide and the rotational hinge. The slider hits a stop at its lower limit, causing the wheel to bounce back up and re-ascend while still spinning in the same direction. Demonstrates rotational + translational KE: a = g / (1 + I/(M·r_axle²)).

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.001 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast

### Wheel body
- Body pos = (0, 0, 0.95) m
- Slide joint `slider`: axis=(0,0,1), `damping` = 0.001, `range` = [-0.40, 0.05]
  - `solreflimit` = "-200000 -20" (very stiff range stop for elastic bounce)
  - `solimplimit` = "0.99 0.999 0.0001"
- Hinge joint `axle`: axis=(0,1,0), `damping` = 0.0005
- Disc geom: cylinder fromto (0,-0.006,0) → (0,0.006,0), `size` = 0.080, `mass` = 0.50 kg, brass
- Axle geoms (mass = 0): two thin cylinders extending y to ±0.046, size 0.008

### Rolling-without-slip equality
- `<joint joint1="slider" joint2="axle" polycoef="0 0.008 0 0 0"`
- Enforces q_slider − 0.008·q_axle = 0 (axle radius r_axle = 0.008 m)
- Predicted descent acceleration ≈ 0.192 m/s² (M=0.5, R=0.08, I=½MR²=0.0016)

### Strings (visual)
- Two `<spatial>` tendons, width 0.0012, sites cross_L/R ↔ axle_L/R_site
- Decoration only — physics is the equality

### Stand
- Two posts: cylinders at x=±0.25, length 1.05 m, radius 0.018
- Crossbar at z=1.05, size 0.30×0.025×0.020

### Camera
- `cam` pos = (1.20, -0.85, 0.65), fovy 38, 3/4 view from front-right
