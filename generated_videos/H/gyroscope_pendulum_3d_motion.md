#### `gyroscope_pendulum_3d_motion` — Coupled gyro + pendulum
**Physics:** A spinning gyroscope attached to a pendulum-like hanging rod — combined motion has both gyroscopic precession and pendulum swing.
**Setup:** Vertical rod (length 0.4 m) hung from a pivot via a hinge with axis y; at its bottom, a fast-spinning disc (R=0.10 m, ω=30 rad/s about disc's own axis). Pull pendulum to 30° angle and release.
**Motion:** Bob swings as a pendulum AND the gyro precesses — combined 3D motion.
**Template:** `pendulum.xml` + `spinning_top.xml`.
**Hints:** Render 6 s. 3/4 camera, fovy 40.
