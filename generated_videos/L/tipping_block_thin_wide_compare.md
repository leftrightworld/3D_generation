#### `tipping_block_thin_wide_compare` — Statics / tipping criterion

**Physics:** A block tips if its centre of mass projects outside its base before the block slides; tip-vs-slide depends on aspect ratio: wide blocks slide (low COM projection overhang needed), tall blocks tip (high torque, easy COM overhang). Critical angle for tipping: θ_tip = arctan(w/(2h)).
**Setup:** Three blocks of equal mass M = 0.5 kg on a ramp, static friction μ = 0.3 for all. Block A (wide): 0.20 × 0.04 × 0.08 m (w × d × h), θ_tip = arctan(0.10/0.04) = 68° — much more than θ_slide = arctan(0.3) = 17°: slides. Block B (square base): 0.08 × 0.04 × 0.08 m, θ_tip = arctan(0.04/0.04) = 45° > 17°: marginal but slides first. Block C (tall): 0.04 × 0.04 × 0.20 m, θ_tip = arctan(0.02/0.10) = 11° < 17°: tips before sliding.
**Motion:** render 3 s. Ramp init-qvel tilts at 3 rad/s. Block C tips first (~t ≈ 0.7 s). Block A slides from the start. Camera: side view showing all three blocks.
**Template:** `incline_friction.xml` + `tipping_vs_sliding.xml`. Three block bodies on a hinge-joint ramp. Individual block dimensions and inertial properties. Same μ = 0.3 floor friction.
**Hints:** Recalculate θ_tip for each block: arctan(half-base-width / half-height). Ensure block dimensions give clearly distinct outcomes. The ramp tilt rate 3 rad/s = reaching 17° in ~0.1 s (very fast) — reduce to 0.5 rad/s for a clearer visual. Check: a ramp hinge joint with init-qvel OR use a motor actuator ramping angle. See gotchas.md §tipping_vs_sliding.

---
