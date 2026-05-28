#### `rigid_body_3axis_stability` — Intermediate-axis theorem / all three axes

**Physics:** Euler's intermediate-axis theorem (Dzhanibekov effect): rotation about the major (longest) and minor (shortest) principal axes is stable; rotation about the intermediate axis is unstable — any perturbation causes the body to flip periodically.
**Setup:** Zero gravity (gravity = "0 0 0"). Three identical box bodies (0.30 × 0.15 × 0.05 m, M = 0.3 kg) at x = −0.4, 0, +0.4 m. Box (a) at x = −0.4: init-qvel ωx = 5 rad/s (longest axis — stable). Box (b) at x = 0: init-qvel ωy = 5 rad/s (intermediate axis — UNSTABLE, will flip). Box (c) at x = +0.4: init-qvel ωz = 5 rad/s (shortest axis — stable). All bodies with freejoint.
**Motion:** render 5 s. Box (a) and (c) spin cleanly about their respective axes. Box (b) initially spins, then begins to flip (~t = 1–2 s), and flips repeatedly. Camera: 3/4 isometric view showing all three boxes simultaneously.
**Template:** `dzhanibekov_effect.xml`. This extends the existing scene by showing all three axes simultaneously. Three bodies with freejoint, gravity off. Principal moments: I_x = m(y²+z²)/12 = 0.3×(0.0225+0.0025)/12 = 0.000625, I_y = m(x²+z²)/12 = 0.3×(0.09+0.0025)/12 = 0.002313, I_z = m(x²+y²)/12 = 0.3×(0.09+0.0225)/12 = 0.002813 kg·m².
**Hints:** Intermediate axis is y (intermediate I_y). Box (b) must be given a tiny perturbation off the pure y-axis (e.g., ωx = 0.01 rad/s) to seed the instability and trigger the flip within the 5 s render. Without perturbation, numerical noise will eventually trigger it but timing is unpredictable. See gotchas.md §dzhanibekov.

---
