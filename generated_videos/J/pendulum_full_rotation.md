#### `pendulum_full_rotation` — Separatrix / rotation

**Physics:** A pendulum released with kinetic energy just above the separatrix energy E = 2mgL transitions from oscillation to continuous rotation; the separatrix is the unstable fixed point at θ = π (inverted position).
**Setup:** Single pendulum, L = 0.5 m, M = 0.1 kg, pivot fixed. init-qpos: θ = 0 (hanging). init-qvel: ω = 6.3 rad/s (just above ω_sep = √(4gL/L²·L) = √(4 × 9.81 / 0.5) ≈ 8.86 rad/s — recalculate: ω_sep = √(4g/L) = √(4×9.81/0.5) ≈ 8.86 rad/s. For L=0.5, ω_sep ≈ 8.86 rad/s; use ω = 9.0 rad/s to be safely above). No damping.
**Motion:** render 6 s. The pendulum sweeps through the bottom, continues past horizontal, passes through the top (θ = 180°) with non-zero speed, and completes full rotations. Camera: side view capturing the full circle.
**Template:** `pendulum.xml`. Set init-qvel on the hinge joint to 9.0. Ensure joint `range` is not clamped (remove range or set range = "-1e9 1e9"). Set `limited="false"` on the hinge.
**Hints:** Critical: remove joint angle limits or MuJoCo will clamp the rotation. ω_sep = √(4g/L); use ω = 1.015 × ω_sep for a clean rotation with a little headroom. If the pendulum just barely passes the top it will look like it "floats" — which is fine for separatrix illustration. See gotchas.md §joint_limits.

---
