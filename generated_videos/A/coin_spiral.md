#### `coin_spiral` — Rotation / friction
**Physics:** A coin set on its edge and given a small wobble spins down in a spiral, transitioning from tall precession to flat rotation with characteristic increasing pitch. Energy lost to floor friction.
**Setup:** A thin cylinder ("coin") on the floor, given an initial vertical orientation with a small tilt and large initial spin about its vertical axis.
**Motion:** Coin spins on edge, gradually tilts more, and finally settles flat after a few seconds of accelerating-pitch oscillation.
**Template:** `spinning_top.xml`.
**Hints:** Use a freejoint with a carefully tuned initial state including a small tilt and large ω. Camera at 3/4 to capture the spiral motion. Render 6–8 s.
