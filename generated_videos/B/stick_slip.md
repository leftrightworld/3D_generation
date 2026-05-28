#### `stick_slip` — Friction
**Physics:** Block dragged by a spring shows alternating stick-and-slip: builds tension until static friction breaks, then slips forward, then sticks again. Generates characteristic sawtooth motion.
**Setup:** Block on floor with high static friction; attached by a spring to a slowly-moving driver. (Driver moves via init-qvel.)
**Motion:** Block sits still while spring stretches, then suddenly jumps forward; then sits still while spring stretches again; repeats.
**Template:** `incline_friction.xml` + `spring_mass.xml`.
**Hints:** μ_static must be > μ_kinetic — MuJoCo distinguishes these via `friction` and `solimp` settings. Driver needs a sustained low velocity, so give it big mass and high init-qvel so it barely slows over the render. Render 6 s.
