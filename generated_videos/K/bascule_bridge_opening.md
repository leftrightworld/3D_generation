#### `bascule_bridge_opening` — Mechanism / counterweight

**Physics:** A bascule bridge uses a counterweight to reduce the net torque required to lift the roadway; if the counterweight torque exceeds the roadway torque (counterweight side heavy), the bridge opens under gravity without external power.
**Setup:** Single plate (total mass distributed as: counterweight M_cw = 2 kg on the short arm L_cw = 0.2 m from pivot, roadway M_road = 0.5 kg uniformly over L_road = 0.6 m, COM at 0.3 m from pivot). Hinge joint at the pivot (y-axis). init-qpos: 5° from horizontal (nearly flat, counterweight side slightly heavy). No actuator.
**Motion:** render 3 s. The counterweight side falls, the roadway side rises. Bridge swings from near-horizontal to near-vertical. Camera: side view, fovy = 50.
**Template:** `pendulum.xml` (hinge) adapted for an asymmetric plate. Model as a single box body with `<inertial>` specifying the asymmetric COM position (mass = 2.5 kg, COM at x_COM = (M_cw × (−0.2) + M_road × 0.3) / 2.5 from pivot). Alternatively, use two box geoms on either side of the hinge.
**Hints:** The net torque at 5° tilt must be confirmed to cause opening (counterweight torque > roadway torque accounting for cosine factors). Torque_cw = 2 × 9.81 × 0.2 × cos(5°) ≈ 3.91 N·m. Torque_road = 0.5 × 9.81 × 0.3 × cos(5°) ≈ 1.47 N·m. Net torque opens bridge. See gotchas.md §asymmetric_inertia.

---
