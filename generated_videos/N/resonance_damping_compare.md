#### `resonance_damping_compare` — Q factor / damping regimes

**Physics:** Three oscillators with different damping coefficients γ driven at their natural frequency show vastly different steady-state amplitudes. High Q (low damping) → large amplitude; overdamped → barely moves.
**Setup:** Three spring-masses, identical k = 100 N/m, M = 0.1 kg. Joint damping: (a) γ = 0.01 (underdamped, Q ≈ 50), (b) γ = 0.63 (critically damped, Q = 1), (c) γ = 2.0 (overdamped). All three driven at ω₀ via gen_resonance.py as above.
**Motion:** Render 20 s. Oscillator (a) builds large amplitude. (b) barely responds. (c) no oscillation. Camera: side view showing all three.
**Template:** `spring_mass.xml` ×3. Adjust joint damping values.
**Hints:** Q = ω₀·M/γ. For clean demo, run at least 20 s so the high-Q oscillator has time to build up significant amplitude. x-separation 0.3 m between each pair.

---
