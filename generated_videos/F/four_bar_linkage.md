#### `four_bar_linkage` — Mechanism
**Physics:** Four bars in a closed loop (ground + crank + coupler + rocker) — driving the crank in continuous rotation makes the rocker oscillate. Classic mechanism (e.g., oil pump jacks, windshield wipers).
**Setup:** 4 rigid bar bodies joined by 4 hinge joints in a closed quadrilateral. Lengths: ground 0.20, crank 0.05, coupler 0.20, rocker 0.15 (satisfies Grashof condition for full rotation). Ground bar fixed to world; crank driven by init-qvel ω=4 rad/s.
**Motion:** Crank rotates uniformly; rocker swings back and forth; coupler bar's midpoint traces a "coupler curve" (complex closed shape).
**Template:** `slider_crank_mechanism.xml` (similar mechanism with crank).
**Hints:** Use four hinge joints forming a loop — MuJoCo handles closed loops via constraint. Side view. Render 4 s.
