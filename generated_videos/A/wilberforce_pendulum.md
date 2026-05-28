#### `wilberforce_pendulum` — Oscillation / coupling
**Physics:** Mass hangs on a spring with both longitudinal and torsional stiffness. With matched periods, energy slowly trades between bobbing and twisting.
**Setup:** Cylindrical bob hangs from a long thin coiled "spring" (modelled by a tendon for visual + a custom stiff+damped joint pair). Bob has a slide joint (z) and a hinge joint (about z). Both joints have stiffness and similar periods.
**Motion:** Initially the bob bobs up-and-down; over 5–10 oscillations the bobbing dies and the bob is twisting; then it twists back to bobbing. Beats.
**Template:** `spring_mass.xml` + `spinning_top.xml`.
**Hints:** Tune k_slide and k_torsion so periods match within 5%. Add small initial qvel in slide only; the coupling (which we'd add via a constraint or pre-existing geometry) will transfer energy. If pure-MuJoCo coupling is hard, use a small `<equality>` linking the two joints with a tiny polycoef. Render 15+ s.
