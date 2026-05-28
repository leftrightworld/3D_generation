#### `cone_balanced_on_tip` — Statics / instability
**Physics:** A cone balanced perfectly on its apex is in unstable equilibrium; any infinitesimal perturbation causes it to fall.
**Setup:** Cone shape (build from cylinder + capsule cap or use a cone-shaped geom). Cone height 0.20 m, base radius 0.06 m. M=0.10 kg. Place upside-down with apex on floor at world (0, 0, 0.20). Initial qpos: tiny tilt (~0.5° about y-axis, i.e. quaternion (1, 0, 0.004, 0)). Floor friction `friction="0.8 0.01 0.001"`.
**Motion:** Cone holds steady for ~0.3 s, then starts tilting visibly, falls completely by 1.5-2 s.
**Template:** `spinning_top.xml` (free body + floor) + `dominoes.xml` (tilt seed).
**Hints:** This is just unstable equilibrium — gravity does the rest. Camera: side view, pos (0, -0.6, 0.15), fovy 38. Render 2.5 s.
