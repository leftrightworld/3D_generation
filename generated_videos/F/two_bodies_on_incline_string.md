#### `two_bodies_on_incline_string` — Friction + constraint
**Physics:** Two blocks on an incline connected by a string. If they have different μ, internal string tension develops; they slide as a unit at an intermediate speed.
**Setup:** Inclined ramp at 25°. Two blocks on it (separated 0.15 m along the slope), connected by a tendon. Block A (uphill): μ=0.1 (low). Block B (downhill): μ=0.4 (high).
**Motion:** Both blocks slide down at the same speed (locked by the string); intermediate between their solo speeds.
**Template:** `incline_friction.xml` + `atwood.xml` (tendon).
**Hints:** Tendon visible. Side view, pos (1.0, -1.5, 0.3), fovy 40. Render 3 s.
