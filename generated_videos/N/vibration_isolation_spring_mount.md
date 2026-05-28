#### `vibration_isolation_spring_mount` — Vibration isolation / transmissibility

**Physics:** A machine (heavy mass) on a spring mount is isolated from floor vibration at frequencies above √2·ω_n. Below resonance, vibration is transmitted fully; at resonance it amplifies; above, it is attenuated (transmissibility < 1).
**Setup:** Floor body (M = 5 kg, slide joint z) given sinusoidal motion via gen_isolation.py at ω_drive = 2·ω_n. Machine (M = 2 kg, box, slide joint z) connected to floor via spring (k = 500 N/m, damping = 0.5). ω_n = √(500/2) ≈ 15.8 rad/s; ω_drive ≈ 31.6 rad/s. Floor amplitude: ±0.02 m.
**Motion:** Render 6 s. Floor oscillates visibly ±2 cm. Machine barely moves (< ±3 mm). Camera: side view showing both floor and machine markers.
**Template:** `spring_mass.xml`. Floor body on a slide joint with gen-driven motion; machine body nested above with spring joint.
**Hints:** At ω_drive = 2·ω_n, transmissibility T = 1/|1 − (ω/ω_n)²| = 1/3 ≈ 0.33 (with light damping). Machine amplitude should be ~1/3 of floor amplitude. Mark the floor and machine with contrasting colored geoms.

---
