#### `billiard_trick_shot_curve` — Spin / friction-induced curve

**Physics:** A ball rolling with sidespin curves due to friction: the contact friction force has a component perpendicular to the direction of motion, equal to μ_k × N × (ω_z × R / v) — the "Magnus-like" friction curve experienced in billiards as the cue ball develops English.
**Setup:** Cue ball (R = 0.028 m, M = 0.17 kg, freejoint) on a flat table (z = 0). init-qpos: z = R (resting on table). init-qvel: vx = 2.0 m/s (forward), vy = 0, vz = 0, ωx = 0, ωy = 0, ωz = 15 rad/s (sidespin — top view clockwise). Table friction: `friction="0.4 0.01 0.005"`.
**Motion:** render 3 s. Ball rolls forward, gradually curving to the right (for positive ωz). The path is a visibly curved arc, not a straight line. Camera: top-down view, pos (0, 0, 0.8), fovy = 45.
**Template:** `marble.xml` + `incline_friction.xml` (friction model). Freejoint ball on flat floor (extend floor to 2 m × 2 m). The table surface is a static box, no slope.
**Hints:** The curve radius depends on friction: R_curve = v²/(μ × g × ω_z × R / v) ≈ v³/(μ × g × R × ω_z). With the given values: R_curve ≈ 8/0.4/9.81/0.028/15 ≈ 0.49 m — a tight curve. Use `solref="0.02 1"` for the contact. The ball will also experience rolling-without-slip transition (initially sliding, then rolling), which adds complexity. Top-down camera essential for visibility. See gotchas.md §spin_friction_curve.

---
