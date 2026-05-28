#### `basketball_tennis_drop` — Collision / energy transfer
**Physics:** Stacked balls dropped together; the bottom one bounces off the floor and immediately collides with the top one, transferring kinetic energy upward. The small top ball can shoot up at ~3× the drop speed.
**Setup:** Two balls stacked vertically (small one on top of big one), released from a height.
**Motion:** Big ball hits floor and rebounds; immediately collides with small ball mid-air; small ball flies up far higher than its drop height.
**Template:** `bowling.xml` + `elastic_collision.xml`.
**Hints:** Use very high contact stiffness (`solref="-200000 -20"`) for both bottom-ball-to-floor AND ball-to-ball contacts. Initial separation between balls: 0.01 m (almost touching). Mass ratio ~10:1 (heavy:light) gives the cleanest effect.
