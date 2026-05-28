#### `rolling_cone` — Rotation
**Physics:** A cone rolling on its side traces a circular path centered on its apex (precession of the rolling axis).
**Setup:** A cone (apex on the floor) rolls in a circular path. Use a thin cone geom or build from segments.
**Motion:** Cone rolls around its apex, completing a circle in proportion to its half-angle.
**Template:** `rolling_race.xml`.
**Hints:** Body needs a freejoint + rolling-without-slip via friction. Initial spin matters: give it angular velocity so it starts rolling, not skidding. fovy ~38, top-down 3/4 camera. Render 4–6 s.
