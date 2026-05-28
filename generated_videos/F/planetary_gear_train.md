#### `planetary_gear_train` — Mechanism
**Physics:** Planetary gear system: sun + 3 planets + ring. Driving the sun makes planets rotate AND orbit; ring stays still. Demonstrates how complex gear ratios arise.
**Setup:** Sun gear: cylinder R=0.04 m at world (0, 0, 0.1) on a hinge. 3 planet gears: cylinders R=0.025 m at world (0.065, 0, 0.1) and 120° rotations, each on a hinge attached to a "planet carrier" body. Ring gear: hollow cylinder, inner R=0.115 m, outer R=0.13 m, fixed to world. Joint-equalities couple sun-to-planet and planet-to-ring as `ω_sun · R_sun = -ω_planet · R_planet` (and similar for ring).
**Motion:** Sun spins (init-qvel ω=4 rad/s); planets rotate AND orbit; ring stays still.
**Template:** `maxwell_wheel.xml` (rolling-without-slip equality).
**Hints:** Use joint equalities, not real gear teeth. Top-down view, pos (0, 0, 0.5), xyaxes="1 0 0  0 1 0", fovy 38. Render 3 s.
