#### `billiard_break_setup` — 2D multi-body collision
**Physics:** A cue ball striking a triangular rack of 10 balls — classic 2D elastic scatter. Energy and momentum redistribute over many bodies.
**Setup:** 10 balls in a triangular pack (4-3-2-1 rows) on a frictionless table. Cue ball positioned 0.3 m away, init-qvel toward the front ball at 2 m/s.
**Motion:** Cue ball strikes; 10-ball rack scatters in a characteristic pattern.
**Template:** `elastic_collision.xml` + `n_body_1d_collisions.xml`.
**Hints:** Top-down camera. Stiff contacts. Render 3 s.
