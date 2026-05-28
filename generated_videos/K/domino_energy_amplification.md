#### `domino_energy_amplification` — Chain reaction / energy amplification

**Physics:** In a chain of geometrically scaled dominoes, each falling domino has more potential energy than the one before it; the small initial push is amplified exponentially through the chain, demonstrating multiplicative energy transfer in mechanical cascades.
**Setup:** 12 dominoes with geometric scaling factor 1.5: heights h_i = 0.02 × 1.5^(i−1) m, widths w_i = h_i/5, thicknesses t_i = h_i/10, masses m_i = ρ × h_i × w_i × t_i (density ρ = 1500 kg/m³). Domino 1: h = 0.02 m, m ≈ 0.000024 kg. Domino 12: h ≈ 0.39 m, m ≈ 0.0089 kg. Spacing: domino i placed so domino i (when falling) just reaches domino i+1 top edge.
**Motion:** render 6 s. First domino pushed (init-qvel ω = 2 rad/s). Each subsequent domino topples with more energy. Final domino fall is dramatically larger. Camera: side view, wide angle.
**Template:** `dominoes.xml`. gen_domino_amplify.py computes positions and dimensions for each domino. Each domino is a separate body with box geom, hinge joint to the floor, correct inertial properties.
**Hints:** Spacing formula: d_i = h_i × sin(θ_fall) + t_{i+1}/2 where θ_fall ≈ 60° for typical aspect ratio. Total energy amplification: PE₁₂/PE₁ ≈ (1.5^11)² × m₁₂/m₁ ≈ 83. Domino sizes grow, so camera needs to adjust — use a dolly-zoom effect or very wide fovy = 70. See gotchas.md §domino_spacing.

---
