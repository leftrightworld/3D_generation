#### `toggle_clamp_overcenter` — Mechanism / over-center locking

**Physics:** A toggle clamp passes through an over-center configuration where the three pivot points become collinear; at this singularity, the mechanical advantage is infinite and any output force cannot backdrive the mechanism — the basis for vice grips and industrial clamps.
**Setup:** Three-link planar mechanism: input arm (L = 0.10 m, M = 0.05 kg, hinge to world at origin, y-axis), coupler (L = 0.08 m, M = 0.03 kg, hinge between input arm tip and output stub base), output stub (L = 0.03 m, M = 0.02 kg, constrained to slide vertically via slide joint to world). init-qvel on input arm: ω = 1.5 rad/s (drives toward over-center). After over-center, apply a large downward force (F = 50 N) on the output platen via a `<actuator forcerange=...>` or body gravity.
**Motion:** render 4 s. Input arm rotates, passing over-center at ~t = 1 s. Output platen locks. Applied force after locking cannot move the mechanism — it remains locked. Camera: front view.
**Template:** `four_bar_linkage.xml`. Remove the fourth link; add a slide joint constraint for the output stub. Key: the over-center condition is when all three pivots (world hinge, coupler–input junction, coupler–output junction) are collinear.
**Hints:** Over-center condition: input arm angle + coupler angle = 180°. Detect in gen script and stop applying input velocity. For the lock test, add a downward external force as a body-level `<force>` after t = 1 s. Numerical stability near singularity: reduce timestep to 0.0005 around the over-center moment. See gotchas.md §mechanism_singularities.

---
