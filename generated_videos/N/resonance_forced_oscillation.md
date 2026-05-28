#### `resonance_forced_oscillation` — Resonance / driven oscillator

**Physics:** A spring-mass oscillator driven at its natural frequency ω₀ = √(k/m) builds amplitude without bound (in the absence of damping). Off-resonance driving at 0.7·ω₀ produces only bounded, small-amplitude oscillation.
**Setup:** Two side-by-side spring-masses: M = 0.1 kg, k = 100 N/m, ω₀ ≈ 31.6 rad/s. Both masses on slide joints along z with stiffness=100. gen_resonance.py injects a periodic impulse (qvel += A·sin(ω_drive·t)·dt each step) at ω_drive = ω₀ for Mass A and ω_drive = 0.7·ω₀ for Mass B. Amplitude A = 0.02 m/s per step, timestep 0.001 s. No damping on either joint.
**Motion:** Render 15 s. Mass A amplitude grows steadily (resonance). Mass B oscillates at small bounded amplitude. Camera: side view, fovy = 45, showing both oscillators.
**Template:** `spring_mass.xml`. Two copies x-separated 0.3 m. gen_resonance.py drives each at its respective frequency.
**Hints:** MuJoCo has no built-in sinusoidal actuator. Implement via gen script that writes qpos/qvel into the model at each step using mujoco.mj_step. Alternatively, attach a driver mass to a long massless rod and give it circular initial conditions — the vertical component acts as a sinusoidal force. See gotchas.md §forced_oscillation.

---
