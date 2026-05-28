#### `swinging_bell_with_clapper` — Multi-body coupling
**Physics:** A bell swinging on a pivot has a clapper inside (a sub-pendulum hung from the bell's interior); the two pendulums have different effective lengths, so the clapper strikes the bell's walls at characteristic intervals.
**Setup:** Bell: outer hollow cup (4 thin walls + closed top, opening down), M=0.5 kg, pivoted at the top with hinge axis y. Inside the bell: a small clapper (sphere R=0.015, M=0.05 kg) on a short string (length 0.10 m) hung from the bell's interior ceiling. Bell pulled to 60° and released.
**Motion:** Bell swings back and forth as a pendulum; clapper swings inside but with its own (shorter) period; clapper periodically strikes the inner bell wall.
**Template:** `pendulum.xml` (basic pendulum) + `double_pendulum.xml` (nested swings).
**Hints:** Bell wall is a few thin box geoms making the hollow cup. Stiff contact between clapper and walls (gotcha #4). Render 5 s. Side view, pos (0, -1.2, 0.5), fovy 40.

---
