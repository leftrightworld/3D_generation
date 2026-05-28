#### `spinning_top_on_incline` — Gyroscope / precession around tilted axis

**Physics:** A spinning top on a tilted surface precesses around the local gravitational vertical (the surface normal), not the world vertical. The precession cone axis is tilted from vertical by the slope angle, creating visually distinct "slanted" precession circles.
**Setup:** Floor tilted 15° from horizontal (geom euler = "0 −15 0"). Spinning top (standard cone+stem body, M = 0.05 kg, cone R = 0.035 m) with freejoint, placed on the slope. init-qvel: spin ω_spin = 60 rad/s about top's symmetry axis (pointing approximately along slope-normal direction), no translational velocity. init-qpos: tip at contact point on slope.
**Motion:** Render 6 s. Top precesses around the slope-normal axis, tracing circles that are tilted from vertical — clearly different from the same top on a flat floor. Camera: oblique view showing the tilted precession cone, pos (0.5, −0.6, 0.4), fovy = 38.
**Template:** `spinning_top.xml`. Tilt the floor geom. Adjust init-qpos/qvel to match slope geometry.
**Hints:** On the slope, effective gravity = g·cos(15°) ≈ 9.48 m/s² perpendicular to slope. Precession rate Ω = M·g·cos(15°)·d/(I·ω_spin) where d is the distance from tip to COM. Floor friction = 0.4. See gotchas.md §world_frame_angular_qvel for setting spin in world frame.

---
