#### `pendulum_wave_decay_pattern` — Coupled waves / damping asymmetry

**Physics:** A pendulum wave machine with heterogeneous damping exhibits asymmetric pattern decay: heavily-damped pendulums on one side lose their oscillations quickly, while lightly-damped ones persist, creating a travelling degradation of the wave pattern.
**Setup:** 15 pendulums (L from 0.28 to 0.42 m tuned for 10 oscillations per pattern period on the right end). Each pendulum on a hinge joint. Damping gradient: pendulums 1–5 (left): `damping="0.5"`, pendulums 6–10 (middle): `damping="0.1"`, pendulums 11–15 (right): `damping="0.01"`. All released simultaneously from 15° amplitude.
**Motion:** render 15 s. Initial wave pattern forms as in `pendulum_waves.xml`. After ~5 s, the left side (heavy damping) pendulums lose amplitude; the pattern degrades from the left, creating an asymmetric visual — the right side still waves while the left side is nearly still.
**Template:** `pendulum_waves.xml`. Apply a damping gradient over the 15 hinge joints. No other changes. Side view or slight 3/4 view to see the wave pattern.
**Hints:** 15 pendulums with lengths tuned for the wave pattern: L_i = g/(2π × f_i)² where f_i varies from f_1 to f_15 to give 9 to 10 oscillations per 15 s pattern period. Heavy damping γ = 0.5 means amplitude halves in ~2 s (e-folding time = 1/γ = 2 s). Light damping γ = 0.01 means amplitude barely changes over 15 s. See gotchas.md §pendulum_wave_tuning.

---
