#### `swinging_door` — Compound pendulum
**Physics:** A door (rectangular plate) hinged on one edge — its swing period depends on moment of inertia, larger than a point-mass pendulum of equivalent length.
**Setup:** Plate dims 0.8 m × 0.6 m × 0.02 m, M=2 kg. Hinged on one vertical edge (axis z). Initial pose: door open 90°. Damping low.
**Motion:** Door swings closed under gravity, oscillates back-and-forth (large period due to extended I).
**Template:** `pendulum.xml` + `compound_pendulum_shapes.xml`.
**Hints:** Top-down camera (door swings in horizontal plane). Render 5 s.
