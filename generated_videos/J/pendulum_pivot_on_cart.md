#### `pendulum_pivot_on_cart` — Coupled translational/rotational

**Physics:** A pendulum mounted on a freely sliding cart couples rotational and translational degrees of freedom. When the cart is given an impulse, kinetic energy transfers between cart translation and pendulum rotation — the system's COM moves at constant velocity.
**Setup:** Cart (M = 0.5 kg, box 0.15 × 0.05 × 0.03 m) on a frictionless slide joint along x. Pendulum (L = 0.5 m, M = 0.1 kg) hung from the cart's top via a hinge joint (y-axis). init-qvel: cart ẋ = 1.5 m/s, pendulum ω = 0. No friction on slide joint (frictionloss = 0, damping = 0).
**Motion:** render 8 s. Cart slides right, pendulum swings behind it (reaction). Energy oscillates between cart KE and pendulum KE+PE; the cart accelerates and decelerates as the pendulum swings. COM of the whole system drifts at constant vx.
**Template:** `pendulum.xml`. Add a slide joint (axis "1 0 0") to the world-to-cart connection, replacing the fixed mount. Cart body defined as parent of the pivot body.
**Hints:** The cart slide joint must have `frictionloss="0"` and `damping="0"` or energy will not be conserved. The system has 2 DOF: cart x and pendulum angle θ. Total linear momentum is conserved. Camera: wide side view (fovy = 50) to capture cart travel. See gotchas.md §chained_joints.

---
