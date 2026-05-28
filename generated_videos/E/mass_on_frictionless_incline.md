#### `mass_on_frictionless_incline` — Constraint
**Physics:** Block on a frictionless inclined plane has acceleration a = g·sin(θ) regardless of mass.
**Setup:** Inclined ramp + a block constrained to slide along its surface (slide joint along the ramp's surface direction).
**Motion:** Block accelerates down the ramp; with no friction, motion is pure linear acceleration along the slope.
**Template:** `incline_friction.xml`. Drop friction to 0.
**Hints:** Set ALL friction values to 0 (block AND ramp — gotcha #1!). Slide joint along the ramp surface gives clean physics without contact instability. Camera: side view. Render 2 s.
