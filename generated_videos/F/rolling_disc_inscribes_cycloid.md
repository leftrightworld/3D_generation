#### `rolling_disc_inscribes_cycloid` — Trajectory geometry
**Physics:** A point on the rim of a rolling disc traces a cycloid in space — the curve that originally motivated cycloid mathematics.
**Setup:** Disc R=0.10 m, thickness 0.02 m, M=0.5 kg, rolling on the floor (init-qvel: vx=0.6, ω_y=-6 for rolling-without-slip). A small bright marker (sphere R=0.005 m) welded to the disc at one point on the rim.
**Motion:** Disc rolls; marker traces high arches (cycloid), touching the ground at intervals.
**Template:** `rolling_race.xml` + `maxwell_wheel.xml`.
**Hints:** Side view, pos (1.5, -2.0, 0.3), fovy 38. Render 4 s — 2-3 cycloid arches.
