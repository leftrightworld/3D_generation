#### `pendulum_with_air_drag` — Oscillation
**Physics:** Quadratic drag (∝ ω²) decays a pendulum faster at large amplitudes than viscous damping; the envelope curves rather than being a clean exponential.
**Setup:** Same as damped pendulum but with quadratic damping if MuJoCo supports it, otherwise high linear damping that mimics drag.
**Motion:** Initially fast amplitude decay, slowing as amplitude shrinks.
**Template:** `pendulum.xml`.
**Hints:** MuJoCo joint damping is linear in ω. To fake quadratic, use a large linear damping and accept the qualitative behavior. Side-by-side render with `damped_pendulum_decay` would be ideal but each scene is rendered alone.
