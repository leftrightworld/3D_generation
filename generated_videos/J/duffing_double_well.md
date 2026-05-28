#### `duffing_double_well` — Nonlinear oscillator / chaos

**Physics:** A Duffing oscillator with two potential wells (W-shaped track) shows qualitatively different behaviour depending on total energy: low-energy trajectories are trapped in one well (quasi-linear), while high-energy trajectories hop between wells (nonlinear chaos territory).
**Setup:** W-shaped curved track: z(x) = a·x⁴ − b·x² with a = 10 m⁻³, b = 1 m⁻¹ (minima at x = ±0.22 m, z_min ≈ −0.025 m, barrier at x = 0, z = 0). Built from ~30 thin box segments approximating the curve, static. Two balls: Ball A (M = 0.1 kg) placed at x = 0.22 m with low init-qvel v = 0.2 m/s (stays in right well); Ball B at x = 0.22 m with v = 1.4 m/s (clears barrier and transitions).
**Motion:** render 6 s. Ball A oscillates back and forth in the right valley. Ball B has enough energy to cross the central barrier and hop between wells, showing the nonlinear dynamics.
**Template:** `brachistochrone.xml` (for curved track segment technique). gen_duffing_track.py generates ~30 box geoms approximating z = 10x⁴ − x² over x ∈ [−0.35, 0.35].
**Hints:** Track segments must be tangentially placed (each segment rotated to match the local slope angle = arctan(dz/dx)). Segment width ~0.015 m. Balls start at x = ±0.22 m. Both balls same y-position but separated in x so they don't collide. See gotchas.md §curved_track_segments.

---
