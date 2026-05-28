#### `bead_on_rotating_horizontal_rod` — Centrifugal
**Physics:** A bead on a horizontal rod that's spinning — without anything to provide centripetal force along the rod, the bead slides outward and flies off the end.
**Setup:** Horizontal rod hinged at its center (axis z), spinning at ω=3 rad/s. Bead on a slide joint along the rod (initial offset 0.02 m from center).
**Motion:** Bead slides outward along the rod, accelerating; eventually flies off the end.
**Template:** `bead_on_helix.xml` + `conical_pendulum.xml`.
**Hints:** Rod must be horizontal (gravity normal to it). Render 2.5 s. Top-down camera.
