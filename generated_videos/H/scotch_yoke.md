#### `scotch_yoke` — Mechanism
**Physics:** Converts rotation to sinusoidal (NOT polygonal) linear motion. Different from slider-crank, which gives non-sinusoidal motion.
**Setup:** Rotating crank with a pin (small post offset from center); the pin engages a vertical slot in a "yoke" (a box with a slide joint along x). As the crank rotates, the pin slides along the slot, pushing the yoke horizontally.
**Motion:** Crank rotates uniformly; yoke moves sinusoidally x(t) = R·cos(ωt).
**Template:** `slider_crank_mechanism.xml`.
**Hints:** Slot is a long groove in the yoke; pin slides along it (slide joint between pin and yoke). Render 3 s.
