#### `galileo_pendulum_peg` — Energy conservation
**Physics:** A pendulum swung from a height rises to the SAME height on the other side, even if a peg in the path shortens the effective length mid-swing.
**Setup:** Pivot at world (0, 0, 1.0); rigid string (length 0.6 m, modelled as a tendon) to a bob (sphere R=0.025 m, M=0.05 kg). Fixed peg at world (0, 0, 0.7). Initial pose: bob pulled back to angle 60° from vertical on the left side.
**Motion:** Bob swings down, string contacts the peg, effective swing length shortens to 0.30 m, bob now swings about the peg, rises to the same height as it started.
**Template:** `pendulum.xml` (basic pendulum) + `cradle_drop_demo.xml`.
**Hints:** Tendon wraps naturally around the peg. Mark the original height with a thin horizontal line for visual proof. Side view, pos (0, -1.5, 0.7), fovy 38. Render 3 s.
