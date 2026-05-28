#### `pendulum_with_lateral_spring` — Oscillation / coupling
**Physics:** A pendulum attached to a horizontal wall-spring shows mode coupling: pure swing and pure spring oscillation are eigenstates only when carefully tuned; otherwise energy sloshes between them.
**Setup:** Hinge-pivoted pendulum with a spring connecting its mass to a horizontal wall.
**Motion:** Initially energy goes into the pendulum swing; over time it transfers to the spring's vibration, then back.
**Template:** `pendulum.xml` + `spring_mass.xml`.
**Hints:** Tune string length and spring k so the periods are close — that gives the strongest beats-like transfer. Render 15 s.
