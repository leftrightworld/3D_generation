#### `triple_pendulum` — Chaos
**Physics:** Adding a third link to the double pendulum increases chaotic sensitivity; the trajectory is wildly path-dependent on initial conditions.
**Setup:** Three rigid arms connected by hinges in series, top pivot fixed. Link lengths 0.30 / 0.25 / 0.20 m, masses 0.15 / 0.12 / 0.10 kg (decreasing as you go down — like double_pendulum). Each hinge has axis y, damping=0.005.
**Motion:** From `init-qpos="1.4, 0, 0"` (top link near horizontal, others vertical), the system rapidly transitions to chaotic flailing where all three links swing wildly.
**Template:** `double_pendulum.xml`. Add a third nested body with the same hinge axis.
**Hints:** Render 8 s — chaos takes a few seconds to fully develop. Camera same as double_pendulum (front view, fovy 38). Damping smaller than double_pendulum so motion lasts longer.
