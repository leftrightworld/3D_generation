#### `worm_gear_nonbackdrivable` — Worm gear / self-locking

**Physics:** A worm gear has a high reduction ratio (N:1) and is self-locking — the worm can drive the wheel but the wheel cannot backdrive the worm, because the friction angle exceeds the lead angle. Used in lifts and hoists where loads must not back-drive.
**Setup:** Worm shaft: cylinder (R = 0.015 m) on a hinge about x, init-qvel ω = 10 rad/s. Worm wheel: cylinder (R = 0.10 m) on a hinge about z. Joint equality coupling: wheel_angle = worm_angle / 20 (20:1 ratio). High rotational friction/damping on worm shaft hinge (damping = 5 N·m·s) acts as the self-locking mechanism. Render scene (a): normal drive (worm spins, wheel turns slowly). Scene (b): give wheel init-qvel, observe worm stays still.
**Motion:** Render 4 s each. (a) Worm rotates at 10 rad/s, wheel at 0.5 rad/s. (b) Wheel given 2 rad/s, worm stays near-stationary. Camera: 3/4 isometric.
**Template:** `gear_train_2_gears.xml` (joint equality coupling).
**Hints:** True self-locking requires friction between the worm thread and wheel tooth faces — approximated here by high damping on the worm hinge that resists reverse torque. Joint equality polycoef = "0 0.05 0 0 0" (ratio 1/20).

---
