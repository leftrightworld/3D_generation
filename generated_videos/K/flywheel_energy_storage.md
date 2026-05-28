#### `flywheel_energy_storage` — Rotational KE / energy transfer

**Physics:** A spinning flywheel stores rotational kinetic energy; when frictionally coupled to a second disc, angular momentum distributes between them according to conservation: ω_final = (I₁ω₁) / (I₁ + I₂).
**Setup:** Flywheel (M = 2 kg, R = 0.15 m, I₁ = ½ × 2 × 0.15² = 0.0225 kg·m², hinge joint y-axis) at x = −0.15 m, init-qvel ω₁ = 40 rad/s. Second disc (M = 0.5 kg, R = 0.10 m, I₂ = 0.0025 kg·m²) at x = +0.10 m, initially ω₂ = 0. At t = 2 s, a friction pad (separate body with high-friction contact) is pressed between the two discs' rim edges — real contact friction couples them.
**Motion:** render 5 s. For t < 2 s: flywheel spins fast, second disc stationary. After t = 2 s: friction coupling — flywheel slows, second disc accelerates. Final: both at ω_f = I₁ω₁/(I₁+I₂) ≈ 36 rad/s. Camera: side view.
**Template:** `maxwell_wheel.xml` (two-disc setup). Add a friction-pad body between the discs' rims, activated at t = 2 s via a slide joint (gen script pushes pad into contact). Pad geom: `friction="1.5 0.01 0.005"`.
**Hints:** The friction coupling is achieved by translating a rubber-pad body into contact with both disc rims simultaneously. Use gen script to set pad slide-joint qpos at t = 2 s. The energy lost to friction heat = ½(I₁I₂/(I₁+I₂)) × (ω₁−ω₂)² ≈ 6.8 J. See gotchas.md §friction_coupling.

---
