#### `double_pendulum_chaos_compare` — Chaos / butterfly effect

**Physics:** Two double pendulums with initial conditions differing by only ε = 0.01° exhibit exponential divergence of trajectories — a hallmark of deterministic chaos and sensitive dependence on initial conditions.
**Setup:** Two identical double pendulums (each link L = 0.3 m, M = 0.1 kg) placed side by side in the xz-plane, x-separated by 0.4 m. Both start from θ₁ = 60°, θ₂ = 0°; the second pendulum's θ₁ is offset by +0.01° = 0.000175 rad. No damping.
**Motion:** render 8 s. For the first 2–3 s the two pendulums swing nearly identically. Around t ≈ 3–5 s the trajectories visibly diverge; by t = 8 s the two bobs are completely out of phase. Camera: front view, fovy = 45, pos (0, -1.2, 0.0).
**Template:** `double_pendulum.xml`. Duplicate the entire double-pendulum body tree, offset by x = 0.4 m. Adjust init-qpos for the second copy's first joint by +0.000175 rad.
**Hints:** Use `integrator="RK4"` and `timestep="0.001"` for accurate long-horizon integration. Keep gravity at default (9.81). Both pendulums must share the same world body but have completely independent joint trees. See gotchas.md §chaos — do NOT use `euler` integrator here; RK4 is required or divergence will be numerical artefact not physical chaos.

---
