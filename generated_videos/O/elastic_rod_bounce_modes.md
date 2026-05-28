#### `elastic_rod_bounce_modes` — Flexible body / impact mode excitation

**Physics:** A flexible rod dropped horizontally onto the floor excites multiple bending modes simultaneously on impact. The rod bounces in complex S-curves and wavy shapes, unlike a rigid rod which bounces uniformly.
**Setup:** 20 rigid links (each L = 0.05 m, M = 0.01 kg, capsule R = 0.006 m) connected by hinge joints (axis y) with stiffness k = 2000 N/m and damping = 0.01. Initial configuration: all hinges at 0 (rod horizontal), centered at world (0, 0, 0.25). All links given init-qvel vz = −1.5 m/s (fall toward floor).
**Motion:** Render 2.5 s. Rod falls, center hits floor first, bends around the contact, bounces back with complex S-shape oscillations. Side view, fovy = 40.
**Template:** `dominoes.xml` (chain) + `hanging_slinky_drop.xml` (release). No gravity compensation — all links released simultaneously.
**Hints:** stiffness = 2000 N/m ensures the rod feels "stiff but not rigid" on impact. The center hits first (slightly due to contact geometry), exciting the odd bending modes (1st, 3rd). Timestep = 0.0005 for stability. nsubsteps = 4.

---
