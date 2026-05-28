#### `dzhanibekov_effect` — Free rigid body / intermediate axis
**Physics:** A free rigid body with three distinct principal moments of inertia, spun about its intermediate axis, periodically flips by 180°. The other two axes are stable; only the intermediate is unstable.
**Setup:** A T-handle or similar asymmetric body in zero gravity, with init-qvel about the intermediate principal axis (with a small perturbation to make the instability manifest).
**Motion:** Body spins about one axis for ~1 s, then suddenly flips by 180°, then spins for another ~1 s, then flips again. Periodic.
**Template:** `spinning_top.xml`. Set `gravity="0 0 0"`.
**Hints:** Use `<option gravity="0 0 0"/>`. Freejoint body. Mass distribution: T-handle (long arm + short cross-piece). Initial qvel slightly off the intermediate axis to seed the instability. Render 4–5 s.
