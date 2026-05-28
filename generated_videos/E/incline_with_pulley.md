#### `incline_with_pulley` — Constraint / Atwood variant
**Physics:** Mass on an incline connected over a pulley to a hanging mass — system accelerates if hanging weight > sin(θ)·incline weight. Classic IPhO-style problem.
**Setup:** Inclined ramp + a block on it + a pulley at the top of the ramp + a string over the pulley + a hanging mass on the other side.
**Motion:** If hanging mass is heavy enough, it descends and pulls the incline block up the ramp; otherwise the reverse.
**Template:** `atwood.xml` + `incline_friction.xml`.
**Hints:** Use joint equality (Atwood-style) between the slide joint on incline and the slide joint of the hanging mass. Adjust masses so the dynamics are visible over 3–4 s. Damping in both joints.
