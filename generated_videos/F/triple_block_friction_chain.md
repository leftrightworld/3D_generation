#### `triple_block_friction_chain` — Friction
**Physics:** Three stacked blocks on a frictionless floor — push the bottom block. Depending on inter-block μ, all three move together, or top blocks slip behind.
**Setup:** 3 boxes stacked vertically, each on a slide joint along x. Bottom block (M=2 kg) given init-qvel vx=2 m/s. Inter-block friction: μ=0.3 between bottom-middle, μ=0.5 between middle-top.
**Motion:** Bottom accelerates fast; top and middle blocks lag (limited by friction); over a short time they catch up.
**Template:** `incline_friction.xml` + `block_on_block_static_friction.xml`.
**Hints:** Floor friction zero (gotcha #1). Render 2.5 s. Side view, pos (0, -1.0, 0.15), fovy 40.
