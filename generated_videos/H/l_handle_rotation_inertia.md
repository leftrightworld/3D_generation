#### `l_handle_rotation_inertia` — Inertia tensor
**Physics:** An L-shaped rigid body has different moments of inertia about its three principal axes. Spinning about different axes shows visibly different dynamics.
**Setup:** L-shape made of two perpendicular rods (each 0.20 m × 0.02 m × 0.02 m). Freejoint, gravity off. Apply init-qvel: angular velocity along (a) the long arm axis, (b) the short arm axis, (c) the perpendicular axis. Render 3 versions OR one with the intermediate-axis instability.
**Motion:** Spinning about extreme axes: stable rotation. Spinning about intermediate axis: tumbles (similar to Dzhanibekov).
**Template:** `dzhanibekov_effect.xml`.
**Hints:** Use `<option gravity="0 0 0"/>`. Render 4 s.
