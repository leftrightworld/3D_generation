#### `wheel_with_pendulum_inside` — Coupled rotation/pendulum
**Physics:** A wheel rolling on the floor with a pendulum mounted at its center — wheel acceleration drives pendulum swing; coupled dynamics.
**Setup:** Hollow cylinder (wheel) R=0.15 m rolling on the floor. Inside the wheel: a thin rod (pendulum, length 0.10 m, mass 0.05 kg) pivoted at the wheel's axle, free to swing. Wheel given initial rolling velocity.
**Motion:** Wheel rolls; pendulum swings due to wheel's transient acceleration; over time, pendulum's swing decays.
**Template:** `rolling_race.xml` + `conical_pendulum.xml`.
**Hints:** Hollow wheel via thin ring of geoms. Render 3 s. Side view.
