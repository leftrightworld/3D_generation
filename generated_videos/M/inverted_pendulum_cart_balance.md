#### `inverted_pendulum_cart_balance` — Instability / coupled motion

**Physics:** An inverted pendulum on a free cart is unstable but the cart's reactive motion creates a brief delay in the fall — the cart accelerates in the direction of the falling rod, reducing the effective gravitational torque momentarily before the pendulum inevitably falls.
**Setup:** Cart (M = 1 kg, box 0.20 × 0.05 × 0.05 m) on a slide joint (x-axis, frictionless). Inverted rod (L = 0.5 m, M = 0.3 kg) pinned at the cart top by a hinge (y-axis), pointing upward. init-qpos: rod tilted 3° from vertical (toward +x). init-qvel: zero for both cart and rod. No friction on cart slide joint.
**Motion:** render 2 s. Rod falls toward +x. Cart slides to +x (reaction). Rod falls faster than it would without the free cart — but the reactive cart motion is visible. Compare mentally with a fixed-pivot inverted pendulum: the cart provides a temporary but ultimately futile reactive force. Camera: side view, fovy = 40.
**Template:** `pendulum.xml` (inverted configuration) + `block_on_accelerating_wedge.xml` (sliding cart). The rod hinge at the top of the cart body. Cart body connected to world via slide joint (x-axis). Hinge joint at cart top: rod points up (init-qpos = π for inverted), gravity will pull it to fall.
**Hints:** Inverted pendulum init-qpos: set hinge joint angle = π − 0.0524 rad (≈ 177° from downward vertical = 3° from inverted vertical). Alternatively, use qpos = 0.0524 and flip pendulum geometry (attach point at bottom, rod upward). The fall time from 3° is approximately t_fall ≈ 1/ω × ln(2θ/θ₀) ≈ 0.9 s (where ω = √(g/L)). See gotchas.md §inverted_pendulum.

---
