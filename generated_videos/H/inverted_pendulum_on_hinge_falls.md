#### `inverted_pendulum_on_hinge_falls` — Instability
**Physics:** An inverted rigid rod pinned at the base, with no support, falls due to instability. Different from `falling_chimney` (which has more pinning detail) and `cone_balanced_on_tip` (which is a free body, not pinned).
**Setup:** Rod (length 0.5 m, M=0.5 kg) pinned at base with a hinge (axis y, no stiffness). Initial pose: vertical (no perturbation), with init-qvel tiny angular velocity (0.05 rad/s) to seed the fall.
**Motion:** Rod falls over, pivot at base.
**Template:** `falling_chimney.xml`.
**Hints:** Render 2 s. Side view.
