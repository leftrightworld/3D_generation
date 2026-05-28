#### `standing_wave_on_string` — Waves
**Physics:** Wave on a fixed-end string forms standing waves at resonance frequencies. The nodes and antinodes are visible.
**Setup:** Long discretized string with one end fixed. The other end is given a small periodic motion via init-qpos (a sinusoidal initial condition matching the lowest mode).
**Motion:** String oscillates with the visible standing-wave pattern.
**Template:** `dominoes.xml` (chain) + `spring_mass.xml`.
**Hints:** Initial qpos = sin(πx/L) gives the fundamental. Run for several periods. Render 3 s. Without actuator, only the freely-oscillating modes are visible.
