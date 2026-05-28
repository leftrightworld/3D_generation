#### `hanging_slinky_drop` — Oscillation / dispersion
**Physics:** A slinky hanging from one end has a tension gradient (tight at top, slack at bottom). When released, the top falls but the bottom STAYS in place for about 0.3 s due to wave propagation along the spring — counter-intuitive.
**Setup:** Long discretized slinky (chain of bodies with stiff springs between them) hanging from one end. Release the support at t=0.
**Motion:** Top of slinky falls immediately; bottom remains stationary for several frames; then everything falls together.
**Template:** `dominoes.xml` + `spring_mass.xml`.
**Hints:** Many small bodies (~20+), spring-joints with high stiffness. Initial qpos = gravity-equilibrium positions (heavy upward bias). Render 1.5 s. Side view, fovy small.
