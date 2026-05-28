#### `bead_on_helix` — Constraint
**Physics:** A bead on a frictionless helical wire descends with combined translation+rotation; ratio of vertical drop to spiral length determines acceleration: a = g·sin(α) where α is the helix pitch angle.
**Setup:** Helix axis vertical (along +z). Generator parameters: radius R=0.06 m, pitch p=0.04 m per turn, 5 turns (total height 0.20 m). Approximate the helix with ~80 short tubular box-segments: at each parameter t ∈ [0, 5·2π], position is `(R·cos(t), R·sin(t), -p·t/(2π))`, segment is a thin box oriented along the local tangent. Bead: sphere R=0.012 m, freejoint, placed just above the top of the helix at world (R, 0, 0.01).
**Motion:** Bead falls onto the helix, slides down spiraling, exits at the bottom after ~3-4 s.
**Template:** Programmatic gen `gen_bead_on_helix.py`. Reuse curve-generation pattern from `gen_brachistochrone.py`.
**Hints:** Make the helix wire from boxes that form a thin "channel" (two parallel walls) so the bead is trapped. Friction off on both bead and helix. Bead radius 0.012 should be much smaller than helix radius 0.06 to fit. Render 4 s. 3/4 view from front-above, pos (0.3, -0.3, 0.15), fovy 38.
