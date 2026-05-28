#### `chain_whip_crack_tip` — Whip / velocity amplification

**Physics:** In a whip, momentum is conserved as wave energy travels from a heavy base to a lighter tip — with decreasing mass per unit length, the wave speed increases and tip velocity can exceed the initial handle velocity by a factor of ~10.
**Setup:** 20-link chain with decreasing link masses. Link i (i = 1 to 20) has mass m_i = 0.02 × (21 − i) / 20 kg (linear gradient: link 1 = 0.020 kg, link 20 = 0.001 kg). All links: box 0.015 × 0.015 × 0.03 m (length scales with mass for constant density). Links connected by hinge joints (y-axis). Link 1 (base) given init-qvel vx = 3 m/s. All other links initially at rest. No gravity (or include gravity for a more realistic droop effect — include it for realism).
**Motion:** render 1.5 s. The velocity impulse propagates from the heavy base toward the light tip. The tip's speed at impact can be estimated as v_tip ≈ v_base × (m_base/m_tip)^(1/2) ≈ 3 × √20 ≈ 13 m/s. Camera: side view capturing the full chain length.
**Template:** `dominoes.xml` (chain of bodies). gen_whip_chain.py constructs the 20 links with decreasing masses. Hinge joints with low damping. init-qvel on link 0 body only.
**Hints:** Use low joint damping (0.001) to preserve the wave amplification. The velocity amplification formula (impedance mismatch model) gives v_tip/v_base ≈ √(m_1/m_N) for ideal chain — numerical result will be lower due to damping and bending losses. If gravity is included, orient the chain horizontally (along x) with init-qpos so all links start in-line. See gotchas.md §chain_wave_propagation.

---
