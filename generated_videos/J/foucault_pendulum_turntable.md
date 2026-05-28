#### `foucault_pendulum_turntable` — Rotating frame / Coriolis

**Physics:** A pendulum mounted on a slowly rotating horizontal platform precesses its swing plane in the lab frame due to the Coriolis effect — analogous to Earth's rotation causing real Foucault pendulum precession.
**Setup:** Platform disk (M = 1 kg, R = 0.15 m, thickness 0.01 m) connected to the world via a hinge joint about z with init-qvel ω_plat = 0.3 rad/s. Pendulum pivot attached to the platform surface; pendulum L = 0.4 m, M = 0.1 kg, hanging from platform. init-qvel: pendulum ω = 2 rad/s about the platform-frame x-axis.
**Motion:** render 15 s. In the lab frame, the pendulum swing plane slowly rotates as the platform turns. Observe at least 1–2 full platform rotations and the corresponding swing-plane rotation. Camera: top-down, pos (0, 0, 0.8), fovy = 50.
**Template:** `conical_pendulum.xml`. Replace the fixed pivot with a platform body having a z-hinge joint. Pendulum body parented to platform.
**Hints:** Platform rotation must be frictionless (damping = 0 on z-hinge) to sustain steady rotation. The pendulum swing damps naturally in MuJoCo due to joint damping — set damping = 0.001 (minimal). Use 15 s render to see clear precession. The turntable angular velocity ω_plat = 0.3 rad/s means one full rotation in ~21 s, so 15 s shows about 3/4 of a rotation. See gotchas.md §rotating_frames.

---
