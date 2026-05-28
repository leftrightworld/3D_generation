#### `snells_law_ball_refraction` — Snell's law analog / momentum at interface

**Physics:** A ball rolling from a low-friction region (fast) into a high-friction region (slow) has its path bent at the interface — analogous to Snell's law. The component of momentum parallel to the boundary is conserved (friction only acts perpendicular to motion), bending the trajectory toward the normal.
**Setup:** Flat frictionless floor divided into two half-planes by a sharp line along z-axis. Left half (x < 0): friction = 0 (fast region). Right half (x > 0): floor friction = 0.6 (slow region, approximated by floor geom segmentation). Ball (R = 0.02 m, M = 0.05 kg, freejoint) starts at (-0.3, 0, 0.02), init-qvel: vx = 1.5 m/s, vy = 0.8 m/s (oblique approach at ~28° to interface normal).
**Motion:** Render 2 s. Ball rolls straight in left region, then bends toward the normal upon entering the right region. Top-down camera, fovy = 50, xyaxes = "1 0 0  0 1 0".
**Template:** `incline_friction.xml`. Two floor geom patches with different friction values.
**Hints:** The analogy is clearest with a perfectly sharp interface and no rolling (use a sliding puck: zero rotational inertia). The "refraction" is approximate — real Snell's law requires wave optics. See gotchas.md §friction_zones.

---
