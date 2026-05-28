#### `torsion_pendulum` — Rotational oscillation
**Physics:** A disc suspended by a wire that resists twisting oscillates torsionally; period T = 2π·sqrt(I/κ) where κ is the torsion constant.
**Setup:** Disc R=0.08 m, M=0.15 kg, hung from a single hinge axis pointing up. Hinge has stiffness κ=0.02 N·m/rad, damping=0.005. Initial qpos: disc twisted to 60°.
**Motion:** Disc rotates back-and-forth about the vertical axis, period ~2 s, slowly decaying.
**Template:** `pendulum.xml` (oscillation pattern).
**Hints:** Render 8 s — multiple periods. Top-down camera, fovy 40.
