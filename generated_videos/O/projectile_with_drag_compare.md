#### `projectile_with_drag_compare` — Projectile / air resistance effect

**Physics:** Air drag (≈ quadratic in speed for real projectiles, linear approximation here) reduces range and shifts the optimal launch angle below 45°. A dragged ball traces a steeper, shorter arc than a vacuum projectile launched identically.
**Setup:** Two balls at (0, 0, 0.02): Ball A (freejoint, no damping — vacuum). Ball B (freejoint, linear damping d = 0.3 kg/s on x and z translational DOFs — drag proxy). Both launched at 45° with v = 5 m/s: init-qvel = (3.54, 0, 3.54) m/s.
**Motion:** Render 2 s. Ball A traces the longer parabola, lands at x ≈ 2.55 m. Ball B lands at x ≈ 1.9 m (shorter) with a steeper descent. Side view, fovy = 45, pos (1.2, -3, 0.8).
**Template:** `projectile_jenga.xml` (projectile + floor). Two freejoint balls, one with damping.
**Hints:** Linear damping on freejoint translational DOFs: add `<joint name="ball_b_tx" ... damping="0.3"/>` for x and z joints. The drag slows both rise and fall asymmetrically. Mark each ball differently (red/blue) for clear comparison.

---
