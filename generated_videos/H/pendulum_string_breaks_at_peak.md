#### `pendulum_string_breaks_at_peak` — Energy + projectile
**Physics:** A pendulum at the peak of its swing has zero KE (all PE). If the string breaks at that instant, the bob falls straight down. Compare with breaking at the bottom (max KE, flies horizontally).
**Setup:** Pendulum pulled to 60° and released. At a specific time (when the bob reaches peak), the string "breaks" — modelled by setting a tendon limit that fails. The bob becomes a free body.
**Motion:** Bob swings up, string breaks at peak, bob falls straight down from peak (vs would fly horizontally if string broke at bottom).
**Template:** `pendulum.xml`. Add a tendon that fails by setting `range` and `solref`.
**Hints:** "Breaking" is implemented by removing the constraint at the right time. Could use two separate scenes: one with string still intact (for comparison) — but render one with the break. Render 2 s.
