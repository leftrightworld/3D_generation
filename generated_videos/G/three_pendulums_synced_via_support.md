#### `three_pendulums_synced_via_support` — Synchronization (Huygens)
**Physics:** Three pendulums on a flexible support (the support itself can move) synchronize in phase over time — Huygens-style coupling through the support's small motion.
**Setup:** Horizontal bar (M=0.5 kg) hanging on two strings (the support, which can swing). Three pendulums (each length 0.30 m, M=0.10 kg) hanging from the bar at evenly spaced points. Initial pendulum angles: 30°, 0°, -30° (out of phase).
**Motion:** Bar's small motion couples the pendulums; over many oscillations, they synchronize to all swing in phase.
**Template:** `pendulum_waves.xml` + `coupled_pendulums.xml`.
**Hints:** Bar needs nonzero mass but small relative to pendulums. Render 20 s (sync takes time). Side view.
