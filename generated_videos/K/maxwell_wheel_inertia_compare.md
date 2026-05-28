#### `maxwell_wheel_inertia_compare` — Rotational inertia / descent

**Physics:** For a Maxwell wheel (yo-yo descending on a string), angular acceleration α = g / (1 + I/(mR²)) — wheels with higher moment of inertia I descend slower. Three wheels with identical mass but different mass distributions illustrate the effect of I on acceleration.
**Setup:** Three Maxwell wheels side by side (x = −0.3, 0, +0.3 m), all M = 0.2 kg, axle R = 0.01 m, string length 0.4 m. (a) Hoop/rim-mass: I = mR_rim² with R_rim = 0.08 m → I ≈ 0.00128 kg·m². (b) Solid disc: I = ½mR² with R = 0.08 m → I ≈ 0.00064 kg·m². (c) Centre-mass (all mass at axle): I ≈ m·R_axle² → I ≈ 0.00002 kg·m². Strings attached to ceiling.
**Motion:** render 4 s. All three released simultaneously. Rim-mass wheel (a) descends slowest. Solid disc (b) intermediate. Centre-mass (c) descends fastest, almost in free fall.
**Template:** `maxwell_wheel.xml` (×3). Override `<inertial diaginertia="...">` for each wheel to set the desired I values. Ensure string (tendon) length and attachment points are identical for all three.
**Hints:** Use `<inertial mass="0.2" diaginertia="I I I">` override. Stagger x-positions. Predicted descent times: use energy conservation — (c) descends in t ≈ √(2h/g) ≈ 0.29 s, (a) in t ≈ √(2h(1 + I_a/(mR²))/g). Camera: front view. See gotchas.md §inertia_override.

---
