#### `ballistic_pendulum` — Collision + oscillation
**Physics:** A "bullet" embeds in a pendulum bob; momentum conservation gives the bob's swing velocity; energy conservation gives the swing height. The combo lets you measure the bullet's speed.
**Setup:** Small fast cube (the bullet) flies horizontally into a heavier cube hanging on a string (the bob). On contact, the bullet sticks (inelastic).
**Motion:** Bullet → impact → bob+bullet swing as one pendulum to a measurable height.
**Template:** `pendulum.xml` + `projectile_jenga.xml`.
**Hints:** Inelastic contact (soft solref) on the bob-bullet pair. Mass ratio matters: bullet/bob ≈ 0.05 gives a visible but modest swing. Camera: side view.
