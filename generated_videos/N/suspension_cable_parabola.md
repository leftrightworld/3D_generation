#### `suspension_cable_parabola` — Distributed load / parabola vs catenary

**Physics:** A catenary (uniform load per arc length = cable self-weight) hangs as y = cosh(x/a). A suspension bridge cable carrying a uniform horizontal load (deck weight) hangs as a parabola y = x²/(2a). Side-by-side demonstration of both shapes.
**Setup:** Two chains of 40 links each (M = 0.01 kg, length 0.04 m per link), endpoints fixed at (±0.8 m, 0, 1.0 m). Chain A: no extra loads — pure catenary. Chain B: 20 evenly spaced vertical rods hanging from every other link, each rod carrying a hanging mass M_load = 0.03 kg at its bottom (uniform horizontal load distribution).
**Motion:** Render 6 s (settle time ~3 s, then static). Camera: side view, both chains overlaid in the same x-z plane (y-separated by 0.1 m), showing different sag shapes.
**Template:** `hanging_chain_catenary.xml`. Chain B: add sub-bodies with tendons every 2 links.
**Hints:** The parabola chain sags more at the center relative to the endpoints. Overlay a thin static arch (or colored geom) tracing the theoretical parabola for visual comparison. Render 6 s — first 3 s for settling, last 3 s static.

---
