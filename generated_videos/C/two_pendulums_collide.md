#### `two_pendulums_collide` — Collision + oscillation
**Physics:** Two pendulums released from opposite sides meet at the bottom and collide elastically; momentum transfer depends on mass ratio.
**Setup:** Two single pendulums side-by-side (small lateral offset so they meet at the bottom). Left: length 0.40 m, mass 0.10 kg, released from 30° (positive angle). Right: length 0.40 m, mass 0.10 kg, released from -30° (negative angle), with a tiny y-offset (0.001) so geoms don't tangle.
**Motion:** Both pendulums swing toward each other; collide at the bottom with equal-mass elastic collision (essentially swap velocities); each bounces back to near-original height.
**Template:** `pendulum.xml` (duplicate) + `elastic_collision.xml` (stiff contact tuning).
**Hints:** Use stiff contact (`solref="-150000 -15"` `solimp="0.99 0.999 0.001"`) for clean elastic transfer (gotcha #4). Render 3 s (two full swings). Side view.
