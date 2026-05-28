#### `rolling_dumbbell` — Rolling / inertia
**Physics:** A dumbbell (two balls on a rod) on a flat floor doesn't roll uniformly — it tumbles end-over-end, alternating between resting on each ball.
**Setup:** Two spheres (R=0.04 m, M=0.1 kg each) connected by a thin rod (length 0.15 m, M=0.02 kg). Free body on the floor; initial qvel includes both translation (vx=0.3) and rotation.
**Motion:** Dumbbell rolls partially, then tumbles end-over-end, then rolls, then tumbles — characteristic gait.
**Template:** `rolling_race.xml`.
**Hints:** Floor friction tuned for rolling. Side view. Render 4 s.
