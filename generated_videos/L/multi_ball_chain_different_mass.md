#### `multi_ball_chain_different_mass` — Momentum / mass gradient collision

**Physics:** Newton's cradle with non-uniform masses violates the simple elastic transfer rule; the momentum wave couples into multiple outgoing velocities determined by the full N-body elastic collision equations, showing mass mismatch effects on momentum transport.
**Setup:** Five hanging balls with masses 0.05, 0.10, 0.15, 0.20, 0.25 kg left to right (all R = 0.020 m, uniform geometry). A 6th ball (M = 0.05 kg, same geometry) swings in from the left at v = 2 m/s (init-qvel on its hinge). All balls suspended on strings (length 0.25 m) from a common ceiling bar, spacing 0.042 m (just touching at rest).
**Motion:** render 3 s. Incoming light ball (6th) strikes the left end of the chain. Unlike a uniform cradle, the momentum wave does not cleanly transfer to the rightmost ball — multiple balls on the right end move with different velocities. Observe which ball(s) emerge fastest.
**Template:** `newton_cradle.xml` + `elastic_collision.xml`. Six ball bodies on hinge-joint strings. Individual mass values. Stiff contact parameters. Side view.
**Hints:** Theoretical prediction for elastic collision of mass m₁ striking stationary m₂: v₂' = 2m₁v₁/(m₁+m₂) — but in a chain it's more complex. The lightest incoming ball (0.05 kg) hitting the 0.05 kg ball should initially have near-elastic transfer to that ball. Increasing masses to the right will show progressive slowing of the momentum wave. See gotchas.md §mass_gradient_cradle.

---
