#### `projectile_max_range_45` — Kinematics
**Physics:** For projectiles launched at the same speed from ground level, the 45° angle maximizes range; angles equidistant from 45° (e.g. 30° and 60°) give equal but shorter ranges.
**Setup:** Three projectiles launched simultaneously at 30°, 45°, 60° from the same point, same initial speed.
**Motion:** All three follow parabolic arcs; the 45° lands furthest; the 30° and 60° land the same distance away but at different times.
**Template:** `projectile_jenga.xml`.
**Hints:** Three freejoint balls with carefully tuned init-qvel (each (v·cos θ, 0, v·sin θ)). Side view camera with wide fovy. Render 1.5 s.
