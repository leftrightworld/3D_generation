#### `kapitza_pendulum` — Parametric stabilization

**Physics:** An inverted pendulum becomes dynamically stable when its pivot is oscillated vertically at high frequency and sufficient amplitude — the Kapitza pendulum effect, where rapid oscillation creates an effective stabilizing potential.
**Setup:** Two side-by-side pendulums (L = 0.5 m, M = 0.1 kg), both inverted (hinge at bottom, rod pointing up). Pendulum A: pivot fixed, initial tilt 3° — falls. Pendulum B: pivot has a slide joint along z driven sinusoidally at A = 0.01 m, f = 20 Hz (ω_drive = 125.7 rad/s >> ω_0 = √(g/L) ≈ 4.4 rad/s) — stands stable. Both start at 3° tilt from vertical.
**Motion:** render 5 s. Pendulum A falls in ~0.5 s. Pendulum B oscillates about the inverted position, stabilized by the rapid pivot motion. Camera: front view.
**Template:** `pendulum.xml` (with gravity flipped for inverted mount, or simply start with rod pointing up from hinge). gen_kapitza.py provides the sinusoidal z-displacement by setting the slide joint qpos each step.
**Hints:** Kapitza stability condition: A·ω_drive > √2 · g·L (approximately). With A = 0.01, ω = 125.7: A·ω = 1.257 m/s. √2·g·L = √2·9.81·0.5 = 6.94 m/s — need to increase A or ω. Use A = 0.02 m, f = 50 Hz: A·ω ≈ 6.28 m/s (closer). Fine-tune in simulation. See gotchas.md §parametric_drive.

---
