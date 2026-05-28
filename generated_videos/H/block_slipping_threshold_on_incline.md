#### `block_slipping_threshold_on_incline` — Friction transition
**Physics:** A block on an incline is static if angle θ < arctan(μ); above that angle, it slides. The transition is abrupt.
**Setup:** Incline angle slowly increases over time (init-qvel slowly tilts the ramp). Block on the incline with μ=0.4 (so critical angle ~22°).
**Motion:** Block stays static while ramp tilts; at critical angle it suddenly starts sliding and accelerates down.
**Template:** `incline_friction.xml` + `tipping_vs_sliding.xml`.
**Hints:** Initial ramp tilt 0°, init-qvel small rotation rate. Render 4 s.
