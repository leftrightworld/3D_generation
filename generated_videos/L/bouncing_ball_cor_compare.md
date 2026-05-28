#### `bouncing_ball_cor_compare` — Coefficient of restitution comparison

**Physics:** The coefficient of restitution (CoR) determines what fraction of pre-collision normal velocity is retained after each bounce: h_n = CoR^(2n) × h_0. Different materials exhibit CoR from ~0.3 (clay) to ~0.95 (super ball).
**Setup:** Three identical balls (R = 0.03 m, M = 0.1 kg) dropped from z = 1.0 m, side by side at x = −0.3, 0, +0.3 m. Ball A (CoR ≈ 0.9): solref = "0.02 1", solimp = "0.99 0.999 0.001". Ball B (CoR ≈ 0.6): solref = "0.02 1", solimp = "0.80 0.90 0.001". Ball C (CoR ≈ 0.3): solref = "0.02 1", solimp = "0.50 0.60 0.001". Flat static floor.
**Motion:** render 5 s. All three balls dropped simultaneously. Ball A bounces high (h₁ ≈ 0.81 m), Ball B medium (h₁ ≈ 0.36 m), Ball C barely bounces (h₁ ≈ 0.09 m). After 5 s, A is still bouncing, C is nearly stationary.
**Template:** `coefficient_of_restitution.xml` (if present) or `bowling.xml`. Three ball bodies with individual geom-level solimp/solref. Verify CoR by measuring bounce heights in sim.
**Hints:** MuJoCo's `solimp` controls the effective CoR indirectly through the contact impedance model. Calibrate: drop a test ball and measure v_after/v_before from consecutive bounce heights. Typical tuning: solimp `d0` parameter near 0.99 gives near-elastic; near 0.5 gives highly inelastic. Stagger x by 0.3 m to prevent inter-ball interaction. See gotchas.md §coefficient_of_restitution_tuning.

---
