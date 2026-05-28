#### `trebuchet_simple` — Projectile / mechanical advantage

**Physics:** A trebuchet converts the gravitational PE of a heavy counterweight into projectile KE via mechanical advantage from an unequal-arm lever; ideal efficiency gives projectile speed v_proj = v_cw × √(M_cw/m_proj) × (L_long/L_short).
**Setup:** Trebuchet arm (total length 0.75 m) pivoted at 0.15 m from the counterweight end. Counterweight: M_cw = 2 kg hanging at the short arm (L_short = 0.15 m). Sling: tendon length L_sling = 0.25 m connecting long arm tip to projectile. Projectile: M_proj = 0.05 kg, R = 0.015 m. init-qpos: counterweight up (arm horizontal, counterweight side high), sling hanging down with projectile resting in a cup.
**Motion:** render 2 s. Counterweight falls, arm rotates, sling whips the projectile upward and releases it (~t = 0.3 s). Projectile follows a high-speed ballistic arc. Camera: side view, wide fovy = 60 to capture full arc.
**Template:** `pendulum.xml` (arm pivot) + `atwood.xml` (counterweight and sling tendon). gen_trebuchet.py assembles the arm body (box geom), counterweight body on a tendon, and sling tendon with projectile. Arm hinge joint (y-axis) to world support frame.
**Hints:** Predicted projectile speed: v ≈ √(2 × M_cw × g × L_short) × L_long/L_short / √m_proj = √(2×2×9.81×0.15) × 0.60/0.15 / √0.05 ≈ √5.886 × 4/0.224 ≈ 105 m/s (unrealistically high for this scale — reduce M_cw to 0.3 kg for v ≈ 13 m/s). The sling release is implemented when the sling attachment angle triggers automatic detach (sling tip exceeds a threshold angle). See gotchas.md §sling_release.

---
