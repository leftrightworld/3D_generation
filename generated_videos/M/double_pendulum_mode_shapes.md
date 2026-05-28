#### `double_pendulum_mode_shapes` — Normal modes / eigenfrequencies

**Physics:** A linearised double pendulum has two normal modes: symmetric (both links swing in phase at ω₋ — lower frequency) and antisymmetric (links out of phase at ω₊ — higher frequency); pure mode initial conditions give periodic (non-chaotic) motion.
**Setup:** Double pendulum: L₁ = L₂ = 0.3 m, M₁ = M₂ = 0.1 kg. Normal mode frequencies (equal masses and lengths): ω₋ = √(g(2−√2)/L) = √(9.81×0.586/0.3) ≈ 4.38 rad/s; ω₊ = √(g(2+√2)/L) ≈ 11.55 rad/s. Two side-by-side renderings: (a) Symmetric: θ₁ = θ₂ = 20°, angular velocities from eigenmode. (b) Antisymmetric: θ₁ = 20°, θ₂ = −20°. Both small-angle to validate linear modes.
**Motion:** render 5 s. (a) both links swing together at ω₋ — slower, synchronized. (b) links swing against each other at ω₊ — faster, opposing. Camera: front view, wide enough to see both pendulums side by side.
**Template:** `double_pendulum.xml`. Two copies side by side (x-offset 0.4 m). Set init-qpos for each copy to the respective mode shape (θ₁, θ₂ pairs). Use small angles (20°) to stay in linear regime.
**Hints:** Symmetric mode period T₋ = 2π/ω₋ ≈ 1.43 s. Antisymmetric mode period T₊ = 2π/ω₊ ≈ 0.54 s. In a 5 s render: symmetric completes ~3.5 cycles, antisymmetric ~9 cycles. The ratio of periods (2.6:1) is visually striking. Keep angles small (≤ 20°) to maintain pure mode shape. Use `integrator="RK4"` for accuracy. See gotchas.md §normal_modes.

---
