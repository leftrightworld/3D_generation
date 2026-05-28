#### `marble_in_funnel` — Gravity / circular motion
**Physics:** A marble released inside a funnel (cone with vertical axis) spirals down, accelerating as the radius decreases — angular momentum NOT conserved (gravity does work) but visually striking.
**Setup:** Funnel: inverted cone shape, top radius 0.15 m, bottom hole radius 0.01 m, height 0.20 m. Built programmatically from ~24 box segments forming the conical wall. Marble: sphere R=0.008 m, M=0.005 kg, placed at the top edge (R=0.14, z=0.20) with initial tangential velocity vt=0.5 m/s.
**Motion:** Marble spirals down the funnel wall, speeding up as the radius decreases; exits the bottom or oscillates at the throat.
**Template:** Programmatic gen (`gen_funnel.py`). Reuse pattern from `gen_rotating_fluid.py` for ring-of-walls.
**Hints:** Marble friction tuned for low slip on the funnel wall (`friction="0.05 0.005 0.001"`). Camera 3/4 from above, pos (0.25, -0.25, 0.30), fovy 38. Render 4 s.
