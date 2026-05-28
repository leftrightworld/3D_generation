#### `yoyo_with_reversal` — Rotation
**Physics:** Like Maxwell wheel but the wheel hits the lower string limit and re-ascends — the string catches and the rotation direction reverses with respect to descent.
**Setup:** Modified Maxwell wheel where the slider joint hits a "stop" at the bottom, causing the equality constraint to allow re-ascent.
**Motion:** Disc descends, rotates, hits bottom, climbs back up while spinning the same way.
**Template:** `maxwell_wheel.xml`. Add a slider range stop at the bottom.
**Hints:** The polycoef equality may bind oddly at the range limit — use stiff `solref` for the slider's range so the bounce is mostly elastic. Render 6–8 s to see one full cycle.
