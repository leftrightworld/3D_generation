#### `anharmonic_pendulum_large_swing` — Oscillation
**Physics:** A pendulum with very large amplitude (~150°) shows period dependence on amplitude — the small-angle approximation breaks. Period at 90° is ~1.18× longer than at 5°.
**Setup:** Single pendulum, init-qpos = 150° (almost vertical-up).
**Motion:** Pendulum oscillates with very large amplitude; period visibly longer than what small-angle predicts.
**Template:** `pendulum.xml`. Just init-qpos = large angle.
**Hints:** Reference: place a second small-amplitude pendulum (5°) side-by-side for visual contrast — but that may be parameter variation in disguise; alternatively, just render one with a long duration to show the period.
