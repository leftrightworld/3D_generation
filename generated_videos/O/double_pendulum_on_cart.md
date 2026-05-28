#### `double_pendulum_on_cart` — 3-DOF / coupled chaos on cart

**Physics:** A double pendulum on a freely sliding cart has three coupled degrees of freedom (cart x, θ₁, θ₂). The additional DOF creates richer dynamics than a fixed double pendulum — the cart recoils from pendulum swings, feeding energy back into the chain chaotically.
**Setup:** Cart (M = 0.5 kg, box 0.15×0.05×0.03 m) on a frictionless slide joint along x (damping = 0). Double pendulum mounted on cart: link 1 (L = 0.30 m, M = 0.10 kg) on hinge y at cart top; link 2 (L = 0.30 m, M = 0.10 kg) on hinge y at link 1 bottom. init-qvel: cart vx = 1.5 m/s, both pendulum angles = 0.
**Motion:** Render 8 s. Cart oscillates back and forth as pendulum swings generate reaction forces; pendulum enters chaotic motion within 3–4 s. Camera: wide side view, fovy = 50.
**Template:** `double_pendulum.xml` + `pendulum_pivot_on_cart.xml`. Cart body is parent of pivot body.
**Hints:** Keep cart damping = 0 (frictionless) to preserve total horizontal momentum. The scene is sensitive to initial conditions — cart vx = 1.5 m/s with both angles at 0 gives a clean initial coupled motion that turns chaotic. See gotchas.md §chained_joints.

---
