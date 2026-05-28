#### `rolling_chain` — Rotation
**Physics:** A flexible chain laid flat on the floor can be pulled like a tank tread — the chain "rolls" by having parts continuously transition between contact and free-fall.
**Setup:** Long chain of small linked bodies on the floor; one end is given a horizontal velocity.
**Motion:** The chain moves like a tractor tread, with the leading end being lifted by tension and falling at the rear.
**Template:** `dominoes.xml` (chain layout) + `atwood.xml` (linked bodies).
**Hints:** Probably needs ~30 small links with friction-enabled contact. Render 4–5 s. May need a programmatic generator (`gen_rolling_chain.py`).
