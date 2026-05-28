#### `ball_bouncing_corner_2d` — Collision geometry
**Physics:** A ball bouncing into a 90° corner (two perpendicular walls) reflects twice and exits in a direction opposite to incoming (parallel reverse).
**Setup:** Two perpendicular walls forming a corner. A ball with init-qvel into the corner at some angle.
**Motion:** Ball hits one wall, reflects; immediately hits the other wall, reflects again; exits in a direction antiparallel to original.
**Template:** `elastic_collision.xml` + `bowling.xml`.
**Hints:** Stiff contacts. Top-down camera. Render 1 s.
