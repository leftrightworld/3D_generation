#### `chain_vs_rod_pendulum` — Rigid vs flexible pendulum / effective length

**Physics:** A rigid rod pendulum has a well-defined period T = 2π√(2L/3g). A chain pendulum of the same total length behaves differently: its COM is at the same height but its effective pendulum length (related to its I/Md) differs, and the chain's flexibility allows internal modes that shift the apparent period.
**Setup:** Side by side: (a) Rigid rod (single body, length L = 0.50 m, M = 0.20 kg, box 0.02×0.02×0.50 m), hinged at its top — pivot at (−0.3, 0, 1.0). (b) Chain (10 links, each 0.05 m, M = 0.02 kg, capsule), top link hinged at (0.3, 0, 1.0), remaining links via hinge joints (axis y, damping = 0.005). Both released from 30° tilt.
**Motion:** Render 6 s. Rod swings at its period T ≈ 1.16 s. Chain swings at a slightly different effective period; lower links lag behind the upper links visibly, creating a whipping motion. Side view, fovy = 45.
**Template:** `pendulum.xml` (rod) + `swinging_chain_pendulum.xml` (chain).
**Hints:** The chain's lower links lag the upper ones — a visual signature of flexibility. Keep chain hinge damping = 0.005 (very low) so the flexible modes don't die too quickly. Mark the bottom of each to compare oscillation phases.

---
