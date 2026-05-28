#### `block_and_tackle` — Mechanical advantage
**Physics:** A 2:1 pulley system halves the force needed to lift a mass (and doubles the distance). This is Atwood with an extra pulley.
**Setup:** Heavy mass on one end of a rope; rope goes over a fixed pulley, around a movable pulley attached to a lighter mass, and ends fixed to the ceiling.
**Motion:** Heavy mass descends slowly; the light load lifts up (also slowly) because the rope on the movable pulley side bears HALF the tension.
**Template:** `atwood.xml`. Add a second pulley + joint-equality coupling: q_heavy + 2·q_light = 0.
**Hints:** Polycoef "0 -0.5 0 0 0" enforces q_heavy = -0.5·q_light (i.e., 2:1 ratio). Mass ratio matters: heavy ≈ 1.0, light ≈ 0.45 to see clean lifting at moderate damping.
