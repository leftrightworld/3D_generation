#### `lissajous_2d_spring_mass` — Parametric curves

**Physics:** A mass on two perpendicular springs with incommensurable natural frequencies traces closed Lissajous figures in 2D. For ω_x : ω_z = 1 : 2 (achieved by k_z = 4 k_x), the trajectory is a figure-8 in the xz-plane.
**Setup:** Single bob (M = 0.1 kg) with two independent slide joints: one along x (stiffness k_x = 100 N/m, equilibrium x = 0) and one along z (stiffness k_z = 400 N/m, equilibrium z = 0). init-qpos: x = 0.05 m, z = 0. init-qvel: ẋ = 0, ż = 0 (starts from x-displaced rest). No damping.
**Motion:** render 10 s. The bob traces a clean figure-8 Lissajous pattern in the xz-plane. Camera: front view, orthographic recommended, fovy = 30, pos (0, -0.5, 0).
**Template:** `spring_mass.xml`. Replace the single slide joint with two orthogonal slide joints (axes "1 0 0" and "0 0 1"). Add spring stiffness via `<joint ... stiffness="100">` (x) and `<joint ... stiffness="400">` (z).
**Hints:** Use zero damping (`damping="0"`) for persistent Lissajous pattern. For k₁ : k₂ = 1 : 4 and starting from x-displacement only, the pattern is 1:2 (figure-8). Add a tracer geom (small sphere) or use the ball itself. The scene should run long enough (≥ 10 s) to show the closed curve traced multiple times. See gotchas.md §spring_stiffness.

---
