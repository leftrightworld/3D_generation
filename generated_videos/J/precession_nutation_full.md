#### `precession_nutation_full` — Euler angles / gyroscope

**Physics:** A spinning top at a large nutation angle (40°) exhibits both slow precession (spin axis orbits the vertical) and superimposed nutation (wobbling of the spin axis up and down), demonstrating the full complexity of Euler angle dynamics beyond the small-angle limit.
**Setup:** Top (M = 0.3 kg, principal moments I_axial = 5×10⁻⁴ kg·m², I_transverse = 3×10⁻⁴ kg·m²) with a ball tip touching the floor. init-qpos: Euler angles giving θ = 40° nutation (tilt from vertical). init-qvel: spin ω_spin = 50 rad/s about the top's symmetry axis; precession and nutation rates initially zero (giving maximum nutation wobble).
**Motion:** render 6 s at least 2 full precession cycles. Observe: the spin axis sweeps a cone (precession) and simultaneously oscillates between two nutation angles (wobble). Camera: 3/4 view, pos (0.5, −0.5, 0.3), fovy = 40.
**Template:** `spinning_top.xml`. Adjust inertia tensor components via `<inertial diaginertia="...">`. Set nutation angle via quaternion in init-qpos: quat = [cos(θ/2), sin(θ/2), 0, 0] gives tilt θ about x.
**Hints:** With zero initial precession rate and θ = 40°, the top will nutate between 40° and a second nutation angle determined by energy/angular momentum conservation. Render long enough (6 s) to see ≥ 2 precession cycles. MuJoCo's freejoint or ball joint work; if using freejoint, set full 6-DOF initial conditions carefully. See gotchas.md §spinning_top_init.

---
