#### `coriolis_turntable_puck` — Rotating frame / Coriolis deflection

**Physics:** A puck launched radially on a frictionless rotating turntable travels in a straight line in the lab frame but traces a curved path in the rotating frame — demonstrating the Coriolis pseudoforce.
**Setup:** Rotating disc (R = 0.25 m, M = 2 kg, thickness 0.01 m) on a fixed vertical hinge with init-qvel ω = 2 rad/s. Puck (R = 0.015 m, M = 0.05 kg) placed on the disc surface at r = 0.05 m from center with init-qvel vr = 0.3 m/s radially outward (in the lab frame). Disc-puck contact: friction = 0. Disc hinge damping = 0.
**Motion:** Render 4 s. Puck slides outward and off the disc edge. Camera: directly top-down, fovy = 60. Marker on puck traces the curved path visible against disc markings (colored sectors painted on disc geom).
**Template:** `rotating_fluid.xml` (spinning disc base). Puck as a sphere with freejoint on the disc surface.
**Hints:** In the lab frame the puck moves in a straight line (no friction). Color the disc with wedge-shaped geoms at different angles to make the rotation visible. Puck traces a curve relative to disc markings. See gotchas.md §rotating_frames.

---
