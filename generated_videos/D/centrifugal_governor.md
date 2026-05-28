#### `centrifugal_governor` — Rotation / equilibrium
**Physics:** Watt's flyball governor: two heavy balls on arms rotate about a vertical axis; at higher RPM, centrifugal effects lift them outward, which (in a real engine) would close a steam valve. Here we just show the equilibrium angle.
**Setup:** Two heavy balls on arms attached to a central spindle by hinge joints (so they can swing outward). Spindle spins about its vertical axis with initial qvel.
**Motion:** Balls swing outward as the system spins; at steady ω, they reach an equilibrium angle determined by ω.
**Template:** `conical_pendulum.xml` (two of them, mirrored).
**Hints:** Damping on the swing hinges so the balls settle. Camera: 3/4 front. Render 4 s.
