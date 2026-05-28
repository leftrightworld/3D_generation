#### `two_objects_on_conveyor_belt` — Friction / belt
**Physics:** Two objects placed on a moving conveyor belt — friction accelerates them up to belt speed; afterwards they move with the belt.
**Setup:** A horizontal belt (rectangular surface) given a constant velocity vx=0.5 m/s. Two boxes placed on the belt with zero initial velocity.
**Motion:** Boxes accelerate due to friction with the belt; reach belt speed; then move with it.
**Template:** `belt_friction.xml` + `incline_friction.xml`.
**Hints:** Belt as a moving plane — give it `init-qvel` and high mass so it doesn't slow. Render 3 s.
