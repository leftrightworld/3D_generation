#### `capstan_effect` — Friction / wrap
**Physics:** A rope wrapped around a fixed cylinder needs only a small holding force to resist a large pulling force; the ratio scales exponentially with wrap angle: F_pull/F_hold = e^(μθ).
**Setup:** Vertical post on the floor; rope wrapped 1.5 turns around it; one end has a heavy weight (10 kg); the other end has a light weight (0.5 kg, hanging just over the edge).
**Motion:** Despite the huge mass ratio, the rope holds — light weight doesn't get lifted because friction along the wrap absorbs the tension.
**Template:** `atwood.xml` (for tendons + hanging weights) + `dominoes.xml` (post setup).
**Hints:** Use a thin spatial tendon for the rope; friction interaction may be approximate. Could fake the effect with a 2:1 joint equality if direct wrap-friction is too hard. Render 5 s.
