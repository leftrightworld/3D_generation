# beats

## Task description
Two mass-spring oscillators side-by-side with slightly different stiffness — left k₁=30 N/m, right k₂=35.4 N/m, ω ratio ≈ 1.087 (≈8% mismatch). Both bobs are released in phase; over time they drift to anti-phase and back, producing the classic visual beats pattern. Beat period = 2π/|ω₂−ω₁| ≈ 9 s; the full clip (~18 s) shows roughly two beat cycles.

## Physics-engine parameters (MuJoCo)

### Global simulation
- `timestep` = 0.001 s
- `gravity` = (0, 0, -9.81) m/s²
- `integrator` = implicitfast

### Left mass (red)
- Body `mass_L` pos = (-0.525, 0.18, 1.00) m
- Slide joint `slide_L`: axis=(0,0,1), **`stiffness` = 30 N/m**, `damping` = 0.04, `range` = [-0.6, 0.6], `springref` = 0
- Geom: box size 0.08×0.08×0.08, `mass` = 0.4 kg
- ω₁ = √(30/0.4) ≈ 8.66 rad/s, T₁ ≈ 0.725 s

### Right mass (blue)
- Body `mass_R` pos = (+0.525, 0.18, 1.00) m
- Slide joint `slide_R`: axis=(0,0,1), **`stiffness` = 35.4 N/m**, `damping` = 0.04, `range` = [-0.6, 0.6], `springref` = 0
- Geom: box size 0.08×0.08×0.08, `mass` = 0.4 kg
- ω₂ = √(35.4/0.4) ≈ 9.41 rad/s, T₂ ≈ 0.668 s
- Δω ≈ 0.75 → beat period ≈ 8.4 s

### Springs (visual)
- Two `<spatial>` tendons (anchor_L ↔ hook_L, anchor_R ↔ hook_R), width 0.012

### Stands (static)
- Left: two posts at (-0.85, 0.18, 0.85) and (-0.20, 0.18, 0.85), crossbeam at (-0.525, 0.18, 1.74)
- Right: mirrored on +x

### Camera
- `cam` pos = (0, -2.4, 1.10), fovy 42, front view framing both stands
