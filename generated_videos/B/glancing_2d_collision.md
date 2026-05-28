#### `glancing_2d_collision` — Collision
**Physics:** Equal-mass elastic collision at an angle: the two balls fly off at 90° to each other. Their final velocity vectors form a right angle.
**Setup:** Two pucks on a frictionless table; one moving, the other stationary, with a small lateral offset so the impact is glancing (not head-on).
**Motion:** Moving puck strikes glancingly; both pucks scatter at angles that sum to 90°.
**Template:** `elastic_collision.xml`. Switch to 2D (top-down camera).
**Hints:** Pucks on a slide-x and slide-y joint pair (no rotation). High contact stiffness, zero friction between pucks and floor. Top-down camera. Render 2 s.
