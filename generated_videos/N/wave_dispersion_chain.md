#### `wave_dispersion_chain` — Dispersion relation / frequency-dependent speed

**Physics:** In a uniform spring chain (linear dispersion at low frequency, but nonlinear at high k), a Gaussian pulse travels without spreading. In a chain with alternating spring constants k₁/k₂, the dispersion relation has a bandgap — the pulse spreads and slows as high-frequency components travel at different speeds.
**Setup:** Two 40-body chains side by side (x-separation 0.3 m). Chain A: uniform k = 500 N/m between all links, damping = 0. Chain B: alternating k₁ = 200 N/m, k₂ = 800 N/m. All bodies M = 0.01 kg on slide joints z. Both chains receive the same initial Gaussian displacement pulse: z_i = 0.02·exp(-(i-5)²/2) for i = 0..39, others at z = 0.
**Motion:** Render 3 s. Chain A pulse travels cleanly. Chain B pulse spreads into multiple components that travel at different speeds. Side view, both chains visible.
**Template:** `wave_reflection_fixed.xml` (discretized chain). gen_dispersion_chain.py for alternating k setup.
**Hints:** Alternating masses also create dispersion (acoustic vs optical branches). Use alternating k (simpler) rather than alternating mass. Timestep 0.0005 for stability.

---
