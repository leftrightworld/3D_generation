#### `slider_crank_mechanism` — Mechanism
**Physics:** Converts rotational motion to linear (reciprocating) motion via a crank arm and connecting rod. Used in every IC engine.
**Setup:** A spinning crank (hinge joint with init-qvel); connecting rod attached at one end of the crank; piston (slide joint) attached at the other end of the rod.
**Motion:** Crank spins continuously → piston reciprocates back and forth.
**Template:** `maxwell_wheel.xml`. Custom rod via hinge joints.
**Hints:** Initial qvel on the crank hinge to make it spin; geometric constraints (the rod's length) drive the piston. Render 3 s, several cycles. Side view.
