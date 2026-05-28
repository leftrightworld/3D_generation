#### `ball_on_saddle` — Constraint / instability
**Physics:** A saddle point (z = x² - y²) is stable in one direction, unstable in the other. A ball placed at the saddle rolls off in the unstable direction.
**Setup:** Saddle-shaped surface (z = a·x² - b·y²) with a ball placed exactly at the center.
**Motion:** Ball is stationary briefly, then with a tiny perturbation rolls off in the unstable y-direction while remaining centered in x.
**Template:** `loop_the_loop.xml` (curved geometry).
**Hints:** Approximate the saddle with many small geoms. Slight initial offset in y to seed the instability. Side view.
