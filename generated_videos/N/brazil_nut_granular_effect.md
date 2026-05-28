#### `brazil_nut_granular_effect` — Granular segregation / size separation

**Physics:** When a mixture of small and large granular particles is vibrated vertically, the large particles rise to the top — the "Brazil nut effect." Caused by a combination of void-filling (small particles fall into gaps left by large particle) and convection cells.
**Setup:** Cylindrical container (R = 0.065 m, H = 0.18 m). 50 small balls (R = 0.007 m, M = 0.003 kg) and 1 large ball (R = 0.020 m, M = 0.07 kg) initially placed with large ball at the bottom. Container body on a slide joint z, gen_brazil_nut.py injects sinusoidal z-displacement (A = 0.012 m, f = 8 Hz). Friction between balls = 0.4.
**Motion:** Render 10 s. Large ball visibly rises through the small-ball bed, reaching the top by ~8 s. Camera: side view with transparent or cut-away container wall.
**Template:** `rotating_fluid.xml` (container geometry). gen_brazil_nut.py for vertical vibration.
**Hints:** Container wall needs to be thin box geoms (or a mesh cylinder) so the interior is visible. The vibration amplitude A must exceed the ball diameter for effective segregation. This is a computationally heavy scene (~50 contacts per step) — use timestep = 0.001 and nsubsteps accordingly.

---
