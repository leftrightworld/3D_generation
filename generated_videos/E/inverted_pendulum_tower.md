#### `inverted_pendulum_tower` — Stability
**Physics:** A tower of inverted pendulums (each hinged on the one below) is unstable — any small perturbation grows.
**Setup:** Stack of N inverted pendulums (link-on-link, each a hinge with stiffness but high amplitude). Small initial tilt.
**Motion:** Tower wobbles initially, then collapses in some direction.
**Template:** `beam_buckling.xml`.
**Hints:** Set hinge stiffness so it's below the buckling-stability threshold. Render 3–4 s.
