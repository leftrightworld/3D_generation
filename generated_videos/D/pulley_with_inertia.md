#### `pulley_with_inertia` — Constraint / rotational
**Physics:** Atwood machine where the pulley has significant moment of inertia — the pulley's I REDUCES the acceleration: a = (m1-m2)·g / (m1 + m2 + I/r²). Pulley I shows up as effective mass.
**Setup:** Same as Atwood but the pulley is a heavy disc (R=0.10 m, thickness 0.02 m, M=0.5 kg) — NOT massless. Pulley rotates via a hinge joint with no damping. The rope is two tendons (one each side) attached to the pulley via sites at radius R; the rope coupling to the pulley rotation enforces no-slip via joint-equality (combination of slide joints + hinge equality).
**Motion:** Heavier mass descends, lighter ascends — but more slowly than ideal Atwood predicts because of the pulley's I.
**Template:** `atwood.xml` (Atwood structure) + `maxwell_wheel.xml` (rolling-without-slip equality).
**Hints:** Connection: two equalities, one per side, each coupling rope-slide to pulley-hinge. Or simpler: ONE equality between (heavy_slide - light_slide) and (pulley_hinge · R). Mass ratio: 0.6 / 0.4 kg gives clean visible acceleration. Render 3 s. Side view.
