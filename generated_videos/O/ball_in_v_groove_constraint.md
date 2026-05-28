#### `ball_in_v_groove_constraint` — Constrained rolling / groove guidance

**Physics:** A ball rolling in a V-groove track (two flat rails at 45° forming a V) is constrained to move only along the groove axis. The groove exerts normal forces from both sides simultaneously, providing lateral guidance without kinetic friction along the axis.
**Setup:** Two flat floor geoms angled at ±45° to form a V-groove, oriented along the x-axis, length 1.0 m. Ball (R = 0.025 m, M = 0.05 kg, freejoint). Ball placed in the groove at x = −0.4 m, init-qvel: vx = 0.8 m/s. Groove-ball friction = 0.3 (rolling without slip along x, constrained laterally).
**Motion:** Render 2.5 s. Ball rolls smoothly along the groove, decelerating slightly due to rolling resistance. No lateral drift. Camera: 3/4 front-side view, fovy = 40.
**Template:** `bead_on_helix.xml` (channel guidance concept). gen_v_groove.py places two angled geom strips.
**Hints:** V-groove geometry: two flat geoms each rotated ±45° around x-axis, meeting at the groove bottom. Ball radius 0.025 m, groove half-angle 45° — contact at ~0.018 m from groove centerline on each side. Groove width at ball contact ≈ 0.036 m. See gotchas.md §groove_contact_geometry.

---
