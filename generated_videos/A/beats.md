#### `beats` — Oscillation
**Physics:** Two mass-spring oscillators with slightly different frequencies appear to slowly modulate each other's amplitude when started in phase. The envelope frequency is the difference frequency.
**Setup:** Two separate mass-spring systems side-by-side, with k values differing by ~5%. Both released with the same initial displacement.
**Motion:** Both bodies oscillate; their RELATIVE phase drifts. Watched together, the visual "beats" pattern is the slow envelope.
**Template:** `spring_mass.xml`. Replicate 2× with slightly different k.
**Hints:** Need to render long enough for the difference frequency to manifest — beat period = 2π/(ω₁-ω₂). If ω₁=2π, ω₂=2π·0.95, beat period = 2π/0.314 ≈ 20 s. Render 25 s or use larger Δk. Camera: front view showing both side by side.
