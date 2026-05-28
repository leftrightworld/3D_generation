#### `n_body_1d_collisions` — Multi-body
**Physics:** A line of N balls with elastic collisions and a small initial perturbation evolves to interesting patterns. Edge cases (light vs heavy ratios) show momentum transfer phenomena.
**Setup:** 6–8 balls on a frictionless track, just barely separated. Strike one end with a fast-moving ball.
**Motion:** Series of elastic collisions propagating; with equal masses, the leftmost ball stops and the rightmost moves off. With varying masses, complex transfer patterns.
**Template:** `elastic_collision.xml` + `newton_cradle.xml`.
**Hints:** Stiff contacts, small timestep. Use freejoints on frictionless track. Camera: side view, wide enough for all N balls.

---
