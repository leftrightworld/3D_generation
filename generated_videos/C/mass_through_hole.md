#### `mass_through_hole` — Angular momentum
**Physics:** A mass on a string passing through a hole in a frictionless table is pulled inward; as the radius shrinks, the angular velocity grows (L = mvr conserved).
**Setup:** A puck on a frictionless table, attached to a string that passes through a central hole. Below the table, the string's lower end is given a downward velocity (or a hanging mass below pulling it).
**Motion:** Puck spirals inward while spinning faster and faster.
**Template:** `conical_pendulum.xml` + `atwood.xml`.
**Hints:** Tricky to set up — the string going through a hole needs to be modelled as a tendon with a fixed point in space (the hole). Alternative: use a slide joint to model the radius and a hinge joint for the angle. Camera: top-down or 3/4.
