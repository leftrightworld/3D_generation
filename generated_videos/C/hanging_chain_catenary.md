#### `hanging_chain_catenary` — Statics / chain
**Physics:** A chain hanging from two pinned endpoints at the same height settles into a CATENARY (cosh) curve, not a parabola — though they look similar for shallow sags.
**Setup:** 40 chain links, each a small capsule (length 0.04 m, radius 0.005 m, M=0.01 kg per link). Links connected by hinge joints with axis y (sag in x-z plane), damping=0.05. Endpoints (link 0 and link 39) are attached to fixed posts via weld constraints at world (-0.5, 0, 1.0) and (+0.5, 0, 1.0). Initial qpos: all hinges = 0 (chain starts as a straight horizontal line stretching between the posts; gravity pulls it down to settle).
**Motion:** Chain dynamically settles under gravity into the catenary shape over ~2-3 s, then stays stable.
**Template:** Programmatic gen (`gen_hanging_catenary.py`). Reuse pattern from `gen_dominoes.py` for chain layout.
**Hints:** Endpoint weld constraints can be done by making link 0 and 39 child bodies of the world post (no joint). Friction off. Render 5 s — first 2 s settle, last 3 s show the catenary shape. Side view, pos (0, -1.8, 0.85), fovy 40.
