#### `com_pair_track` — Momentum
**Physics:** Two masses on a frictionless track connected by a compressed spring — when released, they fly apart, but the center of mass stays still (momentum conservation).
**Setup:** Two cubes on a horizontal frictionless slider track, with a compressed (or stretched) spring between them. Spring releases at t=0.
**Motion:** The two masses fly apart in opposite directions; visibly, their midpoint never moves.
**Template:** `spring_mass.xml` + `elastic_collision.xml`.
**Hints:** Initialize the spring with stored energy (tendons may need init-qvel that gives them stored PE, or use a stiff hinge with init torsion). A pre-marked "COM" indicator (a thin vertical line at the midpoint) makes the demo visually obvious. Mass ratio 2:1 gives unequal velocities but same COM. Camera: side view.
