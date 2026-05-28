#### `gyroscope_on_incline_precesses` — Gyro on slope / non-vertical precession axis

**Physics:** A fast-spinning gyroscope placed on an inclined surface experiences gravity along the slope-normal direction. Its precession axis is the slope normal (not vertical), causing the spin axis to sweep a cone around a tilted axis — visually striking.
**Setup:** Inclined floor at 15° to horizontal. Gyroscope disc (R = 0.08 m, M = 0.30 kg, thin cylinder) with freejoint, placed on the slope. init-qvel: spin ω = 60 rad/s about the disc's own symmetry axis (initially pointing up the slope), no translational velocity.
**Motion:** Render 5 s. Gyroscope precesses around the slope-normal axis; the spin axis traces a tilted cone — not around vertical but around the slope's upward normal. Camera: 3/4 view from above the incline, fovy = 45.
**Template:** `spinning_top.xml` (spin init) + `incline_friction.xml` (tilted floor). Tilt world floor geom 15°.
**Hints:** The precession axis is normal to the slope, not to the world vertical. Precession rate Ω = M·g·cos(15°)·L / (I·ω). Floor friction = 0.4 to maintain contact without excessive sliding. init-qvel in world frame: see gotchas.md §world_frame_angular_qvel for converting body-frame ω to world-frame qvel.

---
