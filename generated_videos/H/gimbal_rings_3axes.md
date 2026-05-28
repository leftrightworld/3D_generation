#### `gimbal_rings_3axes` — Rotational DOF
**Physics:** Three nested gimbals provide three independent rotational DOFs; when two axes align, "gimbal lock" reduces effective DOF to 2.
**Setup:** Outer ring (R=0.20 m) hinged to a fixed stand, axis z. Inner ring (R=0.15 m) hinged to outer, axis y. Innermost ring (R=0.10 m) hinged to inner, axis x. Small rotor inside the innermost ring. Initial qvel: each ring 1-2 rad/s on its own axis.
**Motion:** All three rings rotate independently. If you tune initial conditions, you can show gimbal lock (when two axes coincide).
**Template:** `spinning_top.xml` + `conical_pendulum.xml` (gimbal pattern).
**Hints:** Programmatic gen for the rings. Side view. Render 5 s.
