#### `cam_follower_simple` — Cam/follower mechanism

**Physics:** A rotating cam converts continuous rotational motion into oscillating translational motion; the follower displacement profile is determined entirely by the cam geometry — an elliptical cam gives a sinusoidal-like stroke.
**Setup:** Elliptical cam (modelled as an ellipsoid geom: a = 0.05 m, b = 0.03 m, along x and z in the cam's local frame) mounted on a hinge joint (y-axis) with init-qvel ω = 3 rad/s. A follower rod (box 0.01 × 0.01 × 0.08 m, M = 0.02 kg) on a slide joint (z-axis) rests on the cam surface under gravity. Cam and follower share a common xz-plane.
**Motion:** render 4 s (= 2 cam revolutions at ω = 3 rad/s). Follower moves up when the long axis of the ellipse comes around, down when the short axis is aligned. Stroke amplitude = a − b = 0.02 m. Camera: front view, fovy = 30.
**Template:** `gear_train_2_gears.xml` (hinge for cam rotation) + `spring_mass.xml` (slide joint for follower). Cam body: ellipsoid geom. Follower body: box geom with slide joint to world (z-axis). Follower rests on cam by gravity (no spring needed).
**Hints:** The follower must stay in contact with the cam — ensure follower mass (0.02 kg) provides enough contact force vs. cam acceleration. If contact is lost at high speed, add a light spring (k = 5 N/m) between follower and ceiling to maintain contact. Cam axle at z = 0.02 m above the floor; follower slide joint centred on same z-axis as cam. See gotchas.md §cam_contact_stability.

---
