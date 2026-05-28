#### `normal_modes_2mass` — Oscillation
**Physics:** Two masses with three springs (wall–m–m–wall) have two normal modes: symmetric (both move together) at lower frequency, antisymmetric (move oppositely) at higher frequency.
**Setup:** Two masses on a horizontal frictionless track, three springs in series. Initial conditions chosen to excite ONE mode only (e.g., symmetric: both same displacement; antisymmetric: equal but opposite).
**Motion:** Demonstrates pure mode: in symmetric mode the gap between masses stays constant; in antisymmetric mode the gap oscillates twice per cycle.
**Template:** `spring_mass.xml`.
**Hints:** Use tendons as visual springs + slide joints with stiffness for the dynamics. Render two versions (one for each mode) if desired, or just pick antisymmetric (more visually striking). Camera: side view.
