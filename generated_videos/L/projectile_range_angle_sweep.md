#### `projectile_range_angle_sweep` — Projectile / optimal angle

**Physics:** For a projectile launched at speed v, range R(θ) = v²sin(2θ)/g — maximum at 45°, with complementary pairs (30° and 60°, 15° and 75°) giving equal range. This scene visualises the full angular sweep simultaneously.
**Setup:** Five balls (R = 0.015 m, M = 0.05 kg each, freejoint) launched from the same point (x = 0, z = 0.015). Launch speed v = 4 m/s. Launch angles: θ = 15°, 30°, 45°, 60°, 75° from horizontal. init-qvel for each: vx = 4cos(θ), vz = 4sin(θ), vy = 0. Floor is a long flat surface (5 m × 0.5 m). No air resistance.
**Motion:** render 2 s. Five balls fan out simultaneously, tracing five parabolic arcs. The 45° ball goes furthest (R = 1.63 m). The 30° and 60° balls land at equal range (R = 1.41 m). The 15° and 75° balls land closer (R = 0.82 m). Camera: side view, fovy = 50, wide enough to show all landing points.
**Template:** `projectile_jenga.xml`. Five freejoint ball bodies with individual init-qvel. Long static floor box (5 × 0.02 × 0.5 m). Side-view camera.
**Hints:** Predicted ranges: R(θ) = v²sin(2θ)/g = 16sin(2θ)/9.81. Confirm numerical results match theory. Separate balls in y by 0.05 m to avoid inter-ball collisions. Use thin markers (small static boxes) at predicted landing spots for educational value. Render time 2 s = slightly more than the longest flight time (t_45 = v sin(45°)/g × 2 = 0.58 s). See gotchas.md §projectile_setup.

---
