#### `spring_gun_launch` — Elastic PE → KE

**Physics:** A compressed spring stores elastic potential energy E = ½kx²; upon release, all stored energy converts to kinetic energy of a launched projectile (minus losses), and maximum height is h = E/(mg).
**Setup:** Spring mechanism: a hinge joint with stiffness k = 5000 N/m acts as the launch spring. Ball (M = 0.05 kg, R = 0.015 m) sits in a cup on the spring arm. init-qpos: spring compressed by x = 0.03 m (stored PE = ½ × 5000 × 0.03² = 2.25 J). At t = 0 the ball is released from the cup (unconstrained). Floor and walls absent to show clean ballistic arc.
**Motion:** render 1.5 s. Spring releases, flinging the ball upward. Ball follows a parabolic arc, reaching maximum height h = 2.25/(0.05×9.81) ≈ 4.6 m (adjust scale so this fits in frame — use k = 200 N/m for h ≈ 0.18 m with x = 0.03 m). Ball rises and falls.
**Template:** `spring_mass.xml`. Use a hinge joint (y-axis) with `stiffness="200"` as the launch mechanism. Ball body connected via an equality constraint (weld) that is disabled at t = 0, or simply use contact-based cup. Render with a moderately high camera.
**Hints:** Predicted max height h = kx²/(2mg) = 200×0.03²/(2×0.05×9.81) = 0.18 m — matches a clean 1.5 s scene. For a visually dramatic launch, use k = 2000 N/m and x = 0.04 m → h ≈ 3.3 m with appropriate camera. Weld equality constraint release: set `active="false"` in gen script at t = 0. See gotchas.md §equality_constraints.

---
