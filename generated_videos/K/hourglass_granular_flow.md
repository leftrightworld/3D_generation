#### `hourglass_granular_flow` — Granular flow / constant rate

**Physics:** In an hourglass, granular flow rate through the neck is roughly constant (independent of fill height for h >> neck radius) due to arching dynamics — unlike liquid flow (Torricelli's law) where rate decreases with height.
**Setup:** Two glass chambers (top: box 0.08 × 0.08 × 0.10 m; bottom: box 0.08 × 0.08 × 0.08 m) connected by a narrow neck (cylinder R = 0.006 m, length 0.02 m). Static glass geometry (no joints). 80 balls: R = 0.005 m, M = 0.002 kg, initially packed in the top chamber. Floor of top chamber is a funnel converging to the neck.
**Motion:** render 8 s. Balls flow one by one through the neck at a nearly constant rate. Top chamber empties, bottom chamber fills. Camera: front view with a cross-section cut showing internal flow.
**Template:** `rotating_fluid.xml` (container structure) + `marble.xml` (spherical balls). gen_hourglass.py constructs the glass geometry using box + cylinder geoms. Balls initialized using a grid pattern in the top chamber via gen script.
**Hints:** Neck radius must be > 2.5× ball radius for reliable flow (R_neck = 0.006, R_ball = 0.005 → barely 1.2× — increase to R_neck = 0.015). Ball packing in top chamber: use a grid with slight random jitter to avoid crystalline packing that blocks flow. Enable `solimp` settings that allow slight overlap for high ball counts. See gotchas.md §granular_packing and §neck_flow.

---
