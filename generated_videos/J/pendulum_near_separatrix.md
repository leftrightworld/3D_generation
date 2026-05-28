#### `pendulum_near_separatrix` — Phase space / critical energy

**Physics:** A pendulum given initial speed just below the separatrix energy asymptotes toward the inverted position (θ = π), slowing to near-zero speed at the top — a trajectory that theoretically takes infinite time to reach the unstable equilibrium point.
**Setup:** Single pendulum L = 0.5 m, M = 0.1 kg. init-qpos: θ = 0 (hanging). init-qvel: ω = 4.40 rad/s (99% of separatrix speed ω_sep = √(4g/L) = √(4×9.81/0.5) ≈ 8.86 rad/s — wait, recheck: ω_sep from energy: ½Iω² = 2mgL → ω² = 4mgL/I = 4mg·L/(mL²) = 4g/L → ω_sep = 2√(g/L) = 2√(9.81/0.5) ≈ 8.86 rad/s. Use ω = 0.99 × 8.86 = 8.77 rad/s). No damping.
**Motion:** render 12 s. Pendulum swings up quickly, then decelerates dramatically near θ = 180°, hanging near the top for several seconds before slowly swinging back down. Camera: side view, wide enough to show full arc.
**Template:** `pendulum.xml`. Set init-qvel = 8.77 on the hinge. Remove joint limits. Use `integrator="RK4"` for accurate near-separatrix integration.
**Hints:** At 99% separatrix energy the bob reaches θ ≈ 178° and hangs there for ~8–10 s (numerical precision determines exact hover time). Use RK4 with timestep = 0.0005 for accuracy. The scene illustrates phase-space concepts: the separatrix separates libration from rotation orbits. See gotchas.md §separatrix_integration.

---
