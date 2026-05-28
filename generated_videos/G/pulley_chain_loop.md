#### `pulley_chain_loop` — Mechanism
**Physics:** Closed chain loop around two pulleys (like a tank tread laid flat). Drive one pulley → loop circulates continuously.
**Setup:** Two pulleys (R=0.05 m) at fixed positions 0.3 m apart. Closed chain (~30 links) wrapped around both. One pulley has initial qvel ω=3 rad/s.
**Motion:** Loop circulates around the two pulleys continuously.
**Template:** `belt_friction.xml` + `dominoes.xml`.
**Hints:** Programmatic gen for the loop. Render 3 s.
