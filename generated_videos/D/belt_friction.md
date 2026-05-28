#### `belt_friction` — Friction / coupled rotation
**Physics:** A belt connecting two pulleys couples their rotation — if pulley radii differ, the angular velocities differ inversely. With sufficient slip, the belt slides instead of driving.
**Setup:** Two pulleys (different radii) connected by a closed loop tendon "belt". One pulley is driven (initial spin); the other should follow.
**Motion:** Driven pulley spins; belt transfers motion; driven pulley spins at scaled velocity.
**Template:** `maxwell_wheel.xml` + `atwood.xml` (for tendon as belt).
**Hints:** Belt as a tendon-loop is approximate — true belt-pulley coupling needs friction simulation along the tendon, which MuJoCo doesn't do well. Workaround: use a joint equality coupling the two hinges directly (polycoef = -r₁/r₂). The tendon is purely visual. Render 4 s.

---
