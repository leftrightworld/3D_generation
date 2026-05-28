#### `two_disks_friction_coupling` — Friction-driven rotation
**Physics:** Two discs in contact at their rims, one spinning — friction between rims drives the other disc to spin (opposite direction). No teeth, just friction.
**Setup:** Disc A (R=0.08 m, M=0.5 kg) on a vertical hinge, spinning at ω=10 rad/s. Disc B (R=0.12 m) on a vertical hinge, initially at rest. The two rims pressed together with some normal force.
**Motion:** A spins; friction transfers torque to B; B starts rotating in opposite direction at scaled speed (R_a/R_b ratio).
**Template:** `gear_train_2_gears.xml` (but without equality — let friction couple them).
**Hints:** Tune normal force and friction to get clean coupling. Render 4 s.
