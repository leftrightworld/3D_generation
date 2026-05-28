#### `tipping_vs_sliding` — Friction / statics
**Physics:** A tall block on an inclined plane either tips over or slides, depending on the ratio of its height/width vs μ — the tipping angle is arctan(w/h), the sliding angle is arctan(μ).
**Setup:** Two side-by-side blocks on the same incline: one tall (high h/w), one short (low h/w). Same μ for both. Increase incline gradually.
**Motion:** As the incline tilts, the tall block tips first while the short one is still static; then the short block slides.
**Template:** `incline_friction.xml`. Two blocks with different aspect ratios.
**Hints:** Use a hinged or sliding incline (joint with init velocity to gradually tilt) or just set the incline at a critical angle showing both behaviors at once. Side view camera. Render 4 s.
