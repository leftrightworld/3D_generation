#### `melde_harmonic_3modes` — String harmonics / standing wave modes

**Physics:** A discretized string (both ends fixed) initialized in the shape of its nth harmonic mode oscillates in a pure standing wave. The 1st mode has one antinode (λ = 2L), 2nd has two antinodes (λ = L), 3rd has three (λ = 2L/3). All at different frequencies.
**Setup:** Three discretized strings side by side (x-separation 0.25 m), each 40 nodes, total length L = 0.50 m, both ends fixed (world weld). Each node M = 0.005 kg on slide joint z, stiffness k = 200 N/m between neighbors. init-qpos: z_i = A·sin(n·π·i/39) for n = 1, 2, 3 respectively. A = 0.025 m. Damping = 0 on all joints.
**Motion:** Render 4 s. Each string oscillates cleanly in its mode shape. Camera: front view, fovy = 50, all three strings visible.
**Template:** `standing_wave_on_string.xml`. Three copies with different init-qpos.
**Hints:** Node spacing must be small enough to resolve the 3rd harmonic — 40 nodes easily resolves 3 antinodes. Period of mode n: T_n = 2L/(n·v) where v = √(k·L_seg/M). Ensure natural frequency matches actual MuJoCo frequency with chosen k.

---
