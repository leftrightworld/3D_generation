#### `wave_on_heavy_rope` — Waves
**Physics:** Wave speed in a vertical hanging rope varies with height: v(h) = sqrt(g·h). A pulse at the top moves faster than at the bottom (heavy lower portion has lower tension).
**Setup:** Vertical chain of small bodies hanging by gravity, top fixed, bottom free.
**Motion:** A pulse displaced at one end propagates downward and speeds up (or vice versa).
**Template:** `dominoes.xml` (chain) + `spring_mass.xml`.
**Hints:** Use ~30 nodes; gravity creates the tension gradient automatically. Initial qpos for the pulse. Render 3 s.
