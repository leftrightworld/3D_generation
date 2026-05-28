#### `gyroscope_resists_tipping` — Gyroscopic stabilization

**Physics:** A fast-spinning gyroscope resists applied torques by precessing perpendicular to the applied force — a torque about the x-axis causes precession about the z-axis rather than tipping about x; this gyroscopic rigidity is the basis for gyro stabilizers and navigation instruments.
**Setup:** Gimbal frame (box 0.20 × 0.01 × 0.10 m, M = 0.1 kg) connected to world via hinge (x-axis). Gyro disc (R = 0.07 m, M = 0.3 kg, thickness 0.01 m) inside frame on a second hinge (y-axis). init-qvel: disc spin ω = 80 rad/s about y-axis. init-qpos: frame horizontal (0°). At t = 0.5 s, an impulsive force F = 5 N for 0.1 s applied to frame in z-direction (pushing it sideways).
**Motion:** render 5 s. Without spin: frame would simply tip and swing about the x-axis hinge. With spin (ω = 80): instead, frame precesses about z (rotates in the horizontal plane) — the gyro resists the tipping. Camera: 3/4 view, pos (0.4, −0.4, 0.3).
**Template:** `spinning_top.xml` + `conical_pendulum.xml` (gimbal structure). Frame body with hinge (x-axis) to world. Gyro disc body with hinge (y-axis) to frame. Apply the impulse force in the gen script using `mj_applyFT` at the specified time.
**Hints:** Precession rate Ω_p = τ/(I·ω) = F·r/(I·ω) = 5×0.1/(½×0.3×0.07²×80) ≈ 5×0.1/0.0588 ≈ 8.5 rad/s. This means the frame rotates ~4.25 rad in 0.5 s — clearly visible. The gyro effectively "stores" the applied torque as precession momentum. See gotchas.md §gyroscope_precession.

---
