#### `euler_disk_spindown` — Precession / singularity

**Physics:** As a spinning coin loses energy to rolling friction, it paradoxically spins faster while tilting lower — a finite-time singularity where precession frequency diverges just before the coin abruptly stops, explained by Moffatt's rolling-friction theory.
**Setup:** Thin disc (cylinder, R = 0.05 m, thickness = 0.004 m, M = 0.05 kg) on a flat floor. Freejoint. init-qpos: tilt 3° from vertical (Euler angles). init-qvel: spin ω_z = 20 rad/s (about the disc's symmetry axis). Floor friction: `friction="0.3 0.005 0.001"` (rolling friction nonzero).
**Motion:** render 6 s. Disc initially spins steadily with mild precession. Over time, tilt angle increases and precession rate increases dramatically. Near t ≈ 5–6 s, the disc rattles with very fast precession and abruptly stops flat on the floor.
**Template:** `spinning_top.xml` (freejoint body + floor). Replace sphere/cone tip with a flat cylinder. Set freejoint initial conditions via `qpos` (position + quaternion) and `qvel` (linear + angular velocities).
**Hints:** The freejoint qvel order in MuJoCo is [vx, vy, vz, ωx, ωy, ωz]. The disc's spin axis is its local z (symmetry axis). init-qvel should be [0, 0, 0, 0, 0, 20]. Rolling friction `solimp` must allow realistic energy dissipation — use `solref="0.02 1"` and `solimp="0.9 0.95 0.001"`. See gotchas.md §freejoint_init and §rolling_friction.

---
