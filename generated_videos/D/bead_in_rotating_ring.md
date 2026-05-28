#### `bead_in_rotating_ring` — Constraint
**Physics:** A bead inside a ring that's spinning about its diameter — bead sits at an angle determined by ω, the centrifugal "potential" creating a non-trivial equilibrium.
**Setup:** A ring on a horizontal axis spinning about its diameter; a bead inside it (constrained to the ring's circular path).
**Motion:** Bead settles at an equilibrium angle on the inside of the ring. Higher ω → more horizontal position.
**Template:** `conical_pendulum.xml` + `marble.xml`.
**Hints:** Ring spins via init-qvel on its hinge. Bead's motion is constrained to the ring (geometric setup). Render 4 s. Side view.
