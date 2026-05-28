#### `elastic_longitudinal_wave_chain` — Longitudinal waves

**Physics:** A compressive impulse in a 1D mass-spring chain propagates as a longitudinal (P-wave) at speed v = √(k/m) × Δx — distinct from transverse waves in existing scenes; the compressions and rarefactions travel along the chain axis.
**Setup:** 30 masses (M = 0.01 kg each, box 0.010 × 0.010 × 0.010 m) spaced at Δx = 0.02 m along the x-axis. Each connected to its neighbours by a hinge joint with stiffness k = 1000 N/m along the x-direction (slide joints, not hinges). All slide joints constrained to x-axis only. Mass 0 (leftmost) given init-qvel vx = 1.5 m/s. All other masses stationary. No gravity (gravity = "0 0 0").
**Motion:** render 2 s. A compression wave propagates from left to right. Observe individual masses oscillating longitudinally (along x) as the wave passes. Wave speed v_theory = √(k·Δx²/m) = √(1000×0.0004/0.01) = √40 ≈ 6.3 m/s → wave traverses 30 × 0.02 = 0.6 m in ~0.1 s. Camera: top-down view (pos (0, 0, 0.5), fovy = 60), showing all 30 masses from above.
**Template:** `dominoes.xml` (chain of bodies) + `spring_mass.xml` (stiffness values). Bodies connected by slide joints (axis "1 0 0"), gravity disabled. gen_longitudinal_wave.py sets up all 30 bodies and joints.
**Hints:** Wave speed v = Δx × √(k/m) = 0.02 × √(1000/0.01) = 0.02 × 316 = 6.3 m/s. Render 2 s shows the wave traverse the chain ~20 times — use timestep = 0.0001 for accurate wave propagation. Distinguished from transverse wave scenes by motion direction (along chain axis, not perpendicular). See gotchas.md §longitudinal_waves.

---
