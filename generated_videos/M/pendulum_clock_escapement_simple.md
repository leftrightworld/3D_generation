#### `pendulum_clock_escapement_simple` — Mechanism / feedback

**Physics:** The escapement converts continuous rotational energy (from the falling weight) into discrete angular impulses, regulated by the pendulum — each pendulum half-swing allows the ratchet wheel to advance exactly one tooth, creating the characteristic tick-tock rhythm.
**Setup:** Ratchet wheel (12 teeth, R = 0.06 m, M = 0.1 kg, hinge y-axis). Anchor escapement (two-arm lever, hinge y-axis on the same shaft as pendulum, but offset). Pendulum (L = 0.25 m, M = 0.05 kg, hinge y-axis). Driving weight (M = 0.5 kg) on a string (tendon) wrapped around the wheel axle (R_axle = 0.008 m). All in the xz-plane. The anchor alternately locks and unlocks the ratchet wheel with each pendulum swing.
**Motion:** render 5 s (≥ 4 pendulum ticks). Each pendulum half-swing: anchor releases one ratchet tooth, wheel advances 30°, anchor re-engages. Driving weight descends ~3 mm per tick. Camera: front view, fovy = 35.
**Template:** `geneva_drive.xml` (intermittent rotation concept) + `ratchet_pawl.xml` (if exists) + `pendulum.xml`. gen_escapement.py assembles geometry. Key: the anchor-to-wheel contact is the critical interaction — use stiff contacts between anchor pallet faces and ratchet teeth.
**Hints:** Escapement geometry is intricate — the anchor pallet faces must contact the ratchet tooth flanks at the correct angles to deliver an impulse AND lock. Alternatively, implement the escapement using equality constraints that are conditionally activated based on pendulum angle (programmatic approach in gen script). The pendulum period T = 2π√(L/g) = 2π√(0.25/9.81) ≈ 1.0 s. See gotchas.md §escapement_contacts.

---
