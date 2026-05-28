#### `damped_pendulum_decay` — Oscillation
**Physics:** A pendulum with viscous damping shows exponential decay of amplitude: θ(t) = θ₀·e^(-γt)·cos(ωt). Period is nearly unchanged for light damping.
**Setup:** Single pendulum with a moderate joint damping value.
**Motion:** ~8–10 visible swings, each successively smaller; eventually settles to rest.
**Template:** `pendulum.xml`. Add `damping="0.05"` to the hinge.
**Hints:** Pick damping so the envelope decay is visible within 8 s (try 0.04). Camera: same as `pendulum.xml`. Grid PNG should show monotonically decreasing amplitude.
