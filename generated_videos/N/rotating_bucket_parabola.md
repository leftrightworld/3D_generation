#### `rotating_bucket_parabola` — Rotating frame / centrifugal parabola

**Physics:** In a rotating reference frame, the centrifugal pseudopotential adds to gravity to create an effective gravity pointing outward and downward. Small balls in a spinning cylinder settle on a paraboloid z = ω²r²/(2g), the same shape as a rotating liquid surface.
**Setup:** Cylinder (R = 0.12 m, H = 0.18 m) on a vertical hinge with init-qvel ω = 8 rad/s. Cylinder wall as curved geom or ring of box segments. ~60 balls (R = 0.006 m, M = 0.002 kg) with freejoints, initially piled near the center at z = 0.02 m.
**Motion:** Render 8 s. Balls are thrown outward by rotation, climb the cylinder walls, and settle in a paraboloid surface. Camera: 3/4 overhead, fovy = 50.
**Template:** `rotating_fluid.xml`. Replace fluid visualization with ball granular proxy.
**Hints:** Balls need contact with each other and the cylinder wall. friction = 0.3. At ω = 8 rad/s, parabola height at r = 0.10 m: z = 8²×0.1²/(2×9.81) ≈ 0.033 m — a modest but visible curve. See gotchas.md §granular_initial_conditions.

---
