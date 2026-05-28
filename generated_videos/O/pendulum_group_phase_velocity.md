#### `pendulum_group_phase_velocity` — Wave packet / group vs phase velocity

**Physics:** In a dispersive wave medium, the phase velocity (speed of individual oscillation crests) differs from the group velocity (speed of the packet envelope). A Gaussian-modulated wave packet spreads as it travels because different frequency components move at different speeds.
**Setup:** 20 pendulums (lengths 0.28 to 0.42 m in small steps, creating a dispersive medium). init-qpos: q_i = A·exp(−(i−10)²/8)·cos(k₀·i) with A = 0.15 rad, k₀ = π/3 (a localized wave packet centered at pendulum 10). No damping.
**Motion:** Render 20 s. The packet envelope moves at the group velocity while the oscillation crests inside move at the phase velocity. The envelope broadens over time (dispersion). Camera: front view showing all 20 pendulums, fovy = 55.
**Template:** `pendulum_waves.xml`. Modify lengths to vary linearly; modify init-qpos to wave packet.
**Hints:** Group velocity v_g = dω/dk, phase velocity v_p = ω/k. For pendulums with varying length, ω_i = √(g/L_i) — each pendulum has a different natural frequency, creating dispersion. The packet spreading becomes clear by t = 10 s. Render at least 20 s.

---
