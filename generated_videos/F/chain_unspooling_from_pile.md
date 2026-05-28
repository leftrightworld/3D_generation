#### `chain_unspooling_from_pile` — Self-feeding chain
**Physics:** A chain piled on the floor, with one end pulled up — the chain accelerates as more length is lifted (less mass remains stationary). Tension at the pile-junction pulls more chain out.
**Setup:** ~40 chain links initially piled at world (0, 0, 0.05). Topmost link given a small lift (initial qpos at z=0.15, with downward velocity zero).
**Motion:** Pile feeds chain upward and out, accelerating over time.
**Template:** `dominoes.xml`.
**Hints:** Programmatic gen for the initial loose stack. Side view. Render 3-4 s.
