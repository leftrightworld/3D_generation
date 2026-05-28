#### `gyroscope_on_string` — Rotation
**Physics:** Same gyroscopic precession as the bicycle wheel demo, but with a thin disc (rather than wheel) emphasizing the rotor character. Different aspect ratio yields different I/I_perpendicular ratio.
**Setup:** Thin heavy disc: cylinder R=0.08 m, thickness 0.005 m, M=0.4 kg, on an axle (length 0.15 m). One axle end connected by a 0.4 m tendon to the ceiling. Disc starts at world (0.075, 0, 0.65), axle horizontal, spinning at ω=80 rad/s.
**Motion:** Disc precesses about the vertical through the suspension point.
**Template:** `bicycle_wheel_gyroscope` (copy after building that one first; this is its sibling).
**Hints:** Thinner disc + higher ω compared to bicycle_wheel scene. Precession rate Ω = Mg·L/(½MR²·ω). Render 5 s. Side view, pos (1.0, -0.4, 0.75), fovy 38.
