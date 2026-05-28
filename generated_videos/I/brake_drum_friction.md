#### `brake_drum_friction` — Friction / energy dissipation
**Physics:** A spinning drum is slowed by a friction brake pressing on its rim. Kinetic energy dissipated as heat (or in this case, just observed as slowing rotation).
**Setup:** A heavy disc (drum) R=0.15 m, M=1 kg, on a vertical axle, spinning at ω=20 rad/s. A "brake pad" (block on a slide joint) pressed against the rim with some normal force.
**Motion:** Drum spins; friction torque slows it down; eventually stops.
**Template:** `maxwell_wheel.xml` + `incline_friction.xml`.
**Hints:** Brake pad against the rim has friction coefficient. Render 4 s.
