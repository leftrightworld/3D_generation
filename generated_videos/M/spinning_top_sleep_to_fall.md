#### `spinning_top_sleep_to_fall` — Top lifecycle

**Physics:** A spinning top's "sleeping" state (upright spin axis) is stable only above a critical spin rate ω_crit = 2√(MgℓI_transverse)/I_axial; as friction dissipates the spin, the sleeping state destabilises, nutation grows, and the top eventually falls.
**Setup:** Standard top (M = 0.3 kg, tip at origin, COM at ℓ = 0.03 m above tip, I_axial = 5×10⁻⁴ kg·m², I_transverse = 3×10⁻⁴ kg·m²). Freejoint with ball tip contacting floor. init-qpos: perfectly vertical (no tilt). init-qvel: spin ω = 80 rad/s about symmetry axis. Floor friction: `friction="0.15 0.002 0.001"` (low rolling friction to dissipate spin slowly over 8 s).
**Motion:** render 8 s. Phase 1 (t = 0–4 s): top spins stably upright (sleeping state). Phase 2 (t ≈ 4 s): nutation slowly appears as spin drops below ω_crit. Phase 3 (t = 4–7 s): precession and growing nutation. Phase 4 (t ≈ 7–8 s): rapid tumbling and fall.
**Template:** `spinning_top.xml`. Tune floor friction to give the desired spin-down timescale. ω_crit = 2√(MgℓI_t)/I_a = 2√(0.3×9.81×0.03×3×10⁻⁴)/(5×10⁻⁴) ≈ 25 rad/s.
**Hints:** The key challenge is getting the right friction coefficient so the spin decays from 80 to 25 rad/s in about 4 s. Rolling friction is the main dissipation mechanism for a top (sliding friction at the tip is zero for a perfectly upright top). Start with `friction="0.1 0.003 0.001"` and adjust third parameter (rolling). See gotchas.md §spinning_top_lifecycle.

---
