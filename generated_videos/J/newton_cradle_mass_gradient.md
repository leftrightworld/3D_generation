#### `newton_cradle_mass_gradient` — Momentum / mass mismatch

**Physics:** In a Newton's cradle with non-uniform ball masses, the simple one-in/one-out rule breaks down: the momentum and energy cannot be simultaneously conserved with a clean transfer, resulting in multiple balls moving after impact.
**Setup:** Five balls on strings (string length 0.3 m from pivot) at regulation spacing. Masses left to right: 0.05, 0.08, 0.12, 0.18, 0.25 kg. All same radius R = 0.02 m. Leftmost ball pulled to θ = 40° and released. Contact parameters: stiff (solref = "0.005 1", solimp = "0.99 0.999 0.001").
**Motion:** render 4 s. Leftmost ball strikes the row. Unlike the uniform cradle, the rightmost ball does NOT simply fly off alone — multiple balls on the right end move, with decreasing velocities. On return collisions the pattern continues to break classical expectations.
**Template:** `newton_cradle.xml`. Assign individual `<body ... mass="...">` or `<inertial mass="...">` values to each ball body. Keep geometry (R, string length, pivot spacing) uniform.
**Hints:** The mass gradient makes elastic collision analysis non-trivial. Use very stiff contacts to approximate ideal elastic collisions. Five balls means five equations but only two conservation laws — under-determined, so MuJoCo's contact model determines the actual outcome. Validate: leftmost ball (lightest) should bounce back slightly. See gotchas.md §newton_cradle_contacts.

---
