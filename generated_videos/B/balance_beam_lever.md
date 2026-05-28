#### `balance_beam_lever` — Statics / equilibrium
**Physics:** A lever in static equilibrium: F1·d1 = F2·d2 (torque balance about the fulcrum).
**Setup:** Horizontal rod pinned at center on a fulcrum. Two different weights hanging at different distances from the fulcrum, balanced.
**Motion:** Static initially. Add a small perturbation (a third mass briefly applied), then released — beam returns to equilibrium.
**Template:** `pendulum.xml`. The rod is essentially a pendulum but pinned at center.
**Hints:** The fulcrum is a hinge joint with no stiffness. Two weights attached as nested bodies at different x offsets. Render 3 s.
