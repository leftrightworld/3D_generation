#### `leaning_tower_critical_angle` — Equilibrium / tipping
**Physics:** A tower is stable as long as the projection of its COM onto the floor stays inside the base. Tilt it beyond, and it tips.
**Setup:** A tall thin tower (rectangular box, dims 0.10 × 0.10 × 0.6 m) on a slowly-tilting platform. Platform tilts via init-qvel angular rotation.
**Motion:** Tower stays upright while platform tilts; at critical angle (~10° for this geometry), tower tips and falls.
**Template:** `cone_balanced_on_tip.xml` + `tipping_vs_sliding.xml`.
**Hints:** Render 5 s.
