#### `superball_corner_retroreflection` — Elastic collision / retroreflection

**Physics:** A spinning superball thrown at a 90° corner undergoes two sequential surface bounces; each bounce reverses the spin component normal to that surface. The combined effect sends the ball approximately antiparallel to its initial direction.
**Setup:** 90° corner formed by two perpendicular floor/wall geoms. Ball (R = 0.025 m, M = 0.05 kg, freejoint). Contact: high CoR (solref = "−200000 −20", solimp = "0.99 0.999 0.001"), high friction (friction = "1.0 0.1 0.01"). init-qvel: translational (2.0, 0, −1.0) m/s (toward corner) + angular ω_y = −20 rad/s (backspin).
**Motion:** Render 1.5 s. Ball hits floor, bounces sideways into wall, bounces back approximately antiparallel to original direction. Camera: 3/4 view of corner, fovy = 50.
**Template:** `bowling.xml` (floor + walls) + `elastic_collision.xml` (stiff contact settings).
**Hints:** The retroreflection is only approximate — exact retroreflection requires a specific spin magnitude. The key is high friction (spin-to-velocity coupling) and high CoR. Two bounces in quick succession are the visual signature. See gotchas.md §high_restitution_contacts.

---
