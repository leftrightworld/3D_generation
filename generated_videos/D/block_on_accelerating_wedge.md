#### `block_on_accelerating_wedge` — Action-reaction
**Physics:** A block on a frictionless wedge that can itself slide on a frictionless floor — when released, both bodies accelerate. The wedge slides one way as the block slides down it; momentum in x conserved.
**Setup:** Wedge: triangular prism, 30° incline, base 0.40 m × 0.10 m, height 0.20 m at the high end. M_wedge=1.0 kg. Wedge sits on a slide joint along world x. Block: cube 0.05 m, M_block=0.3 kg, sits on the slope of the wedge, constrained to slide on it via slide joint along the slope direction.
**Motion:** Block accelerates down the slope; wedge accelerates in the opposite direction. The combined center of mass stays fixed in x.
**Template:** `incline_friction.xml` (block-on-wedge) + add a slide joint for the wedge.
**Hints:** Set ALL friction to 0 (gotcha #1). Render 1.5 s. Add a vertical marker line at the initial x of the combined COM to make conservation visually obvious. Side view, fovy 38.
