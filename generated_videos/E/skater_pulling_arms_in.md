#### `skater_pulling_arms_in` — Angular momentum
**Physics:** Conservation of angular momentum — a rotating body retracting mass closer to the axis spins faster (I·ω = const).
**Setup:** A central spinning hub (vertical axis) with two arms extending horizontally. Masses are attached to the arms via slide joints; initially extended. At some point the masses are retracted (via init qpos + spring-loaded sliders) — system spins faster.
**Motion:** System spins at ω₁; arms retract; system now spins at ω₂ > ω₁.
**Template:** `conical_pendulum.xml`.
**Hints:** Tricky to model "retracting" without an actuator. Easiest: start with arms in the extended position, use slide joints with stiffness pulling them toward retracted equilibrium; release and watch them retract under their own spring tension. The conservation effect manifests automatically. Render 4 s.
