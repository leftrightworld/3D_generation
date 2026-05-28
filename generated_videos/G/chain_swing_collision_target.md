#### `chain_swing_collision_target` — Flexibility + collision
**Physics:** A flexible chain pendulum swung into a target hits with the bottom link's whip-effect velocity — higher than a rigid pendulum of the same length.
**Setup:** Chain (~15 links) pivoted at the top, hanging vertically. Bottom link is a heavier "tip". Pulled to 60° and released. A stationary target block at the chain's lowest point.
**Motion:** Chain whips down, bottom link strikes target with whip velocity, target moves off.
**Template:** `dominoes.xml` + `projectile_jenga.xml`.
**Hints:** Render 2.5 s. Side view.
