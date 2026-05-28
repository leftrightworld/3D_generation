#### `epicyclic_compound_reversal` — Compound planetary / direction reversal

**Physics:** In a standard planetary gear train (ring fixed, sun input, carrier output), the carrier rotates in the same direction as the sun. By instead fixing the carrier and using the ring as input, the sun rotates in the OPPOSITE direction to the ring — compound epicyclic direction reversal.
**Setup:** Same geometry as `planetary_gear_train.xml` but with the carrier body fixed to the world and the ring gear body given init-qvel ω = 3 rad/s. Three joint equalities now couple ring-to-planet and planet-to-sun with reversed sign. Sun hinge is free to rotate; carrier hinge is locked (range = "0 0").
**Motion:** Render 3 s. Ring rotates clockwise (top-down). Sun rotates counter-clockwise at ratio ω_sun/ω_ring = −(R_ring/R_sun). Planets spin AND orbit backward. Colored markers on ring and sun show opposite directions clearly.
**Template:** `planetary_gear_train.xml`. Swap which hinge is fixed vs driven. Reverse polycoef signs.
**Hints:** Carrier fixed: add `<joint ... range="0 0"/>` to lock it. Ring input: init-qvel on ring hinge. Joint equality ratio changes sign because the power path reverses. Top-down camera, fovy = 40.

---
