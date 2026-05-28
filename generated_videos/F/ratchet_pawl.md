#### `ratchet_pawl` — Mechanism
**Physics:** A toothed wheel + spring-loaded pawl that locks rotation in one direction only. Forward: pawl clicks over teeth. Backward: pawl catches a tooth and locks.
**Setup:** Wheel R=0.10 m with 12 saw-tooth teeth (each tooth: angled box on the rim). Pawl: small lever hinged to a fixed frame, spring-loaded (joint stiffness) so it presses on the rim. Wheel given init-qvel ω in the "allowed" direction (ratchets freely) — for the "blocked" version, give ω in the other direction (immediately locks).
**Motion:** Allowed direction: wheel rotates freely, pawl clicks over teeth. Blocked: wheel rotates ~5° then locks.
**Template:** Programmatic gen `gen_ratchet.py`. Reuse from `gen_dominoes.py` for tooth layout.
**Hints:** Render two variants if desired, or one render that reverses direction at t=1.5 s. Top-down camera. Render 3 s.
