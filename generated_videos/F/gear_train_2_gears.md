#### `gear_train_2_gears` — Mechanism
**Physics:** Two meshed gears: angular velocities related by gear ratio (ω_a · R_a = -ω_b · R_b), opposite directions.
**Setup:** Two cylinder gears: A (R=0.06 m) at world (-0.07, 0, 0.1), B (R=0.10 m) at world (0.09, 0, 0.1), each on a hinge about z. Joint equality: `<equality><joint joint1="gear_a" joint2="gear_b" polycoef="0 -0.6 0 0 0"/></equality>` (ratio R_a/R_b=0.6). Gear A initial qvel ω=5 rad/s.
**Motion:** A spins; B counter-rotates at 0.6× A's speed.
**Template:** `maxwell_wheel.xml`.
**Hints:** Top-down, fovy 40. Mark a colored dot on each gear so the speed ratio is visible. Render 3 s.
