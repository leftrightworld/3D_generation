#### `rotor_wheel_off_axis_wobble` — Imbalance
**Physics:** A wheel with its center of mass offset from its rotation axis wobbles as it spins. Whole system vibrates.
**Setup:** Wheel (R=0.10 m) with its axle going through a point offset 0.025 m from the wheel's true center. Axle on a hinge with init-qvel ω=10 rad/s.
**Motion:** Wheel spins, but visibly wobbles up-and-down (the offset center swings around the axle).
**Template:** `maxwell_wheel.xml` + `spinning_top.xml`.
**Hints:** Use `<inertial>` to position the COM off-center. Side view. Render 3 s.
