#### `trifilar_pendulum` — Oscillation
**Physics:** Disc suspended by three equally spaced strings; angular oscillation period is sensitive to the disc's moment of inertia (this is how I is measured experimentally).
**Setup:** Horizontal disc hung from a ceiling triangle by three vertical strings (radius r, length L). Twist the disc slightly about the vertical axis; it oscillates torsionally.
**Motion:** Disc rotates back and forth about its vertical axis with period T = 2π·sqrt(I·L/(m·g·r²)).
**Template:** `pendulum.xml` + `atwood.xml` (for the tendon-as-string idea). Three tendons, one disc, init-qpos a small yaw.
**Hints:** Use a single hinge joint about z for the disc, with NO stiffness. The "restoring" comes purely from the three-string geometry — strings tilt as the disc rotates, giving a gravitational restoring torque. Disc body needs a freejoint or constrained body.
