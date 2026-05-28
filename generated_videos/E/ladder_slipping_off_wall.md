#### `ladder_slipping_off_wall` — Friction / statics
**Physics:** A ladder leans against a wall, supported by friction at the floor and the wall. If μ is too low, the ladder slips outward (foot slides, top slides down).
**Setup:** A long thin rod leaning at ~60° against a vertical wall. Friction values at the floor and wall contact tuned.
**Motion:** With high μ: static. With low μ: ladder slips outward.
**Template:** `incline_friction.xml`.
**Hints:** Use a freejoint for the ladder body. Floor and wall geoms. Tune friction so the demo is at the edge of stability. Render 3–4 s.
