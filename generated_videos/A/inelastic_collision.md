#### `inelastic_collision` — Collision
**Physics:** Two bodies stick together after impact; kinetic energy is lost but momentum is conserved.
**Setup:** Two cubes on a frictionless track; one moving toward the other. On contact, they stick (via high-damping contact or an equality constraint that activates).
**Motion:** Moving block hits stationary block, both move off together at half the original velocity (for equal masses).
**Template:** `elastic_collision.xml`.
**Hints:** Disable elastic contact: set `solref` and `solimp` to soft values so the impact dissipates. Or use a tendon equality that snaps in on contact (advanced). Camera: same as elastic_collision.
