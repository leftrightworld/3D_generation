#### `bucket_of_water_overhead_swing` — Vertical circular motion
**Physics:** A bucket swung in a vertical circle keeps its contents inside even at the top (upside-down moment) as long as centripetal acceleration > g.
**Setup:** Pivot at world (0, 0, 1.0). Rigid rod (length 0.5 m, NOT a tendon — tendon would go slack at top) ending in a "bucket" (an open-top 5-sided box, 0.10 × 0.10 × 0.10 m). Inside the bucket: a free ball (R=0.025 m, M=0.05 kg). Arm initial qvel: ω=4 rad/s.
**Motion:** Bucket sweeps a full vertical circle (or two). Ball stays inside even when upside-down at the top.
**Template:** `pendulum.xml` + `conical_pendulum.xml`.
**Hints:** Arm must be RIGID (use a rigid hinge-connected body, not tendon). Ball free inside the cup. Render 3 s (1 full circle).
