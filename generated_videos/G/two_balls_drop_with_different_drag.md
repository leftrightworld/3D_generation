#### `two_balls_drop_with_different_drag` — Drag
**Physics:** Two balls of the same mass dropped from the same height — one with low air drag, one with high — fall at different rates.
**Setup:** Two balls (each M=0.05 kg) at world (0, 0, 1.0). Ball A: sphere R=0.02 m. Ball B: larger sphere R=0.06 m (more drag). Both freejoints. Use joint damping (linear) as drag proxy. Drop both.
**Motion:** A reaches the floor first; B reaches later (a couple frames behind).
**Template:** `galileo_dropballs.xml`.
**Hints:** MuJoCo has no native air drag — use linear joint damping on each freejoint to mimic. Side view. Render 1.2 s.
