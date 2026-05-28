#### `chain_lasso_circular` — Rotating chain / steady state

**Physics:** A chain rotating at constant ω forms a circular shape in the horizontal plane — each link is in centripetal force balance where the tension in the inner links provides centripetal acceleration for all the mass further out.
**Setup:** 20-link chain, M = 0.01 kg per link, link length 0.025 m. Link 0 (innermost) connected to a fixed pivot via a hinge joint (z-axis) with motor velocity = 8 rad/s. Links connected by hinge joints with y-axis (allowing in-plane spreading). All joints in the horizontal plane (gravity = "0 0 0" or arrange so chain lies in xy-plane). init-qpos: chain initially straight along x.
**Motion:** render 4 s. From the initial straight configuration, the chain rotates and gradually settles into a circular loop (each link at equal radius from pivot). At steady state, the outer links are at maximum radial displacement due to centripetal tension. Camera: top-down, pos (0, 0, 0.6), fovy = 50.
**Template:** `conical_pendulum.xml` + `dominoes.xml` (chain of bodies). 20 bodies with hinge joints. Innermost hinge to world with velocity motor ω = 8 rad/s. Chain in horizontal plane.
**Hints:** Equilibrium radius: each link at radius r_i is in balance when tension T_i = m × ω² × (sum of r_j for j ≥ i). For uniform chain, the equilibrium shape is approximately circular with total radius R_total = chain_total_length × 2/(π) for half-circle, or chain_length/2π for a full circle. With 20 links × 0.025 m = 0.5 m total, circle circumference ≈ 0.5 m → R ≈ 0.08 m. Use `gravity="0 0 0"` to keep chain in horizontal plane. See gotchas.md §rotating_chain.

---
