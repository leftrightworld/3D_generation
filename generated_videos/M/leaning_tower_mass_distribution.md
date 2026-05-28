#### `leaning_tower_mass_distribution` — Stability / COM height

**Physics:** A tower tips when its centre of mass projects outside its base; towers with higher COMs require less tilt to reach the tipping threshold. For a uniform tower, tipping angle θ_tip = arctan(w/(2h)); lowering the COM raises the tipping angle (more stable).
**Setup:** Three towers (each 0.10 × 0.10 × 0.5 m total, M = 0.5 kg) on a slow-tilting ramp. Tower A: uniform density, COM at h/2 = 0.25 m, θ_tip = arctan(0.05/0.25) = 11.3°. Tower B: heavy-bottom (COM at 0.10 m height, composite of 0.4 kg at bottom 0.1 m + 0.1 kg at top 0.4 m), θ_tip ≈ 27°. Tower C: heavy-top (COM at 0.40 m), θ_tip ≈ 7.1°. Ramp tilts at ω = 0.3 rad/s.
**Motion:** render 5 s. Ramp tilts gradually. Tower C tips first at ~7.1° (~t = 0.4 s). Tower A tips at ~11.3° (~t = 0.75 s). Tower B tips last at ~27° (~t = 1.5 s). Camera: side view showing all three towers and the ramp.
**Template:** `dominoes.xml` + `tipping_vs_sliding.xml`. Three tower bodies modelled as composite bodies (two box geoms with different densities) to achieve different COM heights. Ramp body with a hinge joint to world and init-qvel or motor.
**Hints:** Ensure tower bases have enough friction to prevent sliding before tipping: μ > tan(θ_tip) for tipping to occur before sliding. For Tower B: μ > tan(27°) = 0.51 — use μ = 0.7 for all. For Tower C: μ > tan(7.1°) = 0.12 — easily satisfied. Set ramp friction accordingly. See gotchas.md §composite_body_com.

---
