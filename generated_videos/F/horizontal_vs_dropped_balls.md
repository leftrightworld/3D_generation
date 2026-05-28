#### `horizontal_vs_dropped_balls` — Independence of motion
**Physics:** Horizontal motion is independent of vertical free fall: two balls dropped from the same height — one pushed horizontally, one not — hit the ground simultaneously.
**Setup:** Two balls at world (0, 0, 1.0), each sphere R=0.025 m, M=0.05 kg, with freejoints. Ball A: init-qvel zero. Ball B: init-qvel "1.5 0 0 0 0 0" (horizontal kick).
**Motion:** Ball A falls straight down; Ball B traces a parabola landing 1m+ to the side. Both touch the floor at the same instant (t = √(2·1.0/9.81) ≈ 0.45 s).
**Template:** `galileo_dropballs.xml`.
**Hints:** Side view, pos (0.7, -1.5, 0.5), fovy 38 — frame both initial position AND ball B's landing point. Render 0.6 s.
