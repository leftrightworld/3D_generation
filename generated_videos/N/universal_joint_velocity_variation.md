#### `universal_joint_velocity_variation` — Cardan joint / velocity ripple

**Physics:** A Hooke's (Cardan) universal joint connecting two shafts at angle θ = 30° transmits constant torque but produces sinusoidal output angular velocity variation: ω_out = ω_in·cos θ/(1 − sin²θ·cos²φ), oscillating ±15% per revolution.
**Setup:** Input shaft: cylinder (L = 0.15 m, R = 0.015 m) on a fixed hinge (axis y), init-qvel ω = 4 rad/s. Cross-piece: small plus-shaped body with two perpendicular hinges connecting input and output shafts. Output shaft: same cylinder, hinge axis rotated 30° from input. Bright colored marker disc on each shaft end to visualize speed.
**Motion:** Render 4 s (~2.5 revolutions). Input marker rotates uniformly. Output marker visibly speeds up and slows down twice per revolution. Side view, fovy = 40.
**Template:** `four_bar_linkage.xml` (crossed hinge concept). gen_universal_joint.py for the cross-piece geometry.
**Hints:** The cross-piece must have exactly two perpendicular hinges — one matching the input shaft axis, one perpendicular for the output. The 30° shaft angle is the key parameter for visible variation. Add a velocity-indicator (arm length proportional to current ω) if possible via colored sector geom.

---
