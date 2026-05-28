#### `coupled_gyroscopes_reaction` — Gyroscopic coupling

**Physics:** Two co-spinning gyroscopes on parallel axles exert reaction torques that oppose frame tilting: tilting the shared frame causes both gyros to precess in opposite directions (or the same, depending on spin direction), creating a net reaction moment that resists the tilt.
**Setup:** Rigid frame body (L = 0.3 m bar) connected to world via hinge about x-axis. Gyro disc A (R = 0.05 m, M = 0.2 kg) on a hinge about y at position x = +0.10 m on the frame, init-qvel ω_A = +60 rad/s. Gyro disc B identical, at x = −0.10 m, init-qvel ω_B = +60 rad/s (same spin direction). Frame init-qpos: 20° tilt about x.
**Motion:** render 5 s. From the initial tilted position, both gyros precess and the frame exhibits a characteristic rocking/precessing motion driven by gyroscopic coupling. Camera: 3/4 view showing both discs and frame.
**Template:** `spinning_top.xml` (×2 disc bodies). Frame body with hinge (axis "1 0 0") to world. Each disc body parented to frame with hinge (axis "0 1 0"). High spin-rate init-qvel on each disc's y-hinge.
**Hints:** Both discs spinning in the same direction about y gives net angular momentum along y; tilting the frame about x will cause precession about z (perpendicular). The frame hinge about x must have low damping (0.001) to allow gyroscopic effects to dominate. With opposite spin directions, angular momenta cancel and no gyroscopic effect appears — use same direction for visible effect. See gotchas.md §gyroscopic_coupling.

---
