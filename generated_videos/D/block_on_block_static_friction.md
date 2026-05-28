#### `block_on_block_static_friction` — Friction
**Physics:** Two stacked blocks on a frictionless floor; pull the bottom block. If μ_static between blocks is high enough, the top block moves WITH the bottom (no slip). If μ exceeded, top stays while bottom slides out.
**Setup:** Bottom block: 0.20 × 0.10 × 0.05 m, M=1 kg, sitting on a frictionless floor, with slide joint along x. Top block: 0.10 × 0.10 × 0.05 m, M=0.2 kg, placed centered on top, also with a slide joint along x. Inter-block contact has μ_static = 0.4. Apply a horizontal initial velocity to the bottom block (vx=1.0 m/s, large enough to slip).
**Motion:** Bottom block slides; top block stays nearly still for a moment, then accelerates due to friction; eventually they share velocity (or stay apart depending on initial velocity).
**Template:** `incline_friction.xml` (stacked geoms) + `elastic_collision.xml` (sliders).
**Hints:** Set floor friction to 0 (gotcha #1). Top block's slide joint allows it to be left behind. Render 2 s. Side view, pos (0, -1.0, 0.15), fovy 40.
