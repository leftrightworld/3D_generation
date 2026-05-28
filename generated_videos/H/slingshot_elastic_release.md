#### `slingshot_elastic_release` — Energy storage/release
**Physics:** A pre-stretched elastic band (spring) releases stored elastic PE into a ball's kinetic energy — slingshot effect.
**Setup:** Two posts with a horizontal "rubber band" (tendon with stiffness, modelled as a spring). Ball placed against the band, band stretched back by initial qpos. At t=0, the ball is unconstrained; band snaps forward, launching the ball.
**Motion:** Ball flies forward at high velocity; arcs through the air.
**Template:** `spring_mass.xml` + `projectile_jenga.xml`.
**Hints:** Tune spring stiffness for visible launch. Side view. Render 1.5 s.
