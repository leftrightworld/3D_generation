#### `compound_pendulum_shapes` — Oscillation
**Physics:** Period of a rigid-body pendulum depends on I_pivot, not just mass — three different shapes pivoted at one end swing at different periods even with the same mass.
**Setup:** Three pendulums side-by-side: a thin rod, a flat plate, and a thin triangular plate, all pivoted at their top with hinge joints. Same mass each.
**Motion:** Released from the same angle, the three swing at visibly different periods.
**Template:** `pendulum.xml`. Replicate 3× with different geom types.
**Hints:** Compute I_pivot for each shape (parallel-axis theorem). Use `<inertial>` to override if needed — gotcha #14. Side-view camera, fovy ~40.
