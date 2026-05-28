#### `spinning_football_stabilized` — Gyrostabilization / prolate body

**Physics:** A prolate body thrown without spin tumbles chaotically (Dzhanibekov instability about the intermediate axis); the same body thrown with a fast spin about its long axis becomes gyroscopically stable and maintains its orientation throughout the flight.
**Setup:** Two prolate ellipsoids (a = 0.11 m semi-major, b = c = 0.035 m semi-minor, M = 0.4 kg, freejoint) in free flight. Same translational launch: vx = 2.0 m/s, vz = 1.0 m/s (giving a parabolic arc over ~0.4 s). Ellipsoid A (no-spin): no rotational init-qvel. Ellipsoid B (spinning): init-qvel includes ωx = 30 rad/s (spin about symmetry axis). Both launched from z = 0.5 m, separated by y = 0.3 m.
**Motion:** render 2 s. Ellipsoid A tumbles chaotically. Ellipsoid B maintains its orientation with the nose pointing consistently along the velocity direction (or at a slight angle). Camera: side view, fovy = 45.
**Template:** `dzhanibekov_effect.xml` (freejoint + gravity). Replace box with ellipsoid geom (`type="ellipsoid" size="0.11 0.035 0.035"`). Include gravity (default). Two separate freejoint bodies.
**Hints:** For the spinning case, the gyroscopic stability condition: ω_spin > ω_tumble × √(I_transverse/I_axial). With ω_spin = 30 rad/s and typical tumble rate ~5 rad/s, this is well satisfied. The Dzhanibekov flip period for the non-spinning case (just translating, no spin) will be purely random/chaotic — add tiny initial angular velocity (ωy = 0.5 rad/s) to seed tumbling for ellipsoid A. See gotchas.md §gyrostabilization.

---
