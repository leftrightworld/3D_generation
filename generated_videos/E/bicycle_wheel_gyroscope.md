#### `bicycle_wheel_gyroscope` — Rotation / precession
**Physics:** A spinning wheel suspended by a string at one end of its axle precesses horizontally rather than falling — gyroscopic stabilization. Precession rate Ω = M·g·L / (I·ω) where L is distance from string to wheel center.
**Setup:** A heavy wheel: cylinder, R=0.10 m, thickness 0.015 m, M=0.5 kg. Mounted on a thin axle (length 0.18 m) sticking through its center. One axle end is connected by a 0.4 m vertical string (tendon) to the ceiling. Initial state: axle horizontal, wheel at world position (0.09, 0, 0.6), and `init-qvel` gives the wheel a spin of ω=60 rad/s about its axle axis.
**Motion:** Wheel doesn't fall; instead, its axle slowly rotates horizontally about the suspension point with Ω ≈ 2-3 rad/s. Render at least one half-revolution.
**Template:** `spinning_top.xml` (for spin physics) + `maxwell_wheel.xml` (for tendon as string).
**Hints:** Use a freejoint on the wheel body. Initial qvel: linear=(0,0,0), angular=(0,ω,0) — see gotcha #10 for world-frame angular qvel. Wheel inertia I_axle = ½MR² = 0.0025. Render 5 s. Camera: side view at the suspension point, pos (1.2, -0.5, 0.7), fovy 38.
