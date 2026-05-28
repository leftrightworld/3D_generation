#### `variable_length_pendulum` — Energy pumping / parametric

**Physics:** Parametric resonance: shortening a pendulum's effective length at the bottom of each swing (when the bob's KE is maximum) injects energy into the oscillation, causing amplitude to grow each cycle — the classic "pumping a swing" mechanism.
**Setup:** Single pendulum, base pivot fixed. A slide joint at the pivot allows the string length to vary between L_min = 0.3 m and L_max = 0.6 m. String shortens by Δ = 0.15 m each time the bob passes through θ = 0 (bottom), then re-extends at the top. Start: L = 0.6 m, θ = 30°, ω = 0.
**Motion:** render 10 s. Amplitude grows visibly over ~5–7 cycles. The bob swings with increasing arc. After 8–10 cycles the amplitude saturates near the joint limit.
**Template:** `pendulum.xml`. Add a slide joint at the pivot with range [−0.3, 0] (controls Δ-length). gen_variable_length_pendulum.py injects qpos commands for the slide joint each timestep based on sign of angular velocity (bottom of swing detection).
**Hints:** Parametric pumping requires precise timing: shorten at θ ≈ 0, extend at θ ≈ ±θ_max. Implement via `mj_step` callback in gen script. Slide joint stiffness = 0, damping = 0. The mass of the "string" should be negligible. See gotchas.md §programmatic_control.

---
