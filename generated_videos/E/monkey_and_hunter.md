#### `monkey_and_hunter` — Kinematics
**Physics:** Both projectiles fall the same Δh in the same time. A dart aimed at the monkey's initial position will hit it regardless of dart speed (within ballistic range), provided both are released at the same instant.
**Setup:** A "cannon" (small box) on the floor angled at ~30° toward a "monkey" ball suspended at height 0.8 m, 1 m away. The monkey is held by a "release point" that activates at t=0.
**Motion:** Cannon fires a small ball at angle; monkey simultaneously begins free-fall. They collide in mid-air regardless of initial dart velocity.
**Template:** `projectile_jenga.xml` (strip the tower).
**Hints:** Both are freejoint balls. The "monkey" has zero initial qvel; the dart has angled init-qvel pointing at monkey. Make 2-3 scenes' worth: vary dart speed, all still collide. Camera: x-z side view, fovy 38.
