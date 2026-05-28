#### `vertical_loop_insufficient_speed` — Energy / centripetal
**Physics:** A ball on a vertical loop track needs minimum speed `v_min = sqrt(g·R)` at the top to maintain contact. With less, it falls off the track partway up.
**Setup:** Closed vertical loop track (radius 0.20 m) — same geometry as `loop_the_loop.xml`. Ball: sphere R=0.025 m, M=0.05 kg. Initial position at the bottom of the loop; initial qvel = small (vx=1.5 m/s — too slow to make it around).
**Motion:** Ball ascends the loop on the inside surface; somewhere past 90° (when gravity component exceeds centripetal requirement), the ball loses contact with the track and falls inward.
**Template:** `loop_the_loop.xml`. Reduce initial speed.
**Hints:** Compare to `loop_the_loop` which uses enough speed. Render 1.5 s. Same camera as loop_the_loop.
