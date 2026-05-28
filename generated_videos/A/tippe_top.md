#### `tippe_top` — Free rigid body
**Physics:** An asymmetric "top" (rounded bottom + protruding stem) spun fast inverts itself: the stem (initially at the top) ends up touching the floor while the body spins on it. Driven by the contact friction torque combined with the asymmetric inertia tensor.
**Setup:** Two-part body via a single freejoint:
- Lower hemisphere: capsule from (0,0,0) to (0,0,0.04), radius 0.04 m, M=0.06 kg (heavy half-sphere bottom).
- Upper stem: thin capsule from (0,0,0.04) to (0,0,0.08), radius 0.005 m, M=0.002 kg.
Initial position: center of mass at z = 0.035 (hemisphere bottom near floor). Initial qvel = (0,0,0, 0,0, 80) — 80 rad/s about world +z. Floor contact uses `friction="0.4 0.005 0.01"` (high sliding friction, moderate torsional to drive the flip).
**Motion:** First 1-2 s: top spins upright. Then it gradually tilts; eventually inverts and ends up balancing on the stem. Total time to flip: ~4-5 s.
**Template:** `spinning_top.xml` for the rotation setup + `bowling.xml` for floor friction.
**Hints:** This is HARD to tune. Margins: see gotcha #11 for the floor-friction subtlety. Mass distribution between hemisphere and stem is critical — hemisphere too light → no flip; too heavy → never tilts. Render 6 s, may need 5-8 iterations to dial in. Camera: 3/4 low-angle, pos (0.3, -0.3, 0.1), fovy 36.
