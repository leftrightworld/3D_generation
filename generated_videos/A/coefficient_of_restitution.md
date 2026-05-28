#### `coefficient_of_restitution` — Collision
**Physics:** A ball bouncing on a floor loses a fixed fraction of energy per bounce. Successive bounce heights follow h_n = h_0 · e^(2n), giving geometric decay.
**Setup:** Single ball dropped from a height onto a hard floor, with contact `solref/solimp` tuned for partially elastic collision.
**Motion:** Ball bounces with decreasing height; the envelope shows geometric decay over 5–8 bounces.
**Template:** `bowling.xml` (for floor + ball pattern).
**Hints:** Use `solref="-100000 -8" solimp="0.98 0.999 0.001"` for ~85% restitution. Camera: side view, frame from 0 to drop height. Render 4–5 s.
