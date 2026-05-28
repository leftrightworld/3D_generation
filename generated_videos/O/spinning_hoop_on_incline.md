#### `spinning_hoop_on_incline` — Gyroscopic / lateral drift on slope

**Physics:** A hoop spinning rapidly about its own axis (gyroscopically stiff) placed on an inclined surface precesses sideways rather than rolling straight down the slope. The gravitational torque (trying to tip the hoop down the slope) is 90°-redirected by angular momentum into a sideways precession.
**Setup:** Hoop (thin cylinder R = 0.10 m, thickness 0.008 m, M = 0.20 kg) on a 15° inclined floor. Freejoint. init-qvel: spin ω_spin = 30 rad/s about the hoop's own axis (pointing along the slope), plus small downhill component vx = 0.05 m/s to keep contact.
**Motion:** Render 4 s. Hoop rolls slowly sideways across the slope (perpendicular to downhill direction) instead of rolling down. Camera: front view of incline, fovy = 40.
**Template:** `rolling_race.xml` (incline) + `spinning_top.xml` (spin init). Inclined floor at 15°.
**Hints:** Precession rate Ω = M·g·L/(I·ω_spin) where L is horizontal distance from contact point to COM. For the hoop, I ≈ MR². Use high spin ω_spin = 30 rad/s to keep precession slow and visible. Friction must be high enough to prevent slipping (friction = 0.5). See gotchas.md §world_frame_angular_qvel.

---
