#### `roller_coaster_loop_minimal` — Centripetal / critical speed

**Physics:** Minimum speed to complete a circular loop: v_min at the top = √(gR), where R is the loop radius. A ball released from height h_min = 5R/2 just barely makes it; from h < h_min it falls off before the top.
**Setup:** Two side-by-side tracks: (a) Launch ramp at 30° slope, height H_a = 5R/2 + ramp_start = 0.375 m + small clearance. (b) Same geometry but H_b = 0.25 m (below critical). Both tracks: straight ramp (1.0 m long) → circular loop (R = 0.15 m). Ball: R = 0.020 m, M = 0.050 kg, freejoint. Tracks as box-geom rails (channel tracks).
**Motion:** render 3 s. Ball (a) released from H_a: rolls down ramp, enters loop, completes the full 360° loop, exits. Ball (b) from H_b: enters the loop, slows, and detaches from the track before reaching the top — falls into the interior. Camera: side view, fovy = 45, showing both tracks.
**Template:** `loop_the_loop.xml` + `brachistochrone.xml` (ramp). Two complete track setups side by side (y-offset 0.25 m). Ball freejoint for each. Channel track (two rails) guides balls.
**Hints:** h_min = 5R/2 = 5×0.15/2 = 0.375 m for a point mass. With a rolling ball (solid sphere), the actual h_min = 5R/2 + 2R/5 × R/(R_ball) (rolling correction) ≈ 0.377 m. Ball (b) set to H = 0.25 m gives v_top < 0 (doesn't make it). Track must be a closed channel (not just a flat ramp) for the ball to stay on past the inverted section. See gotchas.md §loop_track_closure.

---
