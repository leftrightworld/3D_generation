#### `spherical_pendulum_2d` — Oscillation
**Physics:** A pendulum with 2D bob motion (instead of constrained to a plane) traces complex Lissajous-like patterns. Period not necessarily commensurate, so trajectory can be quasi-periodic.
**Setup:** Single bob hung from a pivot at world (0, 0, 1.2) via a 2-DOF gimbal: outer hinge axis y (pitch), inner hinge axis x (roll) — see gotcha #8 for why this is better than a ball joint. Bob: sphere R=0.025 m, M=0.10 kg, at the end of a 0.6 m rod from pivot. Initial qpos: pitch=0.5 rad, roll=0; init-qvel: roll_rate=0.8 rad/s.
**Motion:** Bob traces a rosette pattern in the xy plane (as projected) — not a circle, not a flat line.
**Template:** `conical_pendulum.xml` (gimbal pattern).
**Hints:** Use a long render (10 s) so the pattern becomes visible. Top-down camera, pos (0, 0, 0.4), xyaxes="1 0 0  0 1 0", fovy 42.

---
