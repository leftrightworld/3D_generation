#### `falling_chimney` — Rotational / rigid body
**Physics:** A tall vertical rod pinned at the base falls over by rotating about the base. The TIP accelerates faster than g during part of the fall — counter-intuitive demonstration of how internal stresses redistribute (real chimneys often break mid-fall because of this).
**Setup:** Single rigid rod: a thin box of length 1.0 m, half-extents (0.025, 0.025, 0.5), M=2 kg. Bottom end pinned at world (0, 0, 0) via a hinge joint with axis y, no stiffness. Initial qpos: 2° tilt about y to seed the fall. No damping.
**Motion:** Rod falls over rotating about its base. Tip's vertical velocity exceeds free-fall during the second half of the trajectory (~30° to 60° from vertical).
**Template:** `pendulum.xml` (single rod on hinge).
**Hints:** Compare the tip's z-velocity to g·t to verify the >g effect. Render 1.5 s. Side view, pos (1.5, -1.0, 0.5), fovy 40.
