#### `spinning_disc_floor_wobble` — Precessing coin / Euler disk

**Physics:** A coin spinning on a flat surface exhibits a characteristic wobble where both the tilt angle and the precession rate increase as energy is dissipated by rolling friction — the precession frequency scales as f ∝ 1/√ε where ε is the tilt angle, diverging in the limit.
**Setup:** Flat disc (cylinder R = 0.05 m, thickness = 0.004 m, M = 0.05 kg, freejoint) on flat floor. init-qpos: disc tilted 20° from vertical (quaternion computed for 20° tilt about x-axis). init-qvel: freejoint velocity [0, 0, 0, 0, 0, 30] (vx=vy=vz=0, ωx=ωy=0, ωz=30 rad/s — spin about disc symmetry axis). Floor friction: `friction="0.25 0.005 0.001"`.
**Motion:** render 6 s. Disc initially wobbles and precesses with a stable cycle. Over time, tilt angle increases and precession rate increases dramatically. Near the end, very fast rattling precession followed by abrupt stop (disc flat on floor).
**Template:** `spinning_top.xml`. Replace the conical/spherical tip with a flat cylinder. Use freejoint. This is distinct from `euler_disk_spindown` (Package J) — here the initial tilt is larger (20° vs 3°) so the early wobble phase is clearly visible and more visually prominent.
**Hints:** The tilt of 20° makes the initial wobble large enough to photograph clearly. Rolling friction coefficient `solref="0.02 1"` with small rolling component (`solimp` third parameter = 0.001) provides realistic energy dissipation timescale. Total simulation time 6 s is sufficient to show the full lifecycle. See gotchas.md §euler_disk.

---
