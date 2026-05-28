#### `elastic_wave_2d_grid_pulse` — 2D wave propagation

**Physics:** A 2D mass-spring grid with fixed boundaries supports circular wave fronts after a central impulse; the wave speed is isotropic in the limit of small spacing and the circular ripple expands at v = Δx × √(k/m).
**Setup:** 7×7 grid of masses (M = 0.005 kg each) on slide joints (z-axis only) with spacing 0.03 m in x and y. Adjacent masses connected by stiff springs (k = 500 N/m, implemented as hinge stiffness or actuator springs). Edge masses (border of the 7×7 grid) have their slide joint fixed to world (range = "0 0"). Central mass (position [3,3]) given init-qvel vz = 0.5 m/s. No gravity (gravity = "0 0 0" to isolate wave from sag).
**Motion:** render 3 s. A circular ripple radiates outward from the central mass, reflects off the fixed boundaries, and creates interference patterns. Camera: top-down, pos (0, 0, 0.5), fovy = 45 (looking straight down), showing all 49 masses.
**Template:** `gen_pendulum_waves.py` (adapted for 2D grid). gen_elastic_grid.py creates 49 bodies, 2×(7×6) spring connections (horizontal and vertical), fixed edge joints. Slide joints along z only. Springs between adjacent bodies use actuator (position spring) or joint stiffness.
**Hints:** Wave speed v = 0.03 × √(500/0.005) = 0.03 × 316 = 9.5 m/s → wave crosses 7×0.03 = 0.21 m in 0.022 s. The wave will traverse the grid many times in 3 s, creating complex standing-wave patterns. This is the main visual payoff: concentric ripples + reflection interference. See gotchas.md §2d_spring_grid.

---
