#### `bifilar_pendulum` — Oscillation
**Physics:** Mass suspended by two parallel strings swings, but rotation about the vertical is geometrically blocked. Period depends on string length and lateral separation.
**Setup:** A horizontal rod (or thin plate) hangs from two vertical strings at its two ends. Push it sideways; it swings without rotating.
**Motion:** Rod translates sideways in pure swing; no twisting about its own axis.
**Template:** `pendulum.xml`. Use two tendons instead of one.
**Hints:** Use spatial tendons (`<tendon><spatial>`) for the two strings — see gotcha #2 for placement. Rod needs a freejoint or a slide+slide joint pair; constraints from the two tendons enforce no rotation. Render ~4 s.
