#### `ball_inside_closed_box_bounces` — Multi-bounce containment
**Physics:** A ball inside a closed 5-sided box (open top) bounces off the walls and floor many times; CoR < 1 makes eventually settle.
**Setup:** Cube box (open top), 0.30 m side. Ball (R=0.02, M=0.05 kg) inside, initial qvel (0.5, 0.7, -0.3).
**Motion:** Ball ricochets around the box, eventually losing energy and settling.
**Template:** `bowling.xml` + `elastic_collision.xml`.
**Hints:** Render 4 s. 3/4 camera.
