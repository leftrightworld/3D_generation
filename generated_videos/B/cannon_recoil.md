#### `cannon_recoil` — Momentum
**Physics:** Cannon on wheels firing a projectile experiences recoil; final momenta sum to zero (cannon backward, ball forward).
**Setup:** Heavy cannon (box on wheels — slide joint horizontal) holding a smaller projectile. At t=0, the projectile is given a strong forward velocity; the cannon must accordingly receive backward momentum.
**Motion:** Projectile shoots forward; cannon visibly rolls backward.
**Template:** `marble.xml` (for cart on wheels) + `projectile_jenga.xml`.
**Hints:** Use a freejoint for both bodies but connect them with a "spring" or "rod" until t=0 (then somehow release). Simpler: just give both bodies opposite initial qvel, scaled by inverse mass. Render 2.5 s.
